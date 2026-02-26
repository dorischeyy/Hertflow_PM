# Vault 页面优化_PRD

<div class="Section1">

<div class="contentLayout2">

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## 1. 变更范围

- **涉及页面:** Vaults Page

- **核心改动:** 将原有的扁平化卡片重构优化，分离信息浏览与交易操作区域，提高信息密度以及优化布局层级。

## 2. UI 优化项详细说明

#### **1. 交互定义**

- 适用模块 **：** 本规则仅适用于详情页的 **APY**、**TVL/Supply**、**Market Exposure** 这三个指标区域的 `?` 图标。

- **触发动作：**

  - **Web 端：** 鼠标悬停图标时显示气泡。

  - **H5 端：** 点击图标显示气泡，点击屏幕空白处关闭。

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="ee12f4e1-caca-40f4-808b-cfe86178db40">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="f24a8bf0-f3fc-4d68-956d-5a935e7a71f0">
<th class="confluenceTh" data-highlight-colour="#efefef" data-local-id="da1c6292-1c41-4e89-ab2f-7f0ad26b3321"><p><strong>字段</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#efefef" data-local-id="82a71b99-b556-4094-9063-0e9dc3b6355f"><p><strong>中文文案</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#efefef" data-local-id="49e5cba1-ee5d-43b5-896f-3fcadae4ca5c"><p><strong>英文文案</strong></p></th>
</tr>
&#10;<tr data-local-id="b84b79cc-670f-4c90-84a3-c3bc28e767a6">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="4d4987dc-1afa-4f1e-9459-733fa00cde34"><p><strong>APY</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="48bdc489-32d2-479a-817d-cbec553da622"><p>基于当前市场费率计算的预估年化收益率。</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="bee2d640-9d6e-47b2-9283-867805c182d0"><p>Estimated annualized yield based on current market rates.</p></td>
</tr>
<tr data-local-id="090b06b9-c6bc-46b1-a4f0-a7996b133c21">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="95dd4297-bc84-48ce-810d-2f32ab2e4999"><p><strong>TVL / Supply</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="5a3af662-02a8-4f93-8f93-b75f85b6bba6"><p><strong>TVL:</strong> 当前策略池中锁定的总资产价值。</p>
<p><strong>Supply:</strong> 当前已铸造的凭证代币 (Vault Tokens) 总数量。</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="0c329040-4bff-4e9b-98f4-a45f9c7393a5"><p><strong>TVL:</strong> Total value of assets locked in this strategy.</p>
<p><strong>Supply:</strong> Total number of vault tokens minted.</p></td>
</tr>
<tr data-local-id="9f63d625-3705-4729-b17d-4e7a8a403ee7">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="17b5fb8f-c622-4f5c-9033-310f366a9d81"><p><strong>Market Exposure</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="078d35ce-7440-44fc-b05c-fad2c3689805"><p>该金库策略所持有的标的资产与代币。</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="546f956c-db33-4c71-aa32-e9df8b445978"><p>The underlying assets and tokens held by this vault strategy.</p></td>
</tr>
</tbody>
</table>

</div>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5c1e2dd30aaebcc4907694f2c0059e63c94f1acc904d7abeec0d8293fa5e8c0a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-031931.png?version=1&amp;modificationDate=1770693574427&amp;cacheVersion=1&amp;api=v2" data-height="563" data-width="382" data-unresolved-comment-count="0" data-linked-resource-id="87392266" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-031931.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="0714f108-9900-499a-8fc7-8cc71342f4c4" data-media-type="file" width="356" height="523" alt="image-20260210-031931.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

2.  **新增持仓展示和CTA 按钮:**

    1.  **视觉布局：**

        - 重构 Your Holdings 区域，取消独立分栏，改为垂直堆叠显示（即数值直接位于标题下方）。

        - 右侧新增 Deposit 按钮，样式为主题色实心。

    2.  **交互逻辑：**

        - 唯一入口： 仅点击 Deposit 按钮可跳转至对应的 Vault 详情页。 卡片的背景及其他非按钮区域不再支持点击跳转。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="752e407e9d7c5c0769b64bebf3f204cb49c0f8f0e347c287de63eddacdae2195" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-032707.png?version=1&amp;modificationDate=1770694031256&amp;cacheVersion=1&amp;api=v2" data-height="562" data-width="389" data-unresolved-comment-count="0" data-linked-resource-id="87392277" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-032707.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="ce833afa-62f1-4a4a-b25f-31a4ca712a6c" data-media-type="file" width="389" height="562" alt="image-20260210-032707.png" /></span>

3.  **圆形进度环：**

- 目标元素: Vault 卡片中Deposited字段右侧的 圆形进度圈。

- 交互动作: 鼠标悬停在圆环区域时显示 Tooltip，移出时消失。H5同理，点击出现Tooltip，点击其他任意地方可以消失。⚠️圆环中间新增数字进度.

