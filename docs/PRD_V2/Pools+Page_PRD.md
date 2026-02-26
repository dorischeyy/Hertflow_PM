# Pools Page_PRD

<div class="Section1">

todo：

- 技术

  - 【合约排期&分工】price impact机制：合约wrap一层private调用 deposit跟withdraw时自动分流

    - 验证合约是否支持自动平衡（e.g. 流动性10M：8M，用户质押4M流动性时自动分流：3M空1M多）

    - price impact在此机制下计算结果是否永远为正

  - <span class="inline-comment-marker" ref="89a5dcba-b9e2-44d1-a729-e129ef9190d0">【Error Mapping（本版本不包含）】后端监听合约抛出事件，根据维护的error mapping表格解析selector并map到语义化error code，推送给前端调用</span>

- 产品

  - 【**Shift**】Pool二级页**不支持Shift操作** 不对用户强调这一概念，由后端bot统一管理。

  - 【**二级页面图表**】确认fee apr 还是apr - **fee apr 不含uPnL**

  - **【Pool List】后端维护，后续涉及launch market方便管理**

## 一、需求背景

**页面名称**：Pools\
**模块定位**：单市场隔离流动性池，一级页面为用户展示池列表，二级页面为用户提供池子详细数据展示以及流动性管理操作。

- 存入或取出资产（Deposit / Withdraw）

- 查看实时表现（TVL、APR）

**核心逻辑：**

> 详解请移步至<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#3.1.3-Deposit-%2F-Mint" data-linked-resource-id="32571463" data-linked-resource-version="48" data-linked-resource-type="page">kayce文档</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
用户（LP） 
   ├── 提供流动性到 HzLP（Single market）  
   └─> 合约分流：保证永远自动再平衡池子到1:1，同时添加/移除前端需根据pnlfactor & reserve factor做precheck 
交易者 (Trader)
   ├── 在 某市场（HzLP[Market Symbol]）开仓／平仓 → 用此 HzLP的流动性    
   └─> 收益分配给LP：交易产生的open fee + close fee + borrow fee + liquidation fee；以及PnL 
协议／后台  
   ├── 定价机制（Token Price = 池子AUM ÷ 总供应）  
   ├── 再平衡机制（Shift）  
   └── 风险参数详解（前端precheck）
   └────> 1. 最大可质押/提取；池子AUM计算相关：maxPnlFactorForDeposits/Withdrawals/Trades
   └────> 2. Price Impact相关：？
   └────> 3. 最大可质押/提取相关：maxPoolAUM
