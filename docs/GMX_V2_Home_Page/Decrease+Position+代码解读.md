# Decrease Position 代码解读

<div class="Section1">

## Create Decrease Order

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
         └ OrderStoreUtils.set
```

</div>

</div>

------------------------------------------------------------------------

## Execute Order

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
│     │  └─ DecreaseOrderUtils.processOrder
│     │     ├─ PositionStoreUtils.get
│     │     ├─ DecreasePositionUtils.decreasePosition
│     │     │  ├─ DecreasePositionCollateralUtils.processCollateral
│     │     │  │  ├─ PositionUtils.getPositionPnlUsd
│     │     │  │  ├─ MarketUtils.applyDeltaToPoolAmount
│     │     │  │  ├─ DecreasePositionSwapUtils.swapProfitToCollateralToken
│     │     │  │  ├─ PositionPricingUtils.getPositionFees
│     │     │  │  ├─ payForCost
│     │     │  │  ├─ payForCost
│     │     │  │  ├─ payForCost
│     │     │  │  ├─ payForCost
│     │     │  │  └─ payForCost
│     │     │  ├─ PositionUtils.updateTotalBorrowing
│     │     │  ├─ PositionStoreUtils.set or remove
│     │     │  ├─ MarketUtils.applyDeltaToCollateralSum
│     │     │  ├─ PositionUtils.updateOpenInterest
│     │     │  └─ DecreasePositionSwapUtils.swapWithdrawnCollateralToPnlToken
│     │     └─ SwapUtils.swap
│     └─ GasUtils.payExecutionFee
└─ OracleModule.withOraclePrices
   └─ Oracle.clearAllPrices
```

</div>

</div>

这里逻辑很复杂，主要关注核心的减仓逻辑：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
DecreaseOrderUtils.processOrder
├─ PositionStoreUtils.get
├─ DecreasePositionUtils.decreasePosition
│  ├─ DecreasePositionCollateralUtils.processCollateral
│  │  ├─ PositionUtils.getPositionPnlUsd
│  │  ├─ MarketUtils.applyDeltaToPoolAmount
│  │  ├─ DecreasePositionSwapUtils.swapProfitToCollateralToken
│  │  ├─ PositionPricingUtils.getPositionFees
│  │  ├─ payForCost
│  │  ├─ payForCost
│  │  ├─ payForCost
│  │  ├─ payForCost
│  │  └─ payForCost
│  ├─ PositionUtils.updateTotalBorrowing
│  ├─ PositionStoreUtils.set or remove
│  ├─ MarketUtils.applyDeltaToCollateralSum
│  ├─ PositionUtils.updateOpenInterest
│  └─ DecreasePositionSwapUtils.swapWithdrawnCollateralToPnlToken
└─ SwapUtils.swap
```

</div>

</div>

1.  最外层，三段式逻辑

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
最外层 DecreaseOrderUtils.processOrder 的逻辑比较清晰：
1. 从 datastore 找到对应的 position
2. 调用 decreasePosition 去完成减仓操作，这个函数会返回减仓吐出来的tokens信息
3. 调用 swap 去发送减仓吐出来的 tokens（参考 swap 代码解读文档结尾）
```

</div>

</div>

2.  中间层，两段式逻辑

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
DecreasePositionUtils.decreasePosition 的逻辑略复杂：
1. 调用内层的 DecreasePositionCollateralUtils.processCollateral 去处理仓位保证金逻辑。
  这里会返回减仓出来的保证金数量，仓位减仓后的状态，以及支付的各种费用。
2. 拿着前面返回的计算值，去真正的做一些set操作，把计算结果落地。
  包括仓位本身的状态：position.setSizeInUsd / setSizeInTokens
  全局量：totalBorrowing / collateralSum / OI
  费用相关的状态：borrowing / funding fee 都用的累积算法，这里需要更新仓位的 last factor，避免重复收费
3. 最后还有一步 swap 逻辑，允许用户把 coll 转化为 pnl token。
```

</div>

</div>

3.  最内层，实际减仓的逻辑核心

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
DecreasePositionCollateralUtils.processCollateral 是实际减仓的核心逻辑，主要关注 PNL 和保证金

values.output.outputToken = params.position.collateralToken();
values.output.secondaryOutputToken = cache.pnlToken;

1. 计算 PNL，盈利了则从 market 中移走资金
2. 处理 Price Impact，这里注意价格冲击费用是 lazy 的，寄存在 position 的 pending 字段里面
  这里减仓的时候带来的新一次 imapct 费用要和之前寄存的费用求和。
  如果 impact usd > 0，从 priceImpactPool 中移走资金(注意这个pool，还不清楚有什么用)
    并且从 market pool 中移走对应的资金
3. 如果配置了 pnl token swap to collateral token，做一次 swap。
4. 开始支付费用
  - 费用支付逻辑：
    - 先从减仓吐出的 coll 部分扣费（注意3可能把pnl也swap成coll了）
    - 再从仓位剩余 coll 部分扣费
    - 再从 pnl 部分扣费（注意3可能把pnl也swap成吐出的coll了，这里就不够了）
    - 不够的部分记录下来
    - 如果不够，则根据是否是破产强平来继续（这里看产品文档中破产强平的叙述）
  然后分别使用上述逻辑进行(下面都是usd)：
  - funding fee
  - negative pnl
  - other fees execpt funding fee(borrow/position/liq/ui)
  - negative price impact(注意这个是独立扣的，不在上面这一行)
  - price impact diff(这里需要注意一下，就是impact fee会被 cap，因此一个大value被拆分为 limit+diff了)
  
```

</div>

</div>

> 这里可以看到，2+3都处理了一些datastore资金相关的字段，但是二者的目标不一样：
>
> 2 主要处理费用(cumulative)和仓位(position)信息，还有一些全局的统计(OI, totalXXX)信息。
>
> 3 主要处理 PNL（这里涉及 pool 的余额变化了） 和保证金（这里主要是内存计算，丢给上层的 2 处理）
>
> SWAP 部分，涉及到三层:
>
> 1.  第一层是最内部的：是否把 pnl 转化为 coll token
>
> 2.  第二层是中间的：是否把 coll token 转化为 pnl token
>
> 3.  第三层是 coll 根据接口传入的 swap path 进行出金的统一化。
>
> 这样设计的意图在于，如果你想走1或者2，减仓出金可以在当前仓位的market完成swap。
>
> 例子： ETH/USDC市场内进行减仓
>
> 仓位本身是用ETH开多，出金设置为 ETH，只需要走 1（pnl 就是 ETH，实际上也没swap）
>
> 仓位本身用USDC开多，出金设置为 ETH，需要走 2（pnl 是 ETH 没错，但是保证金是 U，要 swap）
>
> 仓位本身用 USDC 开多，出金设置为 BTC，需要走1+3或者2+3，其中1+3意味着3是 USDC-\>BTC，而 2+3 意味着 3 是 ETH → BTC

</div>
