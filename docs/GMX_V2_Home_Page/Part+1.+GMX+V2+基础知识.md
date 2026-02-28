# Part 1. GMX V2 基础知识

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270756468 {padding: 0px;}
div.rbtoc1772270756468 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270756468 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270756468">

<style>[data-colorid=e3dy0ddu7n]{color:#6554c0} html[data-color-mode=dark] [data-colorid=e3dy0ddu7n]{color:#503fab}[data-colorid=mnyvi7qsgb]{color:#ff5630} html[data-color-mode=dark] [data-colorid=mnyvi7qsgb]{color:#cf2600}[data-colorid=oeje7crxpd]{color:#6554c0} html[data-color-mode=dark] [data-colorid=oeje7crxpd]{color:#503fab}[data-colorid=wd8hxy8pcq]{color:#36b37e} html[data-color-mode=dark] [data-colorid=wd8hxy8pcq]{color:#4cc994}[data-colorid=oly5hr3q1s]{color:#36b37e} html[data-color-mode=dark] [data-colorid=oly5hr3q1s]{color:#4cc994}[data-colorid=glrez6xb2l]{color:#36b37e} html[data-color-mode=dark] [data-colorid=glrez6xb2l]{color:#4cc994}[data-colorid=be4skk5drt]{color:#ff5630} html[data-color-mode=dark] [data-colorid=be4skk5drt]{color:#cf2600}[data-colorid=my5vx7x4e0]{color:#ff5630} html[data-color-mode=dark] [data-colorid=my5vx7x4e0]{color:#cf2600}[data-colorid=tz5gshlnv6]{color:#36b37e} html[data-color-mode=dark] [data-colorid=tz5gshlnv6]{color:#4cc994}[data-colorid=wdt1jez8lr]{color:#6554c0} html[data-color-mode=dark] [data-colorid=wdt1jez8lr]{color:#503fab}[data-colorid=f4h5rqiw64]{color:#ff5630} html[data-color-mode=dark] [data-colorid=f4h5rqiw64]{color:#cf2600}[data-colorid=vm8ngse2qy]{color:#ff5630} html[data-color-mode=dark] [data-colorid=vm8ngse2qy]{color:#cf2600}[data-colorid=jk26nicpee]{color:#36b37e} html[data-color-mode=dark] [data-colorid=jk26nicpee]{color:#4cc994}[data-colorid=bhj18cr6k5]{color:#ff5630} html[data-color-mode=dark] [data-colorid=bhj18cr6k5]{color:#cf2600}[data-colorid=gmj423qyif]{color:#ff5630} html[data-color-mode=dark] [data-colorid=gmj423qyif]{color:#cf2600}[data-colorid=xougap89iw]{color:#6554c0} html[data-color-mode=dark] [data-colorid=xougap89iw]{color:#503fab}[data-colorid=wk8z6l57yn]{color:#6554c0} html[data-color-mode=dark] [data-colorid=wk8z6l57yn]{color:#503fab}[data-colorid=o3qe9ls88u]{color:#ff5630} html[data-color-mode=dark] [data-colorid=o3qe9ls88u]{color:#cf2600}[data-colorid=p3am5lf35d]{color:#36b37e} html[data-color-mode=dark] [data-colorid=p3am5lf35d]{color:#4cc994}[data-colorid=he63ltwiju]{color:#ff5630} html[data-color-mode=dark] [data-colorid=he63ltwiju]{color:#cf2600}[data-colorid=f9wjhvl8wi]{color:#6554c0} html[data-color-mode=dark] [data-colorid=f9wjhvl8wi]{color:#503fab}[data-colorid=p1of71jvmz]{color:#36b37e} html[data-color-mode=dark] [data-colorid=p1of71jvmz]{color:#4cc994}[data-colorid=jnhr8tl3lr]{color:#36b37e} html[data-color-mode=dark] [data-colorid=jnhr8tl3lr]{color:#4cc994}[data-colorid=kmr848jdfx]{color:#ff5630} html[data-color-mode=dark] [data-colorid=kmr848jdfx]{color:#cf2600}[data-colorid=aj3ye8lj1z]{color:#ff5630} html[data-color-mode=dark] [data-colorid=aj3ye8lj1z]{color:#cf2600}[data-colorid=nid4nce3hd]{color:#36b37e} html[data-color-mode=dark] [data-colorid=nid4nce3hd]{color:#4cc994}[data-colorid=ygrtbh357q]{color:#36b37e} html[data-color-mode=dark] [data-colorid=ygrtbh357q]{color:#4cc994}[data-colorid=p1ddmrfjxd]{color:#ff5630} html[data-color-mode=dark] [data-colorid=p1ddmrfjxd]{color:#cf2600}[data-colorid=vc9mlyl159]{color:#ff5630} html[data-color-mode=dark] [data-colorid=vc9mlyl159]{color:#cf2600}[data-colorid=sbctfbb2ax]{color:#ff5630} html[data-color-mode=dark] [data-colorid=sbctfbb2ax]{color:#cf2600}</style>

- [1. GMX V2 如何工作](#Part1.GMXV2基础知识-1.GMXV2如何工作)
- [2. Markets](#Part1.GMXV2基础知识-2.Markets)
- [3. Position Size / PnL](#Part1.GMXV2基础知识-3.PositionSize/PnL)
- [4. Liquidation](#Part1.GMXV2基础知识-4.Liquidation)
- [5. Open Interest (OI)](#Part1.GMXV2基础知识-5.OpenInterest(OI))
- [6. Funding Fee](#Part1.GMXV2基础知识-6.FundingFee)

</div>

## 1. GMX V2 如何工作

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ede2b1d2d3efa112355ae8c8c50eef1653cbc704e7436d931b3df8357cd4eb40" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32505924/image-20251104-080525.png?version=1&amp;modificationDate=1762328105405&amp;cacheVersion=1&amp;api=v2" data-height="1295" data-width="1947" data-unresolved-comment-count="0" data-linked-resource-id="32538697" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251104-080525.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32505924" data-linked-resource-container-version="3" data-media-id="3f5b7b51-dc1a-423a-8a51-75a56e3fa5ea" data-media-type="file" width="468" height="311" alt="image-20251104-080525.png" /></span>

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

GMX V2 主要由四个角色构成，类似 V1：

1.  GMX 合约本身，负责逻辑的实现。

2.  LP，质押资产提供流动性给合约。

3.  Trader，在合约中进行交易，依赖 LP 提供的流动性。

4.  Keeper，链下部署，负责监听 Trader 提交的开仓请求进行执行，以及在合适时机强平其仓位。

</div>

</div>

------------------------------------------------------------------------

## 2. Markets

GMX V2 的资金池（LP Pool）进行了拆分，在 V1 中是一<span class="inline-comment-marker" ref="703f99dd-5603-4c60-abdb-092b69628794">篮子</span>资产，在 V2 中被拆成了两两一对 —— 被称之为 Market。

- Market 定义：

<div class="table-wrap">

|  |  |
|----|----|
| <span colorid="f9wjhvl8wi">Index</span> | Crypto to bet on the price / 追踪的资产价格 |
| <span colorid="my5vx7x4e0">Long</span> <span colorid="sbctfbb2ax">Token</span> | Token paid out to long profit / 多仓获利的出金 |
| <span colorid="ygrtbh357q">Short</span> <span colorid="nid4nce3hd">Token</span> | Token paid out to short profit / 空仓获利的出金 |

</div>

Examples:

<div class="table-wrap">

|  |  |  |
|----|----|----|
| <span colorid="oeje7crxpd">Index</span> | ETH | bet on price of ETH / 追踪 ETH 价格 |
| <span colorid="mnyvi7qsgb">Long Token</span> | WETH | long profit paid in WETH / 多仓获利用 WETH 结算 |
| <span colorid="p1of71jvmz">Short Token</span> | USDC | short profit paid in USDC / 空仓获利用 USDC 结算 |

</div>

- 两种类型的 Market

  - <u>Full Backed</u>: <span colorid="wdt1jez8lr">index</span> ≈ <span colorid="o3qe9ls88u">long token</span> && <span colorid="jk26nicpee">short token</span> == stable coin

  - <u>Synthetic</u>: <span colorid="wk8z6l57yn">index</span> ≠ <span colorid="vm8ngse2qy">long token（两者价格几乎不相关）</span>

Examples:

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="356d8dfe-209b-4b4b-b189-aa8094fc1c66">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>Full Backed Market</p></td>
<td class="confluenceTd"><p>Index = ETH</p>
<p>Long = WETH</p>
<p>Short = USDC</p></td>
<td class="confluenceTd"><ul>
<li><p>假设 <span data-colorid="e3dy0ddu7n">1 ETH = 2000$</span></p></li>
<li><p>Market 持有 <span data-colorid="bhj18cr6k5">100 WETH</span> &amp;&amp; <span data-colorid="oly5hr3q1s">200,000 USDC</span></p></li>
<li><p>其中 <span data-colorid="be4skk5drt">90 WETH</span> 正在被用于<span data-colorid="aj3ye8lj1z">做多，</span><span data-colorid="glrez6xb2l">180,000 USDC</span> 正在被用于<span data-colorid="jnhr8tl3lr">做空</span></p></li>
</ul>
<p>A. 假设 ETH 价格 x10 上涨</p>
<p>此时 long profit ≤ 90 WETH ≤ 100 WETH（Market 有能力支付）</p>
<p>B. 假设 ETH 价格归 0</p>
<p>此时 short profit ≤ 180,000 USDC ≤ 200,000 USDC（Market 有能力支付）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Synthetic Market</p></td>
<td class="confluenceTd"><p>Index = DOGE</p>
<p>Long = WETH</p>
<p>Short = USDC</p></td>
<td class="confluenceTd"><ul>
<li><p>假设 <span data-colorid="xougap89iw">1 DOGE = 0.5$ </span><br />
<span data-colorid="kmr848jdfx">1 WETH = 2000$</span></p></li>
<li><p>Market 持有 <span data-colorid="f4h5rqiw64">100 WETH</span> &amp;&amp; <span data-colorid="tz5gshlnv6">200,000 USDC</span></p></li>
<li><p>其中有 <span data-colorid="gmj423qyif">360,000 DOGE</span> 价值的<span data-colorid="he63ltwiju">多仓，</span><span data-colorid="wd8hxy8pcq">180,000 USDC</span> 正在被用于<span data-colorid="p3am5lf35d">空仓</span></p></li>
</ul>
<p>极端情况：假设 DOGE 价格 x10 上涨，而 WETH 价格完全不变</p>
<p>此时 long profit ≤ 360,000 DOGE ≤ 360,000 * 5 = <span data-colorid="vc9mlyl159">1,800,000</span>$</p>
<p>而同时 Market 中 Long Token WETH 的价值为 100 * 2000$ = <span data-colorid="p1ddmrfjxd">200,000</span>$</p>
<p><span style="background-color: rgb(253,208,236);">于是池子无法支付多头的盈利</span></p>
<p><u>GMX 具体解法为 ADL，此处不展开。</u></p></td>
</tr>
</tbody>
</table>

</div>

------------------------------------------------------------------------

## 3. Position Size / PnL

- Position Size

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
L  = Leverage 杠杆
C0 = USD value of colleteral at entry 初始保证金的 USD 价值
I0 = Price of index at entry 初始 index 价格
I  = Current price of index 最新 index 价格

S0 = position size in USD = L*C0 (杠杆乘以保证金)
T0 = position size in token = S0/I0 (仓位 USD 价值除以 token 价格，转为 index 计价)
```

</div>

</div>

- PnL

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Long Position PnL  = T0*I - S0 (仓位token数量乘以最新价格就得到了最新仓位USD价值)
Short Position PnL = S0 - T0*I (同上，只是做空取反)
```

</div>

</div>

- Example

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
当前 ETH 2000$，投入 1000$ 加 5 倍杠杆做多/空 ETH，随后 ETH 涨到了 3000$
L = 5
C0 = 1000$
I0 = 2000$
I = 3000$

S0 = L*C0 = 5*1000$ = 5000$ (初始仓位 size 是 5000 USD)
T0 = S0/I0 = 5000/2000$ = 2.5(也可以表示为 2.5 ETH)

PnL for Long  = 2.5*3000 - 5000 = 2500$
PnL for short = 5000 - 2.5*3000 = -2500$

其实这里可以看到，计算 T0 是为了方便后续直接乘以 index token 价格去计算最新美元 PnL。
```

</div>

</div>

------------------------------------------------------------------------

## 4. Liquidation

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
collateral - loss - fees < min

collateral: 保证金
loss: 亏损
fees: 各种费
min: 合约的一个 setting
```

</div>

</div>

------------------------------------------------------------------------

## 5. Open Interest (OI)

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
OI = Position Size 累加和, 对应 1.3 中的 S0 或 T0
```

</div>

</div>

GMX 拆分了 4 种不同的 OI，因为 Market 中有 2 种 Token，还有 2 种方向，于是 2\*2 = 4。

- Long with Long Token (用 WETH 做多 ETH)

- Long with Short Token (用 USDC 做多 ETH)

- Short with Long Token (用 WETH 做空 ETH)

- Short with Short Token (用 USDC 做空 ETH)

------------------------------------------------------------------------

## 6. Funding Fee

根据 5. OI 的计算结果，如果 Long OI \> Short OI，则 long pays short，反之亦然。

</div>
