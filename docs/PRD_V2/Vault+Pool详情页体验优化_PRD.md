# Vault + Pool 详情页体验优化 PRD

## 基本信息

| 字段 | 内容 |
|------|------|
| 需求名称 | Vault + Pool 详情页体验优化 |
| JIRA | HZFL-402 |
| 文档版本 | v1.0 |
| 负责人 | @doris |
| 创建日期 | 2026-02-28 |
| 最后更新 | 2026-02-28 |
| 原型图 | [Figma](https://www.figma.com/design/KO0hbbZ9JcKJRAKBYBeYGj/Hertzflow?node-id=109-1212&t=3kPmLrJ9F7fJ2yY0-0) |
| 状态 | 草稿 |
| 涉及模块 | Vault / Pools |

---

## 一、背景与目标

### 1.1 业务背景

当前 Vault 详情页与 Pool 详情页存在以下核心问题：

- **用户核心数据不醒目**：Your Holdings（存款、收益、份额）被折叠在次要区域，用户无法一眼获取个人持仓概况。
- **缺少策略与底层资产说明**：用户不清楚 Vault 的投资策略和资产构成，影响投资决策。
- **图表交互薄弱**：Y 轴/X 轴格式不规范，缺少 Hover Tooltip，图表可读性差。
- **Capacity 环形图信息密度低**：环形图无法有效传递容量紧张程度，缺少状态提醒。
- **缺少个人投资表现追踪**：无 PNL 面板，无法留存和激励用户持续投资。
- **Deposit 面板缺少收益预估**：用户输入金额后没有收益预期，转化率低。

两个详情页（Vault / Pool）布局相同，本次一并优化。

### 1.2 核心目标

- 将 Your Holdings 提升至顶部统计行，与 TVL、Earned Fees 同级，突出个人持仓。
- 新增 Strategy & Market Exposure 面板（仅 Vault），帮助用户理解投资策略和资产构成。
- 优化图表坐标轴格式和 Hover 交互，提升数据可读性。
- 将 Vault Capacity 环形图替换为状态感更强的横向进度条（仅 Vault）。
- 新增 Your Performance Tab（All-time PNL / Unrealized PNL），形成个人投资记录。
- 在 Deposit 面板新增 Estimated Annual Earnings 实时预估，提升用户投入意愿。

### 1.3 成功指标

| 指标 | 目标 |
|------|------|
| Vault 详情页 Deposit 转化率 | 上线后提升 ≥ 10% |
| Your Performance Tab 点击率 | 上线后 ≥ 15% DAU 点击 |
| 页面停留时长 | 较上线前提升 ≥ 15% |

---

## 二、用户与场景

### 2.1 目标用户

- **流动性提供者（LP）**：已存入或考虑存入 Vault / Pool 的用户，关注收益表现和资产安全。
- **新用户**：首次访问 Vault 详情页、需要了解策略和资产构成后做投资决策的用户。

### 2.2 核心场景

**场景一：老用户查看持仓概况**

> LP 用户打开 Vault 详情页，希望一眼看到自己的存款总额、累计收益和份额占比，无需滚动或点击展开。

**场景二：新用户评估投资策略**

> 新用户访问 HertzFlow Bluechip Crypto Vault，希望了解这个 Vault 的策略逻辑和底层资产配比，再决定是否存入。

**场景三：用户预估收益后决策 Deposit**

> 用户在 Deposit 面板输入 $1,000，希望立即看到预计年收益是多少，以便决定存入金额。

**场景四：用户查看历史投资表现**

> 持仓用户点击 Your Performance Tab，查看 All-time PNL 和 Unrealized PNL，评估投资回报。

---

## 三、需求详述

### 3.1 功能列表

| 功能模块 | 功能描述 | 优先级 | 页面 |
|----------|----------|--------|------|
| Your Holdings 顶部统计行 | 将 Deposits / Earnings / Your Share 提升至顶部同级展示 | P0 | Vault + Pool |
| APY 标签 + 7d 趋势 | 标题行新增当前 APY 绿色标签及 7 日趋势文案 | P0 | 仅 Vault |
| Strategy & Market Exposure | 图表上方新增可折叠策略说明面板 + 资产占比堆叠进度条 | P0 | 仅 Vault |
| Top N+1 聚合规则 | 超过 5 种资产时触发聚合，Others 可 Hover 展开明细 | P1 | 仅 Vault |
| 图表坐标轴优化 | Y 轴固定 5 刻度 + 格式缩写；X 轴动态稀疏化 | P0 | Vault + Pool |
| Hover Tooltip | 十字准星 + 完整日期和精确数值浮层 | P0 | Vault + Pool |
| Your Performance Tab | 新增 Tab，展示 All-time PNL / Unrealized PNL | P1 | Vault + Pool |
| Vault Capacity 进度条 | 环形图替换为横向进度条，三档状态颜色和文案 | P1 | 仅 Vault |
| Estimated Annual Earnings | Deposit 面板实时预估年/月/日收益 | P1 | Vault + Pool |
| Activity Tab 命名规范 | Vault: My Activity/Vault Activity；Pool: My Activity/Pool Activity | P2 | Vault + Pool |

### 3.2 详细说明

#### 3.2.1 顶部统计行 — Your Holdings

Your Holdings 区块与 TVL、Total Earned Fees 同级展示在页面顶部统计行。

| 字段 | 说明 | 数据来源 |
|------|------|----------|
| Deposits | 用户在此 Vault/Pool 的存款总额 | 同现有 Your Holdings → Deposits |
| Earnings | 累计已赚收益，正值显示绿色 | Vault: Your Earnings；Pool: Earned Fees |
| Your Share | 用户持有的 LP Token 数量（直接读合约余额） | Vault: HzV token balance；Pool: HzLP token balance（与 Activity 表 Shares 列相同） |

**边界处理：**
- 用户无存款时，各项显示 $0 / $0 / 0%。
- 其余 4 个统计卡片（TVL / Total Earned Fees / Remaining Deposit Cap / Remaining Withdrawal Cap）保持不变。

#### 3.2.2 标题行 APY 标签 + 7d 趋势（仅 Vault）

| 元素 | 示例 | 说明 |
|------|------|------|
| Vault 名称 | Bluechip Crypto | 同现有 |
| APY 标签 | APY 45.26% | 绿色圆角标签，样式同 Vault 列表卡片 |
| 7d 趋势 | ↑ +2.3% vs 7d ago | 前端计算：当前 APY − 7 天前 APY；正值绿色向上箭头，负值红色向下箭头 |

Pool 不加此区块（Pool 的 Fee APY 已在图表 Tab 展示）。

#### 3.2.3 Strategy & Market Exposure（仅 Vault）

图表上方新增可折叠面板，默认展开，Pool 无此区块。

**Strategy 说明文案（前期写死，后续接后台配置接口）：**

| Vault 名称 | English Introduction |
|-----------|---------------------|
| HertzFlow Degen Basket | An aggressive DeFi portfolio focusing on emerging assets and high-yield strategies, ideal for seasoned players seeking high risk-reward. |
| HertzFlow Macro | A macro stable vault tracking global market trends with mainstream assets, suitable for investors focused on capital preservation and hedging. |
| HertzFlow Bluechip Crypto | A core bluechip crypto vault focusing on top assets like BTC and ETH, delivering solid returns via low-risk enhancement strategies, ideal for long-term value investing. |
| HertzFlow Tech Giants | A tech-themed vault anchored in Web3 and tech giant ecosystems with ultra-low volatility, ideal for conservative users looking to deploy in the tech sector. |

**Market Exposure 展示规则：**

1. 堆叠进度条展示底层资产占比（各段颜色与币种对应）。
2. 进度条下方每个币种一张卡片：币种 icon（同 Trade 页资产 icon）+ symbol + weight% + 小进度条。
3. 市场配置数据前期写死，后续接后台配置接口。

**Top N+1 聚合规则（当 Vault 包含币种数量 > 5 时触发）：**

- **排序**：按持仓占比降序排列所有币种。
- **截取**：取前 4 名（Top 4）保留独立展示。
- **聚合**：第 5 名及之后所有币种占比相加，合并为 "Others"。
- **进度条**：最多显示 5 段（Top 4 各自颜色 + Others 中性色，以设计稿为准）。
- **卡片**：下方最多展示 5 张卡片，第 5 张固定为 Others 卡片（通用图标 + "Others" 文案 + 合并后总占比）。
- **Hover/Click 交互**：悬浮或点击 Others 进度条段或卡片时，弹出 Tooltip 浮层，按占比降序列出所有被折叠币种明细（如 MATIC 3%, LINK 2%, UNI 1%）。

#### 3.2.4 图表区 — Tab 结构（Vault + Pool）

| 页面 | Tab |
|------|-----|
| Vault | TVL / Fee APR / Your Performance |
| Pool | TVL / Fee APR / Your Performance |

**TVL / Fee APR 图表 — Y 轴规则：**

- 固定 5 个刻度（均分），底座固定为 $0。
- 最大值：读取数据最大值并向上取整为易读整数（如最大值 1790 → 取整到 1800）。
- 显示格式：
  - < 1,000：显示原数值（如 $450）
  - ≥ 1,000：缩写保留两位小数（如 $1.50K）
  - ≥ 1,000,000：缩写保留两位小数（如 $2.10M）

**TVL / Fee APR 图表 — X 轴动态时间轴规则：**

| 时间范围 | 标签间距 | 格式 | 示例（基准日 2026/02/28） |
|---------|---------|------|--------------------------|
| 7D | 每天 1 个，共 7 个 | MM/DD | 02/22, 02/23, …, 02/28 |
| 30D | 每 5 天 1 个，约 6 个 | MM/DD | 01/30, 02/04, 02/09, 02/14, 02/19, 02/24, 02/28 |
| 90D | 每 15 天 1 个，约 6 个 | MM/DD | 11/30, 12/15, 12/30, 01/14, 01/29, 02/13, 02/28 |
| 180D | 每 30 天 1 个，约 6 个 | MM/DD 或英文月份 | 09/01, 10/01, 10/31, 11/30, 12/30, 01/29, 02/28 |
| All | 动态计算（总天数 ÷ 5 或 6） | YYYY 或 YYYY/MM | 间距约 60 天（1 年数据），约 120 天（2 年数据） |

**Hover 交互 — Tooltip：**

- **触发方式**：横向全区域触发（X 轴跟随），无需精准悬浮在数据点上。
- **十字准星**：垂直浅色虚线 + 数据点对应颜色的高亮圆点。
- **浮层内容**：完整日期 + 精确数值（Tooltip 内不缩写 K/M）。
  - 示例：`2026/02/13` 换行 `TVL $11,620.00`

#### 3.2.5 Your Performance Tab（Vault + Pool）

点击后显示 2 行数据，不显示图表，右侧时间周期选择器隐藏。

| 字段 | 说明 | 数据来源 |
|------|------|----------|
| All-time PNL | 正值绿色 +$X.XX，负值红色 -$X.XX，无数据 N/A | 后端新增 / 前端计算 |
| Unrealized PNL | 同上 | 后端新增 / 前端计算 |

**空状态：**
无存款时显示：图标 + "No Performance Data" + "Deposit into this vault/pool to track your PNL and performance"。

#### 3.2.6 Vault Capacity 进度条（仅 Vault）

替换现有环形图，Pool 无此区块。

| 元素 | 说明 |
|------|------|
| 标题行 | 左：Deposited；右：$1.80K / $1.00M（当前存款 / 上限） |
| 进度条 | 横向，填充比例 = 当前存款 / TVL Cap |
| 底部左 | 当前填充百分比 |
| 底部右 | 状态文案（见下表） |

| 状态 | 填充比例 | 进度条颜色 | 右侧文案 |
|------|---------|------------|---------|
| 正常 | < 80% | 渐变青色 | $XXX remaining |
| 接近满额 | 80%–99% | 渐变橙色 | ⚠ Nearly Full |
| 已满 | 100% | 渐变红色 | ⚠ Full |

数据复用现有 Deposited / TVL Cap，无新增接口。

#### 3.2.7 Deposit/Withdraw 面板 — Estimated Annual Earnings（Vault + Pool）

仅在 Deposit 模式下展示，切换至 Withdraw 时隐藏此区块。

**触发与显隐：**
- 用户输入有效金额（> 0）时，实时（防抖）计算并展示。
- 输入为空或为 0 时隐藏此区块。

**计算逻辑：**
```
年收益 = 输入金额 × 当前实时 APY / 100
月收益 = 年收益 / 12
日收益 = 年收益 / 365
```
- Vault 使用 APY；Pool 使用 Fee APY。
- 所有数值保留 2 位小数。

**展示规范：**

| 元素 | 示例 |
|------|------|
| 标题 | Estimated Annual Earnings (at current APY) |
| 主值（放大 + 品牌色 + 强制 + 号） | +$303.51 |
| 辅助（置灰小字） | ≈ $25.29/month · $0.83/day |

#### 3.2.8 Activity Tab 命名规范（Vault + Pool）

| 页面 | 全局 Tab | 个人 Tab | 默认选中 |
|------|---------|---------|---------|
| Vault | Vault Activity | My Activity | Vault Activity（全局） |
| Pool | Pool Activity | My Activity | Pool Activity（全局） |

字段与现有一致，无新增。

---

## 四、UI/UX 设计

### 4.1 原型参考

Figma：[Hertzflow — node-id=109-1212](https://www.figma.com/design/KO0hbbZ9JcKJRAKBYBeYGj/Hertzflow?node-id=109-1212&t=3kPmLrJ9F7fJ2yY0-0)

### 4.2 交互说明

1. **Strategy & Market Exposure 折叠面板**：默认展开，点击标题行右侧箭头可折叠/展开，状态本地存储（不跨 Vault 同步）。
2. **Others 卡片 Hover**：鼠标悬浮于 Others 卡片或对应进度条段时，浮层出现；移出后浮层消失。
3. **图表 Tooltip**：跟随鼠标 X 轴位置显示，不需要精准点击数据点，浮层在画布边缘时自动反向弹出。
4. **Estimated Annual Earnings**：输入防抖 300ms，防止频繁计算；用户清空输入后区块淡出隐藏。
5. **Vault Capacity**：进度条满额（100%）时，Deposit 按钮置灰并展示 "Deposit Cap Reached" 提示。
6. **Your Performance Tab**：切换至此 Tab 时右侧时间周期按钮组（7D/30D/90D/All）自动隐藏。

---

## 五、技术说明

### 5.1 接口需求

| 接口 | 类型 | 说明 |
|------|------|------|
| Your Performance — All-time PNL | 新增 | 参数：vault_id 或 pool_id + wallet_address；返回 all_time_pnl, unrealized_pnl |
| Strategy & Market Exposure | 暂无（前期写死） | 后续后台提供配置接口，前端按 vault_id 读取策略文案和资产权重 |
| TVL / Fee APR 历史数据 | 现有接口 | 数据来源与现有一致，无新增 |
| Your Share (LP Token Balance) | 现有合约读取 | Vault: HzV token balance；Pool: HzLP token balance，直接读链上余额 |
| Vault Capacity | 现有接口 | 复用 Deposited / TVL Cap，无新增 |

### 5.2 数据需求

- **Your Share**：直接从合约读取 HzV / HzLP 余额，不需要后端额外计算，与 Activity 表 Shares 列数据一致。
- **APY 7d 趋势**：前端从现有 APY 历史数据中取当前值与 7 天前值做差，无需新接口。
- **Estimated Annual Earnings**：纯前端计算，无需接口。
- **图表坐标轴格式化**：纯前端处理，现有图表数据接口不变。

### 5.3 兼容性要求

- PC Web（Chrome / Firefox / Safari，最新两个版本）
- H5 移动端适配（Strategy & Market Exposure 折叠面板在移动端默认折叠以节省屏幕空间）
- 钱包未连接时 Your Holdings 和 Your Performance 均显示空状态

---

## 六、非功能性需求

| 类型 | 要求 |
|------|------|
| 性能 | Estimated Annual Earnings 防抖 300ms，避免高频计算；图表渲染不得引起页面卡顿 |
| 安全 | 无新增敏感操作，LP Token 余额读取沿用现有钱包授权体系 |
| 可用性 | 所有新增数据区块在加载中时显示 Skeleton 骨架屏；接口报错时显示 "--" 而非 $0，避免误导用户 |

---

## 七、上线计划

| 阶段 | 内容 | 预计时间 |
|------|------|----------|
| 研发 | 前端实现各模块 UI + 交互逻辑 | 待排期 |
| 后端 | Your Performance PNL 接口开发 | 待排期 |
| 测试 | 功能测试 + 边界测试（无存款 / 满额 / Others 聚合） | 待排期 |
| 灰度 | Testnet 验证 | 待排期 |
| 全量 | 正式上线 | 待排期 |

---

## 八、遗留问题

| 问题 | 负责人 | 截止时间 | 状态 |
|------|--------|----------|------|
| Your Performance PNL 接口字段定义（All-time PNL 计算口径确认） | 后端 | 待确认 | 待解决 |
| Strategy & Market Exposure 后台配置接口排期 | 后端 | 待确认 | 待解决 |
| Others 聚合卡片通用图标素材确认 | 设计 | 待确认 | 待解决 |
| Vault Capacity 进度条渐变配色（青 / 橙 / 红具体色值） | 设计 | 待确认 | 待解决 |
| Pool 详情页 Fee APY 历史数据接口是否覆盖所有时间范围（All） | 后端 | 待确认 | 待解决 |

---

## 九、变更记录

| 版本 | 修改内容 | 修改人 | 日期 |
|------|----------|--------|------|
| v1.0 | 初稿创建，覆盖 Vault + Pool 详情页全部优化项 | @doris | 2026-02-28 |