```

</div>

</div>

1.  **分流机制：**用户质押/移除流动性产品层面不区分多空，由合约自动再平衡多空保证金至1:1。price impact合约写死成0，前端不展示添加/移除保证金时的price impact这个概念。

    1.  **deposit前端precheck：max{**uPnL_Long, uPnL_Short, 0**}** / (Pool_AUM + Deposit) \<= Max_PnL_Factor_For_Deposit 且 Deposit \<= Max USDC in → 才允许操作；注意uPnL为trader在当前市场总的未实现盈亏，带符号。

    2.  **Withdraw前端precheck：max{**uPnL_Long, uPnL_Short, 0**}** / (Pool_AUM - Withdrawal) \<= Max_PnL_Factor_For_Withdraw 且 Withdraw \<= Max USDC out → 才允许操作；注意uPnL为trader在当前市场总的未实现盈亏，带符号。

2.  **maxPnlFactorForDeposits/Withdrawals：**GMX 在 Deposit 与 Withdraw 执行前都会进行一系列安全校验，校验参数为交易者对赌的未实现盈亏占池价值比值**uPnLFactor。**

    1.  **机制：**合约计算的AUM包括uPnL，但为保证LP不亏，把 uPnL 按场景（trade，deposit，withdraw各不相同）施加系数上限，当uPnL超过AUM \* Factor时，会禁止继续开仓/存入/移除。原因在于 LP Token Price = pool_AUM / lp_supply。当池子 uPnL为正且很高时，池子计入这部分uPnL即将造成的LP亏损，此时LP入场一定会赔，因此 GMX 为保护LP会拒绝操作。

    2.  **效果：**这保证了池子在极端市场下仍保持健康，不会因为流动性操作导致 LP、交易者或池子整体风险失控。同时会设置：

        1.  `MAX_PNL_FACTOR_FOR_DEPOSITS` \< `MAX_PNL_FACTOR_FOR_WITHDRAWALS`：deposit 时对负面 PnL 施加更严格的 cap，使得 deposit 时价格更低。这样可以**人为制造“更便宜的入场吸引力”**，在高 uPnL 时吸引存款来补偿风险。反之，withdrawals 用更宽松的 cap，能保护出金者

        2.  `MAX_PNL_FACTOR_FOR_DEPOSIT <= MAX_PNL_FACTOR_FOR_TRADERS` ：**保证 LP 和 Trader 的利润上限保持一致或更低，防止 LP 存款人通过结构性差异薅 Trader 的羊毛**。

3.  **Reserve** 校验**（Withdraw）**

    1.  机制：Withdraw 后，池子需保持足够可用的 token 以覆盖未平仓头寸（OI）。若 OI 占比过高，将拒绝 Withdraw，避免用户取走过多流动性导致剩余 LP 或交易者风险失衡。

    2.  **前端校验逻辑（仅Withdraw）：**

        <span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67">`Withdraw <= AUM`</span><span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67"> - </span>**max**<span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67">`ReservedUsd`</span><span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67"> / </span><span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67">`ReserveFactor`</span> → 才允许操作。这里reservedUSD即为我们所理解的OI，**max**<span class="inline-comment-marker" ref="984321ad-3661-43b1-a117-bae61f0dba67">`ReservedUsd`</span>代表这里取多空OI中更大的一方。

4.  **Max AUM**校验**（Deposit）**

    1.  机制：因为池子是隔离的，所以每个池子最大流动性都有上限来保持池子之间的均衡。如果一个市场的池子无限大：交易者会优先选择这个池子，因为深度更好、滑点更小。导致其他池子流动性不断被抽走。**生态结构失衡**。同时风险参数逻辑都是**比例制**：OI ≤ AUM × factor；pnl ≤ AUM × maxPnlFactor等。如果 **AUM 无限制增长**：即便占比合规（比如 20%），实际金额可能巨大，风险超出预期导致风险参数完全无法覆盖极端情况。所以需要设置**maxAUM**硬顶**，使风险参数始终在有效区间内工作。**

    2.  **前端校验逻辑（仅Deposit）：**Pool_AUM_Usd + Deposit_USD \<= Max_AUM → 允许操作 不分多空

**页面结构：**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="624ae5a8-aabe-4528-897f-6712b722c973">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr data-local-id="c355468b-c263-4a58-870f-149615b601c1">
<th class="confluenceTh" data-local-id="7ba60dd0-763c-4fcf-aa42-4632cb2e48e8"></th>
<th class="confluenceTh" data-local-id="e01865e8-b498-4fe1-8c0a-586a0c01e39a"></th>
</tr>
&#10;<tr data-local-id="a994b085-cfde-429a-a7c7-8a1da1ef76d5">
<td class="confluenceTd" data-local-id="e87d3826-3c75-402a-8144-312101515e75"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#%E4%B8%80%E7%BA%A7%E5%88%97%E8%A1%A8%E9%A1%B5" rel="nofollow"><strong>一级池列表页</strong></a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="cb9c090f5096bec50c1d5b65247693d12b6d88a00d8ad8e89c0ca4be59fca653" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2010.58.08.png?version=1&amp;modificationDate=1763348399823&amp;cacheVersion=1&amp;api=v2" data-height="864" data-width="1359" data-unresolved-comment-count="0" data-linked-resource-id="38010904" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 10.58.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="8e4b2557-d916-4005-bcc1-c19f03381e5a" data-media-type="file" width="468" height="297" alt="Screenshot 2025-11-17 at 10.58.08.png" /></span></td>
<td class="confluenceTd" data-local-id="71a94c9d-95f1-45ce-bc7a-e14ed0cf582f"><ol>
<li><p>Overview</p></li>
<li><p>Pool List<strong>（前端分页，后端支持排序，过滤，搜索。前端url</strong><code>…/pools/[poolAddress]</code><strong>包括合约地址，用户数据及池子数据取后端）</strong></p></li>
</ol></td>
</tr>
<tr data-local-id="6996d05f-3be6-43da-8026-2110a8fd3bd2">
<td class="confluenceTd" data-local-id="f01d7659-b558-4edd-951d-0b34d2dee61f"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#%E4%BA%8C%E7%BA%A7%E8%AF%A6%E6%83%85%E9%A1%B5" rel="nofollow">二级池详情页</a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ca556fb178cb0fdd6835a4904f10617fb3cf2761a2656a83cfdfe52a4662dc16" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2011.42.46.png?version=1&amp;modificationDate=1763351148409&amp;cacheVersion=1&amp;api=v2" data-height="715" data-width="1147" data-unresolved-comment-count="0" data-linked-resource-id="38076446" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 11.42.46.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="ee35b5c4-fa21-45c4-8d66-1f0859baee65" data-media-type="file" width="468" height="291" alt="Screenshot 2025-11-17 at 11.42.46.png" /></span></td>
<td class="confluenceTd" data-local-id="12d08420-de9f-4112-819c-f6566e9e1ef8"><ol>
<li><p>Pool Info (Pool&amp; User取后端)</p></li>
<li><p>Charts (<strong>可选时间</strong>的TVL, APR, Depth 注意APR这里总数据显示<strong>计算得出的APY</strong>，tooltip及图表给的是<strong>APR</strong>)</p></li>
<li><p>Liquidity Panel（<strong>Keeper推送成功/失败事件）</strong></p></li>
<li><p>Liquidity History (User &amp; Pool)</p></li>
</ol></td>
</tr>
<tr data-local-id="dd550bb9-8113-4590-9eb1-8aed4df3aebd">
<td class="confluenceTd" data-local-id="e509b910-1dd7-4c4e-b64a-c43dd9375b89"><p>后续功能新增（不在此次排期）</p></td>
<td class="confluenceTd" data-local-id="66b4828c-a978-42a9-b85d-dc8d68237185"><ul>
<li><p>存入流动性routing？</p></li>
<li><p>Depth Chart：反应用户注入/移除流动性与LP token的price impact关系</p></li>
<li><p>Share Pool：分享海报 赚返佣</p></li>
<li><p>Shift：做Vault页面时再加；Liquidity History同样新增Shift记录；注意问tnx是否遵循原子性</p></li>
<li><p>Error Mapping</p></li>
</ul></td>
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

### 一级列表页

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="d15cf6d4-9109-4578-b0a5-ac096fce141d">
<tbody>
<tr data-local-id="cf191b7f-7305-43dd-a0f4-d36c996a79b1">
<th class="confluenceTh" data-local-id="b9473dcc-ff62-48cd-8578-08d4e1519b7d"><p><strong>模块</strong></p></th>
<th class="confluenceTh" data-local-id="dd7a3728-3e33-4acb-94c1-b395249101e9"><p><strong>需求</strong></p></th>
<th class="confluenceTh" data-local-id="9fee4acb-2d47-4a19-b854-c5c8be426b61"><p><strong>截图</strong></p></th>
</tr>
&#10;<tr data-local-id="4d7dcdfd-0914-4b5b-a222-20b6c2307f19">
<td class="confluenceTd" data-local-id="c0330fed-de66-4058-b6bb-b78e5d77393f"><p>Pool Overview</p></td>
<td class="confluenceTd" data-local-id="7f59fb99-2ef5-4deb-b42e-987280c9b029"><ul>
<li><p>Title：Pools</p></li>
<li><p>Subtitle：Flexible risks. Simple earn.</p></li>
<li><p>Pools数据：</p>
<ul>
<li><p>TVL：Σ所有隔离池TVL_USD加和</p></li>
<li><p>Total Earned Fees_USD：Σ所有隔离池手续费收入加和</p></li>
</ul></li>
<li><p>Your Holdings用户数据：</p>
<ul>
<li><p>Your Deposits_USD：用户所持有lp token总价值</p></li>
<li><p>Your Earned Fees_USD: 用户赚到的总手续费收入</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="64440c5e-1266-4e50-872b-5f4a6636c990"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bdfc71ae6904cfc99cc9d8850aa2f961dbff99c990e3990d4e81ac6897a3499c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2017.19.43.png?version=1&amp;modificationDate=1763371252256&amp;cacheVersion=1&amp;api=v2" data-height="890" data-width="508" data-unresolved-comment-count="0" data-linked-resource-id="39059458" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 17.19.43.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="3874b880-d6c3-465c-91f2-bca6ba54cf7e" data-media-type="file" width="236" height="412" alt="Screenshot 2025-11-17 at 17.19.43.png" /></span></td>
</tr>
<tr data-local-id="7767618a-b49c-43e1-87c9-f202b4b245da">
<td class="confluenceTd" data-local-id="a5f48c1f-ba15-4039-a08e-3ae27c46ea37"><p>Pool List</p></td>
<td class="confluenceTd" data-local-id="e2c5598b-c14d-4b17-8e24-1e70838fcbc5"><ul>
<li><p>Title：HzLP</p></li>
<li><p>Subtitle：Provide market-specific liquidity with isolated risk management.</p></li>
<li><p><strong>通用规则：</strong></p>
<ul>
<li><p><strong>filter，sort，search可叠加，取子集。</strong></p></li>
<li><p><strong>链式流程：</strong>过滤 → 搜索 (address或symbol)→ 排序 → 分页</p></li>
<li><p><strong>不记filter/sort/搜索词，页面刷新回到默认状态。</strong></p></li>
<li><p><strong>条目数 &lt;= 10</strong> 时不展示分页组件。</p></li>
</ul></li>
<li><p><strong>filter1：分类筛选</strong></p>
<ul>
<li><p>选项：All（默认） / Forex / Equities / Indices / Crypto / Commodities / Meme</p></li>
<li><p>不记状态，刷新后回到 All</p></li>
<li><p>Filter 切换时：</p>
<ul>
<li><p>重置分页至第 1 页</p></li>
<li><p>保留当前搜索词</p></li>
<li><p>保留当前排序状态</p></li>
</ul></li>
</ul></li>
<li><p><strong>filter2: In Wallet 筛选</strong></p>
<ul>
<li><p>开关选项：<strong>默认关闭 展示所有。</strong>点击开关switch on，若已连接钱包，则仅展示用户钱包中所拥有LP的池子。若未连接钱包，则池子列表缺省态，提示词<code>Please connect your wallet to continue.</code></p></li>
<li><p>切换 In Wallet 状态时:</p>
<ul>
<li><p>重置分页至第 1 页</p></li>
<li><p>不记状态（刷新后关闭）</p></li>
</ul></li>
</ul></li>
<li><p><strong>Search：</strong></p>
<ul>
<li><p><strong>默认字段：</strong>Search Pools</p></li>
<li><p><strong>模糊搜索：</strong>模糊搜索<strong>仅作用在 symbol字段,</strong>hzlp为固定字段，不参与匹配。支持symbol的大小写不敏感子串匹配；输入任意字符即可实时过滤列表。优先级为：<strong>精确匹配 &gt; 前缀匹配 &gt; 子串匹配。</strong><br />
<em>&lt;e.g.&gt; hzlp为固定字段，输入l不应出现所有池子，只出现LINK/USD此类symbol中包含L的池子</em></p></li>
<li><p><strong>归一化排序：</strong>排序前移除 <code>/ - _</code> 等符号，只基于字母数字排序。</p></li>
<li><p><strong>输入限制：</strong>字母/数字 最大长度42字符</p></li>
<li><p><strong>地址搜索：</strong>若输入符合 EVM address 格式，则执行地址精确匹配；不支持部分地址匹配。</p></li>
<li><p><strong>UX相关：</strong></p>
<ul>
<li><p>搜索词改变 → 重置分页至第 1 页</p></li>
<li><p>搜索结果为空 → 缺省态（已有no matching result那个）</p></li>
<li><p>输入时以 <strong>200ms debounce</strong> 实时更新结果。</p></li>
</ul></li>
</ul></li>
<li><p><strong>Sort：</strong><code>TVL</code>（<strong>默认desc</strong>）；<code>APY </code></p>
<ul>
<li><p>每次仅允许一个排序字段生效</p></li>
<li><p>三段式点击：未排序 → desc → asc → 未排序。若被中断则变回默认。<br />
<em>&lt;e.g.&gt;点击APY后 desc，此时点击TVL，APY回到初始未排序状态</em></p></li>
<li><p>不记状态（刷新重置）</p></li>
<li><p>UX注意：整个表默认按TVL desc排序，在此之上第一次点击TVL还是desc排序不变（<a href="https://app.gmx.io/#/pools" class="external-link" rel="nofollow">参考GMX pools交互</a>）</p></li>
</ul></li>
<li><p><strong>Pagination：前端分页</strong></p>
<ul>
<li><p>每页10条，页码从 1 开始</p></li>
<li><p><strong>分页行为：</strong>搜索词或排序或过滤方式变化时（包括清除搜索框）<strong>重置到第1页</strong></p></li>
<li><p><strong>越界处理：</strong>当数据减少导致当前页不存在 → 自动跳回最后一页</p></li>
<li><p><strong>新增数据：</strong>插入底部，用户视图不会变化</p></li>
<li><p><strong>滚动行为：</strong>切换分页时<strong>滚动到列表顶部（H5尤其注意）</strong></p></li>
</ul></li>
<li><p><strong>表格：</strong></p>
<ul>
<li><p>Pool: 名称，后端维护配置表/从链同步</p></li>
<li><p>TVL/Supply：池aum以及LP token供应量</p></li>
<li><p>Fee APY: 年化手续费收益 不算pnl</p>
<ul>
<li><p>hover显示tooltip：</p>
<p><code>Annualized projection of fee income from trading activities only (open/close/borrow/liquidations), excluding price impact, PnL, and funding.</code></p></li>
</ul></li>
<li><p>Snapshot：30d APR曲线</p></li>
<li><p>Action: 点击<code>Details</code>或整行 进入二级页面</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="61b27543-925f-4f9c-b56f-360af84db360"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f60a74a00f1eac3de76c4c55fffcf65ada68e8435c067970a4ac017b960fc110" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2017.39.37.png?version=1&amp;modificationDate=1763372410561&amp;cacheVersion=1&amp;api=v2" data-height="817" data-width="1089" data-unresolved-comment-count="0" data-linked-resource-id="38961172" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 17.39.37.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="80e02c50-54e1-4959-9c31-30c8d6deb660" data-media-type="file" width="236" height="177" alt="Screenshot 2025-11-17 at 17.39.37.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a19501a38ea0ad08d9998b6ab277c52893556ccfd443ca7a15d550f987fb39ef" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2011.24.13.png?version=1&amp;modificationDate=1763436458267&amp;cacheVersion=1&amp;api=v2" data-height="292" data-width="862" data-unresolved-comment-count="0" data-linked-resource-id="39780371" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 11.24.13.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="7df670dd-3306-4bb0-9e7c-f039014f99de" data-media-type="file" width="349" height="118" alt="Screenshot 2025-11-18 at 11.24.13.png" /></span></td>
</tr>
</tbody>
</table>

</div>

### 二级详情页

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="288325a8-2f09-48d4-b741-dbf2f04c60ac">
<tbody>
<tr data-local-id="f4cd3540-0df0-4a31-8ef3-833540fb5c05">
<th class="confluenceTh" data-local-id="479475a8-1947-42c2-b981-176bd861b852"><p><strong>模块</strong></p></th>
<th class="confluenceTh" data-local-id="6e7d5553-ab88-47df-a64a-62d142e2a711"><p><strong>需求</strong></p></th>
<th class="confluenceTh" data-local-id="7cd50102-72f7-44bc-9670-decdbcbfeac8"><p><strong>截图</strong></p></th>
</tr>
&#10;<tr data-local-id="cd7b9ebb-dc90-4f18-8ae0-325bd532fe64">
<td class="confluenceTd" data-local-id="9272de67-924a-4e65-8d03-8a8850ba7aff"><p>Pool Info</p>
<p>User Info</p></td>
<td class="confluenceTd" data-local-id="1135e3bc-739e-4491-b831-fef39c420525"><ul>
<li><p>Title：[market icon] + [Pool Name]</p></li>
<li><p>← 返回按钮: 点击当前页面返回一级标签页（不另起新页）</p></li>
<li><p>TVL：池aum的usd金额</p></li>
<li><p>Total Earned Fees：总手续费营收，不包括pnl price impact或funding 取后端</p></li>
</ul>
<h4 id="PoolsPage_PRD-RemainingDepositCap：" data-local-id="06803b73-daa1-453f-bb74-c3e9adb3f260"><strong>Remaining Deposit Cap：</strong></h4>
<p>用户最多可新增 LP 的额度，即剩余可质押usdc多+空上限之和。容量限制由当前池子余额、未平仓仓位占用金额、风险参数共同决定。该项数据需在前端实时展示，并在用户输入金额时即时校验。</p>
<ul>
<li><p>hover展示tooltip：<br />
<code>Max USDC liquidity that the market can currently accept, after accounting for funds reserved for all open positions.</code><br />
<code>Max USDC in: 281.44m USDC ($280.29m/$100m)</code></p>
<ul>
<li><p><strong>Max USDC in_USD</strong>：剩余可质押usdc的美元价值<br />
<strong>=</strong> <code>max_AUM</code> <strong>-</strong> <code>AUM</code></p></li>
<li><p><strong>Max USDC in_amount:</strong> 剩余可质押USDC 数量<br />
= <code>max USDC in_USD</code> / <code>USDC Price</code></p></li>
<li><p><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">其中</span><strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">Max AUM</span></strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">为合约配置的风控参数,代表该池子最大上限。</span><strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">AUM</span></strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">为当前tvl（$）</span></p></li>
</ul></li>
</ul>
<h4 id="PoolsPage_PRD-RemainingWithdrawalCap：" data-local-id="3d87c69d-af60-480a-bfec-5801d721cac8"><strong>Remaining Withdrawal Cap：</strong></h4>
<p>同上。当前最大可取出上限，用于withdraw操作的校验。</p>
<ul>
<li><p>hover展示tooltip：<code>Max USDC liquidity that can be redeemed instantly, after accounting for funds reserved for all open positions.</code><br />
<code>Max USDC out: 617.43m USDC ($619.71k/$100m)</code></p>
<ul>
<li><p><strong><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">Max USDC out_USD 剩余可移除usdc美元价值</span></strong><br />
= Min {<span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>AUM</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> - max{</span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>uPnL_Long</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>uPnL_Short</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, 0} / </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>Max PnL Factor For Withdraw</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>AUM</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> - max</span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>{ReservedUsd</code></span><code>_Long, ReserveduSD_Short</code>}<span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> / </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>ReserveFactor</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">}</span></p></li>
<li><p><strong>Max USDC out_amount 剩余可移除USDC数量</strong><br />
= <strong>Max USDC out_USD</strong> / <strong>USDC Price</strong></p></li>
<li><p>其中<strong>Max PnL Factor for Withdraw</strong>以及<strong>Reserve Factor</strong>为合约配置风控参数，ReserveUSD即为OI</p></li>
</ul></li>
<li><p>Your Holdings用户数据：</p>
<ul>
<li><p>Deposits：[USDC icon] + 用户所持有lp的<strong>usdc价值</strong></p>
<ul>
<li><p><strong>USDC amount</strong> = LP Amount * LP Token Price / USDC Price</p></li>
<li><p>缺省态（未连接钱包/无token）：0 USDC</p></li>
</ul></li>
<li><p>Your Earned Fees: 用户赚到的总手续费收入</p>
<ul>
<li><p><strong>Your Earned Fees</strong> = LP Amount / Pool LP Amount * Pool Earned Fees</p></li>
</ul></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="6be13f9a-028c-4a5c-a468-95361f2a0d8b"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="125557c9f0bd4e179f6f13a27af7b972ed00de5f7a6fa22c2e22fbab3d12b586" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2015.34.10.png?version=1&amp;modificationDate=1763451290794&amp;cacheVersion=1&amp;api=v2" data-height="167" data-width="1627" data-unresolved-comment-count="0" data-linked-resource-id="39780426" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 15.34.10.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="24fc12ab-e192-45b4-883b-42c6e43f4039" data-media-type="file" width="180" height="18" alt="Screenshot 2025-11-18 at 15.34.10.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="42e33d5a5d4e06888f1ccfdc4dc391be77542fa5331ebd7705e9ba0fabb0134e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2016.28.36.png?version=1&amp;modificationDate=1763454557475&amp;cacheVersion=1&amp;api=v2" data-height="599" data-width="973" data-unresolved-comment-count="0" data-linked-resource-id="39780445" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 16.28.36.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="ded86b72-6e03-4419-be38-69373a591394" data-media-type="file" width="405" height="249" alt="Screenshot 2025-11-18 at 16.28.36.png" /></span></td>
</tr>
<tr data-local-id="6a7ad08e-4a5d-42ef-a1d3-a5a01f6ad4c9">
<td class="confluenceTd" data-local-id="a6252e7c-8469-4643-a04d-3a21df157428"><p>Chart</p></td>
<td class="confluenceTd" data-local-id="00533980-ef0f-4131-99c8-96496b3bbbf6"><ul>
<li><p>更新频率：历史数据变；最新数据10s</p></li>
<li><p>图标粒度：1h</p></li>
<li><p>图表：TVL<strong>（默认）</strong>/Fee APR</p></li>
<li><p>维度：30d<strong>（默认）</strong>/90d/180d/All-time</p></li>
<li><p>注意Fee APR这里，图左上角数据总览展示的是计算后的APY，hover tooltip以及流线图画的都是APR。</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="99d678cb-4525-4b7a-90e6-7dfa3f8aa2ed"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4f5a63d7560a6c3fe139b307933f494182f0678f80fb6325a69bc72fbb18309d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2017.13.25.png?version=1&amp;modificationDate=1763457738885&amp;cacheVersion=1&amp;api=v2" data-height="530" data-width="1087" data-unresolved-comment-count="0" data-linked-resource-id="39780485" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 17.13.25.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="4836c4a6-733c-4f96-a5df-02b9b1fa7049" data-media-type="file" width="180" height="87" alt="Screenshot 2025-11-18 at 17.13.25.png" /></span></td>
</tr>
<tr data-local-id="0b53e45b-3314-483f-ac8a-4d37e31dc5ee">
<td class="confluenceTd" data-local-id="2d3a5ef6-3ca4-4191-909e-b56f6ff964f4"><p>Liquidity Panel</p></td>
<td class="confluenceTd" data-local-id="207f2db4-d04c-4041-a14b-763819a7c8df"><h4 id="PoolsPage_PRD-1.Deposit" data-local-id="d9894ab7-ee8f-4103-96ca-47132854f7ce"><strong>1. Deposit</strong></h4>
<h4 id="PoolsPage_PRD-1.1输入框" data-local-id="bdc3e9bb-347c-411a-a087-3eb920025661"><strong>1.1 输入框</strong></h4>
<ul>
<li><p>默认值：0.00</p></li>
<li><p>输入限制：</p>
<ul>
<li><p>最大字符长度：30</p></li>
<li><p>可输入字符：数字，小数点</p></li>
<li><p>小数位数限制：与usdc token精度同</p></li>
</ul></li>
<li><p>输入框自动更正：去除前导零、限制小数位、空输入回退为 <code>0.00</code>、超出钱包余额时更正为其钱包余额</p></li>
</ul>
<p><strong>1.2 按钮显示逻辑</strong></p>
<ul>
<li><p>未连接钱包：<code>Connect Wallet</code> 可点击，触发连接钱包</p></li>
<li><p>已连接钱包：根据输入实时切换</p>
<ul>
<li><p>Input ≤ 0：<code>Enter an Amount</code> Disabled</p></li>
<li><p>Input <strong>美元价值</strong> &gt; <strong>capacity_remaining</strong>：<code>Above Deposit Limit [Deposit Cap_USD]</code>Disabled</p></li>
<li><p>未Approve 或 Approved max spending cap不足：<code>Approve USDC Spending</code>Enabled</p></li>
<li><p>正在Approve：<code>Approving [Spinner图标]</code> Disabled</p></li>
<li><p>校验&amp;计算完成后可质押：<code>Deposit USDC</code> Enabled</p></li>
<li><p>重新计算中：<code>Finalizing Quote [spinner] </code>Disabled</p></li>
<li><p>正在deposit：<code>Depositing USDC [spinner]</code>Disabled</p></li>
</ul></li>
</ul>
<p><strong>1.3 校验链路按顺序执行：</strong></p>
<ol>
<li><p><strong>格式校验</strong>：合法数字 + 小数点位数合法</p></li>
<li><p><strong>余额校验</strong>：Input ≤ 用户钱包中 USDC 余额</p></li>
<li><p><strong>池子可用容量校验</strong>：Input_USD ≤ <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/36372492/Pools+Page_PRD#Remaining-Deposit-Cap%EF%BC%9A" rel="nofollow">Remaining Deposit Capacity</a></p></li>
<li><p><strong>是否需要批准：</strong>allowance &lt; input，则进入approve流程</p>
<ol>
<li><p>按钮<code>Approve USDC Spending</code></p></li>
<li><p>点击approve</p>
<p>→ 钱包弹窗</p>
<p>→ 按钮<code>Approving USDC Spending</code></p>
<p>→ Pending Toast：标题 <code>[approve icon]</code> + <code>Approval</code></p>
<p>；文案<code>Approving token spending</code>+ <code>[spinner图标]</code></p></li>
<li><p>→ <strong>成功:</strong> Toast 文案变为<code>Approval</code> + <code>Completed[tick]</code>；allowance 在 approve 成功后立即读取链上最新数值，直到大于 input 才进入 Deposit 状态；按钮变为：<code>Deposit</code>（可点击）<br />
→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p></li>
</ol></li>
<li><p><strong>风险/可交易状态校验：</strong>池 paused → 禁止操作</p></li>
<li><p><strong>计算 Output：</strong>LP_amount = input / LP_price；Quote 校验有效期 <strong>≤ 5s</strong>，超过后自动重新计算</p></li>
<li><p><strong>按钮状态刷新：</strong>全部通过 → 进入deposit提交流程：</p>
<ol>
<li><p><code>Deposit USDC</code>按钮可点击</p></li>
<li><p>用户点击 Deposit<br />
-&gt; 钱包弹窗</p>
<p>→ 按钮<code>[Depositng USDC] </code>；输入框 locked；面板不可交互</p>
<p>-&gt; <strong>Pending Toast</strong>：标题<code>[deposit icon] </code>+ <code>Deposit</code>;文案<code>Depositing liquidity</code>+ <code>[Spinner]</code></p></li>
<li><p>→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p>
<p>→ <strong>成功：Keeper推送成功事件，pending变为成功Toast：</strong>文案<code>Depositing liquidity</code>+ <code>[Spinner]</code>变为<code>Completed</code> + <code>[tick]</code>；同时换行新增文案<code>[input usdc amount] USDC → [output minted HzLP amount] HzLP: [Pool Symbol]</code>；<strong>同时触发数据刷新：</strong>user LP balance / pool parameters / liquidity history</p></li>
</ol></li>
<li><p><strong>LP价格展示/滑点/费率部分不变。price impact部分判断以及提示先隐藏。</strong></p></li>
</ol>
<h4 id="PoolsPage_PRD-2.Withdraw" data-local-id="15472fae-6649-43d4-ab63-8978afd0f707">2. <strong>Withdraw</strong></h4>
<blockquote>
<p>USDC相关验证改成HzLP: [Symbol] 其他同上。即，不同之处为：</p>
</blockquote>
<p><strong>2.1 输入框</strong></p>
<ul>
<li><p>小数位数限制：与HzLP token精度同</p></li>
<li><p>输入框自动更正：去除前导零、限制小数位、空输入回退为 <code>0.00</code>、超出钱包余额时更正为其钱包HzLP的余额</p></li>
</ul>
<p><strong>2.2 按钮显示逻辑</strong></p>
<ul>
<li><p>已连接钱包：根据输入实时切换</p>
<ul>
<li><p>Input <strong>美元价值</strong> &gt; <strong>capacity_remaining</strong>：<code>Above Withdraw Limit [Withdraw Cap_USD]</code>Disabled</p></li>
<li><p>未Approve 或 Approved max spending cap不足：<code>Approve HzLP:[Symbol] Spending</code>Enabled</p></li>
<li><p>校验&amp;计算完成后可移除：<code>Withdraw USDC</code> Enabled</p></li>
<li><p>正在移除：<code>Withdrawing USDC [spinner]</code>Disabled</p></li>
</ul></li>
</ul>
<p><strong>2.3 校验链路按顺序执行：</strong></p>
<ol>
<li><p><strong>余额校验</strong>：Input ≤ 用户钱包中该池中HzLP 余额</p></li>
<li><p><strong>池子可用容量校验</strong>：Input_HzLP_USD ≤ <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/36372492/Pools+Page_PRD#Remaining-Withdrawal-Cap%EF%BC%9A" rel="nofollow">Remaining Withdraw Capacity</a></p></li>
<li><p><strong>是否需要批准：</strong>allowance &lt; input，则进入approve流程</p>
<ol>
<li><p>按钮<code>Approve HzLP:[Symbol] Spending</code></p></li>
<li><p>点击approve</p>
<p>→ 钱包弹窗</p>
<p>→ 按钮<code>Approving HzLP:[Symbol] Spending</code></p></li>
<li><p>→ <strong>成功:</strong> Toast 文案变为<code>Token spending approved</code> + <code>[tick]</code>；allowance 在 approve 成功后立即读取链上最新数值，直到大于 input 才进入 Withdraw状态；按钮变为：<code>Withdraw</code>（可点击）</p></li>
</ol></li>
<li><p><strong>计算 Output：</strong>USDC_amount = input * LP_price / USDC_Price；Quote 校验有效期 <strong>≤ 5s</strong>，超过后自动重新计算</p></li>
<li><p><strong>按钮状态刷新：</strong>全部通过 → 进入withdraw提交流程：</p>
<ol>
<li><p><code>Withdraw USDC</code>按钮可点击</p></li>
<li><p>用户点击 Withdraw<br />
-&gt; 钱包弹窗</p>
<p>→ 按钮<code>[Withdrawing USDC] </code>；输入框 locked；面板不可交互</p>
<p>-&gt; <strong>Pending Toast</strong>：标题<code>[withdraw icon] </code>+ <code>Withdraw</code>;文案<code>Withdrawing liquidity</code>+ <code>[Spinner]</code></p></li>
<li><p>→ <strong>成功：Keeper推送成功事件，pending变为成功Toast：</strong>文案<code>Withdrawing liquidity</code>+ <code>[Spinner]</code>变为<code>Completed</code> + <code>[tick]</code>；同时换行新增文案</p>
<p><code>[input HzLP amount] HzLP: [Pool Symbol] → </code></p>
<p><code>[output usdc amount] USDC </code>；<strong>同时触发数据刷新：</strong>user LP balance / pool parameters / liquidity history</p></li>
</ol></li>
</ol>
<h4 id="PoolsPage_PRD-3.RemainingDeposit/WithdrawCapacity计算逻辑：" data-local-id="5258393b-aca3-4728-a749-ceff15ef20ae"><strong>3. <span class="inline-comment-marker" data-ref="f3b681c5-9d8c-4a58-940e-fe1e998814ad">Remaining Deposit/Withdraw Capacity计算逻辑：</span></strong></h4>
<blockquote>
<p><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">就是pool info那里对应的质押的Max USDC in ，移除的Max USDC out</span></p>
</blockquote>
<ul>
<li><p><strong><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">Max USDC in_USD：</span></strong><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">剩余可质押usdc的美元价值</span><strong><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f"> = max_AUM - AUM </span></strong></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">其中Max AUM为合约配置的风控参数,代表该池子最大上限。AUM为当前tvl（$）</span></span></p></li>
</ul></li>
<li><p><strong><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">Max USDC out_USD </span></span></strong><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">剩余可移除usdc美元价值</span></span><strong><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f"> </span></span><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">= Min {</span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">AUM - max{uPnL_Long, uPnL_Short, 0} / Max PnL Factor For Withdraw, AUM - </span></span>max{<span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">ReservedUsdLong,ReservedUSDShort} / ReserveFactor} </span></span></strong></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="cd42758a-918e-4c39-a9e9-8837a1967f0f">其中Max PnL Factor for Withdraw以及Reserve Factor为合约配置风控参数，ReserveUSD就是所谓的OI</span></p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="d86fd238-f2db-43a9-84f3-558a026c1062"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="60ed9459cdda94f5d9aa88210a4b4395be6daceebf8c7de6acc664f57df18b9f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/image-20251119-075157.png?version=1&amp;modificationDate=1763538722399&amp;cacheVersion=1&amp;api=v2" data-height="2496" data-width="1421" data-unresolved-comment-count="0" data-linked-resource-id="40697858" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251119-075157.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="2af7e39c-db17-4989-ad8a-ee3d3976b82a" data-media-type="file" width="180" height="316" alt="image-20251119-075157.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="818fed65313dbcf1ff1b80d2040ff0315243d0baab8b7009f96967073fe0d79d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-20%20at%2012.06.07.png?version=1&amp;modificationDate=1763611580105&amp;cacheVersion=1&amp;api=v2" data-height="394" data-width="574" data-unresolved-comment-count="0" data-linked-resource-id="40992806" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-20 at 12.06.07.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="25c6cf3f-9e6a-4d46-a2f6-093b4341ad01" data-media-type="file" width="405" height="278" alt="Screenshot 2025-11-20 at 12.06.07.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f58d448ff1c9705faabf0665b19fcb1dd3e1c2ef3e3141fc86ea9eae6d1fde41" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-20%20at%2012.07.46.png?version=1&amp;modificationDate=1763611690271&amp;cacheVersion=1&amp;api=v2" data-height="456" data-width="722" data-unresolved-comment-count="0" data-linked-resource-id="40960037" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-20 at 12.07.46.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="97f54785-7a32-4803-b6d3-772bdbbc75bc" data-media-type="file" width="180" height="113" alt="Screenshot 2025-11-20 at 12.07.46.png" /></span></td>
</tr>
<tr data-local-id="6a92546a-a975-45e3-93b3-e53f7c8bafcd">
<td class="confluenceTd" data-local-id="e1f2b6fe-263f-4e0e-9541-bf56e5310829"><p>Liquidity History</p></td>
<td class="confluenceTd" data-local-id="1abc310d-a236-4cd7-8534-dd2eb213b18f"><ul>
<li><p>更新频率：同history 10s</p></li>
<li><p>分页：My Activity（默认）/Pool Activity</p></li>
<li><p>刷新按钮：点击刷新</p></li>
<li><p>字段：<strong>时间降序排，新到旧</strong></p>
<ul>
<li><p>Action：Deposit/Withdraw</p></li>
<li><p>Shares：HzLP添加或移除的数量</p></li>
<li><p>Vaule：[Deposit_USD] + [Fees Earned]</p>
<ul>
<li><p><strong>Deposit_USD</strong> = HzLP * Price</p></li>
<li><p><strong>Fees Earned</strong> = Withdraw_USD - Initial Deposit_USD</p></li>
</ul></li>
<li><p>Time/Hash：前端转到用户机器时间，hover变为可点击态，点击跳转至explorer对应哈希</p></li>
<li><p>缺省态：</p>
<ul>
<li><p>已连接钱包：<code>No Liquidity acticity found.</code></p></li>
<li><p>未连接钱包：</p>
<p><code>Please connect your wallet to continue.</code></p>
<p>+ <code>Connect Wallet</code> 按钮（同图2交易历史记录）</p></li>
</ul></li>
</ul></li>
<li><p>UX：默认每页展示6行，后端cursor分页，同图三中的history拉到下面，点击Click to load more内部滚动即可。</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="48f4e3aa-8813-4be5-a0a4-f5a6e523c482"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="995558084abdf05e8c5297b0f700355f5782491b1c46fe8d27e0555d556a81da" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2018.33.21.png?version=1&amp;modificationDate=1763462054858&amp;cacheVersion=1&amp;api=v2" data-height="260" data-width="1048" data-unresolved-comment-count="0" data-linked-resource-id="39845994" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 18.33.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="dd357c53-7e4a-4140-bc59-616b6895d3d1" data-media-type="file" width="181" height="44" alt="Screenshot 2025-11-18 at 18.33.21.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="291bc36622dc8aa72a17bb89b6f488e9b583ee60912718c295676e02ba422e1d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2018.12.17.png?version=1&amp;modificationDate=1763460762575&amp;cacheVersion=1&amp;api=v2" data-height="230" data-width="1252" data-unresolved-comment-count="0" data-linked-resource-id="39747704" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 18.12.17.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="000f08aa-4da8-4c54-96f6-f88841cba965" data-media-type="file" width="468" height="85" alt="Screenshot 2025-11-18 at 18.12.17.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9352ec3df26dc281d8c3b96dcc111453676516e5b7fcc631704f321e3004b9cf" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-18%20at%2018.16.15.png?version=1&amp;modificationDate=1763461010928&amp;cacheVersion=1&amp;api=v2" data-height="318" data-width="1255" data-unresolved-comment-count="0" data-linked-resource-id="39878793" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-18 at 18.16.15.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="8da788c8-a03a-4f22-90ec-bc63eef42290" data-media-type="file" width="429" height="108" alt="Screenshot 2025-11-18 at 18.16.15.png" /></span></td>
</tr>
</tbody>
</table>

</div>

## 四、数据依赖与接口需求

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="81e48fab-84ef-47d5-a83e-14d60c19ca9e">
<tbody>
<tr data-local-id="29724c52-f00f-4fc7-94e5-741090094217">
<th class="confluenceTh" data-local-id="8ca4632a-c374-46a2-b7ae-c09443f12869"><p><strong>页面</strong></p></th>
<th class="confluenceTh" data-local-id="f9bf3789-000a-4242-9d91-ed993dd72b9c"><p><strong>模块</strong></p></th>
</tr>
&#10;<tr data-local-id="10ef4d0d-f677-48b8-a790-ac573c7f4ae4">
<td class="confluenceTd" data-local-id="1d4eed9f-cefd-44fc-8cd2-695573c6a20f"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#%E4%B8%80%E7%BA%A7%E5%88%97%E8%A1%A8%E9%A1%B5" rel="nofollow"><strong>一级池列表页</strong></a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="cb9c090f5096bec50c1d5b65247693d12b6d88a00d8ad8e89c0ca4be59fca653" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2010.58.08.png?version=1&amp;modificationDate=1763348399823&amp;cacheVersion=1&amp;api=v2" data-height="864" data-width="1359" data-unresolved-comment-count="0" data-linked-resource-id="38010904" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 10.58.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="8e4b2557-d916-4005-bcc1-c19f03381e5a" data-media-type="file" width="468" height="297" alt="Screenshot 2025-11-17 at 10.58.08.png" /></span></td>
<td class="confluenceTd" data-local-id="fc4daaa7-6e20-43f2-a0ef-9abf39d808bb"><ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.1-Pool-Overview" rel="nofollow">Overview</a></p>
<ol>
<li><p>接口：<code>/pools/overview</code></p></li>
<li><p>描述：顶部聚合数据</p></li>
</ol></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.2-Pool-List" rel="nofollow">Pool List</a></p>
<ol>
<li><p>接口：<code>/pools/list</code></p></li>
<li><p>描述：列表 + 筛选/排序/分页</p></li>
</ol></li>
</ol></td>
</tr>
<tr data-local-id="74d91be1-ad4c-4a49-ba22-e32575dbf0eb">
<td class="confluenceTd" data-local-id="ea6556da-a30b-4833-8f09-b031f98a5c3e"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#%E4%BA%8C%E7%BA%A7%E8%AF%A6%E6%83%85%E9%A1%B5" rel="nofollow">二级池详情页</a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ca556fb178cb0fdd6835a4904f10617fb3cf2761a2656a83cfdfe52a4662dc16" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-17%20at%2011.42.46.png?version=1&amp;modificationDate=1763351148409&amp;cacheVersion=1&amp;api=v2" data-height="715" data-width="1147" data-unresolved-comment-count="0" data-linked-resource-id="38076446" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-17 at 11.42.46.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="ee35b5c4-fa21-45c4-8d66-1f0859baee65" data-media-type="file" width="468" height="291" alt="Screenshot 2025-11-17 at 11.42.46.png" /></span></td>
<td class="confluenceTd" data-local-id="2acf3b23-8899-4a5f-b291-b82847f5fcab"><ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.3-Pool-Info" rel="nofollow">Pool Info (Pool&amp; User取后端)</a></p>
<ol>
<li><p>接口：<code>/pools/{id}/info</code>；<code>/user/{id}/info</code></p></li>
<li><p>描述：池子基本信息；用户流动性信息</p></li>
</ol></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.5-Chart-%E5%9B%BE%E8%A1%A8%E6%95%B0%E6%8D%AE" rel="nofollow">Charts</a></p>
<ol>
<li><p>接口：<code>/pools/{id}/chart</code></p></li>
<li><p>描述：TVL, APR时间序列（30d 90d 180d all）</p></li>
<li><p>注意：APR这里总数据显示<strong>计算得出的APY</strong>，tooltip及图表给的是<strong>APR</strong></p></li>
</ol></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.6-Liquidity-Panel" rel="nofollow"><del>Liquidity Panel</del></a></p>
<ol>
<li><p><del>接口：POST</del> <strong><del></del></strong><code>/quote</code></p></li>
<li><p><del>描述：根据用户表单返回</del> <strong><del>5s有效</del></strong> <del>的quote preview</del></p></li>
</ol></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/36372492#4.7-Liquidity-History" rel="nofollow">Liquidity History</a></p>
<ol>
<li><p>接口：<code>/pools/{id}/history</code>；</p>
<p><code>/user/{id}/liquidity-history</code></p></li>
<li><p>描述：全池历史；用户历史；需要后端cursor分页</p></li>
<li><p>注意：这里涉及Initial Deposit，代表用户初始质押的USDC美元价值，区分与Deposit，代表持有LP的总值，Deposit = LP amount* LP Price</p></li>
</ol></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

### **4.1 Pool Overview**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="e3474e7a-f211-4cb3-a298-616a0f2c9e72">
<tbody>
<tr data-local-id="6a9dc709-9d2d-44f4-9531-fb91efd2c2c2">
<th class="confluenceTh" data-local-id="0d29e71d-5091-4fe0-9315-df89f9e4ca45"><p>模块</p></th>
<th class="confluenceTh" data-local-id="42307c51-e873-45a3-a23e-21b573174be2"><p>字段</p></th>
<th class="confluenceTh" data-local-id="8b145cba-9050-4554-a3ee-8147e43cebaa"><p>说明</p></th>
<th class="confluenceTh" data-local-id="78e86cac-bd25-4bc2-99a1-60e449a7681a"><p>更新频率 / 缓存</p></th>
</tr>
&#10;<tr data-local-id="e8b1b718-21c6-46ad-9c89-dc7061a4fea3">
<td class="confluenceTd" data-local-id="24195d73-793f-4d76-ae21-323770398197"><p>Pool Overview</p></td>
<td class="confluenceTd" data-local-id="1e039de6-c983-4176-9f10-c0f19b277e71"><p><code>tvl_usd_total</code></p></td>
<td class="confluenceTd" data-local-id="3b7060cc-a9b1-48b1-a66b-91fef85851f3"><p>所有隔离池 TVL_USD 加总</p></td>
<td class="confluenceTd" data-local-id="92aa9320-b7ce-4e0f-84ec-67f8d3cb68ec"><p>10s（与history一致），缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="10060462-b68e-4915-b6ce-1dac886b7dac">
<td class="confluenceTd" data-local-id="bb389055-6d87-4ba8-9b50-66de90595d53"><p>Pool Overview</p></td>
<td class="confluenceTd" data-local-id="32281fc9-19b2-4da2-8426-94b9d257fcf6"><p><code>total_earned_fees_usd</code></p></td>
<td class="confluenceTd" data-local-id="b8f06f94-d1d0-40b4-871a-7ab5b3b3fa8f"><p>所有隔离池手续费收入加和（不含PnL）</p></td>
<td class="confluenceTd" data-local-id="5801f4a4-4a9e-49bc-85ea-d9cf13b30993"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="3961bff5-6360-43c1-881f-47853cf95c92">
<td class="confluenceTd" data-local-id="5c8e3f12-dc94-4ddd-a502-0aec7e96eceb"><p>User Holdings</p></td>
<td class="confluenceTd" data-local-id="af6379ec-685a-4dfd-964e-c2cad501d228"><p><code>user_total_deposits_usd</code></p></td>
<td class="confluenceTd" data-local-id="f8d6d1a6-6f51-4c4a-a4f7-d739a1075578"><p>Σ 用户所持 LP 数量 × LP 价格</p></td>
<td class="confluenceTd" data-local-id="4c25a306-1638-4943-af8b-316af8e8c1c5"><p>钱包连接时 10s 轮询，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="bccf2641-f07e-4187-98f7-b2337ec20d4f">
<td class="confluenceTd" data-local-id="72ac482f-7368-4e9f-b329-2f5c50ab4e00"><p>User Holdings</p></td>
<td class="confluenceTd" data-local-id="b23d60d3-fd9a-48bf-98eb-33e3dcaf2cad"><p><code>user_total_earned_fees_usd</code></p></td>
<td class="confluenceTd" data-local-id="6dd61f22-a778-4ebf-8417-d8451e5d7e76"><p>Σ 用户手续费收入, <strong>不含PnL部分</strong></p>
<p>= Σ(User LP Amount / Pool LP Amount * Pool Earned Fees)</p></td>
<td class="confluenceTd" data-local-id="bfe20867-bd73-46a3-b965-0c0fc4e0a027"><p>钱包连接时 10s 轮询，缓存 ≤ 5s</p></td>
</tr>
</tbody>
</table>

</div>

### **4.2 Pool List**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="4282d294-fe89-4904-9448-0bdb192fd5df">
<tbody>
<tr data-local-id="9ba0715a-8d54-41cb-80da-40bb14014884">
<th class="confluenceTh" data-local-id="bf608d85-383e-4118-a5b1-79ea52302e24"><p>字段</p></th>
<th class="confluenceTh" data-local-id="b67e1369-ce2f-4481-a52c-0f51c528d024"><p>说明</p></th>
<th class="confluenceTh" data-local-id="daaa7b08-ec74-4967-8c1e-892d15191ec2"><p>更新频率 / 缓存</p></th>
</tr>
&#10;<tr data-local-id="c351bc76-3eca-4170-be33-50611ff9a49f">
<td class="confluenceTd" data-local-id="f926aa61-e78b-4ca6-b93e-c9aae5181017"><p><code>pool_name</code></p></td>
<td class="confluenceTd" data-local-id="4c46390f-7a26-421e-965b-2733f7b58673"><p>pool唯一ID；HzLP：[Market Symbol]</p>
<p>其中[Market Symbol]用于搜索字段</p></td>
<td class="confluenceTd" data-local-id="6fa6294d-add0-46b6-a598-6cbc68840cd9"><p>launch成功后刷新一次</p></td>
</tr>
<tr data-local-id="80b30335-6474-4d60-a911-18a37785080c">
<td class="confluenceTd" data-local-id="04eaf334-fd1a-49f3-aa9a-318d46792235"><p><code>category</code></p></td>
<td class="confluenceTd" data-local-id="d9fdb640-d23f-4b1b-b861-63fa9997348d"><p><strong>filter1：</strong>All（默认） / Forex / Equities / Indices / Crypto / Commodities / Meme</p></td>
<td class="confluenceTd" data-local-id="1c7cbc7c-ec88-4d97-a14e-efbbf08ed31e"></td>
</tr>
<tr data-local-id="20af84c6-8d8c-4b34-8c51-150d93a7a5fc">
<td class="confluenceTd" data-local-id="8bbf1a7b-49e8-4105-8e49-11f5130008d7"><p><code>tvl_usd</code></p></td>
<td class="confluenceTd" data-local-id="01a837c7-f88e-4886-b268-d6cbcd32d161"><p><strong>sort1：</strong>当前池 TVL；排序字段</p></td>
<td class="confluenceTd" data-local-id="cbb8d858-2d00-49c5-aa57-56441ba4d8ff"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="35c46980-6943-4a52-b9fd-2e13c1ff3740">
<td class="confluenceTd" data-local-id="2cf3f690-30e3-4674-b19e-86b31f79c665"><p><code>lp_supply</code></p></td>
<td class="confluenceTd" data-local-id="29d8b723-1e8d-4381-b4a7-d944363b93a5"><p>LP Token 总供应量</p></td>
<td class="confluenceTd" data-local-id="5708dce2-06eb-488f-bf44-f271767f766a"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="c425d1ce-110e-4671-b862-9e67d0a8c236">
<td class="confluenceTd" data-local-id="db77cd4d-d21b-4e54-ae4f-35d5fada1351"><p><code>fee_apy</code></p></td>
<td class="confluenceTd" data-local-id="6a5af5a8-1519-40fe-869d-ef96ff25a386"><p><strong>sort2：</strong>年化手续费收益；排序字段</p></td>
<td class="confluenceTd" data-local-id="8805e25c-106a-4cdc-8c0b-63153671d9fe"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="33cb74b1-5ba5-4206-bfbd-a4ccca45d69a">
<td class="confluenceTd" data-local-id="d487661c-b5bb-42a4-ba77-90492f3929a9"><p><code>fee_apr_30d_snapshot[]</code></p></td>
<td class="confluenceTd" data-local-id="4da27348-78cc-4c7d-8fb8-eada42a9305f"><p>30d <strong>APR</strong> 点位（用于小图）；可压缩数据</p></td>
<td class="confluenceTd" data-local-id="a34b0c6d-406e-4ddb-9ddf-e9c5ce1b8e65"><p>1h</p></td>
</tr>
<tr data-local-id="d31206ca-bcd8-462f-9793-1f823c80ef4b">
<td class="confluenceTd" data-local-id="e4100d01-4a80-4e98-9d47-8392543ce6a6"><p><code>userHasBalance: true/false</code></p></td>
<td class="confluenceTd" data-local-id="4f224d48-7238-435a-8995-4ac417e84349"><p><strong>filter2:</strong> 用户在当前池中是否持有该池LP；In-Wallet 过滤字段</p></td>
<td class="confluenceTd" data-local-id="70f4a0a6-8991-49c9-a79d-10ed0ce4686f"><p>钱包连接后 10s；缓存 ≤ 3s</p></td>
</tr>
</tbody>
</table>

</div>

### **4.3 Pool Info**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="6ba80819-6844-45aa-b346-5ff2671e9535">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="baf988bb-00ce-4007-b0d2-e217cfcb8df0">
<th class="confluenceTh" data-local-id="7518e86f-0256-4bb8-a41e-28e8a730a2b6"><p>字段</p></th>
<th class="confluenceTh" data-local-id="87cfa551-7876-4b1f-a03c-338b57cd03b5"><p>说明</p></th>
<th class="confluenceTh" data-local-id="0413312d-8bf8-405a-9ea2-4a94a8e81cbb"><p>更新频率 / 缓存</p></th>
</tr>
&#10;<tr data-local-id="6c1c5c5a-b14c-4a3d-bd57-77f77c978542">
<td class="confluenceTd" data-local-id="eacc4c6e-32a0-4de7-98f9-fe3b71748f82"><p><code>pool_name</code></p></td>
<td class="confluenceTd" data-local-id="60e1e7a1-53fb-4c68-89a7-024a72bd1150"><p>Pool唯一ID；HzLP：[Market Symbol]</p></td>
<td class="confluenceTd" data-local-id="8c00a5d5-ca4b-477e-8633-39bf125ad990"><p>-</p></td>
</tr>
<tr data-local-id="e7f09aa3-9c05-4a0a-bf20-384938936079">
<td class="confluenceTd" data-local-id="b42c00cf-d7ce-4e28-a31a-f47f2c1b2fab"><p><code>tvl_usd</code></p></td>
<td class="confluenceTd" data-local-id="d6a15cec-c39c-4c0e-83c1-dd52cea8690f"><p>池 TVL</p></td>
<td class="confluenceTd" data-local-id="d6ff9726-0add-4a70-8801-0367c7c4b892"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="d7bfb8ce-60fa-46fc-b9dd-91d594d9678e">
<td class="confluenceTd" data-local-id="61852cc3-f751-4404-bcea-2c11a67cd027"><p><code>lp_supply</code></p></td>
<td class="confluenceTd" data-local-id="5dd7b4b0-c97b-4bba-abaf-cf765482ae11"><p>LP Token 总供应量</p></td>
<td class="confluenceTd" data-local-id="c4ef2e09-4561-4349-a815-edd97d614744"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="1bc4b7a6-99d7-4581-88c5-d6354ec13251">
<td class="confluenceTd" data-local-id="8c6b66e3-5899-4c72-94ad-50ea1d259b34"><p><code>total_earned_fees_usd</code></p></td>
<td class="confluenceTd" data-local-id="8e82eaf8-e858-4163-a55d-b4575fecb7e3"><p>手续费累计（排除PnL）</p></td>
<td class="confluenceTd" data-local-id="1c08fcc9-9608-41e5-82e4-5bec7a712f93"><p>10s，缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="e9e7469d-8f9f-406b-a661-4ad25b2b9196">
<td class="confluenceTd" data-local-id="a73246ca-bfa0-4158-9903-10f6edd25adc"><p><code>tvl_cap_usd</code></p></td>
<td class="confluenceTd" data-local-id="2d017572-36b4-41c3-9e56-bda2c4776f23"><p>TVL 最大上限（含buffer）</p>
<ul>
<li><p><strong>TVL Cap：</strong>合约配置的风控参数, 已留buffer（$）</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="76505ddc-25cf-4191-baeb-de920ed6e021"><p>10s</p></td>
</tr>
<tr data-local-id="aab636dc-1676-4538-a613-13cb39e03982">
<td class="confluenceTd" data-local-id="09d65a18-5150-4252-b457-a29758fb5731"><p><code>remaining_deposit_cap_usd</code></p></td>
<td class="confluenceTd" data-local-id="357c7ff5-3ba5-4246-a221-5bbb1841e590"><p>剩余可质押USDC的美元价值</p>
<ul>
<li><p><strong>Max USDC in_USD</strong>：剩余可质押usdc的美元价值 <strong>=</strong> <code>max_AUM</code> <strong>-</strong> <code>AUM</code></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">其中</span><strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">Max AUM</span></strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">为合约配置的风控参数,代表该池子最大上限。</span><strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">AUM</span></strong><span class="inline-comment-marker" data-ref="ea9d0c43-dc41-47d4-a76d-f99b647545c0">为当前tvl（$）</span></p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="3febce3d-1a18-4c76-8483-6fe9dcf3fc57"><p>5s，缓存 ≤ 2s</p></td>
</tr>
<tr data-local-id="1d488771-a776-409c-a439-cf26469747a1">
<td class="confluenceTd" data-local-id="ce367dae-f0bf-459a-ab48-4efc0781573a"><p><code>remaining_deposit_cap_usdc</code></p></td>
<td class="confluenceTd" data-local-id="02fcab47-411b-4463-b5a1-17ccc01191d8"><p>剩余可质押USDC数量</p>
<ul>
<li><p><strong>剩余可质押USDC数量</strong> = (TVL Cap - TVL) / USDC Price</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="c0a826b1-ccbe-479c-97cb-850ea328c472"><p>5s，缓存 ≤ 2s</p></td>
</tr>
<tr data-local-id="91cd3df3-120d-472a-9a8b-d9b474b2f9a2">
<td class="confluenceTd" data-local-id="4b1c54d6-7ede-4673-a1b6-8e1fc4e2faaa"><p><code>remaining_withdraw_cap_usd</code></p></td>
<td class="confluenceTd" data-local-id="2e6dbde4-7eb4-41f3-8405-88979e70cab0"><p>剩余可取USDC价值</p>
<ul>
<li><p><strong><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">Max USDC out_USD 剩余可移除usdc美元价值 </span>=</strong> Min {<span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>AUM</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> - max{</span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>uPnL_Long</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>uPnL_Short</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, 0} / </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>Max PnL Factor For Withdraw</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">, </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>AUM</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> - </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>ReservedUsd</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"> / </span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67"><code>ReserveFactor</code></span><span class="inline-comment-marker" data-ref="984321ad-3661-43b1-a117-bae61f0dba67">}</span></p>
<ul>
<li><p>其中<strong>Max PnL Factor for Withdraw</strong>以及<strong>Reserve Factor</strong>为合约配置风控参数，ReserveUSD就是所谓的OI</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="4d7a737b-3860-4001-b326-3b139c552d3d"><p>5s，缓存 ≤ 2s</p></td>
</tr>
<tr data-local-id="21fd771e-e4e4-4e22-bcff-a27e5893ab57">
<td class="confluenceTd" data-local-id="99282071-01d7-4d0a-b380-835a28351da2"><p><code>remaining_withdraw_cap_usdc</code></p></td>
<td class="confluenceTd" data-local-id="38e0fbe1-10b5-4d9a-8619-e96f9967da50"><p>同上数量</p>
<ul>
<li><p><strong>剩余可质押USDC数量 =</strong> (TVL - OI或uPnL的某个倍数)/ USDC Price</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="b5fe0ad8-5d55-4baa-9f24-bb3ad3890f89"><p>5s，缓存 ≤ 2s</p></td>
</tr>
<tr data-local-id="77ac0696-2882-44c9-a7c7-0e0b0c02dd54">
<td class="confluenceTd" data-local-id="0436bb07-79d9-4232-897a-320a6bb93ddc"><p><code>lp_price_usd</code></p></td>
<td class="confluenceTd" data-local-id="b492592e-30bd-42d5-acc5-ad0cfb1b6a93"><p>LP Token 单价</p></td>
<td class="confluenceTd" data-local-id="435ac1f0-90c6-4d56-bd58-9d483e7563b7"><p>5s，缓存 ≤ 2s</p>
<p>支持实时手动刷新/用户交易完后实时刷新一次</p></td>
</tr>
</tbody>
</table>

</div>

### **4.4 User Info**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="94f54b0f-27c3-43cf-9b69-fc351c7752cb">
<tbody>
<tr data-local-id="e90c912b-0974-4d6c-b662-ef6e4d1e71d6">
<th class="confluenceTh" data-local-id="f1df8a6b-0cfa-40d7-abd5-0d4329ad135e"><p>字段</p></th>
<th class="confluenceTh" data-local-id="22920ee5-8922-486f-8a18-57df490de029"><p>说明</p></th>
<th class="confluenceTh" data-local-id="40a378e3-2f0c-4f52-a836-aa0ff37291dd"><p>更新频率 / 缓存</p></th>
</tr>
&#10;<tr data-local-id="9169f8a3-0b2c-48c1-97a0-1027894f59e6">
<td class="confluenceTd" data-local-id="525051cf-328d-42f8-99e0-3debbc9eaf76"><p><code>user_lp_amount</code></p></td>
<td class="confluenceTd" data-local-id="0c40c108-31d5-428f-99ca-a42b9c3463c4"><p>用户 LP 数量</p></td>
<td class="confluenceTd" data-local-id="d9167020-fe94-4105-b17a-552fa1884d5f"><p>钱包连接后 10s, 缓存 ≤ 5s</p>
<p>用户交易完后自动刷新</p></td>
</tr>
<tr data-local-id="fc1a006c-0b0f-4d80-9948-de9f0ea4fa97">
<td class="confluenceTd" data-local-id="0ffea0c2-83cb-4636-863e-b3a640bdb091"><p><code>user_deposit_usd</code></p></td>
<td class="confluenceTd" data-local-id="c4ab8eb7-6d36-4db2-bb52-7e0ccf6d3e48"><p>LP amount × Price</p></td>
<td class="confluenceTd" data-local-id="869de227-f639-4dbf-9071-ecced1a689eb"><p>10s，缓存 ≤ 5s</p>
<p>用户交易完后自动刷新</p></td>
</tr>
<tr data-local-id="f9304eed-3366-4948-86b7-09138c67cdb8">
<td class="confluenceTd" data-local-id="7f9d8a1c-416f-4db1-bb39-85e571fedbbc"><p><code>user_earned_fees_usd</code></p></td>
<td class="confluenceTd" data-local-id="d2a5dce3-452a-43f7-82dd-f527b811d8a2"><p>用户手续费</p>
<ul>
<li><p><strong>user earned fees</strong> = User LP Amount / Pool LP Supply * Pool Earned Fees</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="4affaade-b7e9-478e-b08b-4090ce03ca25"><p>钱包连接后 10s, 缓存 ≤ 5s</p>
<p>用户交易完后自动刷新</p></td>
</tr>
</tbody>
</table>

</div>

### **4.5 Chart**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="266cb9a3-37a7-451e-88c9-83ac67abdef1">
<tbody>
<tr data-local-id="c18f3a6c-1176-4e40-8e7e-ea8cccc5eb8f">
<th class="confluenceTh" data-local-id="569c6b55-af1b-4b91-9f6a-57e24a26a2d8"><p>图表</p></th>
<th class="confluenceTh" data-local-id="d979a189-f4a5-48cf-9aef-f1b62396d386"><p>字段</p></th>
<th class="confluenceTh" data-local-id="a5be0647-9b75-48a4-a7c4-a50fd4131636"><p>类型</p></th>
<th class="confluenceTh" data-local-id="8c3bf727-4e9d-4c62-9a71-5252ff3fb4f1"><p>说明</p></th>
<th class="confluenceTh" data-local-id="b61daaaf-acdf-495d-8296-34f37dff3190"><p>更新频率 / 缓存</p></th>
</tr>
&#10;<tr data-local-id="6699f32c-6fcd-45d0-8130-c03fa0500dd2">
<td class="confluenceTd" data-local-id="b38d86eb-d256-49ef-b81f-7ed58c34602b"><p>TVL</p></td>
<td class="confluenceTd" data-local-id="69881418-de84-4574-9e75-0abc9e00ab82"><p><code>tvl_timeseries[]</code></p></td>
<td class="confluenceTd" data-local-id="8c5d9bcf-c32c-4505-b48f-d71df2c2d399"><p>array&lt;{timestamp, tvl}&gt;</p></td>
<td class="confluenceTd" data-local-id="7ebe595f-6d0c-4f60-af24-65b00ba684a1"><p>30d/90d/180d/All</p></td>
<td class="confluenceTd" data-local-id="f5ef480d-b4c4-4ba4-bf10-b7cf1fd3f5d4"><p>图表粒度<strong>1h</strong></p>
<p><strong>最新数据</strong>更新频率为<strong>10s，</strong>历史数据不变</p>
<p>缓存 30–60s</p></td>
</tr>
<tr data-local-id="8ed41178-56ee-4595-9ec6-b7f37ee44896">
<td class="confluenceTd" data-local-id="38553b9e-1df8-473a-b92f-17253db1acb6"><p>Fee APR</p></td>
<td class="confluenceTd" data-local-id="d39edc51-8661-4272-898f-38067acf8ca4"><p><code>fee_apr_timeseries[]</code></p></td>
<td class="confluenceTd" data-local-id="6a5cd3d4-ff2b-4567-8954-7fe0726cbd8a"><p>array&lt;{timestamp, apr}&gt;</p></td>
<td class="confluenceTd" data-local-id="a0f93323-993f-4dd1-a2f8-1e6c6ad09470"><p>30d/90d/180d/All</p>
<p>n天内手续费变化值/n天内TVL加成平均 * 时间</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="315b4a65a4d2260ae74b4e018eb0dffb3b5578aa7a59f40377f540424ef7ec33" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-12-18%20at%2010.20.19.png?version=1&amp;modificationDate=1766024474848&amp;cacheVersion=1&amp;api=v2" data-height="82" data-width="385" data-unresolved-comment-count="0" data-linked-resource-id="57901061" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-18 at 10.20.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="42f1f8ce-a2b0-4f26-a12f-3b6324d22d88" data-media-type="file" width="251" height="53" alt="Screenshot 2025-12-18 at 10.20.19.png" /></span></td>
<td class="confluenceTd" data-local-id="4b8f29f2-7d9f-40d7-9bab-2e0f71048ff9"><p>图表粒度<strong>1h</strong></p>
<p><strong>最新数据</strong>更新频率为<strong>10s，</strong>历史数据不变</p>
<p>缓存 30–60s</p></td>
</tr>
<tr data-local-id="1974bb4c-9567-46da-8740-e85574cd4f6e">
<td class="confluenceTd" data-local-id="4dae19dc-666c-4190-9a9e-a4110a1dadf0"><p>附加字段（计算）</p></td>
<td class="confluenceTd" data-local-id="cd38929a-6787-4d17-b50a-21cb4883ad95"><p><code>fee_apy_current</code></p></td>
<td class="confluenceTd" data-local-id="ffadac56-0683-4130-bba6-1e021d8b4428"><p>number</p></td>
<td class="confluenceTd" data-local-id="399db3f9-7687-453c-9072-e8486c3bf37b"><p>T = 30d/90d/180d/All</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8ac8fb0bfe4da6e6572b9c9954e02bf59ea21c80b65ab9275042f09e90c74458" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/36372492/Screenshot%202025-11-19%20at%2012.52.40.png?version=1&amp;modificationDate=1763527997432&amp;cacheVersion=1&amp;api=v2" data-height="67" data-width="304" data-unresolved-comment-count="0" data-linked-resource-id="40468504" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-19 at 12.52.40.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="36372492" data-linked-resource-container-version="18" data-media-id="93630c59-1af9-4308-8154-c0535935b0ab" data-media-type="file" width="251" height="55" alt="Screenshot 2025-11-19 at 12.52.40.png" /></span></td>
<td class="confluenceTd" data-local-id="40bce9ee-032e-41bb-a984-91c52efd35d4"><p>图左上角显示的计算后年化APY</p></td>
</tr>
</tbody>
</table>

</div>

### **4.7 Liquidity History**

- 后端cursor分页：size = 6，点击load more返回 next_cursor，默认按成交时间desc

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="5885b7cb-2aab-45b3-acbe-8862e8235f3f">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="6580bf13-51f5-43b6-a0ba-dd59af5b9de7">
<th class="confluenceTh" data-local-id="3a5b33c2-476a-4ba5-875f-fd321fe156d1"><p>字段</p></th>
<th class="confluenceTh" data-local-id="a7f8ed3a-d28c-45c5-9d13-25d8ef5e5e53"><p>说明</p></th>
<th class="confluenceTh" data-local-id="05d84010-ab3e-4a42-8223-d4c68e43fa97"><p><strong>更新频率/缓存</strong></p></th>
</tr>
&#10;<tr data-local-id="437c1e11-46a8-4721-9305-45cd1db6d590">
<td class="confluenceTd" data-local-id="0e2af88b-70b6-483d-a298-f753cbabf91f"><p><code>pool_address</code></p></td>
<td class="confluenceTd" data-local-id="a6a258fb-8e00-49f3-9f3e-afbbfe0f8407"><p>池子合约地址 相当于作为pool id唯一标识</p></td>
<td class="confluenceTd" data-local-id="49d3aa18-a9cc-469b-952d-796d370e958a"><p><strong>最新数据</strong>更新频率为<strong>10s，</strong>历史数据不变；缓存 ≤ 5s</p></td>
</tr>
<tr data-local-id="5f77605d-1324-4e33-bebe-845b637c5c17">
<td class="confluenceTd" data-local-id="0be0b59e-a537-4291-9b91-45e37ce65f1e"><p><code>wallet_address</code></p></td>
<td class="confluenceTd" data-local-id="28c315d9-1368-460b-baab-8c7070b767f4"><p>用于前端展示user activity</p></td>
<td class="confluenceTd" data-local-id="9ce300b2-6f0d-4a29-88a2-6032ace92d05"></td>
</tr>
<tr data-local-id="8fcf46f4-b6db-43d8-b5bb-6abe605ab723">
<td class="confluenceTd" data-local-id="55844edf-6918-4495-894b-ac7519a3d454"><p><code>tx_hash</code></p></td>
<td class="confluenceTd" data-local-id="ddff9077-b006-46f5-a815-a2551c04dc1b"><p>区块链哈希</p></td>
<td class="confluenceTd" data-local-id="017db343-e90b-4aa3-8ad8-f5ace582bb85"></td>
</tr>
<tr data-local-id="ed940e5d-3917-44b1-9565-5f6adaadf912">
<td class="confluenceTd" data-local-id="d75123b3-8519-4ee7-9adc-317481fe9c7f"><p><code>timestamp</code></p></td>
<td class="confluenceTd" data-local-id="11867d06-efee-452c-933d-e0d22c7f960c"><p>Unix 时间（前端转本地时间）</p></td>
<td class="confluenceTd" data-local-id="e7db9166-7058-4fe0-8b0a-c71f402b78ff"></td>
</tr>
<tr data-local-id="6ddce96e-04f5-47f6-afa2-2d06db531c5b">
<td class="confluenceTd" data-local-id="3a29a87a-306c-4c36-8f99-21bbd6d1e1b3"><p><code>action</code></p></td>
<td class="confluenceTd" data-local-id="411d0f3a-00e0-4b95-968f-521fd2530d19"><p>Deposit / Withdraw/Shift</p></td>
<td class="confluenceTd" data-local-id="39a7c32b-fa06-4aae-9f40-e0b4e8a33a22"></td>
</tr>
<tr data-local-id="f3b9573b-3718-4673-a8c0-be74e70353b5">
<td class="confluenceTd" data-local-id="4f666cb7-bce7-4cd2-a5f3-b05e3ca47af1"><p><code>lp_shares</code></p></td>
<td class="confluenceTd" data-local-id="1a8de4db-2fdb-4ffa-a971-6a9fe3bf084c"><p>HzLP 变动数量</p></td>
<td class="confluenceTd" data-local-id="1aa994be-9b78-47e9-b1b9-346caff384e1"></td>
</tr>
<tr data-local-id="c2cbd13c-14be-4d6c-bc7c-8703688e2f98">
<td class="confluenceTd" data-local-id="3b5d8ff9-8559-4bd1-9016-38b196f55888"><p><code>deposit_usd</code></p></td>
<td class="confluenceTd" data-local-id="f0231d92-3763-48f3-823b-c5dcadb22f10"><p>Deposit_USD = LP × Price</p></td>
<td class="confluenceTd" data-local-id="68282c03-77f5-42c0-9992-cacc0b3a36fc"></td>
</tr>
<tr data-local-id="c8f96e1a-4f06-49ad-b122-429a04fc2108">
<td class="confluenceTd" data-local-id="ddb2edc7-527b-4b4c-bed3-f90f3781eb53"><p><code>fees_earned_usd</code></p></td>
<td class="confluenceTd" data-local-id="c7ea3414-11db-43f9-a653-e51ce8d19c0b"><p>Fees Earned = Withdraw_USD – Initial_Deposit_USD</p></td>
<td class="confluenceTd" data-local-id="a686b501-88c0-41dd-9024-8ba128e851cc"><p>10 HzLP 2$<br />
20HzLP initial deposit = 50<br />
20 - 10/20 * 50 = -5</p></td>
</tr>
<tr data-local-id="32e86578-950e-4b43-a2d6-b6699061cbd2">
<td class="confluenceTd" data-local-id="f786304b-5cc5-432f-8336-a2191da5c6fb"><p><code>total_value_usd</code></p></td>
<td class="confluenceTd" data-local-id="66907c16-f3b4-4f2f-8f49-cb22883faf43"><p>deposit_usd + fees_earned_usd</p></td>
<td class="confluenceTd" data-local-id="ad51fa76-a629-4204-a5e8-57b3997211f2"></td>
</tr>
</tbody>
</table>

</div>

</div>
