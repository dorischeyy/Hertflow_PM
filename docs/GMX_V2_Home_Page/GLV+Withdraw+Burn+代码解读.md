# GLV Withdraw Burn 代码解读

<div class="Section1">

## Create Withdraw

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/router/GlvRouter.sol#L77C1-L83C6" class="external-link" rel="nofollow">GlvRouter.createGlvWithdrawal</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1. Send GLV token to GLV vault
2. Send execution fee to GLV vault
3. Create withdrawal order

GlvRouter.createGlvWithdrawal
└ GlvWithdrawalHandler.createGlvWithdrawal
    └ GlvWithdrawalUtils.createGlvWithdrawal
        ├ GlvVault.recordTransferIn
        └ GGlvWithdrawalStoreUtils.set
```

</div>

</div>

## Execute Withdraw

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/GlvWithdrawalHandler.sol#L49C1-L75C6" class="external-link" rel="nofollow">GlvWithdrawalHandler.executeGlvWithdrawal</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GlvWithdrawalHandler
└ executeGlvWithdrawal
    ├ GlvDepositStoreUtils.get
    └ _executeGlvWithdrawal
        └ GlvWithdrawalUtils.executeGlvWithdrawal
            ├ GlvWithdrawalStoreUtils.remove
            └ _processMarketWithdrawal
               ├ Glv.transferOut
               └ ExecuteWithdrawalUtils.executeWithdrawal
```

</div>

</div>

Withdraw 的流程，就是：

1.  归还 GLV Token 给到 GLV

2.  GLV 归还 Market Token 给到 Market

3.  走一次正常的普通 Market Withdraw 流程，把 Market Token Burn 得到的原始币给回用户。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function _getMarketTokenAmount(
    DataStore dataStore,
    IOracle oracle,
    GlvWithdrawal.Props memory glvWithdrawal
) internal view returns (uint256) {
    uint256 glvValue = GlvUtils.getGlvValue(
        dataStore,
        oracle,
        glvWithdrawal.glv(),
        false // maximize
    );
    uint256 glvSupply = GlvToken(payable(glvWithdrawal.glv())).totalSupply();
    // 把归还的 GLV 转为 USD
    uint256 glvTokenUsd = GlvUtils.glvTokenAmountToUsd(glvWithdrawal.glvTokenAmount(), glvValue, glvSupply);

    Market.Props memory market = MarketUtils.getEnabledMarket(dataStore, glvWithdrawal.market());
    MarketPoolValueInfo.Props memory poolValueInfo = MarketUtils.getPoolValueInfo(
        dataStore,
        market,
        oracle.getPrimaryPrice(market.indexToken),
        oracle.getPrimaryPrice(market.longToken),
        oracle.getPrimaryPrice(market.shortToken),
        Keys.MAX_PNL_FACTOR_FOR_WITHDRAWALS,
        true // maximize
    );

    // 计算最新的 MarketToken 数量
    // Return Glv -> 转化为 Return USD -> 转化为 MarketToken Amount
    uint256 marketTokenAmount = MarketUtils.usdToMarketTokenAmount(
        glvTokenUsd,
        poolValueInfo.poolValue.toUint256(),
        ERC20(market.marketToken).totalSupply()
    );

    return marketTokenAmount;
}
```

</div>

</div>

</div>
