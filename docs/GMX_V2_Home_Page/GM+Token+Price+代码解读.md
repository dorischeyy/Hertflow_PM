# GM Token Price 代码解读

<div class="Section1">

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L135-L165" class="external-link" rel="nofollow">MarketUtils.getMarketTokenPrice</a>

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L2602-L2621" class="external-link" rel="nofollow">MarketUtils.usdToMarketTokenAmount</a>

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L274-L370" class="external-link" rel="nofollow">MarketUtils.getPoolValueInfo</a>

具体的 price 算法：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
int256 marketTokenPrice = Precision.mulDiv(Precision.WEI_PRECISION, poolValueInfo.poolValue, supply);
```

</div>

</div>

这里可以看出，GM Token 的精度是 WEI，也就是18位。

pool value 的一些小细节：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
result.borrowingFeePoolFactor = Precision.FLOAT_PRECISION - dataStore.getUint(Keys.BORROWING_FEE_RECEIVER_FACTOR);
result.poolValue += Precision.applyFactor(result.totalBorrowingFees, result.borrowingFeePoolFactor).toInt256();
```

</div>

</div>

这里不难看出，计算的时候比较精密，borrow fee 有一部分被保留瓜分走了，这里也会减去。

</div>
