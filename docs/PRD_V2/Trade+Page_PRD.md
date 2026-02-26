# Trade Page_PRD

<div class="Section1">

<style>[data-colorid=x51vm8ild0]{color:#bf2600} html[data-color-mode=dark] [data-colorid=x51vm8ild0]{color:#ff6640}</style>todo： market list；价格精度配置表；max lev合约侧确认；funding rate tooltip；确认交易价格打点实现；Max Position Size：合约配置参数是否已有？；10usd改10usdc是否好改；

out of scope：funding history chart；

## 一、需求背景

**页面名称**：Trade

**核心逻辑：**

### **TP Price Cap以及SL Price Cap计算逻辑**

pnl% = 多正空负±(P_tpsl - P_entry) / P_entry \* L + F/C\
TP/SL Price = P_entry \* \[1 ± (pnl% / L - F / S)\]\
TP Price Cap = \[1 ± (25 \* Collateral - Fees) / Size\] \* Entry Price\
SL Price Cap = \[1 ± (-.8 \* Collateral - Fees) / Size\] \* Entry Price\
----------------------------------------------------------------------\|\
P-Price; L-Leverage; C-Collateral; S-Size; F-费用加和;pnl%-盈亏率带符号

### **订单链路：**

**EVM与SUI唯一产品层面区别是EVM无需keeper订单推送，后端数据可直接拿到事件状态。**

### **规则摘要:**

>  <a href="https://hertzflow.atlassian.net/wiki/x/E4D6Ag" data-card-appearance="inline" data-local-id="b6a23213-340e-4b38-a78b-f9bf27d2aba6" rel="nofollow">https://hertzflow.atlassian.net/wiki/x/E4D6Ag</a>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3b81ecffe580948501f8b97b11324d8e0ba7ce42f3a4ae985b4db2e42c8c2aef" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Group%202085659856.png?version=1&amp;modificationDate=1765023407796&amp;cacheVersion=1&amp;api=v2" data-height="744" data-width="1848" data-unresolved-comment-count="0" data-linked-resource-id="50430060" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Group 2085659856.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="69e4a50a-b87a-4732-bab6-8f55e0cc3604" data-media-type="file" width="468" height="188" alt="Group 2085659856.png" /></span>

- **TP/SL订单绑定逻辑：Trigger Order 和 Position/Limit Order 仅通过 positionKey 关联，**这代表：

  - **同市场同方向上只有一个止盈止损单。**下单时自动回填，成交后更新价格。

  - 已有仓位，全平至position size = 0, tp/sl才会被清理。

  - 未成交的限价单，带tpsl。限价单被取消**不会导致**tpsl被清理，因为没有绑定的position id。后续开市价单时会默认绑定至新仓位。

  - Position 变化（size/collateral/entryPrice）不会自动更新 TP/SL triggerPrice。**所以参数过期很常见，需要前端负责警告提示**

- **价格冲突责任范围：仓位变 → TP/SL 不变 → 前端负责告诉用户“参数已失效”**：TP/SL 的有效性与边界限制必须基于合并后的 newEntryPrice / newCollateral / newSize / 合并后 Fees（带符号）**重新计算与校验**，且 TP/SL 应提示用户更新。

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="12ffe2f9-3f3e-47bb-bc64-94583d64383f">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="ecad6078-fd03-4314-80c5-0697498cc647">
<th class="confluenceTh" data-local-id="45bfec39-e134-4aa1-9f2a-f0ffcc578d9e"><p>角色</p></th>
<th class="confluenceTh" data-local-id="deefc43e-0215-4315-b469-e0014772f049"><p>职责</p></th>
<th class="confluenceTh" data-local-id="24090448-e4f1-4996-9d08-5908e150cd39"><p>不负责</p></th>
</tr>
&#10;<tr data-local-id="b84973a2-714f-447a-8869-e70336836a63">
<td class="confluenceTd" data-local-id="382ba740-d538-460a-b910-9c3376093322"><p><strong>前端</strong></p></td>
<td class="confluenceTd" data-local-id="c36f2741-705d-400a-b435-8965cbb4b974"><p>负责输入 TP/SL 参数、监听仓位变化、提供更新入口、警告提示</p></td>
<td class="confluenceTd" data-local-id="a14f7e37-e5e4-4e81-bc15-72ac7fbd4b23"><p>不自动代表用户更新参数（除 UI 自动填充外）</p></td>
</tr>
<tr data-local-id="22c172c3-98c1-4c45-917c-75a5320c5ebe">
<td class="confluenceTd" data-local-id="e704f7c4-6f74-47c3-afa6-71fbaa88c207"><p><strong>合约</strong></p></td>
<td class="confluenceTd" data-local-id="c0d1afe7-135f-4560-a3e5-db250661e13b"><p>存储用户设置的 triggerPrice；提供 updateOrder 修改入口；自动清理无效条件单；执行止盈止损时兼容size（图3逻辑）</p></td>
<td class="confluenceTd" data-local-id="17017d37-8031-4aa5-bdc8-5cac5ce4414d"><p>不自动调整价格；非执行阶段不验证价格是否合理</p></td>
</tr>
<tr data-local-id="cce82df2-53cb-4699-b46b-253dc2445016">
<td class="confluenceTd" data-local-id="4c5ad3a2-08db-446a-bdb9-8127b56be171"><p><strong>Keeper</strong></p></td>
<td class="confluenceTd" data-local-id="47d2e152-99bf-4387-b5a7-de3cb7617c27"><p>只执行：价格满足触发条件 → 执行订单</p>
<ul>
<li><p>PnL ≥ +2500% 接管清算</p></li>
<li><p>有止损单，止损价格合规，PnL ≤ -80% 走止损平仓</p></li>
<li><p>有止损单，止损价格不合规，PnL ≤ -80% 不止损，正常清算逻辑</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="a575f78e-1e26-4219-8391-a764e96a2726"><p>不更新订单；不解决参数过期</p></td>
</tr>
<tr data-local-id="fff20fae-d147-464e-ae2d-f18be45e2245">
<td class="confluenceTd" data-local-id="9c033fd4-b55f-4721-9c88-2e4d315a7235"><p><strong>系统 AutoCancel（建议默认开启）</strong></p></td>
<td class="confluenceTd" data-local-id="bcd039b0-bcc9-40b1-8308-91873b57bf97"><p>在仓位减少/清算时自动取消相关 TPSL</p></td>
<td class="confluenceTd" data-local-id="e08dc314-8229-4599-8d68-a22695bb0e9b"><p>仅针对position size = 0的仓位相关tpsl做清理，不主动对限价单关联的 inactive TPSL 做清理</p></td>
</tr>
</tbody>
</table>

</div>

- **size冲突时：position size \< TP/SL size** → 价格到了则全平，同时清理所有相关tpsl。**position size \> TP/SL size** → 部分成交，保留剩余仓位相关tpsl

### **前端校验矩阵**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="eeb9a10c-3ad9-4ad2-a026-a6e0c78e9d4e">
<tbody>
<tr data-local-id="bc3b8de7-b766-4774-bdef-1e1831f296d2">
<th class="numberingColumn confluenceTh"></th>
<th class="confluenceTh" data-local-id="4a745975-d330-4326-a763-f9c792b75ff7"><p>场景</p></th>
<th class="confluenceTh" data-local-id="b7c79bab-2822-4cb0-93a3-2bf7c9ad9b2f"><p>合规范围</p></th>
<th class="confluenceTh" data-local-id="a37cf017-9d10-4050-b390-5b8ca06ef1e2"><p>UI</p></th>
</tr>
&#10;<tr data-local-id="6ab34a19-0797-4ca0-8de5-b22d10366fd3">
<td class="numberingColumn confluenceTd">1</td>
<td class="confluenceTd" data-local-id="4cb44f67-add7-4acd-ba83-8048c968e7f2"><p>加仓时，TPSL价格限制</p></td>
<td class="confluenceTd" data-local-id="7ab2579a-c69c-4519-8106-2d9705a81edd"><p><strong>Long | Limit 无持仓</strong></p>
<p>max {Limit Price} &lt; TP Price ≤ TP Cap</p>
<p>SL Cap ≤ SL Price &lt; max {Limit Price}</p>
<p><strong>Long | Limit，有持仓 或 Market</strong></p>
<p>Mark Price &lt; TP Price ≤ TP Cap</p>
<p>SL Cap ≤ SL Price &lt; Mark Price</p>
<p><strong>Short | Limit 无持仓</strong></p>
<p>TP Cap ≤ TP Price &lt; min {Limit Price}</p>
<p>min {Limit Price} &lt; SL Price ≤ SL Cap</p>
<p><strong>Short | Limit，有持仓 或 Market</strong></p>
<p>TP Cap ≤ TP Price &lt; Mark Price</p>
<p>Mark Price &lt; SL Price ≤ SL Cap</p></td>
<td class="confluenceTd" data-local-id="471ee023-5505-441b-8260-9bab6b7c9c21"><p>红框 + tooltip；合规范围闭区间的输入框支持回填</p></td>
</tr>
<tr data-local-id="a878b6d3-910a-47d5-a401-3eaa24680bb5">
<td class="numberingColumn confluenceTd">2</td>
<td class="confluenceTd" data-local-id="947d6083-7975-4b91-a132-0ee3070689be"><p>减仓时，TPSL价格限制</p></td>
<td class="confluenceTd" data-local-id="dc2d24e8-6200-4b87-844f-db0221ce6e78"><p>先根据输入价格与市价关系判断其性质为止盈还是止损。</p>
<p><strong>Long｜Trigger Price &gt; Mark Price → 止盈</strong></p>
<p>TP Price ≤ TP Cap</p>
<p><strong>Short｜Trigger Price &lt; Mark Price → 止盈</strong></p>
<p>TP Price ≥ TP Cap</p>
<p><strong>Long｜Trigger Price &lt; Mark Price → 止损</strong></p>
<p>SL Price ≥ SL Cap</p>
<p><strong>Short｜Trigger Price &gt; Mark Price → 止损</strong></p>
<p>TP Price ≤ TP Cap</p></td>
<td class="confluenceTd" data-local-id="c75c8579-3c02-4494-94f7-c51ffa6bca44"><p>红框 + tooltip + 回填</p>
<p>注意输入合法时按钮是<strong>Create Take Profit或Stop Loss Order ，不是市价平仓的close xxx</strong></p></td>
</tr>
<tr data-local-id="a42dd3ae-4c56-489e-9c4a-4ca2e905589f">
<td class="numberingColumn confluenceTd">3</td>
<td class="confluenceTd" data-local-id="b17c2328-b7ec-405b-9ef5-cc636be68fbf"><p>保证金修改时，TPSL价格校验与提示</p></td>
<td class="confluenceTd" data-local-id="e09e8a54-f292-4841-91bf-780c693058e2"><p>这里合规范围是：</p>
<ul>
<li><p><strong>止盈：</strong>新的TP cap优于市价，若原TP Price处于范围外，则明细中提示，并自动变更价格</p></li>
<li><p><strong>止损：</strong>原SL仍优于新的SL Cap，若原SL Price处于范围外，则order以及position中标红为价格无效。</p></li>
</ul>
<p>其他场景如下：</p>
<p><strong>Long｜原TP Price &gt; 新TP Price <sub></sub> Cap <sub></sub> &gt; Mark Price</strong></p>
<p>操作明细中展示<code>TP Price 原 → TP Price新</code> ，成交后更新前端positoin中展示的止盈价格。</p>
<p><strong>Long｜新TP Price <sub></sub> Cap <sub></sub> ≤ Mark Price</strong></p>
<p>黄色警告框提示会立即触发止盈</p>
<p><strong>Long</strong>｜<strong>原SL Price &lt; 新SL Price <sub></sub> Cap</strong></p>
<p>黄色警告框提示止损单会立即失效</p>
<p><strong>Short</strong> ｜<strong>原TP Price &lt; 新TP Price Cap <sub></sub> &lt; Mark Price</strong></p>
<p>操作明细中展示<code>TP Price 原 → TP Price新</code> ，成交后更新前端positoin中展示的止盈价格。</p>
<p><strong>Short｜新TP Price <sub></sub> Cap <sub></sub></strong> ≥ <strong>Mark Price</strong></p>
<p>黄色警告框提示会立即触发止盈</p>
<p><strong>Short｜原SL Price &gt; 新SL Price <sub></sub> Cap <sub></sub></strong></p>
<p>黄色警告框提示止损单会立即失效</p></td>
<td class="confluenceTd" data-local-id="80d37b81-b532-4ccb-9c11-34e5923bf4e2"><p>红框 + tooltip<br />
position 与order价格对应变更至新价格/价格无效状态。</p></td>
</tr>
<tr data-local-id="bdb4dfba-5391-45dc-983c-ad3aae83eed5">
<td class="numberingColumn confluenceTd">4</td>
<td class="confluenceTd" data-local-id="0df9a1bf-5ee1-48bc-93c4-206bcfcbcc30"><p>限价价格修改时，TPSL价格校验与提示</p></td>
<td class="confluenceTd" data-local-id="8127ad19-c242-480f-8b80-7622d4b0197b"><p><strong>Long | orders区价格修改，无持仓</strong></p>
<p>TP Price &gt; Mark Price</p>
<p>SL Price &lt; Mark Price</p>
<p><strong>Long | orders区价格修改，有持仓 或 positions区价格修改</strong></p>
<p>Mark Price &lt; TP Price ≤ TP Cap</p>
<p>SL Cap ≤ SL Price &lt; Mark Price</p>
<p><strong>Short | orders区价格修改，无持仓</strong></p>
<p>TP Price &lt; Mark Price</p>
<p>SL Price &gt; Mark Price</p>
<p><strong>Short | orders区价格修改，有持仓 或 positions区价格修改</strong></p>
<p>TP Cap ≤ TP Price &lt; Mark Price</p>
<p>Mark Price &lt; SL Price ≤ SL Cap</p></td>
<td class="confluenceTd" data-local-id="8a499394-bf77-4792-af24-ac0008699f81"><p>红色tooltip + 按钮提示</p></td>
</tr>
<tr data-local-id="e28b2e48-5d00-4931-a25e-ceb23a0ef6a0">
<td class="numberingColumn confluenceTd">5</td>
<td class="confluenceTd" data-local-id="e68a067b-0b30-4a55-a317-48455f69f121"><p>仓位被动变化时，TPSL价格校验与提示</p></td>
<td class="confluenceTd" data-local-id="fa7e755e-8661-45f9-b837-2587b1fc556f"></td>
<td class="confluenceTd" data-local-id="92470a1d-be63-41a7-bc1c-9c767c818687"></td>
</tr>
</tbody>
</table>

</div>

5.  **页面结构：**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="7dd86f48-a42c-4271-b391-9c7cb713c43d">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr data-local-id="c9b061c0-2147-485c-834c-71547e57af19">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="505b6a3c-aca7-4d69-9bbf-331bab9e255c"><p> </p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="ea45ef21-982b-453a-aa61-922f74d5e364"><p> </p></th>
</tr>
&#10;<tr data-local-id="0a623863-60d2-42e9-a89e-8cecd20c83df">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="6975dec6-cfdf-4464-a24e-01f38b38dc2a"><p>市场详情相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="825a147f3a2466d3c684d421e8a8d30aed7667b64bbb27d585909b9e6f6ef88a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2012.25.57.png?version=2&amp;modificationDate=1763705608950&amp;cacheVersion=1&amp;api=v2" data-height="984" data-width="1663" data-unresolved-comment-count="0" data-linked-resource-id="41648179" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 12.25.57.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="834428f3-7a01-43ec-a41c-c4f96f3cde91" data-media-type="file" width="363" height="214" alt="Screenshot 2025-11-21 at 12.25.57.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="ce5953f9-ba0d-4601-a566-e712cfd4283a"><ol>
<li><p>Carousel</p></li>
<li><p>Market List</p></li>
<li><p>Market Overview</p></li>
<li><p>Chart</p></li>
</ol></td>
</tr>
<tr data-local-id="caf57f79-86cf-47b1-99e0-ec0073b74728">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="44bdad65-6f06-454f-98ca-7524db1fc0d3"><p>用户操作相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ff721e98bc3416388b23003df02fa5f2a19f280ac9f1cf76001f2308b9e146df" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2017.03.28.png?version=1&amp;modificationDate=1763715833462&amp;cacheVersion=1&amp;api=v2" data-height="858" data-width="1616" data-unresolved-comment-count="0" data-linked-resource-id="41713812" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 17.03.28.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="a2ef555e-4f28-43ea-8b17-93bad68399a7" data-media-type="file" width="363" height="192" alt="Screenshot 2025-11-21 at 17.03.28.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="a002f55c-1692-4003-84ae-e2465065134d"><ol>
<li><p>Trade Panel（注意</p></li>
<li><p>Close Position</p></li>
<li><p>Edit Collateral</p></li>
<li><p>Edit Order Price</p></li>
<li><p>Share （不变，可直接复用）</p></li>
</ol></td>
</tr>
<tr data-local-id="59ec4b78-53f9-4dab-a9e1-e80a3a02172f">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="507398aa-d050-4d0a-94f6-c35f280afc7c"><p>交易记录相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6115416c716a7314f43d34b7840c72d4c188615cef9b928bac7c9e4c2c78b7c7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2016.56.19.png?version=1&amp;modificationDate=1763715531292&amp;cacheVersion=1&amp;api=v2" data-height="997" data-width="1665" data-unresolved-comment-count="0" data-linked-resource-id="41582684" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 16.56.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="e3065c53-0521-4aee-9a1a-474e60caf345" data-media-type="file" width="363" height="217" alt="Screenshot 2025-11-21 at 16.56.19.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="1cbfd0d9-9a6d-4bc3-ad61-5e1379086733"><ul>
<li><p>Pool History</p></li>
<li><p>User History - Position/Order/History</p>
<ul>
<li><p>新增列表 Claim（price impact &amp; funding多收取部分以及返佣部分需手动领取）</p></li>
</ul></li>
<li><p>User Portfolio</p></li>
</ul></td>
</tr>
<tr data-local-id="46ffd802-f261-44b1-a290-fcaade70e5f5">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="5e535472-3381-4ef4-a939-ef3039107a83"><p>后续功能新增（不在此次排期）</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="d816dd49-a0fe-4679-86e8-f21ff72b3fdd"><ul>
<li><p>Depth Chart</p></li>
<li><p>Funding History Chart</p></li>
<li><p>其他订单类型（TWAP / Stop Market）</p></li>
<li><p>一键交易（涉及付费rpc，gas token选择，一键交易账户创建以及funding）</p></li>
<li><p>Error Mapping</p></li>
<li><p>高频信息</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

## 二、需求详情

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

1.  **USD数据展示精度：价格同配置表，size fees等2dp，精度不重要的地方kmb**

    1.  适用于：Recent Trade，24h vol; OI; avlb liq

    2.  *\<e.g.\> \$999.12; \$99.12k; \$999.12m*

2.  **百分数展示精度：**2dp，正负号，负红正绿，属于闭区间（-0.01%，+0.01%）则展示+0.00%或 -0.00%

    1.  适用：pnl% chg等

    2.  市场信息栏net rate这里4dp

3.  **币本位展示精度：同v1**

</div>

</div>

### 市场信息区

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="8cd6c410-4fa6-4683-bc2b-972d1a767727">
<tbody>
<tr data-local-id="72762d0b-657f-45da-9612-0c4ed9b5f9ae">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="aa07c776-4a42-4f12-a63a-6b61d94d9877"><p><strong>模块</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="4ff4745d-0881-455e-b60d-6b2e2945061b"><p><strong>需求</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="3bb11ab7-e167-4b91-85b0-9a525f8ccad7"><p><strong>截图</strong></p></th>
</tr>
&#10;<tr data-local-id="450e4626-76a9-4984-86a8-b55f29d8ff64">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="af230fc5-eb65-4910-afd6-538a9b780242"><p>Market List</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="05f28e4a-9da8-4bed-af3e-d492df48cbfb"><ul>
<li><p><strong>通用规则：</strong></p>
<ul>
<li><p><strong>filter，sort，search可叠加，取子集。</strong></p></li>
<li><p><strong>默认排列顺序：BTC/ETH/JPY/SOL/BNB固定前5；剩下的按</strong> <code>rankKey = liquidity * 0.6 + OI * 0.4</code> <strong>desc</strong>;相同者按alphabet <strong>asc</strong></p></li>
<li><p><strong>链式流程：</strong>过滤 → 搜索 (address或symbol)→ 排序 → 分页</p></li>
<li><p><strong>不记filter/sort/搜索词，页面刷新回到默认状态。</strong></p></li>
<li><p><strong>条目数 &lt;= 10</strong> 时不展示分页组件。</p></li>
</ul></li>
<li><p><strong>filter：分类筛选</strong></p>
<ul>
<li><p>选项：All（默认） / Forex / Equities / Indices / Crypto / Commodities / Meme / Newly Listed</p></li>
<li><p>不记状态，刷新后回到 All</p></li>
<li><p>Filter 切换时：</p>
<ul>
<li><p>重置分页至第 1 页</p></li>
<li><p>保留当前搜索词</p></li>
<li><p>保留当前排序状态</p></li>
</ul></li>
</ul></li>
<li><p><strong>Search：</strong></p>
<ul>
<li><p><strong>默认字段：</strong>Search Markets</p></li>
<li><p><strong>模糊搜索：</strong>模糊搜索<strong>仅作用在 ticker字段,</strong> usd为固定字段，不参与匹配。支持ticker的大小写不敏感子串匹配；输入任意字符即可实时过滤列表。优先级为：<strong>精确匹配 &gt; 前缀匹配 &gt; 子串匹配。</strong><br />
<em>&lt;e.g.&gt; /usd为固定字段，输入u不应出现所有池子，只出现 UMA/USD此类ticker中包含U的池子</em></p></li>
<li><p><strong>归一化排序：</strong>排序前移除 <code>/ - _</code> 等符号，只基于字母数字排序。</p></li>
<li><p><strong>输入限制：</strong>字母/数字 最大长度42字符</p></li>
<li><p><strong>地址搜索：</strong>若输入符合 EVM address 格式，则执行地址精确匹配；不支持部分地址匹配。</p></li>
<li><p><strong>UX相关：</strong></p>
<ul>
<li><p>搜索词改变 → 重置分页至第 1 页</p></li>
<li><p>搜索结果为空 → 跟pool页searchbar缺省态一致 <code>No matching results found.</code></p></li>
<li><p>输入时以 <strong>200ms debounce</strong> 实时更新结果。</p></li>
</ul></li>
</ul></li>
<li><p><strong>Sort：</strong>默认排列顺序 BTC/ETH/JPY/SOL/BNB固定前5；剩下的按 rankKey = liquidity * 0.6 + OI * 0.4 desc;相同者按alphabet asc</p>
<ul>
<li><p>排序字段：Price；24h Chg；24h Vol；OI(多空之和）；Avlb Liq（多空加和）；每次<strong>仅允许一个</strong>排序字段生效</p></li>
<li><p>三段式点击：未排序 → desc → asc → 未排序。若被中断则变回默认。<br />
<em>&lt;e.g.&gt;点击Price后 desc，此时点击24h CHG，Price回到初始未排序状态</em></p></li>
<li><p>不记状态（刷新重置）</p></li>
</ul></li>
<li><p><strong>加载方式：lazy load</strong></p></li>
<li><p><strong>表格：这里跟pools一样，后端维护配置表</strong></p>
<ul>
<li><p>Market: USD/JPY + 1000x + Closed</p>
<ul>
<li><p>max leverage 最大可开杠杆倍数：</p>
<ul>
<li><p>ETH/BNB/SOL: 500</p></li>
<li><p>山寨币：50</p></li>
<li><p>美股与指数：25</p></li>
<li><p>FX：1000</p></li>
<li><p>大宗：50</p></li>
</ul></li>
<li><p>Closed：部分闭市状态rwa的标签</p></li>
</ul></li>
<li><p>Price：mark price 预言机价格，展示精度由前端维护配置表</p></li>
<li><p>24h Chg：百分数 2dp 涨绿跌红 带符号 不足+/-0.01%时展示 +0.00% / - 0.00%</p>
<ul>
<li><p><code>24h CHG</code> = 100% x (<code>mark_price</code> - <code>24h_ago_mark_price</code>) / <code>24h_ago_mark_price</code></p></li>
</ul></li>
<li><p>24h Vol：24h 总成交量 <code>24h Vol USD</code> = Σnotional_volume_24h</p></li>
<li><p>OI (L/S) : 持仓的名义价值 多/空</p></li>
<li><p>Avlb Liq (L/S)：池中剩余可用流动性 多/空</p></li>
<li><p>UX：点击整行 跳转到对应市场并自动收起下拉框；点击页面其他区域自动收起下拉框</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="257d7692-e0be-4c6a-98e5-d55366915b86"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1d7eb753e335954aa4639a9f65be66e8d48faf06d31bcb1781dac4dfc589d70b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-24%20at%2010.58.00.png?version=1&amp;modificationDate=1763953112523&amp;cacheVersion=1&amp;api=v2" data-height="877" data-width="1248" data-unresolved-comment-count="0" data-linked-resource-id="42139684" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-24 at 10.58.00.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="0b2a1b56-6895-479d-80e7-9f8786153a93" data-media-type="file" width="180" height="126" alt="Screenshot 2025-11-24 at 10.58.00.png" /></span></td>
</tr>
<tr data-local-id="acb075e8-c349-473d-adcb-9e7f8a4316fb">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="2d193dc3-0ce3-4d63-8d3c-53ce09b157ec"><p>Carousel</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="37624a59-1c06-42ae-87b1-eb8b0333fbca"><ul>
<li><p>按 rankKey = liquidity * 0.6 + OI * 0.4 desc 轮播前20个</p></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="6cb461fb-1590-46b2-acea-ecea9e31ccae"></td>
</tr>
<tr data-local-id="746c96de-8356-4a72-b0d2-c394be5b0a39">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="ec82d157-0c51-4cbb-9198-1cc3db7fabd1"><p>Market Info</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="8127b976-90f8-4cb9-a06e-9ab1ffb0f8da"><ul>
<li><p>Price/24h Chg</p></li>
<li><p>24h High：24h最高成交价</p></li>
<li><p>24h Low：24h最低成交价</p></li>
<li><p>Avlb Liq (L/S)</p></li>
<li><p>OI (L/S)</p></li>
<li><p>1h Net Rate (L/S)</p>
<ul>
<li><p>鼠标hover展示tooltip：Long Positions Net Rate:</p>
<p>8h: -0.469% 24h: -1.408% 365d: -514.21%</p>
<p>Long positions pay a funding fee of -0.027% per hour and a borrow fee of -0.031% per hour.</p>
<p>Short Positions Net Rate:</p>
<p>8h: +0.469% 24h: +1.408% 365d: +514.21%</p>
<p>Short positions receive a funding fee of +0.027% per hour and a borrow fee of +0.031% per hour</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="505b7a7c-8b84-4fda-ada3-a941d8fd8c7e"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4bbc6f6575ff2ed1e17c9a2474f55afd009e4177e4719c96694ac9e1962ba4ec" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-24%20at%2011.40.33.png?version=1&amp;modificationDate=1763955655942&amp;cacheVersion=1&amp;api=v2" data-height="68" data-width="1299" data-unresolved-comment-count="0" data-linked-resource-id="42106910" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-24 at 11.40.33.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="cb15589a-838a-465f-a88d-1dc34ed75036" data-media-type="file" width="453" height="23" alt="Screenshot 2025-11-24 at 11.40.33.png" /></span></td>
</tr>
<tr data-local-id="4087ba0e-455c-4158-8d9f-4826f67e89fc">
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="788d1a2a-5753-4715-94dc-9d0cd9b66c65"><p>Chart</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="5607fb30-43cf-42c6-bffa-4e08f7e82871"><ul>
<li><p>加载时使用蒙层</p></li>
<li><p>历史交易打点</p></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff" data-local-id="4dd614ad-7c82-487a-bc23-d5796e5f80c3"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d1ffc1eca13b7a75ddca928da213f0c2b8ffb0fb42e73b9da65313f1238581f0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-25%20at%2011.38.04.png?version=1&amp;modificationDate=1764041943210&amp;cacheVersion=1&amp;api=v2" data-height="711" data-width="1012" data-unresolved-comment-count="0" data-linked-resource-id="43024394" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-25 at 11.38.04.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="b159ef8d-810a-43bd-8d8f-d965b835482b" data-media-type="file" width="180" height="126" alt="Screenshot 2025-11-25 at 11.38.04.png" /></span></td>
</tr>
</tbody>
</table>

</div>

### 用户操作区

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="center" data-local-id="fb3c0660-a8ca-47f2-9540-821ddcc50f02">
<tbody>
<tr data-local-id="36173889-9d19-4dc0-94d6-85f4cea705ab">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="88ac76e4-bf4f-4ceb-ae98-f40dc33957d9"><p><strong>模块</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="80f7b88f-91dd-46fc-be96-2ab66710ba86"><p><strong>需求</strong></p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="f315894d-02ac-41d8-aea5-4f95aa42f6c5"><p><strong>截图</strong></p></th>
</tr>
&#10;<tr data-local-id="70bd0be5-8807-48af-af2d-17225d2844ed">
<td class="confluenceTd" data-local-id="db3fb39c-a334-4263-984a-7a85406b3cd6"><p>Trade Panel</p></td>
<td class="confluenceTd" data-local-id="b4996db0-8ca4-4654-b763-b44aa9a5682b"><h3 id="TradePage_PRD-0.限价单limitprice输入价格边界修改点：" data-local-id="742e2534-67e6-47f7-a288-e33212445ed2">0. 限价单limit price输入价格边界修改点：</h3>
<p>限价单原0.9x 1.1x mark price删 → 开多需limit price &lt;= mark price; 开空limit price &gt;= mark price 按钮提示删0.9 1.1括号里面的部分，tooltip计算提示min max时取mark price即可</p>
<h3 id="TradePage_PRD-1.止盈止损相关新增交互逻辑" data-local-id="1deee3fc-cbc4-4a9c-93e6-f6c65f87b060">1. 止盈止损相关新增交互逻辑</h3>
<h4 id="TradePage_PRD-1.1TP/SL输入框" data-local-id="bdc3e9bb-347c-411a-a087-3eb920025661"><strong>1.1 TP/SL输入框</strong></h4>
<ul>
<li><p><strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">默认：</span></strong></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">开关：</span></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">无持仓&amp;tpsl时：关闭，整页刷新不记状态，切换多空/订单类型时保留状态。</span></p></li>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">有持仓&amp;tpsl时：打开</span></p></li>
</ul></li>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">输入框：</span></p>
<ul>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">无持仓&amp;tpsl时：TP Price; Gain; SL Price; Loss; - 在止盈右侧的杠杠为蓝色，止损右侧的杠杠为红色</span></p></li>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">已有持仓&amp;tpsl时：</span><strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">下单区</span></strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28"> 用户加仓，自动回填，用户手动关闭tpsl -&gt; 不取消订单，仅视作用户不修改价格</span></p></li>
<li><p><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">已有持仓&amp;tpsl时：</span><strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">下单区 </span></strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">用户加仓，自动回填，用户手动修改tpsl价格 -&gt; </span><strong><span class="inline-comment-marker" data-ref="2215ffa0-cff2-4884-b290-2d9fec5e1c28">只改价格，不改size</span></strong></p></li>
</ul></li>
</ul></li>
<li><p><strong>输入限制：</strong></p>
<ul>
<li><p>最大字符长度：30</p></li>
<li><p>可输入字符：数字，小数点</p></li>
<li><p>小数位数限制：价格输入框与标的资产价格精度同，百分比输入框2dp</p></li>
</ul></li>
<li><p><strong>输入框自动更正：</strong>去除前导零、限制小数位（自动截断）、空输入回退为 <code>默认状态</code></p></li>
<li><p><strong>2种输入方式：</strong>用户在 TP 与 SL 中可切换两种填写方式，价格或盈亏比</p>
<ul>
<li><p>按价格 Price 输入（精度同token decimal）：用户输入 triggerPrice → 联动计算并回填 PnL%</p></li>
<li><p>按PnL%输入（2dp）：用户输入 PnL% → 联动反推并回填Trigger Price</p></li>
<li><p>若<strong>同市场同方向</strong>已有持仓/限价单且绑定了止盈止损单，下单时自动回填当前止盈止损价格。提交成功后同步修改。</p></li>
</ul></li>
<li><p><strong>Price 与 PnL% 与PnL展示数据的联动逻辑</strong><br />
⚠️注意，对于meme这类入场价本身很小的token<strong>开空</strong>时，会出现计算出的<strong>止盈价格为负数</strong>，这代表该价格下永远不会出现pnl超过25倍的情况。所以这是前端当作空值不需验证，仓位那里展示时展示缺省态<strong>-。</strong></p></li>
</ul>
<div class="code panel pdl" style="border-width: 1px;">
<div class="codeContent panelContent pdl">
<pre class="syntaxhighlighter-pre" data-syntaxhighlighter-params="brush: java; gutter: false; theme: Confluence" data-theme="Confluence"><code>pnl% = 多正空负±(P_tpsl - P_entry) / P_entry * L + F/C
Liq Price = [1 ± (1/Lmax - 1/L  - Fees / Size)] * Entry Price
Price_tpsl = 多正空负 P_entry * (1 ± (pnl% / L - F / S))
TP Price Cap = [1 ± (25 * Collateral - Fees) / Size] * Entry Price 
SL Price Cap = [1 ± (-.8 * Collateral - Fees) / Size] * Entry Price
&#10;----------------------------------------------------------------------|
P-Price; L-Leverage; C-Collateral; S-Size; F-费用加和;pnl%-盈亏率带符号</code></pre>
</div>
</div>
<h4 id="TradePage_PRD-1.2按钮/Tooltip显示逻辑" data-local-id="fb9c03c1-1668-4113-a286-bd63dca64e04"><strong>1.2 按钮/Tooltip显示逻辑</strong></h4>
<ul>
<li><p>未连接钱包：<code>Connect Wallet</code> 可点击，触发连接钱包</p></li>
<li><p>已连接钱包：根据输入实时切换</p>
<ul>
<li><p><strong>输入空状态校验：</strong>Input Collateral Delta = Null 或 0：<code>Enter an Amount</code> Disabled</p></li>
<li><p><strong>最小保证金校验：</strong>Input Collateral Amount &lt; 10：<code>Below Min Collateral 10 USDC</code></p></li>
<li><p><strong>【限价单】输入空状态校验：</strong>Input Limit Price = Null 或 0：<code>Enter a Price</code></p></li>
<li><p><strong>【限价单】价格合规性校验：</strong>Input Limit Price_Long &gt; Mark Price 或 Input Limit Price_Short &lt; Mark Price：输入框红色tooltip提示 + 按钮 <strong>开多则为</strong> <code>Above Max Limit Price</code> 或 <strong>开空则为</strong><code>Below Min Limit Price</code></p></li>
<li><p><strong>余额校验：</strong>Input Collateral Delta &gt; 钱包余额：输入框自动更正</p></li>
<li><p><strong>最大交易额校验：</strong>Size Delta ≥ Max{0, Min{Avlb Liq, Max Position Size}}：<code>Above Max Position Size [Max Position Size($)]</code></p>
<ul>
<li><p><strong>Max Position Size = Max{0, Min{Avlb Liq, Max Position Size}}</strong></p></li>
<li><p>Avlb Liq：池中剩余可用流动性，分多空</p></li>
<li><p>Max Position Size：合约配置参数。限制用户单边最大未平仓头寸。（合约没配前端先写死）</p></li>
</ul></li>
<li><p>【<strong>止盈止损单</strong>】<strong>输入价格/PnL%合规性校验：</strong></p>
<p><strong>若输入不合规，另2个联动计算的输入框&amp;展示的数据保持缺省态，不合规处线框变为红色，并展示红色tooltip（样式同limit price的）</strong></p>
<ul>
<li><p><strong>市价开多止盈/止损：</strong></p>
<ul>
<li><p>TP Price ≤ Mark Price：按钮 <code>TP Price Below Mark Price</code>Disabled，tooltip提示：<code>Below Mark Price [预言机价格($)]</code></p></li>
<li><p>TP Price &gt; TP Price Cap：按钮<code>Above Max TP Price</code>Disabled，提示tooltip：<code>Max TP Price [Max TP Price($)]</code> <strong>点击自动回填</strong></p>
<ul>
<li><p><strong>TP Price Cap = [(25 * Collateral - Fees) / Size + 1] * Entry Price</strong></p>
<ul>
<li><p>PnL% = 2500% = [(TP Price Cap - Entry Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ 计算时考虑已有持仓</p></li>
</ul></li>
</ul></li>
<li><p>SL Price ≥ Mark Price: 按钮</p>
<p><code>SL Price Above Mark Price [预言机价格($)]</code></p>
<p>Disabled，tooltip提示：<code>Above Mark Price [预言机价格($)]</code></p></li>
<li><p>SL Price &lt; Min SL Price：按钮<code>Below Min SL Price </code>Disabled，提示tooltip：<code>Min SL Price [Min SL Price($)]</code>自动回填</p>
<ul>
<li><p><strong>Min SL Price = [(-0.8 * Collateral - Fees) / Size + 1] * Entry Price</strong></p>
<ul>
<li><p>PnL% = -80% = [(Min SL Price - Entry Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ 在<strong>已有持仓</strong>的情况下取的是<strong>合并仓位</strong>后的新值；<strong>Fees带符号</strong></p></li>
</ul></li>
</ul></li>
</ul></li>
<li><p><strong>市价开空止盈/止损：</strong></p>
<ul>
<li><p>TP Price ≥ Mark Price：按钮<code>TP Price Above Mark Price</code>disabled，tooltip提示：<code>Above Mark Price [预言机价格($)]</code></p></li>
<li><p>TP Price &lt; Max TP Price：按钮<code>Below Min TP Price</code>Disabled，提示tooltip：<code>Min TP Price [Max TP Price($)]</code>点击回填</p>
<ul>
<li><p><strong>Max TP Price = [1 - (25 * Collateral - Fees) / Size] * Entry Price</strong></p>
<ul>
<li><p>PnL% = 2500% = [(Entry Price - Max TP Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ 在<strong>已有持仓</strong>的情况下取的是<strong>合并仓位</strong>后的新值，注意<strong>Fees带符号的</strong></p></li>
</ul></li>
</ul></li>
<li><p>SL Price ≤ Mark Price: 按钮 <code>SL Price Below Mark Price </code>Disabled，tooltip提示：<code>Below Mark Price [预言机价格($)]</code></p></li>
<li><p>SL Price &gt; Min SL Price：按钮<code>Above Max SL Price</code>Disabled，提示tooltip<code>Max SL Price [Min SL Price($)]</code>点击回填</p>
<ul>
<li><p><strong>Min SL Price = [1 - (-0.8 * Collateral - Fees) / Size] * Entry Price</strong></p>
<ul>
<li><p>PnL% = -80% = [(Entry Price - Min SL Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ 在<strong>已有持仓</strong>的情况下取的是<strong>合并仓位</strong>后的新值；<strong>Fees带符号</strong></p></li>
</ul></li>
</ul></li>
</ul></li>
<li><p><strong>限价开多或开空同市价单止盈/止损：Entry Price/Fees计算时注意合并Limit Price。以限价单开多为例：</strong></p>
<ul>
<li><p>下单时size = 0，且TP Price ≤ <strong>max {Limit</strong> <strong>Price}</strong>：按钮 <code>TP Price Below Highest Limit Price</code>Disabled，tooltip提示：<code>Below Highest Limit Price [该市场所有同方向限价单最高价格($)]</code></p></li>
<li><p>下单时size ≠ 0，且TP Price ≤ <strong>Mark Price</strong>：按钮</p>
<p><code>按钮TP Price Above Mark Price</code>disabled，tooltip提示：<code>Above Mark Price [预言机价格($)]</code></p></li>
<li><p>TP Price &gt; TP Price Cap：按钮<code>Above Max TP Price</code>Disabled，提示tooltip：<code>Max TP Price [Max TP Price($)]</code>点击回填</p>
<ul>
<li><p><strong>Max TP Price = [(25 * Collateral - Fees) / Size + 1] * Entry Price</strong></p>
<ul>
<li><p>PnL% = 2500% = [(Max TP Price - Entry Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ Entry Price<strong>无仓位</strong>取Limit Price。在<strong>已有持仓</strong>的情况下取的是<strong>合并仓位</strong>后的新值，注意<strong>是该订单于当前仓位合并，不是所有限价单与当前仓位合并</strong></p></li>
</ul></li>
</ul></li>
<li><p>下单时size = 0，且SL Price ≥ <strong>max {Limit</strong> <strong>Price}</strong></p>
<p>: 按钮 <code>SL Price Above Highest Limit Price</code>Disabled，tooltip提示：<code>Above Limit Price [价格($)]</code></p></li>
<li><p>下单时size ≠ 0，且SL Price ≥ <strong>Mark Price</strong>：按钮</p>
<p><code>按钮SL Price Above Mark Price</code>disabled，tooltip提示：<code>Above Mark Price [预言机价格($)]</code></p></li>
<li><p>SL Price &lt; Min SL Price：按钮<code>Below Min SL Price</code>Disabled，提示tooltip：<code>Min SL Price [Min SL Price($)]</code>点击回填</p>
<ul>
<li><p><strong>Min SL Price = [(-0.8 * Collateral - Fees) / Size + 1] * Entry Price</strong></p>
<ul>
<li><p>PnL% = -80% = [(Min SL Price - Entry Price) / Entry Price * Size + Fees] / Collateral</p></li>
<li><p><strong>Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee</p></li>
<li><p>⚠️ 在<strong>已有持仓</strong>的情况下取的是<strong>合并仓位</strong>后的新值；<strong>Fees带符号</strong></p></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li><p>未Approve 或 Approved max spending cap不足：<code>Approve USDC Spending</code>Enabled</p></li>
<li><p>正在Approve：<code>Approving [Spinner图标]</code> Disabled</p></li>
<li><p>校验&amp;计算完成后可质押：<code>Long / Short 标的资产</code> Enabled</p></li>
<li><p>重新计算中：<code>Finalizing Quote [spinner] </code>Disabled</p></li>
<li><p>正在开多/空：<code>Longing/Shorting [某标的ticker][spinner]</code>Disabled</p></li>
</ul></li>
</ul>
<p><strong>1.3 校验链路按顺序执行：</strong></p>
<ol>
<li><p><strong>格式校验</strong>：合法数字 + 小数点位数合法</p>
<ul>
<li><p>最大长度 30</p></li>
<li><p>小数点 ≤ token精度 自动截断</p></li>
<li><p>Input Collateral &gt; 0</p></li>
<li><p>Input Limit Price不为空等其他价格相关校验</p></li>
</ul></li>
<li><p><strong>余额校验</strong>：Input ≤ 用户钱包中 USDC 余额</p></li>
<li><p><strong>最小保证金校验：</strong>Collateral Input &gt; 10 <strong>USDC</strong></p></li>
<li><p><strong>最大交易额校验</strong>：Position Size ≤ 剩余可开仓位头寸；且Position Size ≤ 池子剩余可用流动性（跟reserve factor相关）</p></li>
<li><p><strong>是否需要批准：</strong>allowance &lt; input，则进入approve流程</p>
<ol>
<li><p>按钮<code>Approve USDC Spending</code></p></li>
<li><p>点击approve</p>
<p>→ 钱包弹窗</p>
<p>→ 按钮<code>Approving USDC Spending</code></p>
<p>→ Pending Toast：标题 <code>[approve icon]</code> + <code>Approval</code></p>
<p>；文案<code>Approving token spending</code>+ <code>[spinner图标]</code></p></li>
<li><p>→ <strong>成功:</strong> Toast 文案变为<code>Approval</code> + <code>Completed[tick]</code>；allowance 在 approve 成功后立即读取链上最新数值，直到大于 input 才进入 Deposit 状态；按钮变为：<code>Long/Short 标的资产ticker</code>（可点击）<br />
→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p></li>
</ol></li>
<li><p><strong>风险/可交易状态校验：</strong>池 paused → 禁止操作</p>
<ol>
<li><p><span class="inline-comment-marker" data-ref="439b814c-9549-4088-9979-98a9130bfc12">所有操作按钮disabled。market仍展示在列表中。</span></p></li>
</ol></li>
<li><p><strong>计算 Output：</strong>与原来同</p></li>
<li><p><strong>按钮状态刷新：</strong>全部通过 → 进入表单提交流程：</p>
<ol>
<li><p><code>Long/Short XXX</code>按钮可点击</p></li>
<li><p>用户点击按钮<br />
-&gt; 钱包弹窗</p>
<p>→ 按钮<code>[Longing/Shorting xxx] </code>；输入框 locked；面板不可交互</p>
<p>-&gt; <strong>Pending Toast</strong>：标题<code>[token icon] </code>+ <code>订单类型</code>;文案<code>Submitting</code>+ <code>[Spinner]</code>；其中，订单类型分为：Market Order; Limit Order; Take Profit Order; Stop Loss Order; TP/SL Order（止盈止损同时有的）</p></li>
<li><p>→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p>
<p>→ <strong>成功：Keeper推送成功事件，pending变为成功Toast：</strong>⚠️成交字段从<code>Submitted</code>变为<code>Filled</code>；<strong>同时触发数据刷新</strong>：recent trades，portfolio，position / order / history等</p></li>
</ol></li>
<li><p><strong>滑点/费率部分不变。price impact部分判断以及提示先隐藏。</strong></p>
<ol>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">滑点编辑：</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">加减仓通用，全局控制</span></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">acceptable price校验逻辑：</span></strong></p>
<ol>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">市价开仓：</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">Acceptable Price = Mark Price × (1 + Price Impact) ← 反映失衡 × (1 ± Slippage) ← 反映波动容忍，Price Impact </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">展示为0</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">，但Acceptable Price </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">用实际price impact与slippage共同</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">做边界检查</span></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">限价开仓：</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">Acceptable Price = Mark Price × (1 + Price Impact) ← 反映失衡，限价limit price本身就是容忍价格，不存在滑点这一概念。Price Impact </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">展示为0</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">，但Acceptable Price </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">用实际price impact</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">做边界检查</span></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">市价减仓：</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">持仓期间累计的Net Price Impact </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">已经计入PnL显示</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">，Acceptable Price </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">只校验滑点</span></strong></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">TP/SL减仓：</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">用 </span><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">default_impact 校验（止盈impact为0，止损为负无穷，为保证执行成功），止盈止损订单无滑点概念。</span></strong></p></li>
</ol></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">price impact收费逻辑：</span></strong></p>
<ol>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">开仓时</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">: 入场价格 = Oracle Mark Price(无影响)</span></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">持仓期间</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">: Price Impact随OI失衡实时变化(但不收费)</span></p></li>
<li><p><strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">平仓时</span></strong><span class="inline-comment-marker" data-ref="eb61e9f6-530d-4168-a206-419ac2289732">: 结算净价格影响(开仓→平仓整体对市场的影响) 有上限保护(如50 bps),超额部分转为rebate</span></p></li>
</ol></li>
</ol></li>
</ol></td>
<td class="confluenceTd" data-local-id="48decbec-47dd-4f56-9b2a-5941ef86fa9d"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4b18dc64a40929d48a676a7da0d0d50a9b5e417a92de1d1bfcd5c4839c9ff0e7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-28%20at%2012.18.16.png?version=1&amp;modificationDate=1764303506538&amp;cacheVersion=1&amp;api=v2" data-height="746" data-width="406" data-unresolved-comment-count="0" data-linked-resource-id="45711364" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-28 at 12.18.16.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="d3b90954-92d5-4df8-a076-a9e428ae481d" data-media-type="file" width="180" height="330" alt="Screenshot 2025-11-28 at 12.18.16.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e4f4387cd195223f4d8c2d2af53f9a520b7772a8b1e1ab152957b494ffadcb7e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-28%20at%2012.19.29.png?version=1&amp;modificationDate=1764317048898&amp;cacheVersion=1&amp;api=v2" data-height="845" data-width="513" data-unresolved-comment-count="0" data-linked-resource-id="45940737" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-28 at 12.19.29.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="aa02d78d-5f41-4390-ae15-d76d0e91c1f4" data-media-type="file" width="180" height="296" alt="Screenshot 2025-11-28 at 12.19.29.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="80e5d49089a33c39813f24ff4c782058d3417b0174bb591a2b238c593d5e1cc8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-28%20at%2012.19.25.png?version=2&amp;modificationDate=1764317072515&amp;cacheVersion=1&amp;api=v2" data-height="794" data-width="780" data-unresolved-comment-count="0" data-linked-resource-id="45940743" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-28 at 12.19.25.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="ac6bbbaa-a978-45f1-b111-9a41c44e44d4" data-media-type="file" width="180" height="182" alt="Screenshot 2025-11-28 at 12.19.25.png" /></span>
<p>👈合规范围：</p>
<p><strong>Long | size = 0</strong></p>
<p>max {Limit Price} &lt; TP Price ≤ Cap</p>
<p>SL Cap ≤ SL Price &lt; max {Limit Price}</p>
<p><strong>Long | size ≠ 0</strong></p>
<p>Mark Price &lt; TP Price ≤ Cap</p>
<p>SL Cap ≤ SL Price &lt; Mark Price</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="824e08eacd5afdc765fbd32d88d9d1b925746a216e1edcfa05f170ba802ea3c0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/image-20251126-150039.png?version=1&amp;modificationDate=1764169250116&amp;cacheVersion=1&amp;api=v2" data-height="3888" data-width="1872" data-unresolved-comment-count="0" data-linked-resource-id="44793865" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251126-150039.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="372ea3cf-5d06-499e-a67d-4cf0768cf8dc" data-media-type="file" width="180" height="375" alt="image-20251126-150039.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b809df3b97dd93df945234db6e9af31119a81cd5365ee99534ebd0fdb7d13e98" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-26%20at%2023.16.41.png?version=1&amp;modificationDate=1764170244408&amp;cacheVersion=1&amp;api=v2" data-height="916" data-width="1277" data-unresolved-comment-count="0" data-linked-resource-id="44826635" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-26 at 23.16.41.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="816c522d-2f2c-4708-b2b9-60b77cfd8b1e" data-media-type="file" width="180" height="128" alt="Screenshot 2025-11-26 at 23.16.41.png" /></span></td>
</tr>
<tr data-local-id="e327ebc5-0971-43e3-a3a1-26146f6a7f1a">
<td class="confluenceTd" data-local-id="52ed06d4-80fa-4c58-9305-7bbfa5498c2f"><p>Close Position</p></td>
<td class="confluenceTd" data-local-id="5ce3c47b-3beb-4c38-a458-24c663b9d17c"><p>总体修改点：</p>
<ul>
<li><p>You Receive展示的不再是collateral delta 而是总的</p></li>
<li><p>新增Keep Leverage开关，默认非等比减仓（新增），开关打开后为等比减仓（原）；明细中因此新增一行展示杠杆倍数变化</p></li>
<li><p>新增<strong>市价减仓</strong>滑点设置（下单区已有逻辑可直接复用）<br />
⚠️由于触发单的定义，止盈止损<strong>触发单</strong>是<strong>不涉及</strong>滑点的，因为执行价格需要严格处于触发价格区间内，这一点是其与限价单的本质区别。</p></li>
<li><p>新增止盈止损tab</p></li>
</ul>
<h3 id="TradePage_PRD-1.KeepLeverage功能" data-local-id="44eddf43-09a9-40e7-9e27-af7db2f92fec">1. Keep Leverage功能</h3>
<ul>
<li><p>默认：开关关闭，开关状态全局保留。</p></li>
<li><p>状态：<strong>全仓</strong>平时，开关<strong>关闭</strong>，同时<strong>disable</strong>。若用户先打开开关，再点击max全平，则开关变为关闭。用户修改size至减仓非全平仓后，回到上一次保留的打开状态。</p></li>
<li><p>计算逻辑：核心区别为是否退回减仓的保证金部分。开关关闭时，receive仅为<strong>扣除费用后的PnL</strong>，保证金不比变。PnL不足支付费用时从剩余保证金中扣。开关打开，即为v1等比减仓逻辑。</p></li>
</ul>
<h3 id="TradePage_PRD-2.Receive计算" data-local-id="cbd7956c-113b-49b1-ac19-dcdf6b6755c1">2. Receive计算</h3>
<ul>
<li><p>默认状态：0</p></li>
<li><p>计算逻辑：</p>
<ul>
<li><p><strong>Receive =</strong> <strong>Max{</strong>0, <code>Reduce Collateral Delta</code> + <code>Fees</code> + <code>RPnL</code><strong>}</strong></p></li>
<li><p>其中，Keep Leverage开关<strong>关闭</strong>时，Reduce Collateral Delta = <strong>0</strong> ；Keep Leverage开关<strong>打开</strong>时，Reduce Collateral Delta = Reduce Size Delta / Leverage</p></li>
<li><p>Fees = Price Impact + Borrow Fee + Funding Fee + Close Fee 带符号的 正代表rebate，负代表payment</p></li>
<li><p>RPnL = Reduce Size Delta * ± (Trigger Price - Entry Price) / Entry Price；多取正号空取负号；Trigger Price代表市价减仓时的Mark Price以及触发价减仓时的止盈止损价。</p></li>
</ul></li>
</ul>
<h3 id="TradePage_PRD-3.减仓明细" data-local-id="a6a8e3e0-801d-4c6d-85e9-818c1b37ef1c">3. 减仓明细</h3>
<ul>
<li><p><strong>Leverage：默认展示当前仓位杠杆，</strong>2dp，变化值影响2位小数时，展示<code>当前lev → 变化后lev</code>。前后数值没变化到2dp时，仅展示 <code>lev</code><br />
e.g. 实际杠杆倍数10.011x → 10.014x 相当于没变化，展示<code>10.01x</code>；10.011x → 10.015x 展示<code>10.01x → 10.02x</code></p></li>
<li><p><strong>Size：原有逻辑不变，</strong>有输入后按比例减仓</p></li>
<li><p><strong>Collateral：同leverage，默认展示当前仓位保证金，2dp。变化值影响2位小数时，展示</strong><code>当前coll → 变化后coll</code>。</p>
<ul>
<li><p><strong>计算逻辑变为：</strong> Collateral = 原Collateral - <code>Reduce Collateral Delta</code> + Min(Reduce Collateral Delta + <code>Fees</code> + <code>RPnL</code>, 0)</p></li>
<li><p>其中，Reduce Collateral Delta = <strong>0</strong> if Keep Leverage <strong>Off</strong>, Reduce Collateral Delta = <strong>Size Delta/Lev</strong> if Keep Leverage <strong>On</strong></p></li>
<li><p>+ Min(Reduce Collateral Delta + <code>Fees</code> + <code>RPnL</code>, 0)代表如果返给用户的结算保证金+实现盈亏不足支付费用，则需从剩余保证金中扣除。其中Fees包含Price Impact，Borrow，Funding，Close Fee</p></li>
<li><p>RPnL = 多正空负±(P_execute - P_entry) / P_entry * Size；P_execute市价单为mark price，触发单为填入的止盈止损价</p></li>
</ul></li>
<li><p><strong>PnL：</strong>展示未实现盈亏（未实现盈亏率），美元价值以及百分数精度均为2dp。</p>
<ul>
<li><p><strong>默认状态变为：市价平仓size input = null，</strong>则默认展示<code>全仓位的gross pnl以及pnl%（不算费用）</code><strong>，触发价平仓size input 以及trigger price input = null，</strong>则默认展示<code>$0.00 (0.00%)</code><strong>; size input不为空，trigger price input = null时，</strong><code>按input price = mark price去计算并展示</code><strong>。</strong></p></li>
<li><p>计算逻辑不变，仍展示不算费用的gross pnl 以及pnl%</p></li>
</ul></li>
<li><p><strong>Liq Price：价格展示精度同前端配置表</strong></p>
<ul>
<li><p><strong>默认状态：同PnL，触发价平仓只要size input = null，就默认展示当前liq price。size input不为空，trigger price input = null，按input = mark price算 并展示</strong></p></li>
<li><p>计算逻辑不变，多仓：Liq Price = Entry Price * (1/L<sub>max</sub> - 1/L - Fees / Size + 1)；空仓：Liq Price = Entry Price * (1 - (1/L<sub>max</sub> - 1/L - Fees / Size))；其中 Fee = Close Fee + Borrow Fee + Funding Fee + Price Impact + Liq Fee。<strong>注意</strong>这里减仓后的liq price计算时，<strong>entry price</strong>，<strong>Leverage</strong>，<strong>Fees</strong>，<strong>Size</strong>要用减仓后模拟的新值（比如说fees减仓后borrow，funding，price impact会清零），同时注意keep lev on 开关状态对其计算逻辑的影响。</p></li>
</ul></li>
<li><p><strong>Slippage：</strong>仅针对<strong>市价减仓</strong>滑点新增设置（下单区已有逻辑可直接复用）</p></li>
<li><p><strong>Mark Price：价格展示精度同前端配置表</strong></p></li>
<li><p><strong>Entry Price：价格展示精度同前端配置表 减仓时entry price不变，全平时变为缺省台态 -</strong></p></li>
<li><p><strong>Fees：</strong>新增Price Impact，Funding Fee Due这两个</p></li>
</ul>
<h3 id="TradePage_PRD-4.按钮状态" data-local-id="4eb008ed-c4c4-4002-ba35-a1b91f8ae0d8">4. 按钮状态</h3>
<ul>
<li><p><strong>输入空状态校验：</strong>Input Collateral Delta = Null 或 0：<code>Enter an Amount</code> Disabled</p></li>
<li><p><strong>【TPSL单】输入空状态校验：</strong>Input Trigger Price = Null 或 0：<code>Enter a Price</code> Disabled</p></li>
<li><p><strong>仓位头寸校验：</strong>Input Size Delta &gt; Size：输入框自动更正</p></li>
<li><p><strong>最小剩余保证金校验：</strong>Input Collateral Amount &lt; 10：<code>Below Min Residual Collateral 10 USDC</code></p></li>
<li><p><strong>【TPSL单】价格合规性校验（这里同加仓时的 min -80%</strong> &lt;= <strong>PnL% &lt;= max 2500%限制）：</strong>若<strong>开多</strong>Trigger Price_Long &lt; Mark Price 或者<strong>开空</strong>Trigger Price_Short &gt; Mark Price,则视为<strong>止损单</strong>，要求触发价格优于<strong>亏损率80%的离场价；</strong>若<strong>开多</strong>Trigger Price_Long &gt; Mark Price 或者<strong>开空</strong>Trigger Price_Short &lt; Mark Price,则视为<strong>止盈单</strong>，要求触发价格劣于<strong>盈利率2500%的离场价</strong></p>
<ul>
<li><p><strong>开多TP｜Input Trigger Price &gt; Mark Price</strong>：</p>
<p>Input TP Price &gt; Max TP Price：按钮<code>Above Max TP Price</code>Disabled，输入框红色tooltip提示：<code>Max TP Price [Max TP Price($)]</code> 点击自动回填</p>
<ul>
<li><p><strong>Max TP Price = [(25 * Collateral - Fees) / Size + 1] * Entry Price</strong></p></li>
<li><p><strong>Fees，Size，Collateral取的都是Delta变化值。其中，Fees</strong> = Funding Fee + Borrow Fee + Price Impact + Close Fee <strong>带符号</strong></p></li>
</ul></li>
<li><p><strong>开多SL｜Input Trigger Price &lt; Mark Price</strong>：<br />
Input SL Price &lt; Min SL Price: <strong></strong> 输入框红色tooltip提示<code>Min SL Price [Min SL Price ($)]</code>点击自动回填 + 按钮 <code>Below Min SL Price</code>disabled</p>
<ul>
<li><p><strong>Min SL Price = [(-0.8 * Collateral - Fees) / Size + 1] * Entry Price</strong></p></li>
</ul></li>
<li><p><strong>开空TP｜Input Trigger Price &lt; Mark Price</strong>：</p>
<p>Input TP Price &lt; Max TP Price：按钮<code>Below Min TP Price</code>Disabled，输入框红色tooltip提示：<code>Min TP Price [Max TP Price($)]</code> 点击自动回填</p>
<ul>
<li><p><strong>Max TP Price = [1 - (25 * Collateral - Fees) / Size] * Entry Price</strong></p></li>
</ul></li>
<li><p><strong>开空SL｜Input Trigger Price &gt; Mark Price</strong><br />
Input SL Price &gt; Max SL Price: <strong></strong> 输入框红色tooltip提示<code>Max SL Price [Max SL Price ($)]</code>点击自动回填 + 按钮<code>Above Max SL Price</code>disabled</p>
<ul>
<li><p><strong>Max SL Price = [1 - (-0.8 * Collateral - Fees) / Size] * Entry Price</strong></p></li>
</ul></li>
<li><p><strong>输入合法：</strong>按钮<code>Create Take Profit或Stop Loss Order</code></p></li>
</ul></li>
<li><p><strong>最大交易额校验：</strong>Est. Receive ≥ Avlb Liq：<code>Insufficient Liquidity]</code> disabled</p>
<ul>
<li><p>Avlb Liq：池中剩余可用流动性，分多空</p></li>
</ul></li>
<li><p><strong>未Approve 或 Approved max spending cap不足</strong>（除非用户手动操作，一般平仓的时候不会出现这种情况）<strong>：</strong><code>Approve USDC Spending</code>Enabled</p></li>
<li><p>正在Approve：<code>Approving [Spinner图标]</code> Disabled</p></li>
<li><p>校验&amp;计算完成后可质押：<code>Long / Short 标的资产</code> Enabled</p></li>
<li><p>重新计算中：<code>Finalizing Quote [spinner] </code>Disabled</p></li>
<li><p>正在开多/空：<code>Longing/Shorting [某标的ticker][spinner]</code>Disabled</p></li>
</ul>
<h3 id="TradePage_PRD-5.校验流程" data-local-id="e0a122a1-818d-451e-bc11-672b9786da55"><strong>5. 校验流程</strong></h3>
<ol>
<li><p><strong>格式校验</strong>：合法数字 + 小数点位数合法</p>
<ul>
<li><p>最大长度 30</p></li>
<li><p>小数点 ≤ token精度 自动截断</p></li>
<li><p>Input Size &gt; 0</p></li>
<li><p>Input Trigger Price不为空等其他价格相关校验</p></li>
</ul></li>
<li><p><strong>余额校验</strong>：Input Size ≤ 用户仓位USDC头寸</p></li>
<li><p><strong>最小保证金校验：</strong>Collateral - Collateral Delta &gt;= 10 <strong>USDC</strong></p></li>
<li><p><strong>最大交易额校验</strong>：Est. Receive ≤ 池子剩余可用流动性</p></li>
<li><p><strong>是否需要批准：</strong>allowance &lt; input，则进入approve流程</p>
<ol>
<li><p>按钮<code>Approve USDC Spending</code></p></li>
<li><p>点击approve</p>
<p>→ 钱包弹窗</p>
<p>→ 按钮<code>Approving USDC Spending</code></p>
<p>→ Pending Toast：标题 <code>[approve icon]</code> + <code>Approval</code></p>
<p>；文案<code>Approving token spending</code>+ <code>[spinner图标]</code></p></li>
<li><p>→ <strong>成功:</strong> Toast 文案变为<code>Approval</code> + <code>Completed[tick]</code>；allowance 在 approve 成功后立即读取链上最新数值，直到大于 input 才进入 Deposit 状态；按钮变为：<code>Long/Short 标的资产ticker</code>（可点击）<br />
→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p></li>
</ol></li>
<li><p><strong>风险/可交易状态校验：</strong>池 paused → 禁止操作</p></li>
<li><p><strong>计算 Output：</strong>与原来同</p></li>
<li><p><strong>按钮状态刷新：</strong>全部通过 → 进入表单提交流程：</p>
<ol>
<li><p><code>Long/Short XXX</code>按钮可点击</p></li>
<li><p>用户点击按钮<br />
-&gt; 钱包弹窗</p>
<p>→ 按钮<code>[Longing/Shorting xxx] </code>；输入框 locked；面板不可交互</p>
<p>-&gt; <strong>Pending Toast</strong>：标题<code>[token icon] </code>+ <code>订单类型</code>;文案<code>Submitting</code>+ <code>[Spinner]</code>；其中，订单类型分为：Market Order; Limit Order; Take Profit Order; Stop Loss Order; TP/SL Order（止盈止损同时有的）</p></li>
<li><p>→ <strong>用户拒绝导致失败：</strong>failed toast <code>Request rejected by user.</code></p>
<p>→ <strong>其他原因导致失败：</strong><code>Transaction failed. Please try again later.</code><br />
-&gt; 超时<strong>30s：</strong><code>Transaction pending. Please try again later.</code></p>
<p>→ <strong>成功：Keeper推送成功事件，pending变为成功Toast：</strong>⚠️成交字段从<code>Submitted</code>变为<code>Filled</code>；<strong>同时触发数据刷新</strong>：recent trades，portfolio，position / order / history等</p></li>
</ol></li>
<li><p><strong>price impact部分判断以及提示先隐藏。</strong></p></li>
<li><p><span class="inline-comment-marker" data-ref="320ee907-7125-4527-bb6a-62b20677882c">闭市时：不支持任何操作。Market右侧标签展示Closed；按钮</span><span class="inline-comment-marker" data-ref="320ee907-7125-4527-bb6a-62b20677882c"><code>Market Opens in 0D:2H:13M:14S </code></span><span class="inline-comment-marker" data-ref="320ee907-7125-4527-bb6a-62b20677882c">disabled; close按钮，cancel，edit图标 也禁用 - 鼠标hover展示tooltip：</span><span class="inline-comment-marker" data-ref="320ee907-7125-4527-bb6a-62b20677882c"><code>Trading and all related actions are unavailable during market closure.Market reopens in 0D:2H:13M:14S.</code></span></p></li>
</ol></td>
<td class="confluenceTd" data-local-id="c0925535-7ff2-4f64-88a9-63f954f1bfe3"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2495e811b5eb78f744acbfd9aa6d54f132317c266c19cedba18e14af84266326" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-28%20at%2016.43.08.png?version=1&amp;modificationDate=1764319556786&amp;cacheVersion=1&amp;api=v2" data-height="925" data-width="581" data-unresolved-comment-count="0" data-linked-resource-id="45940760" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-28 at 16.43.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="daa2bc3a-7190-46a2-9e3a-ddaf30d35916" data-media-type="file" width="429" height="683" alt="Screenshot 2025-11-28 at 16.43.08.png" /></span>
<p><em><span style="background-color: rgb(220,223,228);">👈⚠️ TP/SL无滑点概念</span></em></p>
<p><em><span style="background-color: rgb(220,223,228);">trigger price 被命中 → orderTriggered → keeper 提交市价平仓 → 以市场价格成交</span></em></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2b40a236ff2e03a670f2b21fdb04f35ac9da39fcc4d2566642a54793b7187d8d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-06%20at%2015.22.53.png?version=1&amp;modificationDate=1765005879763&amp;cacheVersion=1&amp;api=v2" data-height="466" data-width="726" data-unresolved-comment-count="0" data-linked-resource-id="50364448" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-06 at 15.22.53.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="34368183-ad61-40a0-8584-764c664913e8" data-media-type="file" width="180" height="115" alt="Screenshot 2025-12-06 at 15.22.53.png" /></span></td>
</tr>
<tr data-local-id="3aff702c-4593-480a-a716-268200f99cfd">
<td class="confluenceTd" data-local-id="26cef1e9-c279-49cf-8c33-04c7e910ebb1"><p>Edit Collateral</p></td>
<td class="confluenceTd" data-local-id="a4c11151-a2de-47f5-b482-ff15ca500717"><ol>
<li><p><strong>输入框：单位都变成USDC，包括max那里</strong></p></li>
<li><p><strong>验证：</strong></p>
<ol>
<li><p>添加保证金时min collateral从10$变成10 <strong>USDC</strong></p></li>
<li><p><strong>移除保证金时，新止盈止损价格边界会变窄，同时强平价也会变窄。此时需注意原来设置的止盈止损价格，如比新的价格边界宽泛，需计算展示并重新校验合规性以及提交。校验包括：</strong></p>
<ol>
<li><p>先计算新的最大可移除USDC的<strong>数量</strong>上限Max<br />
<strong>Max_ReduceCollateralDelta_Amount = Max{0, Min {Collateral_Amount - 10, Collateral - Size / Max Open Leverage}}</strong></p></li>
<li><p>如果移除保证金数量 &lt; Max, 计算新的<strong>止盈止损价格边界</strong>以及强平价并验证：</p>
<ol>
<li><p><strong>多空止盈价格校验无效：</strong>如果开多<strong>原TP Price &gt; 新TP Price<sub>多Max</sub> &gt; Mark Price，</strong>或者开空<strong>原TP Price &lt; 新TP Price<sub>空Min</sub> &lt; Mark Price，则明细中展示</strong><code>TP Price 原 → TP Price </code><strong>新，成交后更新前端positoin中展示的止盈价格。</strong></p></li>
<li><p><strong>多空止盈价格校验不合规：</strong>如果开多<strong>新TP Price<sub>多Max</sub> &lt;= Mark Price，</strong>或者开空<strong>新TP Price<sub>空Min</sub> &gt;= Mark Price，则黄色警告框提示：</strong></p>
<p><code>New TP Price Cap is worse than market price. Reducing collateral may trigger IMMEDIATE TAKE PROFIT order execution.</code></p></li>
<li><p><strong>多空止损价格无效：</strong>如果开多<strong>原SL Price &lt; 新SL Price<sub>多Min</sub> ，</strong>或者开空<strong>原SL Price &gt; 新SL Price<sub>空Max</sub> ，则黄色警告框提示：</strong></p>
<p><code>Set SL Price is worse than new SL Price capped at -80% PnL%. Reducing collateral may result in INVALID STOP LOSS order.</code></p>
<p><strong>成交时更新前端positoin/order中展示的止损价格不合规状态-价格标红+tooltip</strong></p></li>
<li><p>计算逻辑：<br />
<strong>TP Price<sub>多Max/空Min</sub> = [1</strong> ± <strong>(25 * Collateral - Fees) / Size] * Entry Price</strong><br />
<strong>SL Price<sub>多Min/空Max</sub> = [1</strong> ± <strong>(-.8 * Collateral - Fees) / Size] * Entry Price</strong></p>
<p><strong>Liq Price</strong> <strong>= [1 ± (1/L<sub>max</sub> - 1/L - Fees / Size)] * Entry Price</strong></p></li>
</ol></li>
</ol></li>
</ol></li>
</ol>
<ul>
<li><p><strong>明细：仅</strong>展示Size, Collateral, Leverage, Liq Price，TP Price（移除保证金导致需变化TP Price时展示），Fees</p>
<ul>
<li><p>注意，移除保证金会导致该仓位的止盈止损价格<strong>边界变窄，</strong>所以如果移除保证金时，当前止盈价格在有效边界外，需重新计算并展示，止损价格在有效边界外，需警告。</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="e3268bba-d057-433a-81b1-680612dfe9fb"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c1e666411d7ddcca9b6aa243d77bcff0b388997588b8b5028c57447cef83b217" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-05%20at%2010.59.55.png?version=1&amp;modificationDate=1764903655247&amp;cacheVersion=1&amp;api=v2" data-height="628" data-width="501" data-unresolved-comment-count="0" data-linked-resource-id="49545227" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-05 at 10.59.55.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="49f4c7bb-c267-4596-9bfe-6c1931811c99" data-media-type="file" width="180" height="226" alt="Screenshot 2025-12-05 at 10.59.55.png" /></span></td>
</tr>
<tr data-local-id="4509c15b-851a-437f-aa86-00cf8d7c1a9c">
<td class="confluenceTd" data-local-id="67e26543-a775-47d6-9b1c-d6b5e9a5180a"><p>Edit Order Price</p></td>
<td class="confluenceTd" data-local-id="43743d50-2119-4031-8e02-6b1be74c2018"><ul>
<li><p>限价单limit price修改校验：大体不变，<strong>去掉0.9x;1.1x</strong> 直接跟mark price比较，以及受限于杠杆率。</p></li>
<li><p>触发价修改校验：<a href="https://www.figma.com/design/WDFgkuyX7PmBUKyjJEPdmB/Untitled?node-id=1590-7224&amp;t=cyzKsrL90QgqDGcc-4" class="external-link" rel="nofollow">同场景1</a>，即：</p>
<ul>
<li><p>有持仓止盈价格编辑：TP Price 在(市价，capped TP Price]左开右闭区间内；SL Price 在[capped SL Price, 市价）左闭右开区间内。</p></li>
<li><p>无持仓止盈价格编辑：仅跟mark price做比较。</p></li>
</ul></li>
<li><p>按钮状态以及红框内tooltip提示同下单区：</p>
<ul>
<li><p>按钮<code>TP Price Above Mark Price</code>disabled，tooltip提示：<code>Above Mark Price [预言机价格($)]</code></p></li>
<li><p>按钮<code>Below Min TP Price</code>Disabled，提示tooltip：<code>Min TP Price [Max TP Price($)]</code>点击回填</p></li>
<li><p>按钮 <code>SL Price Below Mark Price </code>Disabled，tooltip提示：<code>Below Mark Price [预言机价格($)]</code></p></li>
<li><p>按钮<code>Above Max SL Price</code>Disabled，提示tooltip<code>Max SL Price [Min SL Price($)]</code>点击回填</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-local-id="e081a274-481a-4c70-b92a-68aa9f72fc9f"></td>
</tr>
</tbody>
</table>

</div>

### 交易记录区

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="87512754-2886-4ae5-a62d-f0791437d94d">
<tbody>
<tr data-local-id="3512a18d-dbe8-4127-a806-a9acb1c142f1">
<th class="confluenceTh" data-local-id="df36985d-8d9d-447e-80d4-c3e03e405119"><p><strong>模块</strong></p></th>
<th class="confluenceTh" data-local-id="ace626d5-18e9-4775-9518-0971c5f25241"><p><strong>需求</strong></p></th>
<th class="confluenceTh" data-local-id="89b244e0-5605-484e-af38-f081331670d3"><p><strong>截图</strong></p></th>
</tr>
&#10;<tr data-local-id="1c088845-ba63-4993-9c57-270b7a99d57f">
<td class="confluenceTd" data-local-id="3cfb049c-528d-482f-ae2a-9f81d388fe24"><p>Pool History</p></td>
<td class="confluenceTd" data-local-id="02f7cb8e-f6c0-4b31-97f7-ea2ed0984c32"><ol>
<li><p>Recent Trades 每五秒刷新<br />
展示24h内该市场<strong>开平仓执行</strong>的交易历史数据，时间顺序倒叙，包括：</p>
<ol>
<li><p>Price：精度同前端配置表</p></li>
<li><p>多空方向：用价格的颜色表示</p></li>
<li><p>Size：2dp，超出1,000用kmb缩略表示 正负号代表开平仓方向</p></li>
<li><p>Time：前端格式化，不用hh:mm:ss格式，转为timestamp - now的时间差形式表示：</p>
<ol>
<li><p>[0s, 5s]: <code>just now</code></p></li>
<li><p>(5s, 60s]: <code>&lt; 1 min</code></p></li>
<li><p>(60s, 60min]: <code>x mins ago</code></p></li>
<li><p>(1h, 24h]：<code>x hours ago</code></p></li>
</ol></li>
<li><p>24h Market Sentiment：左面多用蓝色，右面空用红色，渲染区域以及取值为recent trade里面<strong>ΣSize Long : ΣSize Short, 取整即可</strong></p></li>
<li><p>hover展示Tooltip：hover那一行顶部对齐</p>
<ol>
<li><p>[Market Icon] + Symbol</p></li>
<li><p>Direction: Long/Short 颜色表示</p></li>
<li><p>Leverage：1dp杠杆倍数 - 仅开仓与全平的open/close有，加减仓不展示</p></li>
<li><p>Order Type: Open/Close/Increase/Decrease + Market/Limit/Stop Loss/Take Profit Order</p></li>
<li><p>Size ($)</p></li>
<li><p>Collateral ($)</p></li>
<li><p>Entry Price 仅开加仓</p></li>
<li><p>Exit Price 仅平减仓</p></li>
<li><p>PnL(%) 仅平减仓；展示已实现盈亏<strong>以及</strong>盈亏比；PnL = gross pnl不计费用；PnL% = gross pnl / initial collateral%</p></li>
<li><p>user wallet address：前四…后四</p></li>
<li><p>time：yyyy/mm/dd hh:mm hover变为可点击态，点击跳转到bscscan查看对应的哈希</p></li>
</ol></li>
</ol></li>
</ol></td>
<td class="confluenceTd" data-local-id="b3832a3c-4c36-49d9-813a-d3221a9e3e64"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b86cfdd938698dec64c46e2ff1541b5c23b56cb75994ab87eb449caa9fa89e92" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-03%20at%2018.29.21.png?version=1&amp;modificationDate=1764757796066&amp;cacheVersion=1&amp;api=v2" data-height="471" data-width="334" data-unresolved-comment-count="0" data-linked-resource-id="48431151" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-03 at 18.29.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="a4a86a61-825b-43e2-8613-7742c6c35664" data-media-type="file" width="334" height="471" alt="Screenshot 2025-12-03 at 18.29.21.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="16703d7e8b0fda47c7d7b031ed0b7551a64dddee6e45a3f24eae2c26b190dedc" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-09%20at%2014.43.31.png?version=1&amp;modificationDate=1765262638906&amp;cacheVersion=1&amp;api=v2" data-height="413" data-width="589" data-unresolved-comment-count="0" data-linked-resource-id="52101141" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 14.43.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="d29c7d22-2e17-47e4-9f8a-ef65d32617cb" data-media-type="file" width="181" height="126" alt="Screenshot 2025-12-09 at 14.43.31.png" /></span></td>
</tr>
<tr data-local-id="3e116f3d-8576-46ce-b689-ce4bde5048f4">
<td class="confluenceTd" data-local-id="5220cbfd-d3ae-4bc7-8ed1-6e390d9dff5b"><p>User History</p></td>
<td class="confluenceTd" data-local-id="83630aa1-42ac-488d-84e4-96c1e920e795"><h4 id="TradePage_PRD-1.Positions修改点" data-local-id="95917293-25a8-4492-ae48-10c3970c78bc">1. Positions 修改点</h4>
<ul>
<li><p>Net Value Tooltip上方文字变为：Net Value = Collateral + Net PnL After Fees<span data-colorid="x51vm8ild0"> </span>- Close Fee；Funding Fee Due下方，Close Fee上方新增 Price Impact</p></li>
<li><p>TP/SP Price这一列带符号：多TP，空SL价格前加 <strong>≥</strong> ；空TP，多SL符号前加 <strong>≤</strong></p></li>
<li><p>position整行可点击，点击后trade页变为<strong>所点击的市场</strong>的详情/k线/历史交易/交易面板</p></li>
<li><p>新增止盈止损价格不合规提示：</p>
<ul>
<li><p>止损价格超出Price Cap范围：价格标红，hover展示tooltip：<code>Invalid Stop Loss：Set SL Price is worse than the SL Price capped at -80% PnL%.</code></p></li>
<li><p>止盈价格超出Price Cap 范围：自动计算并更新</p></li>
</ul></li>
</ul>
<h4 id="TradePage_PRD-2.Orders修改点" data-local-id="d9e336d3-a341-409c-9654-6b25f093fac4">2. Orders修改点</h4>
<ul>
<li><p>表头：Collateral &amp; Time删 按以下表头顺序展示列</p></li>
<li><p>Symbol 颜色表示多空</p></li>
<li><p>Type 支持筛选，type = All（默认）/ Limit / Take Profit / Stop Loss</p></li>
<li><p>Size加符号 代表加减仓。limit 加号，tpsl减号。</p></li>
<li><p>Trigger Price ：带<strong>≤ ≥</strong>符号的trigger/limit价格 右侧edit 图标点击出编辑价格弹窗</p></li>
<li><p>Liq. Price After Exec.：订单执行后的仓位新强平价展示。</p></li>
<li><p>列表整行可点击，点击后变为对应市场。</p></li>
<li><p>新增止盈止损价格不合规提示同上</p></li>
</ul>
<h4 id="TradePage_PRD-3.History修改点" data-local-id="0200f098-1206-404f-96f2-542ab0f0dc1e">3. History修改点</h4>
<ul>
<li><p><span class="inline-comment-marker" data-ref="be79831f-34ff-4ba7-b243-bdcc470ac719">type 支持筛选 type = All（默认）/ Market / Limit / Take Profit / Stop Loss</span> / Liquidated</p></li>
<li><p>action 支持筛选 action = Open / Increase / Close / Decrease</p></li>
<li><p>注意type = limit 时action没有close decrease；type = tp或sl时 action没有open increase</p></li>
</ul>
<h4 id="TradePage_PRD-4.Claim新增功能" data-local-id="1e4e5169-42fc-4962-a344-3ad312be5658">4. Claim 新增功能</h4>
<blockquote>
<p>此处为新增功能，用于funding fee &amp; price impact的<strong>实时累计数据展示</strong>，<strong>历史数据展示</strong>，以及<strong>领取操作</strong>。</p>
</blockquote>
<ul>
<li><p>不支持筛选，排列顺序为<strong>置顶</strong>Claim Funding &amp; Claim Price Impact这两个可领取，剩余历史数据默认按时间顺序desc</p></li>
<li><p>Action：这里有两种格式</p>
<ul>
<li><p>Claim Funding Fee/ Price Impact 实时累计数据：用主题色杠杠 + 字段</p></li>
<li><p>Claimed Funding Fee / Price Impact 历史领取数据：灰色杠杠 + 字段 + 交易上链时间 UTC转成机器时间，站内统一的格式展示即可</p></li>
</ul></li>
<li><p>Symbol：这里同vault页那里，展示最多5个symbol，展示顺序按fee多的靠前。若多于5个，则用+n表示，有动画</p></li>
<li><p>Value：总计可领取/单次领取费用之和，悬浮态。鼠标hover展示 tooltip：</p>
<ul>
<li><p>Market：market symbol</p></li>
<li><p>Fee：费用美元价值，加号 2dp &lt;0.01</p></li>
<li><p>Total：求和</p></li>
</ul></li>
<li><p>按钮：点击上方Claim all按钮一键领取所有。或可选逐行点击claim，二者分别领取。针对历史数据点击view跳转explorer看哈希。Toast:</p>
<ul>
<li><p>签名时：Accrued Fees Claiming</p></li>
<li><p>交易成功：Accrued Fees Claimed<br />
Claimed funding fee and price impact: +$123,123.12</p></li>
<li><p>交易失败：Accrued Fees Failed<br />
Transaction failed. Please try again later.<br />
或是Request rejected by user.</p></li>
<li><p>交易超时未响应：Accrued Fees Submitted<br />
Transaction pending. Please check again later.</p></li>
</ul></li>
</ul>
<h4 id="TradePage_PRD-5.全局组件" data-local-id="77009d07-f0e8-4850-ba7a-66824da3c7ff">5. 全局组件</h4>
<ul>
<li><p>Chart Position 新增止盈止损展示，样式同限价单样式，Limit字段变成TP或SL即可。</p></li>
<li><p>Show Chart Position以及Hide Others对Claim不生效</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="791b9bfe-86e4-4fec-81fe-151772653442"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="47bb08ca0a4f95a617beba0ff4cfe67a8173b0617eb8797b660c07216f9b5a5e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-03%20at%2019.24.44.png?version=1&amp;modificationDate=1764761232919&amp;cacheVersion=1&amp;api=v2" data-height="447" data-width="1399" data-unresolved-comment-count="0" data-linked-resource-id="48398434" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-03 at 19.24.44.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="3452f60a-a172-42fa-a6fd-92776bf73c69" data-media-type="file" width="181" height="57" alt="Screenshot 2025-12-03 at 19.24.44.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d6973c208555fe70923b5d4e8688c05868adc8ff599f5ba0da53a7dce3b2ad06" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2016.35.45.png?version=1&amp;modificationDate=1764837395635&amp;cacheVersion=1&amp;api=v2" data-height="276" data-width="1036" data-unresolved-comment-count="0" data-linked-resource-id="49020949" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 16.35.45.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="2416651a-ae3e-438a-90aa-ec8576805d0f" data-media-type="file" width="425" height="113" alt="Screenshot 2025-12-04 at 16.35.45.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="06c7f44d1f95d35acbac3f015b571ddc7e3bae02ffc48961c0143a01fe62978b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2018.36.22.png?version=2&amp;modificationDate=1764844843748&amp;cacheVersion=1&amp;api=v2" data-height="333" data-width="1192" data-unresolved-comment-count="0" data-linked-resource-id="49184792" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 18.36.22.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="db9bcef0-b34b-4f3a-835d-a47cd1f82da5" data-media-type="file" width="181" height="50" alt="Screenshot 2025-12-04 at 18.36.22.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="622175584d4639a4b58ed98311e2a6a179ca06e4ba9d982708fb01635b618f36" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2018.57.02.png?version=1&amp;modificationDate=1764845857355&amp;cacheVersion=1&amp;api=v2" data-height="357" data-width="437" data-unresolved-comment-count="0" data-linked-resource-id="49250365" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 18.57.02.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="23bad2b7-ecfc-4373-9083-980bab5fddd0" data-media-type="file" width="181" height="147" alt="Screenshot 2025-12-04 at 18.57.02.png" /></span>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9aa57f5de3a0a0ea3ee6b58d2607a7bd9179a48bfc43bbf5b6b1102eb444a866" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.12.47.png?version=1&amp;modificationDate=1764847010997&amp;cacheVersion=1&amp;api=v2" data-height="189" data-width="1252" data-unresolved-comment-count="0" data-linked-resource-id="49020990" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.12.47.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="56f8230a-a611-4d8e-a65a-0a15fee87688" data-media-type="file" width="181" height="27" alt="Screenshot 2025-12-04 at 19.12.47.png" /></span></td>
</tr>
<tr data-local-id="4cce0f20-a71f-4e40-b21a-d47076109fa2">
<td class="confluenceTd" data-local-id="420b37d2-78f8-4b15-b106-f450dc7576cd"><p>User Portfolio</p></td>
<td class="confluenceTd" data-local-id="4d014b6d-ca82-4a4d-83b0-0621342889a3"><ol>
<li><p>整体修改：</p>
<ol>
<li><p>Balance变成USDC为单位</p></li>
<li><p>钱包余额这里删，我们只支持USDC下单</p></li>
<li><p>颜色规则：仅有多绿空红</p></li>
</ol></li>
<li><p>Portfolio_Perp Orders：</p>
<ol>
<li><p>文案修改为 Orders</p></li>
<li><p>Size 带加减符号，限价单加号止盈止损减号</p></li>
<li><p>Collateral删</p></li>
</ol></li>
<li><p>Portfolio_Perp Positions：</p>
<ol>
<li><p>同样修改为Positions</p></li>
<li><p>Price改成uPnL 展示未实现盈亏以及盈亏率，带颜色正负号</p></li>
</ol></li>
<li><p>Activity：</p>
<ol>
<li><p>action 变成 Order Type + action + Side。比如，Market Open Long，Take Profit Close Short。H5放不下可以省略side的部分。</p></li>
<li><p>Size符号注意别反了</p></li>
</ol></li>
</ol></td>
<td class="confluenceTd" data-local-id="173ed888-2b05-4395-99be-3e169d00cec0"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9a00a5db4ed05d66870ca97d9caf19bfe222ce69cbc0faa0efc077a72d95aa72" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.22.52.png?version=1&amp;modificationDate=1764847615310&amp;cacheVersion=1&amp;api=v2" data-height="593" data-width="400" data-unresolved-comment-count="0" data-linked-resource-id="49021000" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.22.52.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="291310a4-cabb-4175-b3a6-f61b1b9c8a2c" data-media-type="file" width="400" height="591" alt="Screenshot 2025-12-04 at 19.22.52.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2f07d0a37de3132d781028c0dcbe59f95451c6a3743e7cec6ca1d18c2bf5e4db" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.31.06.png?version=1&amp;modificationDate=1764847957915&amp;cacheVersion=1&amp;api=v2" data-height="503" data-width="665" data-unresolved-comment-count="0" data-linked-resource-id="49250379" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.31.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="842355b4-2158-417b-bf63-248b6845bd53" data-media-type="file" width="401" height="302" alt="Screenshot 2025-12-04 at 19.31.06.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b8882bff07236396c7b547de6822c74a188b830eb724a3e8b50ce5dc987e6416" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.36.56.png?version=1&amp;modificationDate=1764848419001&amp;cacheVersion=1&amp;api=v2" data-height="383" data-width="389" data-unresolved-comment-count="0" data-linked-resource-id="49021010" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.36.56.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="124da7c1-8a36-407a-8e03-e82439bfa7fd" data-media-type="file" width="389" height="382" alt="Screenshot 2025-12-04 at 19.36.56.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2e6629f8023e3ba3c96212eda6d9fd2ab55b710a3674c371563b580e120e194c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.42.32.png?version=1&amp;modificationDate=1764848597737&amp;cacheVersion=1&amp;api=v2" data-height="376" data-width="760" data-unresolved-comment-count="0" data-linked-resource-id="49021017" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.42.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="b3005284-2cd8-444f-8fd6-e1e4d21c7c18" data-media-type="file" width="425" height="210" alt="Screenshot 2025-12-04 at 19.42.32.png" /></span></td>
</tr>
</tbody>
</table>

</div>

## 三、数据依赖与接口需求 (12.17联调，17号前给到）

> 后端缓存 3–5s; 前端刷新 10s

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="2e90a338-2585-4fab-8232-fc52bd0956c4">
<tbody>
<tr data-local-id="eac6ccc9-6307-4f53-a17f-84e43e24c129">
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="16819d01-62e9-4f48-aa7b-3abfe09ed1f4"><p> </p></th>
<th class="confluenceTh" data-highlight-colour="#f0f1f2" data-local-id="999d3ec1-e343-4644-8a62-155be012bdad"><p> 说明 （<span style="background-color: rgb(220,223,228);">前端取合约</span> <span style="background-color: rgb(211,241,167);">后端）</span></p></th>
</tr>
&#10;<tr data-local-id="8eb1e3db-aeff-423e-beec-f98bacb8d13d">
<td class="confluenceTd" data-local-id="342f24d8-68ff-4e08-bbac-2709620526cc"><p>市场详情相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="825a147f3a2466d3c684d421e8a8d30aed7667b64bbb27d585909b9e6f6ef88a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2012.25.57.png?version=2&amp;modificationDate=1763705608950&amp;cacheVersion=1&amp;api=v2" data-height="984" data-width="1663" data-unresolved-comment-count="0" data-linked-resource-id="41648179" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 12.25.57.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="834428f3-7a01-43ec-a41c-c4f96f3cde91" data-media-type="file" width="363" height="214" alt="Screenshot 2025-11-21 at 12.25.57.png" /></span></td>
<td class="confluenceTd" data-local-id="54135c82-960a-4b78-965d-0943fb3a008d"><ol>
<li><p><span style="background-color: rgb(220,223,228);">Carousel：</span>symbol；price；24h chg；按 rankKey = liquidity * 0.6 + OI * 0.4 desc 轮播前20个</p>
<ol>
<li><p>这里后期launch页面开发时有可能变成推荐位，到时候需要后端提供</p></li>
</ol></li>
<li><p><span style="background-color: rgb(211,241,167);">Market List:</span></p>
<ol>
<li><p>支持：sort（Price；24h Chg；24h Vol；OI多&amp;空；Avlb Liq多&amp;空），filter，search（地址&amp;ticker 同pools) ; long &amp; short token address;</p></li>
<li><p>数据：symbol；ticker；max leverage；oracle；24h Vol；OI多&amp;空；Avlb Liq多&amp;空</p>
<p>；市场闭市时间（<a href="https://docs.avantisfi.com/trading/market-hours" class="external-link" rel="nofollow">严格按avantis这里来包括假期</a>）；是否active（用于处理第三方自建池下架）</p></li>
</ol></li>
<li><p><span style="background-color: rgb(211,241,167);">Market Overview</span></p>
<ol>
<li><p>支持：1h/8h/24h/1y net rate（funding + borrow 带符号的）</p></li>
<li><p>数据：24h high成交价，24h low成交价；24h open 24h close, 24h Vol；</p></li>
</ol></li>
<li><p><span style="background-color: rgb(220,223,228);">Chart</span></p></li>
</ol></td>
</tr>
<tr data-local-id="8be7628d-d2b8-464e-8b61-39548a230702">
<td class="confluenceTd" data-local-id="d638ff82-b412-49c0-bdd9-3c9172aaf317"><p>用户操作相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ff721e98bc3416388b23003df02fa5f2a19f280ac9f1cf76001f2308b9e146df" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2017.03.28.png?version=1&amp;modificationDate=1763715833462&amp;cacheVersion=1&amp;api=v2" data-height="858" data-width="1616" data-unresolved-comment-count="0" data-linked-resource-id="41713812" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 17.03.28.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="a2ef555e-4f28-43ea-8b17-93bad68399a7" data-media-type="file" width="363" height="192" alt="Screenshot 2025-11-21 at 17.03.28.png" /></span></td>
<td class="confluenceTd" data-local-id="7c28cc72-e43c-40ea-a36e-ff353b47311b"><ol>
<li><p><span style="background-color: rgb(220,223,228);">Trade Panel</span></p></li>
<li><p><span style="background-color: rgb(220,223,228);">Close Position </span></p></li>
<li><p><span style="background-color: rgb(220,223,228);">Edit Collateral </span></p></li>
<li><p><span style="background-color: rgb(220,223,228);">Edit Order Price </span></p></li>
</ol>
<p>合约可能新增止盈止损价格边界的上限配置 - 不同资产类型会用到不同的max profit以及min loss，而不是全部都2500%或-80%</p></td>
</tr>
<tr data-local-id="5b38014f-0f43-4186-a35b-21373a0315b4">
<td class="confluenceTd" data-local-id="41d06faf-b065-4b01-be3a-50c102b733d3"><p>交易记录相关</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6115416c716a7314f43d34b7840c72d4c188615cef9b928bac7c9e4c2c78b7c7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-11-21%20at%2016.56.19.png?version=1&amp;modificationDate=1763715531292&amp;cacheVersion=1&amp;api=v2" data-height="997" data-width="1665" data-unresolved-comment-count="0" data-linked-resource-id="41582684" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-11-21 at 16.56.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="e3065c53-0521-4aee-9a1a-474e60caf345" data-media-type="file" width="363" height="217" alt="Screenshot 2025-11-21 at 16.56.19.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="16703d7e8b0fda47c7d7b031ed0b7551a64dddee6e45a3f24eae2c26b190dedc" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-09%20at%2014.43.31.png?version=1&amp;modificationDate=1765262638906&amp;cacheVersion=1&amp;api=v2" data-height="413" data-width="589" data-unresolved-comment-count="0" data-linked-resource-id="52101141" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 14.43.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="d29c7d22-2e17-47e4-9f8a-ef65d32617cb" data-media-type="file" width="363" height="254" alt="Screenshot 2025-12-09 at 14.43.31.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="47bb08ca0a4f95a617beba0ff4cfe67a8173b0617eb8797b660c07216f9b5a5e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-03%20at%2019.24.44.png?version=1&amp;modificationDate=1764761232919&amp;cacheVersion=1&amp;api=v2" data-height="447" data-width="1399" data-unresolved-comment-count="0" data-linked-resource-id="48398434" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-03 at 19.24.44.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="3452f60a-a172-42fa-a6fd-92776bf73c69" data-media-type="file" width="363" height="116" alt="Screenshot 2025-12-03 at 19.24.44.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="d6973c208555fe70923b5d4e8688c05868adc8ff599f5ba0da53a7dce3b2ad06" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2016.35.45.png?version=1&amp;modificationDate=1764837395635&amp;cacheVersion=1&amp;api=v2" data-height="276" data-width="1036" data-unresolved-comment-count="0" data-linked-resource-id="49020949" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 16.35.45.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="2416651a-ae3e-438a-90aa-ec8576805d0f" data-media-type="file" width="425" height="113" alt="Screenshot 2025-12-04 at 16.35.45.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="06c7f44d1f95d35acbac3f015b571ddc7e3bae02ffc48961c0143a01fe62978b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2018.36.22.png?version=2&amp;modificationDate=1764844843748&amp;cacheVersion=1&amp;api=v2" data-height="333" data-width="1192" data-unresolved-comment-count="0" data-linked-resource-id="49184792" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 18.36.22.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="db9bcef0-b34b-4f3a-835d-a47cd1f82da5" data-media-type="file" width="363" height="101" alt="Screenshot 2025-12-04 at 18.36.22.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="622175584d4639a4b58ed98311e2a6a179ca06e4ba9d982708fb01635b618f36" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2018.57.02.png?version=1&amp;modificationDate=1764845857355&amp;cacheVersion=1&amp;api=v2" data-height="357" data-width="437" data-unresolved-comment-count="0" data-linked-resource-id="49250365" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 18.57.02.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="23bad2b7-ecfc-4373-9083-980bab5fddd0" data-media-type="file" width="363" height="296" alt="Screenshot 2025-12-04 at 18.57.02.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2f07d0a37de3132d781028c0dcbe59f95451c6a3743e7cec6ca1d18c2bf5e4db" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.31.06.png?version=1&amp;modificationDate=1764847957915&amp;cacheVersion=1&amp;api=v2" data-height="503" data-width="665" data-unresolved-comment-count="0" data-linked-resource-id="49250379" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.31.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="842355b4-2158-417b-bf63-248b6845bd53" data-media-type="file" width="401" height="302" alt="Screenshot 2025-12-04 at 19.31.06.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b8882bff07236396c7b547de6822c74a188b830eb724a3e8b50ce5dc987e6416" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.36.56.png?version=1&amp;modificationDate=1764848419001&amp;cacheVersion=1&amp;api=v2" data-height="383" data-width="389" data-unresolved-comment-count="0" data-linked-resource-id="49021010" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.36.56.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="124da7c1-8a36-407a-8e03-e82439bfa7fd" data-media-type="file" width="389" height="382" alt="Screenshot 2025-12-04 at 19.36.56.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2e6629f8023e3ba3c96212eda6d9fd2ab55b710a3674c371563b580e120e194c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/41713689/Screenshot%202025-12-04%20at%2019.42.32.png?version=1&amp;modificationDate=1764848597737&amp;cacheVersion=1&amp;api=v2" data-height="376" data-width="760" data-unresolved-comment-count="0" data-linked-resource-id="49021017" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-04 at 19.42.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="41713689" data-linked-resource-container-version="33" data-media-id="b3005284-2cd8-444f-8fd6-e1e4d21c7c18" data-media-type="file" width="425" height="210" alt="Screenshot 2025-12-04 at 19.42.32.png" /></span></td>
<td class="confluenceTd" data-local-id="0919f0a5-7f7f-475f-a49b-524e72aecdb8"><ul>
<li><p><span style="background-color: rgb(211,241,167);">Pool History（k线右侧的recent trades） </span><a href="https://hertzflow.atlassian.net/wiki/people/712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3" target="_blank" data-linked-resource-id="360623" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">novax 0x</a></p>
<ul>
<li><p>范围：<strong>仅返回最近 24 小时内的全量数据</strong></p></li>
<li><p>数据：entry price；exit price(<strong>仅decr</strong>）；side；type；size；coll; lev; pnl<strong>(仅decr)</strong>; pnl%(<strong>仅decr)</strong>; timestamp; wallet address; hash；求和<strong>Σ</strong>size 多&amp;空（用于market sentiment）</p></li>
<li><p>规则1：timestamp处理成时间差</p>
<ul>
<li><p>[0s, 5s]: <code>just now</code></p></li>
<li><p>(5s, 60s]: <code>&lt; 1 min</code></p></li>
<li><p>(60s, 60min]: <code>x mins ago</code></p></li>
<li><p>(1h, 24h]：<code>x hours ago</code></p></li>
</ul></li>
<li><p>规则2: Order Type （type + direction）= Open / Close / Increase / Decrease <strong>+</strong> Market / Limit / Stop Loss / Take Profit Order / Liquidated</p></li>
</ul></li>
<li><p><span style="background-color: rgb(211,241,167);">User History - Position/Order/History/Claim </span><a href="https://hertzflow.atlassian.net/wiki/people/712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3" target="_blank" data-linked-resource-id="360623" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">novax 0x</a></p></li>
</ul>
<p>&lt;⚠️ fees计算需加入<strong>funding</strong>以及<strong>price impact</strong>；其中<span style="background-color: rgb(211,241,167);">price impact无法直接查合约</span>拿到，同时新增列表 Claim，用于price impact &amp; funding多收取部分以及返佣部分需手动领取&gt;</p>
<ul>
<li><p>Position: 新增funding fee due；price impact</p></li>
<li><p>orders：支持<strong>sort</strong>（默认时间desc）；<strong>filter</strong>（type = All (默认) / Limit / TP / SL）</p></li>
<li><p>History：支持<strong>filter 1（</strong>type = All（默认）/ Market / Limit / Take Profit / Stop Loss / Liquidated）；<strong>filter2</strong> （action = Open / Increase / Close / Decrease）；</p>
<ul>
<li><p>注意：type = limit 时action没有close decrease；type = tp或sl时 action没有open increase</p></li>
</ul></li>
<li><p><span style="background-color: rgb(211,241,167);">Claim </span><a href="https://hertzflow.atlassian.net/wiki/people/712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3" target="_blank" data-linked-resource-id="360623" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">novax 0x</a> （price impact &amp; funding多收取部分以及返佣部分需手动领取）</p>
<ul>
<li><p>数据：</p>
<ul>
<li><p>实时数据：可领取Fundng<strong>；可领取Price Impact （Value by Symbol；Symbol）</strong></p></li>
<li><p><span class="inline-comment-marker" data-ref="c40df8fd-db40-4edf-abde-dee8109604fe">⚠️注意：price impact可领取部分是</span><strong><span class="inline-comment-marker" data-ref="c40df8fd-db40-4edf-abde-dee8109604fe">当下可领取的，不是像gmx合约里5天后才可领的。</span></strong></p></li>
<li><p>后端历史数据：Value by Symbol；Symbol；Hash；type （funding / price impact）</p></li>
</ul></li>
</ul></li>
<li><p><span style="background-color: rgb(211,241,167);">User Portfolio </span><a href="https://hertzflow.atlassian.net/wiki/people/712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3" target="_blank" data-linked-resource-id="360623" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">novax 0x</a></p>
<ul>
<li><p>Portfolio_Orders：Size 带加减符号，限价单加号止盈止损减号；Collateral删</p></li>
<li><p>Portfolio_Perp Positions：Price改成uPnL（PnL%） 展示未实现盈亏以及盈亏率，带颜色正负号</p></li>
<li><p>Activity：direction 变成 Order Type + action + Side。比如，Market Open Long，Take Profit Close Short。<strong>Size符号注意别反了</strong></p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

</div>
