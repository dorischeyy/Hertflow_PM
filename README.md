# Hertzflow

> 产品研发协作仓库 —— 需求文档、原型与源码统一管理

---

## 仓库结构

```
Hertzflow/
├── docs/
│   ├── PRD_V1/            # V1 阶段产品需求文档
│   ├── PRD_V2/            # V2 阶段产品需求文档
│   ├── Research Report/   # 竞品调研与产品设计文档
│   ├── 后端/               # 后端接口与架构设计文档
│   ├── 测试网相关整理/      # 测试网文档、法律文本等
│   ├── 项目组周报汇总/      # 周报、排期、Release Notes
│   ├── 月报/               # 月报文档及附件
│   ├── prds/              # Markdown 格式需求文档（模板与草稿）
│   │   ├── 需求模板.md
│   │   └── v2.0-超高杠杆需求.md
│   └── assets/            # 原型截图、流程图等静态资源
├── src/                   # 前端页面 / 后端接口源码
├── prototypes/            # Claude 生成的可交互 UI 原型
└── CLAUDE.md              # AI 协作规范
```

---

## 各目录说明

### `docs/PRD_V1/`

V1 阶段全量需求文档，包括产品总览、LP 机制、Swap Fee 拆分、风控参数、前端展示规范等。

### `docs/PRD_V2/`

V2 阶段需求文档，涵盖 Trade / Pools / Vault / Dashboard / Claim 等核心页面，以及超高杠杆、TP/SL 逻辑说明、需求池 Backlog 等。

### `docs/Research Report/`

竞品功能调研、风控参数自动化研究、Leaderboard & Referral 机制调研、V2 产品设计文档等。

### `docs/后端/`

后端接口设计、数据表设计、Keeper 架构、合约状态监控、用户持仓追踪等技术设计文档。

### `docs/测试网相关整理/`

测试网阶段市场配置、Developer Documentation、隐私政策、用户协议等对外文档。

### `docs/项目组周报汇总/`

项目组周报、V1/V2 需求排期、Release Notes、功能记录表。

### `docs/月报/`

HertzFlow 月报正文及 PDF 附件。

### `docs/prds/`

Markdown 格式的需求模板与草稿，新建需求时复制 `需求模板.md` 并按 `vX.X-功能名.md` 命名。

### `docs/assets/`

存放与需求相关的图片资源，包括原型截图、流程图、示意图等。建议命名：`功能名-描述.png`

### `src/`

项目实际运行的源码，包括前端页面或后端接口逻辑。

### `prototypes/`

存放可直接在浏览器打开预览的交互原型（无需构建）。每个原型独立一个子目录，命名格式：`功能名-vX.X/`

---

## 工作流

### 新增需求

```bash
# 1. 基于模板创建新 PRD
cp docs/prds/需求模板.md docs/prds/vX.X-新功能名.md

# 2. 编辑文档后提交
git add docs/prds/vX.X-新功能名.md
git commit -m "docs(prds): 新增 vX.X 新功能名需求文档"
git push
```

### 提交规范

```
type(scope): 简短描述
```

| type | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复问题 |
| `docs` | 文档变更 |
| `refactor` | 代码重构 |
| `chore` | 构建/工具变更 |

### 分支规范

| 分支 | 用途 |
|------|------|
| `main` | 生产分支，禁止直接推送 |
| `develop` | 开发主分支 |
| `feature/xxx` | 功能开发分支 |
| `fix/xxx` | 问题修复分支 |

---

## 注意事项

- `.env` 文件包含敏感配置，**禁止提交到版本控制**
- `docs/assets/` 中避免上传超过 5MB 的大文件
