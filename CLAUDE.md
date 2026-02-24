# Hertzflow

## 项目概述

<!-- 简要描述项目的目的和功能 -->

## 技术栈

<!-- 列出主要技术和框架，例如：
- 语言：TypeScript / Python / Go
- 框架：React / Next.js / FastAPI
- 数据库：PostgreSQL / MongoDB
- 其他：Docker, Redis, etc.
-->

## 项目结构

```
Hertzflow/
├── src/          # 源代码
├── tests/        # 测试文件
├── docs/         # 文档
└── ...
```

## 开发环境搭建

```bash
# 安装依赖
# npm install / pip install -r requirements.txt / ...

# 启动开发服务器
# npm run dev / python main.py / ...
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `npm run dev` | 启动开发服务器 |
| `npm run build` | 构建生产版本 |
| `npm run test` | 运行测试 |
| `npm run lint` | 代码检查 |

## 编码规范

- 使用 2 空格缩进
- 文件名使用 kebab-case（如 `my-component.ts`）
- 组件名使用 PascalCase（如 `MyComponent`）
- 函数和变量使用 camelCase（如 `myFunction`）

## Git 工作流

- `main` / `master`：生产分支，禁止直接推送
- `develop`：开发主分支
- 功能分支命名：`feature/描述`
- 修复分支命名：`fix/描述`

提交信息格式：
```
type(scope): 简短描述

可选的详细说明
```

type 类型：`feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 重要注意事项

<!-- 列出 Claude Code 在协助开发时需要特别注意的事项，例如：
- 不要修改某些关键配置文件
- 数据库迁移需要手动审查
- 部署前必须通过所有测试
-->

## 环境变量

敏感配置通过环境变量管理，参考 `.env.example` 文件。**不要将 `.env` 文件提交到版本控制。**
