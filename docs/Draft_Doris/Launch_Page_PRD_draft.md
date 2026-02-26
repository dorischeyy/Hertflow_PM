# Launch Page PRD（草稿）

## 基本信息

| 字段 | 内容 |
|------|------|
| 需求名称 | Launch Page — 无准入市场创建 |
| 文档版本 | v0.1（草稿） |
| 负责人 | @doris |
| 创建日期 | 2026-02-26 |
| 最后更新 | 2026-02-26 |
| 状态 | 草稿 |
| 关联版本 | V2（白名单阶段）→ V3（完全无准入） |

---

## 一、背景与目标

### 1.1 业务背景

Hertzflow 当前支持的交易市场由协议方统一配置，上架新标的需研发介入，创建周期长，无法满足长尾资产（Meme、RWA、Forex 等）的快速上市需求。

Launch Page 旨在让具备资质的第三方用户（V2 白名单阶段）乃至任意用户（V3 无准入阶段），自行创建永续合约交易市场，缩短新市场从 0 到上线的周期，同时通过协议参数约束保障系统安全。

竞品参照：
- **Perennial（Arbitrum）**：完全无准入，任意用户提供 oracle feed + Base/Quote + 费率/杠杆/资金费参数即可建市场
- **dYdX v4**：半无准入，需通过治理提案，提供 Base/Quote/oracle/IMR/MMR/funding 参数，由 LP 提供流动性

### 1.2 核心目标

- 让白名单用户（V2）/任意用户（V3）完成市场创建全流程，无需研发介入
- 新建市场创建成功后，立即在 Trade 页和 Pools 页展示，可正常交易和注入流动性
- 通过参数 floor / ceiling 约束防止恶意参数配置，保障协议安全

### 1.3 成功指标

| 指标 | 目标 |
|------|------|
| 流程完成率 | 进入 Launch Page 的白名单用户，成功创建市场的比例 ≥ 80% |
| 创建耗时 | 从进入页面到交易上线 ≤ 5 分钟 |
| 上链成功率 | 提交创建交易后，成功出块率 ≥ 99% |

---

## 二、用户与场景

### 2.1 目标用户

| 阶段 | 用户类型 | 准入方式 |
|------|----------|----------|
| V2（当前）| 白名单地址（BD 对接的做市商、合作方等） | 链上白名单地址校验 |
| V3（规划）| 任意持有足够保证金的用户 | 无准入 |

**用户特征：**
- 有明确的标的资产需求，希望快速建立交易市场
- 具备基本 DeFi 经验，理解保证金、杠杆、清算等基本概念
- 有能力提供初始流动性以启动市场

### 2.2 核心场景

**场景一：做市商为新 Meme 代币创建市场**

> 某做市商持有白名单地址，发现某 Meme 代币已有 Pyth 预言机 Feed，希望在 Hertzflow 快速建立该代币的永续合约市场，并提供初始 LP。进入 Launch Page，选择预言机 → 配置参数 → 支付保证金 → 注入初始流动性 → 创建成功后市场立即在 Trade 页上线。

**场景二：RWA / Forex 标的上市（V3）**

> 任意用户为某 RWA 标的（黄金、外汇等）选择 Chainlink Feed 作为预言机，配置保守参数（低杠杆、高 MMR），支付保证金并启动市场。

---

## 三、需求详述

### 3.1 功能列表

| 功能模块 | 功能描述 | 优先级 |
|----------|----------|--------|
| 准入校验 | 连接钱包时检测是否为白名单地址，非白名单不展示入口 | P0 |
| 市场基础参数配置 | 选择 Base Asset、Quote Asset、Market Symbol、Oracle Feed | P0 |
| 交易行为参数配置 | 配置 Max Leverage、MMR | P0 |
| 流动性池参数配置 | 配置 Collateral Tokens、Initial Liquidity、Liquidity Cap、Target Weightage | P0 |
| 费率参数配置 | 配置 Open/Close Position Fee、Liquidation Fee、Swap Fee | P0 |
| 保证金支付 | 用户支付创建市场所需保证金（协议设定固定金额）| P0 |
| 初始流动性注入 | 用户存入初始 LP，为市场提供启动流动性 | P0 |
| 创建确认与上链 | 汇总参数展示，用户确认后提交链上交易 | P0 |
| 风控参数配置 | 配置 Max OI、Skew Limit、Max Position Size、Max Limit Orders（V3） | P1 |
| 权限配置 | 配置 Operator 地址、Fee Recipient 分成比例（V3） | P1 |
| 已创建市场管理 | 市场创建者可查看、编辑已建市场的可更新参数 | P2 |
| 市场标签 & disable | 为市场添加分类标签；支持市场 disable 处理（V3）| P2 |

### 3.2 详细说明

#### 3.2.1 准入校验

**正常流程：**
1. 用户连接钱包（Slush / Suiet / OKX）
2. 前端调用白名单合约，验证当前地址是否在白名单中
3. 白名单地址：顶部导航栏展示「Launch」入口
4. 非白名单地址：不展示「Launch」入口（页面直接 URL 访问时跳转至 403/提示页）

