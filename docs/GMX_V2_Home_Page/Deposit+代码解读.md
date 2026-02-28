# Deposit 代码解读

<div class="Section1">

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/router/ExchangeRouter.sol#L121C1-L140C6" class="external-link" rel="nofollow">ExchangeRouter.createDeposit</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1. Send long and or short tokens to deposit vault
2. Send execution fee to deposit vault
3. Create deposit order

1 和 2 走 sendWnt，可能重复，比如存入的 WETH，一部分用来支付 keeper，剩余的用来 deposit

ExchangeRouter.createDeposit
└ DepositHandler.createDeposit
    └ DepositUtils.createDeposit
        ├ DepositVault.recordTransferIn
        ├ DepositVault.recordTransferIn
        └ DepositStoreUtils.set
```

</div>

</div>

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/DepositHandler.sol#L97C2-L128C6" class="external-link" rel="nofollow">DepositHandler.executeDeposit</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
DepositHandler.executeDeposit
├ DepositStoreUtils.get
└ _executeDeposit
    └ ExecuteDepositUtils.executeDeposit
        ├ DepositStoreUtils.remove
        ├ MarketUtils.distributePositionImpactPool
        ├ PositionUtils.updateFundingAndBorrowingState
        ├ swap
        │   └ SwapUtils.swap
        ├ swap
        │   └ SwapUtils.swap
        ├ _executeDeposit
        │   ├ MarketUtils.applyDeltaToPoolAmount
        │   └ MarketToken.mint
        └ _executeDeposit
            ├ MarketUtils.applyDeltaToPoolAmount
            └ MarketToken.mint
```

</div>

</div>

这里提一下 mint amount 的算法，和 GM Token Price 算法差不多：

- 回忆一下 GM Token Price:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Precision.mulDiv(Precision.WEI_PRECISION, poolValueInfo.poolValue, supply);
```

</div>

</div>

> poolValue / supply 也就是每个 GM Token 的价格了。

- mint amount：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Precision.mulDiv(supply, usdValue, poolValue)
```

</div>

</div>

> 这里就是质押的 USD / 每个 GM Price 计算得到 GM 数量的
>
> usdValue / (poolValue/supply) = usdValue \* supply / poolValue

</div>
