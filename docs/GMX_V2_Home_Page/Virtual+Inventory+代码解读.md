# Virtual Inventory 代码解读

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270780545 {padding: 0px;}
div.rbtoc1772270780545 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270780545 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270780545">

- [1. Swap](#VirtualInventory代码解读-1.Swap)
- [2. Position](#VirtualInventory代码解读-2.Position)

</div>

## 1. Swap

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1772-L1783" class="external-link" rel="nofollow">MarketUtils.getVirtualInventoryForSwaps</a>

通过 market 找到对应的 virtual market，这里需要提前配置好映射关系，也就是说创建一个 ETH/USDC 市场时，需要把这个新建的市场挂靠到一个 virtual market 上，比如专门用于统计类似 \*ETH - USD\* 的市场，后续才能访问到：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
dataStore.getBytes32(Keys.virtualMarketIdKey(market.marketToken))
```

</div>

</div>

## 2. Position

<a href="https://github.com/gmx-io/gmx-synthetics/blob/caf3dd8b51ad9ad27b0a399f668e3016fd2c14df/contracts/market/MarketUtils.sol#L1796-L1803" class="external-link" rel="nofollow">MarketUtils.getVirtualInventoryForPositions</a>

直接查询的 virtual token inventory，不像 swap 一样有市场的概念。因为 swap 的统计概念是 token 数量，而 position 的统计概念是多空力量。

</div>