**异常流程：**
- 白名单合约查询失败：隐藏入口，兜底展示「功能暂不可用」提示

---

#### 3.2.2 市场基础参数配置

| 参数 | 说明 | 输入方式 |
|------|------|----------|
| Base Asset | 标的资产（crypto、Meme、RWA 等） | 下拉搜索，从预言机支持的资产列表中选择 |
| Quote Asset | 计价资产（USDC / USDT） | 下拉选择，当前仅支持稳定币 |
| Market Symbol | 自动生成，格式 `Base/Quote`，如 `ETH/USDC` | 只读展示 |
| Oracle | 对应 Base Asset 的预言机 Feed | 选择 Base Asset 后自动匹配，支持 Pyth（主）+ Chainlink（备） |

**Oracle 校验规则（需研发确认）：**
- Feed ID 必须存在且喂价频率满足协议最低要求
- 最大价格偏差（Staleness Threshold）在协议允许范围内
- [TBD - engineering to confirm] 具体校验参数

---

#### 3.2.3 交易行为参数配置

| 参数 | 说明 | 约束 |
|------|------|------|
| Max Leverage | 开仓可用最大杠杆 | ≤ 100x（前端限制）；协议支持最高 200x |
| MMR（维持保证金率） | = 1 / Max Maintenance Leverage，低于此值触发清算 | ≥ 0.2%（协议最小值） |

**建议**：为非专业用户提供预设档位（如 10x / 25x / 50x / 100x），高级模式允许手动输入。

---

#### 3.2.4 费率参数配置

| 参数 | 说明 | 约束 |
|------|------|------|
| Open Position Fee Rate | 开仓手续费 | floor ≤ 用户设置 ≤ ceiling（协议设定） |
| Close Position Fee Rate | 平仓手续费 | floor ≤ 用户设置 ≤ ceiling |
| Liquidation Fee Rate | 清算费，补偿 Keeper 和 LP | 协议设定，暂不开放自定义 |
| Swap Fee Rate（稳定币） | 稳定币互换费 | 参照全局默认 4 bps，可调 |
| Swap Fee Rate（非稳定币） | 非稳定币互换费 | 参照全局默认 30 bps，可调 |

> 参考当前协议默认费率：开平仓 6 bps；清算 20 bps（来自 CLAUDE.md）

---

#### 3.2.5 流动性池参数配置

| 参数 | 说明 | 约束 |
|------|------|------|
| Collateral Tokens | 池子接受的抵押资产 | 支持稳定币 + 白名单非稳定币 |
| Initial Liquidity Amount | 创建者注入的初始 LP 金额（USD） | ≥ 协议最低启动资金（[TBD]） |
| Liquidity Cap | 硬上限，超出后禁止新增流动性 | 需 ≥ Initial Liquidity |
| Target Weightage | 多资产池目标权重 | 所有 Token 权重之和 = 100% |

**建议**：提供预设模版（参照 dYdX Liquidity Tiers），降低配置门槛。

---

#### 3.2.6 创建流程（主链路）

```
进入 Launch Page
  ↓
Step 1：填写市场基础参数（Base/Quote/Oracle）
  ↓
Step 2：配置交易参数（Leverage/MMR/费率）
  ↓
Step 3：配置流动性参数（抵押资产/初始 LP/上限）
  ↓
Step 4：汇总预览（所有参数 Review + 预估费用）
  ↓
用户确认 → 支付保证金 → 注入初始流动性 → 提交链上交易
  ↓
等待交易确认（loading 状态）
  ↓
成功 → Toast 提示「市场创建成功」→ 跳转至新市场的 Trade 页
失败 → 错误提示 + 允许重试
```

---

#### 3.2.7 创建成功后联动

- **Trade 页**：市场出现在 Market List 和 Market Carousel 中，可正常交易
- **Pools 页**：对应 Pool 自动生成，`pool_name = HzLP: [Market Symbol]`，刷新一次后展示
- **Pools 后端**：需支持 launch market 管理，便于后续运营操作

---

### 3.3 边界与异常

| 场景 | 处理方式 |
|------|----------|
| 钱包未连接 | 不展示 Launch 入口，引导连接钱包 |
| 非白名单地址 | 隐藏入口；直接 URL 访问时展示无权限提示 |
| Oracle Feed 不合法 | 选择后实时校验，不合法时展示错误说明，禁止下一步 |
| 参数超出协议约束 | 输入框实时红色提示，展示允许范围，禁止提交 |
| 初始流动性不足 | 提示最低要求金额 |
| 链上交易失败 | 展示失败原因（钱包拒绝 / Gas 不足 / 合约 revert），保留已填参数，允许重试 |
| 相同 Market Symbol 已存在 | 提交前检测，提示市场已存在 |

---

## 四、UI/UX 设计

### 4.1 页面结构（建议）

