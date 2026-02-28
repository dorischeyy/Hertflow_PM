# Shift 代码解读

<div class="Section1">

## Create Shift

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/router/ExchangeRouter.sol#L219C1-L229C6" class="external-link" rel="nofollow">ExchangeRouter.createShift</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1. Send GM token to shift vault
2. Send execution fee to shift vault
3. Create shift order

ExchangeRouter.createShift
└ ShiftHandler.createShift
    └ ShiftUtils.createShift
        ├ ShiftVault.recordTransferIn
        ├ ShiftVault.recordTransferIn
        └ ShiftStoreUtils.set
```

</div>

</div>

## Execute Shift

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/ShiftHandler.sol#L85C5-L113C6" class="external-link" rel="nofollow">ShiftHandler.ExecuteShift</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ShiftHandler.executeShift
├ ShiftStoreUtils.get
└ _executeShift
    └ ShiftUtils.executeShift
        ├ ShiftStoreUtils.remove
        ├ ExecuteWithdrawalUtils.executeWithdrawal
        ├ ShiftVault.recordTransferIn
        ├ ShiftVault.recordTransferIn
        └ ExecuteDepositUtils.executeDeposit
```

</div>

</div>

这里可以看到，shift 操作就是一个对于 withdraw from Market A && deposit to Market B 的封装。区别点在于用户使用 shift 可以避免支付 swap fees:

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/pricing/SwapPricingUtils.sol#L281C11-L283C10" class="external-link" rel="nofollow">SwapPricingUtils.getSwapFees</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getSwapFees(
    DataStore dataStore,
    address marketToken,
    uint256 amount,
    bool balanceWasImproved,
    address uiFeeReceiver,
    ISwapPricingUtils.SwapPricingType swapPricingType
) external view returns (SwapFees memory) {
    SwapFees memory fees;

    uint256 feeFactor;

    if (swapPricingType == ISwapPricingUtils.SwapPricingType.Swap) {
        feeFactor = dataStore.getUint(Keys.swapFeeFactorKey(marketToken, balanceWasImproved));
    } else if (swapPricingType == ISwapPricingUtils.SwapPricingType.Shift) {
        // Here:
        // empty branch as feeFactor is already zero
        // ...
    } else if (swapPricingType == ISwapPricingUtils.SwapPricingType.AtomicSwap) {
        feeFactor = dataStore.getUint(Keys.atomicSwapFeeFactorKey(marketToken));
    } else if (swapPricingType == ISwapPricingUtils.SwapPricingType.Deposit) {
        feeFactor = dataStore.getUint(Keys.depositFeeFactorKey(marketToken, balanceWasImproved));
    } else if (swapPricingType == ISwapPricingUtils.SwapPricingType.Withdrawal) {
        feeFactor = dataStore.getUint(Keys.withdrawalFeeFactorKey(marketToken, balanceWasImproved));
    } else if (swapPricingType == ISwapPricingUtils.SwapPricingType.AtomicWithdrawal) {
        feeFactor = dataStore.getUint(Keys.atomicWithdrawalFeeFactorKey(marketToken));
    }

    uint256 swapFeeReceiverFactor = dataStore.getUint(Keys.SWAP_FEE_RECEIVER_FACTOR);

    uint256 feeAmount = Precision.applyFactor(amount, feeFactor);

    // ...
}
```

</div>

</div>

</div>
