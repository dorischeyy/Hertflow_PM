# 特殊需求以及 GMX 对应改造点

<div class="Section1">

**<u>需求：</u>**

系统级强制 PnL 机制（+2500% TP / –80% SL）：+2500% TP 为针对**所有仓位**的强制止盈，相当于强平线。-80%SL为**提交止损单**才有的限制，相当于止损价格边界。

**<u>确认点</u>**<u>：</u>

- <span class="placeholder-inline-tasks">盈利不超过保证金 25 倍需强制实现</span>
  - <span class="placeholder-inline-tasks">强制止盈的方式为平仓，而非部分减仓（类ADL）</span>
- <span class="placeholder-inline-tasks">止损不超过 -80% 不强制实现</span>

> 用户可以在提交一个小的止损单后，立马提取仓位的保证金，变向的绕过了-80%止损，因此这里不强制实现，可能是前端的一个限制。

**<u>实现方式：</u>**

25倍盈利监控由 Keeper 实现，触发条件时，由 Keeper 提交平仓请求。

当前对于 `Liquidation Order` ，合约会校验仓位是否可以平仓，用户盈利时显然校验会失败。因此需要新增一个 `order type`，用于绕过 `isPositionLiquidatable` 校验，除此之外一切参数同原 Liquidation 即可：

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3ef5a8f2df098734b9da249acf9f862442cd86f2eda687a9eb3928365f71201a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/50364649/image-20251208-100346.png?version=1&amp;modificationDate=1765188230409&amp;cacheVersion=1&amp;api=v2" data-height="1791" data-width="1879" data-unresolved-comment-count="0" data-linked-resource-id="50430195" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251208-100346.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="50364649" data-linked-resource-container-version="2" data-media-id="805cbbd3-4872-4ac8-945d-a0d5b4762f6b" data-media-type="file" width="468" height="446" alt="image-20251208-100346.png" /></span>

------------------------------------------------------------------------

</div>
