# Trade 超高杠杆模式_PRD

<div class="Section1">

<div class="contentLayout2">

<style>[data-colorid=kb38vra0s9]{color:#ff5630} html[data-color-mode=dark] [data-colorid=kb38vra0s9]{color:#cf2600}[data-colorid=bvol0o3uyn]{color:#ff5630} html[data-color-mode=dark] [data-colorid=bvol0o3uyn]{color:#cf2600}[data-colorid=fhkdoas69n]{color:#ff5630} html[data-color-mode=dark] [data-colorid=fhkdoas69n]{color:#cf2600}[data-colorid=jgjp05qivk]{color:#ff5630} html[data-color-mode=dark] [data-colorid=jgjp05qivk]{color:#cf2600}[data-colorid=vl7r43kje0]{color:#ff5630} html[data-color-mode=dark] [data-colorid=vl7r43kje0]{color:#cf2600}[data-colorid=dfyxrgjnk2]{color:#36b37e} html[data-color-mode=dark] [data-colorid=dfyxrgjnk2]{color:#4cc994}[data-colorid=ald9vvgzuo]{color:#ff5630} html[data-color-mode=dark] [data-colorid=ald9vvgzuo]{color:#cf2600}[data-colorid=ss7hv96vdg]{color:#ff5630} html[data-color-mode=dark] [data-colorid=ss7hv96vdg]{color:#cf2600}[data-colorid=gm24wlcub2]{color:#ff5630} html[data-color-mode=dark] [data-colorid=gm24wlcub2]{color:#cf2600}[data-colorid=v64k1nd0pu]{color:#36b37e} html[data-color-mode=dark] [data-colorid=v64k1nd0pu]{color:#4cc994}[data-colorid=nbjriuco8m]{color:#ff5630} html[data-color-mode=dark] [data-colorid=nbjriuco8m]{color:#cf2600}[data-colorid=e9klo6knxl]{color:#ff5630} html[data-color-mode=dark] [data-colorid=e9klo6knxl]{color:#cf2600}[data-colorid=b63w98d4ma]{color:#36b37e} html[data-color-mode=dark] [data-colorid=b63w98d4ma]{color:#4cc994}[data-colorid=ppq4neo0lr]{color:#ff5630} html[data-color-mode=dark] [data-colorid=ppq4neo0lr]{color:#cf2600}[data-colorid=kj7xazfdi8]{color:#ff5630} html[data-color-mode=dark] [data-colorid=kj7xazfdi8]{color:#cf2600}[data-colorid=tfqfqsojg6]{color:#ff5630} html[data-color-mode=dark] [data-colorid=tfqfqsojg6]{color:#cf2600}[data-colorid=lzv4b4jvi0]{color:#ff5630} html[data-color-mode=dark] [data-colorid=lzv4b4jvi0]{color:#cf2600}[data-colorid=qpy92qxymk]{color:#ff5630} html[data-color-mode=dark] [data-colorid=qpy92qxymk]{color:#cf2600}[data-colorid=n4xi3ytemv]{color:#ff5630} html[data-color-mode=dark] [data-colorid=n4xi3ytemv]{color:#cf2600}[data-colorid=d4rr1p6fis]{color:#ff5630} html[data-color-mode=dark] [data-colorid=d4rr1p6fis]{color:#cf2600}[data-colorid=msblwswx8u]{color:#ff5630} html[data-color-mode=dark] [data-colorid=msblwswx8u]{color:#cf2600}[data-colorid=oq00gyrj43]{color:#36b37e} html[data-color-mode=dark] [data-colorid=oq00gyrj43]{color:#4cc994}[data-colorid=p224szh93j]{color:#ff5630} html[data-color-mode=dark] [data-colorid=p224szh93j]{color:#cf2600}</style>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

## 一、需求背景

**前置需求：**<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/41713689/Trade+Page_PRD" data-linked-resource-id="41713689" data-linked-resource-version="33" data-linked-resource-type="page">Trade页PRD</a>

**核心逻辑：**

> 详见：<a href="https://hertzflow.atlassian.net/wiki/x/IwFMAw" data-card-appearance="inline" data-local-id="904de680-18f8-444a-8c92-d367a0e4efe3" rel="nofollow">https://hertzflow.atlassian.net/wiki/x/IwFMAw</a>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="69c4f40f-ee2b-4ae3-a715-ee9dccbc04c1">
<tbody>
<tr data-local-id="76204682-13b9-42e7-a99a-07a318d870d8">
<th class="confluenceTh" data-local-id="5ff54308-306d-482b-b5ae-e1bd7e14a28e"><p>校验项</p></th>
<th class="confluenceTh" data-local-id="e4cd6169-0be0-43ab-8428-a9ca1af3da71"><p>Normal模式</p></th>
<th class="confluenceTh" data-local-id="3a4a38cc-0042-45d8-a30d-f09b68a3d495"><p>Hyper模式</p></th>
</tr>
&#10;<tr data-local-id="e4150fef-0f8c-493c-9f8a-f1a6a3316867">
<td class="confluenceTd" data-local-id="8f8016ef-3003-4de8-a02f-d9c08137ba1b"><p><strong>杠杆范围</strong></p></td>
<td class="confluenceTd" data-local-id="7d19a09b-27ba-4fd6-8b95-fd49571632be"><p>1.1x ≤ Lev ≤ Max Lev Normal</p>
<blockquote>
<p>e.g. PEPE/USD: 1x - 20x</p>
</blockquote></td>
<td class="confluenceTd" data-local-id="818fbdb2-80b3-46ce-8a09-e4e69b2d4174"><p>Min Lev Hyper ≤ Lev ≤ Max Lev Hyper</p>
<blockquote>
<p>e.g. PEPE/USD: 75x - 100x</p>
</blockquote></td>
</tr>
<tr data-local-id="63d5c5d9-e5c3-4bdd-be9e-c77c8ce89b31">
<td class="confluenceTd" data-local-id="bcd8c8d3-47e7-444f-bbba-3c020728a886"><p><strong>最小开仓size</strong></p></td>
<td class="confluenceTd" data-local-id="21ad9c78-5873-4026-a406-0fa4075a0ad9"><p>无特殊限制</p></td>
<td class="confluenceTd" data-local-id="c50f655c-6d12-4fbb-8adb-58bdb0c5600a"><p>Position Size ≥ Min Position Size</p>
<p>市场级配置</p></td>
</tr>
<tr data-local-id="d5b7ed52-e8fc-4d4a-9612-eff9b8a19de9">
<td class="confluenceTd" data-local-id="6b96f699-71da-43f2-aedc-203b0777042d"><p><strong>订单类型</strong></p></td>
<td class="confluenceTd" data-local-id="860320c1-77f5-4be9-bc37-1224137c9372"><p>市价单 + 限价单</p></td>
<td class="confluenceTd" data-local-id="5f9ed8d9-5e01-47ad-a995-c01fc56c7eb0"><p><strong>仅</strong>市价单</p></td>
</tr>
<tr data-local-id="6ca62514-eada-4b2b-b38f-61c42be2a49c">
<td class="confluenceTd" data-local-id="52981e44-f7cf-4da0-9e50-c8eaccb95761"><p><strong>止盈上限</strong></p>
<p><strong>（all）</strong></p></td>
<td class="confluenceTd" data-local-id="4de2a592-ef6a-4c3e-b5b3-9eeb46bbaea7"><p><strong>单边</strong> PnL% ≤ Profit% Cap</p>
<blockquote>
<p>e.g. PnL% ≤ 2500%</p>
</blockquote></td>
<td class="confluenceTd" data-local-id="ae3cea0e-1a7a-4932-a1a6-568abb48ba5c"><p><strong>单边</strong> PnL% ≤ Profit% Cap</p>
<blockquote>
<p>e.g. PnL% ≤ 2500%</p>
</blockquote></td>
</tr>
<tr data-local-id="53ae5fce-767d-44b6-94c2-b13aac8978c0">
<td class="confluenceTd" data-local-id="0c7d82d1-b194-4580-b081-8d42c5e9c388"><p><strong>止损范围</strong></p>
<p><strong>（SL only）</strong></p></td>
<td class="confluenceTd" data-local-id="0b7831ea-a4e3-4b3e-9734-3e9032db328f"><p><strong>单边</strong> PnL% ≥ Max Loss%</p>
<blockquote>
<p>e.g. -80% ≤ PnL%</p>
</blockquote></td>
<td class="confluenceTd" data-local-id="e9dbc843-1c27-4bb6-b099-aff5e645297f"><p><strong>双边</strong> Max Loss% ≤ PnL% ≤ Min Loss%</p>
<blockquote>
<p>e.g. -80% ≤ PnL% ≤ -30%</p>
</blockquote></td>
</tr>
<tr data-local-id="31742d43-00b8-4905-9e8b-2a7ae36cf77a">
<td class="confluenceTd" data-local-id="4ea3e7e0-a67b-4ac3-9f45-e8f80ae97035"><p><strong>加减仓操作</strong></p></td>
<td class="confluenceTd" data-local-id="9364a8e6-4e9e-4fa0-a764-6c8829397747"><p>同模式下合并，Hyper &amp; Normal仓位<strong>隔离</strong></p></td>
<td class="confluenceTd" data-local-id="6e175da0-d21c-4074-b355-1cbdff7b064c"><p>同模式下合并，Hyper &amp; Normal仓位<strong>隔离</strong></p></td>
</tr>
<tr data-local-id="a67470b0-6ab2-4e3f-be28-9f312e668cc1">
<td class="confluenceTd" data-local-id="12f1b630-8139-46e3-85ee-b0a7ced3a7b5"><p><strong>保证金操作</strong></p></td>
<td class="confluenceTd" data-local-id="c73580e8-3cb9-4a8b-af40-8921f968e117"><p>增：Lev ≥ 1.1</p>
<p>减：Lev ≤ Max Lev Normal；Residual Collateral ≥ 10 USDC</p></td>
<td class="confluenceTd" data-local-id="41614cc0-9b66-4ed7-8f26-63d341ab29bd"><p>增：Lev ≥ Min Lev Hyper</p>
<p>减：Disabled</p></td>
</tr>
<tr data-local-id="a75fcd59-ccf2-4646-84a5-285ad5e4b806">
<td class="confluenceTd" data-local-id="6416f4b0-5282-4d2c-ad6c-69c3b53b23da"><p><strong>收费模型</strong></p></td>
<td class="confluenceTd" data-local-id="2f3a8554-5e94-4a18-89e9-b80a0f6e10e2"><p>open/close/borrow/funding</p>
<p>liq/price impact</p>
<p><strong>损失返还：</strong>针对订单执行开仓时，OI弱势方的仓位，其损失部分，返还Loss Rebate = Loss * LossRebateFactor</p></td>
<td class="confluenceTd" data-local-id="b7280563-8c45-4f2e-906e-73c3445218af"><p>open/close/borrow = 0 其他照收</p>
<p><strong>盈利抽成：</strong>针对盈利部分抽成 Fee = Profit * ProfitShareFactor</p></td>
</tr>
</tbody>
</table>

</div>

**止盈止损校验边界：**

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ade85ace2facfc0f8f51e16aad3f694152013d09b53ac03e66d773f7a8333bf1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2019.10.54.png?version=1&amp;modificationDate=1766747739511&amp;cacheVersion=1&amp;api=v2" data-height="571" data-width="785" data-unresolved-comment-count="0" data-linked-resource-id="61178323" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 19.10.54.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="23217b73-e328-4c70-8890-b8515f782ba6" data-media-type="file" width="438" height="318" alt="Screenshot 2025-12-26 at 19.10.54.png" /></span>

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d70363cf92fad315d6c6e51705d38c2975c44ba883f9acede905cf489d2acc20" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2018.39.13.png?version=1&amp;modificationDate=1766745608195&amp;cacheVersion=1&amp;api=v2" data-height="277" data-width="771" data-unresolved-comment-count="0" data-linked-resource-id="61145502" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 18.39.13.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="d36ad058-be05-4f7a-87c8-7d5b46caf969" data-media-type="file" width="468" height="168" alt="Screenshot 2025-12-26 at 18.39.13.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**页面修改：**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="7dd86f48-a42c-4271-b391-9c7cb713c43d">
<tbody>
<tr data-local-id="c9b061c0-2147-485c-834c-71547e57af19">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="505b6a3c-aca7-4d69-9bbf-331bab9e255c"><p> </p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="ea45ef21-982b-453a-aa61-922f74d5e364"><p> </p></th>
</tr>
&#10;<tr data-local-id="0a623863-60d2-42e9-a89e-8cecd20c83df">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="6975dec6-cfdf-4464-a24e-01f38b38dc2a"><p>市场详情相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8a2a64859a5b6383160774bc9621ceeb98c2ea73dd514757b16403aa89f95789" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.08.19.png?version=2&amp;modificationDate=1766481362644&amp;cacheVersion=1&amp;api=v2" data-height="718" data-width="1265" data-unresolved-comment-count="0" data-linked-resource-id="60588102" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.08.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="dc37f6ab-74ec-4974-9dbf-d1766d13ddc6" data-media-type="file" width="364" height="206" alt="Screenshot 2025-12-23 at 15.08.19.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8a34c1406360fe7ec8270d747248825b0633d737ab7182e40968936b9ec26dec" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.08.39.png?version=2&amp;modificationDate=1766481362643&amp;cacheVersion=1&amp;api=v2" data-height="169" data-width="1128" data-unresolved-comment-count="0" data-linked-resource-id="60555330" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.08.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="7d46742b-a391-4eca-bf64-e49971823873" data-media-type="file" width="363" height="54" alt="Screenshot 2025-12-23 at 15.08.39.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="ce5953f9-ba0d-4601-a566-e712cfd4283a"><ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E5%B8%82%E5%9C%BA%E8%AF%A6%E6%83%85%E5%8C%BA---Market-List" rel="nofollow">Market List（新增激励展示，配置）</a></p></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E5%B8%82%E5%9C%BA%E8%AF%A6%E6%83%85%E5%8C%BA---Market-Overview" rel="nofollow">Market Overview（新增激励展示，配置）</a></p></li>
</ol>
<p><span style="background-color: rgb(223,216,253);">合约配置项</span>：<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E5%B8%82%E5%9C%BA%E8%AF%A6%E6%83%85%E5%8C%BA---Market-List" rel="nofollow">1.</a></p></td>
</tr>
<tr data-local-id="caf57f79-86cf-47b1-99e0-ec0073b74728">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="44bdad65-6f06-454f-98ca-7524db1fc0d3"><p>用户操作相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="82f8a1d7a3f628547cc1d5023034cb3125836027deff8546cefb398b25c488f1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2017.22.03.png?version=1&amp;modificationDate=1766481752563&amp;cacheVersion=1&amp;api=v2" data-height="790" data-width="964" data-unresolved-comment-count="0" data-linked-resource-id="60817493" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 17.22.03.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="c205820c-236f-41f5-a71c-2ed49f2e210b" data-media-type="file" width="240" height="196" alt="Screenshot 2025-12-23 at 17.22.03.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4b9d6ce6911bace3a61ccd39195e042f5b537d298f2711d9328b5e582a4da5c5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2017.24.28.png?version=1&amp;modificationDate=1766481909828&amp;cacheVersion=1&amp;api=v2" data-height="660" data-width="883" data-unresolved-comment-count="0" data-linked-resource-id="60588187" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 17.24.28.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="6718217f-004d-4f1b-a42a-982950769692" data-media-type="file" width="240" height="179" alt="Screenshot 2025-12-23 at 17.24.28.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="317fb85a51e70bd6b37b7936f23dfa64ab0e4a0f7d52f83190781ad15b1857c0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.11.08.png?version=2&amp;modificationDate=1766481362646&amp;cacheVersion=1&amp;api=v2" data-height="711" data-width="948" data-unresolved-comment-count="0" data-linked-resource-id="60686390" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.11.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="9a2c399e-e4cf-4422-b0d6-face7ef78e4c" data-media-type="file" width="240" height="180" alt="Screenshot 2025-12-23 at 15.11.08.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="a002f55c-1692-4003-84ae-e2465065134d"><ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Trade-Panel" rel="nofollow">Trade Panel（新增模式选择，止盈止损 pnl% cap 边界展示与自动回填，订单明细新增激励展示）</a></p></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945?draftShareId=cb8d88d5-6554-41da-8c5f-e8d28b9a98d8#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Close-Position" rel="nofollow">Close Position</a> （订单明细新增激励展示，keep lev限制）</p></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945?draftShareId=cb8d88d5-6554-41da-8c5f-e8d28b9a98d8#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Edit-Collateral" rel="nofollow">Edit Collateral</a> （订单明细新增激励展示，输入框校验限制）</p></li>
</ol>
<p><span style="background-color: rgb(223,216,253);">合约配置项</span>：<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Trade-Panel" rel="nofollow">A.1；A.4</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#B%EF%BD%9C%E6%AD%A2%E7%9B%88%E6%AD%A2%E6%8D%9F%EF%BC%9A" rel="nofollow">B.1&amp;2</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#C%EF%BD%9C%E8%AE%A2%E5%8D%95%E6%98%8E%E7%BB%86" rel="nofollow">C.2.a</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Close-Position" rel="nofollow">减仓弹窗2</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E7%94%A8%E6%88%B7%E6%93%8D%E4%BD%9C%E5%8C%BA---Edit-Collateral" rel="nofollow">保证金编辑3</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/60882945/Trade+_PRD#D-%EF%BD%9C%E8%BE%93%E5%85%A5%E6%A1%86%E6%96%B0%E5%A2%9E%E6%9C%80%E5%B0%8F%E5%A4%B4%E5%AF%B8%E6%A0%A1%E9%AA%8C" rel="nofollow">D最小头寸</a></p>
<p><span style="background-color: rgb(211,241,167);">后端配置项</span>：<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E4%BA%A4%E6%98%93%E8%AE%B0%E5%BD%95%E5%8C%BA---Recent-Trades" rel="nofollow">市场全局交易历史浮窗</a>新增 <strong>position mode</strong> = hyper/normal，具体<strong>返还金额</strong>与返还时使用的<strong>rebate rate%</strong></p></td>
</tr>
<tr data-local-id="59ec4b78-53f9-4dab-a9e1-e80a3a02172f">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="507398aa-d050-4d0a-94f6-c35f280afc7c"><p>交易记录相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="96a8db4e8cb2f7d1a816d32eff903b08efcaef003fda4f8954f60dfb1c5dc885" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.09.30.png?version=2&amp;modificationDate=1766481362628&amp;cacheVersion=1&amp;api=v2" data-height="357" data-width="291" data-unresolved-comment-count="0" data-linked-resource-id="60686377" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.09.30.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="e8c56eed-156c-4d63-a002-5517076878eb" data-media-type="file" width="240" height="294" alt="Screenshot 2025-12-23 at 15.09.30.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7cb6f63e5446e2888d93089096a6c06e31aa8cc707aa0f08022f5426d61821ed" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.11.19.png?version=2&amp;modificationDate=1766481362688&amp;cacheVersion=1&amp;api=v2" data-height="415" data-width="1093" data-unresolved-comment-count="0" data-linked-resource-id="60588096" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.11.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="a5620a55-3912-4490-acb2-1310bf40a5b6" data-media-type="file" width="363" height="137" alt="Screenshot 2025-12-23 at 15.11.19.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="09f133017df930d689e5ce41fd1cf52e7d0de450554371322225846ea3e5fc50" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.11.26.png?version=2&amp;modificationDate=1766481362665&amp;cacheVersion=1&amp;api=v2" data-height="420" data-width="1077" data-unresolved-comment-count="0" data-linked-resource-id="60555323" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.11.26.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="97890dec-21a5-4ccc-8272-a118b4ab8ab7" data-media-type="file" width="363" height="141" alt="Screenshot 2025-12-23 at 15.11.26.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="1cbfd0d9-9a6d-4bc3-ad61-5e1379086733"><ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#%E4%BA%A4%E6%98%93%E8%AE%B0%E5%BD%95%E5%8C%BA---Recent-Trades" rel="nofollow">Recent Trades：</a>浮窗新增激励展示</p></li>
<li><p>User History</p>
<ol>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#A%EF%BD%9CPositions" rel="nofollow">Position：</a>新增激励展示</p></li>
<li><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#B%EF%BD%9CHistory" rel="nofollow">History：</a>修改表格展示，新增激励展示，新增share （position分享功能复用）</p></li>
</ol></li>
<li><p>User Portfolio</p></li>
</ol>
<p><span style="background-color: rgb(223,216,253);">合约配置项：</span><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#A%EF%BD%9CPositions" rel="nofollow">A.1.b</a>；<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#B%EF%BD%9CHistory" rel="nofollow">B.表格pnl那行</a>；</p>
<p><span style="background-color: rgb(211,241,167);">后端配置项</span>：<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#B%EF%BD%9CHistory" rel="nofollow">History列表2-3 总交易记录 &amp; 单条执行明细</a> （<strong>后端数据统计支持比前端实现的全，方便测试网阶段优化调整）</strong></p></td>
</tr>
</tbody>
</table>

</div>

## 二、需求详情

<style type="text/css">/**/
div.rbtoc1771927803461 {padding: 0px;}
div.rbtoc1771927803461 ul {list-style: none;margin-left: 0px;}
div.rbtoc1771927803461 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1771927803461">

- [市场详情区 - Market List](#Trade超高杠杆模式_PRD-市场详情区-MarketList)
- [市场详情区 - Market Overview](#Trade超高杠杆模式_PRD-市场详情区-MarketOverview)
- [用户操作区 - Trade Panel](#Trade超高杠杆模式_PRD-用户操作区-TradePanel)
  - [A｜杠杆：新增模式选择](#Trade超高杠杆模式_PRD-A｜杠杆：新增模式选择)
  - [B｜止盈止损：](#Trade超高杠杆模式_PRD-B｜止盈止损：)
  - [C｜订单明细](#Trade超高杠杆模式_PRD-C｜订单明细)
  - [D ｜输入框新增最小头寸校验](#Trade超高杠杆模式_PRD-D｜输入框新增最小头寸校验)
- [用户操作区 - Close Position](#Trade超高杠杆模式_PRD-用户操作区-ClosePosition)
- [用户操作区 - Edit Collateral](#Trade超高杠杆模式_PRD-用户操作区-EditCollateral)
- [交易记录区 - Recent Trades](#Trade超高杠杆模式_PRD-交易记录区-RecentTrades)
- [交易记录区 - User History_Position/History (Order/Claim无修改）](#Trade超高杠杆模式_PRD-交易记录区-UserHistory_Position/History(Order/Claim无修改）)
  - [A｜Positions](#Trade超高杠杆模式_PRD-A｜Positions)
  - [B｜History](#Trade超高杠杆模式_PRD-B｜History)
- [交易记录区 - User Portfolio](#Trade超高杠杆模式_PRD-交易记录区-UserPortfolio)

</div>

### 市场详情区 - Market List

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8a2a64859a5b6383160774bc9621ceeb98c2ea73dd514757b16403aa89f95789" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.08.19.png?version=2&amp;modificationDate=1766481362644&amp;cacheVersion=1&amp;api=v2" data-height="718" data-width="1265" data-unresolved-comment-count="0" data-linked-resource-id="60588102" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.08.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="dc37f6ab-74ec-4974-9dbf-d1766d13ddc6" data-media-type="file" width="364" height="206" alt="Screenshot 2025-12-23 at 15.08.19.png" /></span>

1.  新增列：表头 alpha edge，内容：标签2个：`Hyper Lev + 图标`（超高杠杆） & `8% + 图标`（损失补偿），8%取自**<span style="background-color: rgb(223,216,253);">合约的市场级配置 loss rebate rate</span>；Hyper Lev<span style="background-color: rgb(223,216,253);">判断同样来自合约配置的杠杆参数</span>**

### 市场详情区 - Market Overview

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8a34c1406360fe7ec8270d747248825b0633d737ab7182e40968936b9ec26dec" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-23%20at%2015.08.39.png?version=2&amp;modificationDate=1766481362643&amp;cacheVersion=1&amp;api=v2" data-height="169" data-width="1128" data-unresolved-comment-count="0" data-linked-resource-id="60555330" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-23 at 15.08.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="7d46742b-a391-4eca-bf64-e49971823873" data-media-type="file" width="363" height="54" alt="Screenshot 2025-12-23 at 15.08.39.png" /></span>

1.  新增Loss Rebate，置于OI右侧：表头：Loss Rebate，内容：`Long + 8%`

    1.  Long：代表OI弱势方；8%代表市场级配置的损失补偿百分比

    2.  数据字段有悬浮tooltip：`Loss Rebate is determined at execution, based on post-trade OI skew, and remains fixed for the position’s lifetime.`\
        `OI Skew: $3,453.23`（计算当前 \|OI Long - OI Short\|）

### 用户操作区 - Trade Panel

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d6b94c5b1eab82c2d5dc3858de8e2e70a68e4a1a438030192b47491dd0086383" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2009.50.28.png?version=1&amp;modificationDate=1766627438883&amp;cacheVersion=1&amp;api=v2" data-height="386" data-width="1041" data-unresolved-comment-count="0" data-linked-resource-id="61145172" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 09.50.28.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="6c7cb449-47e1-4ea5-b1c1-da9ebcd78192" data-media-type="file" width="360" height="133" alt="Screenshot 2025-12-25 at 09.50.28.png" /></span>

#### **A｜杠杆：新增模式选择**

1.  字段：Mode <span style="background-color: rgb(223,216,253);">市场级配置 取合约</span>

2.  hover展示tooltip：`Hyper Lev: 0% Fee. Conditional profit sharing. `\
    `Normal Lev: Standard fees. Conditional loss rebates.`

    `Note: Collateral withdrawal is disabled in hyper mode.`

3.  选项：Normal（默认）；Hyper（仅合约配置有超高杠杆模式的市场可点击，其他市场不展示Hyper）

4.  默认值：**某模式下最低杠杆**（通常为 normal - 1.1x; hyper - 75x)，切换tab记状态，整页刷新不记缓存。**特殊：**切换模式回归默认状态。**<span style="background-color: rgb(223,216,253);">超高杠杆的min & max lev为</span>**<span style="background-color: rgb(223,216,253);">市场级配置 取合约</span>

5.  输入框：最大最小边界值超出后自动校正，防抖200ms。最多支持输入1dp

6.  联动：滑杆输入框以及拉动时的浮窗联动。注意浮窗**水平拖动限制**，左右不能超过滑杆

7.  **快捷输入：**不同市场有不同最大杠杆，下方快捷输入也不同。

    1.  **规则：不同模式各自锚定 MinLev，Max Lev，按风险分层上探**

    2.  **公式：**

        <div class="code panel pdl" style="border-width: 1px;">

        <div class="codeContent panelContent pdl">

        ``` syntaxhighlighter-pre
        普通模式下，Mode = Normal
        快捷输入 = [
          MinLev,
          round(MaxLev * 2/5),
          round(MaxLev * 3/5),
          round(MaxLev * 4/5),
          MaxLev
        ]

        超高杠杆模式下，Mode = Hyper
        快捷输入 = [
          MinLev,
          round(Min Lev +（MaxLev - MinLev） * 1/5),
          round(Min Lev +（MaxLev - MinLev） * 3/5),
          round(Min Lev +（MaxLev - MinLev） * 4/5),
          MaxLev
        ]
        ```

        </div>

        </div>

#### **B｜止盈止损：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3d731bb00f5f9ec82c0a20baa893889323db0c155b0bcf91e7ad31c8145bb13e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2017.35.09.png?version=1&amp;modificationDate=1766655324387&amp;cacheVersion=1&amp;api=v2" data-height="59" data-width="870" data-unresolved-comment-count="0" data-linked-resource-id="61112481" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 17.35.09.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="2bc7d06e-e000-45bb-852f-77c1b50668c7" data-media-type="file" width="360" height="24" alt="Screenshot 2025-12-25 at 17.35.09.png" /></span>

1.  **止盈止损勾选框右侧pnl%展示逻辑（勾选框逻辑不变）：**\
    *这里交互需求不懂可看*<a href="https://app.ostium.com/trade?from=XAU&amp;to=USD" class="external-link" rel="nofollow"><em>ostium</em></a>

    1.  无带tpsl持仓，未勾选**默认**：2500%｜N/A 蓝红区分，空数据置灰

    2.  无带tpsl持仓，已勾选**默认**：2500%｜80%

    3.  无带tpsl持仓，已勾选，有输入且合规时 **联动：**同步回填下方输入的gain%或者loss%

    4.  有带tpsl持仓，**默认**：勾选并自动回填。

    5.  有带tpsl持仓，输入其他合法数值时 **联动**：同步回填下方输入的gain%或者loss%

    6.  有待tpsl持仓，手动取消勾选：回到4中默认

    7.  <span style="background-color: rgb(223,216,253);">这里的三个</span>**<span style="background-color: rgb(223,216,253);">pnl% cap</span>**<span style="background-color: rgb(223,216,253);">取合约 - 止盈上限Profit Cap%（市场级配置），止损上限Loss Ceil%(仅Hyper模式会有，avantis全局配的-30%），止损下限Loss Floor%（仅止损单有，avantis全局配的-80%）⚠️ </span>**<span style="background-color: rgb(223,216,253);">这里的pnl%是计算fee后的net pnl%</span>**

<!-- -->

2.  **hover展示tooltip：**

</div>

</div>

</div>

<div class="columnLayout two-right-sidebar" layout="two-right-sidebar">

<div class="cell normal" data-type="normal">

<div class="innerCell">

若**mode = normal**，则展示字段 `Orders always execute at your specified price, subject to the following caps (gain% & loss% include fees):`

`Gain% (all positions) ≤ +2500% for LP protection`

`Loss% (SL orders only) ≥ –80% for guaranteed execution.`

若**mode = hyper**，则展示字段 `Orders always execute at your specified price, subject to the following caps (gain% & loss% include fees):`

`Gain% (all positions) ≤ +2500% for LP protection`

`-80% ≤ Loss% (SL orders only) ≤ –30% for guaranteed execution.`

数字部分带颜色及正负号，<span style="background-color: rgb(223,216,253);">这里的三个</span>**<span style="background-color: rgb(223,216,253);">pnl% cap</span>**<span style="background-color: rgb(223,216,253);">取合约 - 止盈上限Profit Cap%，止损上限Loss Ceil%，止损下限Loss Floor%</span>

</div>

</div>

<div class="cell aside" data-type="aside">

<div class="innerCell">

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d186b49e08b07fa8030ed1b65d99c85f3d941d37e67f10f4daaa8ba412e32e83" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2011.10.00.png?version=1&amp;modificationDate=1766632248425&amp;cacheVersion=1&amp;api=v2" data-height="240" data-width="769" data-unresolved-comment-count="0" data-linked-resource-id="61112424" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 11.10.00.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="44e37cdc-ed95-49c4-8af6-348d02772fe8" data-media-type="file" width="360" height="112" alt="Screenshot 2025-12-25 at 11.10.00.png" /></span>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="784ab469550473370d8e9cdde63987a9d7e6c2256b1d559df0f9e6afa6d71210" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2011.10.20.png?version=1&amp;modificationDate=1766632248421&amp;cacheVersion=1&amp;api=v2" data-height="536" data-width="765" data-unresolved-comment-count="0" data-linked-resource-id="61177961" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 11.10.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="b3a0a49b-ca22-414d-b460-99d0313380d7" data-media-type="file" width="360" height="252" alt="Screenshot 2025-12-25 at 11.10.20.png" /></span>

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

3.  **<span colorid="qpy92qxymk">市价</span>，Mode = Hyper时的**输入框校验（<span colorid="msblwswx8u">红色为变更部分，hyper不支持限价单</span>）

    <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c07ee914116c37d763678dd898b8b5d41a982ab69e7a567a0410480947e1c3a1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2018.06.32.png?version=1&amp;modificationDate=1766657212641&amp;cacheVersion=1&amp;api=v2" data-height="354" data-width="1141" data-unresolved-comment-count="0" data-linked-resource-id="61210817" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 18.06.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="1dd7ed4d-dc2d-4c22-9b0d-e492dae3f11c" data-media-type="file" width="360" height="111" alt="Screenshot 2025-12-25 at 18.06.32.png" /></span>

    1.  **计算逻辑：**

        1.  **TP/SL价格边界**\
            TP_Price_Cap = Entry_Price × \[1 ± (25 × Collateral - Fees) / Size\]\
            SL_Price_Cap = Entry_Price × \[1 ± (-0.8 × Collateral - Fees) / Size\]\
            <span colorid="nbjriuco8m">SL_Price_Ceil = Entry_Price × \[1 ± (-0.3 × Collateral - Fees) / Size\] // Hyper独有</span>

        2.  **PnL%计算**\
            PnL% = ±(Trigger_Price - Entry_Price) / Entry_Price × Leverage + Fees / Collateral

        3.  **符号规则:**\
            Long: TP用+, SL用-\
            Short: TP用-, SL用+

        4.  **Fees** = Funding Fee + Borrow Fee（超高杠杆下为0）+ Price Impact + Close Fee（超高杠杆下为0）

    2.  **Hyper Mode下，止损价格限制 状态机：**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="0369f4fa-3a13-408d-9c07-d0a0bfe353e7">
<tbody>
<tr data-local-id="b63e4cfb-d97b-492d-8d2a-1454dcbd0a01">
<th class="numberingColumn confluenceTh"></th>
<th class="confluenceTh" data-local-id="2f93f8b2-e6b4-4c3c-a846-cc77f8a07419"><p>场景</p></th>
<th class="confluenceTh" data-local-id="46b6de4f-a27d-4347-8874-4f8ed90fa588"><p><strong>合规</strong>范围</p></th>
<th class="confluenceTh" data-local-id="d4c80744-19c7-447a-8d67-cc88632aff89"><p><strong>不合规</strong>UI</p></th>
</tr>
&#10;<tr data-local-id="ae65f958-e03e-4274-9642-100808c35758">
<td class="numberingColumn confluenceTd">1</td>
<td class="confluenceTd" data-local-id="9cca6267-0f71-4ab0-ac54-0a82c8923bbb"><p>市价加仓</p></td>
<td class="confluenceTd" data-local-id="a1369722-e16d-4caa-a290-8ca88adca0eb"><p><strong>Long | Market（原mark price改为红色部分）</strong></p>
<p>SL Cap ≤ SL Price <span data-colorid="n4xi3ytemv">≤ SL_Price_Ceil</span></p>
<p><strong>Short | Market</strong></p>
<p><span data-colorid="d4rr1p6fis">SL_Price_Ceil</span> <span data-colorid="ss7hv96vdg">≤</span> SL Price ≤ SL Cap</p></td>
<td class="confluenceTd" data-local-id="4ab2e2ad-ef63-4f9e-9224-8f10e7aa59b4"><p>红框 + tooltip；</p>
<p>按钮<code>Above Max</code><span data-colorid="b63w98d4ma"><sub>多</sub> </span>/<code>Below Min</code><span data-colorid="kb38vra0s9"><sub>空</sub></span><code> SL Price </code>Disabled</p>
<p>提示tooltip：<code>Max</code><span data-colorid="oq00gyrj43"><sub>多</sub></span>/<code>Min</code><span data-colorid="lzv4b4jvi0"><sub>空</sub></span><code>SL Price [SL Price Ceil($)]</code>或者<code>Min Loss% 30%</code> 点击自动回填</p></td>
</tr>
<tr data-local-id="5d067636-99c2-418f-bcbd-1704f4bc748c">
<td class="numberingColumn confluenceTd">2</td>
<td class="confluenceTd" data-local-id="e609c17b-7ec7-4655-835b-4334a13c4128"><p>tpsl减仓</p></td>
<td class="confluenceTd" data-local-id="645c2f83-5f08-41c7-9638-43074d64ec5d"><p>先根据输入价格与市价关系判断其性质为止盈还是止损。</p>
<p><strong>Long｜Trigger Price &lt; Mark Price → 止损</strong></p>
<p>SL Cap ≤ TP Cap SL Price ≤ <span data-colorid="tfqfqsojg6">SL_Price_Ceil</span></p>
<p><strong>Short｜Trigger Price &gt; Mark Price → 止损</strong></p>
<p><span data-colorid="gm24wlcub2">SL_Price_Ceil</span> <span data-colorid="fhkdoas69n">≤</span> SL Price ≤ SL Cap</p></td>
<td class="confluenceTd" data-local-id="434992c2-421f-4294-aea0-ae70e49d9301"><p>红框 + tooltip + 回填 同加仓</p>
<p>注意输入合法时按钮是<strong>Create Take Profit或Stop Loss Order ，不是市价平仓的close xxx</strong></p></td>
</tr>
<tr data-local-id="39f327f4-d66d-419a-8464-aeea4d7aa62f">
<td class="numberingColumn confluenceTd">3</td>
<td class="confluenceTd" data-local-id="eb33a18f-a6ba-469a-8b49-9b23e0735f1e"><p>保证金增加</p></td>
<td class="confluenceTd" data-local-id="15695b77-fbdd-4632-bd27-56aafb3c900e"><p><strong>这里合规范围是：</strong>原SL仍优于新的SL Cap<strong><span data-colorid="p224szh93j">（双边）</span></strong>，若原SL Price处于范围外，则order以及position中标红为价格无效。</p>
<p><strong>不合规场景如下：</strong></p>
<p><strong>Long</strong>｜<strong>原SL Price &lt;-80%的新SL Price <sub></sub> Cap 或 <span data-colorid="ald9vvgzuo">原SL Price &gt; -30%的新SL Price <sub></sub> Cap</span></strong></p>
<p>黄色警告框提示止损单会立即失效</p>
<p><strong>Short｜原SL Price &gt; -80%的新SL Price <sub></sub> Cap <sub></sub> 或 <span data-colorid="kj7xazfdi8">原SL Price &lt; -30%的新SL Price <sub></sub> Cap</span></strong></p>
<p>黄色警告框提示止损单会立即失效</p></td>
<td class="confluenceTd" data-local-id="a34e235d-ab36-46df-b710-23264ed55fd7"><p>红框 + tooltip<br />
position 与order价格对应变更至新价格/价格无效状态。<br />
<br />
<br />
</p>
<p><code>Set SL Price is worse than new SL Price capped at -30% PnL%. Reducing collateral may result in INVALID STOP LOSS order.</code></p>
<p><strong>成交时更新前端positoin/order中展示的止损价格不合规状态-价格标红+tooltip</strong></p></td>
</tr>
<tr data-local-id="8463a3ac-582c-4407-bb8a-fc9ce3dc9a9a">
<td class="numberingColumn confluenceTd">4</td>
<td class="confluenceTd" data-local-id="82a0e937-4e36-43b6-a44f-5efd41f516b5"><p>仓位被动变化</p></td>
<td class="confluenceTd" data-local-id="cc3c0958-6448-4313-9bfb-6e6ef644491f"><p><strong>Long | Market Position</strong></p>
<p>SL Cap ≤ SL Price <span data-colorid="jgjp05qivk">≤ SL_Price_Ceil</span></p>
<p><strong>Short | Market Position</strong></p>
<p><span data-colorid="e9klo6knxl">SL_Price_Ceil</span> <span data-colorid="vl7r43kje0">≤</span> SL Price ≤ SL Cap</p></td>
<td class="confluenceTd" data-local-id="d0322627-f7b4-404e-ae24-f9a47b88cbac"><p><code>Invalid Stop Loss：Set SL Price is out of the SL Price range capped at -30% PnL%.</code></p></td>
</tr>
</tbody>
</table>

</div>

#### C｜订单明细

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0506239557e8f5ae00074f3e0dc4b810e8e21ce46f9577ca6d698f474abed809" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-25%20at%2018.12.20.png?version=1&amp;modificationDate=1766658281461&amp;cacheVersion=1&amp;api=v2" data-height="346" data-width="943" data-unresolved-comment-count="0" data-linked-resource-id="61145289" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-25 at 18.12.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="a842dc79-a163-4113-838b-ae8c4bd85aa0" data-media-type="file" width="360" height="132" alt="Screenshot 2025-12-25 at 18.12.20.png" /></span>

1.  Fee超高杠杆模式下零手续费激励展示：

    1.  字段：0 Fee ~~原费用~~

    2.  具体费用明细的tooltip隐藏，没有悬浮态或浮窗

2.  <span class="inline-comment-marker" ref="a9d07e9d-7b6b-4f0e-839b-6e2a139b7d99">普通杠杆模式下，符合条件的Loss Rebate展示： </span>

    1.  展示的前置条件：OI弱势方，才会展示loss rebate这行

    2.  位置：liq price下面一行，市价限价单都会展示

    3.  字段：Loss Rebate + 图标 + 损失补偿百分比 <span style="background-color: rgb(223,216,253);">市场级配置，取合约</span>

    4.  数据：

        1.  格式：**不展示正负号**损失偿还永远为正，2dp，\< 0.01 USDC

        2.  默认：`0 USDC`

        3.  若**size delta \> OI skew = ｜Long OI - Short OI｜**则展示默认的`0 USDC`

        4.  若**size delta \<= OI skew = ｜Long - Short｜**则展示计算后的 `≤ 3.34 USDC`

        5.  计算算逻辑：= **collateral delta \* loss rebate / USDC Price** 计算并展示最大（也就是爆仓时）损失补偿USDC价值

    5.  hover展示tooltip：Loss rebate is determined at execution, based on post-trade OI skew, and remains fixed for the position’s lifetime.

#### D ｜输入框新增最小头寸校验

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2f3ae2513b113e5d2cc7cc0d12506244b903de687631882e4dc4d38a06cf92b1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2020.06.48.png?version=1&amp;modificationDate=1766751113559&amp;cacheVersion=1&amp;api=v2" data-height="403" data-width="486" data-unresolved-comment-count="0" data-linked-resource-id="61145550" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 20.06.48.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="d42f39b7-faf3-49b1-bfcf-0246da25d42a" data-media-type="file" width="360" height="299" alt="Screenshot 2025-12-26 at 20.06.48.png" /></span>

1.  mode = hyper时，新增校验：

    1.  若(current position size + size delta) \< min position size，按钮 `Below Min Position Size [Min Position Size delta($)]` disabled

    2.  **Min Position Size Delta =** min position size - current position size

### 用户操作区 - Close Position

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bddddd1668beefd7fb79e2885a72ae89b6516f2c34633940059dc6d1eaae0989" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2010.06.06.png?version=1&amp;modificationDate=1766714776211&amp;cacheVersion=1&amp;api=v2" data-height="742" data-width="1032" data-unresolved-comment-count="0" data-linked-resource-id="61210848" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 10.06.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="254cbd11-cc93-47b8-9479-c91022938176" data-media-type="file" width="360" height="258" alt="Screenshot 2025-12-26 at 10.06.06.png" /></span>

同上 新增<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#C%EF%BD%9C%E8%AE%A2%E5%8D%95%E6%98%8E%E7%BB%86" rel="nofollow">超高杠杆免手续费 &amp; 普通杠杆下损失返还</a> ，即：

1.  **普通模式：** 平仓弹窗中loss rebate以及对应tooltip**置于liq price上面，仅亏损仓位展示**

    1.  **市价平仓**仅亏损仓位展示**确切计算 r% \* PnL**

    2.  **止盈止损平仓弹窗**展示**均同下单区，loss rebate ≤ r% \* Coll Delta。**

2.  **超高杠杆模式：**不展示loss rebate，新增**零手续分展示。<span style="background-color: rgb(223,216,253);"><span class="inline-comment-marker" ref="aed37fa3-5276-499e-bb69-a965f056dd07">keep leverage勾选禁止修改，写死enabled。</span></span>**

### 用户操作区 - Edit Collateral

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ad7d2841d14176e865ffe8708ba96d6ad2db0de3a162aee1dc4a30bc062de542" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2011.44.43.png?version=1&amp;modificationDate=1766720697138&amp;cacheVersion=1&amp;api=v2" data-height="682" data-width="1039" data-unresolved-comment-count="0" data-linked-resource-id="61178103" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 11.44.43.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="ae57d86e-f91c-40fc-8d66-1e6bba5007b9" data-media-type="file" width="360" height="236" alt="Screenshot 2025-12-26 at 11.44.43.png" /></span>

1.  原max xxx变展示形式：`钱包icon + 钱包USDC余额数量 + USDC为单位`

2.  **普通模式：**新增loss rebate展示，置于liq price下面，同<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#C%EF%BD%9C%E8%AE%A2%E5%8D%95%E6%98%8E%E7%BB%86" rel="nofollow">下单区</a>

3.  **超高杠杆模式：** 超高杠杆下，移除保证金tab可点但`withdraw按钮`**禁用**。展示置顶警告 -` Withdrawal is disabled for Hyper Leverage Mode.`；新增零手续费样式，同下单区

    1.  **输入框校验边界值：(普通模式不变）**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="c76295a7-9011-4d5d-a80b-c024407dbeac">
<tbody>
<tr data-local-id="aeb950b9-ffc6-465f-bbdf-6ac630c19ded">
<th class="confluenceTh" data-local-id="a448cc8c-8f8c-47d0-863d-3c6f6fc54c60"><p><strong>加D/减W</strong></p></th>
<th class="confluenceTh" data-local-id="bc700fb0-06db-432a-a44e-41221fb74746"><p><strong>校验边界值</strong></p></th>
<th class="confluenceTh" data-local-id="3aff8764-eb1d-488b-80f1-52071dddb812"><p><strong>交互</strong></p></th>
</tr>
&#10;<tr data-local-id="a677575a-4c0e-4f23-a733-08700d86f5cb">
<td class="confluenceTd" data-local-id="9cf03578-8cdb-4bc9-a283-4804c371f93a"><p>Dep</p></td>
<td class="confluenceTd" data-local-id="0a42bb0f-a753-45d8-9596-a43f8ed11bc8"><p>Deposit<sub>Min</sub> = 10 USDC</p>
<p>Deposit<sub>Max</sub> = (1/L<sub>min,hyper</sub> - 1/L) * Size</p></td>
<td class="confluenceTd" data-local-id="74641b07-226c-40e1-be2a-c6c8463b7c0d"><ul>
<li><p>按钮 <code>Leverage Too Low (below 75x)</code> disabled</p></li>
<li><p>点击max回填<strong>min{</strong>Deposit<sub>Max</sub>，Wallet Balance<strong>}</strong></p></li>
</ul>
<p><span style="background-color: rgb(223,216,253);">这里的75x就是L<sub>min,hyper</sub>最小可开杠杆，配在合约的市场级参数</span></p></td>
</tr>
<tr data-local-id="0cac8afa-4d4c-4e49-bb3f-bf517d329cfb">
<td class="confluenceTd" data-local-id="2aedc5f5-60e9-4a79-a316-2f95ffad5b78"><p>Wd</p></td>
<td class="confluenceTd" data-local-id="f97d3641-8d49-4cbc-a4a4-b6a37fc8d4b7"><p>Withdraw<sub>min</sub> = Withdraw<sub>max</sub> = 0</p></td>
<td class="confluenceTd" data-local-id="e588d39a-1f8a-4041-8d4b-94e1d320f1b5"><ul>
<li><p>输入框默认态0，禁用，按钮<code>disable</code></p></li>
</ul>
<p><span style="background-color: rgb(223,216,253);">合约需在决定仓位唯一性的position id中加mode这一维度</span></p></td>
</tr>
</tbody>
</table>

</div>

### 交易记录区 - Recent Trades

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="762037c9e0ff684b1fadd57bdec640a3e468f92ff8b8ca64471f718bd7e73d2b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2014.21.49.png?version=1&amp;modificationDate=1766730122029&amp;cacheVersion=1&amp;api=v2" data-height="358" data-width="503" data-unresolved-comment-count="0" data-linked-resource-id="61210912" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 14.21.49.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="798c1688-33f2-41e5-b801-940d85ea8930" data-media-type="file" width="360" height="256" alt="Screenshot 2025-12-26 at 14.21.49.png" /></span>

1.  浮窗位置：注意规定最大高度最小高度 最好不溢出右侧recent trades卡片高度

2.  杠杆新增：新增代表超高杠杆模式的图标 <span style="background-color: rgb(211,241,167);">position mode后端给</span>

3.  明细新增：<span style="background-color: rgb(211,241,167);">（</span>**<span style="background-color: rgb(211,241,167);">仅减仓且rebate\>0</span>**<span style="background-color: rgb(211,241,167);">）</span>Loss Rebate 置于PnL上面 包括具体<span style="background-color: rgb(211,241,167);">返还金额</span>与返还时使用的<span style="background-color: rgb(211,241,167);">rebate rate</span>

### 交易记录区 - User History_Position/History (Order/Claim无修改）

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ed342ee045ecac192d5890753f945d3b1ae451d408c1e7181772d877d0169a2a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2014.52.15.png?version=1&amp;modificationDate=1766731952285&amp;cacheVersion=1&amp;api=v2" data-height="350" data-width="1208" data-unresolved-comment-count="0" data-linked-resource-id="61178158" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 14.52.15.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="b6b8b232-15b1-4130-9a44-0564ee1920fb" data-media-type="file" width="468" height="135" alt="Screenshot 2025-12-26 at 14.52.15.png" /></span>

#### A｜Positions

1.  **普通模式（顶行）：**

    1.  **保证金Collateral这一列**新增**损失补偿图标。置于数字左侧。hover 展示tooltip：**\
        `Loss Rebate is determined at execution, based on post-trade OI skew, and remains fixed for the position’s lifetime.`\
        `Loss Rebate: (10%) ≤ 2.60 USDC`\
        10%是rebate rate，取自合约 后端 position id，\$2.6取 **= collateral \* rebate rate%**

    2.  Net Value的tooltip新增**Loss Rebate** 次要数据位于Gross Pnl - 最后一个Close Fee的正下方：\
        `Loss Rebate: (10%) 2.3 USDC `\
        <span class="inline-comment-marker" ref="ce2e4f7e-ed1b-4b83-bc6e-fceb17c8cf85">10%是rebate rate，取自合约 后端 position id，2.3取 </span>**<span class="inline-comment-marker" ref="ce2e4f7e-ed1b-4b83-bc6e-fceb17c8cf85">= collateral \* pnl% \* rebate rate%</span>**

2.  **超高杠杆模式（底行）：**

    1.  **Symbol这一列** 新增超高杠杆标签，置于仓位杠杆倍数左或右侧，样式同recent trades浮窗。

    2.  Net Value的tooltip：`No trading or borrowing fees. A variable fee is applied only to realized profits at close.`\
        `Funding Fee Due: $0.60`

#### **B｜History**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="425f978ec283fd2917309a9e921c83082949719707e8df09e274b182e6195728" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2015.00.32.png?version=1&amp;modificationDate=1766732476195&amp;cacheVersion=1&amp;api=v2" data-height="836" data-width="1290" data-unresolved-comment-count="0" data-linked-resource-id="61178174" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 15.00.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="b3a9ac42-50b8-4fc1-bcdc-119ec505673d" data-media-type="file" width="468" height="303" alt="Screenshot 2025-12-26 at 15.00.32.png" /></span>

1.  注意这里新增**分享功能：**pnl不为空时支持分享。同position那里

2.  历史列表：**<span style="background-color: rgb(211,241,167);">Symbol；Type；Size；Collateral；Entry Price；Exit Price；PnL；Time/Hash</span>**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="649b14ba-50c2-4efb-a29e-b2a48e60bf7c">
<tbody>
<tr data-local-id="7647b2dc-5546-4738-8d76-3ca050e4a452">
<th class="confluenceTh" data-local-id="5205cd89-f2e9-4d99-b91a-dddaea5e7108"><p>列名</p></th>
<th class="confluenceTh" data-local-id="9c15aae7-6862-4963-9ebc-ce39e11a46e5"><p>数据源</p></th>
<th class="confluenceTh" data-local-id="be4d66e7-af34-49c9-9191-67e936630f95"><p>格式/展示逻辑</p></th>
<th class="confluenceTh" data-local-id="15b173f2-b2ec-407c-9423-841c49887994"><p>筛选/排序</p></th>
</tr>
&#10;<tr data-local-id="b4ea4ec7-bca4-4159-a2e8-e9aff8f13706">
<td class="confluenceTd" data-local-id="d0fc0dab-8c9d-4b66-9fd7-0e2069100db4"><p><strong>Symbol</strong></p></td>
<td class="confluenceTd" data-local-id="42bcdc48-2dec-4c3a-b324-3b32a03e7285"><p><code>Direction</code> + <code>market_id</code> + <code>leverage</code> + <code>mode</code></p></td>
<td class="confluenceTd" data-local-id="45fb7b61-0603-475a-81c6-c121110a8e14"><ul>
<li><p>mode仅hyper展示图标</p></li>
</ul>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2b169f78b32b3532b650333ecd7c13099b77eeef5e7b662302994e4bcc1811ed" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2016.56.09.png?version=1&amp;modificationDate=1766739408343&amp;cacheVersion=1&amp;api=v2" data-height="462" data-width="411" data-unresolved-comment-count="0" data-linked-resource-id="61145450" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 16.56.09.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="56dad2bf-acec-413b-bb08-f66f24e487a1" data-media-type="file" width="100" height="112" alt="Screenshot 2025-12-26 at 16.56.09.png" /></span>
<ul>
<li><p>Lev 仅Open/Close执行成功的展示杠杆</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="ad067e39-6980-491e-81d0-c49ab609dd46"><p>✅ 筛选</p>
<p>Hide Others控制仅展示当前市场</p></td>
</tr>
<tr data-local-id="55713a91-599e-449c-881e-d10d4352c223">
<td class="confluenceTd" data-local-id="1be83426-7a15-4a0c-84f1-6fb60530cd2b"><p><strong>Type</strong></p></td>
<td class="confluenceTd" data-local-id="91272d23-f14e-43d6-a0d0-feff57a9be44"><p><code>order_type</code></p></td>
<td class="confluenceTd" data-local-id="4c08bf41-25a1-4214-9f08-5c9452e63d7a"><ul>
<li><p>枚举: Market / Limit / TP / SL / Liquidated</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="cee201e5-3f34-488c-8d5c-bd0979d1ad9c"><p>✅ 一级筛选，默认All，可多选</p></td>
</tr>
<tr data-local-id="5ea05079-421a-4fa3-9a2a-f6c0c1d4adc3">
<td class="confluenceTd" data-local-id="19b647ae-7f5d-48f1-bb39-5bee9bf26dc6"><p><strong>Size</strong></p></td>
<td class="confluenceTd" data-local-id="54c38a3f-c860-4537-8f4f-5e5549107b96"><p><code>size_delta</code></p></td>
<td class="confluenceTd" data-local-id="953da4bf-c4ee-4b9b-94f4-d443cbcb849c"><ul>
<li><p>带符号: <code>+$10,000</code>（市价加/限价/保证金添加） / <code>-$5,000</code>（市价减/止盈止损/保证金移除/强平）</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="0d830e56-3a5f-4feb-af9a-be6628425137"><p>-</p></td>
</tr>
<tr data-local-id="eca2071a-b39b-4cef-8b32-07f5a1d417b8">
<td class="confluenceTd" data-local-id="af58156d-5aa1-44e5-b4f0-d96c056fa82f"><p><strong>Collateral</strong></p></td>
<td class="confluenceTd" data-local-id="5383ebe1-3085-422a-8a14-abcfbdeb7c73"><p><code>collateral_delta</code> + <code>loss_rebate</code> +<code>tooltip</code></p></td>
<td class="confluenceTd" data-local-id="a96293c6-7dc2-4070-87a6-6a46062dc386"><ul>
<li><p>普通模式增加loss rebate 展示图标 + tooltip 同<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/edit-v2/60882945#A%EF%BD%9CPositions" rel="nofollow">positions A.1</a></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4dd97f7bfacc432e77d0f942d10c4a9010b491d4c0ab4890de0fb5346bfaa535" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2017.22.47.png?version=1&amp;modificationDate=1766740979985&amp;cacheVersion=1&amp;api=v2" data-height="344" data-width="684" data-unresolved-comment-count="0" data-linked-resource-id="61112724" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 17.22.47.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="2235fdb1-67c6-4bb3-92b8-5b6cbe304698" data-media-type="file" width="176" height="88" alt="Screenshot 2025-12-26 at 17.22.47.png" /></span></p></li>
</ul></td>
<td class="confluenceTd" data-local-id="95947e16-f3e5-487a-80b2-680e57237cb8"><p>-</p></td>
</tr>
<tr data-local-id="5a6cb33e-27f7-4270-b1ee-452db7d12fb7">
<td class="confluenceTd" data-local-id="2578db4b-c980-45f9-ab75-90a494d04486"><p><strong>Entry Price</strong></p></td>
<td class="confluenceTd" data-local-id="9b6f24a3-4027-45f4-8d40-a427bc310f59"><p><code>entry_price</code></p></td>
<td class="confluenceTd" data-local-id="654c4181-166c-49d1-8504-3b30756a9c63"><p>执行成功：</p>
<ol>
<li><p><strong>市价加仓：</strong>= <code>execution_price</code></p></li>
<li><p><strong>市价减仓：</strong>= <code>position.avg_entry_price</code></p></li>
<li><p><strong>添加/移除保证金：</strong>= <code>缺省态 -</code></p></li>
<li><p><strong>限价加仓：</strong><code>execution_price</code></p></li>
<li><p><strong>止盈止损减仓：</strong><code>position.avg_entry_price</code></p></li>
<li><p><strong>强平：</strong>=<code> position.avg_entry_price</code></p></li>
</ol>
<p>创建/取消/失败/更新：</p>
<ol>
<li><p><strong>市价加仓：</strong>= <code>execution_price</code></p></li>
<li><p><strong>市价减仓：</strong>= <code>position.avg_entry_price</code></p></li>
<li><p><strong>添加/移除保证金：</strong>= <code>缺省态 -</code></p></li>
<li><p><strong>限价加仓：</strong><code>≤</code><span data-colorid="v64k1nd0pu"><sub>多</sub></span>或<code>≥</code><span data-colorid="ppq4neo0lr"><sub>空</sub></span><code>trigger price</code></p></li>
<li><p><strong>止盈止损减仓：</strong><code>position.avg_entry_price</code></p></li>
</ol></td>
<td class="confluenceTd" data-local-id="9d2f7ba6-6fee-4aef-9d9f-004b67f2e629"><p>-</p></td>
</tr>
<tr data-local-id="2d74cb90-f409-49e7-ad2e-58d9d0be8d9c">
<td class="confluenceTd" data-local-id="98bce640-7292-4256-a1d2-545f4962ac65"><p><strong>Exit Price</strong></p></td>
<td class="confluenceTd" data-local-id="80d96449-5830-44f0-b0a9-67e712757386"><p><code>exit_price</code></p></td>
<td class="confluenceTd" data-local-id="993073ac-3c26-40c3-8154-ff803c527429"><p>执行成功：</p>
<ol>
<li><p><strong>市价加仓：</strong>= <code>缺省态-</code></p></li>
<li><p><strong>市价减仓：</strong>= <code>execution_price</code></p></li>
<li><p><strong>添加/移除保证金：</strong>= <code>缺省态 -</code></p></li>
<li><p><strong>限价加仓：</strong><code>缺省态-</code></p></li>
<li><p><strong>止盈止损减仓：</strong><code>execution_price</code></p></li>
<li><p><strong>强平：</strong>=<code>liq_price</code></p></li>
</ol>
<p>创建/取消/失败/更新：</p>
<ol>
<li><p>市价加仓：= <code>缺省态-</code></p></li>
<li><p>市价减仓：= <code>execution_price</code></p></li>
<li><p>添加/移除保证金：= <code>缺省态 -</code></p></li>
<li><p>限价加仓：<code>缺省态-</code></p></li>
<li><p>止盈止损减仓：<code>≥</code><span data-colorid="dfyxrgjnk2"><sub>多</sub></span>或<code>≤</code><span data-colorid="bvol0o3uyn"><sub>空</sub></span><code>trigger price</code></p></li>
</ol></td>
<td class="confluenceTd" data-local-id="3b099798-b40e-45ac-b6b1-ca50edfd13c2"><p>-</p></td>
</tr>
<tr data-local-id="5d4e42a8-79c1-4c93-9443-afffc9d113fb">
<td class="confluenceTd" data-local-id="01f3328b-00b0-49f8-afd2-192025e884dd"><p><strong>PnL</strong></p></td>
<td class="confluenceTd" data-local-id="b027e22b-68b4-4634-b03e-62afdb09712d"><p><code>net_pnl</code></p>
<p><code>net_pnl%</code></p></td>
<td class="confluenceTd" data-local-id="d9f98f14-2d64-4457-8380-66edabfb82ba"><p>格式: <code>+$500 (+20%)</code>&lt;br&gt;盈利绿色/亏损红色</p>
<ul>
<li><p>Net PnL = Returned Collateral - Initial Collateral ，其中returned代表退还给用户的保证金（<span style="background-color: rgb(223,216,253);">包括损失返还/盈利抽成，这里涉及合约新引入的参数</span>）</p></li>
<li><p>Net PnL% = Net PnL / Initial Collateral</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="5a0f3bf6-6ce4-43a2-9f9f-291a2f40dd37"><p>-</p></td>
</tr>
<tr data-local-id="e54d6649-86b9-4847-a8bb-3abd23a1ba17">
<td class="confluenceTd" data-local-id="c4cb1b0e-74e4-4d48-99c0-2611494ea9d2"><p><strong>Time/Hash</strong></p></td>
<td class="confluenceTd" data-local-id="ba6511b7-b712-46d7-84cc-466dcba7cabc"><p><code>timestamp</code> + <code>tx_hash</code></p></td>
<td class="confluenceTd" data-local-id="75eb8c84-4aa6-475b-9d17-c41ce511a452"><p>用户机器时间 + 哈希</p></td>
<td class="confluenceTd" data-local-id="28145c97-8e21-4362-abee-70d1a2eec9af"><p>✅ 倒序(默认)</p></td>
</tr>
<tr data-local-id="fb62ed8f-b8a8-4108-adc0-978982551ac5">
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="995f5db7-876b-4da1-bcf0-3dc3af5c631f"><p><strong>Action<span style="background-color: rgb(211,241,167);">（当前仅后端实现，测试网期间优化）</span></strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="a50a7e33-4815-4652-9052-585e873e83eb"><p><code>order_type_action</code></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="4e97a986-22af-416d-8956-336f99c9dda8"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d5421b0375c049239440f3229d383166b383125dc7a6d4ccc012aa5ca6d1a7bc" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2016.59.39.png?version=1&amp;modificationDate=1766739901080&amp;cacheVersion=1&amp;api=v2" data-height="263" data-width="196" data-unresolved-comment-count="0" data-linked-resource-id="61211014" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 16.59.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="84739d0d-19d7-4e6d-a8d6-45a57c396a3b" data-media-type="file" width="196" height="263" alt="Screenshot 2025-12-26 at 16.59.39.png" /></span>
<p>枚举：新增创建&amp;失败&amp;取消&amp;更新的所有订单，以及保证金操作</p>
<ul>
<li><p>type = market，action = market open/ market increase/market close/market decrease/deposit/withdrawal/failed market open/failed market increase/ failed market close/failed market decrease/failed deposit/failed withdrawal</p></li>
<li><p>type = limit，action = limit open / limit increase / created limit / updated limit / failed limit / cancelled limit</p></li>
<li><p>type = take profit，action = take profit close / take profit decrease / created take profit / updated take profit / failed take profit / cancelled take profit</p></li>
<li><p>type = stop loss，action = stop loss close / stop loss decrease / created stop loss / updated stop loss / failed stop loss / updated stop loss /</p></li>
<li><p>type = liquidated，action = liquidated</p></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="7873ea37-adb3-4e00-8618-b3bcb8e28bca"><p>✅ 二级筛选，可多选，默认all</p></td>
</tr>
</tbody>
</table>

</div>

3.  **pnl这里的tooltip展示：**先判断mode

</div>

</div>

</div>

<div class="columnLayout two-equal" layout="two-equal">

<div class="cell normal" data-type="normal">

<div class="innerCell">

**Mode = Normal：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="983c87f27ff37b6a91c44f09a1fa84b2840824bd6a30845f247591165bd2d9da" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2016.48.24.png?version=1&amp;modificationDate=1766738953860&amp;cacheVersion=1&amp;api=v2" data-height="427" data-width="636" data-unresolved-comment-count="0" data-linked-resource-id="61210994" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 16.48.24.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="0f2d1b9f-004d-4cc1-bd52-c054f3e8bfb9" data-media-type="file" width="356" height="239" alt="Screenshot 2025-12-26 at 16.48.24.png" /></span>

1.  Initial Collateral \$25.96 初始保证金

2.  Gross PnL -\$23.16 (-89.2%) **净值 不算费用或损失补偿**

3.  Loss Rebate +\$2.60 (+10%) 有则展示具体值 & 率

4.  Fees -\$2.10 **减仓+借贷+funding**

5.  Residual Collateral \$3.30 **= Initial Collateral + Gross PnL + Loss Rebate** 平仓时没扣价格冲击/强平费用的剩余保证金

6.  Price Impact +\$0.34

7.  Liquidation Fee -\$2.24

8.  Returned Collateral \$1.40 **最后到用户手里的剩余保证金**

</div>

</div>

<div class="cell normal" data-type="normal">

<div class="innerCell">

**Mode = Hyper：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="bed68c84f038fdc15f6b06d09532e602c207ca17b0ec49e79925920fe05951f6" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-26%20at%2016.48.26.png?version=1&amp;modificationDate=1766738953879&amp;cacheVersion=1&amp;api=v2" data-height="221" data-width="660" data-unresolved-comment-count="0" data-linked-resource-id="61211000" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-26 at 16.48.26.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="4f1f2c21-2ae8-4372-8771-508b7d3e5487" data-media-type="file" width="356" height="119" alt="Screenshot 2025-12-26 at 16.48.26.png" /></span>

1.  **pnl** = **用户实际Net PnL - <span style="background-color: rgb(223,216,253);">合约盈利抽成</span>**

2.  **PnL% = (用户实际Net PnL - <span style="background-color: rgb(223,216,253);">合约盈利抽成</span>) / Collateral**

3.  pnl不为空时展示tooltip `No trading or borrowing fees. A variable fee is applied only to realized profits at close.`

</div>

</div>

</div>

<div class="columnLayout fixed-width" layout="fixed-width">

<div class="cell normal" data-type="normal">

<div class="innerCell">

### 交易记录区 - User Portfolio

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="48ded952127dfa438bf7be2c4c4b7726d1ed5e202eb9a6e18863f97320ef25a4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/60882945/Screenshot%202025-12-04%20at%2019.36.56.png?version=1&amp;modificationDate=1766473211026&amp;cacheVersion=1&amp;api=v2" data-height="383" data-width="389" data-unresolved-comment-count="0" data-linked-resource-id="60882981" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.36.56.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="60882945" data-linked-resource-container-version="4" data-media-id="87a55bfd-912b-42a2-939a-948c543e982e" data-media-type="file" width="360" height="354" alt="Screenshot 2025-12-04 at 19.36.56.png" /></span>

1.  Portfolio-Positions & Activity**计算变更：**注意Net Value与uPnL与PnL引入了loss rebate以及盈利抽成

</div>

</div>

</div>

</div>

</div>
