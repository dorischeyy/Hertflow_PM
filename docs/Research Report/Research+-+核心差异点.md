# Research - 核心差异点

<div class="Section1">

<style>[data-colorid=oixlsfirv9]{color:#36b37e} html[data-color-mode=dark] [data-colorid=oixlsfirv9]{color:#4cc994}[data-colorid=r4y4p9i8t2]{color:#ffc400} html[data-color-mode=dark] [data-colorid=r4y4p9i8t2]{color:#ffc400}[data-colorid=pylqtppxgp]{color:#ffc400} html[data-color-mode=dark] [data-colorid=pylqtppxgp]{color:#ffc400}[data-colorid=x2smgi4xa2]{color:#ffc400} html[data-color-mode=dark] [data-colorid=x2smgi4xa2]{color:#ffc400}[data-colorid=a1iqz7wt1l]{color:#ffc400} html[data-color-mode=dark] [data-colorid=a1iqz7wt1l]{color:#ffc400}[data-colorid=qunkxw2ga0]{color:#36b37e} html[data-color-mode=dark] [data-colorid=qunkxw2ga0]{color:#4cc994}[data-colorid=w7m26zcajg]{color:#ffc400} html[data-color-mode=dark] [data-colorid=w7m26zcajg]{color:#ffc400}[data-colorid=m6uxpus9bq]{color:#36b37e} html[data-color-mode=dark] [data-colorid=m6uxpus9bq]{color:#4cc994}[data-colorid=rrix27rlwl]{color:#ffc400} html[data-color-mode=dark] [data-colorid=rrix27rlwl]{color:#ffc400}[data-colorid=lv5dlm77tv]{color:#36b37e} html[data-color-mode=dark] [data-colorid=lv5dlm77tv]{color:#4cc994}[data-colorid=c3p6fo787i]{color:#ff5630} html[data-color-mode=dark] [data-colorid=c3p6fo787i]{color:#cf2600}[data-colorid=dk5ha2nlb7]{color:#36b37e} html[data-color-mode=dark] [data-colorid=dk5ha2nlb7]{color:#4cc994}[data-colorid=jebbsp7ffx]{color:#ff5630} html[data-color-mode=dark] [data-colorid=jebbsp7ffx]{color:#cf2600}[data-colorid=jkb7i8d936]{color:#ffc400} html[data-color-mode=dark] [data-colorid=jkb7i8d936]{color:#ffc400}[data-colorid=rveaebayhi]{color:#ffc400} html[data-color-mode=dark] [data-colorid=rveaebayhi]{color:#ffc400}[data-colorid=j43vr25mcf]{color:#ffc400} html[data-color-mode=dark] [data-colorid=j43vr25mcf]{color:#ffc400}[data-colorid=tfuyvkeptf]{color:#36b37e} html[data-color-mode=dark] [data-colorid=tfuyvkeptf]{color:#4cc994}[data-colorid=jc5ry64bk7]{color:#ffc400} html[data-color-mode=dark] [data-colorid=jc5ry64bk7]{color:#ffc400}</style>产品决策点及**需要的合约修改点的完整列表**。

# 1. 核心差异

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="bf722aa9-9ecd-4a9b-85e3-21ef62a545a9">
<tbody>
<tr data-local-id="8e5f9d5b-8ba6-4b08-9d14-3c0a8ec34dc6">
<th class="confluenceTh" data-local-id="6a2d36c2-4f1c-48f9-a406-bff23078c56e"><p>模块</p></th>
<th class="confluenceTh" data-local-id="a10416f8-da71-4da7-b1ca-67d23545fce5"><p>GMX V2</p></th>
<th class="confluenceTh" data-local-id="7ede5e02-9a2b-4c63-9131-2307eaf47b7d"><p>Avantis</p></th>
</tr>
&#10;<tr data-local-id="d5e3881f-5173-4692-97a1-707b96b07d0f">
<td class="confluenceTd" data-local-id="4d20bf0d-0bf6-4c97-8095-289345e4d34b"><p>流动性结构</p></td>
<td class="confluenceTd" data-local-id="93a71895-761b-424b-bdef-c3ed2a30aaa5"><p><strong>多资产、多市场隔离池 GM</strong> + <strong>GLV vault聚合</strong></p>
<ul>
<li><p>LP可选择承担单市场风险：交易者盈利 → LP 损失；交易者亏损 → LP 收益；也可选择不承担：vault</p></li>
<li><p>执行价格：oracle + price impact</p></li>
</ul>
<blockquote>
<p><span class="inline-comment-marker" data-ref="f41f2a70-53a4-4c85-b610-eb30fbec089e">apy比avantis高一倍</span></p>
</blockquote></td>
<td class="confluenceTd" data-local-id="954d69ce-3cb6-4b1f-9ec0-847bab0dd95a"><p><strong>单池 USDC Vault（avUSDC）</strong></p>
<blockquote>
<p><span class="inline-comment-marker" data-ref="6cae4c1b-7382-4954-a391-b94408e12889">底层架构猜测是不同种类资产分别共用一个资金池。</span></p>
</blockquote>
<ul>
<li><p><span class="inline-comment-marker" data-ref="6cae4c1b-7382-4954-a391-b94408e12889">执行价格由 vAMM + oracle 结算。其中vAMM模拟</span></p></li>
<li><p>单独 insurance buffer vault 负责吸收 trader PnL &amp; 波动 → 不计入 LP 的价格波动。</p></li>
</ul>
<blockquote>
<p><span class="inline-comment-marker" data-ref="f41f2a70-53a4-4c85-b610-eb30fbec089e">LP </span><strong><span class="inline-comment-marker" data-ref="f41f2a70-53a4-4c85-b610-eb30fbec089e">不直接</span></strong><span class="inline-comment-marker" data-ref="f41f2a70-53a4-4c85-b610-eb30fbec089e">承担单市风险，LP 收入只来自 fee &amp; vault strategies。把交易风险和 LP 收益彻底拆分，LP 不承担 trader pnl 方向性风险</span></p>
</blockquote></td>
</tr>
<tr data-local-id="d5e3881f-5173-4692-97a1-707b96b07d0f">
<td class="confluenceTd" data-local-id="4d20bf0d-0bf6-4c97-8095-289345e4d34b"><p>仓位模式</p></td>
<td class="confluenceTd" data-local-id="93a71895-761b-424b-bdef-c3ed2a30aaa5"><ul>
<li><p>同市场同方向<strong>自动合并</strong>仓位</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="954d69ce-3cb6-4b1f-9ec0-847bab0dd95a"><ul>
<li><p>同市场同方向仓位仍<strong>保持独立</strong></p></li>
<li><p>限制同市场最多20单（不分方向不分订单类型）</p></li>
</ul></td>
</tr>
<tr data-local-id="75582ad9-95ab-4922-8b33-48677d5c478e">
<td class="confluenceTd" data-local-id="16577439-8133-486f-bffc-34bb5e4eac81"><p>PnL 结算来源</p></td>
<td class="confluenceTd" data-local-id="493bfeff-f200-4216-9e46-9675b3f65e81"><p>直接从池子 <strong>token balance</strong> 扣</p>
<ul>
<li><p>uPnL/TVL &gt; factor 则不让移除流动性</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="19352684-2fe0-4606-9047-74fc32f2ea1a"><p>从 <strong>liquidity buffer</strong> 扣</p>
<ul>
<li><p>(uPnL-VaultBuffer)​/TVL &gt; 5%则动用 AVNT 保险金模块</p></li>
</ul></td>
</tr>
<tr data-local-id="67a9e116-ace8-4781-90c2-5ccc482385d0">
<td class="confluenceTd" data-local-id="e304ee94-9bc6-43b1-9821-d923f2dcf78f"><p><span class="inline-comment-marker" data-ref="f59e66a5-3f24-4d49-9aa0-b56caf5e6b2a">风险模型</span></p></td>
<td class="confluenceTd" data-local-id="b6efeb75-e96e-4015-9675-4c39a05ce64f"><p><strong>GMX - 风险共担（APY 15% - 20%）</strong></p>
<p>交易者盈亏直接作用到 LP，依靠参数防守以及波动性补偿（funding / pnl factor）维持平衡<span class="inline-comment-marker" data-ref="f59e66a5-3f24-4d49-9aa0-b56caf5e6b2a">，</span><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/51118271/Research+-#5.-%E9%A3%8E%E9%99%A9%E5%8F%82%E6%95%B0%E6%A8%A1%E5%9E%8B" rel="nofollow"><span class="inline-comment-marker" data-ref="f59e66a5-3f24-4d49-9aa0-b56caf5e6b2a">详细参数解读见下</span></a></p></td>
<td class="confluenceTd" data-local-id="69f143db-7b83-4d22-9e62-ac7a36b5e0e7"><p><strong>Avantis - 保险池隔离（APY 9.6%，12.7%）</strong></p>
<p>交易者盈亏先进入 buffer，让 LP 只赚不亏，通过 spread 调节流动性，Zero-fee 交易，Skew Spread 调整交易侧成本<strong>，</strong><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/51118271/Research+-#5.-%E9%A3%8E%E9%99%A9%E5%8F%82%E6%95%B0%E6%A8%A1%E5%9E%8B" rel="nofollow"><span class="inline-comment-marker" data-ref="f59e66a5-3f24-4d49-9aa0-b56caf5e6b2a">详细参数解读见下</span></a></p></td>
</tr>
<tr data-local-id="dc8d439b-787c-47e4-a3d6-cf7587d0a4b5">
<td class="confluenceTd" data-local-id="57f9c2a7-4a7f-4f09-be0c-d45d6302f419"><p>高杠杆</p></td>
<td class="confluenceTd" data-local-id="38237e2d-aa30-43eb-9b32-da34ce812bb9"><p>≦ 100x</p></td>
<td class="confluenceTd" data-local-id="9cf8aa76-8137-4673-bf07-88ef3b8dde91"><p>≦ 500–1000x（根据市场）</p></td>
</tr>
<tr data-local-id="62dd43ef-8813-45eb-ab4b-af8c4cbf755d">
<td class="confluenceTd" data-local-id="f6a09413-6de3-4547-ba07-1384308417cf"><p>收费结构</p></td>
<td class="confluenceTd" data-local-id="f4b2c45f-ca06-4e96-a3bb-fc6e3637c260"><p>价格冲击 （针对大额交易，保证流动池可持续）+ 开仓费 + 平仓费 + borrow fee + funding fee + swap fee</p></td>
<td class="confluenceTd" data-local-id="d794d8ab-6d21-4271-a847-a36d3a1a1e30"><p>Zero-Fee Perps：无开平、无借费、无 funding，只有盈利抽成</p>
<p><span class="inline-comment-marker" data-ref="9e87895d-0877-46b7-a1b4-c35fd5d71b71">正常杠杆：点差（来源于做市商报价机制，模拟真实市场点差，作用相当于funding，只不过收入归协议）；借贷费+开仓费</span></p>
<p><a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765" class="external-link" rel="nofollow">详细配置参数见表格</a></p></td>
</tr>
</tbody>
</table>

</div>

# 2. 执行价格差异

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="3ddc4847-afd7-4f8d-bfe7-b54f77a466f7">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="baab8779-c1af-41f2-b1c1-739e96ff6ac5">
<th class="confluenceTh" data-local-id="31c098a8-7cc0-4e34-a28d-897e7644f2d3"><p>项目</p></th>
<th class="confluenceTh" data-local-id="741708af-a6e9-4049-b866-707852629ddd"><p>GMX</p></th>
<th class="confluenceTh" data-local-id="647fb990-a0b3-4344-b00d-bc76762cd7b0"><p>Avantis</p></th>
</tr>
&#10;<tr data-local-id="1c414b74-5d1f-4c20-83c6-f1e766b39d43">
<td class="confluenceTd" data-local-id="5c75f8a5-1737-4fd0-bbb5-85f4993eaa12"><p>Price 来源</p></td>
<td class="confluenceTd" data-local-id="a7df7db0-fe93-41c5-896b-e2c439deafa7"><p>Oracle price</p></td>
<td class="confluenceTd" data-local-id="f3a75ffc-6ae1-4e33-8c6f-04e8877d30bf"><p>Oracle price</p></td>
</tr>
<tr data-local-id="7ee2ec95-15e6-4d85-8133-80be56d9111a">
<td class="confluenceTd" data-local-id="0cd61e36-b229-41ae-a715-1a3e8bdab243"><p>Execution Price</p></td>
<td class="confluenceTd" data-local-id="127b657e-39d7-495b-bcff-f7c409370814"><p>oracle ± priceImpact</p></td>
<td class="confluenceTd" data-local-id="9f800912-d433-4cc8-a579-761afaae0548"><p>vAMM + Skew-based Incentive + External Hedge</p></td>
</tr>
<tr data-local-id="f69cfaca-b38d-4570-aa84-d5da59bc5da3">
<td class="confluenceTd" data-local-id="8843df34-a0cb-4de1-9a74-e04ec6be7e65"><p>Price Impact 内核</p></td>
<td class="confluenceTd" data-local-id="3782ce45-deae-41d3-9097-28d4cc8ecba9"><p>exp=2 的 δ² curve（池子不平衡驱动）</p></td>
<td class="confluenceTd" data-local-id="373a2083-aad9-41b9-97a9-2d1c65ec037e"><p><span class="inline-comment-marker" data-ref="d33b6d58-725d-4e7b-952d-2d376d72fcf9">vAMM invariant（虚拟 liquidity），skew 越大 slippage 越大，反向下单负滑点奖励（更新版本后取消正滑点）</span></p></td>
</tr>
<tr data-local-id="9c562678-232a-47d6-9ce3-ce1626544358">
<td class="confluenceTd" data-local-id="38304ba3-0797-4ace-8710-e6004baa640d"><p>rebate</p></td>
<td class="confluenceTd" data-local-id="f5be9064-60bc-4040-87f8-592497c90f2b"><p>负值时，超过50bps部分先收取再返给用户避免逃费。正值需用户手动领取，防止临近强平高危仓位苟延残喘。</p></td>
<td class="confluenceTd" data-local-id="8d0426c6-4d71-41b4-8b06-c24cd3539ca5"><p>帮助重平衡OI → 正滑点奖励</p>
<p>OI不平衡 → 爆仓补偿；盈利抽成</p></td>
</tr>
</tbody>
</table>

</div>

# 3. 清算 / Buffer / Insurance 差异

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 项目 | GMX | Avantis |
| PnL settlement | <span class="inline-comment-marker" ref="55151785-57cb-41e0-a2ed-5ebe769eb9f2">直接反应在池子里的资产价值</span> | buffer里面吸收 |
| 极端亏损 | LP 资产不足会坏账 | liquidity buffer \< 95% → 动用 SM（AVNT vault）赔付，最多 20% |
| Keeper incentive | 清算费 0.2%-0.45% | liquidation reward（15%）从亏损中给 keeper |
| withdraw gate | maxPnlFactorForWithdrawals | Vault Buffer Ratio% + exit fee（动态） |

</div>

# 4. TPSL / 止盈止损差异

> 1500%TP以及Guaranteed SL 是 GMX 机制完全不支持的，需要修改清算逻辑。

<div class="table-wrap">

|  |  |
|----|----|
| GMX | Avantis |
| TP/SL 都是 limit 行为，oracle触发（无保证） | **Guaranteed SL（亏损方向 SL 一定执行）** |
| 价格限制 | TP\<=2500%，SL\>=-80% |
| 合成市场ADL | 无 |

</div>

# 5. 风险参数模型

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="ab97a03f-9a79-46aa-a646-7bdf19b18ea9">
<tbody>
<tr data-local-id="0b348976-5d81-45d0-a078-44e6b8f68ea3">
<th class="confluenceTh" data-local-id="d8b591a9-b80e-444d-9a79-5bbccf6a2cd6"><p>机制</p></th>
<th class="confluenceTh" data-local-id="2896f7bb-2380-4fae-b753-705235d39728"><p>GMX V2</p></th>
<th class="confluenceTh" data-local-id="823a4814-9688-44fc-8baf-116209cce162"><p>Avantis</p></th>
</tr>
&#10;<tr data-local-id="07dbd154-e43d-42dd-a1f9-ac5004383301">
<td class="confluenceTd" data-local-id="86ef040a-7ee3-4a3b-a3f2-6fb9c14c6296"><p><strong>Funding</strong></p></td>
<td class="confluenceTd" data-local-id="f193e292-4afd-47cd-874e-de9b1e703823"><ul>
<li><p><strong>存在</strong>，基于 <strong>OI imbalance 的指数模型</strong>(OI_long ≠ OI_short 时收费/补贴)</p></li>
<li><p><strong>平衡市场多空仓位、激励对冲</strong>若多仓过多 → 支付 funding 给空仓，迫使持仓朝平衡方向移动</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="d90fc69d-b095-47c1-9381-cc57dbd86b77"><ul>
<li><p><strong>无 Funding但用点差有类似效果</strong></p></li>
<li><p><strong>不使用 funding，而使用 price impact &amp; skew spread 调节仓位分布</strong></p></li>
</ul></td>
</tr>
<tr data-local-id="9ef1fe47-cc19-4a13-a557-4a2d4789dcae">
<td class="confluenceTd" data-local-id="db0c30df-61b7-4c13-8a14-9755d81e8cf7"><p><strong>Borrow Fee</strong></p></td>
<td class="confluenceTd" data-local-id="63876a9b-554e-48fb-9123-2ece8c9c079f"><ul>
<li><p><strong>根据池子 Token 利用率收取</strong>（类似借币费用）</p></li>
<li><p><strong>分段线性模型</strong></p></li>
<li><p><strong>本质是交易者向 LP 借流动性的利息</strong>，reserve usage 越高 → borrow 越贵</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="1ee2c045-456a-4d24-b0bc-7bf0a195595b"><ul>
<li><p><strong>根据 USDC 可用余额与 OI skew 的曲线模型</strong></p></li>
<li><p><strong>分段曲线模型</strong></p></li>
<li><p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f9d4a71ed35e99a80953d396c1b328599d7be479149c89eb8f0a1f9f7a189dcf" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/51118271/Screenshot%202025-09-30%20at%2015.52.21.png?version=1&amp;modificationDate=1765285008361&amp;cacheVersion=1&amp;api=v2" data-height="153" data-width="658" data-unresolved-comment-count="0" data-linked-resource-id="52330638" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 15.52.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="51118271" data-linked-resource-container-version="6" data-media-id="3ad1cc8e-c5cb-448a-836b-8ef6d2d8bcd3" data-media-type="file" width="184" height="42" alt="Screenshot 2025-09-30 at 15.52.21.png" /></span></p>
<p>BaseFee 基于标的对应设定不同值。基于OI skew 与资产占用率utilization调整</p></li>
<li><p>感觉像是按10%APR倒推回去算的</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1825d42ba94cc0178113495c49ce1193ebcb0feaccd6371365daacacf9fd74fe" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/51118271/Screenshot%202025-12-09%20at%2021.09.03.png?version=1&amp;modificationDate=1765285812311&amp;cacheVersion=1&amp;api=v2" data-height="101" data-width="578" data-unresolved-comment-count="0" data-linked-resource-id="52002945" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 21.09.03.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="51118271" data-linked-resource-container-version="6" data-media-id="82a91e45-4412-4ae4-8a03-b0b9e77355df" data-media-type="file" width="149" height="26" alt="Screenshot 2025-12-09 at 21.09.03.png" /></span></p></li>
</ul></td>
</tr>
<tr data-local-id="9caf0455-eb9b-4735-8fb9-5347b463ab7a">
<td class="confluenceTd" data-local-id="493e8b81-65a9-45f3-a612-f09d4f123ff1"><p><strong>Spread / Price Impact</strong></p></td>
<td class="confluenceTd" data-local-id="38dacae7-db80-45b5-a5c1-018513696a79"><p>动态 price impact（指数）</p>
<p><strong>交易成本基础部分</strong>价格波动剧烈、池子失衡、流动性紧张 → spread/price impact↑</p></td>
<td class="confluenceTd" data-local-id="908801fc-8810-4c8e-be72-01d5a628dbae"><ul>
<li><p>Dynamic Spread = Constant + Price Impact + Skew Impact</p></li>
</ul>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f15f13b5b1348070c9c79361d8d6cc0787a607ccb5ef397424502ba6f7157878" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/51118271/Screenshot%202025-12-09%20at%2021.00.13.png?version=1&amp;modificationDate=1765285255249&amp;cacheVersion=1&amp;api=v2" data-height="644" data-width="1343" data-unresolved-comment-count="0" data-linked-resource-id="52330646" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 21.00.13.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="51118271" data-linked-resource-container-version="6" data-media-id="da0a0880-da58-419e-a60b-d1b49fa23f04" data-media-type="file" width="173" height="83" alt="Screenshot 2025-12-09 at 21.00.13.png" /></span></td>
</tr>
<tr data-local-id="bf9c5d4b-4e6b-4d0d-92b4-d3ad8891cf51">
<td class="confluenceTd" data-local-id="2ad88b3e-3aca-44c9-a30b-66905131c126"><p><strong>GMX独有</strong></p></td>
<td class="confluenceTd" data-local-id="1b67bc1a-6ad5-4f1a-b9e2-7b632d4079e3"><ul>
<li><p><strong>PnL Factor</strong> ：分为trade，withdraw，deposit三个行为不同市场下，参数都不同。限制未实现 PnL 对 Pool 估值的计入， <strong>防止极端行情穿仓</strong>，同时可以动态调节费用用来激励用户特定行为。</p></li>
</ul>
<blockquote>
<p>这里 pool value 包含了 uPnL 计算，因此为了保护 LP，避免用户在市场不健康的时候继续添加流动性带来不必要的损失，质押移除操作限制（max buyable sellable）考虑该参数。</p>
</blockquote>
<ul>
<li><p><strong>Reserve Factor：</strong>相当于buffer ratio的作用，给流动性池留有足够缓冲</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="91072168-6e3b-4574-90e4-5ea0619cee2f"></td>
</tr>
<tr data-local-id="e57abbbe-51a5-4e8b-8108-ad9ce1a1def5">
<td class="confluenceTd" data-local-id="a58143c8-3510-4786-8f02-ae5a8e10b455"><p><strong>Avantis独有</strong></p></td>
<td class="confluenceTd" data-local-id="ca9686aa-6342-479c-a314-0e39833d4805"></td>
<td class="confluenceTd" data-local-id="fd80e5db-6cc2-4694-b8b8-b79ba921853a"><ul>
<li><p><strong>仅针对高杠杆仓位：不收手续费；但盈利抽成：</strong>抽成pnl 80%到2.5%不等。pnl%越高抽成越少。虽不收取手续费，止损线很高。</p></li>
</ul>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="778b0f2b24ada48d65f5d355204e2b8363d4de48ef17662455094678d85ce584" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/51118271/Screenshot%202025-12-09%20at%2021.05.53.png?version=1&amp;modificationDate=1765285922714&amp;cacheVersion=1&amp;api=v2" data-height="464" data-width="805" data-unresolved-comment-count="0" data-linked-resource-id="52002953" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 21.05.53.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="51118271" data-linked-resource-container-version="6" data-media-id="6474eb11-2079-46ce-80ea-88b281570b3b" data-media-type="file" width="204" height="117" alt="Screenshot 2025-12-09 at 21.05.53.png" /></span>
<ul>
<li><p><strong>仅针对于市场行情极度单边倒的资产：</strong>爆仓补偿 最高返20%给亏损交易者</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="47bc8bb47b15e54bccfda59ecac906adf32c798ef90c07c6bc925fa3bf4aea3c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/51118271/Screenshot%202025-12-09%20at%2021.13.19.png?version=1&amp;modificationDate=1765286301214&amp;cacheVersion=1&amp;api=v2" data-height="476" data-width="718" data-unresolved-comment-count="0" data-linked-resource-id="52002963" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-09 at 21.13.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="51118271" data-linked-resource-container-version="6" data-media-id="3a0f5722-9b55-4406-b495-d3f21d6bbeb6" data-media-type="file" width="173" height="114" alt="Screenshot 2025-12-09 at 21.13.19.png" /></span></p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

# 6. 决策点

> 技术架构基于gmx：\
> 1. 合约只支持：pool - pair 1v1

## A. 市场结构与流动性层

1.  第三方创建的Pool 流动性添加移除权限是否开放给 LP：<span colorid="tfuyvkeptf">✅ 开放给用户。</span>

    1.  <span colorid="jebbsp7ffx"> ~~冲突点：avantis没有自主建池，所以用户直接存钱进vault层，不与market做交互。但是在自主建池的场景下，我们无法把vault层的资金投入高风险市场。~~</span>

2.  自主建池是否强制隔离（每个 market 独立 token）HzLP：BNB/USD - oracle

    1.  <span colorid="m6uxpus9bq">没有那么大自由度，强限制场景。</span>

3.  Vault 是否支持用户手动 shift allocation <span colorid="c3p6fo787i"> 不支持</span>

    1.  ~~冲突点：GMX支持多空保证金相同的LP token swap。但我们都是多空usdc，理论上可以随意shift。~~

4.  pool & vault是否接入第三方对冲（keyrock 等）

    1.  <span colorid="dk5ha2nlb7">考虑在rwa资产场景下，需要对应的产品设计。可以留出对应的合约设计接口。测试网阶段暂时不考虑。</span>

5.  vault页：市场列表放那些，vault对应聚合哪几个 当前沿用demo版本4个vault对应聚合4个不同资产类型的池子。

    1.  <span colorid="qunkxw2ga0">开放多级的vault存入，以及gm pool 流动性存提权限，提供更高的 lp 存取自由度。</span>

6.  是否需要增加体验金功能。

    1.  一般交易所体验金功能只返回盈利。avantis，gmx，lighter，edgex主流dex没有体验金功能。

    2.  <span colorid="oixlsfirv9">怎么能实现怎么做，是需要的。运营层面规避套利风险</span>

## B. 仓位与交易逻辑

6.  仓位合并 vs 独立仓位<span colorid="pylqtppxgp"> 待确认，测试网版本按合并做。</span>

    1.  <span colorid="w7m26zcajg">冲突点：所有内部查询逻辑必须从 “按 4 元组 index 查” → “按 positionId 查”，这导致从底层到上层的链式变化，订单模型、清算模型、TPSL 全量受影响。代码修改中但影响范围大。</span>

7.  <span colorid="rveaebayhi">系统级 TP/SL 是否采用 ±2500% / -80% 待确认。</span>

    1.  <span colorid="x2smgi4xa2">冲突点：-80%止损是指，针对pnl为负的止损单，哪怕劣于预言机价格，也按用户输入止损价格严格执行。猜测由keeper fee那部分资金来补偿。</span>

8.  <span colorid="jc5ry64bk7">Liquidation rebate（爆仓补贴）是否启用？</span>

    1.  <span colorid="r4y4p9i8t2">冲突点：若补贴，是否会影响到LP的收益？具体如何实现？是否通过改变强平价格公式来‘假实现’？</span>

9.  <span colorid="a1iqz7wt1l">高杠杆是否 zero-fee，盈利抽成（profit share）机制是否启用</span>

10. 一键交易是否启用？

## C. 收费/返佣体系 待确认

14. <span colorid="j43vr25mcf">是否做多级返佣体系？沿用 Avantis？</span>

15. <span colorid="rrix27rlwl">交易费 split 到 LP / keeper / treasury 的比例</span>

16. <span colorid="jkb7i8d936">Keeper incentive 结构是否更改</span>

## D. 风险管理

17. 是否采用 GMX 风格 PnL factor

18. 是否需要 insurance module（隔离极端 pnl）

19. extreme loss handling 是否照抄 Avantis 的 buffer/SM 逻辑

## E. 产品交互与上线策略

20. <span colorid="lv5dlm77tv">主网上线时的交互范围 ok</span>

21. 合约审计是否需要排在测试网发布前

22. 主网时间窗口（需要锁定范围）；能接受主网上线的时候整个交互情况是怎么样的。

# **7. 修改哪些合约？（产品确认后技术补充）**

## **价格机制：移除 GMX price impact → 引入 vAMM Engine**

涉及合约：

- `PositionPricing.sol`

- `SwapPricingUtils.sol`

- `MarketUtils.sol`

- `PriceImpactUtils.sol`（彻底废弃）

替换为：

- `vAMM.sol`

  - 维护虚拟 liquidity（k=xy 或其他 invariant）

  - 维护 skew（net long - net short）

  - 通过 skew 计算 slippage

  - positive slippage incentive

  - negative skew rebate

根本变化：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GMX: real AMM price impact = f(tokenBalance)
Avantis: vAMM curve price impact = f(skew)
```

</div>

</div>

这两个模型无法共存，需要完全替换 price route。

## **PnL 机制：从 GM 池子余额 → buffer-based PnL**

涉及 GMX 合约：

- `PositionUtils`.

- `PositionStore`.

- `MarketToken.sol`（GM token）

- `MarketUtils.sol`（LP token 估值）

- `FeeHandler.sol`

修改方向：

- 移除 GM token（每个市场独立 LP）→ **单一 avUSDC vault (ERC4626)**

- PnL 只影响 buffer（uint256 bufferUSD）

新增：

- `BufferManager.sol`（liquidity buffer）

- `InsuranceModule.sol`（SM vault）

- `WithdrawalGuard.sol`（VBR + dynamic exit fee）

GMX LP 的所有风险参数（reserveFactor, maxPnlFactor, borrowing factor）全部移除。

## **Fees：移除交易费 → 添加 ZFP（profit-sharing）**

> ZFP 是“只有盈利抽取手续费”，GMX 的全套 fee 模型全部要换掉。

删除 GMX 费用：

- borrow fee

- funding fee

- swap fee

新增：

- `ZFPFeeManager.sol`

  - on close position：profit × curve(percent)

## **Liquidation：加入 Avantis 风格的 guaranteed SL + liquidation reward**

GMX 清算模块：

- `LiquidationUtils.sol`

替换要点：

- oracle jump 时亏损方向 SL 也按用户设置价格执行（需 keeper 补差价 → 从 buffer or SM 出）

- liquidation reward 固定占亏损的 15%

- ZFP: minimum SL distance（ -30%）

## **External MM hedge**

如果加入 Keyrock 类似外部对冲：

- 新增 `HedgeRouter.sol`

- 保证 Oracle/ keeper 的 hedge 和 protocol PnL 对齐

GMX 不支持外部 hedge。

# 8. GMX → Avantis 机制迁移的技术难度 / 风险总结**（产品确认后技术补充复杂程度，影响涉及与大概耗时）**

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 组件 | 可复用？ | **需修改** | **牵扯** |
| 订单系统（TP/SL） | **部分可复用** | 触发逻辑可复用，执行逻辑需重写 |  |
| PositionStore / account engine | **部分可复用** | sizing、margin 很像 |  |
| GM liquidity pool | ❌ 不可复用 | 完全不同 |  |
| price impact | ❌ 不可复用 | 必须用 vAMM |  |
| PnL 计算 | ❌ | LP exposure 不同 |  |
| funding/borrow fee | ❌ | ZFP 避免 funding/borrow |  |
| Liquidation | 部分可复用 | keeper 系统可用，但流程与清算线不同 |  |
| Fee 分配模型 | ❌ | ZFP 完全不同 |  |

</div>

</div>
