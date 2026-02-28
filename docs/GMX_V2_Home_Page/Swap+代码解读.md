# Swap 代码解读

<div class="Section1">

## Create Swap Order

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExchangeRouter.multicall
├ ExchangeRouter.sendWnt                -- 发送 keeper 执行费
├ ExchangeRouter.sendTokens             -- 发送 swap in token
└ ExchangeRouter.createOrder
   └ OrderHandler.createOrder
      └ OrderUtils.createOrder
         ├ OrderVault.recordTransferIn  -- 这个函数的功能是校验入金是否成功
         ├ OrderVault.recordTransferIn
         └ OrderStoreUtils.set
```

</div>

</div>

## Execute

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
OrderHandler.executeOrder
├ OracleModule.withOraclePrices
│  └ Oracle.setPrices
├ OrderStoreUtils.get
├ _executeOrder
│  └ ExecuteOrderUtils.executeOrder
│     ├ OrderStoreUtils.remove
│     ├ MarketUtils.getMarketPrices
│     ├ MarketUtils.distributePositionImpactPool
│     ├ PositionUtils.updateFundingAndBorrowingState
│     ├ processOrder
│     │  └ SwapOrderUtils.processOrder
│     │     └ SwapUtils.swap
│     │        ├ OrderVault.transferOut
│     │        └ for loop for each market in swap path
│     │           └ _swap
│     │              ├ Oracle.getPrimaryPrice
│     │              ├ Oracle.getPrimaryPrice
│     │              ├ SwapPricingUtils.getPriceImpactUsd
│     │              ├ SwapPricingUtils.getSwapFees
│     │              ├ MarketToken.transferOut
│     │              ├ MarketUtils.applyDeltaToPoolAmount
│     │              │  └ applyDeltaToVirtualInventoryForSwaps
│     │              └ MarketUtils.applyDeltaToPoolAmount
│     │                 └ applyDeltaToVirtualInventoryForSwaps
│     └ GasUtils.payExecutionFee
└ OracleModule.withOraclePrices
   └ Oracle.clearAllPrices
```

</div>

</div>

这里需要注意一些 solidity 的特殊语法，很多重要的功能比如 ACL 和 Oracle 都使用的 modifier 修饰符语法实现的：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function executeOrder(
    bytes32 key,
    OracleUtils.SetPricesParams calldata oracleParams
) external
    globalNonReentrant
    onlyOrderKeeper
    withOraclePrices(oracleParams)

// onlyOrderKeeper 这里校验的权限
// withOraclePrices 这里设置的价格，后续整个 tx 都可以访问到

modifier withOraclePrices(
    OracleUtils.SetPricesParams memory params
) {
    oracle.setPrices(params);
    _;
    oracle.clearAllPrices();
}

// 这里可以看到 oracle 都逻辑，是在 tx 执行之前，先 set 好所有要使用的价格
// 然后执行 tx
// 执行完毕后，把 oracle 的数据清空
```

</div>

</div>

最后看一下间接 swap 的核心逻辑：

假设我们正在从 DAI - USDC - WETH 路径，用 DAI 交换到 WETH

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 初始设置为 input token 的类型和数量
address tokenOut = params.tokenIn;
uint256 outputAmount = params.amountIn;

// 遍历 DAI/USDC 和 USDC-WETH
for (uint256 i; i < params.swapPathMarkets.length; i++) {
    Market.Props memory market = params.swapPathMarkets[i];

    // ...

    // 如果遍历到结尾了，出金就是 WETH 了，该转给 user
    // 否则，还在 swap 流程中，上一个 pool 转出的币比如 USDC 应该转给下一个 pool
    // 也就是说用 DAI 从 DAI-USDC 换出的 USDC 应该转给 USDC-WETH
    uint256 nextIndex = i + 1;
    address receiver;
    if (nextIndex < params.swapPathMarkets.length) {
        receiver = params.swapPathMarkets[nextIndex].marketToken;
    } else {
        receiver = params.receiver;
    }

    // 执行 swap
    _SwapParams memory _params = _SwapParams(
        market,
        tokenOut,
        outputAmount,
        receiver,
        i == params.swapPathMarkets.length - 1 ? params.shouldUnwrapNativeToken : false // only convert ETH on the last swap if needed
    );

    (tokenOut, outputAmount) = _swap(params, _params);
}
```

</div>

</div>

<span style="background-color: rgb(254,222,200);">注意，SwapUtils.swap 函数，被设计为一个通用的东西了（指的是 swap 本身和 transfer 的融合）：</span>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function swap(ISwapUtils.SwapParams memory params) external returns (address, uint256) {
        if (params.amountIn == 0) {
            return (params.tokenIn, params.amountIn);
        }

        // NOTE: 这个分支，接受不做任何 swap 的情况
        if (params.swapPathMarkets.length == 0) {
            // 本质上就是把传入的 swap in(token, token_amount) 转给 receiver
            // 所以这里需要校验一下，传入的 in 不能 < out
            if (params.amountIn < params.minOutputAmount) {
                revert Errors.InsufficientOutputAmount(params.amountIn, params.minOutputAmount);
            }
          
            // 这里做 transfer
            if (address(params.bank) != params.receiver) {
                params.bank.transferOut(
                    params.tokenIn,  // 传入的 token
                    params.receiver, // 转给某个人
                    params.amountIn, // 传入的 token amount in
                    params.shouldUnwrapNativeToken
                );
            }

            return (params.tokenIn, params.amountIn);
        }

        // ...
}
```

</div>

</div>

因此 GMX 在加减仓位的时候，经常在结尾处调用一下 swap，完成仓位的资金结算流程，哪怕逻辑上看起来和 swap 无关。

</div>
