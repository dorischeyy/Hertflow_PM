# Funding Fee 代码解读

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270796844 {padding: 0px;}
div.rbtoc1772270796844 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270796844 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270796844">

- [1. Funding Fee 如何计算？](#FundingFee代码解读-1.FundingFee如何计算？)
- [2. Funding Fee Rate 如何计算？](#FundingFee代码解读-2.FundingFeeRate如何计算？)
- [3. Funding Fee 何时更新？](#FundingFee代码解读-3.FundingFee何时更新？)
- [4. Funding Fee 如何提取？](#FundingFee代码解读-4.FundingFee如何提取？)

</div>

## 1. Funding Fee 如何计算？

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/market/MarketUtils.sol#L1916C5-L1941C6" class="external-link" rel="nofollow">MarketUtils.getFundingAmount</a>

算法比较简单，在计算时直接求两次 cumulativeFundingFactor 差值乘以 position size 即可。

因为这里的 factor 已经抽象成了 per size 的概念。

------------------------------------------------------------------------

## 2. Funding Fee Rate 如何计算？

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1261-L1385" class="external-link" rel="nofollow">MarketUtils.getNextFundingFactorPerSecond</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
F = funding factor per second
L = Long open interest
S = Short open interest
e = Funding exponent factor

Fi = Funding increase factor per sec
Fd = Funding decrease factor per sec
F_min = min funding factor per sec
F_max = max funding factor per sec
F_market = Funding factor for this market

f = |L - S| ^ e / (L + S)

if Fi = 0
   F = min(f * F_market, F_max)

F0 = Saved funding factor per second
F0 > 0 = longs pay shorts
F0 < 0 = shorts pay longs

Ts = Threshold for stable funding
Td = Threshold for decrease funding

if (F0 > 0 and L > S) or (F0 < 0 and L < S)
   if f > Ts
      increase funding rate
   else if f < Td
      decrease funding rate
else
   increase funding rate

if funding rate increase
   F = F0 +/- f * Fi * dt (sign depends on direction of next funding)

if funding rate decrease
   if |F0| <= Fd * dt
      F = F0 / |F0|
   else
      F = (|F0| - Fd * dt) * F0 / |F0|

s = F / |F|
F = s * min(|F|, F_max)
F = s * max(|F|, F_min)
```

</div>

</div>

这个算法看起来极其复杂，下面分步进行解释：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
提示：小写的 f 理解为失衡比例 factor，动态计算得到的；大写的 F_? 都是配置。

-----------------------------------------------------

1. 计算失衡程度
f = |L - S| ^ e / (L + S)
这里用指数放大了失衡比例。如果完全平衡，则 L == S，f = 0。

-----------------------------------------------------

2. 情况 1（静态算法）
if Fi = 0
   F = min(f * F_market, F_max)
这里的含义是，资金费率不进行动态调整，直接让资金费率 = 失衡程度 x 基准费率去计算（不超过上限）。
这里可以提前返回，作为计算的一个分支（静态算法）。

-----------------------------------------------------

// 接下来进入情况 2 动态算法，动态的调整资金费率

-----------------------------------------------------

3. 判断费用方向
F0 > 0  → 多头支付空头
F0 < 0  → 空头支付多头
F0 是上次记录的 F，通过正负判断流向，和 CEX 一致。

-----------------------------------------------------

4. 判断是否需要上调或下调资金费率，这里是动态算法的一个关键点
if (F0 > 0 and L > S) or (F0 < 0 and L < S)
   if f > Ts
      increase funding rate
   else if f < Td
      decrease funding rate
else
   increase funding rate
- 当资金费率方向（F0 正负）与市场失衡方向一致时：
  - 如果失衡还在扩大（f > Ts），就继续增加资金费率；
  - 如果市场回归平衡（f < Td），就降低资金费率。
- 否则（方向反了，比如多头多但当前是空头付费），就立即增加资金费率（反转）。

-----------------------------------------------------

5. 开始调整资金费率

如果是上调：
F = F0 ± f * Fi * dt
- 符号取决于谁在付费（方向与下一轮一致）。
- Fi * dt 控制上调速率。
- f 控制调整幅度——失衡越大，变化越快。

反之则下调：
if |F0| <= Fd * dt。   // 下调的幅度，超出了当前存在的费率，资金费还是要收，不能免掉
   F = F0 / |F0|       // 因此方向不变的同时，归一，后续有区间调整
else
   F = (|F0| - Fd * dt) * F0 / |F0| 后面这个 'F0 / |F0|' 也是计算方向而已

-----------------------------------------------------

6. 区间 cap
s = F / |F|
F = s * min(|F|, F_max)
F = s * max(|F|, F_min)
限制结果在区间内，同时保留符号。
```

</div>

</div>

注意，上面计算的 F 是 funding rate per second。

- 拿这个 F \* duration 计算出 funding USD，也就是资金费总额

- 再用 funding USD / OI，就计算出了 funding factor per size。（因为资金费是方向上所有仓位共享，因此转化为 factor per size 才能计算每个仓位分别应该支付多少费用）。

基于上面的考虑，结合实际情况，其实我们会得到 4 个值，因为 GMX 做多，可以用 market.LongToken 来做，也可以用 ShortToken 来做，因此我们有 2 方向 \* 2 token = 4个 factor_per_size 值。具体代码看这里：<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/market/MarketUtils.sol#L1323C5-L1483C6" class="external-link" rel="nofollow">MarketUtils.getNextFundingAmountPerSize</a>。

同样的，计算了应该 pay 多少 funding fee，还会对应的记录对手方可以 claim 多少 funding fee。因此在上面的代码中，有 8 个 factor per size (4 pay + 4 claim)。当然，每次计算，方向是确定的，要么多头支付，要么空头支付，因此每次会更新 4 个 factor per size ( pay long → claim long, pay short → claim short)。

也就是说，在多pay空的情况下，用 long token 做多的人，需要支付 long token，否则支付 short token；对于空头来说，他们按照自己仓位所占的份额，可以同时 claim long && short token。

------------------------------------------------------------------------

## 3. Funding Fee 何时更新？

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExecuteOrderUtils.executeOrder
├─ PositionUtils.updateFundingAndBorrowingState (update funding fee)
│  └─ MarketUtils.updateFundingState
└─ processOrder
   └─ IncreaseOrderUtils.processOrder
      └─ IncreasePositionUtils.increasePosition
         ├─ if position.sizeInUsd = 0 (set funding fee to latest for new position)
         │   ├─ position.setFundingFeeAmountPerSize
         │   ├─ position.setLongTokenClaimableFundingAmountPerSize
         │   └─ position.setShortTokenClaimableFundingAmountPerSize
         ├─ processCollateral
         │   └─ PositionPricingUtils.getPositionFees
         │      ├─ MarketUtils.getFundingFeeAmountPerSize (get latest funding fees for position)
         │      ├─ MarketUtils.getClaimableFundingAmountPerSize
         │      ├─ MarketUtils.getClaimableFundingAmountPerSize
         │      └─ getFundingFees (calculate funding fees and claimable fees)
         │         ├─ MarketUtils.getFundingAmount
         │         ├─ MarketUtils.getFundingAmount
         │         └─ MarketUtils.getFundingAmount
         ├─ position.setCollateralAmount
         ├─ PositionUtils.incrementClaimableFundingAmount (store claimable funding fees)
         │   └─ MarketUtils.incrementClaimableFundingAmount
         ├─ position.setFundingFeeAmountPerSize (update funding fees to latest)
         ├─ position.setLongTokenClaimableFundingAmountPerSize
         └─ position.setShortTokenClaimableFundingAmountPerSize

ExecuteOrderUtils.executeOrder
├─ PositionUtils.updateFundingAndBorrowingState (update funding fee)
│  └─ MarketUtils.updateFundingState
└─ processOrder
   └─ DecreaseOrderUtils.processOrder
      └─ DecreasePositionUtils.decreasePosition
         ├─ DecreasePositionCollateralUtils.processCollateral
         │   └─ PositionPricingUtils.getPositionFees
         ├─ position.setCollateralAmount
         ├─ PositionUtils.incrementClaimableFundingAmount
         ├─ position.setFundingFeeAmountPerSize
         ├─ position.setLongTokenClaimableFundingAmountPerSize
         └─ position.setShortTokenClaimableFundingAmountPerSize

MarketUtils.updateFundingState
├─ getNextFundingAmountPerSize
│  ├─ getOpenInterest
│  ├─ getOpenInterest
│  ├─ getOpenInterest
│  ├─ getOpenInterest
│  ├─ getSecondsSinceFundingUpdated
│  ├─ getNextFundingFactorPerSecond
│  ├─ getFundingAmountPerSizeDelta
│  ├─ getFundingAmountPerSizeDelta
│  ├─ getFundingAmountPerSizeDelta
│  └─ getFundingAmountPerSizeDelta
├─ applyDeltaToFundingFeeAmountPerSize
├─ applyDeltaToClaimableFundingAmountPerSize
└─ setSavedFundingFactorPerSecond
```

</div>

</div>

------------------------------------------------------------------------

## 4. Funding Fee 如何提取？

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ExchangeRouter.claimFundingFees
└─ for loop for each market
   └─ MarketUtils.claimFundingFees
      ├─ Keys.claimableFundingAmountKey(market, token, account);
      ├─ DataStore.getUint(key)
      ├─ DataStore.setUint(key, 0)
      ├─ DataStore.decrementUint
      └─ MarketToken.transferOut
```

</div>

</div>

</div>
