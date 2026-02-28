# Price Impact 代码解读

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270775090 {padding: 0px;}
div.rbtoc1772270775090 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270775090 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270775090">

- [1. Swap](#PriceImpact代码解读-1.Swap)
  - [1.1 swap 时 price impact fee 如何计算](#PriceImpact代码解读-1.1swap时priceimpactfee如何计算)
  - [1.2 swap 时如何处理 price impact fee](#PriceImpact代码解读-1.2swap时如何处理priceimpactfee)
- [2. Long / Short](#PriceImpact代码解读-2.Long/Short)
  - [2.1 仓位操作如何计算 price impact fee](#PriceImpact代码解读-2.1仓位操作如何计算priceimpactfee)
  - [2.2 仓位操作何时处理 price impact fee](#PriceImpact代码解读-2.2仓位操作何时处理priceimpactfee)
- [3. Deposit](#PriceImpact代码解读-3.Deposit)
  - [3.1 Deposit 时 price impact fee 如何计算](#PriceImpact代码解读-3.1Deposit时priceimpactfee如何计算)
  - [3.2 Deposit 时如何处理 price impact fee](#PriceImpact代码解读-3.2Deposit时如何处理priceimpactfee)

</div>

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**Price Impact Fee Math**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
d0 = initial imbalance USD
d1 = next imbalance USD
e = exponent factor

# Same side
f = impact factor depends on positive or negative impact
same side price impact = d0 ^ e * f - d1 ^ e * f

# Cross over
p = positive impact factor
n = negative impact factor

p <= n

cross over price impact = d0 ^ e * p - d1 ^ e * n
```

</div>

</div>

一句话总结：

多空不平衡 x 用 usd 来衡量，然后基于指数函数: f(x) = ax^n 放大不平衡之后，求差得到费用。

</div>

</div>

## 1. Swap

### 1.1 swap 时 price impact fee 如何计算

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/pricing/SwapPricingUtils.sol#L109-L166" class="external-link" rel="nofollow">SwapPricingUtils.getPriceImpactUsd</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getPriceImpactUsdForSameSideRebalance(
    uint256 initialDiffUsd,
    uint256 nextDiffUsd,
    uint256 impactFactor,
    uint256 impactExponentFactor
) internal pure returns (int256) {
    bool balanceWasImproved = nextDiffUsd < initialDiffUsd;

    // 对比这里和开头 Math 列出的公式，利用指数函数放大后求 diff 计算费用
    uint256 deltaDiffUsd = Calc.diff(
        applyImpactFactor(initialDiffUsd, impactFactor, impactExponentFactor),
        applyImpactFactor(nextDiffUsd, impactFactor, impactExponentFactor)
    );

    int256 priceImpactUsd = Calc.toSigned(deltaDiffUsd, balanceWasImproved);

    return priceImpactUsd;
}
```

</div>

</div>

### 1.2 swap 时如何处理 price impact fee

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/swap/SwapUtils.sol#L271-L337" class="external-link" rel="nofollow">SwapUtils._swap</a>

对于 positive impact，给出奖励，形式为增加部分 amount out。

对于 negative impact，给出惩罚，形式为扣除部分 amount in。

> **PS：**positive impact 是有上限的。GMX 使用 Swap Impact Pool `<Market, TokenIn/Out>` 解耦存储 price impact fee，因此给出的 Token Out 奖励无法超出这个池子的值。此时，GMX 会尝试使用 Token In 再次奖励用户。
>
> 直接奖励：amountOut += rebate
>
> tokenIn 间接奖励：
>
> 1.  amountOut += rebate0
>
> 2.  amountIn += rebate1，随后参与计算 amountOut 的时候才得到体现。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e46691d96d6fc13f031f7a24a5f7812b399853d1b87b30cd59d1ec84b66ebf7f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/35160083/image-20251110-102053.png?version=1&amp;modificationDate=1762770060544&amp;cacheVersion=1&amp;api=v2" data-height="691" data-width="879" data-unresolved-comment-count="0" data-linked-resource-id="35225630" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251110-102053.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="35160083" data-linked-resource-container-version="5" data-media-id="c27ab9da-6cfb-4940-ad1d-c25ee52c2fc5" data-media-type="file" width="468" height="367" alt="image-20251110-102053.png" /></span>

------------------------------------------------------------------------

## 2. Long / Short

### 2.1 仓位操作如何计算 price impact fee

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/pricing/PositionPricingUtils.sol#L159-L182" class="external-link" rel="nofollow">PositionPricingUtils.getPriceImpactUsd</a>

逻辑同 swap。只不过 imbalance 的计算逻辑，从 `poolAmount` 变化为了 `openInterest`。

### 2.2 仓位操作何时处理 price impact fee

- <a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/position/PositionUtils.sol#L621-L714" class="external-link" rel="nofollow">PositionUtils.getExecutionPriceForIncrease</a> 加仓

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="52f3db7e721431b054cbb57fce0f233494962fa604fb72dc0fec13fa8445d224" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/35160083/image-20251111-050141.png?version=1&amp;modificationDate=1762837315693&amp;cacheVersion=1&amp;api=v2" data-height="422" data-width="864" data-unresolved-comment-count="0" data-linked-resource-id="35913748" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251111-050141.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="35160083" data-linked-resource-container-version="5" data-media-id="587a94ff-5936-4f09-b380-9c3f2f36cfe4" data-media-type="file" width="468" height="228" alt="image-20251111-050141.png" /></span>

- <a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/position/DecreasePositionCollateralUtils.sol#L139-L173" class="external-link" rel="nofollow">DecreasePositionCollateralUtils.processCollateral (positive impact)</a>

  <a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/position/DecreasePositionCollateralUtils.sol#L379-L386" class="external-link" rel="nofollow">DecreasePositionCollateralUtils.processCollateral (negative impact)</a>

仓位的 price impact 费在 increase 时会被记录在 pending 字段中，只有在 decrease 时才会被真正从保证金扣除。与此同时，price impact 还引入了 distribute 的功能，把一部分费用分发到一个特定池子中供提取。

------------------------------------------------------------------------

## 3. Deposit

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/deposit/ExecuteDepositUtils.sol#L399-L486" class="external-link" rel="nofollow">ExecuteDepositUtils.executeDeposit</a>

### 3.1 Deposit 时 price impact fee 如何计算

同 swap，复用 swap 相同的函数计算的 imbalance 以及 price impact usd。

### 3.2 Deposit 时如何处理 price impact fee

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/deposit/ExecuteDepositUtils.sol#L399-L486" class="external-link" rel="nofollow">ExecuteDepositUtils._executeDeposit</a>

rebate → mint more

penalty → less token in

值得一提的是，由于前面讲过 GMX 使用单独的 price impact pool 保存罚金，因此有正向的奖励时，奖励金从 price impact pool 取出后，也会影响到 deposit pool 的 amount（可以理解为从两个地方 deposit 了），这里不单单只影响 mint amount。

</div>
