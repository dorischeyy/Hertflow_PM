# ADL 代码解读

<div class="Section1">

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

本质上来说核心的 ADL 监控和发起请求策略，都在链下由 keeper 维护。

合约本身只做了一些基本的校验：

1.  是否开启了这个 feature？

2.  当前池子的 pnl 是否超出了阈值？

校验通过后，底层调用 decreasePosition 进行减仓。

</div>

</div>

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/exchange/AdlHandler.sol#L76C1-L164C2" class="external-link" rel="nofollow">AdlHandler.executeAdl</a>

Keeper 走这里交互。

<a href="https://github.com/gmx-io/gmx-synthetics/blob/7c502568117500181b3e8ce5520e95402c6102d6/contracts/market/MarketUtils.sol#L3049C5-L3068C6" class="external-link" rel="nofollow">MarketUtils.isPnlFactorExceeded</a>

这里校验池子盈利是否过多。算法是用 OI（in tokens）\* price 计算 USD，然后除以 poolUSD 计算出比例，与配置的阈值比例进行比较。

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/adl/AdlUtils.sol#L127C5-L205C6" class="external-link" rel="nofollow">AdlUtils.createAdlOrder</a>

底层调用这里创建订单。订单随后会被视为 decreaseOrder 进行处理。

</div>
