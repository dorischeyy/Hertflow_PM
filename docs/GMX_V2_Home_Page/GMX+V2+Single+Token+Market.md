# GMX V2 Single Token Market

<div class="Section1">

GMX V2 支持单币种市场，也就是一个 Market 的 long token 和 short token 一致。比如：

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ffb2e3eaaa60ed9562d55ce32249d0b314181d4de778dde974091aa189a4b8bc" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/42991642/image-20251125-052701.png?version=1&amp;modificationDate=1764048425536&amp;cacheVersion=1&amp;api=v2" data-height="810" data-width="1478" data-unresolved-comment-count="0" data-linked-resource-id="42991650" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251125-052701.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="42991642" data-linked-resource-container-version="2" data-media-id="13cb97d2-67ed-4392-839c-ecb8a35c9271" data-media-type="file" width="468" height="256" alt="image-20251125-052701.png" /></span>

上面这个 Market 中，long / short token 均为 BTC，index token 也是 BTC。

<u>这个设计对于我们的单 USDC Market 产品有重要影响。</u>

------------------------------------------------------------------------

<style type="text/css">/**/
div.rbtoc1772270889594 {padding: 0px;}
div.rbtoc1772270889594 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270889594 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270889594">

- [1. Liquidity](#GMXV2SingleTokenMarket-1.Liquidity)
  - [1.1 Deposit](#GMXV2SingleTokenMarket-1.1Deposit)
  - [1.2 Withdraw](#GMXV2SingleTokenMarket-1.2Withdraw)
- [2. Position](#GMXV2SingleTokenMarket-2.Position)

</div>

## 1. Liquidity

### 1.1 Deposit

- createDeposit

用户创建 deposit 请求时，在单币市场内，只需要传入 long token。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createDeposit(
    DataStore dataStore,
    EventEmitter eventEmitter,
    DepositVault depositVault,
    address account,
    uint256 srcChainId,
    IDepositUtils.CreateDepositParams memory params
) external returns (bytes32) {
    // ...

    // if the initialLongToken and initialShortToken are the same, only the initialLongTokenAmount would
    // be non-zero, the initialShortTokenAmount would be zero
    uint256 initialLongTokenAmount = depositVault.recordTransferIn(params.addresses.initialLongToken);
    uint256 initialShortTokenAmount = depositVault.recordTransferIn(params.addresses.initialShortToken);

    // ...
}
```

</div>

</div>

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**技术实现**：

<u>用户/前端可以自定义 long short 的数量传入，依赖前端逻辑显然是不现实的</u>。

合约在技术上真正实现只有 long token 有 amount 的底层逻辑在于：

`recordTransferIn` 本身是一个基于 token 的计数器，调用这个方法会触发 token amount 更新。

用户需要提前通过 `sendWnt` / `sendToken` 存入 token 到合约，然后创建请求的时候去触发更新:

1.  let cur_amount = read();

2.  return cur_amount - old_amount;

由于 long / short token 是一致的，所以第一次调用该方法的时候，触发了更新，差值 diff 被记录到 long amount 里面，第二次调用时，diff 为 0，从而实现了只有 long token 计数。

</div>

</div>

- executeDeposit

公式：`gmTokenPrice = poolValue / totalSupply`

totalSupply 这里不展开，也就是每次 mint / burn 的时候更新计数。

回忆 `poolValue` 的计算逻辑：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
LP token price = pool value USD / market token total supply

pool value USD = USD values of long
  + USD values of short
  + pending borrowing fees
  - pnl
  - position impact pool
  + lent impact
```

</div>

</div>

这里 USD value of (long/short) tokens 在单币市场内其实是同一个，合约自动处理为一边一半，强制平衡：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
result.longTokenAmount = getPoolAmount(dataStore, market, market.longToken);
result.shortTokenAmount = getPoolAmount(dataStore, market, market.shortToken);

result.longTokenUsd = result.longTokenAmount * longTokenPrice.pickPrice(maximize);
result.shortTokenUsd = result.shortTokenAmount * shortTokenPrice.pickPrice(maximize);

result.poolValue = (result.longTokenUsd + result.shortTokenUsd).toInt256();
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 单币市场:
// 1. dataStore.getUint 获取的是同一个 value: key=hash(market, token)
// 2. pool Amonut 直接除以 2
function getPoolAmount(DataStore dataStore, Market.Props memory market, address token) internal view returns (uint256) {
    uint256 divisor = getPoolDivisor(market.longToken, market.shortToken);
    return dataStore.getUint(Keys.poolAmountKey(market.marketToken, token)) / divisor;
}

function getPoolDivisor(address longToken, address shortToken) internal pure returns (uint256) {
    return longToken == shortToken ? 2 : 1;
}
```

</div>

</div>

对于 OI 来说也是一样：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getOpenInterest(
    DataStore dataStore,
    Market.Props memory market,
    bool isLong
) internal view returns (uint256) {
    // div 2
    uint256 divisor = getPoolDivisor(market.longToken, market.shortToken);
    uint256 openInterestUsingLongTokenAsCollateral = getOpenInterest(dataStore, market.marketToken, market.longToken, isLong, divisor);
    uint256 openInterestUsingShortTokenAsCollateral = getOpenInterest(dataStore, market.marketToken, market.shortToken, isLong, divisor);

    return openInterestUsingLongTokenAsCollateral + openInterestUsingShortTokenAsCollateral;
}

function getOpenInterestInTokens(
    DataStore dataStore,
    Market.Props memory market,
    bool isLong
) internal view returns (uint256) {
    // div 2
    uint256 divisor = getPoolDivisor(market.longToken, market.shortToken);
    uint256 openInterestUsingLongTokenAsCollateral = getOpenInterestInTokens(dataStore, market.marketToken, market.longToken, isLong, divisor);
    uint256 openInterestUsingShortTokenAsCollateral = getOpenInterestInTokens(dataStore, market.marketToken, market.shortToken, isLong, divisor);

    return openInterestUsingLongTokenAsCollateral + openInterestUsingShortTokenAsCollateral;
}

// OI 是用来计算 PnL 的
// PnL = OIInTokens * LatestPrice - OI
```

</div>

</div>

最后关注一下 price impact，注意，这里的 price impact 指的是 deposit 本身的 swap price impact，而不是仓位的 price impact。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getNextPoolAmountsUsd(
    GetPriceImpactUsdParams memory params
) internal view returns (PoolParams memory) {
    // 这里两个值是一样的，都为 pool token amount 的一半
    uint256 poolAmountForTokenA = MarketUtils.getPoolAmount(params.dataStore, params.market, params.tokenA);
    uint256 poolAmountForTokenB = MarketUtils.getPoolAmount(params.dataStore, params.market, params.tokenB);

    return getNextPoolAmountsParams(
        params,
        poolAmountForTokenA,
        poolAmountForTokenB
    );
}

function getNextPoolAmountsParams(
    GetPriceImpactUsdParams memory params,
    uint256 poolAmountForTokenA,
    uint256 poolAmountForTokenB
) internal pure returns (PoolParams memory) {
    uint256 poolUsdForTokenA = poolAmountForTokenA * params.priceForTokenA;
    uint256 poolUsdForTokenB = poolAmountForTokenB * params.priceForTokenB;

    if (params.usdDeltaForTokenA < 0 && (-params.usdDeltaForTokenA).toUint256() > poolUsdForTokenA) {
        revert Errors.UsdDeltaExceedsPoolValue(params.usdDeltaForTokenA, poolUsdForTokenA);
    }

    if (params.usdDeltaForTokenB < 0 && (-params.usdDeltaForTokenB).toUint256() > poolUsdForTokenB) {
        revert Errors.UsdDeltaExceedsPoolValue(params.usdDeltaForTokenB, poolUsdForTokenB);
    }

    // 这里两个 next 值不一样了，因为前面说过 create deposit 的时候只有 long 没有 short
    uint256 nextPoolUsdForTokenA = Calc.sumReturnUint256(poolUsdForTokenA, params.usdDeltaForTokenA);
    uint256 nextPoolUsdForTokenB = Calc.sumReturnUint256(poolUsdForTokenB, params.usdDeltaForTokenB);

    PoolParams memory poolParams = PoolParams(
        poolUsdForTokenA,
        poolUsdForTokenB,
        nextPoolUsdForTokenA,
        nextPoolUsdForTokenB
    );

    return poolParams;
}


function _getPriceImpactUsd(DataStore dataStore, Market.Props memory market, PoolParams memory poolParams) internal view returns (int256, bool) {
    // 根据前面的推导，initialDiffUsd = 0, nextDiffUsd = deposit 金额
    uint256 initialDiffUsd = Calc.diff(poolParams.poolUsdForTokenA, poolParams.poolUsdForTokenB);
    uint256 nextDiffUsd = Calc.diff(poolParams.nextPoolUsdForTokenA, poolParams.nextPoolUsdForTokenB);
    // ...
}
```

</div>

</div>

综上，这里会收取 price impact fee，因此需要把 `SWAP_IMPACT_FACTOR` 这个配置设置为 0，才能避免收费。

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**总结：**

流动性模块，需要把 SWAP_IMPACT_FACTOR 设置为 0 避免收取 price impact fee，别的功能支持的比较完善。不需要做额外改造。

</div>

</div>

------------------------------------------------------------------------

### 1.2 Withdraw

从两侧 token 各取一半，原理和 deposit 一样： poolAmount 共享除以 2

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getProportionalAmounts(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices,
    uint256 totalUsd
) internal view returns(uint256, uint256) {
    uint256 longTokenPoolAmount = getPoolAmount(dataStore, market, market.longToken);
    uint256 shortTokenPoolAmount = getPoolAmount(dataStore, market, market.shortToken);

    uint256 longTokenPoolUsd = longTokenPoolAmount * prices.longTokenPrice.max;
    uint256 shortTokenPoolUsd = shortTokenPoolAmount * prices.shortTokenPrice.max;

    uint256 totalPoolUsd = longTokenPoolUsd + shortTokenPoolUsd;

    uint256 longTokenOutputUsd = Precision.mulDiv(totalUsd, longTokenPoolUsd, totalPoolUsd);
    uint256 shortTokenOutputUsd = Precision.mulDiv(totalUsd, shortTokenPoolUsd, totalPoolUsd);

    return (longTokenOutputUsd / prices.longTokenPrice.max, shortTokenOutputUsd / prices.shortTokenPrice.max);
}
```

</div>

</div>

由此可以看到，前端计算 Withdraw limit 时，仍然需要关注 OI 力量，因为两侧都会 validate：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
MarketUtils.validateReserve(params.dataStore, market, prices, true); // long
MarketUtils.validateReserve(params.dataStore, market, prices, false); // short
```

</div>

</div>

比如 10000\$ USDC 虽然 amount 共享，但是 OI 如果倾斜，比如 5000\$ 的 short 被 reserve 了 4900\$，5000\$ 的 long 基本没怎么用，能够提取的部分，依然要用短板的 short 来算，也就是 5000-4900 = 100\$，然后乘以 2（因为 long 部分也可以提取对应部分出来，因为不是短板，所以肯定 ≥ 100\$ 的可提取量）。至于其他的 validate 逻辑，更为精密，前端可以视情况 copy 合约算法。

------------------------------------------------------------------------

## 2. Position

position 这里，主要关注 OI 这个指标即可，因为 funding fee 和 reserve 以及 pending PnL 之类的东西，都是基于 OI 计算的，一个是 OI Usd，一个是 OI in tokens：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function updateOpenInterest(
    PositionUtils.UpdatePositionParams memory params,
    int256 sizeDeltaUsd,
    int256 sizeDeltaInTokens
) internal {
    if (sizeDeltaUsd != 0) {
        MarketUtils.applyDeltaToOpenInterest(
            params.contracts.dataStore,
            params.contracts.eventEmitter,
            params.market,
            params.position.collateralToken(), // here
            params.position.isLong(),          // here
            sizeDeltaUsd
        );

        MarketUtils.applyDeltaToOpenInterestInTokens(
            params.contracts.dataStore,
            params.contracts.eventEmitter,
            params.position.market(),
            params.position.collateralToken(), // here
            params.position.isLong(),          // here
            sizeDeltaInTokens
        );
    }
}
```

</div>

</div>

可以看到，正常的 Market 里面有 4 种情况，用 long / short token 做多/空 = 2x2 = 4，在单币市场里面简化为 2 种，因为 token 只有一种了。

对应的，依赖 OI 计算的部分，也做了对应的除 2 操作，比如前面提到的 poolValue，这里再列举一下 funding fee 和 reserved usd：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getNextFundingAmountPerSize(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices
) internal view returns (GetNextFundingAmountPerSizeResult memory) {
    GetNextFundingAmountPerSizeResult memory result;
    GetNextFundingAmountPerSizeCache memory cache;

    uint256 divisor = getPoolDivisor(market.longToken, market.shortToken);

    // get the open interest values by long / short and by collateral used
    // xxx.long 视为一个整体了，long.longToken 和 shortToken 都 / 2 了
    // xxx.short 同理
    cache.openInterest.long.longToken = getOpenInterest(dataStore, market.marketToken, market.longToken, true, divisor);
    cache.openInterest.long.shortToken = getOpenInterest(dataStore, market.marketToken, market.shortToken, true, divisor);
    cache.openInterest.short.longToken = getOpenInterest(dataStore, market.marketToken, market.longToken, false, divisor);
    cache.openInterest.short.shortToken = getOpenInterest(dataStore, market.marketToken, market.shortToken, false, divisor);

    // sum the open interest values to get the total long and short open interest values
    cache.longOpenInterest = cache.openInterest.long.longToken + cache.openInterest.long.shortToken;
    cache.shortOpenInterest = cache.openInterest.short.longToken + cache.openInterest.short.shortToken;

    // ...
}

function getReservedUsd(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices,
    bool isLong
) internal view returns (uint256) {
    uint256 reservedUsd;
    if (isLong) {
        // for longs calculate the reserved USD based on the open interest and current indexTokenPrice
        // this works well for e.g. an ETH / USD market with long collateral token as WETH
        // the available amount to be reserved would scale with the price of ETH
        // this also works for e.g. a SOL / USD market with long collateral token as WETH
        // if the price of SOL increases more than the price of ETH, additional amounts would be
        // automatically reserved
        uint256 openInterestInTokens = getOpenInterestInTokens(dataStore, market, isLong);
        reservedUsd = openInterestInTokens * prices.indexTokenPrice.max;
    } else {
        // for shorts use the open interest as the reserved USD value
        // this works well for e.g. an ETH / USD market with short collateral token as USDC
        // the available amount to be reserved would not change with the price of ETH
        reservedUsd = getOpenInterest(dataStore, market, isLong);
    }

    return reservedUsd;
}
```

</div>

</div>

</div>
