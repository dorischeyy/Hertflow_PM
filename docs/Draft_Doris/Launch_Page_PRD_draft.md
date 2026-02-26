# Launch Page PRD（草稿）

## 基本信息

| 字段 | 内容 |
|------|------|
| 需求名称 | Launch Page — 无准入市场创建 |
| 文档版本 | v0.2（草稿） |
| 负责人 | @doris |
| 创建日期 | 2026-02-26 |
| 最后更新 | 2026-02-26 |
| 状态 | 草稿 |
| 关联版本 | V2（白名单阶段）→ V3（完全无准入） |

> **说明**：本草稿内容 100% 来源于已有文档，来源注释标注在各节末尾。未有记录的内容统一标注「待补充」，不做推断性填写。

---

## 一、背景与目标

### 1.1 业务背景

当前产品支持的交易市场由协议方统一配置，Launch Page 旨在让白名单用户（V2 阶段）或任意用户（V3 阶段）无需研发介入，自行创建永续合约交易市场，覆盖 crypto、Meme、RWA、Forex 等长尾标的。

> 来源：`docs/项目组周报汇总/V1需求排期.md`、`docs/测试网相关整理/Product+Docs.md`

### 1.2 核心目标

- 白名单用户（V2）可通过 Launch Page 完成无准入市场创建全流程
- 创建成功后市场立即在 Trade 页展示，可正常交易

> 来源：`docs/项目组周报汇总/V1需求排期.md`

### 1.3 成功指标

待补充（现有文档无量化指标记录）

---

## 二、用户与场景

### 2.1 目标用户

| 阶段 | 准入方式 |
|------|----------|
| V2（当前）| 白名单钱包地址，连接 BSC 测试网时识别 |
| V3（规划）| 无准入，任意用户 |

> 来源：`docs/项目组周报汇总/V1需求排期.md`（Wallet Connect 章节：「链接BSC测试网，支持白名单钱包地址识别。针对白名单地址，比普通用户多展示一个 Launch 无准入创建市场页面」）

### 2.2 核心场景

待补充（现有文档无用户场景描述）

---

## 三、需求详述

### 3.1 功能列表

以下来源于 `docs/项目组周报汇总/V1需求排期.md` Launch Page 章节：

| 功能 | 描述 | 优先级 |
|------|------|--------|
| 准入控制 | 仅白名单地址可访问 | P0 |
| 市场 & 预言机选择 | 无准入建池，市场和预言机通过下拉栏选择 | P0 |
| 参数自定义 | 用户可自定义市场参数 | P0 |
| 保证金支付 + 初始流动性 | 支付保证金并注入初始流动性以创建市场 | P0 |
| 创建后 Trade 页展示 | 创建市场成功后，市场在 Trade 页展示 | P0 |

以下来源于 `docs/项目组周报汇总/功能记录（V1.0.0）.csv`，V3 阶段（P2）：

| 功能 | 描述 | 优先级 |
|------|------|--------|
| 无准入市场创建 | V3 去掉白名单限制 | P2 |
| 预言机选择 | — | P2 |
| 风控参数自定义 | — | P2 |
| 市场权衡指标 | 市场新增权衡指标 | P2 |
| 市场标签 | — | P2 |
| Disable 处理 | 市场 disable 状态管理 | P2 |

### 3.2 可配置参数（来源：竞品调研报告）

以下参数体系整理自 `docs/Research Report/Research_permissionless+market+creation.md`，为 Hertzflow 参数梳理章节的原始记录，各字段的协议约束值需研发确认。

#### 市场基础参数

| 参数 | 说明 | 约束/备注 |
|------|------|-----------|
| Base Asset | 标的资产（cryptos、Memes、RWA tokens 等） | — |
| Quote Asset | 计价资产（USDC/USDT/其他稳定币） | — |
| Market Symbol | `Base Asset`/`Quote Asset`，如 ETH/USDC | 自动生成 |
| Oracle | 支持哪些预言机、喂价频率要求、最大价格偏差（on-chain 校验延迟）| 待研发确认具体校验标准 |

#### 交易行为参数

| 参数 | 说明 | 约束 |
|------|------|------|
| Max Leverage | 开仓可用最大杠杆 | ≤ 100（前端限制）；协议支持 ≤ 200 |
| MMR | 维持保证金率 = 1 / Max Maintenance Leverage，低于此值触发 Keeper 强平 | ≥ 0.2%（协议设定值）|

> 协议默认：Max Leverage 100x，MMR 0.2%（来源：`CLAUDE.md`）

#### 流动性池参数（假定不与 HzLP 共用流动性）

| 参数 | 说明 |
|------|------|
| Collateral Tokens | 池子支持的抵押资产（Stable + Non Stable Collaterals）|
| Initial Liquidity Amount | 启动资金 |
| Liquidity Cap | 硬上限，超出后不再支持添加新流动性 |
| Target Weightage | 目标权重，启动时 Current Weightage 初始值配成目标权重 |

> 注：「假定不与 HzLP 共用流动性」为调研报告原文标注，是否共用待产品 & 研发确认。

#### 费用参数（假定不与 HzLP 共用流动性）

| 参数 | 说明 | 约束 |
|------|------|------|
| Swap Fee Rate（稳定币）| — | floor ＜ 用户设置值 ＜ ceiling |
| Swap Fee Rate（非稳定币）| — | floor ＜ 用户设置值 ＜ ceiling |
| Open Position Fee Rate | — | ＜ 协议设置的硬上限 |
| Close Position Fee Rate | — | ＜ 协议设置的硬上限 |
| Liquidation Fee Rate | 补偿 Keeper 及 LP | — |

