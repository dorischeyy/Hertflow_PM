# Position Fees 代码解读

<div class="Section1">

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/pricing/PositionPricingUtils.sol#L316-L397" class="external-link" rel="nofollow">PositionPricingUtils.getPositionFees</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 给到池子的费用
fees.feeAmountForPool =
    fees.positionFeeAmountForPool +
    fees.borrowing.borrowingFeeAmount -
    fees.borrowing.borrowingFeeAmountForFeeReceiver +
    fees.liquidation.liquidationFeeAmount -
    fees.liquidation.liquidationFeeAmountForFeeReceiver;

// 抽水
fees.feeReceiverAmount +=
    fees.borrowing.borrowingFeeAmountForFeeReceiver +
    fees.liquidation.liquidationFeeAmountForFeeReceiver;

// 资金费给对手方
fees.funding = getFundingFees(
    fees.funding,
    params.position
);

// ui 费给提供商
fees.ui = getUiFees(
    params.dataStore,
    params.collateralTokenPrice,
    params.sizeDeltaUsd,
    params.uiFeeReceiver
);
```

</div>

</div>

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**xxxForReceiver:**

GMX 中抽水的部分的算法比较简单，就是自定义一个factor作为抽水比例，直接乘以原始 fee 即可。

</div>

</div>

</div>
