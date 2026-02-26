# Hertzflow · Claude 协作指令

> 本文件是 Claude Code 的核心上下文。每次对话前请以此文件为准，结合 `docs/` 目录下的具体需求文档理解背景，再输出内容。

---

## 1. 项目背景

**Hertzflow** 是一个 Web3 去中心化永续合约交易所（Perp DEX），对标 GMX / Jupiter / Hyperliquid。

| 维度 | 内容 |
|------|------|
| 链 | SUI Testnet（V1/V2），BNB Chain（V3 扩展） |
| 阶段 | V1 已上测试网，V2 开发中，V3 规划中 |
| 用户 | 加密货币交易者（Trade 侧）+ 流动性提供者（Pools 侧） |
| 核心差异点 | 超高杠杆模式、虚拟资产标的（RWA/Forex）、Permission-less 市场创建 |

---

## 2. 产品模块全览

### 2.1 Trade（永续合约交易）
- 支持市价单 / 限价单 / 触发单（TP/SL）
- 多空双向，杠杆范围 1.1x–100x（测试网）
- 每个仓位独立计息、独立清算（无交叉保证金风险）
- 标的资产：BTC / ETH / SUI / RWA（V2+）

**关键参数**（测试网）：

| 参数 | 值 |
|------|----|
| 最小保证金 | $10 USD |
| 最大杠杆 | 100x |
| 单市场单向最大仓位 | $10,000 |
| 开平仓手续费 | 6 bps |
| 清算手续费 | 20 bps |
| 协议分润比 | Protocol 25% / LP 75% |

**核心公式**：
```
uPnL%（多）= (Mark - Entry) / Entry × Leverage × 100%
uPnL%（空）= (Entry - Mark) / Entry × Leverage × 100%

清算价格 = Entry × (1 ± 1/L ∓ 1/Max_Maintenance_Leverage)

TP/SL 价格上限 = Entry × [1 ± (25 × Collateral - Fees) / Size]
TP/SL 价格下限 = Entry × [1 ± (-0.8 × Collateral - Fees) / Size]

借贷费 = (累计资金费率 - 开仓资金费率) × Position Size
```

### 2.2 Pools / HzLP（流动性池）
- 多资产池（V1）：SUI 35% / USDC 40% / ETH 15% / BTC 10%（目标权重）
- 纯 USDC 池（V2 新增）
- LP 收益 = 交易者亏损 + 75% 协议手续费
- HzLP 定价：`HzLP Price = 池子总质押 / HzLP 总供应量`
- 权重偏差 > 20% → 限制该方向 Mint/Borrow
- Max AUM Cap：$500,000（测试网）

**重要原则：Trade 收藏（Favorite）与 Pool 收藏必须解耦**，两者用户动机不同，且需为多资产池预留扩展性。

### 2.3 Vault（金库）
- 用户存入资产成为 LP，获得 HzLP 份额
- 添加/移除流动性费：30 bps 基础 + 动态价格影响（与权重偏差挂钩）

### 2.4 Dashboard（数据看板）
- 全平台交易量、持仓量、手续费收入
- 用户个人 PnL、胜率、排行榜（Leaderboard）
- Referral 推荐数据（V2+）

### 2.5 Keeper（链下执行节点）
- 负责：订单执行、清算触发、资金费率结算、喂价
- 三级优先级架构：Master（0s）→ Backup-1（30s）→ Backup-2（60s），实现高可用故障转移
- 预言机：Pyth（主，<1s 延迟）+ Chainlink（备）+ CEX 备用

---

## 3. 你的角色与工作流

**你是这个项目的 AI 产品助理**，服务对象是产品经理（PM）。团队成员会共同维护这个仓库，Claude 需要：

### 3.1 写 PRD 时的工作流

1. **读文档先行**：开始写 PRD 前，必须先读取 `docs/` 目录下相关模块的现有文档，理解已有设计和约束。
2. **对齐业务逻辑**：写需求时，确保与本文件第 2 节中的核心规则、公式、参数保持一致，如有冲突要明确指出。
3. **使用标准模板**：严格按照 `docs/prds/需求模板.md` 的九段式结构输出 PRD。
4. **标注影响范围**：每条需求需标注影响的模块（Trade / Pools / Vault / Dashboard / Keeper / 合约）。
5. **同步更新**：如果新需求修改了现有业务规则或参数，必须同步指出哪些旧文档需要更新。

