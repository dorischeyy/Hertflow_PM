# GLV Shift 代码解读

<div class="Section1">

## Create Shift

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/GlvShiftHandler.sol#L41C1-L47C6" class="external-link" rel="nofollow">GlvShiftHandler.createGlvShift</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
external globalNonReentrant onlyOrderKeeper returns (bytes32)
```

</div>

</div>

这里限制了只能由 keeper 自产自销。

## Execute Shift

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/GlvShiftHandler.sol#L49C1-L68C6" class="external-link" rel="nofollow">GlvShiftHandler.executeGlvShift</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 1. 先把 from market 的 GM Token 转出到 shiftVault
Bank(payable(glvShift.glv())).transferOut(
    glvShift.fromMarket(),
    address(params.shiftVault),
    glvShift.marketTokenAmount()
);
params.shiftVault.syncTokenBalance(glvShift.fromMarket());

// 2. 调用 shift，回收 to market 的 GM Token
cache.shift = Shift.Props(
    Shift.Addresses({
        account: glvShift.glv(), // self
        receiver: glvShift.glv(), // self
        callbackContract: address(0),
        uiFeeReceiver: address(0),
        fromMarket: glvShift.fromMarket(),
        toMarket: glvShift.toMarket()
    }),
    Shift.Numbers({
        minMarketTokens: glvShift.minMarketTokens(),
        marketTokenAmount: glvShift.marketTokenAmount(),
        updatedAtTime: glvShift.updatedAtTime(),
        executionFee: 0,
        callbackGasLimit: 0,
        srcChainId: 0 // srcChainId is the current block.chainId
    }),
    new bytes32[](0)
);

ShiftUtils.ExecuteShiftParams memory executeShiftParams = ShiftUtils.ExecuteShiftParams({
    // ...
});

cache.receivedMarketTokens = ShiftUtils.executeShift(executeShiftParams, cache.shift);
```

</div>

</div>

</div>
