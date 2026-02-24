# Prototypes

此目录用于存放由 Claude 自动生成的可交互 UI 原型。

## 使用说明

每个原型以独立子目录存放，命名格式建议：`功能名-vX.X/`

```
prototypes/
├── 超高杠杆-v1.0/
│   ├── index.html     # 可直接在浏览器打开预览
│   └── ...
└── ...
```

## 技术说明

原型通常使用以下技术栈生成，无需构建即可在本地运行：

- HTML / CSS / JavaScript
- React（通过 CDN 引入）
- Tailwind CSS（通过 CDN 引入）
