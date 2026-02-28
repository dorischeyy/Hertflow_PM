# Borrow Fee 代码解读

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270793229 {padding: 0px;}
div.rbtoc1772270793229 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270793229 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270793229">

- [1. Borrow Fee 如何计算？](#BorrowFee代码解读-1.BorrowFee如何计算？)
- [2. Borrow Fee 何时更新？](#BorrowFee代码解读-2.BorrowFee何时更新？)
- [3. Borrow Fee Factor 如何计算？](#BorrowFee代码解读-3.BorrowFeeFactor如何计算？)
- [4. Pending Borrowing Fee](#BorrowFee代码解读-4.PendingBorrowingFee)

</div>

## 1. Borrow Fee 如何计算？

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1708-L1715" class="external-link" rel="nofollow">MarketUtils.getBorrowingFees</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getBorrowingFees(DataStore dataStore, Position.Props memory position) internal view returns (uint256) {
    uint256 cumulativeBorrowingFactor = getCumulativeBorrowingFactor(dataStore, position.market(), position.isLong());
    if (position.borrowingFactor() > cumulativeBorrowingFactor) {
        revert Errors.UnexpectedBorrowingFactor(position.borrowingFactor(), cumulativeBorrowingFactor);
    }
    uint256 diffFactor = cumulativeBorrowingFactor - position.borrowingFactor();
    return Precision.applyFactor(position.sizeInUsd(), diffFactor);
}
```

</div>

</div>

算法十分简单：查看借贷费率的累积值，距离上次增长了多少，然后用增长的部分 \* position_size 即可。

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**CumulativeBorrowingFactor**

根据<a href="https://hertzflow.atlassian.net/wiki/spaces/~712020911aa4676af94facaccba78eea495f59/pages/32571463/Part+2.+GMX+V2#1.1.5-Borrowing-Fee-%E5%80%9F%E8%B4%B7%E8%B4%B9" data-linked-resource-id="32571463" data-linked-resource-version="48" data-linked-resource-type="page">业务文档</a>里面的解释:，不难理解这个变量指代的是：借贷费率 R per second 在过去每一秒的累加。

更通俗的理解是，这里可以认为是我的仓位由于借贷费而扣除的百分比之和。

比如：

1.  在上周一，我进行开仓(100 USD)，此时还没收取任何比例，即0%;

2.  在本周一，过去一周，借贷费需要扣除我的仓位 10% 的费用，此时累积出来是 10 %，diff 为 10 %，因此结算的时候，我需要支付的费用就是 10% \* position_size_usd_1 (100 USD) = 10U。

    1.  支付了 10U fee

    2.  仓位从 100U 减少到 90U

    3.  最后一次收费的 factor 记录下来为 10%

3.  在下周三的时候，又过去一周，借贷费又需要扣除我 15%的比例，此时 cumulative 增长到了 25%，但我们不会用 25%直接参与计算，因为 2 中已经扣过一次。此时计算 diff = 25 - 10(2.c中记录了) = 15%。此时收取 15% \* position_size_usd_2 (90U) = 13.5U。

    1.  支付了 13.5 U fee

    2.  仓位从 90 U 减少到 76.5 U

    3.  最后一次收费的 factor 记录下来为 25%

</div>

</div>

------------------------------------------------------------------------

## 2. Borrow Fee 何时更新？

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1417-L1440" class="external-link" rel="nofollow">MarketUtils.updateCumulativeBorrowingFactor</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExecuteOrderUtils.executeOrder
├ PositionUtils.updateFundingAndBorrowingState
└ processOrder
    └ IncreaseOrderUtils.processOrder
        └ IncreasePositionUtils.increasePosition
            ├ processCollateral
            │   ├ PositionPricingUtils.getPositionFees
            │   │  └ MarketUtils.getBorrowingFees
            │   └ MarketUtils.applyDeltaToPoolAmount
            ├ params.position.setCollateralAmount
            ├ MarketUtils.getCumulativeBorrowingFactor
            ├ PositionUtils.updateTotalBorrowing
            └ params.position.setBorrowingFactor
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExecuteOrderUtils.executeOrder
├ PositionUtils.updateFundingAndBorrowingState
└ processOrder
    └ DecreaseOrderUtils.processOrder
        └ DecreasePositionUtils.decreasePosition
            ├ DecreasePositionCollateralUtils.processCollateral
            │   ├ PositionPricingUtils.getPositionFees
            │   │  └ MarketUtils.getBorrowingFees
            │   └ MarketUtils.applyDeltaToPoolAmount
            ├ MarketUtils.getCumulativeBorrowingFactor
            ├ PositionUtils.updateTotalBorrowing
            ├ params.position.setBorrowingFactor
            └ params.position.setCollateralAmount
```

</div>

</div>

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

加减仓的时候会触发更新。因为加减仓操作，同时变更了两个 borrow fee 的计算参数。

- position_size 在加减仓后会发生改变，这里很好理解。

- borrow_fee_rate 本身是根据资金利用率变化的，加减仓操作不可避免的会影响池子的资金状态，由此间接影响 rate。

- 因此在加减仓时，首先更新 borrow fee factor，然后在计算完 borrow fee 后，再调整仓位 size。

</div>

</div>

------------------------------------------------------------------------

## 3. Borrow Fee Factor 如何计算？

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1417-L1440" class="external-link" rel="nofollow">MarketUtils.updateCumulativeBorrowingFactor</a>

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L2368-L2430" class="external-link" rel="nofollow">MarketUtils.getBorrowingFactorPerSecond</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
PositionUtils.updateFundingAndBorrowingState
└ MarketUtils.updateCumulativeBorrowingFactor
    ├ getNextCumulativeBorrowingFactor
    │    ├ getSecondsSinceCumulativeBorrowingFactorUpdated
    │    ├ getBorrowingFactorPerSecond
    │    │  ├ getOptimalUsageFactor
    │    │  ├ if optimal usage factor != 0
    │    │  │  └ getKinkBorrowingFactor
    │    │  │      └ getUsageFactor
    │    │  ├ getBorrowingExponentFactor
    │    │  └ getBorrowingFactor
    │    └ getCumulativeBorrowingFactor
    └ incrementCumulativeBorrowingFactor
```

</div>

</div>

**Breakdown:**

1.  更新累积值

> 这里比较简单，new_cumulative_factor = old_cumulative_factor + delta。
>
> delta = time_gap \* factor_per_sec

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getNextCumulativeBorrowingFactor(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices,
    bool isLong
) internal view returns (uint256, uint256, uint256) {
    // 获取 time_gap
    uint256 durationInSeconds = getSecondsSinceCumulativeBorrowingFactorUpdated(dataStore, market.marketToken, isLong);

    // 获取 factor_per_sec
    uint256 borrowingFactorPerSecond = getBorrowingFactorPerSecond(
        dataStore,
        market,
        prices,
        isLong
    );

    // 获取 old
    uint256 cumulativeBorrowingFactor = getCumulativeBorrowingFactor(dataStore, market.marketToken, isLong);

    // 如上公式所述
    uint256 delta = durationInSeconds * borrowingFactorPerSecond;
    uint256 nextCumulativeBorrowingFactor = cumulativeBorrowingFactor + delta;
    return (nextCumulativeBorrowingFactor, delta, borrowingFactorPerSecond);
}
```

</div>

</div>

2.  获取 borrowingFactorPerSecond

这里比较复杂，总的来说，GMX 借贷费支持两种算法：

- 一种是曲线算法，也就是利用指数函数放大借贷费，资金利用率越高，指数膨胀越快。

- 另一种是双斜率算法，换句话来说是折线分段函数，当资金利用率低于某个阈值，按照平缓斜率收费，超出部分按照陡峭斜率收费。这个算法比较常见。

首先看指数算法：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// e
uint256 borrowingExponentFactor = getBorrowingExponentFactor(dataStore, market.marketToken, isLong);

// r^e
uint256 reservedUsdAfterExponent = Precision.applyExponentFactor(reservedUsd, borrowingExponentFactor);

// r^e / P
uint256 reservedUsdToPoolFactor = Precision.toFactor(reservedUsdAfterExponent, poolUsd);

// b
uint256 borrowingFactor = getBorrowingFactor(dataStore, market.marketToken, isLong);

// r^e / P * b
return Precision.applyFactor(reservedUsdToPoolFactor, borrowingFactor);
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
e = borrowing exponent factor，走配置
r = reserved USD, 其实就是 long/short OI USD
P = pool USD, 池中全部 token 的 USD 价值
b = borrowing factor，配置值
r^e / P * b

这个公式就是常见的指数函数：f(x) = a*x^e
本身 r/P 表达了资金的利用率，但是使用指数放大了 r
```

</div>

</div>

双斜率算法（kink）：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
u = usage factor, 就是 OI / PoolUSD
u_o = optimal usage factor，拐点
b0 = base borrowing factor，基础斜率
b1 = above optimal usage borrowing factor，陡峭斜率差

kink borrowing factor per second = b0 * u

if u > u_o
    kink borrowing factor per second += max(b1 - b0, 0) * (u - u_o) / (1 - u_o)
```

</div>

</div>

------------------------------------------------------------------------

## 4. Pending Borrowing Fee

借贷费用不是实时结算的，但是由于借贷费应当缴纳给池子，因此池子的价值会因为借贷费增长。池子价值本身会影响 LP 的 mint burn 数量，因此 borrow fee 即使没有缴纳，也要纳入计算。这里 GMX 合约统计了未结算的 borrow fee 价值来帮助计算 pool 价值。具体实现方式如下：

`MarketUtils.updateTotalBorrowing` 方法统计了 total borrowing，其逻辑就是采用下面的值更新 datastore 的对应 value：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getNextTotalBorrowing(
    DataStore dataStore,
    address market,
    bool isLong,
    uint256 prevPositionSizeInUsd,
    uint256 prevPositionBorrowingFactor,
    uint256 nextPositionSizeInUsd,
    uint256 nextPositionBorrowingFactor
) internal view returns (uint256) {
    uint256 totalBorrowing = getTotalBorrowing(dataStore, market, isLong);
    // total - prev
    totalBorrowing -= Precision.applyFactor(prevPositionSizeInUsd, prevPositionBorrowingFactor);
    // total + cur
    totalBorrowing += Precision.applyFactor(nextPositionSizeInUsd, nextPositionBorrowingFactor);

    return totalBorrowing;
}

// 整体思路：totalBorrowing 对应了所有的仓位
// 当一个仓位的 size 变更的时候，我们应该把这个仓位最新的 size 更新进去。
// 因此需要先减去 old size 再加上 cur size，其实就是一个 sizeDelta 的概念。
// 至于为什么 size 后面还需要乘以一个最新的 cumulative borrowing factor，见下文。
```

</div>

</div>

`MarketUtils.getTotalPendingBorrowingFees`:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getTotalPendingBorrowingFees(
    DataStore dataStore,
    Market.Props memory market,
    MarketPrices memory prices,
    bool isLong
) internal view returns (uint256) {
    // 获取 OI
    uint256 openInterest = getOpenInterest(
        dataStore,
        market,
        isLong
    );

    // 获取最新的 CumulativeBorrowingFactor
    (uint256 nextCumulativeBorrowingFactor, /* uint256 delta */, ) = getNextCumulativeBorrowingFactor(
        dataStore,
        market,
        prices,
        isLong
    );

    // 查看上文中提到的，记录下来的 total borrowing
    uint256 totalBorrowing = getTotalBorrowing(dataStore, market.marketToken, isLong);

    // OI * CumulativeBorrowingFactor - totalBorrowing
    return Precision.applyFactor(openInterest, nextCumulativeBorrowingFactor) - totalBorrowing;
}

// 整体思路：加减仓操作，先缴纳 borrow fee，再更新 totalBorrowing 字段。
// 于是，在计算 totalPendingBorrowingFees 的时候，需要排掉「先缴纳了」的部分。
// 先简单的理解公式逻辑：
// OI * curCumulativeFactor - totalBorrowing
// 其实逻辑上表达的就类似于 OI * curCumulativeFactor - OI * oldCumulativeFactor
// 这个思路和前面讲解过的 cumulative 机制一致。
// 
// totalBorrowing 的逻辑在上文列出了，结合这里不难看出，实际上这个字段统计的是：
// 最新的需要支付借贷费的部分
// 这么说有点抽象，举个例子：
// 一个 pos 进行加仓，从 100 加到 120U，那么：
// 1. 支付原先 100U 应付的 borrow fee
// 2. totalBorrowing - 100*old_cumulative_fac 这里就清理掉了 1 中付过的钱的部分
// 3. totalBorrowing + 120*new_cumulative_fac 这里就 reset 了一下计费
// 于是计算 pending 的时候，OI*latest_cumulative_factor - totalBorrowing 就对上了
//
// E.g 假设初始时整个单边就我们一个仓位
// 此时 pos_size = 100U, totalBorrowing = 100U * 0(初始因为没有 duration，显然是 0) = 0
// 加仓 20 U
// 1. 支付 100U 持续 n 秒占用的 borrow fee
// 2. 减去 old 部分：totalBorrowing - 100*old_fac => totalBorrowing - 0 = 0
// 3. 加上 new 部分：totalBorrowing += 120*new_fac => 120*new_fac
// 过一段时间，计算 pending：OI * new_new_fac - totalBorrowing
// => 120 * new_new_fac - 120*new_fac
```

</div>

</div>

</div>
