# Dashboard_PRD

<div class="Section1">

<div class="contentLayout2">

<style>[data-colorid=qz94hrb95f]{color:#bf2600} html[data-color-mode=dark] [data-colorid=qz94hrb95f]{color:#ff6640}[data-colorid=mb267gq57n]{color:#bf2600} html[data-color-mode=dark] [data-colorid=mb267gq57n]{color:#ff6640}</style>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<style type="text/css">/**/
div.rbtoc1771927826130 {padding: 0px;}
div.rbtoc1771927826130 ul {list-style: none;margin-left: 0px;}
div.rbtoc1771927826130 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1771927826130">

- [顶部关键指标卡片（5x）](#Dashboard_PRD-顶部关键指标卡片（5x）)
- [各指标对应图表（12x）](#Dashboard_PRD-各指标对应图表（12x）)
  - [0. 筛选器交互说明（后续不再赘述，只说明特殊处理）](#Dashboard_PRD-0.筛选器交互说明（后续不再赘述，只说明特殊处理）)
  - [1. Volume - 交互总量图表（注意与3中total trading volume交易总量区分）](#Dashboard_PRD-1.Volume-交互总量图表（注意与3中totaltradingvolume交易总量区分）)
  - [2. Open Interest - 持仓分布](#Dashboard_PRD-2.OpenInterest-持仓分布)
  - [3. Total Trading Volume - 总交易量](#Dashboard_PRD-3.TotalTradingVolume-总交易量)
  - [4. Ann. Funding Rate - 年化资金费率](#Dashboard_PRD-4.Ann.FundingRate-年化资金费率)
  - [5. Realized PnL - 已实现盈亏](#Dashboard_PRD-5.RealizedPnL-已实现盈亏)
  - [6. Loss Rebate - 损失返还（合约尚未补充实现方式，后续可能修改需求）](#Dashboard_PRD-6.LossRebate-损失返还（合约尚未补充实现方式，后续可能修改需求）)
  - [7. Liquidations - 清算数据](#Dashboard_PRD-7.Liquidations-清算数据)
  - [8. Fees - 平台费用收入（合约尚未补充Profit Sharing实现方式，后续可能修改需求）](#Dashboard_PRD-8.Fees-平台费用收入（合约尚未补充ProfitSharing实现方式，后续可能修改需求）)
  - [9. Total Value Locked - 显示所有池子总流动性，也就是TVL，随时间的变化](#Dashboard_PRD-9.TotalValueLocked-显示所有池子总流动性，也就是TVL，随时间的变化)
  - [10. HzLP Price - 代币价格](#Dashboard_PRD-10.HzLPPrice-代币价格)
  - [11. Users - 用户统计](#Dashboard_PRD-11.Users-用户统计)
  - [12. Top 100 Users - 前100用户排行榜](#Dashboard_PRD-12.Top100Users-前100用户排行榜)
- [颜色系统（需要设计整理）](#Dashboard_PRD-颜色系统（需要设计整理）)

</div>

**竞品：Hyperliquid开源代码参考**

1.  **Python SDK** <a href="https://github.com/hyperliquid-dex/hyperliquid-python-sdk" class="external-link" data-card-appearance="inline" data-local-id="e969307a-0cd7-43dd-9196-df43f0eee81c" rel="nofollow">https://github.com/hyperliquid-dex/hyperliquid-python-sdk</a>

2.  **代码分支** <a href="https://github.com/orgs/hyperliquid-dex/repositories" class="external-link" data-card-appearance="inline" data-local-id="a3098895-74ee-44f8-a059-3e89a61772ad" rel="nofollow">https://github.com/orgs/hyperliquid-dex/repositories</a>

3.  **API文档** <a href="https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api" class="external-link" data-card-appearance="inline" data-local-id="a4abf8fc-8736-4f6f-af8c-cb4c27b17565" rel="nofollow">https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api</a>

# 一、各图表详细规范

## 顶部关键指标卡片（5x）

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="47dc98d22e35037518d203080f7497cb2f90f575b6acc6026f0493cd97a4ccc8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202025-12-31%20at%2017.20.31.png?version=1&amp;modificationDate=1767172861510&amp;cacheVersion=1&amp;api=v2" data-height="254" data-width="1304" data-unresolved-comment-count="0" data-linked-resource-id="61211336" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-31 at 17.20.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="0eee7285-ab26-4e34-b266-1ba33bd4fcb8" data-media-type="file" width="468" height="91" alt="Screenshot 2025-12-31 at 17.20.31.png" /></span>

**标题：**Dashboard

**可信标记：**Checkpoint `xxx` (`YYYY-MM-DD HH:MM:SS`)

- `XXX`:检查点 点击另起标签页跳转到explorer

- `YYYY/MM/DD HH:MM:SS`：UTC转用户机器时间

**指标卡片**:

</div>

</div>

</div>

<div class="columnLayout three-equal" layout="three-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

Total Volume

总累计的交易+流动性操作量

24H变化值

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Open Interest

最近一次快照的总持仓名义价值

24H变化值

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

Total Users

总累计去重后的用户数量

24H变化值

Total Value Locked

最近一次快照的池子内总流动性

24H变化值

Total Fees

总累计手续费收入

24H变化值

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**更新频率**: 1h（与图表一致即可）

**数据展示：**美元；KMB；2dp；CHG绿涨红跌

## 各指标对应图表（12x）

### 0. 筛选器交互说明（后续不再赘述，只说明特殊处理）

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="221cad008370fe2ff14c5e334a5273f7746ff073c409a2272666d89dcd54f7b0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202025-12-31%20at%2018.43.33.png?version=1&amp;modificationDate=1767177844158&amp;cacheVersion=1&amp;api=v2" data-height="862" data-width="1222" data-unresolved-comment-count="0" data-linked-resource-id="61178598" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-31 at 18.43.33.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="4e902fb1-2862-4c6a-af76-5618063ec2bb" data-media-type="file" width="468" height="330" alt="Screenshot 2025-12-31 at 18.43.33.png" /></span>

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="30c9fbd8-55cb-486c-a05b-9653d2aabe2a">
<tbody>
<tr data-local-id="4aaeeafd-7e96-4795-a672-1282b427a766">
<th class="confluenceTh" data-local-id="e40b8ff9-ba65-46be-85bd-1f8d42d0d609"><p>模块</p></th>
<th class="confluenceTh" data-local-id="b57adffb-0775-4249-b428-93ff3557c536"><p>规则 / 说明</p></th>
</tr>
&#10;<tr data-local-id="4495a9c9-4ee2-4f97-afe8-bea024dd3da3">
<td class="confluenceTd" data-local-id="145303ca-70ab-4364-a461-a93c7f31dc47"><p><strong>整体说明</strong></p></td>
<td class="confluenceTd" data-local-id="2d23be70-0235-4ebf-8271-c8e2db7eb60c"><ol>
<li><p><strong>筛选器组成：三者联动</strong></p>
<ol>
<li><p>View by：展示维度 单选</p></li>
<li><p>Selected：不同维度下多选</p></li>
<li><p>Period：时间 - 7天/30天/90天/365天/所有</p></li>
</ol></li>
<li><p><strong>联动规则：</strong>View by 决定 Selected 形态；任一变化触发数据刷新</p>
<ol>
<li><p><strong>View by 切换：</strong>Selected 自动恢复该模式默认值</p></li>
<li><p><strong>Period 切换：</strong>不影响</p></li>
<li><p><strong>View by - Selected：</strong>All - All，禁用下拉框；Asset Types / Pairs - <code>选中数量 + Types </code><strong>/</strong> <code>选中币对 + Pairs</code>，下拉框可多选</p></li>
</ol></li>
<li><p><strong>交互状态：</strong></p>
<ol>
<li><p>点击展开选项列表</p></li>
<li><p>选中项高亮显示</p></li>
<li><p>选择后自动关闭并更新图表</p></li>
<li><p>数据加载中筛选器可操作，图表区显示 Loading</p></li>
<li><p>reset：点击回到<strong>默认状态 View by = All （📝</strong>这里指的是<strong>筛选器的reset</strong>，不是<strong>下拉框的reset）</strong></p></li>
</ol></li>
<li><p><strong>用色说明：</strong></p>
<ol>
<li><p>图表中未选中的others同一用白/黑/灰色</p></li>
<li><p>不同资产下有十个不同色块，按市场中的字母顺序依次循环分配，如图所示，三套循环：</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3dc9e0cb385ef81f5e478180b0ee128c1b159acdc91b0403e9c1a3398b605010" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2017.00.52.png?version=1&amp;modificationDate=1767690057360&amp;cacheVersion=1&amp;api=v2" data-height="278" data-width="328" data-unresolved-comment-count="0" data-linked-resource-id="63537238" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 17.00.52.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="5cf18b7a-1769-481e-8342-591be6435e39" data-media-type="file" width="328" height="277" alt="Screenshot 2026-01-06 at 17.00.52.png" /></span></p></li>
</ol></li>
</ol></td>
</tr>
<tr data-local-id="7206a974-c97c-41ce-bd8b-64172d8dc7b4">
<td class="confluenceTd" data-local-id="e79539ee-4d4e-41fd-98da-453fca72f820"><p><strong>View by</strong></p></td>
<td class="confluenceTd" data-local-id="b6605927-f724-42a7-924c-acffc7e6f940"><ol>
<li><p><strong>类型：单选</strong> 控制数据聚合维度</p></li>
<li><p><strong>枚举：</strong><code>All</code>（默认） / <code>Asset Types</code> / <code>Pairs</code></p>
<ol>
<li><p>注意这里非通用，部分表格不涉及asset type/pairs。</p></li>
</ol></li>
<li><p><strong>交互状态：</strong>切换时 <strong>重置 Selected 为该维度默认状态</strong></p></li>
</ol></td>
</tr>
<tr data-local-id="28f82b23-e982-47ee-9e53-1d973c670308">
<td class="confluenceTd" data-local-id="33f1ae7c-5e90-4a25-98c0-0153cbca81fd"><p><strong>Selected</strong></p></td>
<td class="confluenceTd" data-local-id="5b4bb64f-2fa9-46b0-b7f5-4f4938aad946"><ol>
<li><p><strong>类型：下拉多选</strong></p></li>
<li><p><strong>标题：</strong><code>All</code> <strong>/</strong> <code>选中数量 + Types </code><strong>/</strong> <code>选中币对 + Pairs</code> ,分别对应 <strong>View By = All / Asset Types /Pairs</strong></p></li>
<li><p><strong>交互：</strong></p>
<ol>
<li><p>点击展开；<span style="background-color: rgb(254,222,200);">最大高度</span>设计规定，超出滚动</p></li>
<li><p><strong>分区 - Selected（上）</strong> / <strong>Others（下）</strong></p>
<ol>
<li><p><strong>排序：</strong>按各自规则 - <code>View by = Asset Type</code>按<strong>固定顺序</strong>，<code>View by = Pairs</code>按首字母顺序。</p></li>
<li><p><strong>展示：</strong><code>Selected (6)</code>代表选中的数量。Others可不展示数量</p></li>
<li><p><strong>选中/取消：</strong>点击 Selected 区 → 取消选中 → 移至 Others（按排序规则插入）；点击 Others 区 → 选中 → 移至 Selected（按排序规则插入）；操作<strong>不强制滚动</strong>，保持当前视野稳定</p></li>
<li><p><strong>边界：</strong>若全部选中，others与分割线不展示。允许空选，支持 Selected (0)</p></li>
</ol></li>
<li><p><strong>重置：</strong>点击下拉框内重置图标，恢复默认选中</p></li>
</ol></li>
<li><p><strong>状态枚举：</strong></p>
<ol>
<li><p>View by = All 时，Selected = <code>All</code>，下拉框禁用</p></li>
<li><p>View by = Asset Types时，Selected = <code>Crypto</code> / <code>Forex</code> / <code>Equities</code> / <code>Indices</code> / <code>Commodities</code> / <code>Meme</code> / <code>Newly Listed</code> （即，<strong>3.b</strong>中<strong>固定顺序</strong>），<strong>默认选中</strong>除Newly Listed外前六项</p></li>
<li><p>View by = Pairs时，Selected = <code>所有可交易的Market Symbol</code>，按<strong>字母顺序</strong>排序，<strong>默认选中12个 -</strong> BONK/USD, BTC/USD, DOGE/USD, ETH/USD, FARTCOIN/USD, HYPE/USD, PEPE/USD, SHIB/USD, SOL/USD, USD/JPY, WIF/USD, XRP/USD</p></li>
</ol></li>
</ol></td>
</tr>
<tr data-local-id="1b8a96c0-4533-42e7-88e8-281eb10314f8">
<td class="confluenceTd" data-local-id="0ffeda68-1247-4f92-aef2-8c2399b11815"><p><strong>Period</strong></p></td>
<td class="confluenceTd" data-local-id="46ceb30a-52b7-4848-8205-eb86d3891d11"><ol>
<li><p><strong>类型：单选 -</strong> 控制时间聚合粒度</p></li>
<li><p><strong>枚举：</strong><code>Week</code> / <code>Month</code>（<strong>默认</strong>） / <code>Quarter</code> / <code>Year</code> / <code>All</code></p></li>
<li><p><strong>交互状态：</strong>切换时立即触发数据刷新，不允许空选</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

### 1. Volume - 交互总量图表（注意与3中total trading volume交易总量区分）

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="92e41bda09b2daaa933a1437d58e8d1990473db1dd79336b3786b56e460516f4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202025-12-31%20at%2017.42.37.png?version=1&amp;modificationDate=1767174181805&amp;cacheVersion=1&amp;api=v2" data-height="504" data-width="1004" data-unresolved-comment-count="0" data-linked-resource-id="61178580" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-31 at 17.42.37.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="0721a783-2141-43ad-bc8e-b6f88fb8c871" data-media-type="file" width="468" height="234" alt="Screenshot 2025-12-31 at 17.42.37.png" /></span>

**图表类型**: 堆叠柱状图

**筛选器**:（特殊部分）

- **View by** (不可选) `Action Type`

- **Selected** (不可选)`All`

- **Period** (下拉单选) ⚠️**这里不是全局，每个图表都有，后续不重复叙述**

  - `Week` - 按7天聚合

  - `Month` - 按30天聚合**（默认状态）**

  - `Quarter` - 按90天聚合

  - `Year` - 按年聚合

  - `All` - 全部时间

- **Reset：**点击重置回默认状态。整页刷新同样重置回默认。⚠️**这里不是全局，每个图表都有，后续不重复叙述**

**图表元素**:

- X轴: 时间轴，`MM/DD` - 按周/月/季度/全部时间（上线不满一年）聚合；`YYYY/MM` - 按年/全部时间（上线满一年）聚合（**⚠️其他图表x轴也是一样的 后不赘述**）

- Y轴: 交易总量 (美元, 自动格式化为K/M/B)

- 柱状图: 不同颜色代表不同交易对,从下往上堆叠

- 统计数据tooltip: （原型图位于图表右侧是为了方便看，实际位于图表上层）

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Total`: 当日总交易量

  - `Perps Trading`：永续合约当日总交易量

  - `Liquidity Providing`：流动池（包括vault）总质押的USDC美元价值

  - `Liquidity Removing`：流动池（包括vault）总移除的USDC美元价值

  - `Cumulative`：累计总（**⚠️注意全部数据的每日零点的不要加重了 后续不重复**）

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 每日交易量计算
daily_volume = 当日的sum(Perps Trading + Liquidity Providing + Liquidity Removing）
当日:[0:00 - 23:59)，或者后端自己定
# 每日永续交易量
volume_by_pair = sum(Open Size + Close Size) 加/减/开/平/强平
# 流动性添加/移除
Liquidity Providing/Removing = USDC Amount * USDC Price_上链时的，而非当下的价格
```

</div>

</div>

### 2. Open Interest - 持仓分布

</div>

</div>

</div>

<div class="columnLayout two-right-sidebar" layout="two-right-sidebar">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4e298b4f123fe7803a047267c51bcc3f0aa22a1207dbfe3e72db515040b787f8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202025-12-31%20at%2018.10.46.png?version=1&amp;modificationDate=1767175858693&amp;cacheVersion=1&amp;api=v2" data-height="508" data-width="986" data-unresolved-comment-count="0" data-linked-resource-id="61113079" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-31 at 18.10.46.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="c0120928-5534-4bf7-a02b-35755fd3f500" data-media-type="file" width="468" height="241" alt="Screenshot 2025-12-31 at 18.10.46.png" /></span>

</div>

</div>

<div class="cell aside" data-type="aside">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0b6e460fc3d6e405065e4fdcabc3907ce87d82060e82abe399b3f9ccf33d1556" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2016.11.53.png?version=1&amp;modificationDate=1767600723684&amp;cacheVersion=1&amp;api=v2" data-height="632" data-width="916" data-unresolved-comment-count="0" data-linked-resource-id="61146066" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 16.11.53.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="03848894-46f8-493a-9e48-31b492a8cb8d" data-media-type="file" width="396" height="273" alt="Screenshot 2026-01-05 at 16.11.53.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c743e4099885e02932d2b576ee5c59ce96fd215a032c3683d8439e602e31c192" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2016.17.05.png?version=1&amp;modificationDate=1767601036216&amp;cacheVersion=1&amp;api=v2" data-height="717" data-width="1021" data-unresolved-comment-count="0" data-linked-resource-id="61146075" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 16.17.05.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="7014d86b-077d-45a8-a39c-929c1e010dc8" data-media-type="file" width="356" height="250" alt="Screenshot 2026-01-05 at 16.17.05.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**图表类型**: 堆叠柱状图 + 折线图

**筛选器**:<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89" data-card-appearance="inline" data-local-id="9da9eda5-80c5-4b2b-969e-faf838e5b3a6" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89</a>

**图表元素**:

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

默认**View by all**

- 多头: 绿色柱状图，空头: 红色柱状图

- 单Y轴: 左侧显示，子项的Long OI，Short OI柱状图，daily total流线表示

- 堆叠：按tooltip里的展示顺序**下至上**堆叠

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日持仓总量 美元价值

  - `Long OI`: 当日多头持仓总量 美元价值

  - `Short OI`：当日空头持仓总量 美元价值

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

有筛选**View by asset types/pairs**

- 不分多空，展示选中子项的总OI，未选中的求和并统一记作others 展示在图表以及tooltip中

- 堆叠：按tooltip里的展示顺序**下至上**堆叠

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `选中项1`：当日选中项的持仓总量 美元价值

  - `选中项2`：当日选中项的持仓总量 美元价值

  - `选中项n`：当日选中项的持仓总量 美元价值

  - `Others`: 当日未选中项求和持仓总量 美元价值

  - tooltip选中项1至n的排列顺序即为下拉栏中的排列顺序

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**计算逻辑**: （**⚠️如果有筛选，以下聚合的就是对应选项的总量，后续不赘述）**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
默认View by All
# Long OI 计算
long_oi = sum(Position Size_USD if position.side == 'long')

# Short OI 计算
short_oi = sum(Position Size_USD if position.side == 'short')

# 总持仓
total_oi = Long OI + Short OI
——————————————————————————————————————————————————————————————————————————————————————————
筛选View by Asset Types/Pairs
#选中项OI计算
选中项 OI =  sum(Position Size_USD if position.type == '选中项')

#Others OI计算
Others OI =  sum(Position Size_USD if position.type != '选中项1'，‘选中项2’，..., '选中项n')
```

</div>

</div>

### 3. Total Trading Volume - 总交易量

</div>

</div>

</div>

<div class="columnLayout two-right-sidebar" layout="two-right-sidebar">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="874f186f713b81d96a1345466fe950ea4e1795e752d724075e0e5f67851ee191" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2016.04.57.png?version=1&amp;modificationDate=1767600336751&amp;cacheVersion=1&amp;api=v2" data-height="366" data-width="730" data-unresolved-comment-count="0" data-linked-resource-id="61178838" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 16.04.57.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="43bd63fd-f701-4fb7-8e5f-0d80791f5462" data-media-type="file" width="468" height="234" alt="Screenshot 2026-01-05 at 16.04.57.png" /></span>

</div>

</div>

<div class="cell aside" data-type="aside">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bee514c96e95eecb5c8f7fbacccd4ffb4f45ce5a1736c690b086547c52d5ea52" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2016.31.06.png?version=2&amp;modificationDate=1767601913481&amp;cacheVersion=1&amp;api=v2" data-height="605" data-width="511" data-unresolved-comment-count="0" data-linked-resource-id="61146082" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 16.31.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="ba91bc2b-50c1-4eee-b840-64b328030f15" data-media-type="file" width="221" height="261" alt="Screenshot 2026-01-05 at 16.31.06.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="18ceea41f8e871c774f4b13919dbf7ab25f65940f6e7f8b1d9b8d8cf75f7d7b8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2016.29.53.png?version=2&amp;modificationDate=1767601913742&amp;cacheVersion=1&amp;api=v2" data-height="497" data-width="512" data-unresolved-comment-count="0" data-linked-resource-id="61211628" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 16.29.53.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="88873e11-30cf-4e05-830c-513161b11f35" data-media-type="file" width="221" height="214" alt="Screenshot 2026-01-05 at 16.29.53.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**图表类型**: 柱状图 + 累计折线图

**筛选器**: <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89" data-card-appearance="inline" data-local-id="9e9a37a8-de3f-439b-9c90-1376a47d27e1" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89</a>

**图表元素**:

- 柱状图: 每日交易量；折线图: 累计交易量

- 双Y轴：左Y轴Daily Total，右Y轴累计 Cumulative

- 若有筛选按颜色分。其他总计为others

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日开平仓总量 美元价值

  - `有筛选则展示选中项1至n`：当日选中项的开平仓总量 美元价值

  - `Others：`当日未选中项的开平仓总量 美元价值

  - `Cumulative`: 总累计开平仓总量 美元价值

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 永续交易量计算
daily_trading_volume = sum（open size + close size）- 其中，close包括强平liquidated
```

</div>

</div>

### 4. Ann. Funding Rate - 年化资金费率

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="129f12751f96d8d1223e253e988bbfaf1f8988ef1b4cef1106b3ff76d00e0597" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-05%20at%2018.50.38.png?version=1&amp;modificationDate=1767610243921&amp;cacheVersion=1&amp;api=v2" data-height="651" data-width="956" data-unresolved-comment-count="0" data-linked-resource-id="61211675" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-05 at 18.50.38.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="0aca4e41-f9d6-42ca-b9dd-829755658af3" data-media-type="file" width="468" height="318" alt="Screenshot 2026-01-05 at 18.50.38.png" /></span>

**图表类型**: 折线图

**筛选器**:

1.  **View by**: `Pairs`不可选

2.  **Selected**: `12 Pairs` 默认

**图表元素**:

- 多条折线,每条代表一个交易对的资金费率

- Y轴单位: 百分比 (%)，注意有正有负

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `选中项1至n`年化funding rate：比如，BTC/USD: 8.45%；ETH/USD: -2.31%；SOL/USD: 12.78%

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 年化资金费率计算 - 假设每1小时收取一次资金费率
avg_hourly_rate = sum（hourly funding rate in last 24h）/24 #以小时为单位的加权平均
annual_rate = avg_hourly_rate * 24 * 365 #转化成百分比而非bps
```

</div>

</div>

### 5. Realized PnL - 已实现盈亏

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="fda8240081cab5b358cc2a96bd1e144f983b2eefaf2cb8453943c8de8d9753a2" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.55.17.png?version=1&amp;modificationDate=1767679276312&amp;cacheVersion=1&amp;api=v2" data-height="362" data-width="725" data-unresolved-comment-count="0" data-linked-resource-id="63537155" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.55.17.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="233fce25-6d52-405a-941e-e14bef3ad620" data-media-type="file" width="468" height="233" alt="Screenshot 2026-01-06 at 11.55.17.png" /></span>

**图表类型**: 双向柱状图 + 累计折线图

**筛选器特殊处理：**view by = asset type或pair时，**只支持单选**，其他同<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89" data-card-appearance="inline" data-local-id="a49b6b58-af31-4798-924b-211259167eb4" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89</a>

**图表元素**:

- 盈利柱: 向上柱状图

- 亏损柱: 向下柱状图

- 双Y轴:左侧对应子项的pnl，右侧对应累计总pnl

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Net Profit`：当日总pnl为正时展示在这里，同时当日net loss展示0

  - `Net Loss`：当日总pnl为负时展示在这里，同时当日net profit展示0

  - `Cumulative`：总的累计pnl求和

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 已实现盈亏 = 平仓价 - 开仓价
daily_realized_pnl = sum((close price - entry price)/entry price * size * direction))
其中，direction = 1 for long, -1 for short

# 累计
cumulative_pnl = sum(daily rpnl for all historical dates)
```

</div>

</div>

### 6. Loss Rebate - 损失返还<span colorid="mb267gq57n">（合约尚未补充实现方式，后续可能修改需求）</span>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="13ef497bcd4e2a960ea173bb22b4a4bb2f98a4eb4a5a54cbd841de4f535a4157" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.55.25.png?version=1&amp;modificationDate=1767679888751&amp;cacheVersion=1&amp;api=v2" data-height="366" data-width="761" data-unresolved-comment-count="0" data-linked-resource-id="63537163" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.55.25.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="a09feff5-269e-4958-9e36-81ffb0703dce" data-media-type="file" width="468" height="225" alt="Screenshot 2026-01-06 at 11.55.25.png" /></span>

**图表类型**: 柱状图 + 累计折线图

**筛选器**:<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89" data-card-appearance="inline" data-local-id="8b41d80d-bf94-47a9-862f-4086de5a81ef" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89</a>

**图表元素**:

- 柱状图: 每日损失返loss rebate还总值

- 折线图: 累计损失返还

- 双y轴：左侧对应子项，右侧对应累计 注意loss rebate为平台补贴，永远为非负数。

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日总返还的loss rebate

  - `选中项1至n`：当日筛选器所选中的子项，对应总返还loss rebate

  - `Others`：当日未选中项的loss rebate 加和

  - `Cumulative`：总的累计loss rebate求和

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 损失返还
loss rebate为新增的针对普通杠杆下，开仓时处于OI弱势方，且减仓时rpnl<0的损失补贴一定百分比的机制
返还占比由合约配置，loss_rebate = sum（loss * rebate_rate）
```

</div>

</div>

### 7. Liquidations - 清算数据

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="998820e51c1907c498161cd9f85cc9977ceab784e0e0ebb0adc6f91a4b22dcb5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.55.37.png?version=1&amp;modificationDate=1767681417950&amp;cacheVersion=1&amp;api=v2" data-height="366" data-width="725" data-unresolved-comment-count="0" data-linked-resource-id="63569933" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.55.37.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="f703234d-18a5-4f85-8b58-9706c35e51f8" data-media-type="file" width="468" height="236" alt="Screenshot 2026-01-06 at 11.55.37.png" /></span>

**图表类型**: 柱状图 + 累计折线图

**筛选器**: <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89" data-card-appearance="inline" data-local-id="d3fb80f6-38a1-4f88-8b84-02be9f83e08e" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/61145629#0.-%E7%AD%9B%E9%80%89%E5%99%A8%E4%BA%A4%E4%BA%92%E8%AF%B4%E6%98%8E%EF%BC%88%E5%90%8E%E7%BB%AD%E4%B8%8D%E5%86%8D%E8%B5%98%E8%BF%B0%EF%BC%8C%E5%8F%AA%E8%AF%B4%E6%98%8E%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86%EF%BC%89</a>

**图表元素**:

- 柱状图: 被强平仓位总名义价值；折线图: 累计被强平的名义价值

- 双Y轴：左Y轴Daily Total，右Y轴累计 Cumulative

- 若有筛选按颜色分。其他总计为others

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日被强平名义价值总量 美元价值

  - `有筛选则展示选中项1至n`：当日选中项的强平总量 美元价值

  - `Others：`当日未选中项的强平总量 美元价值

  - `Cumulative`: 总累计强平量 美元价值

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 清算size
daily liquidation size = sum(tnx size｜where type == liquidated && date == target_date)
```

</div>

</div>

### 8. Fees - 平台费用收入<span colorid="qz94hrb95f">（合约尚未补充Profit Sharing实现方式，后续可能修改需求）</span>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="71e08b589765c1971de51b80c9ebbb7feac03dc781c14f1a13032fe43abe2bb0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2014.47.39.png?version=1&amp;modificationDate=1767682072085&amp;cacheVersion=1&amp;api=v2" data-height="375" data-width="727" data-unresolved-comment-count="0" data-linked-resource-id="63537195" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 14.47.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="ee46fdb1-5d8d-4793-9ff7-2e9ab8458986" data-media-type="file" width="468" height="241" alt="Screenshot 2026-01-06 at 14.47.39.png" /></span>

**图表类型**: 堆叠柱状图 + 累计折线图

**筛选器**:

- **View by**: `Fee Type` 不可选

- **Selected**: `All` 不可选

**图表元素**:

- 柱状图: 不同类型的费用下至上堆叠，包括：

  - Trading Fee (开平仓费)

  - Borrow Fee (借贷费)

  - Liquidation Fee (清算费)

  - Profit Sharing (利润分成 - 合约新增针对超高杠杆仓位的机制，抽取一部分利润当手续费)

  - Keeper Fee (Keeper费)

- 折线图：累计

- 双Y轴：左Y轴Daily Total，右Y轴累计 Cumulative

- 统计数据tooltip:

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日手续费收入总量 美元价值

  - `Trading`：开平仓费

  - `Borrow` ：借贷费

  - `Liquidate`：清算费

  - `Profit Sharing` ：利润分成 - 合约新增针对超高杠杆仓位的机制，抽取一部分利润当手续费

  - `Keeper`：Keeper执行费

  - `Cumulative`: 总累计收入 美元价值

**费用计算**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 交易费
trading_fee = Open Fee + Close Fee

# 利润分成
Profit Sharing 合约新增超高杠杆仓位盈利抽成

# 总费用
total_fees = trading_fee + borrow_fee + liquidation_fee + profit sharing + keeper fee
```

</div>

</div>

### 9. Total Value Locked - 显示所有池子总流动性，也就是TVL，随时间的变化

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b11297dc9fa297882cb2ba2f436cad72d8eeb0aabea7460935faf01862b82116" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.55.52.png?version=1&amp;modificationDate=1767683087622&amp;cacheVersion=1&amp;api=v2" data-height="381" data-width="715" data-unresolved-comment-count="0" data-linked-resource-id="63537209" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.55.52.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="83a3d13e-02b6-4e7d-8dc3-94a3dfb3f771" data-media-type="file" width="468" height="249" alt="Screenshot 2026-01-06 at 11.55.52.png" /></span>

**图表类型**: 面积图

**筛选器**:

1.  **View by**: `All` 不可选

2.  **Selected**: `All` 不可选

**图表元素**:

- 渐变面积图

- Y轴: 美元金额

- 统计数据tooltip：

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日tvl快照 美元价值

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# TVL = 所有用户质押流动性的总值
tvl = sum(lp token amount * lp token price）
```

</div>

</div>

### 10. HzLP Price - 代币价格

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bca5cf7fdd7615548755d9394f560d2d20cf4566943a21fa9f1793e698e8d50c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.56.01.png?version=1&amp;modificationDate=1767683417929&amp;cacheVersion=1&amp;api=v2" data-height="498" data-width="749" data-unresolved-comment-count="0" data-linked-resource-id="63438870" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.56.01.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="382bf11a-b7db-4d5a-9f42-b9f846ca5ded" data-media-type="file" width="468" height="311" alt="Screenshot 2026-01-06 at 11.56.01.png" /></span>

**图表类型**: 多折线图

**筛选器**:

1.  **View by**: `Pairs`不可选

2.  **Selected**: `12 Pairs` **默认** 可多选

**图表元素**:

- 多条折线,每条代表一个交易对的价格走势，不同颜色区分不同交易对

- Y轴: 价格

- 数据统计tooltip：

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `池子symbol`：当日某池子的LP价格快照，比如 BTC/USD: 10.42K；DOGE/USD: 5K；ETH/USD: 5K

### 11. Users - 用户统计

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a79c0139fc14e14f39aed2824e123deca1557937c1c3da99b837666f22bf9697" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2015.22.42.png?version=1&amp;modificationDate=1767684173454&amp;cacheVersion=1&amp;api=v2" data-height="364" data-width="734" data-unresolved-comment-count="0" data-linked-resource-id="63438878" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 15.22.42.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="95af3b7d-4ad1-4d3d-a218-c353a4daa840" data-media-type="file" width="468" height="232" alt="Screenshot 2026-01-06 at 15.22.42.png" /></span>

**图表类型**: 堆叠柱状图 + 累计折线图

**筛选器**:

1.  **View by**: `All` 不可选

2.  **Selected**: `All` 不可选

**图表元素**:

- 柱状图: 老用户+新用户 下至上堆叠

- 折线图: 累计去重后总用户数量

- 双Y轴: 左侧 子项；右侧 总累计

- 数据统计tooltip：

  - `YYYY-MM-DD`：鼠标所处x位移对应的日期

  - `Daily Total`：当日去重后的用户数量

  - `Recurring Users`：当日老用户

  - `New Users`：当日新用户

  - `Cumulative`：总累计用户

**计算**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 新用户: 首次交易的用户
new_userss = count(当日与合约交互的独立钱包地址，且为首次)

# 回归用户:
recurring_users = count(当日与合约交互的独立钱包地址，且非首次)

# 累计用户
cumulative_users = count(distinct user_wallet address for all_time)
```

</div>

</div>

### 12. Top 100 Users - 前100用户排行榜

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bcc2c535d09e15b608a612ae0fec9d6d9c7482bc460a0ff56b67639395016ef4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2011.56.14.png?version=1&amp;modificationDate=1767683755740&amp;cacheVersion=1&amp;api=v2" data-height="333" data-width="757" data-unresolved-comment-count="0" data-linked-resource-id="63569957" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 11.56.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="7939af09-b6c1-4e8a-90bd-1ff23b8700ea" data-media-type="file" width="468" height="205" alt="Screenshot 2026-01-06 at 11.56.14.png" /></span>

**表格类型**: 数据表格

**排序器**:

1.  **Trading Volume** 默认选中，且固定为降序排序。

2.  **Net PnL%** 可选，降序排序。**二者不支持同时选中**。

**表格列**:

- 虚拟滚动长列表，最大高度设计规定

- 用户地址：前4+后4

- Trading Volume：永续合约总交易量（开平仓；包括强平）

- Net PnL%：总的已实现收益亏损率

**计算逻辑**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# 交易量
Trading Volume = 该钱包地址的 sum（open size + close size）close这里包括强平

# 平均已实现盈利亏损率
Net PnL% = Sum（平仓时的 Net Value） /sum（平仓时的close size) * 100，包括强平
```

</div>

</div>

## 颜色系统（需要设计整理）

**需求描述：**在一个堆叠柱状图中，按用户所选中的币对展示最多90+个市场，面临以下挑战：

1.  人眼能区分的颜色有限（约15-20种）

2.  小面积色块难以识别

3.  相邻色块容易混淆

4.  需要保持视觉以及对应语义的一致性

**解决方案：分层颜色策略 - 资产类别通过色相区分,市场通过明度区分**

- 每个资产类别分配**一个主色系**

- 资产类别内市场使用该色系的不同明度/饱和度变化的**十个子项**

- 主要市场使用饱和度高的颜色，次要市场使用饱和度低的颜色

- 不同资产下有十个不同色块，按市场中的字母顺序依次循环分配。图表中未选中的others统一用白/黑/灰色。不理解的话见下图，三套循环：

  <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3dc9e0cb385ef81f5e478180b0ee128c1b159acdc91b0403e9c1a3398b605010" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2017.00.52.png?version=1&amp;modificationDate=1767690057360&amp;cacheVersion=1&amp;api=v2" data-height="278" data-width="328" data-unresolved-comment-count="0" data-linked-resource-id="63537238" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 17.00.52.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="5cf18b7a-1769-481e-8342-591be6435e39" data-media-type="file" width="328" height="277" alt="Screenshot 2026-01-06 at 17.00.52.png" /></span>

**色板示例：**<a href="https://claude.ai/public/artifacts/6941c043-8d19-4768-a908-94c76539d89a" class="external-link" data-card-appearance="inline" data-local-id="2bafd228-dda7-42af-90a4-95ba6ea1474b" rel="nofollow">https://claude.ai/public/artifacts/6941c043-8d19-4768-a908-94c76539d89a</a> 可借助AI工具调整，查看效果，并整理。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="85b0a0a77eaf28ebc9bdc36e175a4cb2b320d316ef8afa7a664f4ac14ec3718d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/61145629/Screenshot%202026-01-06%20at%2017.03.13.png?version=1&amp;modificationDate=1767690216490&amp;cacheVersion=1&amp;api=v2" data-height="852" data-width="1153" data-unresolved-comment-count="0" data-linked-resource-id="63537245" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-06 at 17.03.13.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="61145629" data-linked-resource-container-version="1" data-media-id="45d87e0f-1c38-4da0-a226-83915b7d10af" data-media-type="file" width="468" height="346" alt="Screenshot 2026-01-06 at 17.03.13.png" /></span>

</div>

</div>

</div>

</div>

</div>
