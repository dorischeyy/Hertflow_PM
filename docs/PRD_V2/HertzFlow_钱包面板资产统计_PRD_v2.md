**HertzFlow**

**钱包面板资产统计 PRD**

v2.0 \| 2026-02-25

**1. 概述**

当前钱包面板仅显示 USDT 可用余额，未统计 Pools、Vaults、持仓及挂单中的资产。本需求将钱包面板升级为全站资产总览，显示 Total Assets（USD）、Total PnL、Unrealised PnL，并在 Portfolio / Activity 两个标签页中展示持仓、订单、池子、金库及操作历史。

**可扩展性**

当前资产来源为 5 类（USDT Balance / Pools / Vaults / Positions / Orders）。架构设计上，Total Assets 采用“求和各资产源 valueUsd”的模式。未来新增资产类型（如 Staking、Lending、NFT 等）只需：

- 注册新的资产源（提供 name / valueUsd / color）

- Total Assets 自动累加，分布条自动新增对应色段

- Portfolio 标签页新增对应折叠区块

无需修改核心计算逻辑。PnL 体系同理：新资产类型的 unrealised/realised 分别注入对应公式的求和项即可。

**2. Total Assets**

**计算公式**

> Total Assets = USDT Balance + Σ Pool Value + Σ Vault Value + Σ Position Net Value + Σ Order Collateral

**各分项数据来源**

| **分项** | **计算** | **数据来源** |
|----|----|----|
| USDT Balance | 用户 USDT 可用余额 | 钱包合约 balanceOf |
| Pool Value | Your Deposits + Earned Fees，每个 HzLP Pool 求和 | Pools 合约 getUserInfo |
| Vault Value | Your Deposits + Your Earnings，每个 Vault 求和 | Vaults 合约 getUserInfo |
| Position Net Value | Collateral + uPnL − Pending Fees，每个 Open Position 求和 | Perps Engine getOpenPositions |
| Order Collateral | 挂单占用抵押品总和 | Order Book getOpenOrders |

**显示**

- **标题：**TOTAL ASSETS（不带 (USD)，\$ 已表达币种）

- **数值：**\$X,XXX.XX，36px 粗体白色

- **Tooltip（ⓘ）：**USDT Balance + Pools + Vaults + Positions (collateral + uPnL − fees) + Pending Order Collateral

**USDT Balance 独立展示**

在 Total Assets 下方单独展示 USDT 原始余额（如 1,000.35 USDT）及其 USD 等值（≈ \$1,000.35），区分“全站总值”与“钱包现金”。

**资产分布条**

分段进度条 + 图例，按占比显示各资产类别。值为 0 的类别图例降为 35% 不透明度，进度条不显示该段。颜色编码与 dashboard 保持一致，由设计确认。

**3. PnL 盈亏**

**Total PnL**

> Total PnL (\$) = Unrealised PnL + Realised PnL
>
> Total PnL (%) = Total PnL (\$) / Total Bought × 100%

**Total Bought** = 用户历史所有投入本金总额，来源于 Event Indexer 聚合。

**Tooltip：**Total PnL (\$) = Unrealised + Realised PnL；Total PnL (%) = Total PnL / Total Bought

**Unrealised PnL**

> Unrealised PnL (\$) = Positions uPnL + Pools uPnL + Vaults uPnL

- **Positions uPnL** = Σ (position_uPnL − pending_fees)，来源 Perps Engine。

- **Pools uPnL** = Σ earned_fees（未提取的手续费收益），来源 Pools 合约。

- **Vaults uPnL** = Σ your_earnings（未提取的 vault 收益），来源 Vaults 合约。

> Cost Basis = Σ position_collateral + Σ pool_deposits + Σ vault_deposits
>
> Unrealised PnL (%) = Unrealised PnL (\$) / Cost Basis × 100%

**Tooltip：**Unrealised PnL (\$) = Profit/loss on current balance relative to cost basis

**Realised PnL**

不在面板上单独展示，作为 Total PnL 的计算输入。

> Realised PnL = Σ closed_position_pnl + Σ withdrawn_pool_fees + Σ withdrawn_vault_earnings

数据来源：Event Indexer 中历史 Activity 记录的 PnL 字段求和。

**显示规范**

