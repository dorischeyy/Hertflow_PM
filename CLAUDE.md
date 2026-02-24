# Hertzflow

## 1. 项目与业务背景

- **项目名称**: Hertzflow
- **业务定位**: Web3 去中心化永续合约交易所（Perp DEX，对标 GMX / Jupiter）。
- **核心模块**: 前端交易面板（Trade / Pools / Vaults）、后端 Keeper 节点、链上智能合约。
- **核心业务概念**（AI 必须深刻理解）：
  - `Trade`：交易侧，用户为了博取价差收益，具有高风险偏好。
  - `Pools`：流动性侧，用户作为 LP 提供流动性赚取手续费，规避无常损失。
  - **重要原则**：交易收藏（Trade Favorite）与资金池收藏（Pool Favorite）必须解耦，因为两者用户动机不同，且需为未来多资产池预留扩展性。

## 2. 你的角色与工作流

你是一个具备资深产品 Sense 的全栈 Web3 工程师。本项目实行 **Docs-as-Code（文档即代码）** 流程，请严格遵循以下工作流：

- **读取需求**：在编写任何核心功能代码前，必须优先读取 `docs/prds/` 目录下的 Markdown 需求文档。
- **任务拆解**：如果被要求开发新需求，请先将 PRD 拆解为可执行的任务清单（`tasks.md`）。
- **原型先行**：涉及 UI 变更时，优先在 `prototypes/` 目录下生成基于 React + Tailwind 的单页占位原型供产品评审，评审通过后再整合到 `src/` 中。
- **同步文档**：如果在代码实现中发现逻辑漏洞并进行了修改，必须同步修改对应的 PRD 文件。

## 3. 项目结构

```
Hertzflow/
├── docs/
│   ├── prds/          # 存放所有 PRD（Markdown 格式）
│   │   ├── 需求模板.md
│   │   └── v2.0-超高杠杆需求.md
│   └── assets/        # 原型截图、流程图等静态资源
├── src/               # 实际前端/后端源码
├── prototypes/        # Claude 生成的可交互 UI 原型
└── CLAUDE.md
```

## 4. 技术栈

- **前端**: React 18, TypeScript, Tailwind CSS, Vite（Web3 交互使用 wagmi / viem 或 ethers.js）
- **后端/Keeper**: Node.js, TypeScript
- **包管理器**: pnpm / yarn

## 5. 编码规范

1. **No Placeholders**：不要生成 `// ... existing code ...` 等占位符，修改代码时给出完整的可运行代码片段。
2. **TypeScript Strict Mode**：所有前端组件和后端接口必须有完善的 Interface 或 Type 定义，禁止使用 `any`。
3. **Web3 特定安全**：
   - 处理金额时，必须使用 BigInt 或特定的大数库处理精度（Decimals），禁止使用普通 Number 计算导致精度丢失。
   - 所有钱包地址处理必须统一转为小写或 Checksum 格式进行比对。
4. **组件化**：前端 UI 遵循极简与直观原则。如资产统计面板需拆分为独立的小组件：`<PositionCard />`, `<PendingOrders />`, `<PoolsList />`, `<VaultsOverview />`。
5. **通用格式**：使用 2 空格缩进，文件名使用 kebab-case，组件名使用 PascalCase，函数和变量使用 camelCase。

## 6. Git 工作流

- `main`：生产分支，禁止直接推送
- `develop`：开发主分支
- 功能分支命名：`feature/描述`
- 修复分支命名：`fix/描述`

**提交规范（Angular 规范，中文描述）**：

| type | 说明 | 示例 |
|------|------|------|
| `feat` | 新增功能 | `feat: 新增 Trade 和 Pool 的独立收藏逻辑` |
| `fix` | 修复 bug | `fix: 修复 Markets 接口数据同步问题` |
| `docs` | 文档更新 | `docs: 更新 v2.0-超高杠杆 PRD 文档` |
| `refactor` | 代码重构 | `refactor: 重构收藏夹状态管理逻辑` |
| `test` | 测试相关 | |
| `chore` | 构建/工具变更 | |

## 7. 环境变量

敏感配置通过环境变量管理，参考 `.env.example` 文件。**不要将 `.env` 文件提交到版本控制。**
