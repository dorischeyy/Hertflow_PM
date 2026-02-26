# Hertzflow · Claude 协作指令

> **使用说明**：本文件是 Claude 的核心上下文，每次对话自动加载。PM 可直接描述需求，Claude 会结合本文件 + `docs/` 目录里的文档，输出 PRD、周报、月报等内容。团队成员共同维护此仓库，文档即真相。

---

## 一、项目背景

**Hertzflow** 是一个 Web3 去中心化永续合约交易所（Perp DEX），对标 GMX / Jupiter / Hyperliquid。

| 维度 | 说明 |
|------|------|
| 公链 | SUI Testnet（V1/V2）→ BNB Chain（V3 扩展） |
| 当前阶段 | V1 已上测试网，V2 开发中，V3 规划中 |
| 核心用户 | 加密货币交易者（Trade 侧）+ 流动性提供者（Pools 侧） |
| 核心差异 | 超高杠杆模式、虚拟资产标的（RWA/Forex）、Permission-less 市场创建 |
| 竞品参考 | GMX（gmx-io/gmx-synthetics）、Jupiter、Hyperliquid |

---

## 二、产品模块全览

### 2.1 Trade（永续合约交易）

**核心规则：**
- 支持市价单 / 限价单 / 触发单（TP/SL）
- 多空双向，杠杆 1.1x–100x（测试网）
- 每个仓位**独立计息、独立清算**，无交叉保证金风险
- 标的资产：BTC / ETH / SUI / RWA（V2+）/ Forex / Commodities（V3+）
- EVM 与 SUI 唯一产品差异：**EVM 无需 Keeper 推送订单**，后端可直接从链上事件获取状态

**关键参数（测试网）：**

| 参数 | 值 |
|------|----|
| 最小保证金 | $10 USD |
| 最大杠杆 | 100x（Max Open Leverage: 200） |
| 单市场单向最大仓位 | $10,000 |
| 最大维持杠杆 | 500（MMR = 0.2%） |
| 开平仓手续费 | 6 bps |
| 清算手续费 | 20 bps |
| 协议分润 | Protocol 25% / LP 75% |
| Swap 基础费（非稳定币）| 30 bps + 150 bps 价格影响 |
| Swap 基础费（稳定币）| 4 bps + 20 bps 价格影响 |

**核心公式：**
```
未实现盈亏（多）= (Mark - Entry) / Entry × Leverage × 100%
未实现盈亏（空）= (Entry - Mark) / Entry × Leverage × 100%

清算价格 = Entry × (1 ± 1/Leverage ∓ 1/Max_Maintenance_Leverage)

TP Price Cap = Entry × [1 ± (25 × Collateral - Fees) / Size]
SL Price Cap = Entry × [1 ± (-0.8 × Collateral - Fees) / Size]

借贷费 = (最新累计资金费率 - 开仓时资金费率) × Position Size
资金费率增量 = Δt(小时) × funding_fee_rate
```

### 2.2 Pools / HzLP（流动性池）

**核心规则：**
- V1 多资产池目标权重：SUI 35% / USDC 40% / ETH 15% / BTC 10%
- V2 新增纯 USDC 池
- LP 收益 = 交易者亏损 + 75% 协议手续费
- HzLP 定价：`HzLP Price = 池子总质押 / HzLP 总供应量`
- Max AUM Cap：$500,000（测试网），达到上限后禁止新 Mint
- 权重偏差 δ% > 20% → 限制该方向 Mint/Borrow
- δ% > 2000 bps → 拒绝操作

**⚠️ 重要原则**：Trade 收藏（Favorite）与 Pool 收藏必须**解耦**，两者用户动机不同，需为多资产池预留扩展性。

### 2.3 Vault（金库）

- 用户存入资产获得 HzLP 份额，添加/移除费：30 bps 基础 + 动态价格影响
- V2：Vault 与 Pools 页面整合优化，新增自动路由存取逻辑

### 2.4 Dashboard（数据看板）

- 全平台：交易量、持仓量、手续费收入
- 用户个人：PnL、胜率、历史记录
- Leaderboard 排行榜（V2）、Referral 推荐数据（V2+）

### 2.5 Keeper（链下执行节点）

- 职责：订单执行、清算触发、资金费率结算、喂价
- **三级优先级架构**：Master(0s) → Backup-1(30s) → Backup-2(60s)，高可用故障转移
- 预言机：Pyth（主，<1s 延迟）+ Chainlink（备）+ CEX 备用

---

## 三、版本迭代上下文

