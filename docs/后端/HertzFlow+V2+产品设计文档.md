# HertzFlow V2 产品设计文档

<div class="Section1">

# 概述

1.  核心功能点：

    1.  支持纯usdc池子

    2.  支持 虚拟资产标的，rwa交易

    3.  支持 referrals

# 产品架构

## herzflow 稳定币池子架构

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b5762880e1872411b319fbd061514f2c436626eccf00b443b15bf81abb8ffa29" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/27787284/image-20251030-120513.png?version=1&amp;modificationDate=1761825918981&amp;cacheVersion=1&amp;api=v2" data-height="796" data-width="1230" data-unresolved-comment-count="0" data-linked-resource-id="27721765" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251030-120513.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="27787284" data-linked-resource-container-version="5" data-media-id="ad687bf1-84ab-422d-978a-dec1b1de19b0" data-media-type="file" width="468" height="303" alt="image-20251030-120513.png" /></span>

1.  每个gm pool都被视为是一个单独的market。单个market包含\[index,long-collateral,short-collateral,pool-address\]作为特征参数。

2.  每个可交易标的（index）可以选择使用不同market的流动性。每个market只能绑定到一个index上。

3.  每个gm pool可支持灵活的多空保证金币种选择，例如：USDC-USDC（纯u池子），ETH-stETH（不同封装跨链资产池子），或者是 BNB-USDC。

4.  对GLV池子来说，他实质上是针对GM pool的灵活vault。他负责调配资金去gm pool。单个GLV所能存入的gm pool需要考虑到兼容性。例如，存入资产为BNB、USDC的<span class="inline-comment-marker" ref="b92d48eb-b192-4519-a87a-81b3fdcfd805">GLV池子</span>，只能存入 多空保证金为 BNB-BNB，USDC-USDC，BNB-USDC这三种组合的GM 池子去获取收益。

5.  GLV存在三种操作，deposit，withdraw，shift。

    1.  deposit：存入资金到GM 池子

    2.  withdraw：从GM池子提取资金。

    3.  shift：从A GM池子提取流动性，存入B GM 池子。

6.  index 的创建，主要取决于预言机以及keeper的对接。理论上，对于同一资产的不同预言机报价，会产生多个index。例如：对于BTC/USD交易对，会存在BTC/USD-chainlink index以及BTC/USD-pyth index。这个创建操作，在V2版本上，只能由hertzflow协议方管理。

# oracle

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b194eeb553b012deb84afa2db7d30af2c015a2a26e07b4b69a86289a2ee66f5c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/27787284/image-20251030-154221.png?version=1&amp;modificationDate=1761838947753&amp;cacheVersion=1&amp;api=v2" data-height="786" data-width="1130" data-unresolved-comment-count="0" data-linked-resource-id="28246019" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251030-154221.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="27787284" data-linked-resource-container-version="5" data-media-id="6fe51e36-a4a9-4cea-b787-fba68313acbf" data-media-type="file" width="468" height="325" alt="image-20251030-154221.png" /></span>

# 自主建池

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7913fd88e3329b43ee64b0277badc181ba3c21e437cb4f02205e75708bb60660" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/27787284/image-20251030-160148.png?version=1&amp;modificationDate=1761840113459&amp;cacheVersion=1&amp;api=v2" data-height="766" data-width="1085" data-unresolved-comment-count="0" data-linked-resource-id="28278787" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251030-160148.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="27787284" data-linked-resource-container-version="5" data-media-id="06829ab4-bb3a-4073-9f38-6ab1e10a27b8" data-media-type="file" width="468" height="330" alt="image-20251030-160148.png" /></span>

1.  curator 向协议方发起 oracle 创建请求。

2.  curator需要自行搭建oracle的链下设施，以及符合协议oracle定义标准的喂价合约。

3.  协议方审核后，安排keeper对接，以及oracle 聚合合约对接。同时，curator需要质押一定量的bnb/hz到保证金池。

4.  在完成对接后，协议方将会开放对应的oracle到前端网页<u>可供在gm创建页面中选择。</u>

5.  curator可以自行发起market（gm pool）创建请求，并选择对应的自定义oracle作为标的的价格来源。

6.  在该创建请求中，包含以下参数：

    1.  多空保证金币种。

    2.  gm 池子配置参数，包括 最大杠杆，维持保证金率，swap费率，开平仓费率。

7.  在完成该池子创建后，其他用户可以向池子内自由存入资金。

## 创建 自定义oracle

1.  

</div>
