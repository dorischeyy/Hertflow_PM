# Part 2. GMX V2 业务部分

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270766114 {padding: 0px;}
div.rbtoc1772270766114 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270766114 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270766114">

- [0. GMX Market 资金图](#Part2.GMXV2业务部分-0.GMXMarket资金图)
- [1. Trading](#Part2.GMXV2业务部分-1.Trading)
  - [1.1 Fees 费用](#Part2.GMXV2业务部分-1.1Fees费用)
    - [1.1.1 Price Impact Fee 价格冲击费](#Part2.GMXV2业务部分-1.1.1PriceImpactFee价格冲击费)
    - [1.1.2 Virtual Inventory 虚拟库存](#Part2.GMXV2业务部分-1.1.2VirtualInventory虚拟库存)
    - [1.1.3 Swap Fees 兑换涉及费用](#Part2.GMXV2业务部分-1.1.3SwapFees兑换涉及费用)
    - [1.1.4 Position Fees 仓位涉及费用](#Part2.GMXV2业务部分-1.1.4PositionFees仓位涉及费用)
    - [1.1.5 Borrowing Fee 借贷费](#Part2.GMXV2业务部分-1.1.5BorrowingFee借贷费)
    - [1.1.6 Funding Fee 资金费](#Part2.GMXV2业务部分-1.1.6FundingFee资金费)
  - [1.2 Order Types 订单类型](#Part2.GMXV2业务部分-1.2OrderTypes订单类型)
  - [1.3 Swap 兑换](#Part2.GMXV2业务部分-1.3Swap兑换)
    - [1.3.1 Token Flow](#Part2.GMXV2业务部分-1.3.1TokenFlow)
    - [1.3.2 Market swap 市价兑换](#Part2.GMXV2业务部分-1.3.2Marketswap市价兑换)
    - [1.3.3 Limit swap 限价兑换](#Part2.GMXV2业务部分-1.3.3Limitswap限价兑换)
  - [1.4 Perpetual 合约交易](#Part2.GMXV2业务部分-1.4Perpetual合约交易)
    - [1.4.1. Long 做多](#Part2.GMXV2业务部分-1.4.1.Long做多)
    - [1.4.2. Short 做空](#Part2.GMXV2业务部分-1.4.2.Short做空)
    - [1.4.3. TP && SL 止盈止损](#Part2.GMXV2业务部分-1.4.3.TP&&SL止盈止损)
    - [1.4.4. Claim Funding Fees 提取资金费](#Part2.GMXV2业务部分-1.4.4.ClaimFundingFees提取资金费)
    - [1.4.5. Claim Collateral 提取保证金](#Part2.GMXV2业务部分-1.4.5.ClaimCollateral提取保证金)
- [2. Liquidation 强平](#Part2.GMXV2业务部分-2.Liquidation强平)
  - [2.1 Liquidation 逻辑](#Part2.GMXV2业务部分-2.1Liquidation逻辑)
  - [2.2 Approximate Liquidation Price 预估强平价](#Part2.GMXV2业务部分-2.2ApproximateLiquidationPrice预估强平价)
  - [2.3 ADL Auto Deleveraging 自动去杠杆](#Part2.GMXV2业务部分-2.3ADLAutoDeleveraging自动去杠杆)
  - [2.4 Insolvent Closing 破产强平](#Part2.GMXV2业务部分-2.4InsolventClosing破产强平)
- [3. Liquidity 流动性](#Part2.GMXV2业务部分-3.Liquidity流动性)
  - [3.1 GM Pool](#Part2.GMXV2业务部分-3.1GMPool)
    - [3.1.1 GM Token Price](#Part2.GMXV2业务部分-3.1.1GMTokenPrice)
    - [3.1.2 Fees](#Part2.GMXV2业务部分-3.1.2Fees)
    - [3.1.3 Deposit / Mint](#Part2.GMXV2业务部分-3.1.3Deposit/Mint)
    - [3.1.4 Withdraw / burn](#Part2.GMXV2业务部分-3.1.4Withdraw/burn)
    - [3.1.5 Shift](#Part2.GMXV2业务部分-3.1.5Shift)
  - [3.2 GLV](#Part2.GMXV2业务部分-3.2GLV)
    - [3.2.1 GLV Token Price](#Part2.GMXV2业务部分-3.2.1GLVTokenPrice)
    - [3.2.2 GLV Fees](#Part2.GMXV2业务部分-3.2.2GLVFees)
    - [3.2.3 GLV Deposit Mint](#Part2.GMXV2业务部分-3.2.3GLVDepositMint)
    - [3.2.4 GLV Withdraw Burn](#Part2.GMXV2业务部分-3.2.4GLVWithdrawBurn)
    - [3.2.5 GLV Shift](#Part2.GMXV2业务部分-3.2.5GLVShift)

</div>

## 0. GMX Market 资金图

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1680b60e7da201a3dafe194d1badfaa45cab23cb0bae53665d00fe6235986e2e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571463/image-20251123-062406.png?version=1&amp;modificationDate=1763879052324&amp;cacheVersion=1&amp;api=v2" data-height="467" data-width="526" data-unresolved-comment-count="0" data-linked-resource-id="42008589" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251123-062406.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571463" data-linked-resource-container-version="48" data-media-id="b2584967-5989-4ad4-89fe-6c5a626ee822" data-media-type="file" width="468" height="414" alt="image-20251123-062406.png" /></span>

- **Pool Amount**: LP deposit 的资金 + 作为对手方的盈利 + 手续费沉淀，用于给 pool 估值。简单理解为 pool value without (pending)PnL，也就是 Pool 资产。这是一个逻辑概念，本质上在合约内由以下部分计算：

  - <u>long token amount</u>

  - <u>short token amount</u>

  - <u>long OI</u>

  - <u>short OI</u>

  - <u>long OI in tokens</u>

  - <u>short OI in tokens</u>

  - 有了以上部分，参考当前 oracle 价格和费率等信息，可以辅助计算出 pnl，pending fee 等。

- **Collateral:** 用户开仓的保证金，不会计入 pool 资产中，而是单独存储。（扣除的funding fee也留存在里面，但是 position.collateral 字段会减少，逻辑上不持有）

- **Pending PnL:** 用户仓位的 PnL，用户浮盈时，就会侵占 Pool Amount，影响 LP 质押的 mint 计算。

- **Claimable Funding Fee:** 可提取资金费单独计费，也不会计入 Pool 资产。

- **Swap Price Impact:** swap 操作带来的 price impact fee 是单独存储在这里的，不会计入 Pool 资产。注意，Position Price Impact 和 swap 不一样，是直接和 pool 资产交互结算的，没有独立出来，只是维护了一个负债表，见这里：<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#3.1.4-Withdraw-%2F-burn" data-card-appearance="inline" data-local-id="c19fd5c4-b191-4e32-b32f-a813e42768b9" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#3.1.4-Withdraw-%2F-burn</a> 的 validate lendable 章节有进一步说明。

- **Claimable Fees:** 部分费用按照一定比例留下来放到这里，剩余部分才转入 pool 中。

  - Position Fees: borrow fee + liquidation fee

  - Swap Fees: swap fee

  - Deposit/Withdraw: swap fee

- **UI Fees:** 图中没列举，就是 UI provider 的费用，固定收费。

------------------------------------------------------------------------

## 1. Trading

### 1.1 Fees 费用

#### 1.1.1 Price Impact Fee 价格冲击费

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**保持多空平衡，如果一个操作（swap, long/short, deposit):

- 减少了不平衡 =\> positive impact =\> rebate ⬆️⬆️⬆️

- 加剧了不平衡 =\> negative impact =\> extra fee ⬇️⬇️⬇️

**冲击类型**：

- Same Side，操作后，不平衡仍在同一边，比如 long OI 还是大于 short OI

- Cross Over，操作后，不平衡方向发生了改变，比如之前 long OI \> short OI，之后则 short \> long

对于不同的冲击类型，收取费用的算法是不一致的。

**可视化：**

<a href="https://www.desmos.com/calculator/sykma4sbbb" class="external-link" data-card-appearance="inline" data-local-id="3df0147e-4bb2-4b44-8118-c6c698d36eed" rel="nofollow">https://www.desmos.com/calculator/sykma4sbbb</a>

**For 研发**：

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/35160083/Price+Impact" data-linked-resource-id="35160083" data-linked-resource-version="5" data-linked-resource-type="page">Price Impact 代码解读</a>

</div>

</div>

- Swap

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Imbalance for swap = |long tokens in pool USD - short tokens in pool USD|
Positive impact -> bonus to amount out
Negative impact -> fee to amount in
```

</div>

</div>

- Long and Short

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Imbalance for long and short = |long open interest - short open interest|
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Open
  Long
    Positive impact -> increase size delta in tokens -> lower execution price
    Negative impact -> decrease size delta in tokens -> higher execution price
  Short
    Positive impact -> decrease size delta in tokens -> higher execution price
    Negative impact -> increase size delta in tokens -> lower execution price
Close
  Positive impact -> receive token
  Negative impact -> pay from collateral
```

</div>

</div>

- Deposit Liquidity 添加流动性

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Imbalance for deposit liquidity = |long tokens in pool USD - short tokens in pool USD|
Positive impact -> mint additional market token
Negative impact -> fees deducted from deposit amounts
```

</div>

</div>

------------------------------------------------------------------------

#### 1.1.2 Virtual Inventory 虚拟库存

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**防止价格操纵，或者说减少套利空间

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/35946541/Virtual+Inventory" data-linked-resource-id="35946541" data-linked-resource-version="1" data-linked-resource-type="page">Virtual Inventory 代码解读</a>

</div>

</div>

由于 GMX 拆分了多个市场，市场往往具有相同的一个 token，例如 \[ETH/USDC\] 和 \[ETH/USDT\]，不同市场之间的不平衡往往不相同。

于是用户可以通过拆分交易，从而避免部分 price impact 费用。比如用户试图使用大量 USDC 去换出 ETH，此时用户可以选择有利于他的池子去做 swap。

Virtual Inventory 则实现了 token 的聚合：

- 对于 swap 来说，GMX 维护一个虚拟的 virtual market，这个 market 也有 long / short token 之分，每个真实 market 都可以挂靠在一个 virtual market 下，这个 virtual market 会统计相关真实 market 的 long token 之和作为自己的 long token，short token 同理。

  - 例子：\[ETH/USDC\] / \[ETH/USDT\] / \[WETH / USDC\] 均挂靠在同一个 virtual market。由于 token 数量不区分type进行糅合，因此需要 long/short token 的价格近似，这里假定了 ETH≈WETH 以及 USDC ≈ USDT。

- 对于 position 来说，GMX 则是按照 token 类型进行维护，构造的不是 virtual market 而是 virtual token。全局用户开仓时，如果 long OI 增加了，则认为 virtual token 被借走，减少其值，short OI 增加则相反，认为用户卖出了 token 给我们，于是增加其值。

在计算 price impact 费用时，GMX 会按照相同的算法，<u>首先计算当前 market 不平衡下的 price impact 费用，然后再根据 virtual inventory 体现的不平衡（也就是全局不平衡）计算一遍，取两者之中最大的那一个值作为最终 price impact fee，从而避免了逃费。</u>

------------------------------------------------------------------------

#### 1.1.3 Swap Fees 兑换涉及费用

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

Swap 操作在页面上展示的费用与合约里面实际收取的费用并不完全对照；

产品层面省略了部分具体的费用类型，取而代之的是一些模糊的估计值。

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/36012113/Swap+Fees" data-linked-resource-id="36012113" data-linked-resource-version="1" data-linked-resource-type="page">Swap Fees 代码解读</a>

</div>

</div>

具体来说，swap 收取了如下费用：

- 根据操作类型收取不同比例的固定交易费用，称之为 swap fee

  - swap fee 中的一部分，会被按照固定比例瓜分一部分到 `receiver` 中

  - 瓜分之后的剩余部分，才会被纳入池中保留

- 还会收取一笔 UI Fee，用来奖励 GMX UI 开发者，这部分奖励会按照 market 和 tokenIn 进行分类保存。

------------------------------------------------------------------------

#### 1.1.4 Position Fees 仓位涉及费用

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**仓位收取费用如下：**

- Execution fee，执行费，一次性费用，支付给 keeper

- Borrowing fee，借贷费，持续性费用，支付给池子

- Liquidation fee，强平费，一次性费用，支付给池子

- Funding fee，资金费，持续性费用，支付给对手

- UI fee，页面费，一次性费用，支付给 UI 提供商

- Price impact fee，价格冲击费，一次性费用，支付给池子

- Deposit / withdrawal fee，一次性费用，支付给池子

- Swap fee，一次性费用，支付给池子

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/36372519/Position+Fees" data-linked-resource-id="36372519" data-linked-resource-version="2" data-linked-resource-type="page">Position Fees 代码解读</a>

</div>

</div>

------------------------------------------------------------------------

#### 1.1.5 Borrowing Fee 借贷费

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**防止用户持续持仓，直到盈利才平仓；以及激励 LP。

**可视化**：

- kink 双斜率费用：<a href="https://www.desmos.com/calculator/9khv07nrfb" class="external-link" data-card-appearance="inline" data-local-id="0a02608a-1faa-4878-9679-33a0163b1e23" rel="nofollow">https://www.desmos.com/calculator/9khv07nrfb</a>

- curve 曲线费用：<a href="https://www.desmos.com/calculator/m8hkic2pxn" class="external-link" data-card-appearance="inline" data-local-id="ee6484c9-1962-4cff-9de5-475c4b87359a" rel="nofollow">https://www.desmos.com/calculator/m8hkic2pxn</a>

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=36438077&amp;draftShareId=cde6a307-a30c-4f61-82ea-1a95eb1b1b11&amp;atlOrigin=eyJpIjoiZDA2NTVlMzdiODQ4NDY0ZjhlMjFlYTNkNzBkZmRlYzQiLCJwIjoiYyJ9" data-card-appearance="inline" data-local-id="089ac2f9-4167-410d-b141-ec04e914023b" rel="nofollow">https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=36438077&amp;draftShareId=cde6a307-a30c-4f61-82ea-1a95eb1b1b11&amp;atlOrigin=eyJpIjoiZDA2NTVlMzdiODQ4NDY0ZjhlMjFlYTNkNzBkZmRlYzQiLCJwIjoiYyJ9</a>

</div>

</div>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7077bb9714a426b68038e3684f6d29c9c88982f2c198f506da02d1b51e671071" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571463/image-20251112-070334.png?version=1&amp;modificationDate=1762931017963&amp;cacheVersion=1&amp;api=v2" data-height="1251" data-width="1003" data-unresolved-comment-count="0" data-linked-resource-id="36012235" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251112-070334.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571463" data-linked-resource-container-version="48" data-media-id="663a0f6c-d839-47d6-95c9-b6c4aa1e975d" data-media-type="file" width="468" height="585" alt="image-20251112-070334.png" /></span>

**解释：**

- 直观：借贷费率 R 每秒都在变化，仓位每秒支付一次借贷费，费用为仓位大小 C 乘以 R。

- 工程：每秒进行费用收取计算量过大，gas fee 消耗过多。可以看到仓位大小 C 在不进行加减仓操作时，是一个常量不会变化。这段时间内(from time k to N)可以抽象为上面的公式，公式中的 C 以及借贷费累积在工程上更好实现。

------------------------------------------------------------------------

#### 1.1.6 Funding Fee 资金费

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**促进多空平衡

**支付方式：**力量更强的一方直接支付给力量更弱的一方，与 LP 无关

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=36831248&amp;draftShareId=efb81fb3-a2c4-45d4-abda-a9fff6514179&amp;atlOrigin=eyJpIjoiNGJiYTM1ODg0NDljNDVjM2FkYmE5MTdhNDhhNTc3ZjgiLCJwIjoiYyJ9" data-card-appearance="inline" data-local-id="4a081450-c469-4766-a83a-9583b406ffac" rel="nofollow">https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=36831248&amp;draftShareId=efb81fb3-a2c4-45d4-abda-a9fff6514179&amp;atlOrigin=eyJpIjoiNGJiYTM1ODg0NDljNDVjM2FkYmE5MTdhNDhhNTc3ZjgiLCJwIjoiYyJ9</a>

</div>

</div>

**公式：**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
f: 基础费率 per second

dt: 距离上次资金费支付的时间，in seconds

divisor: 
- If Long OI > Short OI, divisor = 2.
- else divisor = 1.

size of larger side: OI USD.

size of smaller side: OI USD.
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Funding Fee per Size (USD) = f * dt * (size of larger side / size of smaller side) / divisor

简化理解：f(x) = ax：
- 其中 x 对应上面 f*dt，代表需要支付的费用 (rate_per_sec * duration)
- a 代表不平衡，large/small/divisor，比如 51%/49%/2
```

</div>

</div>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3861d801daf5563a87305a5a638aad88be33199084be234e42c51cb06c8721b4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571463/image-20251113-064816.png?version=1&amp;modificationDate=1763016501327&amp;cacheVersion=1&amp;api=v2" data-height="1639" data-width="1053" data-unresolved-comment-count="0" data-linked-resource-id="36831241" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251113-064816.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571463" data-linked-resource-container-version="48" data-media-id="52aa30bd-f344-4a11-8743-899800fae2f7" data-media-type="file" width="468" height="726" alt="image-20251113-064816.png" /></span>

------------------------------------------------------------------------

### 1.2 Order Types 订单类型

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="7934aca7-3f1f-4b1c-b4d3-d1e8d494c355">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="f0a78aa1-cba2-442a-b12d-4c5344748004">
<th class="confluenceTh" data-local-id="dcb7918f-e217-4b65-a858-ade672a0dcea"><p><strong>Order Type</strong></p></th>
<th class="confluenceTh" data-local-id="fb204a87-4505-4e6e-89f6-410c0aef7215"><p><strong>Desc</strong></p></th>
<th class="confluenceTh" data-local-id="5474c267-c936-41dc-8964-2905b12221b5"><p><strong>Desc Zh</strong></p></th>
</tr>
&#10;<tr data-local-id="c472c3fa-31a5-42d8-864d-e17627239c03">
<td class="confluenceTd" data-local-id="d0c523d2-ae22-4d4b-8402-6f59a1db57f6"><p>market swap</p></td>
<td class="confluenceTd" data-local-id="fa0df07a-d06c-4116-b8ec-8fadffae60d9"><p>swap token A to token B at the current market price</p>
<ul>
<li><p>the order will be <code>cancelled</code> if the <code>minOutputAmount</code> cannot be fulfilled</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="76d031f6-c7e0-4721-9581-7be6fc52823a"><p>市价兑换</p></td>
</tr>
<tr data-local-id="f6854ba7-a291-4172-9bff-6baa952561ef">
<td class="confluenceTd" data-local-id="8ed0acd4-4a65-4bfb-86cf-bfb46326aac1"><p>limit swap</p></td>
<td class="confluenceTd" data-local-id="07da7c64-164c-4ff1-a72e-c79ef7eb5b80"><p>swap token A to token B if the <code>minOutputAmount</code> can be fulfilled</p></td>
<td class="confluenceTd" data-local-id="8d8d7945-ab3f-4235-97eb-492b777c9f9d"><p>限价兑换</p></td>
</tr>
<tr data-local-id="0194d651-9a54-405c-b51e-3071676ed15c">
<td class="confluenceTd" data-local-id="ad63e367-58f5-4b74-ae13-aeed6c5b4da8"><p>market increase</p></td>
<td class="confluenceTd" data-local-id="b11e6f72-92d9-4abb-bcf1-ae26306440fd"><ul>
<li><p>market open</p></li>
<li><p>increase position size</p></li>
<li><p>the order will be <code>cancelled</code> if the position cannot be increased at the <code>acceptablePrice</code></p></li>
</ul></td>
<td class="confluenceTd" data-local-id="0fefdf7b-0ba7-4df8-9a82-34786a24de6a"><p>市价开仓或加仓</p></td>
</tr>
<tr data-local-id="b40d93a4-bcbb-48e8-9798-79f95a57366a">
<td class="confluenceTd" data-local-id="02b67c32-780d-4b12-b10a-94830e77f427"><p>limit increase</p></td>
<td class="confluenceTd" data-local-id="a71d510d-fd3d-466b-812b-e3114db15043"><p>increase position if the <code>triggerPrice</code> is reached and the <code>acceptablePrice</code> can be fulfilled</p></td>
<td class="confluenceTd" data-local-id="b3436597-4776-4bbb-a342-cd18642bef52"><p>限价开仓或加仓</p></td>
</tr>
<tr data-local-id="f462b5d7-2659-42e0-a549-b40f9acbd879">
<td class="confluenceTd" data-local-id="d38d8c87-4a34-4508-85b4-7f627c000951"><p>market decrease</p></td>
<td class="confluenceTd" data-local-id="21d26b6f-58d8-43f2-8b8f-ca753f5bffab"><ul>
<li><p>market close</p></li>
<li><p>decrease position size</p></li>
<li><p>the order will be <code>cancelled</code> if the position cannot be decreased at the <code>acceptablePrice</code></p></li>
</ul></td>
<td class="confluenceTd" data-local-id="0413628c-1e0c-44e6-9343-93a7f918570c"><p>市价平仓或减仓</p></td>
</tr>
<tr data-local-id="305e6a69-fcee-450b-ba15-8783ef8ff76d">
<td class="confluenceTd" data-local-id="9f053029-47ad-4640-8f0d-20847d45250b"><p>limit decrease</p></td>
<td class="confluenceTd" data-local-id="3c12ad3c-a480-41ee-913e-82d8cdb8e656"><p>take profit</p>
<ul>
<li><p>decrease position if the <code>triggerPrice</code> is reached and the <code>acceptablePrice</code> can be fulfilled</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="f248b8cb-630f-41a0-ae5a-64e62aaac78b"><p>限价减仓（止盈）</p></td>
</tr>
<tr data-local-id="23cb73ad-08af-4519-87ce-c6bdd411f9e4">
<td class="confluenceTd" data-local-id="630fc35e-99ce-4cd9-ae2a-31196f248bbd"><p>stop loss decrease</p></td>
<td class="confluenceTd" data-local-id="a562db93-76dc-4ee0-8aa8-37c4013ccf66"><p>stop loss</p>
<ul>
<li><p>decrease position if the <code>triggerPrice</code> is reached and the <code>acceptablePrice</code> can be fulfilled</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="acd3f326-0d84-449f-90bf-eb0b82a2f835"><p>限价减仓（止损）</p></td>
</tr>
<tr data-local-id="b5e7674f-2733-48eb-94f7-d8acf85ab807">
<td class="confluenceTd" data-local-id="350e44e0-a5d9-44c3-8c4a-4d4b67dedd10"><p>liquidation</p></td>
<td class="confluenceTd" data-local-id="0e8d89f2-1d32-4b11-8170-a0797358f78e"><p>allows liquidation of positions if the criteria for liquidation are met</p></td>
<td class="confluenceTd" data-local-id="a84d9943-0d2d-49c7-8d0b-5b6a01d660cb"><p>强平</p></td>
</tr>
<tr data-local-id="097dafae-c66f-470a-b110-a48a7f2c3be4">
<td class="confluenceTd" data-local-id="af65cae0-bf6a-4335-96f8-dc0acfc695b6"><p>stop increase</p></td>
<td class="confluenceTd" data-local-id="e3cc7450-c331-425e-a167-7659db53a078"><p>increase position if the <code>triggerPrice</code> is reached and the <code>acceptablePrice</code> can be fulfilled</p></td>
<td class="confluenceTd" data-local-id="e3ae6932-007a-4148-9852-c0da230b7bbf"><p>限价加仓（抄底，止损的反面）</p></td>
</tr>
</tbody>
</table>

</div>

------------------------------------------------------------------------

### 1.3 Swap 兑换

> **For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/39747670/Swap" data-linked-resource-id="39747670" data-linked-resource-version="2" data-linked-resource-type="page">Swap 代码解读</a>

#### 1.3.1 Token Flow

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c9e006eff915032e1715912ac68785c5956389d71c5bd8061cef16248ae4092d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571463/image-20251118-083611.png?version=1&amp;modificationDate=1763454974219&amp;cacheVersion=1&amp;api=v2" data-height="646" data-width="977" data-unresolved-comment-count="0" data-linked-resource-id="39845943" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251118-083611.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571463" data-linked-resource-container-version="48" data-media-id="0550043a-ef54-4567-ba2d-6ed252ec9818" data-media-type="file" width="468" height="309" alt="image-20251118-083611.png" /></span>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
背景：User 用 DAI 换取 WETH, 但 GMX 没有 DAI-WETH pool，因此需要间接 swap。

0. User 发送 DAI 作为入金，以及部分 WETH 作为 Execution Fee 到 OrderVault，创建 SwapOrder。
1. Keeper 调用 OrderHandler 执行订单
2. OrderHandler 从 OrderVault 中取出 0 中 User 存入的 DAI
3+4. OrderHandler 把 DAI 发送到 DAI-USDC swap only pool 中换取 USDC。
5+6. 换出的 USDC 发送到 USDC-WETH pool 中换取 WETH
7. 换出的 WETH 转给 User
8+9+10+11. User 存入 OrderVault 的 WETH，其中一部分被 keeper 拿走作为执行费用，另一部分 refund 回 User。
```

</div>

</div>

------------------------------------------------------------------------

#### 1.3.2 Market swap 市价兑换

#### 1.3.3 Limit swap 限价兑换

这里产品层面上没有特别需要注意的点，Market 和 Limit 的实现，通过 minOut 参数实现。

比如 ETH 现在 3000\$，我用 USDC 做 swap

- minOut 只要 \<= 1 就可以认为是市价了。

- minOut \> 1，比如设置为 2，就意味着我限价 1500\$ 用 USDC 去 swap ETH。

------------------------------------------------------------------------

### 1.4 Perpetual 合约交易

GMX V2 仍然沿用仓位合并逻辑：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// key: account-market-collateral-isLong
bytes32 positionKey = Position.getPositionKey(params.order.account(), params.order.market(), collateralToken, params.order.isLong());
Position.Props memory position = PositionStoreUtils.get(params.contracts.dataStore, positionKey);

// initialize position
if (position.account() == address(0)) {
    position.setAccount(params.order.account());
    if (position.market() != address(0) || position.collateralToken() != address(0)) {
        revert Errors.UnexpectedPositionState();
    }

    position.setMarket(params.order.market());
    position.setCollateralToken(collateralToken);
    position.setIsLong(params.order.isLong());
}
```

</div>

</div>

<div class="confluence-information-macro confluence-information-macro-note">

<span class="aui-icon aui-icon-small aui-iconfont-warning confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

可以看到，key 里面包含了 market 字段，因此如果需要保持仓位的合并，一定不能出现相同的 market。

即：当用户试图用 USDC 做空 ETH 时，不能让他找到两个 ETH/USD\[WETH-USDC\] 的 market。否则即使 account / collateral / isLong 一致，也会因为 market 不一致导致仓位分开。

目前 GMX 合约直接禁止了创建相同市场的操作：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
bytes32 salt = keccak256(abi.encode(
    "GMX_MARKET",
    indexToken,
    longToken,
    shortToken,
    marketType
));

address existingMarketAddress = dataStore.getAddress(MarketStoreUtils.getMarketSaltHash(salt));
if (existingMarketAddress != address(0)) {
    revert Errors.MarketAlreadyExists(salt, existingMarketAddress);
}
```

</div>

</div>

</div>

</div>

#### 1.4.1. Long 做多

#### 1.4.2. Short 做空

> **For 研发**：
>
> <a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/40534046/Increase+Position" data-linked-resource-id="40534046" data-linked-resource-version="2" data-linked-resource-type="page">Increase Position 代码解读</a>
>
> <a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/40697884/Decrease+Position" data-linked-resource-id="40697884" data-linked-resource-version="2" data-linked-resource-type="page">Decrease Position 代码解读</a>

------------------------------------------------------------------------

#### 1.4.3. TP && SL 止盈止损

开仓时设置止盈止损会一口气（原子的）创建三个订单：

1.  多空仓单

2.  创建 Stop Loss order，通过修改 order type 实现，见 <a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#1.2-Order-Types-%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B" data-card-appearance="inline" data-local-id="159817cb-e106-466f-953c-f51336eb3384" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#1.2-Order-Types-%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B</a> 的 Stop Loss Order

3.  创建 Take Profit order，同 2，见<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#1.2-Order-Types-%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B" data-card-appearance="inline" data-local-id="20f0faa7-30d9-4e0b-b812-e6f3fdc0c13f" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#1.2-Order-Types-%E8%AE%A2%E5%8D%95%E7%B1%BB%E5%9E%8B</a> 的 Limit Decrease Order

------------------------------------------------------------------------

#### 1.4.4. Claim Funding Fees 提取资金费

合约把资金费提到了一个单独的池子里面，提供了一个单独的接口给用户 claim。需要用户手动触发。

`ExchangeRouter.claimFundingFees`

------------------------------------------------------------------------

#### 1.4.5. Claim Collateral 提取保证金

1.  减仓的时候触发一次 funding fee 结算，claimable 部分由 keeper 负责提取。\
    减仓本身有两种 output token，一个是 coll，一个是 pnl，pnl 可能和 coll 不一样，比如 WETH/USDC 市场，用 USDC 做多，此时 coll = USDC, pnl = WETH\
    资金费设计为从你的 coll token 中划走一部分支付。\
    如果你的仓位减仓的时候，coll 已经不足以支付 funding 了，就要从 pnl 里面扣。\
    但是为了统一，所以还是需要 funding 和 coll 一致，因此 pnl 划扣出来的等价 WETH，暂存在这里，等待 keeper 提取出来做 swap 回 USDC 再返给池子。这样就对上了。

2.  减仓的时候触发一次 price impact 结算，这里如果给你的是 bonus 奖励，丢到这里由用户提取。\
    这里逻辑是：GMX 判断是否能平仓的时候，把你的 price impact bonus \>0 强制设置为 0，惩罚\<0则保留下来计数，（目的是为了避免脆弱的仓位，靠 impact 奖励续命，其实离强平也不远了）\
    但是判断完之后，这部分奖励还是会随着减仓给到用户，但是这个奖励不计入pnl，而是丢这里了。

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

Funding Fee Keeper 托管逻辑：（猜测）

用户 claimable funding fee，收到奖励的时候，会提走两种 token，有 WETH 和 USDC，因为对手方可以用这两种 token 开仓，所以不同的对手支付不同的 token 作为 funding。\
如果不这样平衡swap一下，可能会导致其中一种 token 提多了不补上，进而导致 pool.longToken amount 不足，但池子 usd 是对的。

</div>

</div>

------------------------------------------------------------------------

## 2. Liquidation 强平

### 2.1 Liquidation 逻辑

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**避免合约损失

注意，虽然合约上对于强平的实现，有各种严格的校验，但是本质上重点还是应该放在 keeper 身上。keeper 必须时刻监控仓位是否触发强平条件，然后正确且及时的提交强平请求。合约的校验只是一个兜底，防止仓位被错误的平仓。

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/36798521/Liquidation" data-linked-resource-id="36798521" data-linked-resource-version="3" data-linked-resource-type="page">Liquidation 代码解读</a>

</div>

</div>

**强平条件：**

- remaining collateral \< min collateral USD, 剩余保证金低于阈值

- remaining collateral \<= 0，剩余保证金 ≤ 0

- remaining collateral \< `minCollateralUsdForLeverage`，最小杠杆校验

  - `minCollateralUsdForLeverage` = minCollateralFactor \* positionSizeUsd

如上，强平条件只与剩余保证金有关，因此关注剩余保证金的计算逻辑：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
remaining collateral = collateral USD + // 保证金
  position PnL USD +                    // 加上 PnL
  price impact USD -                    // 加上 price imapct fee
  collateral cost USD                   // 减去各种 cost

1. position PnL USD
long  -> position size in token * price - position size in USD
short -> position size in USD - position size in token * price

2. price impact USD
注意，price impact 在平仓时，必须 ≤ 0，因为即使平仓会带来积极影响，这些仓位也过于脆弱。
你可以理解为：仓位被 price impact fee 吊着最后一口气才不被平仓。
这种类型的仓位不应该被创建出来，因此 GMX 强行把这部分补偿取消了。

3. collateral cost USD (包含仓位费，强平费，借贷费，ui费，折扣)
position fee = position size * position fee factor
borrowing fee = ...
liquidation fee = position size * liquidation fee factor
ui fee = position size * UI fee factor
discount = ...(referral)
```

</div>

</div>

<div class="panel" style="background-color: #FFFAE6;border-width: 1px;">

<div class="panelContent" style="background-color: #FFFAE6;">

**<u>Position PnL 如何计算的？</u>**

GMX 中一个仓位有两个指标：

- sizeInUsd，代表了仓位的名义价值，USD计价。

- sizeInTokens，代表了仓位的名义价值，但用 token 计价了。

1.  **<u>PnLUsd</u>**

这样设计是为了吻合这个公式：

long profit = sizeInTokens \* tokenPrice - sizeInUsd

short profit = sizeInUsd - sizeInTokens \* tokenPrice

见这里：<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32505924/Part+1.+GMX+V2#3.-Position-Size-%2F-PnL" data-linked-resource-id="32505924" data-linked-resource-version="3" data-linked-resource-type="page">Part 1. GMX V2 基础知识</a>

那么 sizeInTokens 的 token 是哪个币？—— 是 market.indexToken，也就是追踪的资产。

这样结算的时候就可以根据追踪标的价格迅速计算 pnLUsd。

\
显然，在 increase / decrease position 的时候，仓位大小才会发生变化，前端总是会传入 sizeDelta 这个参数和 collateral token amount 来联合体现杠杆。其中 sizeDelta 其实是美元计价，会直接累积到 position.sizeInUsd 字段中，至于 sizeInTokens(delta) 则是合约根据标的资产现场计算的。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// size in usd
cache.nextPositionSizeInUsd = params.position.sizeInUsd()
  + params.order.sizeDeltaUsd();

params.position.setSizeInUsd(cache.nextPositionSizeInUsd);


// size in token(index token)
cache.baseSizeDeltaInTokens = params.order.sizeDeltaUsd() 
  / prices.indexTokenPrice.max

params.position.setSizeInTokens(params.position.sizeInTokens() 
  + cache.baseSizeDeltaInTokens);
```

</div>

</div>

2.  **<u>PnL 出金</u>**

出金的时候（减仓或者强平导致的减仓），pnl 本身的 token 是固定的，多仓走 long token，反之亦然：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
cache.pnlToken = params.position.isLong() ?
  params.market.longToken : params.market.shortToken;

// 保证金部分是一个 token
values.output.outputToken = params.position.collateralToken();

// pnl 部分又是另一个 token
values.output.secondaryOutputToken = cache.pnlToken;

// 如果保证金和 pnl token 一致，则统一用 outputToken 计算，不需要 secondary 了
```

</div>

</div>

这也就是为什么，<u>强平减仓出金的时候，可能收到2个token</u>，一部分是保证金，一部分是 pnl。

当然减仓可以进行一系列 swap 来统一出金，具体见 <a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/40697884/Decrease+Position" data-linked-resource-id="40697884" data-linked-resource-version="2" data-linked-resource-type="page">Decrease Position 代码解读</a>

</div>

</div>

------------------------------------------------------------------------

### 2.2 Approximate Liquidation Price 预估强平价

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
基本公式：
C_usd + PnL_usd - f < m

- C_usd: 保证金 usd
- Pnl_usd: 盈亏 usd
- f: 手续费
- m: 配置的最小值

C_usd 很好计算，这里不赘述
PnL_usd 以做多为例，算法是 pos_size_in_tokens * (p_after-p_now)
f 和 m 走配置
综上，需要计算出 pos_size_in_tokens 就可以通过不等式计算出 p_after。
```

</div>

</div>

------------------------------------------------------------------------

### 2.3 ADL Auto Deleveraging 自动去杠杆

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的**：ADL 本质上就是帮用户自动平仓，但是目的不是强平，而是止盈。

**根源：**GMX 的市场有两种类型，<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32505924/Part+1.+GMX+V2#2.-Markets" data-linked-resource-id="32505924" data-linked-resource-version="3" data-linked-resource-type="page">Part 1. GMX V2 基础知识</a>

其中 Fully Backed Market，无论价格如何波动，池子内的币总能支付用户盈利，而 Synthetic Market 中，锚定的币与 long token 不同，因此当锚定的币大幅上涨，而 long token 价格没有跟上时，池子由于没有对冲属性，可能会导致多头的盈利无法用 long token 支付。

此时，需要引入 ADL，在情况变的糟糕之前，提前帮用户止盈，保证盈利可以支付，把损失从事实转换为机会成本。

**For 研发：**<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/37388297/ADL" data-linked-resource-id="37388297" data-linked-resource-version="2" data-linked-resource-type="page">ADL 代码解读</a>

</div>

</div>

**例子：**

- 资金池构成：1000 ETH（主要为多头提供支持）和100万USDC（主要为空头提供支持）。

- 未平仓合约限额：假设在开仓时，DOGE多头的最大未平仓合约价值上限相当于300 ETH。

- 场景：假设有一个市场事件导致DOGE的价格上涨了10倍。同一时期，为这些DOGE多头头寸提供支持的资产ETH的价格仅上涨了2倍。

- 问题：欠DOGE多头交易者的利润负债是根据DOGE价格上涨10倍来计算的。然而，资金池中用于支付这些多头的ETH仅升值了2倍。这种差异意味着支付DOGE多头利润所需的价值超过了用于支持他们的ETH的当前价值，这可能会造成资金缺口，并威胁到资金池的偿付能力。

------------------------------------------------------------------------

### 2.4 Insolvent Closing 破产强平

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**目的：**强行清理破产仓位，绕过部分检查。

**例子：**由于各种原因，例如 keeper 宕机，市场踩踏，黑天鹅事件等，一个仓位可能会在「来得及」清算之前就破产。此时，正常的减仓/强平订单，是无法被执行的，合约认为仓位剩余的保证金不足以支付执行费等各种费用，从而拒绝平仓。

</div>

</div>

这里主要偏技术一些，GMX 合约通过这个逻辑判断 keeper 发起的强平请求是否是破产强平：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
collateralCache.isInsolventCloseAllowed =
        params.order.sizeDeltaUsd() == params.position.sizeInUsd() &&
        (
            Order.isLiquidationOrder(params.order.orderType()) ||
            params.secondaryOrderType == Order.SecondaryOrderType.Adl
        );
```

</div>

</div>

> - 订单的 `sizeDeltaUsd` 字段必须和仓位的 `sizeInUsd` 完全相等
>
> - 订单类型必须是「强平 Liquidation」或者是「ADL」

达成以上条件后，GMX 在还有部分 cost 无法被收取的情况下，会放行这个请求:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
if (!collateralCache.isInsolventCloseAllowed) {
    revert Errors.InsufficientFundsToPayForCosts(collateralCache.result.remainingCostUsd, step);
}
```

</div>

</div>

------------------------------------------------------------------------

## 3. Liquidity 流动性

### 3.1 GM Pool

#### 3.1.1 GM Token Price

<a href="https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=37584911&amp;draftShareId=0fc91fc5-d104-4cb2-af04-4bf6fcc55f33&amp;atlOrigin=eyJpIjoiYTI3NzAzMGU4MTZiNGMzZmJlMmIwY2UyZDcwZGM0YTkiLCJwIjoiYyJ9" data-card-appearance="inline" data-local-id="fcb2e696-4a7a-4e22-8129-6b5d56aa1438" rel="nofollow">https://hertzflow.atlassian.net/wiki/pages/resumedraft.action?draftId=37584911&amp;draftShareId=0fc91fc5-d104-4cb2-af04-4bf6fcc55f33&amp;atlOrigin=eyJpIjoiYTI3NzAzMGU4MTZiNGMzZmJlMmIwY2UyZDcwZGM0YTkiLCJwIjoiYyJ9</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
LP token price = pool value USD / market token total supply

pool value USD = USD values of long
  + USD values of short
  + pending borrowing fees
  - pnl
  - position impact pool
  + lent impact
```

</div>

</div>

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**Pool Value 算法**

前面几行比较好理解——

- 计算池子中 long / short token usd 价值

- 加上应收的 borrow fee

- 减去未实现盈亏

<u>复杂点在于 impact 部分逻辑：</u>

具体来说，swap impact 是独立于 pool amount 的，资金不冲突。

但是 position impact 和 pool amount 是重合的，比如池子收取了 User 100\$ 开仓导致的 impact 费，那么 pool amount 和 position impact pool amount 会同时增加 100\$。

这个看似矛盾的记账在上面这个算法被处理：pool value 要减去 position impact pool amount——于是实现了逻辑上的「收取的 100\$ 在折算 pool value 的时候其实不参与计算」。

举个例子：

pool amount = 1000\$, position impact pool amount = 0\$

此时收取了 100\$ impact fee

账面展示为：pool amount = 1100\$, position impact pool amount = 100\$。

但是在计算 pool value 的时候，会减去 position impact pool amount，因此 pool value 还是 1000\$，实现了逻辑上的自洽。也就是收的 impact fee 其实不影响池子的 value，还是独立的存放了。

**为什么要这么做？**

GMX 官方文档解释如下：

- Due to the difference in positive and negative position price impact, there can be a build up of virtual token amounts in the position impact pool which would affect the pricing of market tokens, the position impact pool should be gradually distributed if needed

大意应该是说 impact fee 实时计入的话会影响 market token 价格。他们希望能够平缓的分发，避免手续费抬高 pool 价格（也许是说，deposit 操作迅速抬升 pool 是符合预期的，但是被某种费用猛然抬高 pool 则不是）。

然后 GMX 在每个重要的合约接口上，比如订单执行层面，都会调用一次 distribute 方法去分发这部分费用，分发的算法为：按照时间费率\*duration 去扣掉 position impact pool 的账面余额。

举个例子：

还是上面的 pool amount = 1100\$, impact amount = 100\$，随着时间的流逝，impact amount 会逐渐变成0，然后 pool amount 不变，最终收敛到 pool amount = 1100\$, impact amount = 0\$。

在这个过程中，pool value 的价格是缓慢抬升的（pool value - impact 越来越大）。

\
最后一步：+lent amount，这个字段见下方的 <a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#3.1.4-Withdraw-%2F-burn" data-card-appearance="inline" data-local-id="9c8fb523-9956-409b-bde5-08f82a72de32" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#3.1.4-Withdraw-%2F-burn</a> 的 validate lendable 章节。加回来的含义应当是不希望 rebate 影响了 pool value：正向激励也许会让池子略微亏损（负向扣费的 impact 不足以激励用户时，池子会自己贴钱），然后 GMX 在这里加回来应该是为了避免这部分 diff。

</div>

</div>

------------------------------------------------------------------------

#### 3.1.2 Fees

- Deposit Fees

  - Execution fee

  - Deposit fee

  - UI fee

  - Price impact

- Withdraw Fees

  - Execution Fee

  - Withdraw fee

  - UI fee

可以看到，price impact 费只在 deposit 的时候收取，withdraw 的时候不会收取。

------------------------------------------------------------------------

#### <span class="inline-comment-marker" ref="f00b590b-1915-4981-8d87-f04428e3be7a">3.1.3 Deposit / Mint</span>

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/37584939/Deposit" data-linked-resource-id="37584939" data-linked-resource-version="2" data-linked-resource-type="page">Deposit 代码解读</a>

这里产品层面只需要关注 GM Token 的 price 算法是 pool value / supply 即可。

再使用入金 USD 价值除以上面的 price，就得到了 mint amount。

**<u>Token Flow:</u>**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="739a892b4eb87561224bffd6ef7c91c296ffd42be95fce25f3f873ac88a70c8e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571463/image-20251121-070728.png?version=1&amp;modificationDate=1763708855711&amp;cacheVersion=1&amp;api=v2" data-height="642" data-width="1006" data-unresolved-comment-count="0" data-linked-resource-id="41582638" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251121-070728.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571463" data-linked-resource-container-version="48" data-media-id="f538d85f-f39a-443f-9547-d920ee030af5" data-media-type="file" width="468" height="298" alt="image-20251121-070728.png" /></span>

> 1.  用户创建 deposit 请求，资金会存入 Deposit Vault
>
> 2.  keeper 执行 deposit 请求，资金从 Deposit Vault 转移到 Market。token transfer 之后，逻辑上进行拆分—— impact 部分不计入 pool amount。
>
> **<span style="background-color: rgb(253,208,236);"><u>注</u></span>**：price impact 为正，激励用户时，以相反的 token 进行激励。比如 ETH / USDC pool，deposit ETH 时，如果带来了正反馈，计算出 positive impact usd 之后，用 USDC 激励它，也就是说会从 short swap impact pool 中划转一部分 USDC 出来，丢到 short token pool 里面去。
>
> 反之，如果是 negative impact，则相当于从用户的 ETH 中扣除一部分，进入 long token pool 的流动性变少，但是扣除的部分 ETH 会丢到 long swap impact pool 里面去。
>
> Market 锁定的 token 是统一的，通过逻辑隔离，用 token pool 来展示真实的流动性。也就是说池子的流动性一定 ≤ 池子锁定的 token 数量。

**<u>validate Max PnL</u>**

注意，deposit 本身还会收到池子当前的 PnL 限制，当池子目前的 PnL 过高的时候，GMX 会拒绝你继续添加流动性。

- <u>原因</u>：lp_token_price = pool_value / lp_supply， ~~这里 pool_value 不包含 unrealized PnL，只是 token 市值。因此，当池子 PnL 过高的时候，pool_value 实际上处于虚高的状态，很快当用户平仓 take profit 之后，pool_value 就会下跌，导致 LP Token Price 下跌~~。这里 pool value 包含了 PnL 计算，因此当 PnL 太高的时候，GM Token 价格实际上很低，GMX 为了保护 LP，避免了用户在市场不健康的时候继续添加流动性带来不必要的损失。（换句话来说，针对 deposit 操作，GMX 保护你只有在 GM Token 值钱的时候添加流动性，这个限制仅仅存在于 deposit，真正的 GM Token 价格是市场决定的，GMX并不干预）。

- <u>算法</u>：pnl_usd / pool_value_usd \> maxPnLFactor 时触发拒绝。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function isPnlFactorExceeded(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices,
    bool isLong,
    bytes32 pnlFactorType
) internal view returns (bool, int256, uint256) {
    int256 pnlToPoolFactor = getPnlToPoolFactor(dataStore, market, prices, isLong, true);
    uint256 maxPnlFactor = getMaxPnlFactor(dataStore, pnlFactorType, market.marketToken, isLong);

    bool isExceeded = pnlToPoolFactor > 0 && pnlToPoolFactor.toUint256() > maxPnlFactor;

    return (isExceeded, pnlToPoolFactor, maxPnlFactor);
}
```

</div>

</div>

- <u>配置项</u>：long short token 都校验，复用同一个比例 factor：MAX_PNL_FACTOR_FOR_DEPOSITS

**<u>validate pool amount</u>**

参照开头的 Token Flow 章节的注解，可以发现，price impact 机制会以相反的 token 激励用户，从而给池子带来额外的资产。

考虑此时 ETH-USDC pool 中，USDC 的 deposit amount 已经达到阈值，而 ETH 非常短缺。此时 deposit ETH 会带来 positive impact，于是池子以 USDC impact 进行奖励，最终入金除了 ETH 之外，还会有一部分 USDC 入金（从而给用户 mint 更多 GM Tokens），这里会报错（因为 USDC 早就满了）。

这个校验解决了上述场景的问题。

校验逻辑：「校验相反方向 token amount 是否超出阈值」

配置项：HASH(MAX_POOL_AMOUNT, market, token)

当然，还会校验本方向 token amount 是否超出阈值。

**<u>validate max pool usd</u>**

这里和 pool amount 概念类似，但是转向 USD 计价再次限制一遍。

校验逻辑：「校验 pool USD 是否超出阈值」

配置项：HASH(MAX_POOL_USD_FOR_DEPOSIT, market, token)

**<u>validate market balance</u>**

校验池子中锁定的 balance，足以支付一切费用。

注意，这里的维度是池子合约中锁定的所有 token 的 balance，前面的所有校验都是池子中锁定 token 的一部分，都是逻辑上的概念。Market 合约锁定的 USDC 包含了 swap impact, short token amount, claimable funding fee, claimable ui fee, collateral sum 等。

校验逻辑：

- 校验 expectedMinBalance：

  - token balance ≥ cache.poolAmount\
    + cache.swapImpactPoolAmount (略)\
    + cache.claimableCollateralAmount (减仓的时候 price impact 有个最大limit，超出limit的部分还是会收钱，但是不入池子，而是给到 claimable 里面去)\
    + cache.claimableFeeAmount (borrow,liq fee按比例瓜分一部分给receiver了)\
    + cache.claimableUiFeeAmount (略)\
    + cache.affiliateRewardAmount (referral 相关的费用)

- 校验 collateralSum:

  - token balance \> collateralSum 保证金在加减仓的时候单独记录，不入池子 pool amount 中。

- 校验 claimable funding fee amount:

  - token balance \> claimable funding fee，加减仓的时候触发收费，逻辑隔离，不计入 pool amount。

------------------------------------------------------------------------

#### 3.1.4 Withdraw / burn

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/38764551/Withdraw" data-linked-resource-id="38764551" data-linked-resource-version="2" data-linked-resource-type="page">Withdraw 代码解读</a>

**<u>validate reserve</u>**

GMX 合约会校验 Withdraw 之后，池子剩余的 token，是否足够健康。其中一个标准是查看 reserved Usd 是否超出阈值：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function validateReserve(
        DataStore dataStore,
        Market.Props memory market,
        MarketPrices memory prices,
        bool isLong
    ) internal view {
        // poolUsd is used instead of pool amount as the indexToken may not match the longToken
        // additionally, the shortToken may not be a stablecoin
        uint256 poolUsd = getPoolUsdWithoutPnl(dataStore, market, prices, isLong, false);
        uint256 reserveFactor = getReserveFactor(dataStore, market.marketToken, isLong);
        uint256 maxReservedUsd = Precision.applyFactor(poolUsd, reserveFactor);

        uint256 reservedUsd = getReservedUsd(
            dataStore,
            market,
            prices,
            isLong
        );

        if (reservedUsd > maxReservedUsd) {
            revert Errors.InsufficientReserve(reservedUsd, maxReservedUsd);
        }
    }
```

</div>

</div>

这个逻辑很简单，reservedUsd 其实就是 OI，通过查看 OI 是否 \> pool_value \* reserveFactor 判断是否超出阈值。reserveFactor 配置 key = HASH(RESERVE_FACTOR, market, is_long)。

**<u>validate lendable</u>**

这里和 price impact 相关，具体来说，price impact 结算本身其实是直接从 pool 里面拿钱。

但是 GMX 维护了一个负债表，其中一个叫做 price impact pool，记为余额池；另一个叫做 lent price impact pool，记为负债池，池中单位是 index token。

支付 price impact 时，先从余额扣（注意只是逻辑记账），不够了就去增加负债。这里只是记账，钱是一定会从 pool 本身出的，会支付 long / short token。

记账本身用于一些池子的校验，比如这里。

校验逻辑：lent usd \> pool_value_usd \* factor 则报错。factor key = HASH( RESERVE_FACTOR, market, isLong)

**<u>validate Max PnL</u>**

同 deposit 里面的 validate。逻辑一样，但是 factor 不一样: MAX_PNL_FACTOR_FOR_WITHDRAWALS。

**<u>validate market balance</u>**

同 deposit 里面的 validate。

------------------------------------------------------------------------

#### 3.1.5 Shift

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/38764614/Shift" data-linked-resource-id="38764614" data-linked-resource-version="2" data-linked-resource-type="page">Shift 代码解读</a>

Shift 只是对 Withdraw From Market A && Deposit to Market B 的一个封装，产品层面上减免了 swap fee。

------------------------------------------------------------------------

### 3.2 GLV

#### 3.2.1 GLV Token Price

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/38764673/GLV+Token+Price" data-linked-resource-id="38764673" data-linked-resource-version="1" data-linked-resource-type="page">GLV Token Price 代码解读</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GLV token price = GLV pool value / GLV total supply
GLV pool value = sum(USD value of GM tokens owned by GLV)
```

</div>

</div>

------------------------------------------------------------------------

#### 3.2.2 GLV Fees

GLV 的手续费没有额外抽象，就是底层去某个具体 market 做 deposit withdraw 操作时，market 收取的费用。

------------------------------------------------------------------------

#### 3.2.3 GLV Deposit Mint

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/38076565/GLV+Deposit+Mint" data-linked-resource-id="38076565" data-linked-resource-version="2" data-linked-resource-type="page">GLV Deposit Mint 代码解读</a>

GLV 投资分为两种：用原始币（WETH，USDC）或者用 GM Tokens。

GLV 本身只持有 Market Tokens，因此如果你用 USDC 等非 GM Token 投资，他会帮你去底层 market 做一次 deposit 拿到对应市场的 market token，然后再转给 GLV。

------------------------------------------------------------------------

#### 3.2.4 GLV Withdraw Burn

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/39157794/GLV+Withdraw+Burn" data-linked-resource-id="39157794" data-linked-resource-version="2" data-linked-resource-type="page">GLV Withdraw Burn 代码解读</a>

Withdraw 的流程，就是：

1.  归还 GLV Token 给到 GLV

2.  GLV 归还 Market Token 给到 Market（用户指定）

3.  走一次正常的普通 Market Withdraw 流程，把 Market Token Burn 得到的原始币给回用户。

------------------------------------------------------------------------

#### 3.2.5 GLV Shift

<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/39190549/GLV+Shift" data-linked-resource-id="39190549" data-linked-resource-version="2" data-linked-resource-type="page">GLV Shift 代码解读</a>

这里主要是 keeper 执行，官方通过一系列未公开的算法，决定是否要改变 GLV 对各大 Market 的持仓比例。如果决定了，就交给 keeper 去执行，底层和 GM Pools 的 Shift 一致，只是 Holder 从 User 变为了 GLV。

</div>
