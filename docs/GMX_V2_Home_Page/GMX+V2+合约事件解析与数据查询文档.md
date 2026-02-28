# GMX V2 合约事件解析与数据查询文档

<div class="Section1">

# 目录

- [概览](#%E6%A6%82%E8%A7%88)

- [架构设计](#%E6%9E%B6%E6%9E%84%E8%AE%BE%E8%AE%A1)

- [GM Pool (Market) 模块](#gm-pool-market-%E6%A8%A1%E5%9D%97)

- [GLV Pool 模块](#glv-pool-%E6%A8%A1%E5%9D%97)

- [Order 订单模块](#order-%E8%AE%A2%E5%8D%95%E6%A8%A1%E5%9D%97)

- [Position 仓位模块](#position-%E4%BB%93%E4%BD%8D%E6%A8%A1%E5%9D%97)

- [Trades 交易历史模块](#trades-%E4%BA%A4%E6%98%93%E5%8E%86%E5%8F%B2%E6%A8%A1%E5%9D%97)

- [事件字段映射表](#%E4%BA%8B%E4%BB%B6%E5%AD%97%E6%AE%B5%E6%98%A0%E5%B0%84%E8%A1%A8)

- [查询接口文档](#%E6%9F%A5%E8%AF%A2%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3)

- [数据精度说明](#%E6%95%B0%E6%8D%AE%E7%B2%BE%E5%BA%A6%E8%AF%B4%E6%98%8E)

- [常见问题](#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)

------------------------------------------------------------------------

## 概览

### 系统职责

本系统负责监听 BNB Chain 上 GMX V2 Synthetics 协议的链上事件，解析事件数据并持久化到 PostgreSQL 数据库，同时提供 HTTP API 供前端查询。

### 核心功能模块

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | 功能 | 事件来源 |
| **GM Pool** | GM 市场池管理（流动性提供） | `MarketCreated`, `MarketUpdated` |
| **GLV Pool** | GLV 全局流动性池管理 | `GlvPoolCreated`, `GlvPoolUpdated` |
| **Order** | 订单生命周期管理 | `OrderCreated`, `OrderExecuted`, `OrderCancelled`, `OrderUpdated`, `OrderFrozen` |
| **Position** | 仓位状态管理 | `PositionIncrease`, `PositionDecrease` |
| **Trades** | 交易历史记录 | 基于 Position 事件生成 |

</div>

### 数据流向

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
BNB Chain Events (EventEmitter)
    ↓
Block Scanner (事件监听)
    ↓
Event Handlers (事件解析器)
    ↓
Service Layer (业务逻辑)
    ↓
DAL (数据访问层)
    ↓
PostgreSQL (数据持久化)
    ↓
HTTP API (对外查询接口)
```

</div>

</div>

------------------------------------------------------------------------

## 架构设计

### 事件处理流程

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 1. 事件监听
BlockScannerService -> 扫描区块 -> 提取 EventEmitter 日志

// 2. 事件路由
EventRegistry -> 根据 EventName 路由到对应 Handler

// 3. 事件解析
Handler.Handle() -> 使用 EventDataAccessor 提取字段

// 4. 业务逻辑
Service.HandleXXX() -> 计算派生字段、状态转换

// 5. 数据持久化
DAL.Create/Update() -> 保存到数据库分区表
```

</div>

</div>

### 关键组件

#### EventDataAccessor

GMX V2 使用 EventEmitter 合约发出通用事件，事件数据存储为 key-value 结构：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// EventData 结构
type EventData struct {
    AddressItems  map[string]common.Address
    UintItems     map[string]*big.Int
    IntItems      map[string]*big.Int
    BoolItems     map[string]bool
    Bytes32Items  map[string][32]byte
    // ...
}

// 访问方式
accessor := event.NewEventDataAccessor(eventData)
account, ok := accessor.Address(consts.BscEventKeyAccount)
sizeUsd, ok := accessor.Uint(consts.BscEventKeySizeDeltaUsd)
```

</div>

</div>

所有事件字段的 key 常量定义在 `data-statistics-infra/consts/bsc_event_key.go`。

#### 表分区策略

所有用户相关数据表使用 **128 分区** 策略，基于 `account` 地址的哈希值：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 计算分区号
partitionId = HexAddrMod(account, 128)

// 生成表名
tableName = fmt.Sprintf("bsc_perp_order_%d", partitionId)
// 示例: bsc_perp_order_42, bsc_perp_position_0, bsc_perp_trades_127
```

</div>

</div>

适用表：

- `bsc_perp_order_{0..127}`

- `bsc_perp_position_{0..127}`

- `bsc_perp_trades_{0..127}`

------------------------------------------------------------------------

## GM Pool (Market) 模块

### 功能说明

GM Pool 是 GMX V2 的流动性市场池，每个市场对应一个交易对（如 BTC/USD, ETH/USD）。

### 事件解析

#### MarketCreated

**触发时机**: 新市场创建时

**关键字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
type MarketCreatedEvent struct {
    Market      common.Address  // GM 市场合约地址（Pool Address）
    IndexToken  common.Address  // 标的资产（如 WBTC）
    LongToken   common.Address  // 多头抵押代币（如 WBTC）
    ShortToken  common.Address  // 空头抵押代币（如 USDC）
    MarketToken common.Address  // GM LP Token 地址
}
```

</div>

</div>

**字段映射**:

<div class="table-wrap">

|               |                |             |                        |
|---------------|----------------|-------------|------------------------|
| 事件字段      | 数据库字段     | 类型        | 说明                   |
| `market`      | `pool_address` | varchar(66) | 市场地址，也是唯一标识 |
| `indexToken`  | `index_token`  | varchar(66) | 标的资产地址           |
| `longToken`   | `long_token`   | varchar(66) | 多头抵押代币           |
| `shortToken`  | `short_token`  | varchar(66) | 空头抵押代币           |
| `marketToken` | `market_token` | varchar(66) | GM LP Token            |

</div>

**处理逻辑**:

1.  从 `MarketCreated` 事件提取基本信息

2.  调用 Reader 合约的 `GetMarketInfo()` 获取完整市场数据

3.  保存到 `bsc_gm_pools` 表

#### MarketUpdated

**触发时机**: 市场状态变化时（不常见，通常用于启用/禁用市场）

**处理逻辑**:

- 更新 `is_disabled` 字段

- 刷新市场的实时数据快照

### 数据库模型

**表名**: `bsc_gm_pools` (无分区)

**核心字段分组**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 基础信息
symbol              VARCHAR(50)      -- 显示符号 (如 BTC/USD)
pool_address        VARCHAR(66)      -- 市场地址（唯一键）
market_token        VARCHAR(66)      -- GM LP Token
index_token         VARCHAR(66)      -- 标的资产
long_token          VARCHAR(66)      -- 多头抵押代币
short_token         VARCHAR(66)      -- 空头抵押代币
is_disabled         BOOLEAN          -- 是否禁用

-- 资金规模
total_supply        DECIMAL(78,0)    -- GM Token 总供应量
total_value_locked  DECIMAL(78,0)    -- TVL (USD, 30位精度)
long_token_amount   DECIMAL(78,0)    -- 多头代币数量
short_token_amount  DECIMAL(78,0)    -- 空头代币数量
long_token_amount_usd  DECIMAL(78,0) -- 多头代币价值 (USD)
short_token_amount_usd DECIMAL(78,0) -- 空头代币价值 (USD)

-- 持仓数据 (Open Interest)
open_interest_long          DECIMAL(78,0)  -- 多头 OI (USD)
open_interest_short         DECIMAL(78,0)  -- 空头 OI (USD)
open_interest_in_tokens_long  DECIMAL(78,0)  -- 多头 OI (tokens)
open_interest_in_tokens_short DECIMAL(78,0)  -- 空头 OI (tokens)

-- 盈亏数据
long_pnl                DECIMAL(78,0)  -- 多头盈亏 (USD)
short_pnl               DECIMAL(78,0)  -- 空头盈亏 (USD)
net_pnl                 DECIMAL(78,0)  -- 净盈亏 (USD)
total_borrowing_fees    DECIMAL(78,0)  -- 总借款费 (USD)

-- 费率配置
funding_factor                 DECIMAL(78,0)  -- 资金费率
borrowing_factor_for_longs     DECIMAL(78,0)  -- 多头借款费率
borrowing_factor_for_shorts    DECIMAL(78,0)  -- 空头借款费率
swap_fee_factor                DECIMAL(78,0)  -- Swap 基础费率
position_fee_factor            DECIMAL(78,0)  -- 开平仓手续费率
position_impact_factor         DECIMAL(78,0)  -- 价格冲击因子

-- 容量限制
max_pool_amount_long_token   DECIMAL(78,0)  -- 多头代币存入上限
max_pool_amount_short_token  DECIMAL(78,0)  -- 空头代币存入上限
max_open_interest_long       DECIMAL(78,0)  -- 多头最大 OI
max_open_interest_short      DECIMAL(78,0)  -- 空头最大 OI

-- 元数据
last_update_block_number  BIGINT        -- 最后更新区块
last_update_time_ms       BIGINT        -- 最后更新时间 (毫秒)
last_update_tx_hash       VARCHAR(66)   -- 最后更新交易哈希
```

</div>

</div>

### 主动同步接口

#### POST /api/v1/gm-pools/sync

**功能**: 从区块链主动同步所有 GM Pool 的最新状态

**请求体**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "block_number": 12345678  // 可选：指定同步的区块高度
}
```

</div>

</div>

**返回示例**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "success": true,
  "synced_count": 15,
  "pools": [
    {
      "pool_address": "0x...",
      "symbol": "BTC/USD",
      "total_value_locked": "15000000000000000000000000000000",
      "open_interest_long": "8000000000000000000000000000000",
      "open_interest_short": "7000000000000000000000000000000"
    }
  ]
}
```

</div>

</div>

**实现原理**:

1.  调用 Reader 合约的 `GetMarkets()` 获取所有市场地址

2.  对每个市场调用 `GetMarketInfo()` 获取详细数据

3.  更新数据库记录

------------------------------------------------------------------------

## GLV Pool 模块

### 功能说明

GLV (Global Liquidity Vault) 是 GMX V2 的全局流动性池，可以将流动性分配到多个 GM 市场。

### 事件解析

#### GlvPoolCreated

**触发时机**: 新 GLV Pool 创建时

**关键字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
type GlvPoolCreatedEvent struct {
    GlvAddress  common.Address  // GLV 合约地址
    GlvToken    common.Address  // GLV ERC20 Token
    LongToken   common.Address  // 长头寸代币
    ShortToken  common.Address  // 短头寸代币
}
```

</div>

</div>

#### GlvPoolUpdated

**触发时机**: GLV 状态变化时

**处理逻辑**: 类似 MarketUpdated，刷新 GLV 实时数据

### 数据库模型

**表名**: `bsc_glv_pools` (无分区)

**核心字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 基础信息
glv_address         VARCHAR(66)      -- GLV 地址（唯一键）
glv_token           VARCHAR(66)      -- GLV Token 地址
long_token          VARCHAR(66)      -- 长头寸代币
short_token         VARCHAR(66)      -- 短头寸代币
is_disabled         BOOLEAN          -- 是否禁用

-- 资金规模
total_supply        DECIMAL(78,0)    -- GLV Token 总供应
total_locked_value  DECIMAL(78,0)    -- 总锁定价值 (USD)
long_token_amount   DECIMAL(78,0)    -- 长头寸代币数量
short_token_amount  DECIMAL(78,0)    -- 短头寸代币数量

-- 持仓数据
open_interest_long          DECIMAL(78,0)  -- 多头 OI
open_interest_short         DECIMAL(78,0)  -- 空头 OI
open_interest_in_tokens_long  DECIMAL(78,0)
open_interest_in_tokens_short DECIMAL(78,0)

-- 元数据
last_update_block_number  BIGINT
last_update_time_ms       BIGINT
last_update_tx_hash       VARCHAR(66)
```

</div>

</div>

### GLV 市场分配表

**表名**: `bsc_glv_market_distributions` (无分区)

记录 GLV 如何将流动性分配到各个 GM 市场：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
glv_address         VARCHAR(66)      -- GLV 地址
gm_market_address   VARCHAR(66)      -- GM 市场地址
allocation_weight   DECIMAL(78,0)    -- 分配权重
allocated_amount    DECIMAL(78,0)    -- 已分配金额
last_sync_time_ms   BIGINT           -- 最后同步时间
```

</div>

</div>

------------------------------------------------------------------------

## Order 订单模块

### 功能说明

管理 GMX V2 的订单生命周期，支持多种订单类型（市价单、限价单、止损单等）。

### 订单类型枚举

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const (
    GmxOrderTypeMarketSwap       = 0  // 市价 Swap
    GmxOrderTypeLimitSwap        = 1  // 限价 Swap
    GmxOrderTypeMarketIncrease   = 2  // 市价开仓/加仓
    GmxOrderTypeLimitIncrease    = 3  // 限价开仓/加仓
    GmxOrderTypeMarketDecrease   = 4  // 市价平仓/减仓
    GmxOrderTypeLimitDecrease    = 5  // 限价平仓/减仓
    GmxOrderTypeStopLossDecrease = 6  // 止损单
    GmxOrderTypeLiquidation      = 7  // 强平单
)
```

</div>

</div>

### 订单状态流转

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Created (创建)
    ↓
  [等待执行]
    ↓
  ┌─────────┬─────────┐
  ↓         ↓         ↓
Executed  Cancelled  Frozen (冻结)
```

</div>

</div>

### 事件解析

#### OrderCreated

**触发时机**: 用户提交新订单

**关键字段**:

<div class="table-wrap">

|                                |             |                          |
|--------------------------------|-------------|--------------------------|
| 事件字段                       | 类型        | 说明                     |
| `orderKey`                     | bytes32     | 订单唯一键               |
| `account`                      | address     | 用户地址                 |
| `market`                       | address     | 目标市场                 |
| `orderType`                    | uint256     | 订单类型 (0-7)           |
| `sizeDeltaUsd`                 | uint256     | 规模变化 (USD, 30位精度) |
| `initialCollateralToken`       | address     | 初始抵押代币             |
| `initialCollateralDeltaAmount` | uint256     | 抵押品数量               |
| `triggerPrice`                 | uint256     | 触发价格 (0表示市价单)   |
| `acceptablePrice`              | uint256     | 可接受价格 (滑点保护)    |
| `executionFee`                 | uint256     | 执行费用                 |
| `isLong`                       | bool        | 做多/做空                |
| `triggerAboveThreshold`        | bool        | 价格向上/向下触发        |
| `swapPath`                     | address\[\] | Swap 路径                |
| `updatedAtTime`                | uint256     | 创建时间 (秒)            |

</div>

**字段映射逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (h *OrderCreatedHandler) convertToOrderModel(ev *OrderCreatedEvent, ctx *event.Context) (*bscmodel.BscPerpOrderModel, error) {
    order := &bscmodel.BscPerpOrderModel{
        OrderKey:                fmt.Sprintf("0x%x", ev.OrderKey),
        Account:                 ev.Account.Hex(),
        Market:                  ev.Market.Hex(),
        InitialCollateralToken:  ev.InitialCollateralToken.Hex(),
        OrderType:               h.mapOrderType(ev.OrderType.Int64()),
        OrderStatus:             consts.OrderStatusCreated,
        IsLong:                  ev.IsLong,
        SizeDeltaUsd:            decimal.NewFromBigInt(ev.SizeDeltaUsd, 0),
        AcceptablePrice:         decimal.NewFromBigInt(ev.AcceptablePrice, 0),
        TriggerPrice:            decimal.NewFromBigInt(ev.TriggerPrice, 0),
        ExecutionFee:            decimal.NewFromBigInt(ev.ExecutionFee, 0),
        TriggerAboveThreshold:   ev.TriggerAboveThreshold,
        // ...
        CreateTimestampMs:       ctx.Tx.BlockTimestamp * 1000, // 转换为毫秒
    }

    // Swap 路径转 JSON
    if len(ev.SwapPath) > 0 {
        swapPathJSON, _ := json.Marshal(ev.SwapPath)
        order.SwapPath = string(swapPathJSON)
    }

    // 设置 reduce_only
    if order.OrderType == consts.GmxOrderTypeMarketDecrease ||
       order.OrderType == consts.GmxOrderTypeLimitDecrease ||
       order.OrderType == consts.GmxOrderTypeStopLossDecrease {
        order.ReduceOnly = true
    }

    return order, nil
}
```

</div>

</div>

#### OrderExecuted

**触发时机**: 订单被执行

**关键字段**:

- `orderKey`: 订单键

- `executionPrice`: 实际执行价格

- `collateralDeltaAmount`: 实际抵押品变化

**处理逻辑**:

1.  根据 `orderKey` 查询已有订单记录

2.  更新订单状态为 `Executed`

3.  填充 `execution_price` 和 `collateral_delta_amount`

4.  更新 `update_block_number`, `update_tx_hash`, `update_timestamp_ms`

**重要说明**:

- `OrderExecuted` 事件 **不直接** 更新 Position，Position 更新由 `PositionIncrease`/`PositionDecrease` 事件负责

- 同一笔交易中会同时出现 `OrderExecuted` + `PositionIncrease`/`Decrease` 事件

#### OrderCancelled

**触发时机**: 订单被取消（用户主动取消或系统取消）

**关键字段**:

- `orderKey`

- `reason` / `reasonBytes`: 取消原因

**处理逻辑**:

- 更新订单状态为 `Cancelled`

- 记录 `cancellation_reason`

#### OrderUpdated

**触发时机**: 订单参数更新（较少使用）

#### OrderFrozen

**触发时机**: 订单被冻结（通常是因为执行条件未满足）

**处理逻辑**:

- 更新订单状态为 `Frozen`

- 记录 `frozen_reason`

### 数据库模型

**表名**: `bsc_perp_order_{0..127}` (128 分区，按 `account` 哈希)

**核心字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 核心标识
order_key               VARCHAR(66)      -- 订单唯一键（bytes32 hex）
account                 VARCHAR(42)      -- 用户地址
market                  VARCHAR(42)      -- 目标市场

-- 订单类型和状态
order_type              INT              -- 订单类型 (0-7)
order_status            VARCHAR(20)      -- 状态: created/executed/cancelled/frozen
is_long                 BOOLEAN          -- 多空方向
reduce_only             BOOLEAN          -- 是否只减仓

-- 订单参数
size_delta_usd          DECIMAL(78,0)    -- 规模变化 (USD)
acceptable_price        DECIMAL(78,0)    -- 可接受价格
trigger_price           DECIMAL(78,0)    -- 触发价格 (0=市价单)
execution_fee           DECIMAL(78,0)    -- 执行费用
trigger_above_threshold BOOLEAN          -- 向上/向下触发

-- 抵押品
initial_collateral_token  VARCHAR(42)    -- 初始抵押代币
swap_path                 TEXT           -- Swap 路径 (JSON 数组)
min_output_amount         DECIMAL(78,0)  -- 最小输出量
should_unwrap_native_token BOOLEAN       -- 解包原生代币

-- 回调和UI
referral_code           VARCHAR(66)      -- 推荐码
callback_contract       VARCHAR(42)      -- 回调合约
ui_fee_receiver         VARCHAR(42)      -- UI 费用接收者

-- 创建信息
create_block_number     BIGINT           -- 创建区块
create_tx_hash          VARCHAR(66)      -- 创建交易
create_timestamp_ms     BIGINT           -- 创建时间 (毫秒)

-- 最后更新信息
update_block_number     BIGINT           -- 更新区块
update_tx_hash          VARCHAR(66)      -- 更新交易
update_timestamp_ms     BIGINT           -- 更新时间 (毫秒)

-- 执行结果（仅执行后填充）
execution_price         DECIMAL(78,0)    -- 实际执行价格
collateral_delta_amount DECIMAL(78,0)    -- 实际抵押品变化

-- 取消/冻结原因
cancellation_reason     VARCHAR(512)     -- 取消原因
frozen_reason           VARCHAR(512)     -- 冻结原因
```

</div>

</div>

### 辅助方法

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 判断订单类型
func (m *BscPerpOrderModel) IsMarketOrder() bool {
    return m.TriggerPrice.IsZero()
}

func (m *BscPerpOrderModel) IsTriggerOrder() bool {
    return !m.TriggerPrice.IsZero()
}

func (m *BscPerpOrderModel) IsIncreaseOrder() bool {
    return m.OrderType == consts.GmxOrderTypeMarketIncrease ||
           m.OrderType == consts.GmxOrderTypeLimitIncrease
}

func (m *BscPerpOrderModel) IsDecreaseOrder() bool {
    return m.OrderType == consts.GmxOrderTypeMarketDecrease ||
           m.OrderType == consts.GmxOrderTypeLimitDecrease ||
           m.OrderType == consts.GmxOrderTypeStopLossDecrease
}

// 分类触发单为 TP/SL
func (m *BscPerpOrderModel) ClassifyTriggerOrder() string {
    if !m.IsTriggerOrder() {
        return "not_trigger_order"
    }

    if m.IsLong {
        if m.TriggerAboveThreshold {
            return "tp_long"  // 多单止盈：价格上涨触发
        }
        return "sl_long"  // 多单止损：价格下跌触发
    } else {
        if m.TriggerAboveThreshold {
            return "sl_short" // 空单止损：价格上涨触发
        }
        return "tp_short" // 空单止盈：价格下跌触发
    }
}
```

</div>

</div>

------------------------------------------------------------------------

## Position 仓位模块

### 功能说明

管理用户的永续合约仓位状态。一个仓位由 `(account, market, collateralToken, isLong)` 唯一标识。

### Position Key 计算

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Position Key = keccak256(abi.encode(account, market, collateralToken, isLong))
func calculatePositionKey(
    account common.Address,
    market common.Address,
    collateralToken common.Address,
    isLong bool,
) string {
    // Solidity ABI 编码：每个参数填充为 32 字节
    encoded := make([]byte, 0, 128)
    encoded = append(encoded, common.LeftPadBytes(account.Bytes(), 32)...)
    encoded = append(encoded, common.LeftPadBytes(market.Bytes(), 32)...)
    encoded = append(encoded, common.LeftPadBytes(collateralToken.Bytes(), 32)...)

    boolPadded := make([]byte, 32)
    if isLong {
        boolPadded[31] = 1
    }
    encoded = append(encoded, boolPadded...)

    hash := crypto.Keccak256(encoded)
    return strings.ToLower(hexutil.Encode(hash))
}
```

</div>

</div>

### 仓位状态枚举

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const (
    PositionStatusGmxActive     = "active"      // 活跃仓位
    PositionStatusGmxClosed     = "closed"      // 已平仓
    PositionStatusGmxLiquidated = "liquidated"  // 已强平
    PositionStatusGmxADL        = "adl"         // ADL 平仓
)
```

</div>

</div>

### 事件解析

#### PositionIncrease

**触发时机**: 开仓或加仓

**关键字段**:

<div class="table-wrap">

|                         |         |                     |
|-------------------------|---------|---------------------|
| 事件字段                | 类型    | 说明                |
| `positionKey`           | bytes32 | 仓位唯一键          |
| `account`               | address | 用户地址            |
| `market`                | address | 市场地址            |
| `collateralToken`       | address | 抵押代币地址        |
| `isLong`                | bool    | 多空方向            |
| `executionPrice`        | uint256 | 执行价格            |
| `sizeDeltaUsd`          | uint256 | 规模增加量 (USD)    |
| `sizeDeltaInTokens`     | uint256 | 规模增加量 (tokens) |
| `collateralDeltaAmount` | uint256 | 抵押品增加量        |
| `priceImpactUsd`        | uint256 | 价格冲击            |
| `orderType`             | uint256 | 订单类型            |
| `indexTokenPrice`       | uint256 | 指数代币价格        |
| `collateralTokenPrice`  | uint256 | 抵押代币价格        |

</div>

**处理逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (h *PositionIncreaseHandler) Handle(ctx context.Context, evt event.Context) error {
    // 1. 解析事件
    payload := buildPositionIncreaseEvent(accessor)

    // 2. 查找关联的 OrderKey (从同一笔交易中的 OrderExecuted 事件)
    orderKey := findOrderKeyFromTransaction(evt.Tx, h.eventEmitterAddr)

    // 3. 提取费用数据 (从 PositionFeesCollected 事件)
    feeData, _ := FindPositionFeesInTransaction(evt.Tx, orderKeyBytes, h.eventEmitterAddr)
    fundingFee, borrowingFee, positionFee := feeData.ToDecimalFees()

    // 4. 构建参数
    params := &position.PositionUpdateParams{
        PositionKey:           positionKey,
        Account:               account,
        Market:                payload.Market.Hex(),
        CollateralToken:       payload.CollateralToken.Hex(),
        IsLong:                payload.IsLong,
        SizeDeltaUsd:          decimal.NewFromBigInt(payload.SizeDeltaUsd, 0),
        SizeDeltaTokens:       decimal.NewFromBigInt(payload.SizeDeltaInTokens, 0),
        CollateralDeltaAmount: decimal.NewFromBigInt(payload.CollateralDeltaAmount, 0),
        ExecutionPrice:        decimal.NewFromBigInt(payload.ExecutionPrice, 0),
        RealizedPnlUsd:        decimal.Zero, // 加仓无已实现盈亏
        PositionFee:           positionFee,
        FundingFee:            fundingFee,
        BorrowingFee:          borrowingFee,
        OrderKey:              orderKey,
        OrderType:             consts.GmxOrderType(payload.OrderType.Int64()),
        TxHash:                evt.Tx.TxHash,
        BlockNumber:           evt.Tx.BlockNumber,
        Timestamp:             evt.Tx.BlockTimestamp * 1000,
        EventType:             consts.GmxPositionEventTypeIncrease,
    }

    // 5. 调用 Position Service 处理业务逻辑
    return h.positionSvc.HandlePositionIncrease(ctx, params)
}
```

</div>

</div>

**Service 层处理**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (s *Service) HandlePositionIncrease(ctx context.Context, params *PositionUpdateParams) error {
    // 1. 查询现有仓位
    existingPos, err := s.positionDAL.GetByPositionKey(ctx, params.PositionKey, params.Account)

    var position *bscmodel.BscPerpPositionModel
    var isNewPosition bool

    if err != nil || existingPos == nil {
        // 新开仓
        isNewPosition = true
        position = s.createNewPosition(params)
    } else {
        // 加仓
        isNewPosition = false
        position = existingPos
        s.applyPositionIncrease(position, params)
    }

    // 2. 更新平均入场价格
    position.UpdateAvgEntryPrice(oldSize, params.SizeDeltaUsd, params.ExecutionPrice)

    // 3. 累加费用
    position.CumulativeFundingFee = position.CumulativeFundingFee.Add(params.FundingFee)
    position.CumulativeBorrowingFee = position.CumulativeBorrowingFee.Add(params.BorrowingFee)
    position.CumulativePositionFee = position.CumulativePositionFee.Add(params.PositionFee)

    // 4. 重新计算杠杆
    position.Leverage = position.CalculateLeverage()

    // 5. 更新元数据
    position.LastIncreasedAt = params.Timestamp
    position.LastTxHash = params.TxHash
    position.LastBlockNumber = params.BlockNumber
    position.LastEventType = params.EventType
    position.Status = consts.PositionStatusGmxActive

    // 6. 保存仓位
    if err := s.positionDAL.SavePosition(ctx, position); err != nil {
        return err
    }

    // 7. 创建交易历史记录
    tradeAction := consts.TradeActionOpen
    if !isNewPosition {
        tradeAction = consts.TradeActionIncrease
    }

    trade := s.buildTradeRecord(params, position, tradeAction)
    return s.tradesDAL.Create(ctx, trade)
}
```

</div>

</div>

#### PositionDecrease

**触发时机**: 平仓或减仓

**关键字段** (相比 PositionIncrease 额外):

<div class="table-wrap">

|                          |        |                |
|--------------------------|--------|----------------|
| 事件字段                 | 类型   | 说明           |
| `basePnlUsd`             | int256 | 基础盈亏 (USD) |
| `uncappedBasePnlUsd`     | int256 | 未封顶基础盈亏 |
| `pnlAfterPriceImpactUsd` | int256 | 价格冲击后盈亏 |

</div>

**处理逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (h *PositionDecreaseHandler) Handle(ctx context.Context, evt event.Context) error {
    // 1. 解析事件
    payload := buildPositionDecreaseEvent(accessor)

    // 2. 提取已实现盈亏
    var realizedPnl decimal.Decimal
    if payload.PnlAfterPriceImpactUsd != nil {
        realizedPnl = decimal.NewFromBigInt(payload.PnlAfterPriceImpactUsd, 0)
    } else if payload.BasePnlUsd != nil {
        realizedPnl = decimal.NewFromBigInt(payload.BasePnlUsd, 0)
    }

    // 3. 构建参数（与 PositionIncrease 类似）
    params := &position.PositionUpdateParams{
        // ... 基础字段 ...
        RealizedPnlUsd: realizedPnl,  // 关键区别：有已实现盈亏
        EventType:      consts.GmxPositionEventTypeDecrease,
    }

    // 4. 调用 Position Service
    return h.positionSvc.HandlePositionDecrease(ctx, params)
}
```

</div>

</div>

**Service 层处理**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (s *Service) HandlePositionDecrease(ctx context.Context, params *PositionUpdateParams) error {
    // 1. 必须存在现有仓位
    existingPos, err := s.positionDAL.GetByPositionKey(ctx, params.PositionKey, params.Account)
    if err != nil || existingPos == nil {
        return fmt.Errorf("position not found for decrease")
    }

    // 2. 应用减仓逻辑
    oldSize := existingPos.SizeInUsd
    newSize := oldSize.Sub(params.SizeDeltaUsd)

    existingPos.SizeInUsd = newSize
    existingPos.SizeInTokens = existingPos.SizeInTokens.Sub(params.SizeDeltaTokens)
    existingPos.CollateralAmount = existingPos.CollateralAmount.Sub(params.CollateralDeltaAmount)

    // 3. 累加已实现盈亏
    existingPos.RealizedPnlUsd = existingPos.RealizedPnlUsd.Add(params.RealizedPnlUsd)

    // 4. 累加费用
    existingPos.CumulativeFundingFee = existingPos.CumulativeFundingFee.Add(params.FundingFee)
    existingPos.CumulativeBorrowingFee = existingPos.CumulativeBorrowingFee.Add(params.BorrowingFee)
    existingPos.CumulativePositionFee = existingPos.CumulativePositionFee.Add(params.PositionFee)

    // 5. 判断是否完全平仓
    if newSize.IsZero() || newSize.LessThan(decimal.NewFromInt(1000)) { // 小于阈值视为平仓
        existingPos.Status = consts.PositionStatusGmxClosed
        now := params.Timestamp
        existingPos.ClosedAt = &now
    }

    // 6. 重新计算杠杆
    existingPos.Leverage = existingPos.CalculateLeverage()

    // 7. 更新元数据
    existingPos.LastDecreasedAt = params.Timestamp
    existingPos.LastTxHash = params.TxHash
    existingPos.LastBlockNumber = params.BlockNumber
    existingPos.LastEventType = params.EventType

    // 8. 保存仓位
    if err := s.positionDAL.SavePosition(ctx, existingPos); err != nil {
        return err
    }

    // 9. 创建交易历史记录
    tradeAction := consts.TradeActionDecrease
    if existingPos.Status == consts.PositionStatusGmxClosed {
        tradeAction = consts.TradeActionClose
    }

    trade := s.buildTradeRecord(params, existingPos, tradeAction)
    return s.tradesDAL.Create(ctx, trade)
}
```

</div>

</div>

### 数据库模型

**表名**: `bsc_perp_position_{0..127}` (128 分区，按 `account` 哈希)

**核心字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 核心标识
position_key        VARCHAR(66)      -- 仓位唯一键（bytes32 hex）
account             VARCHAR(42)      -- 用户地址
market              VARCHAR(42)      -- 市场地址
collateral_token    VARCHAR(42)      -- 抵押代币地址
is_long             BOOLEAN          -- 多空方向

-- 仓位规模
size_in_usd         DECIMAL(78,0)    -- 仓位规模 (USD, 30位精度)
size_in_tokens      DECIMAL(78,0)    -- 仓位规模 (tokens)
collateral_amount   DECIMAL(78,0)    -- 抵押品数量

-- 价格信息
open_price          DECIMAL(78,0)    -- 开仓价格（首次开仓时的执行价）
avg_entry_price     DECIMAL(78,0)    -- 平均入场价格（加权平均）

-- 费用累计
cumulative_funding_fee   DECIMAL(78,0)  -- 累计资金费
cumulative_borrowing_fee DECIMAL(78,0)  -- 累计借款费
cumulative_position_fee  DECIMAL(78,0)  -- 累计开平仓费

-- 费用快照（用于增量计算）
funding_fee_snapshot    DECIMAL(78,0)   -- 资金费快照
borrowing_fee_snapshot  DECIMAL(78,0)   -- 借款费快照

-- 风险指标
leverage            DECIMAL(30,10)   -- 杠杆倍数
liquidation_price   DECIMAL(78,0)    -- 强平价格（计算得出）

-- 已实现盈亏
realized_pnl_usd    DECIMAL(78,0)    -- 累计已实现盈亏 (USD)

-- 仓位状态
status              VARCHAR(20)      -- active/closed/liquidated/adl

-- 时间戳
last_increased_at   BIGINT           -- 最后加仓时间 (毫秒)
last_decreased_at   BIGINT           -- 最后减仓时间 (毫秒)
closed_at           BIGINT           -- 平仓时间 (毫秒，可为 NULL)

-- 最后更新信息
last_tx_hash        VARCHAR(66)      -- 最后更新交易
last_block_number   BIGINT           -- 最后更新区块
last_event_type     VARCHAR(20)      -- 最后事件类型 (increase/decrease)
```

</div>

</div>

### 主动同步接口

#### POST /api/v1/positions/sync

**功能**: 从区块链主动同步指定用户的所有仓位

**请求体**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "account": "0x1234...",        // 必填：用户地址
  "force_update": false,         // 可选：是否强制更新已有仓位
  "start": 0,                    // 可选：起始索引（分页）
  "end": 100                     // 可选：结束索引（分页）
}
```

</div>

</div>

**返回示例**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "success": true,
  "data": {
    "account": "0x1234...",
    "synced_positions": 5,
    "updated_positions": 2,
    "new_positions": 3,
    "skipped_positions": 1,
    "positions": [
      {
        "position_key": "0xabcd...",
        "market": "0x5678...",
        "collateral_token": "0x0b7d...",
        "is_long": true,
        "size_in_usd": "10000000000000000000000000000000",
        "collateral_amount": "2000000000000000000000000000000",
        "leverage": "5.000000000",
        "status": "active"
      }
    ]
  }
}
```

</div>

</div>

**实现原理**:

1.  调用 Reader 合约的 `GetAccountPositions(dataStore, account, start, end)`

2.  对每个返回的 Position：

    - 计算 Position Key

    - 转换为数据库模型

    - 保存或更新记录

3.  注意事项：

    - **历史数据不可用**: 链上只有当前状态，无法获取 `OpenPrice`, `AvgEntryPrice`, `CumulativeFees`

    - **仅适用于补充数据**: 主要用于初始化或修复丢失的仓位

**字段来源**:

<div class="table-wrap">

|                        |          |                                           |
|------------------------|----------|-------------------------------------------|
| 字段                   | 来源     | 说明                                      |
| `SizeInUsd`            | 链上     | `PositionNumbers.SizeInUsd`               |
| `SizeInTokens`         | 链上     | `PositionNumbers.SizeInTokens`            |
| `CollateralAmount`     | 链上     | `PositionNumbers.CollateralAmount`        |
| `FundingFeeSnapshot`   | 链上     | `PositionNumbers.FundingFeeAmountPerSize` |
| `BorrowingFeeSnapshot` | 链上     | `PositionNumbers.BorrowingFactor`         |
| `LastIncreasedAt`      | 链上     | `PositionNumbers.IncreasedAtTime * 1000`  |
| `LastDecreasedAt`      | 链上     | `PositionNumbers.DecreasedAtTime * 1000`  |
| `OpenPrice`            | **事件** | 无法从链上获取，设为 0                    |
| `AvgEntryPrice`        | **事件** | 无法从链上获取，设为 0                    |
| `CumulativeFees`       | **事件** | 无法从链上获取，设为 0                    |
| `RealizedPnlUsd`       | **事件** | 无法从链上获取，设为 0                    |

</div>

------------------------------------------------------------------------

## Trades 交易历史模块

### 功能说明

记录每一次仓位变化（开仓、加仓、减仓、平仓）的交易历史，包含详细的费用、盈亏数据。

### 交易动作枚举

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const (
    TradeActionOpen      = "open"       // 开仓
    TradeActionIncrease  = "increase"   // 加仓
    TradeActionDecrease  = "decrease"   // 减仓
    TradeActionClose     = "close"      // 平仓
    TradeActionLiquidate = "liquidate"  // 强平
    TradeActionADL       = "adl"        // ADL
)
```

</div>

</div>

### 数据来源

Trades 记录 **不是** 直接由事件生成，而是在 Position Service 处理 `PositionIncrease` / `PositionDecrease` 时创建：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func (s *Service) HandlePositionIncrease(ctx context.Context, params *PositionUpdateParams) error {
    // ... 处理仓位逻辑 ...

    // 创建交易记录
    trade := &bscmodel.BscPerpTradesModel{
        TxHash:                params.TxHash,
        LogIndex:              params.LogIndex,
        PositionKey:           params.PositionKey,
        Account:               params.Account,
        Market:                params.Market,
        CollateralToken:       params.CollateralToken,
        IsLong:                params.IsLong,
        TradeAction:           tradeAction,  // open/increase
        OrderType:             ConvertToTradeOrderType(params.OrderType),
        SizeDeltaUsd:          params.SizeDeltaUsd,
        SizeDeltaTokens:       params.SizeDeltaTokens,
        CollateralDeltaAmount: params.CollateralDeltaAmount,
        ExecutionPrice:        params.ExecutionPrice,
        MarkPrice:             params.MarkPrice,
        RealizedPnlUsd:        params.RealizedPnlUsd,  // Increase 时为 0
        PositionFee:           params.PositionFee,
        FundingFee:            params.FundingFee,
        BorrowingFee:          params.BorrowingFee,
        SwapFee:               params.SwapFee,
        TotalFee:              totalFee,
        PositionSizeAfter:     position.SizeInUsd,
        PositionCollateralAfter: position.CollateralAmount,
        IsLiquidation:         false,
        BlockNumber:           params.BlockNumber,
        Timestamp:             params.Timestamp,
        EventType:             params.EventType,
        OrderKey:              params.OrderKey,
    }

    return s.tradesDAL.Create(ctx, trade)
}
```

</div>

</div>

### 数据库模型

**表名**: `bsc_perp_trades_{0..127}` (128 分区，按 `account` 哈希)

**核心字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 唯一标识（交易哈希 + 日志索引）
tx_hash             VARCHAR(66)      -- 交易哈希
log_index           INT              -- 日志索引
-- 组合唯一索引：(tx_hash, log_index)

-- 仓位标识
position_key        VARCHAR(66)      -- 关联的仓位
account             VARCHAR(42)      -- 用户地址
market              VARCHAR(42)      -- 市场地址
collateral_token    VARCHAR(42)      -- 抵押代币
is_long             BOOLEAN          -- 多空方向

-- 交易类型
trade_action        VARCHAR(20)      -- open/increase/decrease/close/liquidate/adl
order_type          VARCHAR(20)      -- market/limit/stop_loss

-- 规模变化
size_delta_usd          DECIMAL(78,0)  -- 规模变化 (USD)
size_delta_tokens       DECIMAL(78,0)  -- 规模变化 (tokens)
collateral_delta_amount DECIMAL(78,0)  -- 抵押品变化

-- 价格
execution_price     DECIMAL(78,0)    -- 执行价格
mark_price          DECIMAL(78,0)    -- 标记价格

-- 盈亏
realized_pnl_usd    DECIMAL(78,0)    -- 已实现盈亏 (USD)

-- 费用明细
position_fee        DECIMAL(78,0)    -- 开平仓手续费
funding_fee         DECIMAL(78,0)    -- 资金费
borrowing_fee       DECIMAL(78,0)    -- 借款费
swap_fee            DECIMAL(78,0)    -- Swap 费用
total_fee           DECIMAL(78,0)    -- 总费用

-- 仓位状态快照
position_size_after       DECIMAL(78,0)  -- 交易后仓位规模
position_collateral_after DECIMAL(78,0)  -- 交易后抵押品数量

-- 强平信息
is_liquidation      BOOLEAN          -- 是否为强平
liquidation_price   DECIMAL(78,0)    -- 强平价格（可选）

-- 元数据
block_number        BIGINT           -- 区块号
timestamp           BIGINT           -- 时间戳 (毫秒)
event_type          VARCHAR(20)      -- increase/decrease
order_key           VARCHAR(66)      -- 关联的订单（可选）
```

</div>

</div>

### 辅助方法

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 判断交易类型
func (m *BscPerpTradesModel) IsIncrease() bool {
    return m.TradeAction == consts.TradeActionOpen ||
           m.TradeAction == consts.TradeActionIncrease
}

func (m *BscPerpTradesModel) IsDecrease() bool {
    return m.TradeAction == consts.TradeActionDecrease ||
           m.TradeAction == consts.TradeActionClose
}

func (m *BscPerpTradesModel) IsForcedClose() bool {
    return m.TradeAction == consts.TradeActionLiquidate ||
           m.TradeAction == consts.TradeActionADL
}

// 计算净盈亏
func (m *BscPerpTradesModel) CalculateNetPnl() decimal.Decimal {
    return m.RealizedPnlUsd.Sub(m.TotalFee)
}

// 订单类型转换
func ConvertToTradeOrderType(gmxOrderType consts.GmxOrderType) consts.TradeOrderType {
    switch gmxOrderType {
    case consts.GmxOrderTypeMarketIncrease,
         consts.GmxOrderTypeMarketDecrease,
         consts.GmxOrderTypeMarketSwap:
        return consts.TradeOrderTypeMarket
    case consts.GmxOrderTypeLimitIncrease,
         consts.GmxOrderTypeLimitDecrease,
         consts.GmxOrderTypeLimitSwap:
        return consts.TradeOrderTypeLimit
    case consts.GmxOrderTypeStopLossDecrease:
        return consts.TradeOrderTypeStopLoss
    default:
        return consts.TradeOrderTypeMarket
    }
}

// 判断交易动作
func DetermineTradeAction(
    eventType consts.GmxPositionEventType,
    positionBefore *BscPerpPositionModel,
    positionAfter *BscPerpPositionModel,
) consts.TradeActionType {
    switch eventType {
    case consts.GmxPositionEventTypeIncrease:
        if positionBefore == nil || positionBefore.SizeInUsd.IsZero() {
            return consts.TradeActionOpen
        }
        return consts.TradeActionIncrease
    case consts.GmxPositionEventTypeDecrease:
        if positionAfter.SizeInUsd.IsZero() {
            return consts.TradeActionClose
        }
        return consts.TradeActionDecrease
    case consts.GmxPositionEventTypeLiquidated:
        return consts.TradeActionLiquidate
    case consts.GmxPositionEventTypeADL:
        return consts.TradeActionADL
    default:
        return consts.TradeActionDecrease
    }
}
```

</div>

</div>

------------------------------------------------------------------------

## 事件字段映射表

### 事件字段 Key 常量

所有事件字段 key 定义在 `data-statistics-infra/consts/bsc_event_key.go`：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 通用字段
BscEventKeyAccount       = "account"
BscEventKeyMarket        = "market"
BscEventKeyUpdatedAtTime = "updatedAtTime"

// Order 相关
BscEventKeyOrderKey                     = "orderKey"
BscEventKeyOrderType                    = "orderType"
BscEventKeySizeDeltaUsd                 = "sizeDeltaUsd"
BscEventKeyInitialCollateralToken       = "initialCollateralToken"
BscEventKeyTriggerPrice                 = "triggerPrice"
BscEventKeyAcceptablePrice              = "acceptablePrice"
BscEventKeyIsLong                       = "isLong"

// Position 相关
BscEventKeyPositionKey           = "positionKey"
BscEventKeyCollateralToken       = "collateralToken"
BscEventKeySizeDeltaInTokens     = "sizeDeltaInTokens"
BscEventKeyExecutionPrice        = "executionPrice"
BscEventKeyCollateralDeltaAmount = "collateralDeltaAmount"
BscEventKeyIndexTokenPrice       = "indexTokenPrice"
BscEventKeyBasePnlUsd            = "basePnlUsd"
BscEventKeyPnlAfterPriceImpactUsd = "pnlAfterPriceImpactUsd"

// Fees 相关
BscEventKeyFundingFeeAmount   = "fundingFeeAmount"
BscEventKeyBorrowingFeeAmount = "borrowingFeeAmount"
BscEventKeyPositionFeeAmount  = "positionFeeAmount"
```

</div>

</div>

### 重要字段区分

#### `initialCollateralToken` vs `collateralToken`

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 | 使用场景 | 说明 |
| `initialCollateralToken` | Order 事件 | 用户创建订单时指定的抵押代币 |
| `collateralToken` | Position 事件 | 实际backing仓位的抵押代币（可能经过swap） |

</div>

**示例**:

- 用户提交订单：抵押 USDC（`initialCollateralToken = USDC`）

- 订单执行时进行 Swap：USDC → WETH

- 最终仓位：抵押 WETH（`collateralToken = WETH`）

#### 费用字段详解

**PositionFeesCollected 事件**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
type PositionFeesData struct {
    FundingFeeAmount   *big.Int  // 资金费（正数=支付，负数=收取）
    BorrowingFeeAmount *big.Int  // 借款费（总是支付）
    PositionFeeAmount  *big.Int  // 开平仓手续费
    TotalCostAmount    *big.Int  // 总费用
}
```

</div>

</div>

**费用关系**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
TotalFee = PositionFee + |FundingFee| + BorrowingFee + SwapFee
NetPnL = RealizedPnL - TotalFee
```

</div>

</div>

------------------------------------------------------------------------

## 查询接口文档

### Position 相关接口

#### 1. 根据 Position Key 查询

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/positions/:positionKey?account={account}
```

</div>

</div>

**参数**:

- `positionKey` (path): 仓位唯一键 (hex)

- `account` (query): 用户地址（必填）

**返回**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "position": {
    "position_key": "0x...",
    "account": "0x...",
    "market": "0x...",
    "collateral_token": "0x...",
    "is_long": true,
    "size_in_usd": "10000000000000000000000000000000",
    "collateral_amount": "2000000000000000000000000000000",
    "avg_entry_price": "50000000000000000000000000000000",
    "leverage": "5.000000000",
    "realized_pnl_usd": "100000000000000000000000000000",
    "cumulative_funding_fee": "5000000000000000000000000000",
    "cumulative_borrowing_fee": "3000000000000000000000000000",
    "cumulative_position_fee": "10000000000000000000000000000",
    "status": "active",
    "last_increased_at": 1705881600000,
    "last_decreased_at": 0,
    "last_tx_hash": "0x..."
  }
}
```

</div>

</div>

#### 2. 查询用户所有仓位

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/positions?account={account}&limit=100&offset=0
```

</div>

</div>

**参数**:

- `account` (query): 用户地址（必填）

- `limit` (query): 每页数量（默认 100）

- `offset` (query): 偏移量（默认 0）

**返回**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "positions": [...],
  "count": 5,
  "limit": 100,
  "offset": 0
}
```

</div>

</div>

#### 3. 查询市场所有仓位

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/positions/market?market={market}&limit=100&offset=0
```

</div>

</div>

#### 4. 查询所有活跃仓位

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/positions/open?limit=100&offset=0
```

</div>

</div>

#### 5. 查询仓位交易历史

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/positions/:positionKey/trades?account={account}&limit=100&offset=0
```

</div>

</div>

**返回**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "trades": [
    {
      "tx_hash": "0x...",
      "log_index": 5,
      "trade_action": "open",
      "order_type": "market",
      "size_delta_usd": "10000000000000000000000000000000",
      "execution_price": "50000000000000000000000000000000",
      "realized_pnl_usd": "0",
      "position_fee": "10000000000000000000000000000",
      "funding_fee": "0",
      "borrowing_fee": "0",
      "total_fee": "10000000000000000000000000000",
      "position_size_after": "10000000000000000000000000000000",
      "timestamp": 1705881600000
    }
  ],
  "count": 10,
  "limit": 100,
  "offset": 0
}
```

</div>

</div>

#### 6. 查询用户交易历史

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/trades?account={account}&limit=100&offset=0
```

</div>

</div>

#### 7. 主动同步用户仓位

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST /api/v1/positions/sync
Content-Type: application/json

{
  "account": "0x1234...",
  "force_update": false,
  "start": 0,
  "end": 100
}
```

</div>

</div>

### 其他接口

#### 健康检查

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET /api/v1/ping
```

</div>

</div>

**返回**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "message": "pong"
}
```

</div>

</div>

#### 手动扫描区块

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST /api/v1/scan-blocks
Content-Type: application/json

{
  "start_block": 12345678,
  "end_block": 12345700
}
```

</div>

</div>

#### 同步 GM Pools

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST /api/v1/gm-pools/sync
Content-Type: application/json

{
  "block_number": 12345678
}
```

</div>

</div>

#### 重放交易

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST /api/v1/replay-transaction
Content-Type: application/json

{
  "tx_hash": "0x...",
  "block_number": 12345678
}
```

</div>

</div>

------------------------------------------------------------------------

## 数据精度说明

### 精度标准

GMX V2 使用 **30 位小数精度** 表示 USD 金额和价格：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1 USD = 10^30 = 1000000000000000000000000000000
$50,000 = 50000 * 10^30
```

</div>

</div>

### 数据库存储

- **类型**: `DECIMAL(78, 0)`

- **整数存储**: 所有金额字段存储为 **原始整数**（无小数点）

- **查询时转换**: 客户端需要除以 `10^30` 转换为实际金额

### 示例

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
-- 存储的原始值
size_in_usd = 10000000000000000000000000000000

-- 转换为实际金额 (Golang)
sizeUsdDecimal := decimal.NewFromBigInt(sizeInUsd, 0)
actualUsd := sizeUsdDecimal.Div(decimal.NewFromInt(10).Pow(decimal.NewFromInt(30)))
// actualUsd = 10

-- 转换为实际金额 (SQL)
SELECT
  size_in_usd / 1e30 AS size_usd,
  collateral_amount / 1e30 AS collateral_usd
FROM bsc_perp_position_0;
```

</div>

</div>

### 其他精度

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段类型 | 精度 | 说明 |
| USD 金额 | 30 位 | `size_in_usd`, `collateral_amount`, `realized_pnl_usd`, 费用字段 |
| 价格 | 30 位 | `execution_price`, `trigger_price`, `acceptable_price` |
| Token 数量 | Token 精度 | 取决于代币（如 USDC 6位，WETH 18位） |
| 杠杆 | `DECIMAL(30,10)` | 支持10位小数 |
| 百分比/费率 | 30 位 | 如 `funding_factor` (1% = 0.01 \* 10^30) |

</div>

### 转换工具函数

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Golang
func ToDecimalUSD(rawValue *big.Int) decimal.Decimal {
    return decimal.NewFromBigInt(rawValue, 0).Div(decimal.NewFromInt(10).Pow(decimal.NewFromInt(30)))
}

func FromDecimalUSD(usdValue decimal.Decimal) *big.Int {
    scaled := usdValue.Mul(decimal.NewFromInt(10).Pow(decimal.NewFromInt(30)))
    return scaled.BigInt()
}

// SQL 查询示例
SELECT
  position_key,
  account,
  size_in_usd / 1e30 AS size_usd,
  collateral_amount / 1e30 AS collateral_usd,
  (size_in_usd / NULLIF(collateral_amount, 0)) AS leverage,
  realized_pnl_usd / 1e30 AS realized_pnl_usd
FROM bsc_perp_position_0
WHERE account = '0x...'
  AND status = 'active';
```

</div>

</div>

------------------------------------------------------------------------

## 常见问题

### Q1: Position 数据不完整怎么办？

**A**: 使用主动同步接口 `/api/v1/positions/sync` 从区块链补充数据。注意历史字段（如 `avg_entry_price`, `cumulative_fees`）无法从链上获取，只能通过事件重放恢复。

### Q2: 如何区分止盈和止损单？

**A**: 使用 `BscPerpOrderModel.ClassifyTriggerOrder()` 方法：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
order.ClassifyTriggerOrder()
// 返回: "tp_long", "sl_long", "tp_short", "sl_short", "not_trigger_order"
```

</div>

</div>

**逻辑**:

- **多单止盈**: `isLong=true, triggerAboveThreshold=true` (价格上涨触发)

- **多单止损**: `isLong=true, triggerAboveThreshold=false` (价格下跌触发)

- **空单止盈**: `isLong=false, triggerAboveThreshold=false` (价格下跌触发)

- **空单止损**: `isLong=false, triggerAboveThreshold=true` (价格上涨触发)

### Q3: 为什么 Order 和 Position 事件分离？

**A**:

1.  **职责分离**: Order 管理用户意图，Position 管理实际仓位状态

2.  **数据完整性**: OrderExecuted 不保证包含完整的 Position 数据

3.  **事件可靠性**: PositionIncrease/Decrease 事件是仓位变化的唯一可靠来源

### Q4: 交易手续费如何计算？

**A**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
总费用 = 开平仓手续费 + 资金费 + 借款费 + Swap费用

// Golang
totalFee := positionFee.Add(fundingFee.Abs()).Add(borrowingFee).Add(swapFee)
netPnl := realizedPnl.Sub(totalFee)
```

</div>

</div>

注意：

- **FundingFee** 可以为负（收取资金费），计算总费用时取绝对值

- **BorrowingFee** 总是正数（支付）

- **PositionFee** 开仓和平仓都会收取

### Q5: 如何处理分区表查询？

**A**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 单个用户查询 - 自动路由到正确分区
position, err := positionDAL.GetByPositionKey(ctx, positionKey, account)

// 查询所有用户 - 需要查询所有分区
var allPositions []*bscmodel.BscPerpPositionModel
for i := 0; i < 128; i++ {
    tableName := fmt.Sprintf("bsc_perp_position_%d", i)
    positions, _ := db.Table(tableName).Where("status = ?", "active").Find(&positions).Error
    allPositions = append(allPositions, positions...)
}
```

</div>

</div>

### Q6: EventDataAccessor 如何使用？

**A**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 1. 创建 accessor
accessor := event.NewEventDataAccessor(emitted.EventData)

// 2. 提取字段
account, ok := accessor.Address(consts.BscEventKeyAccount)
sizeUsd, ok := accessor.Uint(consts.BscEventKeySizeDeltaUsd)
isLong, ok := accessor.Bool(consts.BscEventKeyIsLong)
swapPath, ok := accessor.AddressArray(consts.BscEventKeySwapPath)

// 3. 处理可选字段
if triggerPrice, ok := accessor.Uint(consts.BscEventKeyTriggerPrice); ok && triggerPrice != nil {
    order.TriggerPrice = decimal.NewFromBigInt(triggerPrice, 0)
} else {
    order.TriggerPrice = decimal.Zero
}
```

</div>

</div>

### Q7: 如何调试事件解析？

**A**:

1.  **启用详细日志**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
h.Logger().Debug("parsing event",
    zap.String("event_name", evt.Emitted.EventName),
    zap.String("tx_hash", evt.Tx.TxHash),
    zap.Any("event_data", evt.Emitted.EventData),
)
```

</div>

</div>

2.  **使用重放接口**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
curl -X POST http://localhost:9087/api/v1/replay-transaction \
  -H "Content-Type: application/json" \
  -d '{"tx_hash": "0x...", "block_number": 12345678}'
```

</div>

</div>

3.  **检查事件字段**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 打印所有可用字段
for key := range evt.Emitted.EventData.AddressItems {
    h.Logger().Debug("address field", zap.String("key", key))
}
for key := range evt.Emitted.EventData.UintItems {
    h.Logger().Debug("uint field", zap.String("key", key))
}
```

</div>

</div>

------------------------------------------------------------------------

## 附录

### A. 事件处理器列表

<div class="table-wrap">

|                     |                                 |                      |
|---------------------|---------------------------------|----------------------|
| 事件名称            | 处理器                          | 功能                 |
| `MarketCreated`     | `market_created_handler.go`     | 创建 GM Pool         |
| `MarketUpdated`     | `market_updated_handler.go`     | 更新 GM Pool         |
| `GlvPoolCreated`    | `glv_pool_created_handler.go`   | 创建 GLV Pool        |
| `GlvPoolUpdated`    | `glv_pool_updated_handler.go`   | 更新 GLV Pool        |
| `OrderCreated`      | `order_created_handler.go`      | 创建订单             |
| `OrderExecuted`     | `order_executed_handler.go`     | 订单执行             |
| `OrderCancelled`    | `order_cancelled_handler.go`    | 订单取消             |
| `OrderUpdated`      | `order_updated_handler.go`      | 订单更新             |
| `OrderFrozen`       | `order_frozen_handler.go`       | 订单冻结             |
| `PositionIncrease`  | `position_increase_handler.go`  | 开仓/加仓            |
| `PositionDecrease`  | `position_decrease_handler.go`  | 平仓/减仓            |
| `DepositCreated`    | `deposit_created_handler.go`    | 流动性存入（未实现） |
| `WithdrawalCreated` | `withdrawal_created_handler.go` | 流动性取出（未实现） |

</div>

### B. 数据库表列表

<div class="table-wrap">

|                                |      |              |
|--------------------------------|------|--------------|
| 表名                           | 分区 | 用途         |
| `bsc_gm_pools`                 | 无   | GM 市场池    |
| `bsc_glv_pools`                | 无   | GLV 池       |
| `bsc_glv_market_distributions` | 无   | GLV 市场分配 |
| `bsc_perp_order_{0..127}`      | 128  | 订单记录     |
| `bsc_perp_position_{0..127}`   | 128  | 仓位快照     |
| `bsc_perp_trades_{0..127}`     | 128  | 交易历史     |

</div>

### C. 配置文件示例

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# bnb-block-scanner/configs/local-dev.toml

[GMX]
contracts_json = '''
{
  "DataStore": "0x0E5bf50F0Cf2ea2632C6D151F89AE991Cd9E3663",
  "Reader": "0x4D966424F5f2490b3791462132ff90754c09f375",
  "EventEmitter": "0xC8ee91A54287DB53897056e12D9819156D3822Fb",
  "Oracle": "0xa11B501c2dd83Acd29F6727570f2502FAaa617F2"
}
'''
```

</div>

</div>

### D. 相关文档链接

- <a href="https://docs.gmx.io/" class="external-link" rel="nofollow">GMX V2 Synthetics 文档</a>

- <a href="../CLAUDE.md" rel="nofollow">数据统计系统架构文档</a>

- <a href="./gmx_v2_gm_pool_full.md" rel="nofollow">GM Pool 详细文档</a>

- <a href="./gmx_v2_glv_pool_full.md" rel="nofollow">GLV Pool 详细文档</a>

- <a href="../COLLATERAL_TOKEN_FIX.md" rel="nofollow">Position Key 修复文档</a>

------------------------------------------------------------------------

**文档维护**: 如有疑问或发现错误，请联系开发团队或提交 Issue。

</div>