| 版本 | 状态 | 核心目标 |
|------|------|----------|
| V1 | ✅ 测试网已上线 | PC/H5 交易闭环、HzLP 流动性、基础 Dashboard |
| V2 | 🔧 开发中 | 超高杠杆、纯 USDC 池、Referral、TP/SL 优化、Dashboard 增强 |
| V3 | 📋 规划中 | BNB Chain、Permission-less 市场、RWA/Forex 标的 |

**V2 重点需求文档索引（`docs/PRD_V2/`）：**
- `Trade+超高杠杆模式_PRD.md` — 超高杠杆核心逻辑
- `TP_SL核心逻辑说明文档.md` — TP/SL 价格上下限规则
- `HertzFlow_钱包面板资产统计_PRD_v2.md` — 钱包面板重构
- `Dashboard_PRD.md` — Dashboard 增强
- `Vault+页面优化_PRD.md` / `Pools+Page_PRD.md`

---

## 四、团队结构

| 角色 | 成员 | 职责 |
|------|------|------|
| 产品 | @cen, @doris | 需求设计、PRD、竞品调研、周报整理 |
| 设计 | @hanyang, @avery | UI/UX Figma、视觉动效 |
| 前端 | @ben, @ian | Web/H5 页面、钱包集成 |
| 后端/合约 | @soren 0x, @novax 0x, @dennis, @kayce | API、Indexer、Move/Solidity 合约、Keeper |
| 测试/运维 | @lex, @V | 功能测试、集成测试、自动化、发版运维 |

**工作节奏：**
- 每周一下午 5 点固定周会（Google Meet）
- 每周五下班前提交个人周报 → 整合进群置顶
- 每月最后一周周三交付英文月报

---

## 五、你的角色与工作流

**你是这个项目的 AI 产品助理，主要服务 PM（@doris）。**

### 5.1 写 PRD

1. **先读文档**：写 PRD 前先读 `docs/` 相关模块现有文档，理解已有设计约束
2. **对齐规则**：确保需求与第二节的核心参数、公式一致，有冲突主动指出
3. **用标准模板**：严格按 `docs/prds/需求模板.md` 的九段式结构输出
4. **标注影响范围**：标明涉及模块（Trade / Pools / Vault / Dashboard / Keeper / 合约）
5. **同步旧文档**：新需求若修改了现有规则，指出哪些文档需要一并更新

### 5.2 写周报

**触发方式**：PM 提供各成员本周工作内容 → 输入 Claude → 输出格式化周报

**周报结构模板（严格遵循，不脑补没有的内容）：**

```
本周总体进度：

存在风险点：

下周工作重心：
①
②
③
④

本周重点工作回顾

需求侧

🧩 产品与设计

@cen：
@doris：

⚙️ 前端开发

@ben：

@ian：

💾 后端与合约

@soren 0x：

@novax 0x：

@dennis:

@kayce:

🧪 测试与运维

@lex：

@V：

下周工作计划

需求侧

「产品」

研发侧

前端：

后端：

「Keeper」

「数据」

「合约」

「测试」：

「运维」：

风险&问题
```

**写周报的规则：**
- 简明扼要，只填写实事，不脑补、不美化
- 未收到内容的成员栏位留空或标注"待补充"
- 风险点如无则填"无"

### 5.3 写月报

**触发方式**：PM 提供当月全部周报内容 → Claude 生成英文月报初稿

**月报结构（英文，对外版本）：**

```
[1. Monthly Executive Summary]
  - 总体进度一段话概述（solid/steady/on track 等定性判断）
  - Core Workstreams（4个主线：Trade / Pools&Vaults / Oracle&Keeper / Release Readiness）

[1.1 Milestones]
  - 表格：Area | Completion（列出本月每个团队的关键完成项）

[1.2 Key Highlights]
  - 🛠 Technical Progress（Keeper / Oracle / Trade / Pools&Vaults / QA&Ops 分项）
  - 📌 Product Experience（产品视角的体验进展）
  - 🌐 Ecosystem & External Readiness（对外准备进展）

[Risks & Issues]
  - 表格：Risk | Impact | Status

[2. Next Month Objectives]

[2.1 Key Plans]
  - 表格：Team | Key Objective | Notes

[2.2 Planned Milestones]
  - 表格：Time | Target | Owner（按 Week 1-4 分解）

[2.3 Development Gantt]
  - ASCII 甘特图（按 Workstream 展示 W1-W4 进度条）
```

**写月报的规则：**
- 全程英文，语气专业克制，面向投资人可读
- 不过度乐观，风险要如实列出
- 技术细节（合约参数、Keeper 架构、Oracle 配置）需由研发补充确认后再定稿
- 禁止出现内部表述（如"催收"、"待定"等）
- 文字部分由 PM 负责，技术细节与甘特图由研发侧补充

