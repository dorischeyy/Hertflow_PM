# Increase Position 代码解读

<div class="Section1">

## Create Increase Order

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExchangeRouter.multicall
├ ExchangeRouter.sendWnt
├ ExchangeRouter.sendTokens
└ ExchangeRouter.createOrder
   └ OrderHandler.createOrder
      └ OrderUtils.createOrder
         ├ OrderVault.recordTransferIn
         ├ OrderVault.recordTransferIn
         └ OrderStoreUtils.set
```

</div>

</div>

## Execute Increase Order

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
OrderHandler.executeOrder
├─ OracleModule.withOraclePrices
│  └─ Oracle.setPrices
├─ OrderStoreUtils.get
├─ _executeOrder
│  └─ ExecuteOrderUtils.executeOrder
│     ├─ OrderStoreUtils.remove
│     ├─ MarketUtils.getMarketPrices
│     ├─ MarketUtils.distributePositionImpactPool
│     ├─ PositionUtils.updateFundingAndBorrowingState
│     ├─ processOrder
│     │  └─ IncreaseOrderUtils.processOrder
│     │     ├─ SwapUtils.swap
│     │     ├─ PositionStoreUtils.get
│     │     └─ IncreasePositionUtils.increasePosition
│     │        ├─ processCollateral
│     │        │  ├─ PositionPricingUtils.getPositionFees
│     │        │  ├─ MarketUtils.applyDeltaToCollateralSum // coll-fees
│     │        │  └─ MarketUtils.applyDeltaToPoolAmount    // fees
│     │        ├─ MarketUtils.updateTotalBorrowing
│     │        ├─ PositionStoreUtils.set
│     │        ├─ PositionUtils.updateOpenInterest
│     │        ├─ MarketUtils.validateReserve              // 这里校验 market cap
│     │        ├─ MarketUtils.validateOpenInterestReserve  // 同上
│     │        └─ PositionUtils.validatePosition           // 兜底校验 coll 和 liquidatable
│     └─ GasUtils.payExecutionFee
└─ OracleModule.withOraclePrices
   └─ Oracle.clearAllPrices
```

</div>

</div>

</div>