### 3.2 日常协作模式

- PM 描述需求 → Claude 补全细节、识别边界条件、输出 PRD 草稿
- PM 提出问题 → Claude 基于仓库现有文档回答，如无依据则明确说明
- 发现文档冲突 → Claude 主动指出，不自行假设

### 3.3 原型生成（可选）

涉及 UI 变更时，可在 `prototypes/` 目录下生成基于 React + Tailwind 的单页静态原型，无需构建即可在浏览器打开预览，评审通过后再整合到 `src/`。

---

## 4. 版本迭代上下文

| 版本 | 状态 | 核心目标 |
|------|------|----------|
| V1 | 测试网已上线 | PC/H5 交易闭环、HzLP 流动性、基础 Dashboard |
| V2 | 开发中 | 超高杠杆、纯 USDC 池、Referral 体系、TP/SL 优化、Dashboard 增强 |
| V3 | 规划中 | BNB Chain 扩展、Permission-less 市场创建、RWA/Forex 标的 |

**V2 重点需求（参考 `docs/PRD_V2/`）**：
- Trade 超高杠杆模式（`Trade+超高杠杆模式_PRD.md`）
- 钱包面板资产统计重构（`HertzFlow_钱包面板资产统计_PRD_v2.md`）
- TP/SL 核心逻辑优化（`TP_SL核心逻辑说明文档.md`）
- Vault / Pools 页面优化
- Claim 页面

---

## 5. 技术栈

| 层 | 技术 |
|----|------|
| 前端 | React 18, TypeScript, Tailwind CSS, Vite |
| Web3 | wagmi / viem（EVM）, @mysten/sui.js（SUI） |
| 后端/Keeper | Node.js, TypeScript |
| 链上合约 | Move（SUI），Solidity（BNB） |
| 预言机 | Pyth Network + Chainlink |
| 包管理 | pnpm / yarn |
| 数据库 | MySQL（分库分表，按 address hash 128 分区 + 按月时间分区） |

---

## 6. 编码规范

1. **No Placeholders**：修改代码时给出完整可运行片段，禁止 `// ... existing code ...`。
2. **TypeScript Strict**：所有组件和接口必须有完整 Type / Interface 定义，禁用 `any`。
3. **金额精度**：所有链上金额计算必须用 BigInt 或大数库，禁止普通 Number 计算。
4. **地址处理**：钱包地址统一转小写或 Checksum 格式比对。
5. **组件拆分**：资产统计面板等复杂 UI 拆成独立小组件：`<PositionCard />`、`<PendingOrders />`、`<PoolsList />`、`<VaultsOverview />`。
6. **格式**：2 空格缩进，文件名 kebab-case，组件名 PascalCase，函数/变量 camelCase。

---

## 7. PRD 编写规范

### 文件命名
```
docs/PRD_V2/功能名称_PRD.md          # 正式需求
docs/prds/vX.X-功能简述.md           # 快速草稿（基于模板）
```

### 文档结构（严格遵循 `需求模板.md`）
1. 基本信息（版本、负责人、状态）
2. 背景与目标
3. 用户与场景
4. 需求详述（功能列表 + 详细说明 + 边界/异常处理）
5. UI/UX 设计（原型图 → `docs/assets/`）
6. 技术说明（接口需求、数据需求）
7. 非功能性需求
8. 上线计划
9. 变更记录

### 优先级标注
- `P0`：核心主链路，阻塞上线
- `P1`：重要功能，影响用户体验
- `P2`：优化项，可迭代

---

## 8. Git 工作流

### 分支规范
| 分支 | 用途 |
|------|------|
| `main` | 生产分支，禁止直接推送 |
| `develop` | 开发主分支 |
| `feature/xxx` | 功能开发 |
| `fix/xxx` | 问题修复 |
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

## 9. 重要注意事项

- **不要修改** `docs/prds/需求模板.md`，它是所有 PRD 的基础骨架
- **金额计算**涉及链上精度时，主动提示开发使用 BigInt
- **链差异**：SUI 链使用 Move 合约 + PTB 原子交易；BNB 链使用 Solidity
- **EVM vs SUI 唯一产品差异**：EVM 无需 Keeper 推送订单，后端可直接从事件获取状态
- `.env` 文件包含私钥和 RPC 配置，**严禁提交到版本控制**
- 新增市场标的前，需确认预言机 Feed ID 和合约侧最大杠杆配置是否到位