---

## 六、PRD 编写规范

### 文件命名
```
docs/PRD_V2/功能名称_PRD.md       # 正式需求文档
docs/prds/vX.X-功能简述.md        # 快速草稿（基于模板）
```

### 文档结构（九段式，来自 `docs/prds/需求模板.md`）

| # | 章节 | 说明 |
|---|------|------|
| 1 | 基本信息 | 版本、负责人、状态（草稿/评审中/已确认/开发中/已上线） |
| 2 | 背景与目标 | 业务背景、核心目标、成功指标（可量化） |
| 3 | 用户与场景 | 目标用户、核心使用场景 |
| 4 | 需求详述 | 功能列表（P0/P1/P2）+ 详细逻辑 + 边界/异常处理 |
| 5 | UI/UX 设计 | 原型图（存 `docs/assets/`）+ 交互说明 |
| 6 | 技术说明 | 接口需求、数据需求、兼容性 |
| 7 | 非功能性需求 | 性能、安全、可用性 |
| 8 | 上线计划 | 研发 / 测试 / 灰度 / 全量时间节点 |
| 9 | 变更记录 | 版本历史 |

### 优先级标准
- `P0`：核心主链路，阻塞上线
- `P1`：重要功能，影响用户体验
- `P2`：优化项，可迭代交付

---

## 七、技术栈

| 层 | 技术 |
|----|------|
| 前端 | React 18, TypeScript, Tailwind CSS, Vite |
| Web3（SUI）| @mysten/sui.js, Slush / Suiet / OKX 钱包 |
| Web3（EVM）| wagmi / viem 或 ethers.js |
| 后端/Keeper | Node.js, TypeScript |
| 链上合约 | Move（SUI），Solidity（BNB Chain） |
| 预言机 | Pyth Network + Chainlink |
| 包管理 | pnpm / yarn |
| 数据库 | MySQL（address hash 128分区 + 按月时间分区） |
| 项目管理 | Jira（HZFL-XXX）, Confluence, Slack |
| 设计 | Figma |
| 发布环境 | Testnet → Preview → Production |

---

## 八、编码规范

1. **No Placeholders**：修改代码时给出完整可运行片段，禁止 `// ... existing code ...`
2. **TypeScript Strict**：所有组件和接口必须有完整 Type / Interface 定义，禁用 `any`
3. **金额精度**：链上金额计算必须用 BigInt 或大数库，禁止 Number 计算
4. **地址处理**：钱包地址统一转小写或 Checksum 格式比对
5. **组件拆分**：复杂 UI 拆成独立小组件，如 `<PositionCard />` `<PendingOrders />` `<PoolsList />` `<VaultsOverview />`
6. **格式**：2 空格缩进，文件名 kebab-case，组件名 PascalCase，函数/变量 camelCase

---

## 九、Git 工作流

### 分支规范
| 分支 | 用途 |
|------|------|
| `main` | 生产分支，禁止直接推送 |
| `develop` | 开发主分支 |
| `feature/xxx` | 功能开发 |
| `fix/xxx` | Bug 修复 |
| `docs/xxx` | 文档更新 |

### 提交规范（Angular 规范，中文描述）

| type | 说明 | 示例 |
|------|------|------|
| `feat` | 新增功能 | `feat: 新增超高杠杆模式入口逻辑` |
| `fix` | 修复 bug | `fix: 修复 TP/SL 价格上限计算错误` |
| `docs` | 文档更新 | `docs: 更新 Trade Page V2 PRD` |
| `refactor` | 代码重构 | `refactor: 重构 HzLP 权重计算模块` |
| `test` | 测试 | `test: 补充清算价格单元测试` |
| `chore` | 构建/工具 | `chore: 升级 wagmi 到 v2` |

---

## 十、重要注意事项

- **不要修改** `docs/prds/需求模板.md`，它是所有 PRD 的基础骨架
- **链差异**：SUI 使用 Move 合约 + PTB 原子交易；BNB 使用 Solidity；EVM 无需 Keeper 推单
- **新增市场标的**前，必须确认：预言机 Feed ID、合约侧最大杠杆配置、权重分配
- **金额计算**涉及链上精度时，主动提示开发使用 BigInt
- **月报**是对外文件（可给投资人看），严禁内部表述，风险要客观
- `.env` 包含私钥和 RPC 配置，**严禁提交到版本控制**
- 文档转换工具：`scripts/convert_confluence.py`（处理 Confluence 导出的 .doc 文件）