> 协议当前默认费率：开平仓 6 bps；清算 20 bps；Swap（稳定币）4 bps；Swap（非稳定币）30 bps（来源：`CLAUDE.md`）

#### 风控参数（建议与协议机制绑定，非用户自定义）

| 参数 | 说明 | 约束/备注 |
|------|------|-----------|
| Max OI | 单个市场单边允许最大未平仓限制 | — |
| Skew Limit | \| OI_Long − OI_Short \| / Total OI 可容许最大偏差比值 | — |
| Max Position Size | 单个钱包地址下最大仓位大小 | 参考 Avantis 做法：＜ 15% OI_symbol |
| Max Limit Orders | 单个钱包地址下单市场 open orders 个数上限 | floor ＜ 用户设置 ＜ ceiling；当前设定 20 |
| Insurance Fund Size | 用于覆盖 bad debt | 参考值：10% AUM |

#### 权限

| 参数 | 说明 |
|------|------|
| Operator | 是否可更新已定参数及更新范围 |
| Fee Recipient | 手续费分成比例（admin / LP / protocol）|

### 3.3 创建流程

以下为 `docs/项目组周报汇总/V1需求排期.md` 原文描述，未做扩展：

1. 市场 & 预言机选择（下拉栏）
2. 参数自定义
3. 支付保证金；注入初始流动性并创建市场
4. 创建市场成功后，Trade 页展示

具体步骤设计、交互流程、异常处理待 PM & 设计确认。

---

## 四、UI/UX 设计

待设计侧（@hanyang / @avery）提供原型后补充。

---

## 五、技术说明

### 5.1 与其他模块的联动

**Trade 页：**
- Market Carousel 后期 launch 页面开发时有可能变成推荐位，届时需后端提供数据支持

> 来源：`docs/PRD_V2/Trade+Page_PRD.md`

**Pools 页：**
- Pool List 由后端维护，后续涉及 launch market 方便管理
- `pool_name = HzLP: [Market Symbol]`，Market Symbol 用于搜索字段
- launch 成功后 Pool List 刷新一次

> 来源：`docs/PRD_V2/Pools+Page_PRD.md`

### 5.2 合约说明

新增市场标的前，需确认：预言机 Feed ID、合约侧最大杠杆配置、权重分配。

SUI 链使用 Move 合约 + PTB 原子交易。

> 来源：`CLAUDE.md`

### 5.3 接口需求

待研发确认后补充。

---

## 六、非功能性需求

待补充（现有文档无相关记录）

---

## 七、上线计划

| 阶段 | 内容 | 预计时间 |
|------|------|----------|
| 研发（V2 白名单）| 前端 Launch Page | 前端 1 周（来源：V1需求排期）|
| 研发（后端 / 合约）| 待排 | — |
| 测试 | 待排 | — |
| V3 全量 | 去掉白名单限制，开放无准入 | V3 规划阶段 |

---

## 八、遗留问题

| 问题 | 负责人 | 状态 |
|------|--------|------|
| 流动性池是否与 HzLP 共用，还是每个市场独立池子？ | 待产品 & 研发确认 | 待确认 |
| Oracle 校验标准（staleness threshold、最低喂价频率） | 合约侧 | 待确认 |
| 各费率参数的 floor / ceiling 具体值 | 合约侧 | 待确认 |
| 创建市场所需保证金金额 | 合约侧 | 待确认 |
| 白名单合约地址 & 校验接口 | 后端 | 待确认 |
| 风控参数是否对用户开放自定义，还是协议固定 | 产品 & 合约侧 | 待确认 |
| V3 Operator / Fee Recipient 权限设计细节 | 合约侧 | 待排 |

---

## 九、竞品参考

来源：`docs/Research Report/Research_permissionless+market+creation.md`

| 协议 | 是否支持用户自行 Launch Market | 机制 |
|------|-------------------------------|------|
| Perennial（Arbitrum）| ✅ 完全 permissionless | 任何人提供 oracle feed + Base/Quote + fee/leverage/funding 参数即可创建；市场有独立 operator 及 risk coordinator（multisig + timelock）|
| dYdX v4 | ❌ 半 permissionless | 需通过治理提案，提供 Base/Quote/oracle/IMR/MMR/funding 参数；风控参数根据 liquidity tier 自动计算，不可更改 |

---

## 十、变更记录

| 版本 | 修改内容 | 修改人 | 日期 |
|------|----------|--------|------|
| v0.1 | 初稿（含推断性内容）| @doris | 2026-02-26 |
| v0.2 | 删除无文档依据内容，仅保留有记录的信息，空白处标注「待补充」| @doris | 2026-02-26 |

---

> **文档来源索引**
> - `docs/项目组周报汇总/V1需求排期.md` — Launch Page 原始需求（准入、建池、参数、保证金、上链流程）
> - `docs/项目组周报汇总/功能记录（V1.0.0）.csv` — V3 功能范围（P2）
> - `docs/Research Report/Research_permissionless+market+creation.md` — 参数体系 + 竞品调研
> - `docs/PRD_V2/Trade+Page_PRD.md` — Carousel 联动说明
> - `docs/PRD_V2/Pools+Page_PRD.md` — Pool List 联动说明
> - `CLAUDE.md` — 协议默认费率、合约技术说明