- 悬停文案：

  - 中文: 该策略池当前的总资金填充进度。当进度达到 100% 时，将暂停接收新的存款。

  - 英文: The progress of total deposits from all users against the vault's maximum cap.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d583b922a23cc1efdb6c0f068db999d4b0a655db50f1f8c89e841af81e434563" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-032725.png?version=1&amp;modificationDate=1770694049244&amp;cacheVersion=1&amp;api=v2" data-height="562" data-width="390" data-unresolved-comment-count="0" data-linked-resource-id="87293962" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-032725.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="b54e1540-b73f-4a21-995b-7d12c82c4060" data-media-type="file" width="390" height="563" alt="image-20260210-032725.png" /></span>

4.  **新增列表搜索功能：**

    1.  **目标元素：** 功能栏左侧的搜索输入框。

    2.  **交互动作：** 输入字符时实时过滤列表。输入框有内容时右侧显示清除按钮。无匹配结果显示空状态。

    3.  **搜索规则：** 模糊匹配策略名称和底层资产（如 BTC、ETH），不区分大小写。

    4.  **占位文案：**

        - 中文：搜索策略...

        - 英文：Search vaults...

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="56b448ab3a5adce9cbeb4acc7d4bd32b15d9003ffd7c7b7532310645316c01b4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-032819.png?version=1&amp;modificationDate=1770694103129&amp;cacheVersion=1&amp;api=v2" data-height="597" data-width="936" data-unresolved-comment-count="0" data-linked-resource-id="87293969" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-032819.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="ae5ac937-f0ef-4132-877f-7269352005b7" data-media-type="file" width="468" height="298" alt="image-20260210-032819.png" /></span>

5.  **新增列表视图：**

    1.  目标元素: 新增Vaults 页面功能栏右侧 视图切换按钮，为网格/列表图标,展示的各个字段与卡片视图保持一致.

    2.  默认状态: 页面默认以卡片视图展示。

    3.  切换逻辑: 用户点击列表图标后，页面内容区域从卡片网格布局切换为紧凑的 列表行布局 (List View)。再次点击卡片图标可切回原视图。

    4.  交互动作：悬停时会有边框亮起的效果,显示主题色

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a6cbdc373e9f7b929691164ee154094eaa32d286d8cbdba8d8cadee3366ced7f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-032914.png?version=1&amp;modificationDate=1770694157667&amp;cacheVersion=1&amp;api=v2" data-height="573" data-width="906" data-unresolved-comment-count="0" data-linked-resource-id="87359500" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-032914.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="826bc4cb-bb1a-4576-9d0c-ba0048e1b6ae" data-media-type="file" width="468" height="296" alt="image-20260210-032914.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6e0c91bdfa43d466961e89d495f9aa96428107ba098c695d1d0278f861e7d775" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260210-033014.png?version=1&amp;modificationDate=1770694217166&amp;cacheVersion=1&amp;api=v2" data-height="603" data-width="948" data-unresolved-comment-count="0" data-linked-resource-id="87425035" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260210-033014.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="ec831dee-6a30-4f68-ba6d-d94aa853e79d" data-media-type="file" width="468" height="297" alt="image-20260210-033014.png" /></span>

6.  **新增排序功能**（卡片和列表视图皆有）

    1.  **列表排序功能：**

        **目标元素：** 功能栏右侧的排序下拉菜单。

        **交互动作：**

        - **默认状态：** 默认为按 APY 降序排列。

        - **展开与选择：** 点击按钮展开下拉菜单，选中任一选项后，列表区域根据对应规则立即重新排序。点击菜单外部区域或再次点击按钮可收起菜单。

        **排序规则：**

        - **APY High to Low：** 按策略的年化收益率数值进行降序排列（数值越大越靠前）。

        - **TVL High to Low：** 按策略的总锁仓量美元价值进行降序排列（TVL越大越靠前）。

## Out of Scope

允许用户根据其持有的或计划存入的特定资产类型（如 USDT, ETH, BTC 等），对 Vaults（策略）列表进行筛选，以便快速定位到支持该资产的投资标的。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="164bbb9a333198c686682ec0dc62fd538c7afb45556e53b42aab759646619ac1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/85098501/image-20260206-080115.png?version=1&amp;modificationDate=1770364889617&amp;cacheVersion=1&amp;api=v2" data-height="294" data-width="540" data-unresolved-comment-count="0" data-linked-resource-id="85426196" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20260206-080115.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="85098501" data-linked-resource-container-version="7" data-media-id="326a88d7-638b-4dec-8350-6a9e2db398fd" data-media-type="file" width="468" height="254" alt="image-20260206-080115.png" /></span>

- **入口位置：** 位于 Vault 列表页顶部功能栏右侧，搜索框 (Search vaults) 旁边。

- **默认状态：**

  - 按钮文案显示 Deposit Asset。

  - 默认选中 All Assets（即展示所有策略）。

  - 左侧带有一个调节/筛选的图标。

- **操作流程：**

  1.  用户点击 Deposit Asset 按钮。

  2.  向下展开下拉菜单，选项列表包含：`All Assets`（置顶）, `USDT`, `USDC`, `BTC`, `ETH` 等。

  3.  用户点击任意单一选项。

  4.  下拉菜单收起，列表区域自动刷新，仅展示支持该存款资产的 Vault 卡片。

</div>

</div>

</div>

</div>

</div>
