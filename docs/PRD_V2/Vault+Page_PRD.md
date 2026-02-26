# Vault Page_PRD

<div class="Section1">

## 一、需求背景

**时间安排：**

- 后端：**下周联调之前接口ready**

- 设计：**周四UI 视觉 ready**

**页面名称**：Vaults\
**模块定位**：项目方/第三方策略聚合池，调用多个pools来综合保证收益率高，风险曝光更均衡防止pools lp的单一市场性风险，一级页面为用户展示池列表，二级页面为用户提供池子详细数据展示以及流动性管理操作。

- 存入或取出资产（Deposit / Withdraw）

- 查看实时表现（TVL、Net APR、exposure）

**核心逻辑**

vault本质上是帮用户用存入的usdc像指数一样购买一群lp。不引入shift概念，前端替用户自动分流，优先存入tvl cap最高的池子。

#### **页面结构**

**很多pools部分的组件可直接复用，逻辑上max withdraw cap & 注入移除流动性分配略有区别，数据上相当于基于pools数据做了个聚合，操作上比pools多了一个替用户分配的流程。**\

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="dfd9f6ad-1911-4737-b64e-b6e97fdb38af">
<tbody>
<tr data-local-id="498c540c-9eb6-4eaf-ad92-298c174b960e">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="778c64b3-5ca2-40b5-aadb-16c18e9fcc58"><p> </p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="d8b7d0f6-aabd-41d2-a53f-bbeea4f41371"><p> </p></th>
</tr>
&#10;<tr data-local-id="f474b9ef-b9cd-4987-967e-0a1d3e88e60b">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="977575b3-c8d7-4d2f-9228-9d0523ab8582"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/52330716/Vault+Page_PRD#%E4%B8%80%E7%BA%A7%E5%88%97%E8%A1%A8%E9%A1%B5" rel="nofollow">一级列表页</a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bbd660d63a24dc1984c1c6997966deef9d6e3a2778f35ce6beea909599234137" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-11%20at%2011.23.24.png?version=2&amp;modificationDate=1765423577917&amp;cacheVersion=1&amp;api=v2" data-height="530" data-width="1273" data-unresolved-comment-count="0" data-linked-resource-id="53575682" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-11 at 11.23.24.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="a2d8c68a-fd52-4cea-94ee-d68ad66848db" data-media-type="file" width="363" height="151" alt="Screenshot 2025-12-11 at 11.23.24.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="31ba527e-75ec-45df-8b88-ef1383236e80"><ol>
<li><p>Overview：TVL, <span style="background-color: rgb(211,241,167);">Total Earned Fees</span>, Your Deposits<span class="inline-comment-marker" data-ref="7f1e32c5-8cdf-4546-882a-8aa66645d69c">, </span><span style="background-color: rgb(211,241,167);"><span class="inline-comment-marker" data-ref="7f1e32c5-8cdf-4546-882a-8aa66645d69c">Your Earnings</span></span><br />
⚠️ <em>排序：RankKey = 0.6 * APY Rank + 0.4 * TVL Rank 升序排列 测试网阶段vault不多，产品可接受后面再支持排序功能</em></p></li>
<li><p>Vault List <span style="background-color: rgb(211,241,167);">Curator</span>, Curator Logo（后续后端加图床）, <span style="background-color: rgb(211,241,167);">Vault Name</span>, <span style="background-color: rgb(211,241,167);">Net APY</span>, TVL, Supply,<span style="background-color: rgb(211,241,167);"> Market Exposure,</span> TVL Cap，Your Holdings</p></li>
</ol>
<blockquote>
<p><strong>Net APY = Fee APY * （1 - Performance Fee Rate）;</strong>其中<strong>Performance Fee</strong>：vault参数，后端配的</p>
<p><strong>Your Holdings = LP Amount * LP Price;</strong> 即二级详情页User Info中的Deposited_USD</p>
</blockquote></td>
</tr>
<tr data-local-id="36879729-7156-4697-838a-f50e5a201b6f">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="2f77e3bf-54ac-4202-8227-9b212a45147f"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/52330716/Vault+Page_PRD#%E4%BA%8C%E7%BA%A7%E8%AF%A6%E6%83%85%E9%A1%B5" rel="nofollow">二级详情页</a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0762629f456acf965151b351b465676d65cf33df5cd38c08013411f3ba80977c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-11%20at%2017.38.47.png?version=1&amp;modificationDate=1765446045503&amp;cacheVersion=1&amp;api=v2" data-height="110" data-width="1126" data-unresolved-comment-count="0" data-linked-resource-id="54132742" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-11 at 17.38.47.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="0cf8958f-4826-44aa-808e-7eece514b51c" data-media-type="file" width="468" height="45" alt="Screenshot 2025-12-11 at 17.38.47.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4706f9a95f5177dc31cd05e04c5900e9d680c5633c3005661ceda1ca6046c417" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-11%20at%2018.53.32.png?version=1&amp;modificationDate=1765450425851&amp;cacheVersion=1&amp;api=v2" data-height="504" data-width="1276" data-unresolved-comment-count="0" data-linked-resource-id="54132796" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-11 at 18.53.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="a00e006f-8831-4cde-a78f-70ec66715259" data-media-type="file" width="468" height="184" alt="Screenshot 2025-12-11 at 18.53.32.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5c0a5bf172810be5c9e1439a56fcede54738e6f65350578294126208bdd1cf3a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.05.39.png?version=1&amp;modificationDate=1765764347945&amp;cacheVersion=1&amp;api=v2" data-height="494" data-width="1263" data-unresolved-comment-count="0" data-linked-resource-id="55410841" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.05.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="d1546118-4fd2-4f23-bd85-b60fee11234d" data-media-type="file" width="468" height="183" alt="Screenshot 2025-12-15 at 10.05.39.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="31cfe9ed4c05dccf87d82558c3f8d836f6bab2b65286d7e76ad5e742a04d38b2" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.22.14.png?version=1&amp;modificationDate=1765765434095&amp;cacheVersion=1&amp;api=v2" data-height="375" data-width="959" data-unresolved-comment-count="0" data-linked-resource-id="55509123" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.22.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="34a2c03f-0d65-4275-92d4-895463728a75" data-media-type="file" width="468" height="183" alt="Screenshot 2025-12-15 at 10.22.14.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="22ac6b9effe6fba02ec9a711f89be0c313aada371f59f134aba93a933e301087" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2011.35.02.png?version=1&amp;modificationDate=1765769750963&amp;cacheVersion=1&amp;api=v2" data-height="388" data-width="1271" data-unresolved-comment-count="0" data-linked-resource-id="55509162" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 11.35.02.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="488fe334-0fe1-4569-a654-34a7177569f5" data-media-type="file" width="241" height="73" alt="Screenshot 2025-12-15 at 11.35.02.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="caa63d958ef17dad17875c623606a13ba991ed8f545c42192cd2c75edd8c721d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2012.58.30.png?version=1&amp;modificationDate=1765774728126&amp;cacheVersion=1&amp;api=v2" data-height="252" data-width="1093" data-unresolved-comment-count="0" data-linked-resource-id="55443652" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 12.58.30.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="99499c4a-56e3-4720-995f-48281be6d4d2" data-media-type="file" width="468" height="107" alt="Screenshot 2025-12-15 at 12.58.30.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="297994d3-3bbc-43bd-a2d0-eabcb671b1ef"><ol>
<li><p>Pool Info：<span style="background-color: rgb(211,241,167);">Vault Name</span>；TVL；Total Earned Fees；Remaining Deposit Cap；Remaining Withdraw Cap<br />
⚠️ <em>后两个参数计算时需用到vault包含的池列表，以及各个池子的Remaining Withdraw Cap</em></p></li>
<li><p>User Info：<span class="inline-comment-marker" data-ref="395a8f01-6112-43e6-8e85-c1041bde92ac">Your Earnings = LP Price Delta * LP amount</span></p></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/52330716#Chart" rel="nofollow"><span style="background-color: rgb(211,241,167);">Charts</span></a><span style="background-color: rgb(211,241,167);">：</span><strong><span style="background-color: rgb(211,241,167);">可选30d/90d/180d时间</span></strong><span style="background-color: rgb(211,241,167);">的TVL, </span><strong><span style="background-color: rgb(211,241,167);">Net </span></strong><span style="background-color: rgb(211,241,167);">APR,以及Market Exposure </span></p>
<ol>
<li><p><strong>TVL图表及右侧卡片数据：</strong></p>
<ol>
<li><p>图表：历史数据，1h更新；<strong>可选30d/90d/180d时间</strong></p></li>
<li><p>卡片数据：TVL Cap = Pool Cap求和，Deposited = TVL求和，Remaining = 二者差值<br />
⚠️ <em>TVL cap计算时需要用到这个vault包含的池子列表，以及各个池子在合约配置的PoolCap</em></p></li>
</ol></li>
<li><p>Net APR图表及右侧卡片数据：</p>
<ol>
<li><p>图表：<strong>Net APR可选30d/90d/180d时间；左上角是计算后的当前的Net APY</strong></p></li>
<li><p>卡片数据：</p>
<ol>
<li><p>Fee APY：不计入PnL的total earned fees算的年化</p></li>
<li><p>Performance Fee Rate：vault参数，后端配的，我们的池子先配成5%</p></li>
<li><p>Performance Fee：Fee APY * Management Fee Rate 带负号</p></li>
<li><p>Net APY = Fee APY + Performance Fee</p></li>
</ol></li>
</ol></li>
<li><p>Market Exposure图表及右侧卡片数据：</p>
<ol>
<li><p>图表：池子占比。（仅展示cap的<strong>前四</strong>，剩余<strong>合并计算</strong>为<strong>others。cap相同时按默认的展示顺序来排列</strong>）。<strong>可选30d/90d/180d时间。</strong>纵轴为<strong>composition = Pool TVL / Vault TVL。hover</strong>里面展示<strong><span style="background-color: rgb(211,241,167);">日期</span></strong><span style="background-color: rgb(211,241,167);">，</span><strong><span style="background-color: rgb(211,241,167);">池子名称，</span></strong><span style="background-color: rgb(211,241,167);">以及</span><strong><span style="background-color: rgb(211,241,167);">百分比</span></strong></p></li>
<li><p><span class="inline-comment-marker" data-ref="5524c5ba-1cb2-4f92-ba3f-1d05fb495110">卡片数据</span>：这里的market跟cap<strong>合约配置</strong>，<span style="background-color: rgb(211,241,167);">展示顺序</span>为：按Cap倒叙，Cap相同按字母顺序</p>
<div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre class="syntaxhighlighter-pre" data-syntaxhighlighter-params="brush: java; gutter: false; theme: Confluence" data-theme="Confluence"><code>HertzFlow Gold Rush
{
1 XAG/USD $10.0m
2 XAU/USD $10.0m
}
&#10;HertzFlow Trending Equities
{
1 QQQ/USD $30.0m
2 SPY/USD $30.0m
3 AAPL/USD $2.0m
4 AMZN/USD $2.0m
5 COIN/USD $2.0m
6 GOOG/USD $2.0m
7 META/USD $2.0m
8 MSFT/USD $2.0m 
9 NVDA/USD $2.0m
10 TSLA/USD $2.0m
}
&#10;HertzFlow Bullish Run
{
1 BTC/USD $30.0m
2 ETH/USD $30.0m
3 BNB/USD $7.5m
4 DOGE/USD $6.0m
5 SHIB/USD $2.0m
6 HYPE/USD $4.0m
7 PENDLE/USD $4.0m
8 ARB/USD $2.0m
9 ARKM/USD $2.0m
}
&#10;HertzFlow Global Macro FX
{
1 USD/JPY $30.0m
2 EURO/USD $20.0m
3 GBP/USD $20.0m
4 USD/CAD $15.0m
}</code></pre>
</div>
</div></li>
</ol></li>
</ol></li>
<li><p><span style="background-color: rgb(211,241,167);">Liquidity History (User &amp; Vault)</span>：同pools prd</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

