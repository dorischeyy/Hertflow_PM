# GMX 配置项梳理

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270915954 {padding: 0px;}
div.rbtoc1772270915954 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270915954 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270915954">

<style>[data-colorid=f8daqtt6hm]{color:#ff5630} html[data-color-mode=dark] [data-colorid=f8daqtt6hm]{color:#cf2600}</style>

- [1. Market 核心配置](#GMX配置项梳理-1.Market核心配置)
- [2. General 配置](#GMX配置项梳理-2.General配置)

</div>

## 1. Market 核心配置

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="b04b6103-6e06-49a4-ba2f-2fb94c90f3ad">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr data-local-id="b8e10b23-dd9e-406f-b23d-b66c348ded25">
<th class="confluenceTh" data-local-id="fee6f58a-3cbc-46f7-b422-1dc44a3e0e02"><p>Key</p></th>
<th class="confluenceTh" data-local-id="abb103b4-4409-4d5f-9771-0baa67d1f5a6"><p>精度</p></th>
<th class="confluenceTh" data-local-id="3e1c9ed0-abf2-4fbd-b141-c4f0f579ef0c"><p>Example</p></th>
<th class="confluenceTh" data-local-id="2019aed2-c6ac-4f7c-9b31-8f0e557f2285"><p>Desc</p></th>
</tr>
&#10;<tr data-local-id="beff6f3d-5d13-4a43-aad5-1346fa79efb2">
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="08687e90-ed15-4ac8-9245-82730809b179"><p>tokens.indexToken</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="f3f45135-5f57-425a-a041-d928a12aaeda"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="b6a00a18-cfbf-4d44-82f9-8d798fbedbca"><p>BTC</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="7f7b9662-509f-48e3-8b2e-c76f59bb6ffd"><p>-</p></td>
</tr>
<tr data-local-id="2e5a13b3-94bd-4bf4-8eea-b312bd1b9516">
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="ee71b0ef-63a7-4a36-a1f1-3c325ca095bb"><p>tokens.longToken</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="7a070634-ab29-41d9-8f60-206f60c7427f"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="54496f72-2268-40e1-aea6-10a5035b0a8b"><p>BTC</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="2f57beb3-c23e-4bf7-bca2-877ad67b20af"><p>-</p></td>
</tr>
<tr data-local-id="3b921ee1-5d80-4198-aa88-d38f68e1fe17">
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="ba86b9e5-2ba1-4f9f-9139-071f9884ab99"><p>tokens.shortToken</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="0bb497c9-7603-45ab-af16-d8ffcce496cd"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="f3b80d79-08ee-48e0-8f09-1b4032f61dad"><p>USDC</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="80116938-e736-4231-97d1-8ef6414e213b"><p>-</p></td>
</tr>
<tr data-local-id="733aeccf-43c6-418c-b7cf-9340d99bd7dd">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="429143f8-8459-46c0-bd50-b5c97680f2d5"><p>swapOnly</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b89f738e-f20e-405c-9b49-65020d157199"><p>bool</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="43d4a6eb-387f-4e7a-aee7-38c4edc4fd0a"><p>true</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="abad42cd-b5be-464d-b860-5ac8232ae69b"><p>是否仅支持代币兑换（不支持永续仓位）。</p></td>
</tr>
<tr data-local-id="e43c5e39-8f13-4b57-8a56-1e0a6a023e1e">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="9314c354-86ed-4688-aa95-93e403ae1f12"><p>virtualMarketId</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="82bfb8de-9480-46f7-9518-748aea722367"><p>bytes32</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="3226e2a4-851d-45cd-9b35-bf315917d2a6"><p>hashString("SPOT:APE/USD")</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="dea7c9fc-5799-4bf1-9c0a-f143c01970a9"><p>swap 的虚拟市场标识。</p></td>
</tr>
<tr data-local-id="e0b75f32-35bf-4941-9e92-ab165014fdcf">
<td class="confluenceTd" data-highlight-colour="#ffbdad" data-local-id="ecca7545-c4e8-4463-8aa0-3318cec7750c"><p>virtualTokenIdForIndexToken</p></td>
<td class="confluenceTd" data-highlight-colour="#ffbdad" data-local-id="7059e437-d5de-416e-925e-28bb114262d4"><p>bytes32</p></td>
<td class="confluenceTd" data-highlight-colour="#ffbdad" data-local-id="a2b0a363-e0f4-4df9-8d0c-9fb0f2c5492e"><p>hashString("PERP:APE/USD")</p></td>
<td class="confluenceTd" data-highlight-colour="#ffbdad" data-local-id="47f222bc-0633-404c-b50e-b732bf476d55"><p>合约的 index token 的虚拟库存</p></td>
</tr>
<tr data-local-id="4c68bced-b0cb-4f2d-bd36-202b4a2d5040">
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="7fc710f3-0e3f-4faa-a35d-87cc14bdbd57"><p>isDisabled</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="6c4b53b0-6df6-4f35-9d02-cc86567dfc24"><p>bool</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="d0d23e85-41bf-4023-9564-2d2d31ff0ece"><p>false</p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7" data-local-id="4faf1bc8-36a7-40b4-a03e-8ae93df597e3"><p>是否禁用此市场。</p></td>
</tr>
<tr data-local-id="e9347c84-c7b5-42f7-9566-b29c0343964a">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="693609ac-ca15-42e4-83e8-b01a563ea35f"><p>reserveFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="ae3e0893-8014-476d-b949-78e98a6aa484"><p>uint256, 30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="217f52d6-be93-482d-8e7a-503df4668ae1"><p>100%=1E30</p>
<p>60%=6E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="9137772d-0957-4dba-ad0c-171b52cdd963"><p>OI 可以占用的 poolUSD 比例</p>
<p>swap/increase/withdraw</p></td>
</tr>
<tr data-local-id="62b9955d-a557-4f79-a1ec-90212e325900">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="a51b28eb-2f2c-473d-b4c8-6d7af0aad37f"><p>reserveFactorLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="195676e0-5368-4738-adbf-75116f8fbd9b"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="febc6b44-8674-4d5b-8724-15755717af02"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="102d042b-cfb8-4fa2-aae8-be03e5b988fd"><p>多头侧的储备系数。</p></td>
</tr>
<tr data-local-id="eb918857-0524-4ccf-818a-7a3777c8ebfe">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="cd5454ae-c31d-435d-bd13-22c174a08c9d"><p>reserveFactorShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="86923b4c-0afc-4da1-8978-63aa290d8799"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="640ed296-7d1f-466e-bcf8-4fcf87e892d5"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f4fb6a05-4ca9-454d-80c6-18d74f3a52bf"><p>空头侧的储备系数。</p></td>
</tr>
<tr data-local-id="74721d06-4b27-41e4-aeeb-5c8e64de1bae">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1959403a-45d5-4043-8f54-256406160935"><p>openInterestReserveFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6862edfb-eae6-4f93-855f-650dcc9b183b"><p>uint256, 30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="911daed1-4ebe-42aa-9a73-f2b8039294c4"><p>100%=1E30</p>
<p>60%=6E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9501e196-96a5-4c4a-95fb-15ff95640961"><p>OI 可以占用的 poolUSD 比例，其实和上面的 reserveFactor 算法一模一样。</p>
<p>increase</p></td>
</tr>
<tr data-local-id="a310629f-4af3-40fd-b7d0-bf758ad3dc3a">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="2baf09c9-407e-4c81-83db-9df5ea2e7f36"><p>openInterestReserveFactorLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1fce63fa-652d-4a3c-9f06-789a40df740d"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="3ab3fbe3-5255-4da4-953d-7f2230fb3d19"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="809f65d4-8bf0-4d90-ae6f-6c14be120937"><p>多头 OI 储备系数。</p></td>
</tr>
<tr data-local-id="9c1e26e7-7c15-4064-a932-8dfe693510ae">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="378c7204-434f-4250-9a4e-51ab9e316bd8"><p>openInterestReserveFactorShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="2d2b09d8-8796-4e84-9b35-69b209485a4c"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5383fc01-c0cd-47d6-b9e2-6234a6d97b35"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5fe1dc2e-990c-4ce2-8a0e-3d8447c0fe6a"><p>空头 OI 储备系数。</p></td>
</tr>
<tr data-local-id="2ebd665a-3eb5-4318-81c7-fe2257320940">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="da58db8e-be68-4971-a3bf-3c695cd34ebf"><p>minCollateralFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="dc75a94b-03c4-481a-a477-2e51537411f4"><p>uint256, 30</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="a53fd0a4-ebdf-4e10-b728-6608a96e1ccc"><p>100%=1E30</p>
<p>60%=6E29</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="b8973ad5-ceb5-4fa3-9cdf-0469ac404546"><p>最小抵押率（影响最大杠杆）。</p></td>
</tr>
<tr data-local-id="16998606-17b6-48ec-9e33-52b359cc8b61">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="eb2f5243-a854-430a-8edd-3ffc9c6b1c48"><p>minCollateralFactorForLiquidation</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="6a6920f0-51a0-4970-9b38-0cf83f6195b0"><p>uint256, 30</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="067b91e5-2d8b-4fc9-a258-8f8b3afca667"><p>100%=1E30</p>
<p>60%=6E29</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="cd46e2cf-5976-4c68-89ce-31b478240305"><p>清算最小抵押率（低于则可被清算）。</p></td>
</tr>
<tr data-local-id="0171daa5-0ffc-40d4-96c7-6b41dbdb29ca">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="9e975fd9-9ead-499c-b713-d5532f7a34c6"><p>minCollateralFactorForOpenInterestMultiplier</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="b41ac50b-8950-4331-8bba-416f861e56a0"><p>uint256, 30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f2d9da51-d67e-4279-a391-b40199819fe4"><p>1.0=1E30</p>
<p>0.6=6E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e45322e8-8a8b-447e-aa1d-404e8dddb497"><p>辅助上面的 minCollateralFactor 使用，这个factor的算法是 OI * 该配置项，也就是说，OI越大，允许的最大杠杠就越小，是一种极端保守策略。</p></td>
</tr>
<tr data-local-id="d4bfbbe3-8d2e-419e-a859-1808e327961c">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="7290c649-0904-4c6a-bfbf-b4e9e08e81a0"><p>minCollateralFactorForOpenInterestMultiplierLong</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="eefa3cf2-df64-4aa0-b0d1-243b335177cc"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="62031af0-460a-4f03-bf10-0e02408f3556"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="9f94c60d-bb32-4003-a43c-0807698d3c4d"><p>多头随 OI 变化的抵押率增量。</p></td>
</tr>
<tr data-local-id="0e4e4db8-1ae8-4c7b-bd1c-472683362052">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="b7d1660e-31b7-4088-bc4d-ee390d10517e"><p>minCollateralFactorForOpenInterestMultiplierShort</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="7cf4c238-8ff7-4190-b879-9d9a50c6f2f1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="6853a3ec-9e78-4b67-9ea1-aa4afd31eee1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="309447ee-4919-4bff-aa2b-fd94b363a96a"><p>空头随 OI 变化的抵押率增量。</p></td>
</tr>
<tr data-local-id="2836ebbf-e8d4-4574-868d-05ebd76f92e2">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="eca4434a-d8a6-48a3-943b-a598d9cd3b9c"><p>maxPoolAmount</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="787b7181-c8d2-4d19-b9ac-99d8a0fe6521"><p>token 精度，比如 ETH = 18</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5267077f-3279-45fc-9cf3-6bb10d9a7cca"><p>3 ETH = 3E18</p>
<p>5 DOGE = 5E8</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e2b439dc-f298-4a23-aa42-f274917edceb"><p>最大代币数量</p>
<p>swap</p></td>
</tr>
<tr data-local-id="d4eb56b3-d814-4012-9678-152e3060bbf0">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6f36b245-1c8c-4054-80a7-f7c14915c828"><p>maxLongTokenPoolAmount</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e0839ac8-f220-43ef-813a-a3cb47ab7af1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0ff8c59b-aa57-44cc-9b3d-bb9e02d912f8"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9baafc0b-a7a3-49b4-82f7-ef60573059b4"><p>多头侧池子的最大代币数量。</p></td>
</tr>
<tr data-local-id="637e6998-c3c5-4baf-bf11-dd67f8d9047e">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="37121dca-6883-400d-a19f-dde79ffe6338"><p>maxShortTokenPoolAmount</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c7f9fac3-05ab-489f-b9d1-810dc414beb8"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="913e53da-f378-49fc-beb4-a74ca42e0995"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="51a83aba-d379-4014-ac9b-0322abb7f364"><p>空头侧池子的最大代币数量。</p></td>
</tr>
<tr data-local-id="39ec7711-e70b-4a11-91ed-7d2c559d1654">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="8d68aaeb-a45a-4495-b2b6-789daf952512"><p>maxPoolUsdForDeposit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="29c75e84-fc6f-48d8-b99e-77c97d36d889"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="dd47127a-f876-4f46-87ca-fc53bdee5daf"><p>5 USD = 5E30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f0867c40-0997-44eb-b95e-1570ec8d7e64"><p>市场可接受的最大美元存入上限。</p></td>
</tr>
<tr data-local-id="034d923c-ccf9-4973-87b7-615e99a52dad">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="c7350ac7-d1b5-41f3-8a76-9a0be2d8c016"><p>maxLongTokenPoolUsdForDeposit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="33154be2-653a-4c3a-b9cd-e1894156d17d"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="60ee04d5-37f4-4aac-b5d9-79a5b17d6a0e"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="b38928f9-07f8-47f5-a0ed-a4a138d41548"><p>多头侧最大美元存入上限。</p></td>
</tr>
<tr data-local-id="4862eb08-0bee-43ba-8277-c7fa6917f247">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="ed25b931-ea6e-4709-875c-bbc72c68a544"><p>maxShortTokenPoolUsdForDeposit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="d01b0aa7-7181-4fdd-a2ec-fee805e832a3"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="6d9bbbdc-28b0-4daf-a99a-fe1a0e50bebe"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="4a0e6f0b-1906-4c44-b312-3322124d7ab3"><p>空头侧最大美元存入上限。</p></td>
</tr>
<tr data-local-id="401be404-d516-4133-8e35-a9d21b19c987">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="18ad2dc0-9a7e-4626-bd7f-eb96cb4431ed"><p>maxOpenInterest</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="63a66c98-b760-4568-b66f-ce1037fb7a67"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="b0df6487-1ddf-4b8d-8bd7-24f1af940020"><p>5 USD = 5E30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0373e142-aa26-4928-9773-d459900d02b2"><p>市场允许的最大总持仓（美元）。</p>
<p>Increase / Decrease</p></td>
</tr>
<tr data-local-id="5cf64fd3-e116-48c5-8ec1-94d946005fbc">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="042662df-f95f-4090-af70-5d5546992dc1"><p>maxOpenInterestForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="71d8d7fd-f666-401b-b21b-5ae2d30206c2"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e2b1c5ff-726a-43c3-8b7e-6a7e1c33dd78"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="eac9a9d6-4dd8-414f-af5e-dae1d7a2b8f2"><p>多头最大持仓（美元）。</p></td>
</tr>
<tr data-local-id="08271538-d0a9-4e8f-8649-9a455201421f">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cd0bb69a-ae0e-4685-9e4e-16d52a01887e"><p>maxOpenInterestForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d87cc3d1-5686-485a-8018-11b362bf0734"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6d1b72ae-8e3e-4628-b328-7669413e0fa9"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="ac2a5c42-2e41-4669-9770-6a238447f96f"><p>空头最大持仓（美元）。</p></td>
</tr>
<tr data-local-id="b22761ee-c66a-4178-9aa6-5d392a0a3e07">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="ba346abc-4efd-4d4b-bf21-5adf8c087e0b"><p>maxPnlFactorForTraders</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="fb53cc81-13ce-40eb-9230-d0cf80e674ba"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="167d0c35-b5ea-446b-b362-1fa312463f6a"><p>10%=1E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="6fa0594f-fd9e-452e-a898-7d6c3559a868"><p>交易者可实现的最大利润因子（相对池子USD）。</p>
<p>Decrease 计算仓位 PnL 时使用这个做 cap。</p>
<p>这里应该贴近于 100%，代码逻辑看来是强制缩放，就是直接把 PnL 打折。</p></td>
</tr>
<tr data-local-id="049fad5b-b21e-49b2-9646-9f8412427ca1">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e2e219fe-8875-4af9-9a27-e54444fa52ee"><p>maxPnlFactorForTradersLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="4ea96e6f-fe14-4fbe-b6c6-b26bba981dfd"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="4f4eb75a-2d88-48c1-a23a-3be497b8c034"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="36c1eda0-85f9-48f3-a969-4e6569ba9aaf"><p>多头交易者的最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="7dd9630c-f967-45d0-93b2-343419edaa2c">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="c0647623-d246-4a5b-a6b8-b44f97c14d0d"><p>maxPnlFactorForTradersShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="00def394-f78f-41c4-8a7b-123725a08833"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="c61675b3-1e12-4188-af0d-f004d398f6b2"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e21f278f-653c-4ecb-8974-cc0b10461b21"><p>空头交易者的最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="a41dfe86-55d9-4fa9-a054-996e883c30bd">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0944ff61-5c72-490b-90f9-e17b6b068cd1"><p>maxPnlFactorForAdl</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="fab9e440-c81a-44ad-a0e5-796df669f4cb"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="63cdc742-62fa-4765-84fb-de95b8cc3cf3"><p>80%=8E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="93536e8e-14f8-4f85-afd6-4cafc8a6018c"><p>ADL（自动减仓）触发的最大 PnL 因子阈值。</p>
<p>用于给 ADL 单做校验。</p></td>
</tr>
<tr data-local-id="0fe64863-31c4-4d67-ad27-91a8395459cf">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="bed3de31-d91f-4217-808c-f89e46e52ab1"><p>maxPnlFactorForAdlLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1b319aaa-625e-4b41-b68e-dad678240298"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9cf2dfad-43d4-4460-986b-cace1860a1b1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="2f8c830e-f2bb-46e6-ba63-0f2c883b2453"><p>多头侧 ADL 最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="7be5546c-963a-4b19-b377-e41a76b2bcc2">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c33ea1c0-c44a-4a7d-8aa2-1ff5e359f7ba"><p>maxPnlFactorForAdlShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="3de39e45-2402-4e0f-8984-595af9ad6ada"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f43b3ad1-6ea4-4219-a7bf-a931e7cf690e"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d43b075d-70da-42e4-8c24-2865ea0a5e7d"><p>空头侧 ADL 最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="e7f240c3-7d56-4f0c-b5b1-db13f6c03c32">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="dbf65079-a571-4258-9380-81a447f9d8e5"><p>minPnlFactorAfterAdl</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="d6700da8-7785-41fb-9fbb-719cd0dd828a"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="62204d30-6dfe-4a83-8399-eb178d03c38f"><p>75%=75E28</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="a3c43d26-cd2a-4c41-886d-d99f2dc1fb94"><p>ADL 后保留的最小 PnL 因子。</p>
<p>执行 ADL 之后，不能小于这个值，否则认为 ADL 过度。</p></td>
</tr>
<tr data-local-id="8f843495-931a-46ae-b514-ac74300696d7">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="688a92b4-46ff-4c86-8532-439378ba075d"><p>minPnlFactorAfterAdlLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="d0d82e1d-c4a1-44fe-b05a-796571f8ceef"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="70706f8c-2796-4311-a06c-0e3329a87930"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="da93594c-f6e9-4684-8cdc-499f90cbe875"><p>多头 ADL 后最小 PnL 因子。</p></td>
</tr>
<tr data-local-id="436b724e-365f-490e-b375-6b5f82df7a99">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="5177adf6-44db-4177-bfe2-5743cdf1c8a0"><p>minPnlFactorAfterAdlShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="39fe0d60-008c-4f87-920a-d9160408efd9"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="3ef6aee7-55e0-4c5a-a665-3b3f901f7647"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f7b17688-55af-471c-b3bc-acfb04738f31"><p>空头 ADL 后最小 PnL 因子。</p></td>
</tr>
<tr data-local-id="dea07adc-bf64-49ee-8dab-ba34ad1f721c">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="2e3b9f0a-56e4-4c57-8fe5-8b71afd1f9c9"><p>maxPnlFactorForDeposits</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="ef59f8b4-8ec0-44b8-b9ea-d8918def2ab9"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="4f4a7d64-4108-4e0a-9d36-6dfe42c56b9e"><p>80%=8E29</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="29b1342b-5e4c-4748-9330-0b10b1a06fd1"><p>入金估值时使用的最大 PnL 因子（防存入博弈）。</p>
<p>也用来校验 swap 之后是否会导致超出。</p></td>
</tr>
<tr data-local-id="9659437e-3f0d-44bc-848f-60fa61891532">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="44890714-ffa1-4717-a658-333dba6712a8"><p>maxPnlFactorForDepositsLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="bd6fc17a-dd1f-49c3-aa6a-059439989090"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="c4dd1baf-e8b5-48df-a9f6-5601a31f0ee7"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="24c954b3-074f-493f-bda0-9bd2ac236dd6"><p>多头入金最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="6866eed5-b96c-47f4-adcf-13195d03cfb2">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="0ee7aa8e-e26f-4253-a0a2-57acf84891c0"><p>maxPnlFactorForDepositsShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="6e594081-ea3c-4489-8d6f-4b15caf8e84b"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="69b8d0cb-1125-40ae-b377-93aa96071cc3"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="f71e79c9-b061-4eea-be64-04216ff93ff7"><p>空头入金最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="22f7d7a4-0ac0-4ba1-a8da-d746bd0a438b">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="c50c12ec-70f7-40a7-9a75-99053f7be226"><p>maxPnlFactorForWithdrawals</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="2ab1f538-de62-46e8-84a2-7871b51b91d3"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="21f86c39-d1a0-4773-92a9-9f66fc4d7dc8"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="c7108afd-1df9-4e07-84e5-448919550dff"><p>出金估值使用的最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="1bd075cc-26c4-4eae-86f9-2cbc23e70b31">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="f2c30b40-2d62-41d1-aab0-03db4023b72c"><p>maxPnlFactorForWithdrawalsLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="dc24bb73-0ad4-4ac3-becb-327d6ab77298"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="b19f2355-3de0-4b2c-859d-64e2be00a974"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="24c31afe-d4a3-43b5-ba77-3f44c4c4531b"><p>多头出金最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="71740509-76a0-4864-b6b4-4412a931ea21">
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="7bf3e64f-18d5-4690-b569-aca5dac80a58"><p>maxPnlFactorForWithdrawalsShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="f0054655-60b6-4af9-b15c-b97a83df655c"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="6be00f34-99b8-4b89-880b-54dbd7ab058d"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#abf5d1" data-local-id="d8b813da-e759-4b82-bb32-9d0913edf5b0"><p>空头出金最大 PnL 因子。</p></td>
</tr>
<tr data-local-id="9cca266d-ec58-4910-8f9a-2d0706f49824">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="635ddf18-4938-4deb-834f-33303586c365"><p>positionFeeFactorForPositiveImpact</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="beee35a4-3b77-41e1-93df-aaea79c6976f"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="8df04605-b7cf-49ed-b873-ee62e9050ec9"><p>1% = 1E28</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="337580a8-2ac0-4e0d-9c94-2c9d3b9522f9"><p>建仓/平仓 fee 在正向影响时的费用因子。</p>
<p>Increase / Decrease</p></td>
</tr>
<tr data-local-id="45bddbed-31f2-43cf-a7b4-8389a3d10cd8">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="7e09269b-7322-41d6-938b-297106b8abd1"><p>positionFeeFactorForNegativeImpact</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="ed8178bb-6c24-4a1f-9ce7-44d79bd213ca"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="b77b9560-238a-4768-bd55-03c73b203f20"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="82e67baf-8700-4005-9758-905df359a562"><p>建仓/平仓在负向影响时的费用因子。</p></td>
</tr>
<tr data-local-id="e44b5399-6889-427c-af1e-f30f575f6091">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7fbc50c5-1a33-476e-8dc3-e7e1f28a470e"><p>negativePositionImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="05691a19-12c7-4677-91e4-689b9b3084bb"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d6ba2d68-8ad7-4314-b943-5953d1bd4fcc"><p>1.1 = 11E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="59eb14cd-fc0e-4bf5-b6aa-01990e45c23c"><p>仓位负面价格冲击的强度系数。</p>
<p><code>d0 ^ e * f - d1 ^ e * f</code></p>
<p>这个指代 f</p></td>
</tr>
<tr data-local-id="9ce7f40c-7226-4672-8c44-5cb049079819">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="458776cb-28fe-41ca-8eea-0f435ba2685e"><p>positivePositionImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c2163353-eed5-4843-aa6a-f1b0b75983c8"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1d64ed27-e5b3-410d-930f-8ae500e0d6ba"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="63505bbe-5824-4174-9cd2-2d8e56d58f8a"><p>仓位正面价格冲击的强度系数。</p></td>
</tr>
<tr data-local-id="d7d7ff70-3587-45bd-b2d4-e35be2d8b127">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="224ded05-1c97-4509-ac0a-3a4adbb87645"><p>positionImpactExponentFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6e786aff-c42c-49c5-a78c-7808a1905a88"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cf1300f1-ed97-4b1b-a8e2-d006570386da"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="92d41438-bbaf-4e07-9d1f-8786704e831e"><p>仓位影响的指数（曲线陡峭度）。</p>
<p><code>d0 ^ e * f - d1 ^ e * f</code></p>
<p>这个指代 e</p></td>
</tr>
<tr data-local-id="3be4b9e6-7884-4c8d-8884-020801a61209">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e2b226a6-c4f0-4040-9754-d14fdc0fb6e2"><p>negativeSwapImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cfc0ba25-abde-4f9d-96e7-a0302f54f108"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8a08bb92-5125-489c-9496-4f1fb1becb96"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6334c037-bab5-4710-9a49-866d634a599d"><p>兑换负面价格冲击强度系数。</p></td>
</tr>
<tr data-local-id="3a1b2af4-ebfb-4a0c-abd0-03d7388ed9aa">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9636292b-afad-481b-94cd-99204cf49fc5"><p>positiveSwapImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4a9f4dc7-d68d-4f0b-83b9-feff6f53e510"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="93993e13-0fae-4141-a90a-d4fb45d5b2bc"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d37b5f06-7e80-48c9-8eb6-7cfa3350dfb1"><p>兑换正面价格冲击强度系数。</p></td>
</tr>
<tr data-local-id="7d01a1fe-265c-424f-971a-0d3e9c797368">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="95edd983-3783-4805-8e3e-e46d85989d72"><p>swapImpactExponentFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9e2f5c9c-b6e0-4974-a743-cdbf1d4ab0c4"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4dbf77b7-41e7-44c2-afc2-8f72d57df3ea"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9e8f3978-b4fe-447d-ac45-61a2d74483fc"><p>兑换影响的指数（曲线陡峭度）。</p></td>
</tr>
<tr data-local-id="afa13354-2872-4e1c-b97f-05d5001cf9b9">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="545aa905-7800-4bfb-aff5-d9d6c7a21d63"><p>negativeMaxPositionImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f77a1f23-7fdd-4ea0-8ce3-5e0e845d8cd7"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="c6609207-5071-4438-a62c-c5a296892d66"><p>2%=2E28</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="b726452a-b03f-4963-a6fa-b776812b2a06"><p>仓位负面价格冲击的最大上限。</p></td>
</tr>
<tr data-local-id="90342978-6b6f-4122-bd08-ed88f8f39c04">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="f01cc7e6-e9be-4788-a8cb-a01671fe1809"><p>positiveMaxPositionImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="ca47342f-e1bc-4284-aade-c3c0f516e8e0"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="50ef2fd8-f42b-4f4e-a254-fe6cf4b6d756"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="82611cca-eefa-4fda-a69e-29b7b81fa95d"><p>仓位正面价格冲击的最大上限。</p></td>
</tr>
<tr data-local-id="0b21ffaa-8406-4ac0-ae2b-bf8e5830ae72">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="c9adad71-de4c-433b-a8be-c6f8d36745f9"><p>maxPositionImpactFactorForLiquidations</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="a6498071-cb48-47de-9e65-cb71f62fb56b"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="232ee7b1-ac94-4251-90f2-a23483eb1f1d"><p>2%=2E28</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="7e38cafe-f038-41ab-b939-2bf8908b04d8"><p>清算校验时可应用的最大价格冲击上限。</p>
<p>// if there is a large build up of open interest and a sudden large price movement, it may result in a large imbalance between longs and shorts, this could result in very large price impact temporarily, cap the max negative price impact to prevent cascading liquidations</p>
<p>这里只是判断 isLiquidatable 的时候会尝试少扣一些 impact fee之后，看看保证金是不是还是够的。</p></td>
</tr>
<tr data-local-id="39704a6b-3dd4-4944-8626-a36297098b03">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="a81f43b6-0588-42b1-9885-fa71347c4e8f"><p>liquidationFeeFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d355af62-57d2-449f-9ea0-4ea8e6e01897"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cb9f0b07-2278-42db-9c2f-91635dc28bd4"><p>1% = 1E28</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="edfdca0b-7a5f-450d-8ee9-b525363b8094"><p>清算费用因子。</p></td>
</tr>
<tr data-local-id="663039a4-576a-4196-acf7-8fdfb3a763b8">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="ccef8d08-8c08-44d1-a899-6dddd3438f77"><p>swapFeeFactorForPositiveImpact</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6d5102c8-db41-429b-981f-c9c480d9d853"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="ac47f5fc-c2fc-46e2-bfed-a3e134557150"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="52c9b029-c7d7-4502-8497-b7cbeb93c0e0"><p>兑换在正向影响时的费用因子。</p></td>
</tr>
<tr data-local-id="d105db9e-3146-4c81-9804-426e9b44649f">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f457575d-b833-4712-88ce-c315b06d29c3"><p>swapFeeFactorForNegativeImpact</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e20e47fd-5a7c-4272-92cb-a61e7a702b56"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f5421615-6d85-48c6-93b5-0dd3f712e5e1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="73a460ec-2419-4e98-92f3-e9252b248358"><p>兑换在负向影响时的费用因子。</p></td>
</tr>
<tr data-local-id="24e98b1f-f0cf-4c02-81df-81d4c50d0109">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="99d10ef3-cbd9-4b99-806f-7140d2593fdb"><p>atomicSwapFeeFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7127145a-b029-4670-9e25-2ea47b790aea"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9cf082d2-e775-4927-812e-37986708bb1b"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="76b13801-e2a9-426c-be27-00c8102fc680"><p>原子兑换（同块内即时）费用因子。</p></td>
</tr>
<tr data-local-id="b2f9a1cf-c6db-4676-afb7-42c4fc9cd595">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0f4ba309-d445-448d-aeb3-ec180812b32d"><p>atomicWithdrawalFeeFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="b7922518-3de3-4c19-bdca-28286e629152"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="21ba228d-9da9-42b6-9102-d57c332a5888"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="18b0d3cb-a2ae-456f-a0da-e57dee5915f4"><p>原子提取费用因子。</p></td>
</tr>
<tr data-local-id="ac8e2ff5-7a7a-4c50-beea-7f7b4b89f7d2">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="25a3ccd3-80bc-4e4d-851b-3f13f96938a1"><p>minCollateralUsd</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="21fb2fe2-4c9a-49bf-9c90-d6522d060f50"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e4b40630-73f5-44e2-a109-11cb95921439"><p>100 USD = 1E32</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="097f9742-fcbe-4dd3-9e83-553bbaeffd4c"><p>开仓所需的最小美元抵押。</p></td>
</tr>
<tr data-local-id="f5b1bb46-8488-4e7d-a287-f6e0e1e98964">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="da175041-65ac-44ad-b32e-dced54edbd0c"><p>aboveOptimalUsageBorrowingFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="25b0ac78-4712-45c3-ad94-22a83e527c98"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="ee1de613-3a74-40aa-b860-6275dc348291"><p>1.1 = 11E29</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="c930663d-dda5-4f6a-8b00-a06237f92867"><p>超过最优利用率后的借款费率增量。</p>
<p>kink 模型大斜率</p></td>
</tr>
<tr data-local-id="d5c6fc7c-2277-42d7-8d6e-27e6123aeee9">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="4b055b04-c786-4d7b-89b1-fa7bc37d2d7c"><p>aboveOptimalUsageBorrowingFactorForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="934c9ae4-a604-4153-8396-356feadf3f67"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b695e3af-ff2a-438d-ad71-bbc4a8a1a1da"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="236b85d7-d071-460a-ae70-568a887822ba"><p>多头侧超额利用率的借款增量。</p></td>
</tr>
<tr data-local-id="3ea1fd34-32f0-475f-90e9-163b01c33d58">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="3d7c7e65-fa3e-4881-9e3d-b726f23cd964"><p>aboveOptimalUsageBorrowingFactorForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="85e26150-ffa6-4a6e-a8fa-8b42e04e6d02"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="a68debc1-90f3-49f2-8fad-33bfd4e98f64"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="00b94917-5ae3-4058-a0b7-89e713749c9b"><p>空头侧超额利用率的借款增量。</p></td>
</tr>
<tr data-local-id="2ad1f99d-1835-469e-9e0a-f820aa49553e">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="66c058e7-79d8-4492-a9f1-63f6e157c85d"><p>baseBorrowingFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="a69c9e55-6f46-49fc-89a2-1c13d1bfcd3c"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="16369156-a3a8-4213-8d78-c707da0079ad"><p>1.1 = 11E29</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="1af1e490-2da0-4d56-8991-4242b9261eec"><p>基础借款费率。</p>
<p>kink 模型小斜率</p></td>
</tr>
<tr data-local-id="88059695-fc72-4012-b125-5823bee5f9a9">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="4e580cd2-e4e3-4bda-9644-d55157553839"><p>baseBorrowingFactorForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="97110ceb-2024-4bbe-b414-1e94598bcdbc"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="bd815769-6cc8-4611-adc4-3bd1dc0532f8"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="f0ac48b6-2d6f-4ae8-8e3f-7db824396870"><p>多头基础借款费率。</p></td>
</tr>
<tr data-local-id="fd4876f7-0d78-4145-b3c2-334b57f5a2f4">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="6b766789-ec0b-44d0-9e7a-cedf073c0fd1"><p>baseBorrowingFactorForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="c701607e-af28-4bd1-9ce9-2dc1730c0bf9"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b8357f0d-443f-43b5-bc3c-82add0531afe"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b705a735-7adc-4c03-9a88-a3fbf7bb991d"><p>空头基础借款费率。</p></td>
</tr>
<tr data-local-id="97a75b02-4168-423f-8040-e44a25fe48c7">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="30450c00-ac9e-471f-be24-cbbad455554e"><p>optimalUsageFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="a3383d7f-b612-4063-ba24-c25e437d6355"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b944f4b2-c84a-430f-9fbb-5c00fdaf01eb"><p>30%=3E29</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="f7f8f451-e4e7-4bfb-871b-56f8169fb38e"><p>资金池的最优利用率（拐点）。</p></td>
</tr>
<tr data-local-id="a690947b-567a-4c5b-9732-c06c7bbc2ae2">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="db320f1c-726a-40de-8e6a-392ded54d0fb"><p>optimalUsageFactorForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="ce76ff1f-95a5-4eb4-a980-540d46d227ef"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="512b45ac-697f-4e54-92f6-042ed6284310"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="ef25cd36-8648-4bd3-864b-c450083f642a"><p>多头侧最优利用率。</p></td>
</tr>
<tr data-local-id="116b554c-9d08-4ef9-bece-11278c41f58c">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="87d7f2de-335b-45a9-a214-ac8a16746f2f"><p>optimalUsageFactorForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="ea2df1b3-5f52-4617-b514-d76124cb53b9"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="a8933e2e-5087-48f7-8604-37b5e88ab92d"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="9f3e2bb4-fca1-4460-8f5f-f358705df997"><p>空头侧最优利用率。</p></td>
</tr>
<tr data-local-id="ede9c8f9-cc28-47fb-b6db-9016063cf9ad">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="cf3aee38-a43f-4691-b550-5db0be07548a"><p>borrowingFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="cf878b02-90f7-44e4-849a-4f36bafec0e8"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="1b55b03d-af25-4109-a399-0e1feec84f1f"><p>1.1 = 1.1E30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="9f004597-bec3-4d63-9eaf-93f2a3d37d4b"><p>借款费率（随利用率变动的系数）。</p>
<p>curve 模型乘数。</p>
<p>r^e / P * b 的 b</p></td>
</tr>
<tr data-local-id="e54c35fc-9b7c-46e5-8c37-a879cb7f0e62">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="e416cf83-5d92-4765-bc59-3cb0d16edaf4"><p>borrowingFactorForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="fc2a6aa0-a098-40aa-8a06-8b56c735363a"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="15970cbe-e566-4186-9268-45dbff9c0e92"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="e8b45208-0bff-4cf8-afdd-24255ec623da"><p>多头借款费率系数。</p></td>
</tr>
<tr data-local-id="a96dfc81-da2f-416c-b586-97c103386684">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="10713139-5bfd-4022-bf9d-f02fc4d0cb91"><p>borrowingFactorForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="9ad128b4-81d6-46e3-91c0-e02e42c9a665"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="8c1828fb-bb72-443e-904e-ded3b011d939"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="42b9364c-780c-49f7-a2f0-63b2344b05cb"><p>空头借款费率系数。</p></td>
</tr>
<tr data-local-id="0c45d097-f55b-44f8-af9a-167ae0606c32">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="7364a9c2-8f74-4a59-9603-464f8cbdd4d6"><p>borrowingExponentFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="307229b7-1efe-4403-b541-64976d56f2b1"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="292b0855-1282-4690-9c53-9ae8f230a623"><p>2 = 2E30</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="71283cca-a9e2-47d9-9ac9-746e2acd7b9f"><p>借款费率曲线的指数参数。</p>
<p>r^e / P * b 的 e</p></td>
</tr>
<tr data-local-id="43e28ebc-0085-435d-98fa-e272e012c205">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="5c67fb09-7473-4107-8742-d7ce4bb1a16c"><p>borrowingExponentFactorForLongs</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="18789050-6a3a-4684-9c79-d65b1e717d08"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="24d77c38-015b-429c-b892-bd6788a28e4d"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="9db4223a-9881-43ca-adc3-a1f32ec7a857"><p>多头借款曲线指数。</p></td>
</tr>
<tr data-local-id="eb403407-4cfd-4291-96fc-2889bce026f9">
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="84ae3c6c-4622-41aa-9900-c41c06cab51c"><p>borrowingExponentFactorForShorts</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="df995beb-85f5-4cc6-b2d1-97b5a71cb2b6"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="113e5e39-ad55-4370-93ad-1746e029e099"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#c0b6f2" data-local-id="0e006ff2-dcd2-426e-a1ef-6099a7f468ff"><p>空头借款曲线指数。</p></td>
</tr>
<tr data-local-id="46aa809f-6e55-4fcf-94df-c10f9bddc788">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cecd4404-3390-4545-80af-4d51462a91a8"><p>fundingFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="dc847313-8ffe-4462-995a-c9dcc86fc8c7"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="b65b716a-f402-489c-9516-327d167b6089"><p>1.1 = 11E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d856d01f-d666-4c11-a7f7-3f16f3b2ca10"><p>资金费率基数（与仓位偏斜相关）。</p>
<p>静态算法的乘数：</p>
<p><code>计算失衡程度 f = |L - S| ^ e / (L + S)</code></p>
<p><code>F = min(f * F_market, F_max)</code></p>
<p>这里的 F_market</p></td>
</tr>
<tr data-local-id="ac7d2b45-9607-420d-8db5-1d57413ae65d">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="647af0de-6f36-4f96-a680-8d3166406d50"><p>fundingExponentFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f52ae913-09aa-4a4a-9e7e-8340f247684a"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9f4e8724-7566-4b77-b42d-ee2c9d1dcf95"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="ff6b8125-c97b-41fe-b73b-e7a163d907ce"><p>资金费率曲线的指数参数。</p>
<p>上面的 e</p></td>
</tr>
<tr data-local-id="1ac6a327-c475-48ed-ba32-a488cb55f79d">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="b2c17044-56a8-4cb1-9f4c-dc014dc32adb"><p>fundingIncreaseFactorPerSecond</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1dcba046-c7eb-48da-b555-13bd7c595bff"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1f60da27-8c83-4c1a-b399-36a13903f2b4"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="45905551-7145-4a18-b5b9-cd7c7f05b052"><p>资金费率每秒上调速度（偏斜扩大时）。</p>
<p>动态算法。</p></td>
</tr>
<tr data-local-id="2720c2fb-b32b-4efb-bb99-2ad310d0c520">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8c5afedd-f068-4497-ae54-3c9578f5633f"><p>fundingDecreaseFactorPerSecond</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="630cd377-5158-446d-bcf0-eef0953226a1"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="24dcef90-5235-47d1-a33a-20d846a17a0b"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4ca01ce7-6105-45bc-bca5-cb6fdfeddcb1"><p>资金费率每秒下调速度（回归平衡时）。</p></td>
</tr>
<tr data-local-id="accb820d-3a05-49d0-b076-e27361a9cce5">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="73ff7968-3e8a-4b47-b966-10dcd13df687"><p>thresholdForStableFunding</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4b384c6d-ddf7-446f-99b9-553b13138fdf"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="72067941-f890-4677-8e25-084d7598fc14"><p>50% = 5E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5533b37e-9bdc-449c-b385-cb306d961179"><p>视为稳定（低偏斜）时的阈值。</p></td>
</tr>
<tr data-local-id="5bcb878e-4cc9-46e5-875c-5332c3b8d93d">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6edd7fda-0adf-413a-84f5-90bbf457ce83"><p>thresholdForDecreaseFunding</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="75d63e56-c026-4feb-8f77-55b73fe3c0d5"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="25e6cc25-cf34-44ef-a50c-ed04e3bcb725"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e1375dc3-2e33-40e0-b007-050033b0118e"><p>允许资金费率下降的偏斜阈值。</p></td>
</tr>
<tr data-local-id="ecbeefce-b154-40eb-8930-69360efca4e6">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9d14c990-7697-4393-a807-1ea9c6246080"><p>minFundingFactorPerSecond</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="03c1d88b-6f6f-4d9c-b4d6-eadbd315a1d0"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="fea17496-7535-4f84-a977-e8b2c86811e5"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="bfc99726-b818-4923-9875-e9cb9f58cda2"><p>每秒资金费率的下界。</p>
<p>cap</p></td>
</tr>
<tr data-local-id="101c994d-d26f-4879-a333-66831f3c5a2f">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="58041fc3-7318-4c22-ad3b-f43bce0b4541"><p>maxFundingFactorPerSecond</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f5168427-2b0a-4109-9494-91b54dab2377"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="83833517-b5ca-45e9-a882-ea8085ddb27f"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f69e2a53-2a3d-4022-91e6-3261be4ccc1e"><p>每秒资金费率的上界。</p></td>
</tr>
<tr data-local-id="9c08dc79-59a0-4c2a-8671-fce9a6aeb7e2">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="63affe10-00f0-4bda-84ff-b7fa595f10a0"><p>positionImpactPoolDistributionRate</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="3ec8f481-57e0-4a1c-a4be-b62b6bbaac57"><p>token 精度</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="ff5c068e-401a-4213-8de9-57b5674666cf"><p>每秒 distribute 的 token amount</p>
<p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e0a4598f-fd73-4400-ad35-90e2521f0728"><p>仓位影响池的分配速率（按标的代币计）。</p></td>
</tr>
<tr data-local-id="71c743b0-4f6f-4acd-bdde-65689068b102">
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="e2a0b09a-fb04-461d-8f9b-9c79fee9fa2b"><p>minPositionImpactPoolAmount</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="dfab5e0b-77b8-4ad4-895a-de51f486bf6f"><p>token 精度</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="c7af1066-d850-44dc-b8fb-73923a9a4be2"><p>1 USDC = 1E18</p></td>
<td class="confluenceTd" data-highlight-colour="#b3d4ff" data-local-id="92f6e812-a271-4a28-b5a7-0bb01ba1829b"><p>仓位影响池的最小余额。多的部分不 distribute 了，也就是说收了 impact fee，这部分逻辑上不会入池子，也就无法增加 pool value。</p></td>
</tr>
<tr data-local-id="62f6da74-122c-45e1-be7e-40a3fe8f343c">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="3ec59334-0003-4328-a355-afa5ed8bd41e"><p>maxLendableImpactFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e65f3d8a-008a-4b4c-9646-5cc8e8562060"><p>30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1d621be0-217b-454a-a426-6cbcd31230f9"><p>10% = 1E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5add1bdc-f253-4ebf-bf5c-094b9e0429f0"><p>可出借额度的影响因子上限。</p>
<p>impact 逻辑维护负债表避免奖励过度。</p></td>
</tr>
<tr data-local-id="422dd7c2-3210-4917-8d41-9bc5a805ee29">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="230b8d89-dc6d-4fed-a846-8737f8ae414c"><p>maxLendableImpactFactorForWithdrawals</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e069b707-97d6-4e93-ac2a-d115a4d0c9cf"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7e2db58d-a912-40c9-a2a1-29c47574ff7e"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="dfdd3a91-57e3-4a04-9aa0-f0dee4489275"><p>出金时可出借影响因子上限。</p>
<p>仅影响 withdraw</p></td>
</tr>
<tr data-local-id="dc74623b-2970-4fbb-ae34-86bea558ee87">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0b0bdb1b-9adf-4230-a5b4-53c4014d381d"><p>maxLendableImpactUsd</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4b566355-561a-42e9-b4f6-cac74fc9ee89"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e7f3c0a6-05f6-4ad5-aa7b-c186c1fb4d61"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c04a82a5-f9ac-4e5c-9e3b-c671a4986833"><p>可出借影响的美元上限。</p>
<p>cap 第一行。</p></td>
</tr>
</tbody>
</table>

</div>

## 2. General 配置

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a6b7abc6-aba3-47aa-a030-47d5108a239f">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr data-local-id="075441ee-a8a4-41a6-865f-c3b9b50f4916">
<td class="confluenceTd" data-local-id="57394515-7abb-4dba-aca1-c4b684575bb8"><p>Key</p></td>
<td class="confluenceTd" data-local-id="4ddc5f56-ac7f-4b5f-956f-eda2f33a50ef"><p>精度</p></td>
<td class="confluenceTd" data-local-id="8f969850-5f20-43d3-b6ec-7634b9881931"><p>example</p></td>
<td class="confluenceTd" data-local-id="921a0b12-4dbb-4ca1-bfe6-239f8c14d402"><p>Desc</p></td>
</tr>
<tr data-local-id="4a4ee958-1563-413f-97f0-faa034891f9f">
<td class="confluenceTd" data-local-id="3cfc5e12-af15-4c38-8468-080c135c41d8"><p>feeReceiver</p></td>
<td class="confluenceTd" data-local-id="212f7a24-dc0d-4f69-b1ee-5642e39de658"><p> addr</p></td>
<td class="confluenceTd" data-local-id="8d27cd9c-b340-4cc6-8813-80b4d4f4cf30"><p>0x123</p></td>
<td class="confluenceTd" data-local-id="d3336277-cf04-4863-9b7e-5aadd26cbccc"><p>FeeDistributorVault 地址，和抽水分配有关</p></td>
</tr>
<tr data-local-id="92d65aa9-517b-4f63-bf28-3ba80da0e2f0">
<td class="confluenceTd" data-local-id="1155e71c-69fb-4ea6-a92d-b6a21ff41e4c"><p>holdingAddress</p></td>
<td class="confluenceTd" data-local-id="32e75346-1851-4b39-9c50-e94b3dbc5246"><p> addr</p></td>
<td class="confluenceTd" data-local-id="6364db20-3736-4635-a1d0-afe90c35556c"><p>0x123</p></td>
<td class="confluenceTd" data-local-id="4658d48a-011a-4c25-8fe4-dbb27a90cd4c"><p>资金托管/持有地址，在转账失败的时候，不会直接 revert，而是会托管到这里。比如 GAS 不够。</p></td>
</tr>
<tr data-local-id="a2145c8e-f6fd-4d33-94e6-84649713db4f">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="232b311d-02a9-4add-bf00-b7d051961e8f"><p>sequencerUptimeFeed</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="75619329-547b-4401-b2a0-75ebaf42cde1"><p> addr</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c0d51e3b-6a26-4f69-9344-4fc23aeb8995"><p>0x123</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f60f27d7-87f8-404a-952c-d17e53cca266"><p>L2 定序器地址，BSC 应该不需要这个东西</p></td>
</tr>
<tr data-local-id="60404ee9-37c1-4b48-96be-b06946a5348e">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0c28d5b9-a4e6-4c0a-b635-8840590dcc07"><p>sequencerGraceDuration</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e0ca3e3b-1684-46ae-a48e-ec9d58bb808d"><p> seconds</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c1430c2b-0d8f-4d0f-a39f-b22db9195d0b"><p>300</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7158f1bf-0f7c-4dd9-a53d-b9a72a5ee2fe"><p>序列器故障宽限时间（秒）</p></td>
</tr>
<tr data-local-id="91204089-af9b-4ba2-9cce-41f3d69dad3a">
<td class="confluenceTd" data-local-id="71ae921f-a75e-4db4-ba64-d163fcccaa4a"><p>maxUiFeeFactor</p></td>
<td class="confluenceTd" data-local-id="c708a16e-f3d0-412c-963d-c9978303dde4"><p> 30</p></td>
<td class="confluenceTd" data-local-id="59ce81c5-2e4c-4baa-a7af-48c53ad12d34"><p>10%=1E29</p></td>
<td class="confluenceTd" data-local-id="ad6dc0e9-5961-4e5a-a796-499e3747c7cf"><p>前端/界面最大费用因子</p></td>
</tr>
<tr data-local-id="f82f1292-0562-462e-a32a-34d26d074957">
<td class="confluenceTd" data-local-id="69a41a5e-d380-4072-a64e-75ddaf4ba821"><p>maxAutoCancelOrders</p></td>
<td class="confluenceTd" data-local-id="fed6f39a-2212-4b71-8a75-4338c4e1673f"><p> 1</p></td>
<td class="confluenceTd" data-local-id="45aef651-872b-4224-990e-d4adb019dfcd"><p>11</p></td>
<td class="confluenceTd" data-local-id="0b636e7e-0b6f-49cb-a02e-8463e76c8106"><p>自动取消订单的最大数量</p></td>
</tr>
<tr data-local-id="ecb424a4-ea3a-48d2-bd5a-e09639ada681">
<td class="confluenceTd" data-local-id="557dccf7-dc5b-425a-8f08-f465a1efb746"><p>maxTotalCallbackGasLimitForAutoCancelOrders</p></td>
<td class="confluenceTd" data-local-id="9cfd800b-30ae-45ec-8beb-05042d79b29f"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="5c774009-70fb-4a58-9bf4-12f4b57bfef8"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="dbe8b8e7-a0ac-4e85-bc94-4c366ffc379e"><p>自动取消订单回调的总最大 Gas 限额</p></td>
</tr>
<tr data-local-id="f150515f-c00e-4db2-a3fb-6a31a3a32a5b">
<td class="confluenceTd" data-local-id="8c13f59b-6768-4dc3-ad4a-5438c9eb5d48"><p>minHandleExecutionErrorGas</p></td>
<td class="confluenceTd" data-local-id="843b8796-fbb0-4c3e-967b-2f4436cbd88d"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="4ab0c109-8e20-42a0-8b4e-231e3eb8758f"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="1f445c07-ee09-44da-a65a-04b953dae9f9"><p>处理执行错误的最小 Gas</p></td>
</tr>
<tr data-local-id="631809b9-f1e4-405a-b89f-e43c70192178">
<td class="confluenceTd" data-local-id="3d30bb5f-e6c8-4afc-aca6-a8d7a96888cf"><p>minHandleExecutionErrorGasToForward</p></td>
<td class="confluenceTd" data-local-id="42e9c376-c606-45e5-890b-f9ac714f2d7e"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="755b1ca9-da21-469e-aeb5-8bb6e858b910"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="965cf35e-0378-49c9-a6b0-1250db19fc51"><p>转发执行错误时的最小 Gas</p></td>
</tr>
<tr data-local-id="2082f34a-0953-4266-a612-338b814c7db4">
<td class="confluenceTd" data-local-id="367656ae-5a0f-42dd-8dff-e60429c86432"><p>minAdditionalGasForExecution</p></td>
<td class="confluenceTd" data-local-id="0ef8536a-7f11-4aab-9438-509f8f77bd29"><p>  token 精度</p></td>
<td class="confluenceTd" data-local-id="3810bcd9-2212-4bee-bc97-bb54746f17b4"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="1199b507-982c-4702-874d-fbd08c3642bd"><p>额外执行所需的最小 Gas</p></td>
</tr>
<tr data-local-id="8c781b26-ae16-4934-9c12-2c4563850751">
<td class="confluenceTd" data-local-id="4c7f9c9b-deef-4b0f-a74f-0de77606e0b6"><p>refundExecutionFeeGasLimit</p></td>
<td class="confluenceTd" data-local-id="c44d463f-2d3c-423e-9e8b-8033f59d7bbd"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="97e6c815-f899-43eb-a27d-9aa2820e67d2"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="55edf129-8cd0-49f4-8af3-30bba77fad3e"><p>退款执行费的 Gas 限额</p></td>
</tr>
<tr data-local-id="34ba45c0-1f81-4702-be86-2cd07d3ab40a">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="49ad1384-c2bf-4279-a574-1e5e499eda7a"><p>depositGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c2169193-41c5-4c55-8833-96d924c9a79f"><p>  token 精度</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8d738787-8353-479f-9601-ae9f1e7cf29f"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6d5fac98-b6f5-4469-819c-b9aea016a148"><p>存款操作 Gas 限额</p></td>
</tr>
<tr data-local-id="f1560787-d754-4d23-be96-6d0186ba581d">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0851870b-f78a-4a30-841e-0dc71f94ed62"><p>withdrawalGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5ff0285c-a6b7-495c-af6d-28e3328594bc"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0a93829f-af9e-43bb-ae1f-f79c25145840"><p>-</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="39466da2-92c4-4f18-ab98-00b6f93173a0"><p>提现操作 Gas 限额</p></td>
</tr>
<tr data-local-id="816f941f-c217-4f85-9876-682cf1d2e0a1">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d1d80640-0bc2-4a05-b448-21674a82ec3c"><p>shiftGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="a17fd075-006a-463d-881c-041a15bd61cf"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0277f13c-a41f-4697-9c50-13375cd7a134"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6c709fd2-3b26-41ab-8343-511e2c3bdd3d"><p>资产迁移/转移操作 Gas 限额</p></td>
</tr>
<tr data-local-id="b261dbfd-fd57-4dde-afb8-f7ef50b02de8">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="06146ca3-3dee-4fbc-a0f3-6d0f2c0cbbd3"><p>createDepositGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="475b5452-90ec-4cbd-9ea8-e83f2502fb18"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5e0ae23a-d73a-45a3-a0ff-038d664893fc"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="edfec2a6-03fc-44a0-b3b7-5d5c309ed2c0"><p>创建存款请求的 Gas 限额</p></td>
</tr>
<tr data-local-id="270b511e-3a6b-41b0-893a-fd75de259bee">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="fa43931f-185c-4bde-83a1-79e7df4fd5cd"><p>createGlvDepositGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="2fbae609-1478-4398-a20c-5dda57516cb9"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="dbb2ab4d-fcf8-47ec-8230-c9c81084b356"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="a2eaf9e4-ba2d-45f7-8b86-ad97aeae25eb"><p>创建 GLV 存款请求的 Gas 限额</p></td>
</tr>
<tr data-local-id="739a72eb-298e-4289-b618-5068511ba9b1">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9cfc613d-bb43-40e5-95ae-b53072c92fb5"><p>createWithdrawalGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="354ac181-ffdf-43a9-9b65-2d69ccf0215f"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d351644b-b2ce-4206-8be2-97857a56e275"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7e1cbc52-f58a-448a-943c-f4e91a1ad508"><p>创建提现请求的 Gas 限额</p></td>
</tr>
<tr data-local-id="f7da22c8-adc4-435e-a946-32eeec9260b4">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c46f36e3-9dd7-4d7e-88d4-93b41550520c"><p>createGlvWithdrawalGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9c3c1d4a-062b-4ad0-af40-1bac9cc52d8f"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="06936a5c-ef55-41ca-95bd-bd2259a99c2e"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6045341f-7fcd-4178-809e-5a90c22194c4"><p>创建 GLV 提现请求的 Gas 限额</p></td>
</tr>
<tr data-local-id="287021a3-8091-40a3-9c8f-c33491d9dccb">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e9cc58d5-bf8c-4db9-9831-ac9eb288695c"><p>singleSwapGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c4890834-838c-4082-a356-5a3dc1a48440"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4b470dec-8573-4a82-9453-9f6868560ee4"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="345d9309-dfe4-436a-b8ed-864ee0b95c6d"><p>单次交换操作 Gas 限额</p></td>
</tr>
<tr data-local-id="6c47997d-3a8a-48a0-a275-3fb10f6f2331">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8317313f-1505-4c7c-8d70-02ec011e1d5f"><p>increaseOrderGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="829e0343-2fb1-41bb-b14c-26a288559b09"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8e1f8f3d-7069-498d-802b-2a9644fde564"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9f15eb83-7e68-4d1a-84a9-a739eb3025fd"><p>增加仓位订单 Gas 限额</p></td>
</tr>
<tr data-local-id="247a1fc2-196c-4a1e-ac4c-9d581499e571">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="298943df-d318-457c-9ed8-9752b5f53638"><p>decreaseOrderGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="6b13807e-9913-43e1-a332-6a85f6193295"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="04fde75d-6be4-40ee-9292-ce168f3648ec"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8e87e4bf-185a-4ed5-af8c-d5466634167d"><p>减少仓位订单 Gas 限额</p></td>
</tr>
<tr data-local-id="b7b7f6f5-405f-4cec-bdfa-c2ab7a27fd38">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="1dd11608-a22f-4fa2-96bc-a83983c3a960"><p>swapOrderGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="a677ac44-36ab-4cb3-acc7-3a13cf1481e3"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0d173c90-6747-47d0-8b53-bd9981496953"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="b357e35b-9ea8-4502-b9c8-4919cbc30866"><p>交换订单 Gas 限额</p></td>
</tr>
<tr data-local-id="82c74ac6-c4cc-43a0-be14-f153cadc3246">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="567c5d2f-4a64-430e-9704-a05ee21a7f92"><p>glvPerMarketGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e1878a5d-89aa-49ae-a4c9-3fa028656e2b"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d2a1b29e-cd8d-4afa-a96c-a953e79e7d92"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="42c5c780-6baa-4f88-908e-e0347f4fd7f1"><p>每市场的 GLV 操作 Gas 限额</p></td>
</tr>
<tr data-local-id="3fa86be5-fdb8-498c-9378-666ca29e8270">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="5c699316-f991-4ef0-9d2b-ede5816eea05"><p>glvDepositGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4ff9aa06-a9ce-42b7-a4a6-f05a73f26f68"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="64d47c7a-4936-4269-9606-bfb6f9442bbb"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7831f3db-d52b-4dca-a5a7-c637e9be671a"><p>GLV 存款操作 Gas 限额</p></td>
</tr>
<tr data-local-id="b98e7d26-92c9-4cf8-a7f9-551ae8017ae3">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f0e3bc53-fc49-4866-99fb-cc85c4a92727"><p>glvWithdrawalGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e70b8fb3-7417-42c1-9689-115f03dbef35"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="bbb24f4d-d813-4471-9cb7-0e2aa964bb60"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="fdc9f29e-912d-43ef-a0fe-ea38f0b67821"><p>GLV 提现操作 Gas 限额</p></td>
</tr>
<tr data-local-id="bf67ab52-9642-4499-a252-8ea77c80a72c">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="8d22cb19-a20e-4399-a618-32dd8e23c084"><p>glvShiftGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="c66b4d0b-f3d1-4307-9923-c36762b83f32"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9d8fc94b-7c8d-44d5-a20e-bbd310073e37"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="0a16c0c6-24b3-4bd0-9c66-03e8717c3a79"><p>GLV 转移操作 Gas 限额</p></td>
</tr>
<tr data-local-id="432d4e5f-fcdc-42ac-8537-fbd2d07d59bc">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7ca2e98b-b55d-4f26-9554-5efd00ac00cb"><p>tokenTransferGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="e9b67fd3-d5dd-49c6-a164-12e42e3c8dd5"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="f23b4dda-5ca5-4bb5-97ed-fd5da795285c"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9f0874cb-5708-46d5-8a6e-4342762f8a80"><p>代币转账 Gas 限额</p></td>
</tr>
<tr data-local-id="dacfe96b-7783-4eb3-8108-5850882efd16">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="94a8a931-923f-4cb6-99f5-a5c5791d9370"><p>nativeTokenTransferGasLimit</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="4bdde4ea-9f1d-4cea-9814-6dc3c9b1bc54"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cca82e71-ab43-4642-85f4-6c4e1a55cb35"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9b0eb1f7-5278-4f93-941a-f0e5a99e7d58"><p>原生代币转账 Gas 限额</p></td>
</tr>
<tr data-local-id="12478812-6fe2-4047-8f2e-7d43014a9127">
<td class="confluenceTd" data-local-id="55188faa-a5d1-4704-82b9-fdaaa98cafb9"><p>estimatedGasFeeBaseAmount</p></td>
<td class="confluenceTd" data-local-id="e4e683ef-98bd-4a7f-828d-8dad0d1d10c7"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="0e0aee9c-2ac3-44a0-a742-14fd1e82ec7a"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="9b404b52-d024-41d5-b0fe-68645b225cba"><p>估算费用的基础 Gas 量</p></td>
</tr>
<tr data-local-id="5c90ab09-127a-4685-bf06-d9f49117bc02">
<td class="confluenceTd" data-local-id="286eeabb-60e7-4db5-8405-067eb314c095"><p>estimatedGasPerOraclePrice</p></td>
<td class="confluenceTd" data-local-id="1d4d014d-d6fe-4825-a5e8-1a1c55227428"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="da33d673-44c3-4dc0-acc5-d8324a800f4c"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="f0b88aa6-a875-4681-8010-99c2645bbd34"><p>每条预言机价格的估算 Gas</p></td>
</tr>
<tr data-local-id="e26197a5-71c8-44c2-9e82-cc462e4d2bfb">
<td class="confluenceTd" data-local-id="0859497e-9826-4afb-b5b8-b090834fa815"><p>estimatedGasFeeMultiplierFactor</p></td>
<td class="confluenceTd" data-local-id="e370022c-3cc7-437d-b256-5fadb89b5b6c"><p> 30</p></td>
<td class="confluenceTd" data-local-id="ccdcaf41-e0a5-4e05-a3a0-78c2f474fbeb"><p>1 = 1E30</p></td>
<td class="confluenceTd" data-local-id="46223d6c-5de3-494a-97f2-8ba9666a6b46"><p>估算费用的乘数因子</p></td>
</tr>
<tr data-local-id="94c652a0-129a-471a-8cf5-d76ce289031b">
<td class="confluenceTd" data-local-id="70f815ad-64da-4e19-b6de-58ff1ebc3938"><p>executionGasFeeBaseAmount</p></td>
<td class="confluenceTd" data-local-id="b92fdc54-ccb8-40f1-97b5-ca20bce3719d"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="0c460a46-4134-4678-9580-32bad8cd9f89"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="dec27ee2-0713-41ae-bbcb-9ced8b12551f"><p>实际执行费用的基础 Gas 量</p></td>
</tr>
<tr data-local-id="dcec3ec5-7978-4c4f-8e34-6f0a48987b81">
<td class="confluenceTd" data-local-id="c823197e-1f7a-40d8-bb66-df75d699e276"><p>executionGasPerOraclePrice</p></td>
<td class="confluenceTd" data-local-id="691df308-08e9-4dd6-b4cd-3a3732e213df"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="cf99cd40-3806-4348-88fb-1e37716291d4"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="d8a51c7b-0dad-41fb-95ac-f02a6cd7992e"><p>每条预言机价格的执行 Gas</p></td>
</tr>
<tr data-local-id="eacd3b93-7715-499a-bcd2-8d843a19379b">
<td class="confluenceTd" data-local-id="e7248083-d9f3-47d7-9a40-850d1753c585"><p>executionGasFeeMultiplierFactor</p></td>
<td class="confluenceTd" data-local-id="48e3db3d-c055-4838-a795-5e3f976e38c4"><p> 30</p></td>
<td class="confluenceTd" data-local-id="36aa287a-533f-404d-b5e9-182180386816"><p>1 = 1E30</p></td>
<td class="confluenceTd" data-local-id="98445c71-436f-4ee9-ada7-91cb98ca958d"><p>执行费用的乘数因子</p></td>
</tr>
<tr data-local-id="ce6e773e-0d15-4250-b2dc-1eea8dcade97">
<td class="confluenceTd" data-local-id="4eaea3a9-c997-45de-8f89-8d8c3d3e5e48"><p>requestExpirationTime</p></td>
<td class="confluenceTd" data-local-id="90f86e33-9df5-4800-a9ca-4501a9aad183"><p> 1</p></td>
<td class="confluenceTd" data-local-id="80e66e94-dd5b-4959-97ae-94cbde931396"><p>100s = 100</p></td>
<td class="confluenceTd" data-local-id="f431e369-9097-4691-9d33-c98c9d0343a7"><p>请求过期时间（秒）</p></td>
</tr>
<tr data-local-id="dc4aa71b-3880-4ed8-a1a3-20ef8a7d8981">
<td class="confluenceTd" data-local-id="f6be68af-ded8-47c9-a277-74578b2fea76"><p>maxSwapPathLength</p></td>
<td class="confluenceTd" data-local-id="be52442e-8d4f-43f3-9902-7e5d804e46dd"><p> 1</p></td>
<td class="confluenceTd" data-local-id="162dae90-33f1-4bc4-9510-7d49408df216"><p>11</p></td>
<td class="confluenceTd" data-local-id="b4ea3ccf-1e95-4d96-8468-5c220749b027"><p>最大交换路径长度</p></td>
</tr>
<tr data-local-id="201c02bd-f889-415e-8762-1ad7ab0356e6">
<td class="confluenceTd" data-local-id="eaf0e88e-c7da-425a-bde3-1993f01ed307"><p>maxCallbackGasLimit</p></td>
<td class="confluenceTd" data-local-id="49d1fed9-98ca-4f46-9f39-8d2cd7643a4a"><p> token 精度</p></td>
<td class="confluenceTd" data-local-id="8ce1b8e8-d313-4115-b7b4-477e17588171"><p>1 ETH = 1E18</p></td>
<td class="confluenceTd" data-local-id="a4ced885-d34f-4609-99b2-85e3b5365e2d"><p>回调最大 Gas 限额</p></td>
</tr>
<tr data-local-id="ecd6b83d-93f3-40a4-b7a9-57780be3c535">
<td class="confluenceTd" data-local-id="ef3e4a85-06fb-4263-b4b9-8c7d32937019"><p>minCollateralUsd</p></td>
<td class="confluenceTd" data-local-id="76d780c9-164d-41fc-a58a-734a1531e2d1"><p> 30</p></td>
<td class="confluenceTd" data-local-id="5e7cf2b3-78ea-4d1e-baef-461261375f39"><p>1 USD = 1E30</p></td>
<td class="confluenceTd" data-local-id="e9d4f1c2-a6c2-40f1-a0fd-695c8d8321fd"><p>最小抵押金额（USD）</p></td>
</tr>
<tr data-local-id="a641a630-a7b0-427b-a98c-e8c856ee852e">
<td class="confluenceTd" data-local-id="b2683354-5a5d-4660-a88d-23832aa29624"><p>minPositionSizeUsd</p></td>
<td class="confluenceTd" data-local-id="4bec02f2-8bb6-4d9e-a9ea-0e4e9e150ce2"><p> 30</p></td>
<td class="confluenceTd" data-local-id="d1a42a50-e0ad-4fee-aab0-f34cf30ce9c9"><p>1 USD = 1E30</p></td>
<td class="confluenceTd" data-local-id="018cd229-2e1f-489b-86f0-a02128500b70"><p>最小仓位规模（USD）</p></td>
</tr>
<tr data-local-id="5ce01478-9791-4829-8713-039d4e263d22">
<td class="confluenceTd" data-local-id="f7b2c0c1-ac71-41d9-9eb2-5843c40e9a5d"><p>claimableCollateralTimeDivisor</p></td>
<td class="confluenceTd" data-local-id="81545245-7c11-4db3-8339-9c811a919e24"><p> second</p></td>
<td class="confluenceTd" data-local-id="a51fc7ea-a2b3-40bd-ba19-7b886433df9f"><p>1s = 1</p></td>
<td class="confluenceTd" data-local-id="14c5988a-7afb-4c84-957c-9a9218943707"><p>可领取抵押的时间除数</p>
<p>每个 range 可以独立限制可提取的数量</p></td>
</tr>
<tr data-local-id="cb268cec-e160-4c0d-a944-4f5e0c964042">
<td class="confluenceTd" data-local-id="f2228534-a719-4f88-8350-365983364130"><p>claimableCollateralDelay</p></td>
<td class="confluenceTd" data-local-id="85814f31-8812-4ff1-a1fb-046537fbcf88"><p> second</p></td>
<td class="confluenceTd" data-local-id="cb6e4d9a-6acf-43c4-9bc5-d2006ed21819"><p>60s = 60</p></td>
<td class="confluenceTd" data-local-id="1478b2c3-4954-4be1-847a-53f8cc337e0a"><p>抵押可领取的延迟时间（秒），超过这个 delay 就认为 100%可提取</p></td>
</tr>
<tr data-local-id="0a990208-b394-4e5c-8f07-6550c752124c">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d15b2f3b-0317-405f-92f9-bf777888c05a"><p>positionFeeReceiverFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="7394c7aa-d3d1-4d6f-8221-16d8528e8fab"><p> 30</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="33d728a4-d14d-41c7-8e41-606dec6e02ea"><p>10%=1E29</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="58cd3e9f-2fac-4e26-a388-6f0ca9817224"><p>持仓费用分配比例</p></td>
</tr>
<tr data-local-id="c0624355-b187-4c26-9adc-e3a5f53b905e">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="571bb9bb-6c17-4d77-9d0d-9fbdb35598fc"><p>swapFeeReceiverFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="968aba18-d1bc-41ad-ab80-b0f5996a787c"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="96e04253-6b39-4c1f-b3f1-6dd5c78cdf46"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="710296b3-be0d-4429-a346-cbe6c41c04b2"><p>交换费用分配比例</p></td>
</tr>
<tr data-local-id="65514769-c749-4aea-aaaf-221c5fb61a3c">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="03a725ad-9c0d-4aae-96fe-8942702979a2"><p>borrowingFeeReceiverFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cb8764e0-a090-4bed-bc7b-905090b877e5"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="d15942d2-f5bf-493e-b4c2-5d59d571a147"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="34409186-5b15-4047-9cef-4337ecf946fc"><p>借贷费用分配比例</p></td>
</tr>
<tr data-local-id="de5af0ae-c677-460a-9eda-4c6a65412d0c">
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="3308cfe5-bc83-4074-8c97-b43aa434c9e9"><p>liquidationFeeReceiverFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="df54d65f-ba38-4a7d-8b91-00ad0d8fa1f1"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="9163162e-b5b4-4ffc-ac0b-14c129bc295d"></td>
<td class="confluenceTd" data-highlight-colour="#b3f5ff" data-local-id="cb287a86-4bfd-4a24-b5b7-3d92fb4bfa33"><p>清算费用分配比例</p></td>
</tr>
<tr data-local-id="c53b821a-5a0d-43df-9db2-a3c9f9260fb0">
<td class="confluenceTd" data-local-id="2a6c7201-98eb-4d34-991b-edf2ee4e34c7"><p>skipBorrowingFeeForSmallerSide</p></td>
<td class="confluenceTd" data-local-id="f345e208-518c-493e-a03f-bdade30dcf46"><p> bool</p></td>
<td class="confluenceTd" data-local-id="8411b977-24a9-4f4b-a210-80f0a555afea"><p>true</p></td>
<td class="confluenceTd" data-local-id="0e9119c2-11b0-4a07-b080-af5ce23c907e"><p>对较小侧免收借贷费开关</p></td>
</tr>
<tr data-local-id="edc92a8c-0df7-4ad8-b27f-30ce042bd301">
<td class="confluenceTd" data-local-id="f19afacc-eaef-45e0-a2f7-951191a5d40d"><p>maxExecutionFeeMultiplierFactor</p></td>
<td class="confluenceTd" data-local-id="2a20f358-12e2-4ea0-909e-46787ba92564"><p> 30</p></td>
<td class="confluenceTd" data-local-id="d8d4f780-087d-41d3-b5e8-50f3310b6f76"><p>1 = 1E30</p></td>
<td class="confluenceTd" data-local-id="5bac2ae3-2ebb-4f18-94bf-9d0595c5964c"><p>最大执行费乘数因子，一般就是 1</p></td>
</tr>
<tr data-local-id="bcada193-0b1d-46f8-9ca1-2fb3d4daa35f">
<td class="confluenceTd" data-local-id="1dc9c784-46ad-4168-bde2-d819dfbc7cb0"><p>oracleProviderMinChangeDelay</p></td>
<td class="confluenceTd" data-local-id="c96d9155-24f8-4a22-bed7-848652fee6fb"><p> seconds</p></td>
<td class="confluenceTd" data-local-id="fd95db29-a6f0-4ef4-ade8-f99d20f2fd09"><p>1s = 1</p></td>
<td class="confluenceTd" data-local-id="fa24b2ac-73eb-4345-b417-d78697662823"><p>预言机供应商最小变更延迟（秒），每次变更 token 的 provider 的间隔不能低于这个</p></td>
</tr>
<tr data-local-id="ee5ed24c-01c7-42bc-b16f-3903679768bc">
<td class="confluenceTd" data-local-id="fcaf94fe-518b-455f-b808-f70b34e47920"><p>configMaxPriceAge</p></td>
<td class="confluenceTd" data-local-id="87264616-9ca2-4f79-b368-3aef75c6f7f3"><p> second</p></td>
<td class="confluenceTd" data-local-id="83cdecc3-4b93-42b0-bfbc-e14676bdb281"><p>1s = 1</p></td>
<td class="confluenceTd" data-local-id="d6b0152c-c32e-4ce5-bf55-d514635c1301"><p>配置允许的最大价格年龄（秒）</p></td>
</tr>
<tr data-local-id="4543dccf-2a65-477f-a38a-37f450aaf568">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="ca1308bc-6f49-4a70-918e-4c869d89bb7e"><p>gelatoRelayFeeMultiplierFactor</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="751b1837-7dcb-4a25-8f3d-1e406bd7f66a"><p> 30</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="b30ca8b8-29ab-41e8-893b-40c0e9cbfc20"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="72bfe80b-beba-428d-ad68-47d52415e7fa"><p>Gelato 中继费用乘数因子，<span data-colorid="f8daqtt6hm">这个感觉先不需要考虑，是基于 gelato 代付用户的 gas fee 的优惠功能</span></p></td>
</tr>
<tr data-local-id="3b44acb4-1a15-4c5c-bdb9-65a830cd07b0">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="732e10be-5194-4a8e-b438-556d1545fd6b"><p>gelatoRelayFeeBaseAmount</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="6a43047c-41c1-40ac-92d9-3b6ab1dcf69f"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="69ecf95d-77fc-419c-8e7f-75d2d19bb1c0"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="68ea6381-c3d3-416e-8517-b9d668ce2d79"><p>Gelato 中继基础 Gas 量</p></td>
</tr>
<tr data-local-id="1ee0a45b-418e-4330-8e53-629d79064ddb">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="0c91ba5a-4de4-4231-bb01-fc929d9dc934"><p>relayFeeAddress</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="8080fb47-237b-45ce-becc-47c1bb8492a1"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="1e4493be-8968-4b70-8fe3-d7f3f2332ddd"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e7685917-c971-4405-a908-635ffaee930d"><p>中继费用接收地址</p></td>
</tr>
<tr data-local-id="21726662-606b-430a-9a5c-bc7b1ed5ed16">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="493e2ec7-bbeb-4d2a-92cc-46c35d0d1cb3"><p>maxRelayFeeUsdForSubaccount</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="26192374-8cea-4a6d-beba-a5f26d08272b"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e7737513-bbda-41d3-abe6-68e9e0046541"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="81f17429-dbf3-450e-9974-98a9e8e8224e"><p>子账户可用的中继费上限（USD）</p></td>
</tr>
<tr data-local-id="6ab0f6ea-8449-4280-9f5c-0376b0b7a03c">
<td class="confluenceTd" data-local-id="def00ec1-be3d-4c6f-9b1f-1e1c508e72ac"><p>maxDataLength</p></td>
<td class="confluenceTd" data-local-id="b392abdf-9fd4-46c4-9fee-757c8c6e44f7"><p> 1</p></td>
<td class="confluenceTd" data-local-id="2b4276dc-ce10-483c-adac-26e113c811fc"><p>10</p></td>
<td class="confluenceTd" data-local-id="f659e375-0357-45f4-bb05-f8cba3b88780"><p>最大数据长度</p></td>
</tr>
<tr data-local-id="b8a823e8-d798-432b-9edf-3f3c31c25807">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="4b01116b-9515-4baf-b088-4dbccc0e91ab"><p>multichainProviders</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e95e1cbe-38df-4bf2-ab91-d283de3b208b"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="a734c1b0-5cd0-4d22-b2c5-50d5de25b4cd"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e49ac25c-d7eb-4a14-81fa-d8b23395647e"><p>跨链提供者白名单（地址→是否启用）</p></td>
</tr>
<tr data-local-id="672f1466-5ab1-4909-bda8-ede6fe62cb52">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="913f5135-229c-4261-a1a7-658bd2997add"><p>multichainEndpoints</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="c0d4358a-0cfa-497d-92b7-03f75ed77f0b"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="7dcd74c6-1df0-4562-afb0-7709ef5d5165"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="03a548a4-92f4-4db3-b974-7cfc73cf3ebd"><p>跨链端点白名单（地址→是否启用）</p></td>
</tr>
<tr data-local-id="158046c8-7e80-4a32-8adf-de21870e0bd5">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="eb719f1b-16a0-4b3f-9a0f-14a004331d9b"><p>srcChainIds</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e124b1f3-0e04-4e57-9ce2-0482e897fefb"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="84b26537-b504-4f86-a5e0-4b31c081aecf"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="400a3811-c7a3-4250-9234-989dd255390e"><p>源链 ID 白名单（链 ID→是否启用）</p></td>
</tr>
<tr data-local-id="4663d31b-13f9-43d2-9f67-0b15e924c4c3">
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="e0872319-1145-41b2-aed8-638f041d13ab"><p>eids</p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="d4c506be-3a59-4cc8-8d5c-18b61b41d604"><p> </p></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="16c223ad-be91-48f2-a911-83f89d30b851"></td>
<td class="confluenceTd" data-highlight-colour="#fff0b3" data-local-id="c522ccc6-0a7b-471e-ae2c-04f8b0308d0e"><p>跨链端点编号映射（链 ID→端点 ID）</p></td>
</tr>
</tbody>
</table>

</div>

</div>
