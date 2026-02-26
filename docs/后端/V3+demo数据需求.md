# V3 demo数据需求

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772008277612 {padding: 0px;}
div.rbtoc1772008277612 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772008277612 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772008277612">

<style>[data-colorid=cuhw5uxera]{color:#4c9aff} html[data-color-mode=dark] [data-colorid=cuhw5uxera]{color:#004eb3}[data-colorid=gkeal1kwlh]{color:#0747a6} html[data-color-mode=dark] [data-colorid=gkeal1kwlh]{color:#5999f8}[data-colorid=zglezkrpkt]{color:#6554c0} html[data-color-mode=dark] [data-colorid=zglezkrpkt]{color:#503fab}[data-colorid=b2b2rbu39y]{color:#6554c0} html[data-color-mode=dark] [data-colorid=b2b2rbu39y]{color:#503fab}[data-colorid=l03npkmkdl]{color:#0747a6} html[data-color-mode=dark] [data-colorid=l03npkmkdl]{color:#5999f8}[data-colorid=g0ylptepdy]{color:#00b8d9} html[data-color-mode=dark] [data-colorid=g0ylptepdy]{color:#26deff}</style>

- [底部导航栏](#V3demo数据需求-底部导航栏)
- [Launch 页](#V3demo数据需求-Launch页)
- [Trade 页](#V3demo数据需求-Trade页)
  - [Trade页面模块划分与数据分层](#V3demo数据需求-Trade页面模块划分与数据分层)
  - [后端数据结构与接口需求表](#V3demo数据需求-后端数据结构与接口需求表)
- [Vault & Pool页](#V3demo数据需求-Vault&Pool页)
  - [Vault & Pool页面模块划分与数据分层](#V3demo数据需求-Vault&Pool页面模块划分与数据分层)
  - [后端数据结构与接口需求表](#V3demo数据需求-后端数据结构与接口需求表.1)

</div>

# 底部导航栏

1.  **Portfolio Tracker 前端写死 固定展示8条 不足时自适应**

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    表头字段：{Asset, Price, 24h CHG, Holdings}

    a16z （默认选中）
    {UNI;$6.73;+14.85%;$430.08M}
    {COMP,$34.77,+4.23%, $9.6M}
    {OP;$0.44;+8.16%;$8.5M}
    {IMAGE；$0.00053；+12.19%；$42.26K}
    {ETH;$3,615.78;+6.4%;$26.2K}
    {MAMA;$0.0093;-0. 082%;$10.07K}
    {TUA;$0.000012;+1.68%;$515.73}
    {UDS;$2.32;+0.87%;$512.53}

    Delphi
    {USDC;$1;+0%;$3.07k}
    {ETH;$3,615.78;+6.4%;$1.25K}
    {OP; $0.44;+6.25%;$1.04k}
    {ZEUM;$0.0009;-0.44%;$863.28}
    {WETH;$3,605.61;+6.02%;$506.24}
    {BNB;$1007.5;+2.08%;$100.57}
    {OHM;$21.34;+0.47%;$46.66}

    Multicoin
    {ACX;$0.076;+8.01%;$1.57M}
    {G;$0.0068;+2.33%;$1.05M}
    {FLY;$0.0027;-1.31%;$53.14K}
    {ETH;$3,615.78;+6.4%;$33.47K}
    {SOMM;$0.0014;+3.61%;$28.13K}
    {OP;$0.44;+8.16%;$1.57K}
    {SALD;$0.0000092;+1.43%;$1.42K}
    {USDC;$1;+0%;$18.51}

    Pantera
    {ONDO;$0.69;+7.37%;$154.6M}
    {USDC;$1;+0%;$5M}
    {INST;$4.11;+10.19%;$1.55M}
    {BGB;$4.13;+4.29%;$454.13K}
    {WETH;$3,605.61;+6.02%;$72.74K}
    {NOTE;$0.013;+6.63%;$60.95K}
    {ETH;$3,615.78;+6.4%;$40.4K}
    {UNI;$6.73;+14.85%;$7.13K}

    Paradigm
    {NRN;$0.025;+5.34%;$119.93K}
    {ETH;$3,615.78;+6.4%;$3.61K}
    {OP;$0.44;+8.16%;$118.82}
    {QWLA;$0.18;+6.07%;$18.13}
    {BNB;$1,008.86;+2.14%;$4.09}
    {HEX;$0.0017;+4.88%;$1.72}

    Yzi Labs
    {1INCH,$0.21,+9.15%;$14.81M}
    {BNB;$1007.5;+2.08%;$15.28K}
    {ETH;$3,615.78;+6.4%;$172.02}
    ```

    </div>

    </div>

2.  **Sector Mover**

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="792cd1ce45bc0858d345baa064539a9e99dc26aa2b067c91b0755eb02dda274d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-10%20at%2015.58.31.png?version=1&amp;modificationDate=1762767948341&amp;cacheVersion=1&amp;api=v2" data-height="432" data-width="1063" data-unresolved-comment-count="0" data-linked-resource-id="35160093" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-10 at 15.58.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="b8c281e1-e016-414b-9c65-e2b9b5a2fc51" data-media-type="file" width="468" height="190" alt="Screenshot 2025-11-10 at 15.58.31.png" /></span>

    1.  写死推荐位：BNB；CHG

    2.  按种类平均CHG的绝对值排序部分：AVG CHG = sum CHG / market amount

    3.  Top Gainer Top Loser分别展示CHG最大及最小的标的D

3.  **News 取后端接口{内容，时间，url}，点击另起标签页跳转至链接**

4.  **Smart Flows 后端接口返还；固定高度展示5条；最多展示all 40条，whale smart flows各20条**

    1.  <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="903ad2aa849495757be48b2f8486436cd22a50ce9593fb6bc7d4519a74a3d4ca" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-10%20at%2017.51.09.png?version=1&amp;modificationDate=1762768303890&amp;cacheVersion=1&amp;api=v2" data-height="464" data-width="444" data-unresolved-comment-count="0" data-linked-resource-id="34865251" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-10 at 17.51.09.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="7846c245-ab50-4c61-a8cd-6aa24f7eadad" data-media-type="file" width="444" height="464" alt="Screenshot 2025-11-10 at 17.51.09.png" /></span>

        <span class="inline-comment-marker" ref="ebc37257-9369-454f-8419-f82c50b7715d">头像前端写死 随机取自(336x336 svg 顺序已随机打乱)</span> <img src="72bf9da988225cdc2a8ad1e12e46fcaf93e902425a623abfe5f4d43ecff7b4c1" style="margin: 2px; border: 1px solid #ddd; box-sizing: border-box; vertical-align: text-bottom;" width="250" height="250" />

    2.  按时间降序排列（新至旧）

5.  **Rankings 前端写死**

    1.  头像同上

    2.  数据

        <div class="code panel pdl" style="border-width: 1px;">

        <div class="codeContent panelContent pdl">

        ``` syntaxhighlighter-pre
        {#1;Ox8E...15A6 ; +$2,055,201}
        {#2;Ox8F...8057;+$501,870}
        {#3;Ox63...29eA;+$274,710}
        {#4;Ox7c...8Fe8;+$176,375}
        {#5;Ox6B...211E;+$139,526}
        {#6;OxFa...ADbE;+$134,809}
        {#7;0xa9...0307;+$108,165}
        {#8;Ox55...806e;+$105,484}
        {#9;Ox2A...1dB1;+$90,803}
        {#10;Ox6e...0578;+$75,467}
        {#100+;0xd0...23e8;+$459}
        ```

        </div>

        </div>

# Launch 页

**Step1. Select Market**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="702c8019ea2b946ffa9d7a190ac11d73e88d9f8ffdef9a1ad7b3300afb762d4e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-06%20at%2011.13.59.png?version=1&amp;modificationDate=1762401097357&amp;cacheVersion=1&amp;api=v2" data-height="649" data-width="986" data-unresolved-comment-count="0" data-linked-resource-id="33488939" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-06 at 11.13.59.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="09b2e7de-63f5-40f9-a7b7-aeb963cd2ad1" data-media-type="file" width="408" height="268" alt="Screenshot 2025-11-06 at 11.13.59.png" /></span>

1.  **Market：前端写死** 单选下拉框 coinlist样式 选项包括以下16个（icon + ticker），字母顺序asc排序\

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    AMZN/USD; ARB/USD; BONK/USD; COIN/USD; ETH/USD; META/USD; MSFT/USD; PENDLE/USD; PEPE/USD; QQQ/USD; SHIB/USD; SPY/USD; WIF/USD; WLD/USD; XAG/USD
    ```

    </div>

    </div>

2.  **Price Oracle：前端写死**，取以下选项9个 字母顺序asc排序

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    Acurast; API3; Chainlink; Band Protocol; DIA; Hertzflow; Pyth Network; SEDA; SupraOracles
    ```

    </div>

    </div>

3.  **多空保证金：前端写死**

    1.   单选下拉框 coinlist样式 选项包括 BNB，BTC，ETH，USDC这四个

    2.  价格会随所选保证金资产以及所选oracle自动变化，不同oracle 对应不同价格，按以下规则写死即可：oracle 6是hertzflow oracle，取oracle price。剩余8个oracle1 -5，7-9，按顺序，oracle price分别在基础上 -0.1%；-0.075%；-0.05%；-0.025%；+0.025%；+0.05%；+0.075%；+0.1%；即可。

4.  风险偏好：**前端写死** low mid high单选，默认low；点击customize出输入框。输入框默认填low的

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    指标字段 Initial TVL；Impact Factor; MMR; Max Leverage
    Low/Customize：10k；50%；4%；25x
    Mid：100k；68%；1%；100x
    High：1m；86%；0.2%；500x
    ```

    </div>

    </div>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b656596ad40f30e3b7625f80f2e5fdaf470176a3abb7da9587b0bc9efe686e97" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-06%20at%2011.14.06.png?version=1&amp;modificationDate=1762401097194&amp;cacheVersion=1&amp;api=v2" data-height="724" data-width="959" data-unresolved-comment-count="0" data-linked-resource-id="33456158" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-06 at 11.14.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="f2d9ddc7-7ab7-42bd-99fb-cdf8b9da63bd" data-media-type="file" width="464" height="350" alt="Screenshot 2025-11-06 at 11.14.06.png" /></span>

5.  池详情 列表

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    以btc市场，多保证金bnb空保证金usdc为例：
    Pool Name: HzGM: BTC/USD [BNB-USDC]

    Pool Detail
    ---------------------------------------
    Market：BTC/USD
    Oracle：2中所选的预言机名称
    Collateral (L-S): BNB-USDC
    Fee:Input Fee Tiers 里面所填写的三个费率

    Risk Config
    ---------------------------------------
    tag:若TVL[0,100k)则为Low-Risk;[100k,1m)则Mid-Risk；[1m,无穷] 为High-Risk
    Risk Level：同标签的判断
    Pool Admin：钱包地址 0xd0888...423E8 （7+5）点击跳转testnet explorer
    Initial TVL：4中所选填初使流动性 $10,000
    Impact Factor：4中所选填百分数
    MMR：4中所选填百分数
    Max Leverage：4中所选填整数
    ```

    </div>

    </div>

6.  注入流动性 & 保证金

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    Paying： 不可选，只能BNB支付 数量+美元价格
    Lock up Period:写死 ~30 days
    Initial Pool TVL: 同上方TVL，美元价值
    Fees：= 1% * TVL 写死，美元价值
    ```

    </div>

    </div>

# Trade 页

## Trade页面模块划分与数据分层

交易页按模块分为以下层级：

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | 描述 | 更新频率 |
| Market Overview | 市场价格、成交量、涨跌幅、OI、可用流动性等 | 实时 |
| Fee Rate Panel | 资金费率与净利率 | 1h |
| Price Chart & Depth | K线与深度图与funding history | 实时 |
| Trade Form | 下单参数与配置 | 实时 |
| Positions / Orders / History | 用户仓位、挂单与历史记录 | 实时 |

</div>

## 后端数据结构与接口需求表

1.  **Market Overview**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a9646f7c-5d98-486e-bbbb-3ede1386954d">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>字段</p></th>
<th class="confluenceTh"><p>含义</p></th>
<th class="confluenceTh"><p>计算逻辑/说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>Market List</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="dcd7f99f7e20de0fc38887e1bb65ab778dd0f0e75f149975eac8f3c655819978" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-05%20at%2011.08.51.png?version=2&amp;modificationDate=1762326278783&amp;cacheVersion=1&amp;api=v2" data-height="774" data-width="837" data-unresolved-comment-count="0" data-linked-resource-id="32505868" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-05 at 11.08.51.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="b1725509-49cb-4db0-abfe-f446bd888682" data-media-type="file" width="236" height="218" alt="Screenshot 2025-11-05 at 11.08.51.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p>市场列表；选择标的，不同标的有不同最大杠杆（风控考量）；支持rwa资产，并根据标签分类</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><ol>
<li><p>支持搜素 搜索逻辑与当前产品站内保持一致</p></li>
<li><p>支持筛选：根据标签过滤展示</p></li>
<li><p>暂时不用支持排序：默认按24h vol desc降序排列</p></li>
<li><p>支持翻页，页面固定展示x个，不足时自适应</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market_Metadata</p></td>
<td class="confluenceTd"><p>包括symbol / icon / max open lev（最大可开仓位杠杆，注意勿与合约MMR的最大杠杆率混淆） / category</p></td>
<td class="confluenceTd"><p><strong>Symbol 后端写死：</strong></p>
<p><a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765" class="external-link" data-card-appearance="inline" rel="nofollow">https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765</a> 表中标绿50个</p>
<p><strong>Icon <span data-colorid="gkeal1kwlh">前端写死</span>：（后端无图床 无法维护）</strong></p>
<p><strong>max open lev后端写死</strong>：</p>
<ol>
<li><p>ETH/BNB/SOL: 500</p></li>
<li><p>山寨币：50</p></li>
<li><p>美股与指数：25</p></li>
<li><p>FX：100</p></li>
<li><p>大宗：50</p></li>
</ol>
<p><strong>Category 后端写死：</strong></p>
<ol>
<li><p>Newly Listed x2 - 第三方白名单创建的市场 <strong>美股与指数各自选一个市场给到第三方自建标签</strong></p></li>
<li><p>Equities</p></li>
<li><p>Indices</p></li>
<li><p>Crypto</p></li>
<li><p>Forex</p></li>
<li><p>Commodities</p></li>
<li><p>Memes</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price_USD</p></td>
<td class="confluenceTd"><p>预言机价格</p></td>
<td class="confluenceTd"><p>美元价格 2dp</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>24h CHG_%</p></td>
<td class="confluenceTd"><p>24小时<strong>mark price</strong>涨跌幅</p></td>
<td class="confluenceTd"><p><strong><span data-colorid="l03npkmkdl">前端计算</span></strong> 百分数 2dp 涨绿跌红 带符号 不足+/-0.01%时展示 +0.00% / - 0.00%</p>
<p><code>24h CHG</code> = 100%x (mark_price - 24h_ago_mark_price) / 24h_ago_mark_price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>24h Vol_USD</p></td>
<td class="confluenceTd"><p>24h 总成交量</p></td>
<td class="confluenceTd"><p><code>24h Vol USD</code> = Σnotional_volume_24h</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>OI Long/Short_USD</p></td>
<td class="confluenceTd"><p>24h 多空持仓总名义价值</p></td>
<td class="confluenceTd"><p><code>OI Long/Short_USD</code> = Σ(long/short open position size) 24h</p>
<p><code>OI_USD</code> = OI Long + OI Short</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>AVLB LIQ Long/Short_USD</p></td>
<td class="confluenceTd"><p>池中剩余可用流动性总和</p></td>
<td class="confluenceTd"><p><code>AVLB LIQ Long/Short_USD</code> = ΣVault_BNB/USDC_avlb liq long/short + ΣGM_BNB/USDC_avlb liq long/short<br />
以BNB/USDC市场举例</p></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>Market Info</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c09e60995e2ed904abcd42941d3fc424cbab23657a36d1b6ca94f8ada5b058a0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-05%20at%2011.09.19.png?version=1&amp;modificationDate=1762312658673&amp;cacheVersion=1&amp;api=v2" data-height="65" data-width="940" data-unresolved-comment-count="0" data-linked-resource-id="32571407" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-05 at 11.09.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="f0820374-15b7-47a9-b4a2-d31ffe7bac00" data-media-type="file" width="468" height="32" alt="Screenshot 2025-11-05 at 11.09.19.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p>市场详情栏</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price &amp; 24h CHG &amp; OI_Long / OI_Short &amp; Avlb Liq Long / Short 同上</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>24h High_USD</p></td>
<td class="confluenceTd"><p>24小时最高<strong>execution price 成交价</strong></p></td>
<td class="confluenceTd"><p>max(<code>exec price</code>) within 24h</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>24h Low_USD</p></td>
<td class="confluenceTd"><p>24小时最低<strong>execution price 成交价</strong></p></td>
<td class="confluenceTd"><p>min(<code>exec price</code>) within 24h</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>OI Long/Short_%</p></td>
<td class="confluenceTd"><p>多空持仓比</p></td>
<td class="confluenceTd"><p><code>OI Long_%</code> = OI Long / OI × 100%</p>
<p><code>OI Short_%</code> = OI Short / OI × 100%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>1h Funding Rate(L/S)_%</p></td>
<td class="confluenceTd"><p>多空动态费率调节（根据OI判断）</p></td>
<td class="confluenceTd"><p><strong>后端</strong></p>
<p>百分数 4dp</p>
<p><code>funding rate long</code> = (OI Short - Long) / OI × 0.006%</p>
<p><code>funding rate short</code> = (OI Long - OI Short) / OI × 0.006%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>1h Borrow Rate_%</p></td>
<td class="confluenceTd"><p>借贷费率</p></td>
<td class="confluenceTd"><p><strong>后端</strong></p>
<p>百分数 4dp</p>
<p><code>borrow rate long</code> = (OI Short - Long) / OI × 0.0032%</p>
<p><code>funding rate short</code> = (OI Long - OI Short) / OI × 0.0032%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>1h Net Rate_%</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>百分数 4dp 正负号 绿红区分</p>
<p><code>1h Net Rate_%</code> = 1h Funding Rate + 1h Borrow Rate</p></td>
</tr>
</tbody>
</table>

</div>

2.  **Positions/Orders/History**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="897da95c-512f-4bd1-b089-c3d7ff1b8200">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>字段</p></th>
<th class="confluenceTh"><p>含义</p></th>
<th class="confluenceTh"><p>计算逻辑/说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>Position</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5dc5788dc457b655c20ca5ad053861015d9fe4263096b46b148681460e3e6d22" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-05%20at%2018.18.17.png?version=1&amp;modificationDate=1762337941767&amp;cacheVersion=1&amp;api=v2" data-height="223" data-width="1404" data-unresolved-comment-count="0" data-linked-resource-id="32604320" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-05 at 18.18.17.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="62edd012-c5a2-4494-91c4-4c6fb8f14a78" data-media-type="file" width="468" height="74" alt="Screenshot 2025-11-05 at 18.18.17.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><ol>
<li><p>新增止盈止损价格编辑弹窗</p></li>
<li><p>mark/liq price放一起</p></li>
<li><p>TP/SL price放一起</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Take Profit Price</p></td>
<td class="confluenceTd"><p>止盈订单价格</p>
<ul>
<li><p>开多：止盈价需&gt;市价</p></li>
<li><p>开空：止盈价需&lt;市价</p></li>
</ul></td>
<td class="confluenceTd"><p>开多：&gt; + 止盈价格</p>
<p>开空：&lt; + 止盈价格</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Stop Loss Price</p></td>
<td class="confluenceTd"><p>止损订单价格</p>
<ul>
<li><p>开多：强平价 &lt; 止损价需 &lt; 市价</p></li>
<li><p>开空：市价&lt; 止损价需 &lt; 强平价</p></li>
</ul></td>
<td class="confluenceTd"><p>开多：&lt; + 止盈价格</p>
<p>开空：&gt; + 止盈价格</p></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>Orders</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4dbaadcd929f8bd9647bd0e2331e314665fd898d9d9a84ff070bbb5839f28bb4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-05%20at%2018.42.58.png?version=1&amp;modificationDate=1762339550354&amp;cacheVersion=1&amp;api=v2" data-height="382" data-width="1427" data-unresolved-comment-count="0" data-linked-resource-id="32604336" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-05 at 18.42.58.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="e0c18ca8-1f23-4aa8-aa7a-0102f94de051" data-media-type="file" width="212" height="56" alt="Screenshot 2025-11-05 at 18.42.58.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p>订单栏</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Side变成Type</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p>不用支持筛选</p></li>
<li><p>Type = Limit / Take Profit / Stop Loss</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Positions</strong></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Type</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p>不用支持筛选</p></li>
<li><p>Type = All / Market / Limit / Take Profit / Stop Loss</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Action</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p>不用支持筛选</p></li>
<li><p>Action = All / Open / Close / Increase / Decrease / Liquidated</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

# Vault & Pool页

## Vault & Pool页面模块划分与数据分层

页面分为三层数据：

1.  **聚合层（Overview）** — 多 Vault 汇总视图（Vaults、TVL、Fees、HzLV Buy/Sell）

2.  **<span colorid="zglezkrpkt">后端mock</span> Vault 层（Vault Detail）** — 单个 Vault 的绩效、构成与指标

3.  **<span colorid="b2b2rbu39y">后端mock</span> 子池层（General Market Pool Detail 1池子支持1个市场）** — 对应 HzGM Pools 或 HzLP 的细分指标

4.  **<span colorid="cuhw5uxera">前端写死</span><span colorid="g0ylptepdy"> </span>用户层 （User Detail）- 用户钱包持有vault与LP token**

## 后端数据结构与接口需求表

1.  **Vault Overview**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="c7bc2b8e-66b9-46f5-a615-dd2f92ad638a">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>字段</strong></p></th>
<th class="confluenceTh"><p><strong>含义</strong></p></th>
<th class="confluenceTh"><p><strong>计算逻辑 / 说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>总可用流动性相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3a0511a2ec31b3693fc0bead428d3e1de69f17dff838252b3ff5bfbf0cab0081" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2017.33.41.png?version=1&amp;modificationDate=1762162431733&amp;cacheVersion=1&amp;api=v2" data-height="193" data-width="893" data-unresolved-comment-count="0" data-linked-resource-id="30670962" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 17.33.41.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="16e815e9-15d7-4e04-93df-573a80d7b7cf" data-media-type="file" width="330" height="71" alt="Screenshot 2025-11-03 at 17.33.41.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL_USD</p></td>
<td class="confluenceTd"><p>当前所有 Vaults 总锁仓量</p></td>
<td class="confluenceTd"><p>= <strong>Σ</strong>Vault TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Total Earned Fees</p></td>
<td class="confluenceTd"><p>累计手续费收入，不含uPnL</p></td>
<td class="confluenceTd"><p>= <strong>Σ</strong>Vault Eearned Fees</p></td>
</tr>
</tbody>
</table>

</div>

2.  **Vault层 - 单vault指标**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="73ed8d20-65d0-4297-896e-120d4b46dab7">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>字段</strong></p></th>
<th class="confluenceTh"><p><strong>含义</strong></p></th>
<th class="confluenceTh"><p><strong>计算逻辑 / 说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>可用流动性相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8378f4a3a0142a33342b17bcd70d80dd7b51e27faa824ad0b1d9d4034223bd73" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2017.22.20.png?version=1&amp;modificationDate=1762161748372&amp;cacheVersion=1&amp;api=v2" data-height="246" data-width="921" data-unresolved-comment-count="0" data-linked-resource-id="30638157" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 17.22.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="2c8dae40-79e1-43f0-bd4f-3a5f0125c2bf" data-media-type="file" width="167" height="44" alt="Screenshot 2025-11-03 at 17.22.20.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Vaults_Metadata</p></td>
<td class="confluenceTd"><p>包括vault_id / name / category</p></td>
<td class="confluenceTd"><p><strong>demo版后端给</strong></p>
<ol>
<li><p>Gauntlet Bullish BNB ｜ Cryptos<br />
BNB-USDC</p></li>
<li><p>MEV Trending RWAs｜Stocks<br />
BNB-USDC</p></li>
<li><p>Steakhouse USDC｜Forex<br />
USDC-USDC</p></li>
<li><p>Hyperithm Gold Rush｜Commod<br />
BNB-BNB</p></li>
</ol>
<p><code>name</code> = 策略名称 + 底层资产</p>
<ul>
<li><p>名称：第三方+策略</p></li>
<li><p>底层资产：Collateral L-S</p></li>
</ul>
<p><code>category</code>：cryptos / forex / stocks / stables / commod</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL_USD</p></td>
<td class="confluenceTd"><p>该vault锁仓量美元价值</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～10m即可</strong></p>
<p>合约返还的<code>Vault AUM_Vault id</code></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Supply_amount</p></td>
<td class="confluenceTd"><p>对应vault token供应量</p></td>
<td class="confluenceTd"><p><strong>后端mock</strong></p>
<p>合约返还的<code>Minted GLV Token Amount_Vault id</code></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price</p></td>
<td class="confluenceTd"><p>对应vault token价格</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～$1.5 - $2之间即可</strong></p>
<p><code>HzVPrice_Vault id</code> = Vault TVL / Vault Supply</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>buyableHzV_USD</p></td>
<td class="confluenceTd"><p>当前可购买 Vault Token 美元价值，及供应量</p></td>
<td class="confluenceTd"><p><code>BuyableHzV_usd</code> = <strong>Σ</strong>（对应市场可分配流动性的TVL Cap - TVL)</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>buyableHzV_amount</p></td>
<td class="confluenceTd"><p>当前可购买 Vault Token 供应量</p></td>
<td class="confluenceTd"><p><code>BuyableHzV_amount </code>= Buyable_usd / Token Price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>sellableHzV_amount</p></td>
<td class="confluenceTd"><p>当前可赎回Vault Token 美元价值</p></td>
<td class="confluenceTd"><p><code>SuyableHzV_usd</code> = 90% × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>SellableHzV_USD</p></td>
<td class="confluenceTd"><p>当前可赎回 Vault Token 数量</p></td>
<td class="confluenceTd"><p><code>SuyableHzV_amount </code>= 90% × TVL / Token Price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>TVL相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e119c19eddc73156259078085d084c3e480c9dd0bc1da2e245a31b528112f3fc" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-04%20at%2015.18.20.png?version=1&amp;modificationDate=1762240797255&amp;cacheVersion=1&amp;api=v2" data-height="200" data-width="982" data-unresolved-comment-count="0" data-linked-resource-id="31555629" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-04 at 15.18.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="0661f85e-c616-418e-97d6-7db508ce3c13" data-media-type="file" width="167" height="33" alt="Screenshot 2025-11-04 at 15.18.20.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL_USD（已有）</p></td>
<td class="confluenceTd"><p>该vault锁仓量美元价值</p></td>
<td class="confluenceTd"><p>TVL = Pool Reserve + Available Liquidity + Liquidity Buffer</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market<span class="inline-comment-marker" data-ref="9ded4dcc-d746-4e10-849f-98dff70847f3"> Open Interest</span></p></td>
<td class="confluenceTd"><p>保留给未结算部分的底层资产美元价值</p></td>
<td class="confluenceTd"><p><code>Market OI</code> = Pool Reserve Long + Pool Reserve Short</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market OI Long_USD</p></td>
<td class="confluenceTd"><p>未结算持仓开多部分pool reserve usd</p></td>
<td class="confluenceTd"><p><code>Market OI Long_USD</code> = Pool Reserve Long</p>
<p><code>Market OI Long_%</code> = Market OI Long / Market OI × 100%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market OI Short_USD</p></td>
<td class="confluenceTd"><p>未结算持仓开空部分pool reserve usd</p></td>
<td class="confluenceTd"><p><code>Market OI Short_USD</code> = Pool Reserve Short</p>
<p><code>Market OI Short_%</code> = Market OI Short / Market OI × 100%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>费用相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="aad6162af9f701b85502b39b8716fd63d43242f4b5050398f1d5884d5475217c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2017.24.21.png?version=1&amp;modificationDate=1762161868508&amp;cacheVersion=1&amp;api=v2" data-height="305" data-width="992" data-unresolved-comment-count="0" data-linked-resource-id="30769204" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 17.24.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="1b7c0443-295d-4d2c-9c9f-d7a4864b7be1" data-media-type="file" width="167" height="51" alt="Screenshot 2025-11-03 at 17.24.21.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Total Earned Fees_usd</p></td>
<td class="confluenceTd"><p>累计手续费收入（开平仓/划转/借贷/清算，不包含uPnL）</p></td>
<td class="confluenceTd"><p><strong>后端mock</strong><br />
合约返还的<code>Vault Earned Fees_Vault id</code></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee APR_24h</p></td>
<td class="confluenceTd"><p>24h总收益率 图表中体现</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～5% 至 20%之间即可</strong></p>
<p><code>NetAPR%_24h </code>= (ΔFee,24h × 365/ TVL_avg24h) × 100%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Yield APY</p></td>
<td class="confluenceTd"><p>第三方策略年化收益（比如闲置资金在morpho开个闪电贷池子的额外收入）</p></td>
<td class="confluenceTd"><p><strong>后端mock，1% 至 5%之间常量</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Management Fee</p></td>
<td class="confluenceTd"><p>管理费</p></td>
<td class="confluenceTd"><p><strong>前端写死，-0% 至 -0.3%之间的常量</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Net APY</p></td>
<td class="confluenceTd"><p>年收益率</p></td>
<td class="confluenceTd"><p><strong>前端计算</strong></p>
<p><code>NetAPY =</code> (1 + APR/365)<sup>365</sup> - 1 +<code> Yield APY</code> + <code>Management Fee</code></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>底层资产相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d436169517f7de056a3c5f74a9035d9f1121bac64216cf0c9c6569c12b819a57" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2017.21.35.png?version=1&amp;modificationDate=1762161703244&amp;cacheVersion=1&amp;api=v2" data-height="244" data-width="934" data-unresolved-comment-count="0" data-linked-resource-id="30769197" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 17.21.35.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="a14eee43-446e-466e-bdb9-4a1b2661781e" data-media-type="file" width="167" height="43" alt="Screenshot 2025-11-03 at 17.21.35.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Collateral Long</p></td>
<td class="confluenceTd"><p>支持开多的保证金标的</p></td>
<td class="confluenceTd"><p><strong>后端</strong></p>
<ol>
<li><p>Gauntlet Bullish BNB ｜ Cryptos<br />
BNB</p></li>
<li><p>MEV Trending RWAs｜Stocks<br />
BNB</p></li>
<li><p>Steakhouse USDC｜Forex<br />
USDC</p></li>
<li><p>Hyperithm Gold Rush｜Commod<br />
BNB</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Collateral Short</p></td>
<td class="confluenceTd"><p>支持开空的保证金标的</p></td>
<td class="confluenceTd"><p><strong>后段</strong></p>
<ol>
<li><p>Gauntlet Bullish BNB ｜ Cryptos<br />
USDC</p></li>
<li><p>MEV Trending RWAs｜Stocks<br />
USDC</p></li>
<li><p>Steakhouse USDC｜Forex<br />
USDC</p></li>
<li><p>Hyperithm Gold Rush｜Commod<br />
BNB</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Current Weightage Long</p></td>
<td class="confluenceTd"><p>当前开多流动性占TVL比</p></td>
<td class="confluenceTd"><p><strong>后端mock，45.00% 至 55.00%之间的常量</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Current Weightage Short</p></td>
<td class="confluenceTd"><p>当前开空流动性占TVL比</p></td>
<td class="confluenceTd"><p>= 1 - current weightage long%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Target Weightage</p></td>
<td class="confluenceTd"><p>50%</p></td>
<td class="confluenceTd"><p>常量 50%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Pool Size Long</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>= current weightage long × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Pool Size Short</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>= current weightage short × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>市场风险敞口相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f05594ba2c6cfd94e747b79afdfac4d0d142e6b2da14681f05d5a9db099b7ace" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2017.21.06.png?version=1&amp;modificationDate=1762161677097&amp;cacheVersion=1&amp;api=v2" data-height="232" data-width="846" data-unresolved-comment-count="0" data-linked-resource-id="30965804" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 17.21.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="78db3aaf-2622-4fc6-a3ff-eb21292e5024" data-media-type="file" width="167" height="45" alt="Screenshot 2025-11-03 at 17.21.06.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market</p></td>
<td class="confluenceTd"><p>该Vault流动性分配至哪几个市场</p></td>
<td class="confluenceTd"><p><strong>Market：Pool Size/Cap Size Composition 后端</strong></p>
<ol>
<li><p>Gauntlet Bullish BNB ｜ Cryptos<br />
BNB-USDC</p>
<ol>
<li><p>BNB/USD: 35%× TVL / $10.0m 35%</p></li>
<li><p>BTC/USD: 30% × TVL / $10.0m 30%</p></li>
<li><p>HYPE/USD: 20% × TVL / $5.0m 20%</p></li>
<li><p>DOGE/USD：15% × TVL / 5.0m 15%</p></li>
</ol></li>
<li><p>MEV Trending RWAs｜Stocks<br />
BNB-USDC</p>
<ol>
<li><p>TSLA/USD: 25%× TVL / $10.0m 25%</p></li>
<li><p>NVDA/USD: 25% × TVL / $10.0m 25%</p></li>
<li><p>AAPL/USD: 25% × TVL / $10.0m 25%</p></li>
<li><p>GOOG/USD：25% × TVL / $10.0m 25%</p></li>
</ol></li>
<li><p>Steakhouse USDC｜Forex<br />
USDC-USDC</p>
<ol>
<li><p>EUR/USD: 35%× TVL / $8.0m 35%</p></li>
<li><p>GBP/USD: 30%× TVL / $6.0m 30%</p></li>
<li><p>USD/JPY: 25%× TVL / $4.0m 25%</p></li>
<li><p>USD/CAD: 10%× TVL / $4.0m 10%</p></li>
</ol></li>
<li><p>Hyperithm Gold Rush｜Commod<br />
BNB-BNB</p>
<ol>
<li><p>XAU/USD: 65%× TVL / $20.0m 65%</p></li>
<li><p>BTC/USD: 20% × TVL / $15.0m <del>20</del>35%</p></li>
<li><p><del>USOILSPOT/USD: 15% × TVL / $10.0m 15%</del></p></li>
</ol></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL</p></td>
<td class="confluenceTd"><p>当前</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Cap</p></td>
<td class="confluenceTd"><p>TVL</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Composition</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

3.  **子池层**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="7048bd6c-2afb-45cd-b0a4-0ae5d742d8bf">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>字段</strong></p></th>
<th class="confluenceTh"><p><strong>含义</strong></p></th>
<th class="confluenceTh"><p><strong>计算逻辑 / 说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Pool Overview总览</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d014a215e92f67a27462cdf221ad26605b05b1208de4fde1e3c86044454f23f6" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2018.17.36.png?version=1&amp;modificationDate=1762165065719&amp;cacheVersion=1&amp;api=v2" data-height="249" data-width="534" data-unresolved-comment-count="0" data-linked-resource-id="30670970" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 18.17.36.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="8d494fa6-231c-439b-a92f-c94dc76bba8a" data-media-type="file" width="167" height="77" alt="Screenshot 2025-11-03 at 18.17.36.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL_USD</p></td>
<td class="confluenceTd"><p>当前所有 Pools 总锁仓量</p></td>
<td class="confluenceTd"><p>= <strong>Σ</strong>HzGM TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Total Earned Fees</p></td>
<td class="confluenceTd"><p>累计手续费收入，不含uPnL</p></td>
<td class="confluenceTd"><p>= <strong>Σ</strong>HzGM Eearned Fees</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>单HzGM池详情</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1f8ea339df39b638454a4462cf4a04349f03e29b05d6ee300e0f0ee80e54e919" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2018.29.47.png?version=1&amp;modificationDate=1762165803013&amp;cacheVersion=1&amp;api=v2" data-height="215" data-width="937" data-unresolved-comment-count="0" data-linked-resource-id="30769223" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 18.29.47.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="b6bf0714-2b04-40ff-9aa8-b094317d558b" data-media-type="file" width="167" height="38" alt="Screenshot 2025-11-03 at 18.29.47.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4fceb62f43a9b5b15f05c9eb50654ad966bd543935b989ed377a0a995219c9a7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2018.30.18.png?version=1&amp;modificationDate=1762165825334&amp;cacheVersion=1&amp;api=v2" data-height="607" data-width="817" data-unresolved-comment-count="0" data-linked-resource-id="30769230" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 18.30.18.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="6b8a7b0b-f714-47a6-ab95-ba322504684c" data-media-type="file" width="167" height="124" alt="Screenshot 2025-11-03 at 18.30.18.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Pool_Metadata</p></td>
<td class="confluenceTd"><p>包括pool_id / name</p></td>
<td class="confluenceTd"><p><strong>demo阶段放15个，后端写死，见下方列表：</strong></p>
<p><code>name</code> = HzGM + 市场symbol + 底层资产</p>
<blockquote>
<p>e.g. HzGM: BNB/USDC [BNB-USDC]</p>
<p>代表仅针对BNB/USDC市场，且保证金为多BNB空USDC的隔离HzGM池</p>
</blockquote>
<p><strong>HzGM列表：</strong>（下面名称中不再重复叙述HzGM）</p>
<ol>
<li><p>BNB/USD [BNB-USDC]</p></li>
<li><p>BTC/USD [BNB-USDC]</p></li>
<li><p>HYPE/USD [BNB-USDC]</p></li>
<li><p>DOGE/USD [BNB-USDC]</p></li>
<li><p>TSLA/USD [BNB-USDC]</p></li>
<li><p>NVDA/USD [BNB-USDC]</p></li>
<li><p>APPL/USD [BNB-USDC]</p></li>
<li><p>GOOG/USD [BNB-USDC]</p></li>
<li><p>EUR/USD [USDC-USDC]</p></li>
<li><p>GBP/USD [USDC-USDC]</p></li>
<li><p>USD/JPY [USDC-USDC]</p></li>
<li><p>USD/CAD [USDC-USDC]</p></li>
<li><p>XAU/USD [BNB-BNB]</p></li>
<li><p>BTC/USD [BNB-BNB]</p></li>
<li><p><del>USOILSPOT/USD [BNB-BNB]</del></p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL_USD</p></td>
<td class="confluenceTd"><p>该pool锁仓量美元价值</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～50m即可</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Supply_amount</p></td>
<td class="confluenceTd"><p>对应HzGM token供应量</p></td>
<td class="confluenceTd"><p><strong>后端mock</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price</p></td>
<td class="confluenceTd"><p>对应lp token价格</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～$1 - $5之间即可</strong></p>
<p><code>HzVPrice</code> = Pool TVL / Pool Token Supply</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>buyableHzGM_USD</p></td>
<td class="confluenceTd"><p>当前可购买 Pool Token 美元价值，及供应量</p></td>
<td class="confluenceTd"><p><code>BuyableHzV_usd</code> = 100m - TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>buyableHzGM_amount</p></td>
<td class="confluenceTd"><p>当前可购买 Vault Token 供应量</p></td>
<td class="confluenceTd"><p><code>BuyableHzV_amount </code>= Buyable_usd / Token Price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>sellableHzGM_amount</p></td>
<td class="confluenceTd"><p>当前可赎回Vault Token 美元价值</p></td>
<td class="confluenceTd"><p><code>SuyableHzGM_usd</code> = 90% × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>SellableHzGM_USD</p></td>
<td class="confluenceTd"><p>当前可赎回 Vault Token 数量</p></td>
<td class="confluenceTd"><p><code>SuyableHzGM_amount </code>= 90% × TVL / Token Price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Total Earned Fees_usd</p></td>
<td class="confluenceTd"><p>累计手续费收入（开平仓/划转/借贷/清算，不包含uPnL）</p></td>
<td class="confluenceTd"><p><strong>后端mock</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee APR_24h</p></td>
<td class="confluenceTd"><p>24h总收益率 图表中体现</p></td>
<td class="confluenceTd"><p><strong>后端mock，量级 ～5% 至 25%之间即可</strong></p>
<p><code>NetAPR%_24h </code>= (ΔFee,24h × 365/ TVL_avg24h) × 100%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee APY</p></td>
<td class="confluenceTd"><p>年收益率</p></td>
<td class="confluenceTd"><p><strong>前端计算</strong></p>
<p><code>FeeAPY =</code> (1 + APR/365)<sup>365</sup> - 1</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Collateral Long</p></td>
<td class="confluenceTd"><p>支持开多的保证金标的</p></td>
<td class="confluenceTd"><p><strong>后端 按HzGM列表来，中括号中前面的标的就是</strong></p>
<ol>
<li><p>BNB/USD [<strong>BNB</strong>-USDC]</p></li>
<li><p>BTC/USD [<strong>BNB</strong>-USDC]</p></li>
<li><p>HYPE/USD [<strong>BNB</strong>-USDC] 等等</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Collateral Short</p></td>
<td class="confluenceTd"><p>支持开空的保证金标的</p></td>
<td class="confluenceTd"><p><strong>后端 按HzGM列表来，中括号中后面的标的就是</strong></p>
<ol>
<li><p>BNB/USD [BNB-<strong>USDC</strong>]</p></li>
<li><p>BTC/USD [BNB-<strong>USDC</strong>]</p></li>
<li><p>HYPE/USD [BNB-<strong>USDC</strong>] 等等</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price Long</p></td>
<td class="confluenceTd"><p>开多流动性Collateral Long的标的价格</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price Short</p></td>
<td class="confluenceTd"><p>开空流动性Collateral Short 标的价格</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Current Weightage Long</p></td>
<td class="confluenceTd"><p>当前开多流动性占TVL比</p></td>
<td class="confluenceTd"><p><strong>后端mock，45.00% 至 55.00%之间的常量</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Current Weightage Short</p></td>
<td class="confluenceTd"><p>当前开空流动性占TVL比</p></td>
<td class="confluenceTd"><p>= 1 - current weightage long%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Target Weightage</p></td>
<td class="confluenceTd"><p>50%</p></td>
<td class="confluenceTd"><p>常量 50%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL Long</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>= current weightage long × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>TVL Short</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>= current weightage short × TVL</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Supply Long</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>TVL Long / Price Long</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Supply Short</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>TVL Short / Price Short</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Utilization Long</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>后端mock，10.00% 至 50.00%之间的常量</strong></p>
<p>1 - Pool Available Liquidity Long / Pool AUM</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Utilization Short</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>后端mock，10.00% 至 50.00%之间的常量</strong></p>
<p>1 - Pool Available Liquidity Short / Pool AUM</p></td>
</tr>
</tbody>
</table>

</div>

4.  **用户层 - 用户个人持有vault/LP token相关数据**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="5305dfba-450f-4713-b4c6-06044aff8b5c">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>字段</strong></p></th>
<th class="confluenceTh"><p><strong>含义</strong></p></th>
<th class="confluenceTh"><p><strong>计算逻辑 / 说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Vault相关</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="108d7721e3981349fcd5344ae11d54240b4eaa0301ffe1b9a4dd9a9667eb4faf" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2019.03.26.png?version=1&amp;modificationDate=1762167899124&amp;cacheVersion=1&amp;api=v2" data-height="503" data-width="959" data-unresolved-comment-count="0" data-linked-resource-id="30769240" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 19.03.26.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="4748d8aa-34ba-4603-a578-cbafcb3320f1" data-media-type="file" width="167" height="87" alt="Screenshot 2025-11-03 at 19.03.26.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="50e548874b50e506e6227d0c782e496f08a456ad1856cf54674b43c170eb28e0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/30703625/Screenshot%202025-11-03%20at%2019.08.55.png?version=1&amp;modificationDate=1762168168503&amp;cacheVersion=1&amp;api=v2" data-height="114" data-width="932" data-unresolved-comment-count="0" data-linked-resource-id="30638201" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-03 at 19.08.55.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="30703625" data-linked-resource-container-version="22" data-media-id="75bf05d7-b1eb-4370-b96b-1abe0ff0c77c" data-media-type="file" width="167" height="20" alt="Screenshot 2025-11-03 at 19.08.55.png" /></span></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>My Total Deposits_USD</p></td>
<td class="confluenceTd"><p>该用户当前所有 Vaults 总锁仓量</p></td>
<td class="confluenceTd"><p><strong>前端写死</strong></p>
<p>= <strong>Σ</strong>My Deposits</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>My Total Earned Fees</p></td>
<td class="confluenceTd"><p>该用户所有Vaults 累计手续费收入，不含uPnL</p></td>
<td class="confluenceTd"><p><strong>前端写死</strong></p>
<p>= <strong>Σ</strong>My Eearned Fees</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>My Deposits_USD</p></td>
<td class="confluenceTd"><p>该用户当前Vaults 锁仓量</p></td>
<td class="confluenceTd"><p><strong>前端写死，0.00% 至 1.00%之间的常量乘对应Vault的TVL</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>My Earned Fees</p></td>
<td class="confluenceTd"><p>该用户当前Vaults 累计手续费收入，不含uPnL</p></td>
<td class="confluenceTd"><p><strong>前端写死，同样的常量乘对应Vault的Earned Fees</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Pool 相关同上</strong></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

</div>