## 二、需求详情

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

1.  **USD或供应量数据展示精度：**小写 k/m/b；2dp

    1.  适用于：TVL/Fees/Supply/Holdings/HzLP Shares/Value

    2.  *\<e.g.\> \$999.12; \$99.12k; \$999.12m*

2.  **百分数展示精度：**2dp，正负号，负红正绿，属于闭区间（-0.01%，+0.01%）则展示+0.00%或 -0.00%

    1.  适用：APY

</div>

</div>

<style type="text/css">/**/
div.rbtoc1771927721415 {padding: 0px;}
div.rbtoc1771927721415 ul {list-style: none;margin-left: 0px;}
div.rbtoc1771927721415 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1771927721415">

- [页面结构](#VaultPage_PRD-页面结构)
- [一级列表页](#VaultPage_PRD-一级列表页)
  - [Vault Overview](#VaultPage_PRD-VaultOverview)
  - [Vault List](#VaultPage_PRD-VaultList)
- [二级详情页](#VaultPage_PRD-二级详情页)
  - [Vault & User Info](#VaultPage_PRD-Vault&UserInfo)
  - [Chart](#VaultPage_PRD-Chart)
  - [Liquidity Panel](#VaultPage_PRD-LiquidityPanel)
  - [Vault Liquidity History](#VaultPage_PRD-VaultLiquidityHistory)

</div>

### 一级列表页

#### Vault Overview

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c8da00da72cece620bb3032f5dff9b1b3b91243233f03461935ea38134b269e8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-12%20at%2017.18.54.png?version=1&amp;modificationDate=1765531203478&amp;cacheVersion=1&amp;api=v2" data-height="102" data-width="985" data-unresolved-comment-count="0" data-linked-resource-id="54657082" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-12 at 17.18.54.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="f7cf0fa1-81e2-4b07-bda9-5999a3088c2d" data-media-type="file" width="468" height="48" alt="Screenshot 2025-12-12 at 17.18.54.png" /></span>

1.  Title：Vaults

2.  数据同Pools：TVL; Total Earned Fees；Your Deposits；Your Earned Fees **缺省态\$0,杠杠不好看**

#### Vault List

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b933f02d2f0dae6d874389965ec058520ea1a91eeded29f478c49d74bd231e62" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-13%20at%2016.48.10.png?version=1&amp;modificationDate=1765615711679&amp;cacheVersion=1&amp;api=v2" data-height="471" data-width="1237" data-unresolved-comment-count="0" data-linked-resource-id="55410714" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-13 at 16.48.10.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="3e297930-db86-4740-9dd2-0bbae5a5f56a" data-media-type="file" width="468" height="178" alt="Screenshot 2025-12-13 at 16.48.10.png" /></span>

1.  卡片展示顺序：RankKey = 0.6 \* APY Rank + 0.4 \* TVL Rank 升序排列

2.  卡片详情：后端配

    1.  头图（视觉avery负责）

    2.  第三方合作方logo（测试网无第三方，都是我们项目方池子，用hertzflow logo）

    3.  名字：\[合作方名字\] + \[Vault名字\]

        1.  HertzFlow Gold Rush

        2.  HertzFlow Bullish Run

        3.  HertzFlow Trending Equities

        4.  HertzFlow Global Macro FX

    4.  Net APY：**总**值，不仅是费用 - **注意与pools不同，且这里没有tooltip**

    5.  TVL：vault中LP总美元价值

    6.  Supply：vault中LP总数量

    7.  Market Exposure：市场曝光，展示composition比例最高的前三个，多余的表示成**+n**

    8.  Deposited：渲染部分比例 = \[TVL\] / \[TVL Cap之和\]

    9.  Your Holdings：用户钱包持有LP的**USDC**价值 = LP Price \* LP Amount / USDC Price

### 二级详情页

#### Vault & User Info

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0762629f456acf965151b351b465676d65cf33df5cd38c08013411f3ba80977c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-11%20at%2017.38.47.png?version=1&amp;modificationDate=1765446045503&amp;cacheVersion=1&amp;api=v2" data-height="110" data-width="1126" data-unresolved-comment-count="0" data-linked-resource-id="54132742" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-11 at 17.38.47.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="0cf8958f-4826-44aa-808e-7eece514b51c" data-media-type="file" width="468" height="45" alt="Screenshot 2025-12-11 at 17.38.47.png" /></span>

1.  Title：\[Vault Name\]；返回按钮点击当前页面返回一级标签页（不另起新页）

2.  Vault Info：

    1.  TVL：vault里包含的各个池子pool size求和

    2.  Total Earned Fees：<span class="inline-comment-marker" ref="dbe9f1fe-d8fc-4d13-aa73-ab41f91ef5ac">用代币价格变化算的。因为vault里面池子的组成（composition）一直在动态变化，所以无法计算独立的费用。</span>

    3.  剩余可添加/移除流动性上限计算\
        Remaining Deposit Cap：`$280.29m`

        1.  `280.29m`：剩余可质押美元价值，计算为\
            **= min{**Σ(maxBalanceUSD - PoolBalanceUSD), Σ\[(Glv.market.maxBalanceAmount - PoolAmount)\*Pool Token Price\]**}**

            <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b1160a29cb260a12d3edd0ae118fa40c7ae8e5e48017613b54661e83950d784b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.35.14.png?version=1&amp;modificationDate=1765766148770&amp;cacheVersion=1&amp;api=v2" data-height="134" data-width="682" data-unresolved-comment-count="0" data-linked-resource-id="55312526" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.35.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="4e7c266d-76b3-4216-99fc-f9e94b8943d0" data-media-type="file" width="468" height="91" alt="Screenshot 2025-12-15 at 10.35.14.png" /></span>

        2.  hover展示tooltip：\
            `Max USDC liquidity that the vault can currently accept.`\
            `Max USDC in: 281.44m USDC ($280.29m/$100m)`

            1.  括号外`281.44m USDC`：剩余可质押USDC 数量，计算为\
                = `max USDC in_USD` / `USDC Price`

            2.  括号内左边`280.29m`上面的remaining deposit cap

            3.  括号内右边`$100m`：总上限，计算为\
                = **min{**ΣmaxBalanceUSD, Σ\[Glv.market.maxBalanceAmount \*Pool Token Price**}**

    4.  Remaining Withdraw Cap：`$619.71k`

        1.  `$619.71k`：剩余可移除美元价值，相当于各池子的withdraw remaining cap与poolsize两者取最小值再求和，计算为\
            **=** Σ**Min{**Pool Remaing Withdraw Cap, Pool Size**}**

            <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3c18751565fec3bedf11de6c2e6a2efa261f8405a3cac0879b925a429c8d0e4d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.35.24.png?version=1&amp;modificationDate=1765766186032&amp;cacheVersion=1&amp;api=v2" data-height="134" data-width="745" data-unresolved-comment-count="0" data-linked-resource-id="55443604" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.35.24.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="fbb243a0-92f8-498b-abcf-f7c35c80bff8" data-media-type="file" width="468" height="84" alt="Screenshot 2025-12-15 at 10.35.24.png" /></span>

        2.  hover展示tooltip：`Max USDC liquidity that can be redeemed instantly.`\
            `Max USDC out: 617.43m USDC ($619.71k/$100m)`

            1.  括号外`617.43m USDC`：Remaining Withdraw Cap / usdc price

            2.  括号内左边` ($619.71k`：Remaining Withdraw Cap

            3.  括号内右边`/$100m)`：Vault TVL

> 👆 Cap：代表用户最多可新增/移除 LP 的额度，受限于各池子的 **Glv.market.maxBalanceAmount / maxBalanceUSD**。该项数据需在前端**实时展示**，并在用户输入金额时**即时校验**。

3.  Your Holdings：

    1.  Deposits：美元图标 + 用户所持有lp的**usdc价值，计算为**\
        Deposits = LP Amount \* LP Token Price / USDC Price

        1.  缺省态（未连接钱包/无token）：0

    2.  Your Earned Fees: 用户赚到的总手续费收入，蓝色，计算为：\
        **Your Earned Fees** = LP Amount / Pool LP Amount \* Pool Earned Fees

        1.  缺省态：\$0

#### Chart

1.  TVL:

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4706f9a95f5177dc31cd05e04c5900e9d680c5633c3005661ceda1ca6046c417" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-11%20at%2018.53.32.png?version=1&amp;modificationDate=1765450425851&amp;cacheVersion=1&amp;api=v2" data-height="504" data-width="1276" data-unresolved-comment-count="0" data-linked-resource-id="54132796" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-11 at 18.53.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="a00e006f-8831-4cde-a78f-70ec66715259" data-media-type="file" width="468" height="184" alt="Screenshot 2025-12-11 at 18.53.32.png" /></span>

    1.  30D(默认）/90D/180D：切换tabs**保留**选中，整页刷新**不记**状态

    2.  左上角数据，hover tooltip同demo

    3.  Vault Capacity 同demo。TVL Cap = Pool Cap求和，Deposited = TVL，Remaining = 二者差值

2.  Net APR

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5c0a5bf172810be5c9e1439a56fcede54738e6f65350578294126208bdd1cf3a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.05.39.png?version=1&amp;modificationDate=1765764347945&amp;cacheVersion=1&amp;api=v2" data-height="494" data-width="1263" data-unresolved-comment-count="0" data-linked-resource-id="55410841" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.05.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="d1546118-4fd2-4f23-bd85-b60fee11234d" data-media-type="file" width="468" height="183" alt="Screenshot 2025-12-15 at 10.05.39.png" /></span>

    1.  30D(默认）/90D/180D：切换tabs**保留**选中，整页刷新**不记**状态

    2.  左上角数据是计算后的APY，hover tooltip同demo

    3.  Vault Performance：

        1.  Fee APY：费用收入 不算PnL

        2.  Performance Fee Rate：管理费率。协议从利润中抽成的百分比

        3.  Performance Fee：管理费。协议抽成的美元价值

        4.  Net APY：总年化

        5.  计算关系：**Net APY = Fee APY + 带负号的Performance Fee**

3.  Market Exposure

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e3d01e81d4454c24eca87caa2aef3bffc0189cb9ca1a85c808041ef8ac712138" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2014.46.31.png?version=1&amp;modificationDate=1765781222628&amp;cacheVersion=1&amp;api=v2" data-height="437" data-width="1152" data-unresolved-comment-count="0" data-linked-resource-id="55312616" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 14.46.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="2a5cdf6d-bf27-477a-b2fa-04e39d26d698" data-media-type="file" width="468" height="177" alt="Screenshot 2025-12-15 at 14.46.31.png" /></span>

    1.  30D(默认）/90D/180D：切换tabs**保留**选中，整页刷新**不记**状态

    2.  图表：池子占比。（仅展示cap的**前四**，剩余**合并计算**为**others。cap相同时按默认的展示顺序来排列**）。纵轴为**composition = Pool TVL / Vault TVL。hover**里面展示**日期，池子名称，以及百分比**

    3.  卡片数据：字段为Market；TVL/Cap；Comp. 代表意义同demo。展示顺序取自后端。

#### Liquidity Panel

1.  **分配逻辑**

这里校验逻辑同pools，但是比pools多了一个**需要前端帮用户分配流动性到不同池子，并给合约入参**的流程。优先级为**tvl cap大至小，cap相同时按composition大至小的顺序**。分配时留出**10% \* cap**的缓冲。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="31cfe9ed4c05dccf87d82558c3f8d836f6bab2b65286d7e76ad5e742a04d38b2" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2010.22.14.png?version=1&amp;modificationDate=1765765434095&amp;cacheVersion=1&amp;api=v2" data-height="375" data-width="959" data-unresolved-comment-count="0" data-linked-resource-id="55509123" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 10.22.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="34a2c03f-0d65-4275-92d4-895463728a75" data-media-type="file" width="468" height="183" alt="Screenshot 2025-12-15 at 10.22.14.png" /></span>

👆 举例来说，在这个vault里，用户注入1m流动性时，全部给到XAG。注入4m流动性时，先验证4m \< max deposit cap，再按compositoin大至小分配 - 先给 5m \* 90% - 4.37m 到xag，剩下的给到xau。

2.  **页面展示**

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5c5b69f0e3a5313917aa61f5939cbed3704e74c9649f6e63d073633b294926c1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2014.35.00.png?version=1&amp;modificationDate=1765780607555&amp;cacheVersion=1&amp;api=v2" data-height="721" data-width="694" data-unresolved-comment-count="0" data-linked-resource-id="55312603" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 14.35.00.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="bc1350a9-26ac-4b85-917f-b1754712149e" data-media-type="file" width="282" height="292" alt="Screenshot 2025-12-15 at 14.35.00.png" /></span>

    1.  Pay / Receive 不可选

    2.  Receive HzLP 数量 = PayUSD \* （1 - LP Fee Rate）/HzV Price

    3.  LP价格展示/滑点/费率部分不变。**price impact部分展示，判断以及提示先隐藏。**

3.  **状态机（同pools）**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="304c9a7b-8694-44e1-9bbd-d73fbbab8db2">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr data-local-id="ede45925-acf2-4cf7-aabb-ad94de7c5b3c">
<th class="confluenceTh" data-local-id="a444901f-9e25-4eba-b772-337b8024bfbe"><p><strong>状态 State</strong></p></th>
<th class="confluenceTh" data-local-id="7d238b98-7687-4498-9248-9f5d20ccf827"><p><strong>进入条件</strong></p></th>
<th class="confluenceTh" data-local-id="5466e205-e13b-4905-98b2-1aa4b1c0f131"><p><strong>主要行为</strong></p></th>
<th class="confluenceTh" data-local-id="d2a73d25-74b5-424b-9473-4958a650c8f4"><p><strong>按钮状态</strong></p></th>
<th class="confluenceTh" data-local-id="1d04b58c-9568-4b8e-90e3-eaf17d7815d2"><p><strong>下一步状态</strong></p></th>
</tr>
&#10;<tr data-local-id="8c03e58f-7a2f-4097-9a36-b6e57aa8969f">
<td class="confluenceTd" data-local-id="6815ec27-ebaf-4fac-9924-f29852df80cc"><p><code>WALLET_NOT_CONNECTED</code></p></td>
<td class="confluenceTd" data-local-id="9df0aa98-3b78-48fb-ad0a-6a52adfc56ca"><p>wallet == null</p></td>
<td class="confluenceTd" data-local-id="c519e548-47b7-4436-b467-08e4ac27c55b"><p>显示输入框，等待连接钱包</p></td>
<td class="confluenceTd" data-local-id="9f888310-1c77-4cbe-bb91-bf0631a3bb1f"><p><code>Connect Wallet </code>Enabled</p></td>
<td class="confluenceTd" data-local-id="2a36d773-c343-4f49-af7a-853d4de76aaf"><p><code>INPUT_INVALID</code> / <code>INPUT_VALID</code></p></td>
</tr>
<tr data-local-id="88cb94a6-5324-431b-995a-f96e0bdd03f5">
<td class="confluenceTd" data-local-id="9e8a12b3-4126-4e41-b2be-82f381b55f15"><p><code>INPUT_INVALID</code></p></td>
<td class="confluenceTd" data-local-id="1c6868da-e5c0-4327-9487-e5fc2e6d4bba"><ol>
<li><p>任一成立：input ≤ 0｜非法数字｜pool paused</p></li>
<li><p>input &gt; remaining capacity</p></li>
<li><p>input &gt; 钱包余额</p></li>
</ol></td>
<td class="confluenceTd" data-local-id="25fd93fb-7cde-4637-b2a9-45c38b160734"><ol>
<li><p>阻止后续计算</p></li>
<li><p>阻止后续计算</p></li>
<li><p>自动修改成钱包余额，并继续计算。debounce 200ms</p></li>
</ol></td>
<td class="confluenceTd" data-local-id="7b3b14e0-1645-4fa6-a1fd-33069d11cda6"><ol>
<li><p><code>Enter an Amount</code> Disabled</p></li>
<li><p><code>Above Deposit Limit [Deposit Cap_USD]</code>Disabled</p></li>
<li><p>Enabled</p></li>
</ol></td>
<td class="confluenceTd" data-local-id="067105a8-2fee-446b-9193-e558adffd459"><p><code>INPUT_VALID</code></p></td>
</tr>
<tr data-local-id="91383799-7391-41c1-aeba-5fe7bf284470">
<td class="confluenceTd" data-local-id="e4d884eb-21f5-499e-b192-96a89121dd95"><p><code>INPUT_VALID</code></p></td>
<td class="confluenceTd" data-local-id="14a49f2b-66ca-4d5b-9bd1-abf015243a74"><p>输入合法且 &gt;0</p></td>
<td class="confluenceTd" data-local-id="2bd86049-53c9-4eaf-b72a-07c551f97546"><p>触发 Quote 计算</p></td>
<td class="confluenceTd" data-local-id="cbcd89bf-2c40-4486-b636-7354754e9c71"><p><code>Finalizing Quote</code> Disabled + Spinner</p></td>
<td class="confluenceTd" data-local-id="b2da1e42-5a14-425d-b178-127c54984976"><p><code>QUOTE_CALCULATING</code></p></td>
</tr>
<tr data-local-id="1c1d4242-13d2-437d-aacc-5e176ac5f7f0">
<td class="confluenceTd" data-local-id="1d338d69-44f7-4fc1-af87-78972a5efa41"><p><code>QUOTE_CALCULATING</code></p></td>
<td class="confluenceTd" data-local-id="452a0647-709b-4a2e-9cc0-b4734c4637a9"><p>请求 LP_price / output</p></td>
<td class="confluenceTd" data-local-id="5567bef7-f9bd-4806-a3fe-af20662675a6"><p>等待 quote 返回</p></td>
<td class="confluenceTd" data-local-id="2430c655-500f-4ef3-9a62-6bfbc5c6b477"><p><code>Finalizing Quote</code>Disabled + Spinner</p></td>
<td class="confluenceTd" data-local-id="370b3304-00d3-4576-ac25-e20fa72d1248"><p><code>NEED_APPROVAL</code> / <code>READY_TO_DEPOSIT</code> / <code>INPUT_INVALID</code></p></td>
</tr>
<tr data-local-id="31bad25f-a423-46c3-b216-57d39e98c321">
<td class="confluenceTd" data-local-id="b6a958ce-7ab0-440d-a62f-969812e7c289"><p><code>NEED_APPROVAL</code></p></td>
<td class="confluenceTd" data-local-id="ed18e282-79cd-4c72-b9ef-f3fbd90712f7"><p>allowance &lt; input</p></td>
<td class="confluenceTd" data-local-id="f0760414-e8a1-4d76-91a5-03d78f853b5c"><p>等待用户点击 approve</p></td>
<td class="confluenceTd" data-local-id="9864395a-acc7-446f-b32b-47826ee04bfa"><p><code>Approve USDC Spending</code>（Enabled）</p></td>
<td class="confluenceTd" data-local-id="df3c2f96-9d12-4c9a-abd7-17b98af19ce4"><p><code>APPROVING</code></p></td>
</tr>
<tr data-local-id="53f2ba28-15dd-46e3-8da8-059382d0adb8">
<td class="confluenceTd" data-local-id="9a557a8c-d9a6-48b8-bc2c-f90f3fd88abe"><p><code>APPROVING</code></p></td>
<td class="confluenceTd" data-local-id="1f3c0a55-9de2-411b-9999-aa1faaf5136f"><p>approve tx 已提交</p></td>
<td class="confluenceTd" data-local-id="01745578-416c-4388-aca9-84ae755f9424"><p>调钱包设置中的 allowance</p></td>
<td class="confluenceTd" data-local-id="050df0b1-8bb0-47ef-9902-25030526c9bb"><p><code>Approving </code>Disabled + Spinner</p></td>
<td class="confluenceTd" data-local-id="78b6aee1-85a8-4f5b-a9ca-85150226ee56"><p><code>APPROVE_SUCCESS</code> / <code>NEED_APPROVAL</code></p></td>
</tr>
<tr data-local-id="ec7790a4-f89a-41d6-b5b6-aae343e105ae">
<td class="confluenceTd" data-local-id="115c2a46-6ecf-4814-9811-373fd75a3e2b"><p><code>APPROVE_SUCCESS</code></p></td>
<td class="confluenceTd" data-local-id="f38463be-61a8-4586-a0f8-3a582d498095"><p>allowance ≥ input</p></td>
<td class="confluenceTd" data-local-id="6cc44357-3b47-4c62-95c4-966ed9a2cb94"><p>自动刷新状态</p></td>
<td class="confluenceTd" data-local-id="ee12637f-73bf-4195-93ac-ec144ccd9b71"><p><code>Deposit USDC</code> Enabled</p></td>
<td class="confluenceTd" data-local-id="b23a99e2-9b41-4c0a-b0e5-d9c0d535bc10"><p><code>READY_TO_DEPOSIT</code></p></td>
</tr>
<tr data-local-id="e93fb61c-96e5-4f48-98d9-ce05020806bb">
<td class="confluenceTd" data-local-id="1c285d0c-4883-4e25-b0b0-f7d9acd60536"><p><code>READY_TO_DEPOSIT</code></p></td>
<td class="confluenceTd" data-local-id="1ae36b8e-f405-4b90-a0c1-791f74e4960e"><p>allowance ≥ inputquote valid ≤ 5s</p></td>
<td class="confluenceTd" data-local-id="7460a90e-11d6-4e14-abf6-feb0709f58d0"><p>等待用户确认 deposit</p></td>
<td class="confluenceTd" data-local-id="9e53f813-6969-4164-8dcc-2641d4ca21c2"><p><code>Deposit USDC</code> Enabled</p></td>
<td class="confluenceTd" data-local-id="f5cced15-7c50-496f-9158-2f00e74e3aac"><p><code>DEPOSITING</code> / <code>QUOTE_CALCULATING</code></p></td>
</tr>
<tr data-local-id="32bcc5e3-8618-418b-af5c-85f3ff144bf1">
<td class="confluenceTd" data-local-id="ea74d01d-1899-4522-8abf-240cdcde842a"><p><code>DEPOSITING</code></p></td>
<td class="confluenceTd" data-local-id="7e2d3e23-6994-4ccb-93fa-b1498c0a4b82"><p>deposit tx 已提交</p></td>
<td class="confluenceTd" data-local-id="d2f7f2bf-4df9-43e1-a09f-54259a8c7d21"><p>锁定输入，禁用面板</p></td>
<td class="confluenceTd" data-local-id="00b8fcec-8ab9-43a5-9619-1364e42fb252"><p><code>Depositing USDC</code> Disabled + Spinner</p></td>
<td class="confluenceTd" data-local-id="c6579032-5764-4a82-9388-3d28cd6944d3"><p><code>DEPOSIT_SUCCESS</code> / <code>DEPOSIT_FAILED</code></p></td>
</tr>
<tr data-local-id="307d2b5d-5ac0-4494-966d-0c26374935d3">
<td class="confluenceTd" data-local-id="9243144e-6c0a-45ef-9def-12eb988af7b0"><p><code>DEPOSIT_SUCCESS</code></p></td>
<td class="confluenceTd" data-local-id="ab308b95-bef5-4dc1-9409-d3df697e0eae"><p>Keeper 执行成功事件</p></td>
<td class="confluenceTd" data-local-id="d992a931-a6d5-4857-9fc3-5697cd23abfc"><p>刷新数据、reset input 返还toast</p></td>
<td class="confluenceTd" data-local-id="ea92a823-87a5-41b2-9ac3-8084f7b3ad6a"><p><code>Deposit USDC</code> Enabled</p></td>
<td class="confluenceTd" data-local-id="0493f09c-8d82-473b-a5e5-e1acd879500c"><p><code>INPUT_INVALID</code></p></td>
</tr>
<tr data-local-id="9eba3667-5c33-48c7-a6ff-1221bf2cb8cf">
<td class="confluenceTd" data-local-id="72577816-980b-4bac-afc8-b9ec812b4328"><p><code>DEPOSIT_FAILED</code></p></td>
<td class="confluenceTd" data-local-id="8dbd8038-83b0-471c-9279-a287e94846fd"><p>reject / revert / timeout</p></td>
<td class="confluenceTd" data-local-id="7ce9e9ee-8a38-48a8-9a18-4b796304bf1d"><p>显示失败 toast</p></td>
<td class="confluenceTd" data-local-id="62046d61-cced-448c-a134-8593ddd700d4"><p><code>Deposit USDC</code> Enabled</p></td>
<td class="confluenceTd" data-local-id="641bbf57-1feb-4926-882e-75ac96d6ef96"><p><code>READY_TO_DEPOSIT</code> / <code>NEED_APPROVAL</code></p></td>
</tr>
</tbody>
</table>

</div>

#### Vault Liquidity History

tab 字段My Activity（默认）/ Vault Activity，其他同Pools\
vault activity比my activity多了一列钱包地址，前4 + … + 后4

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="caa63d958ef17dad17875c623606a13ba991ed8f545c42192cd2c75edd8c721d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/52330716/Screenshot%202025-12-15%20at%2012.58.30.png?version=1&amp;modificationDate=1765774728126&amp;cacheVersion=1&amp;api=v2" data-height="252" data-width="1093" data-unresolved-comment-count="0" data-linked-resource-id="55443652" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-15 at 12.58.30.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="52330716" data-linked-resource-container-version="8" data-media-id="99499c4a-56e3-4720-995f-48281be6d4d2" data-media-type="file" width="468" height="107" alt="Screenshot 2025-12-15 at 12.58.30.png" /></span>

</div>
