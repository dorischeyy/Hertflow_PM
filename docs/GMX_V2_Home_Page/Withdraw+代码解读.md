# Withdraw 代码解读

<div class="Section1">

## Create Withdraw

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/router/ExchangeRouter.sol#L169C1-L179C6" class="external-link" rel="nofollow">ExchangeRouter.createWithdraw</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1. Send market token to withdrawal vault
2. Send execution fee to withdrawal vault
3. Create withdrawal order

ExchangeRouter.createWithdrawal
└ WithdrawalHandler.createWithdrawal
    └ WithdrawalUtils.createWithdrawal
        ├ WithdrawalVault.recordTransferIn
        ├ WithdrawalVault.recordTransferIn
        └ WithdrawalStoreUtils.set
```

</div>

</div>

## Execute Withdraw

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/WithdrawalHandler.sol#L97C1-L132C6" class="external-link" rel="nofollow">WithdrawHandler.executeWithdrawal</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
WithdrawalHandler.executeWithdrawal
├ WithdrawalStoreUtils.get
└ _executeWithdrawal
    └ ExecuteWithdrawalUtils.executeWithdrawal
        ├ WithdrawalStoreUtils.remove
        ├ MarketUtils.distributePositionImpactPool
        ├ PositionUtils.updateFundingAndBorrowingState
        └ _executeWithdrawal
            ├ _getOutputAmounts
            │   ├ MarketUtils.getPoolAmount
            │   └ MarketUtils.getPoolAmount
            ├ MarketUtils.applyDeltaToPoolAmount
            ├ MarketUtils.applyDeltaToPoolAmount
            ├ MarketToken.burn
            ├ _swap
            │   └ SwapUtils.swap
            └ _swap
                └ SwapUtils.swap
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function marketTokenAmountToUsd(
    uint256 marketTokenAmount,
    uint256 poolValue,
    uint256 supply
) internal pure returns (uint256) {
    if (supply == 0) { revert Errors.EmptyMarketTokenSupply(); }

    return Precision.mulDiv(poolValue, marketTokenAmount, supply);
}
```

</div>

</div>

> withdraw 的 usd 数量，就是用 marketTokenPrice \* marketTokenAmount，其中 marketTokenPrice 等价于：poolValue / supply

</div>
