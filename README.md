# Hertzflow

> 产品研发协作仓库 —— 需求文档、原型与源码统一管理

---

## 仓库结构

```
Hertzflow/
├── docs/
│   ├── prds/          # 产品需求文档（Markdown）
│   │   ├── 需求模板.md
│   │   └── v2.0-超高杠杆需求.md
│   └── assets/        # 原型截图、流程图等静态资源
├── src/               # 前端页面 / 后端接口源码
├── prototypes/        # Claude 生成的可交互 UI 原型
└── CLAUDE.md          # AI 协作规范
```

---

## 各目录说明

### `docs/prds/`

存放所有产品需求文档，统一使用 Markdown 格式。

- 新建需求时，复制 `需求模板.md` 并按 `vX.X-功能名.md` 命名
- 文档状态在文件头部的基本信息表中维护

### `docs/assets/`

存放与需求相关的图片资源，包括原型截图、流程图、示意图等。

建议命名格式：`功能名-描述.png`

### `src/`

项目实际运行的源码，包括前端页面或后端接口逻辑。

### `prototypes/`

存放可直接在浏览器打开预览的交互原型（无需构建）。

每个原型独立一个子目录，命名格式：`功能名-vX.X/`

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
