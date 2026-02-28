# GLV Deposit Mint 代码解读

<div class="Section1">

## Create Deposit

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/router/GlvRouter.sol#L42C1-L48C6" class="external-link" rel="nofollow">GlvRouter.createGlvDeposit</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1. Send tokens to deposit GLV vault
2. Send execution fee to GLV vault
3. Create deposit order

GlvRouter.createGlvDeposit
└ GlvDepositHandler.createGlvDeposit
    └ GlvDepositUtils.createGlvDeposit
        ├ GlvVault.recordTransferIn
        ├ GlvVault.recordTransferIn
        ├ GlvVault.recordTransferIn
        └ GlvDepositStoreUtils.set
```

</div>

</div>

## Execute Deposit

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/GlvDepositHandler.sol#L48C2-L70C6" class="external-link" rel="nofollow">GlvDepositHandler.executeGlvDeposit</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GlvDepositHandler
└ executeGlvDeposit
    ├ GlvDepositStoreUtils.get
    └ _executeGlvDeposit
        └ ExecuteGlvDepositUtils.executeGlvDeposit
            ├ GlvDepositStoreUtils.remove
            ├ _processMarketDeposit
            │  └ ExecuteDepositUtils.executeDeposit
            ├ _getMintAmount
            └ GlvToken.mint
```

</div>

</div>

Deposit 大致可以分为两类，一类是用 WETH / USDC 之类的币入金，另一类是用 GM Tokens 入金。

本质上来说，最后都要落到 GM Tokens 上，当你用 WETH / USDC 入金时，GLV 会帮你去底层 market 做一次 deposit，获得 market token（GM Token）。

因为 GLV 本质上持有的是 market tokens，它并不直接持有 WETH / USDC。

经过了前面的转换（或者没转换直接投资 GM Token），就走如下的算法计算 mint amount:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getMintAmount(
    DataStore dataStore,
    IOracle oracle,
    GlvDeposit.Props memory glvDeposit,
    uint256 receivedMarketTokens,
    uint256 glvValue,
    uint256 glvSupply
) external view returns (uint256) {
    Market.Props memory market = MarketUtils.getEnabledMarket(dataStore, glvDeposit.market());
    MarketPoolValueInfo.Props memory poolValueInfo = MarketUtils.getPoolValueInfo(
        dataStore,
        market,
        oracle.getPrimaryPrice(market.indexToken),
        oracle.getPrimaryPrice(market.longToken),
        oracle.getPrimaryPrice(market.shortToken),
        Keys.MAX_PNL_FACTOR_FOR_DEPOSITS,
        false // maximize
    );
    // 这里计算了 marketToken 的 USD 市值
    uint256 marketTokenSupply = MarketUtils.getMarketTokenSupply(MarketToken(payable(market.marketToken)));
    uint256 receivedMarketTokensUsd = MarketUtils.marketTokenAmountToUsd(
        receivedMarketTokens,
        poolValueInfo.poolValue.toUint256(),
        marketTokenSupply
    );
    // 用 USD 价值计算 mint amount
    return GlvUtils.usdToGlvTokenAmount(receivedMarketTokensUsd, glvValue, glvSupply);
}
```

</div>

</div>

</div>
