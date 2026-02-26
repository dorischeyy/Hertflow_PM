# 需求池Backlog

<div class="Section1">

<div class="contentLayout2">

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

> 简要记录可迭代功能，在整体没问题后，测试网阶段进行功能迭代

# **Trade页**

## Wallet Ops

一键交易账户 - 用户转usdc用于交易 以及 bnb作为手续费 → 协议创建托管钱包 （avantsi用pin+EOA - 私钥可导出；而GMX用SCA 智能合约钱包 + 付费节点）

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d397abf0833a5c4305089eca71aa6d09fd483701fed53f5228ccbdd7ca29ee28" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-09%20at%2016.32.27.png?version=1&amp;modificationDate=1768187324847&amp;cacheVersion=1&amp;api=v2" data-height="511" data-width="528" data-unresolved-comment-count="0" data-linked-resource-id="66748422" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-09 at 16.32.27.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="bd106354-c14d-49d1-827f-b4eef8eab141" data-media-type="file" width="165" height="159" alt="Screenshot 2026-01-09 at 16.32.27.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ac42debe4a38ae30cb9bd5a580f7883f2c21e6e4bd1a2d58eab8684cd354b8ef" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-09%20at%2016.32.49.png?version=1&amp;modificationDate=1768187324918&amp;cacheVersion=1&amp;api=v2" data-height="397" data-width="582" data-unresolved-comment-count="0" data-linked-resource-id="66748429" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-09 at 16.32.49.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="1496018f-b10a-459d-b89a-0cfaa42f63b4" data-media-type="file" width="165" height="112" alt="Screenshot 2026-01-09 at 16.32.49.png" /></span>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b52a90e4fde26f599d7fc5de6e84c4a0cbf370aef49f7d8bb83153a390ca9187" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-09%20at%2016.34.34.png?version=1&amp;modificationDate=1768187324952&amp;cacheVersion=1&amp;api=v2" data-height="686" data-width="386" data-unresolved-comment-count="0" data-linked-resource-id="66748435" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-09 at 16.34.34.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="a5f4c194-44c4-480b-9351-22d4d7a0e3f3" data-media-type="file" width="169" height="299" alt="Screenshot 2026-01-09 at 16.34.34.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## **图表**

</div>

</div>

</div>

<div class="columnLayout three-equal" layout="three-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**Depth Chart**

- 模拟订单部深度图以及对应买卖造成的价格冲击。

- 本质上是price impact函数演变的，x轴为执行价格，中线在预言机价格。y轴为size delta

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="032fb51a90ae9250c1739c7514e11f52f7357d7960a65e9ec3cf7617fe5e486f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-08%20at%2017.48.11.png?version=1&amp;modificationDate=1768187250317&amp;cacheVersion=1&amp;api=v2" data-height="492" data-width="908" data-unresolved-comment-count="0" data-linked-resource-id="66781193" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-08 at 17.48.11.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="07900044-8eb0-4720-8b67-6a3365ad313a" data-media-type="file" width="154" height="83" alt="Screenshot 2026-01-08 at 17.48.11.png" /></span>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

**1h Net Rate 历史**

- 图表展示funding + borrow之和

- 浮窗跟随鼠标展示子项：funding，borrow

- 可用其他颜色线条展示其他交易所funding，方便对冲套利

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="34eedfee5918ae5b6f657560b2d512690f7241263caba354569cf6235edc09fa" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-08%20at%2017.39.19.png?version=1&amp;modificationDate=1768187250348&amp;cacheVersion=1&amp;api=v2" data-height="595" data-width="800" data-unresolved-comment-count="0" data-linked-resource-id="66781200" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-08 at 17.39.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="04e55175-eb77-4bae-8c70-30eb62cf55e8" data-media-type="file" width="468" height="348" alt="Screenshot 2026-01-08 at 17.39.19.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="725137914a3a69248f73d915b3f44c7931e4c6ceac7534cb00135fd65c81acde" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-08%20at%2017.34.20.png?version=1&amp;modificationDate=1768187250387&amp;cacheVersion=1&amp;api=v2" data-height="985" data-width="1442" data-unresolved-comment-count="0" data-linked-resource-id="66781206" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-08 at 17.34.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="e1da8200-70ec-4631-94d8-ac4337da85a6" data-media-type="file" width="468" height="319" alt="Screenshot 2026-01-08 at 17.34.20.png" /></span>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

**市场配置表**

- 展示与产品相关的合约配置参数

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="af010894711ee027b73853bb0495308bbb3471b3b03ac603daecdd28165c924d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-08%20at%2017.39.45.png?version=1&amp;modificationDate=1768187250402&amp;cacheVersion=1&amp;api=v2" data-height="765" data-width="799" data-unresolved-comment-count="0" data-linked-resource-id="66781212" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-08 at 17.39.45.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="ec4e9661-6b2c-42ec-85c2-e983ace9c753" data-media-type="file" width="442" height="423" alt="Screenshot 2026-01-08 at 17.39.45.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

# Pool页

## Onboarding

**新手引导侧边栏 - 前置条件：docs写完**

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="cb6146cfccccd8b23e186eca7ea4d2b73579c80a7b93f6cea69efe673fa5f4f1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-12%20at%2018.15.49.png?version=1&amp;modificationDate=1768213094091&amp;cacheVersion=1&amp;api=v2" data-height="1000" data-width="1786" data-unresolved-comment-count="0" data-linked-resource-id="67010615" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-12 at 18.15.49.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="28555468-fac0-4957-b304-fe0ccb0d88d6" data-media-type="file" width="356" height="199" alt="Screenshot 2026-01-12 at 18.15.49.png" /></span>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="95c98e4b40428e89833e8f5486789f23a128f74ea0eb7ec44a76c1521db27686" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/66617371/Screenshot%202026-01-12%20at%2018.15.36.png?version=1&amp;modificationDate=1768213107254&amp;cacheVersion=1&amp;api=v2" data-height="847" data-width="1183" data-unresolved-comment-count="0" data-linked-resource-id="66617422" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-12 at 18.15.36.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="66617371" data-linked-resource-container-version="2" data-media-id="0eb4f788-9ed6-4692-b719-baf21c5549b9" data-media-type="file" width="356" height="255" alt="Screenshot 2026-01-12 at 18.15.36.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

</div>

</div>

</div>

</div>

</div>