```
Launch Page
├── Header：页面标题 + 简介（Create a New Market）
├── Step Indicator：1 → 2 → 3 → Review（步骤进度条）
├── Step 1：Market Info
│   ├── Base Asset 下拉搜索
│   ├── Quote Asset 下拉选择
│   ├── Oracle（自动匹配 + 可手动覆盖）
│   └── Market Symbol（只读预览）
├── Step 2：Trading Parameters
│   ├── Max Leverage（预设档位 + 自定义）
│   ├── MMR（只读 or 联动 Leverage 自动计算）
│   └── Fee Rates（Open / Close / Liquidation / Swap）
├── Step 3：Liquidity Setup
│   ├── Collateral Token 选择
│   ├── Initial Liquidity 金额输入
│   ├── Liquidity Cap 输入
│   └── Target Weightage 配置
└── Step 4：Review & Create
    ├── 所有参数汇总展示
    ├── 预计 Gas 费 + 保证金费用明细
    └── [Create Market] 主 CTA 按钮
```

### 4.2 交互说明

- 步骤间支持前后导航，已填参数不丢失
- 每步完成校验后方可进入下一步
- Review 页任意参数支持点击跳回对应 Step 修改
- 创建中展示 Loading + 链上交易哈希链接（跳转区块浏览器）
- 原型图待设计侧（@hanyang / @avery）提供后补充

---

## 五、技术说明

### 5.1 接口需求

| 接口 | 说明 | 负责方 |
|------|------|--------|
| 白名单地址校验 | 查询当前钱包地址是否在白名单合约中 | 合约 / 后端 |
| Oracle Feed 列表 | 返回当前协议支持的预言机 Feed 及对应资产信息 | 后端 |
| 协议参数约束查询 | 返回各参数的 floor/ceiling 值 | 后端 / 合约 |
| 创建市场（链上） | PTB 原子交易，包含保证金支付 + 初始 LP 注入 + 市场创建 | 合约 |
| Pools 刷新 | 市场创建成功后触发 Pools 列表刷新 | 后端 |

### 5.2 合约说明

- **SUI 链**：使用 Move PTB（Programmable Transaction Block）原子执行：保证金划转 + LP 注入 + 市场创建，三步原子化，任一失败全部回滚
- **BNB Chain（V3）**：使用 Solidity，无需 Keeper 推单，后端可直接从链上事件获取状态
- 新增市场标的前，需确认：Pyth / Chainlink Feed ID、合约最大杠杆配置、池子权重分配

### 5.3 兼容性

- PC 优先，H5 同步支持
- 钱包：Slush / Suiet / OKX（SUI）；MetaMask / OKX（BNB Chain V3）

---

## 六、非功能性需求

| 类型 | 要求 |
|------|------|
| 性能 | 参数校验实时响应 < 300ms；链上交易提交后 loading 反馈 < 1s |
| 安全 | 参数范围在合约层二次校验，前端校验不作为唯一防线；白名单合约地址需审计 |
| 可用性 | 创建流程中途刷新，已填参数本地缓存保留（localStorage） |

---

## 七、上线计划

| 阶段 | 内容 | 预计时间 |
|------|------|----------|
| 研发（V2 白名单） | 前端 Launch Page + 合约集成 + 后端接口 | 前端 1 周（参见 V1 排期） |
| 测试 | 功能测试 + 链上集成测试 | 待排 |
| 灰度 | 仅白名单地址可访问，监控创建成功率 | 待排 |
| V3 全量 | 去掉白名单限制，开放无准入创建 | V3 规划阶段 |

---

## 八、遗留问题

| 问题 | 负责人 | 状态 |
|------|--------|------|
| 创建市场所需保证金金额（协议设定值是多少？） | @soren 0x / @novax 0x | 待确认 |
| Oracle Feed 的校验标准（staleness threshold、最低喂价频率） | @soren 0x | 待确认 |
| 各费率参数的 floor / ceiling 值 | 合约侧 | 待确认 |
| 流动性池参数：是否与 HzLP 共用，还是独立池子？ | @soren 0x | 待确认 |
| 白名单合约地址 & 校验接口 | @dennis / @kayce | 待确认 |
| 初始流动性最低金额限制 | 合约侧 | 待确认 |
| V3 Operator / Fee Recipient 权限设计细节 | 合约侧 | 待排 |

---

## 九、变更记录

| 版本 | 修改内容 | 修改人 | 日期 |
|------|----------|--------|------|
| v0.1 | 初稿，基于 V1需求排期、竞品调研报告、功能记录整合 | @doris | 2026-02-26 |

---

> **数据来源说明**
> 本草稿整合自以下文档，正式评审前需与研发侧核对标注 [TBD] 的技术参数：
> - `docs/项目组周报汇总/V1需求排期.md` — Launch Page 原始需求描述
> - `docs/项目组周报汇总/功能记录（V1.0.0）.csv` — V3 功能范围
> - `docs/Research Report/Research_permissionless+market+creation.md` — 竞品调研（Perennial / dYdX）
> - `docs/PRD_V2/Trade+Page_PRD.md` / `Pools+Page_PRD.md` — 联动模块约束