正值绿色 (#10B981)，负值红色 (#EF4444)。格式：+\$XX.XX / -\$XX.XX，百分比 +XX.XX% / -XX.XX%，统一 2 位小数。Cost Basis 或 Total Bought 为 0 时对应 % 显示 0.00%。

**4. Portfolio**

四个可折叠区块，默认全展开。无数据时显示空状态（虚线框 + 图标 + 引导文案）。

**Positions**

数据来源：Perps Engine getOpenPositions。

| **字段** | **说明** | **来源字段** |
|----|----|----|
| Symbol + Leverage + Side | 如 XAU/USD 51.5x Long，Side 绿/红标签 | symbol / leverage / isLong |
| Size | 仓位规模 (\$) | size |
| Net Value | 净值 = Collateral + uPnL − Fees | netValue |
| uPnL | 未实现盈亏，含绝对值和百分比，红绿色 | unrealisedPnl / unrealisedPnlPct |

**Orders**

数据来源：Order Book getOpenOrders。

| **字段**             | **说明**              | **来源字段**                |
|----------------------|-----------------------|-----------------------------|
| Symbol + Type + Side | 如 BTC/USD Limit Long | symbol / orderType / isLong |
| Size                 | 订单规模 (\$)         | size                        |
| Price                | 触发价格              | triggerPrice                |

**Pools**

数据来源：Pooling 合约 getUserInfo。

| **字段**      | **说明**                       | **来源字段** |
|---------------|--------------------------------|--------------|
| Pool Name     | 如 HzLP: XAU/USD               | poolName     |
| Your Deposits | 用户在该 Pool 的存款           | userDeposits |
| Earned Fees   | 累计赚取的手续费，绿色 +\$X.XX | earnedFees   |

**Vaults**

数据来源：Vault 合约 getUserInfo。

| **字段** | **说明** | **来源字段** |
|----|----|----|
| Vault Name + APY | 如 HertzFlow Bluechip Crypto，APY 绿色标签 | vaultName / apy |
| Your Deposits | 用户存入金额 | userDeposits |
| Your Earnings | 累计收益，绿色 +\$X.XX | userEarnings |

**5. Activity**

纯时间线列表，按时间倒序，无筛选。数据来源：Event Indexer API。

**单条记录布局（三行卡片）**

| **行** | **内容** | **说明** |
|----|----|----|
| 第一行 | Asset 图标 + 名称 + Action 标签（含 Side）+ ⇗ | 如 🥇 XAU \[Market Open Long\] ⇗ |
| 第二行 | Size / Price / PnL | 三列网格；无 PnL 时两列；deposit/withdrawal 无 Price 时一列 |
| 第三行 | 完整时间戳 | YYYY/MM/DD HH:MM:SS |

**字段规则**

| **字段** | **规则** | **来源字段** |
|----|----|----|
| Action 标签 | 显示 Action + Side，如 "Market Open Long" "Liquidated Long" | actionType + side |
| Size | 开仓/加仓/入金显示 +\$，平仓/减仓/清算/出金显示 -\$ | size |
| Price | 执行价格，仅交易类记录显示 | executionPrice |
| PnL | 仅 close/liquidated/TP/SL 类记录显示，红绿色 | realisedPnl |
| Timestamp | 完整时间 YYYY/MM/DD HH:MM:SS | timestamp |
| ⇗ | 跳转区块浏览器交易详情 | txHash |

**订单类型枚举**

| **类别** | **Actions** |
|----|----|
| market | Market Open / Market Close / Market Increase / Market Decrease / Deposit / Withdrawal 及对应 Failed |
| limit | Limit Open / Limit Created / Limit Updated / Limit Cancelled / Failed Limit |
| take_profit | Take Profit (close) / TP Decrease / TP Created / TP Updated / TP Cancelled |
| stop_loss | Stop Loss (close) / SL Decrease / SL Created / SL Updated / SL Cancelled |
| liquidated | Liquidated |

**6. 边界情况**

| **场景** | **处理** |
|----|----|
| 未连接钱包 | 所有数值显示 \$0.00，引导连接 |
| 某接口失败 | 已加载部分正常显示，失败部分显示 “—” + Retry |
| 所有模块为空 | Total Assets = USDT Balance，各区块显示空状态 |
| Cost Basis / Total Bought = 0 | 对应 PnL % 显示 0.00%，避免除以零 |
| 历史记录为空 | Activity 列表显示空状态 |

**7. UI 规范**

- 数值统一 2 位小数 + 千分位分隔符

- Tooltip：Hover/Click 触发，鼠标可移入浮层复制文字（150ms 延迟关闭），向下弹出

- ⓘ 图标：16px 圆形底色 + border，保证点击区域可见

- 折叠区块默认全展开，数量徽章有数据时紫色、无数据时暗色

- 颜色体系与 dashboard 保持一致，具体色值由设计确认

- 字段名称全站统一：Size / Net Value / uPnL / Your Deposits / Earned Fees / Your Earnings 等与 Trade、Pools、Vaults 页保持一致

**8. 数据流**

钱包连接后并行拉取各数据源，前端计算 Total Assets / PnL，后续通过 WebSocket 增量更新。

| **数据** | **接口** | **更新频率** |
|----|----|----|
| USDT Balance | 钱包合约 balanceOf | 实时 / WebSocket |
| Pools | Pools 合约 getUserInfo | 实时 |
| Vaults | Vaults 合约 getUserInfo | 实时 |
| Positions | Perps Engine getOpenPositions | 实时 / 5s 轮询 |
| Orders | Order Book getOpenOrders | 实时 |
| Activities / Realised PnL / Total Bought | Event Indexer API | 增量拉取 |

**9. 后续规划**

- Pool IL（Impermanent Loss）计算纳入

- Vault HzV Token 折算精度优化

- PnL 历史图表（时间线盈亏曲线）

- 新资产类型接入（Staking / Lending 等）

- 多钱包支持

— End of Document —
