# Liquidation 代码解读

<div class="Section1">

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
LiquidationHandler.executeLiquidation
├─ LiquidationUtils.createLiquidationOrder
│  ├─ PositionStoreUtils.get
│  └─ OrderStoreUtils.set
└─ ExecuteOrderUtils.executeOrder
   ├─ OrderStoreUtils.remove
   └─ processOrder
      └─ DecreaseOrderUtils.processOrder
         ├─ PositionStoreUtils.get
         ├─ DecreasePositionUtils.decreasePosition
         │  ├─ PositionUtils.isPositionLiquidatable
         │  └─ DecreasePositionCollateralUtils.processCollateral
         └─ MarketToken.transferOut
```

</div>

</div>

涉及到减仓:<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/40697884/Decrease+Position?atlOrigin=eyJpIjoiMTRmMzYxMzk1ODMwNGMwMjg4MTkyOTRlMDI3MjY1OTMiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/40697884/Decrease+Position?atlOrigin=eyJpIjoiMTRmMzYxMzk1ODMwNGMwMjg4MTkyOTRlMDI3MjY1OTMiLCJwIjoiYyJ9</a> 。

关注一下强平条件的代码实现：<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/position/PositionUtils.sol#L307C5-L439C6" class="external-link" rel="nofollow">PositionUtils.isPositionLiquidatable</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
remaining collateral = collateral USD + // 保证金
  position PnL USD +                    // 加上 PnL
  price impact USD -                    // 加上 price imapct fee
  collateral cost USD                   // 减去各种 cost
和业务文档描述的一致。
```

</div>

</div>

</div>
