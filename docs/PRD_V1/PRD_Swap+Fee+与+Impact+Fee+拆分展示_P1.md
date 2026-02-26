# PRD_Swap Fee 与 Impact Fee 拆分展示_P1

<div class="Section1">

## 背景

1.  当前问题：目前前端仅展示一个合并的 `swap fee`以及合并的`Lp fee`，实际两者都包含了 **Base Fee** 与 **Impact Fee**（Rebate/Tax）的计算结果。这会导致用户无法理解交易费用来源，且与行业竞品（GMX、Jupiter）不一致。

2.  目标：将两部分拆分并在前端的【交易面板swap fee费用明细】【平仓弹窗swap fee费用明细】【swap小窗swap fee费用明细】【HzLP 交易面板】展示，同时【swap 小窗新增\|c% - t%\| / t\
    % \<= 20%所涉及的输入框限制，仅前端】，提升透明度和用户信任度。

## 范围

### **In Scope**

- 前端 UI 调整：新增费用明细展示。

- SDK 接口/计算逻辑：区分 Base Fee 与 Impact Fee；swap max size根据\|c% - t%\| / t\
  % \<= 20%设限

- 合约确认逻辑：确保 SDK 获取的数据与链上 fee 计算结果一致。

### **Out of Scope**

- 当前仅针对池子权重变化有<a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees?utm_source=chatgpt.com#h_01K49EKS1AT92J7833Q61XY50B" class="external-link" rel="nofollow">linear price impact</a>，而OI Imbalance的<a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees?utm_source=chatgpt.com#h_01K49FQVFH1595HRYRYGCVJ1BK" class="external-link" rel="nofollow">exponential price impact</a>没考虑。

- 优化 LP 收费机制 - 当前与GMX存在差异。

## 功能需求

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="5a60fac9-ef03-40fd-b5d7-f41889b48e89">
<tbody>
<tr>
<td class="confluenceTd"><p><strong>需求</strong></p></td>
<td class="confluenceTd"><p><strong>功能项</strong></p></td>
<td class="confluenceTd"><p><strong>对应产品截图</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Swap 小窗</p>
<p>交易面板费用明细</p>
<p>平仓弹窗费用明细</p></td>
<td class="confluenceTd"><ol>
<li><p>【所有】新增swap fee与price impact分开展示 <em>(Fig1.1 - Fig1.3)</em></p>
<ol>
<li><p><strong>Swap Fee</strong> = （-1）*<code> Input Swap Size </code>* <code>swap_fee_bps</code></p></li>
<li><p><strong>Price Impact</strong> = （-1 ）* （<code>Fee_Amount</code> -<code> Swap Fee</code>)</p>
<ol>
<li><p><code>Fee_Amount</code>为原合约返还的计算后总值</p></li>
<li><p><code>Swap Fee </code>与 <code>Price Impact</code>为新增的前端计算</p></li>
<li><p><code>swap_fee_bps</code>取配置值<strong>「SwapFee」</strong>stable &amp; non stable swap那里</p></li>
<li><p>展示时正数展示加号 负数展示负号</p></li>
</ol></li>
</ol></li>
<li><p>【所有】新增price impact过高警示，放于按钮上方<br />
<em>(Fig2)</em></p>
<ol>
<li><p>若<code>price impact_nonstable</code> /<code> input swap size</code> &lt; <strong>-20bps</strong>, 按钮上方出提示：High Price Impact: [<code>swap impact_nonstable</code> / <code>input swap size</code> * <code>100%</code>]；点击关闭按钮提示消失，不记关闭按钮点击状态</p></li>
<li><p>若<code>swap impact_stable</code> / <code>input swap size</code> &lt; <strong>-2bps</strong>, 按钮上方出提示，同上</p></li>
</ol></li>
<li><p>【交易面板 &amp; Swap小窗】新增权重偏差超过20%的警示，放于按钮上方<br />
<em>（Fig2-3）</em></p>
<ol>
<li><p><strong>Swap 小窗</strong>：<br />
若：<br />
Swap所支付的注入流动性<code>X</code>（即<code>CoinIn_USD</code>）与Swap所得到的释放流动性<code>Y</code>（即<code>CoinOut_USD</code>）不满足下述关系：<br />
</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="60fbf340484e2a9329a95f628efea8925b8057c3615c578649ab445edaf37f91" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.21.05.png?version=1&amp;modificationDate=1758100876585&amp;cacheVersion=1&amp;api=v2" data-height="128" data-width="1096" data-unresolved-comment-count="0" data-linked-resource-id="3244094" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.21.05.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="16a55470-4d35-4176-8f38-1021ac18c44e" data-media-type="file" width="343" height="40" alt="Screenshot 2025-09-17 at 17.21.05.png" /></span></p>
<ol>
<li><p><strong>X</strong>：CoinInusd，即用户注入池子的资产美元价值。</p></li>
<li><p><strong>Y</strong>：CoinOutusd，即用户从池子换出的资产美元价值。</p></li>
<li><p><strong>t%ˉa</strong> = t%a * (1 + 20%) ；代表CoinIn 资产的目标权重<strong>上限</strong>，</p></li>
<li><p><strong>t%_a</strong> = t%a * (1 - 20%)</p>
<p>；CoinIn 目标权重<strong>下限</strong></p></li>
<li><p><strong>t%ˉb,t%_b：</strong>同理，对应 CoinOut（即池子释放的资产）的目标权重上下限。</p></li>
<li><p><strong>S_a =</strong> TVL * c%a；代表CoinIn资产在当前池子的规模（Pool Size，美元计）</p></li>
<li><p><strong>TVL_0</strong>：池子总资产规模（AUM，美元计）。</p></li>
</ol>
<p><br />
则：</p>
<ol>
<li><p>按钮上方出提示：High Swap Impact on Weightage<code> [权重偏差比]</code> [<code>取权重偏差比绝对值更大者；保留符号；计算公式如下</code>]；</p>
<p>点击关闭按钮提示消失，不记关闭按钮点击状态;</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b4d2c493cddcd4e13ce0b26eb817679f43e395a957314fa75d7262f775b26a67" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.04.27.png?version=1&amp;modificationDate=1758099873939&amp;cacheVersion=1&amp;api=v2" data-height="264" data-width="1000" data-unresolved-comment-count="0" data-linked-resource-id="3211373" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.04.27.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="3926288c-c2c0-4d9c-abda-8229602478f7" data-media-type="file" width="343" height="90" alt="Screenshot 2025-09-17 at 17.04.27.png" /></span></p>
<p><br />
举例来说：Impact_CoinIn=+12%；Impact_CoinOut = -25% → 最终展示 = <strong>-25%</strong> （因为 ∣−25%∣&gt;∣+12%∣，取前者，保留符号）</p></li>
<li><p>按钮disable并展示Max Swap Size: <code>Max{0, </code></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="60fbf340484e2a9329a95f628efea8925b8057c3615c578649ab445edaf37f91" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.21.05.png?version=1&amp;modificationDate=1758100876585&amp;cacheVersion=1&amp;api=v2" data-height="128" data-width="1096" data-unresolved-comment-count="0" data-linked-resource-id="3244094" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.21.05.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="16a55470-4d35-4176-8f38-1021ac18c44e" data-media-type="file" width="343" height="40" alt="Screenshot 2025-09-17 at 17.21.05.png" /></span></p>
<p><code>}</code></p></li>
</ol></li>
<li><p><strong>交易面板：Max Borrow Size已有逻辑可复用；提示文案中的swap impact变为borrow impact, 即：</strong></p>
<ol>
<li><p>若：<br />
开平仓所借贷的<code>borrow size</code>（即<code>Collaterla_USD * (Leverage - 1)</code>）</p>
<p><strong>大于</strong>下述公式算出的值：</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8950a7a2630499a91a1548a7e8625f6d1a978835b2fad1d56dffd86e1a9d5a7b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-18%20at%2011.22.43.png?version=1&amp;modificationDate=1758166008583&amp;cacheVersion=1&amp;api=v2" data-height="147" data-width="701" data-unresolved-comment-count="0" data-linked-resource-id="4096021" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-18 at 11.22.43.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="a1a33982-ea3f-4474-86c1-0e92d7f37cdc" data-media-type="file" width="300" height="62" alt="Screenshot 2025-09-18 at 11.22.43.png" /></span></p>
<p>则：</p>
<ol>
<li><p>按钮上方出提示：High Borrow Impact on Weightage<code> [权重偏差比；计算公式如下</code>]；</p>
<p>点击关闭按钮提示消失，不记关闭按钮点击状态;</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b4d2c493cddcd4e13ce0b26eb817679f43e395a957314fa75d7262f775b26a67" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.04.27.png?version=1&amp;modificationDate=1758099873939&amp;cacheVersion=1&amp;api=v2" data-height="264" data-width="1000" data-unresolved-comment-count="0" data-linked-resource-id="3211373" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.04.27.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="3926288c-c2c0-4d9c-abda-8229602478f7" data-media-type="file" width="343" height="90" alt="Screenshot 2025-09-17 at 17.04.27.png" /></span></p>
<p>举例来说：Impact_CoinIn=+12%；Impact_CoinOut = -25% → 最终展示 = <strong>-25%</strong> （因为 ∣−25%∣&gt;∣+12%∣，取前者，保留符号）</p></li>
<li><p>按钮disable并展示Max Swap Size: <code>Max{0, </code></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="60fbf340484e2a9329a95f628efea8925b8057c3615c578649ab445edaf37f91" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.21.05.png?version=1&amp;modificationDate=1758100876585&amp;cacheVersion=1&amp;api=v2" data-height="128" data-width="1096" data-unresolved-comment-count="0" data-linked-resource-id="3244094" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.21.05.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="16a55470-4d35-4176-8f38-1021ac18c44e" data-media-type="file" width="343" height="40" alt="Screenshot 2025-09-17 at 17.21.05.png" /></span></p>
<p><code>}</code></p></li>
</ol></li>
</ol></li>
</ol></li>
</ol></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ed145c160d982d99e0cb0e1b0d6d7978ae90b432d577bf3b942ce3358d912ce3" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/%20%20.png?version=1&amp;modificationDate=1758090042495&amp;cacheVersion=1&amp;api=v2" data-height="65" data-width="354" data-unresolved-comment-count="0" data-linked-resource-id="3178543" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="  .png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="9e6fa3ac-904b-49f2-bf3a-4a8dda796b23" data-media-type="file" width="229" height="42" alt=" .png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7a095ac31ae833a6d4076fbab61e9d6e06da6bb2f55192f663d1d3a773ef3cdf" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2010.16.24.png?version=2&amp;modificationDate=1758089992672&amp;cacheVersion=1&amp;api=v2" data-height="106" data-width="285" data-unresolved-comment-count="0" data-linked-resource-id="3178526" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 10.16.24.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="7bce5ec5-3a7f-4b9b-ba53-fd1e183cd73d" data-media-type="file" width="228" height="84" alt="Screenshot 2025-09-17 at 10.16.24.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5b6f43149ffcc74ecf6d7a75bc225e002517cabb0d18fdbaaf5eb84df9c1c169" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2010.13.48.png?version=3&amp;modificationDate=1758090105621&amp;cacheVersion=1&amp;api=v2" data-height="76" data-width="365" data-unresolved-comment-count="0" data-linked-resource-id="3244047" data-linked-resource-version="3" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 10.13.48.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="2d1425c0-e8d5-4976-83c4-c6e22f596cf2" data-media-type="file" width="228" height="47" alt="Screenshot 2025-09-17 at 10.13.48.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0ed256c991251a19f2690b177c48a19b0bf3db47a51cd14a5c4fd8fdc52a0f62" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2015.12.19.png?version=1&amp;modificationDate=1758095462445&amp;cacheVersion=1&amp;api=v2" data-height="615" data-width="429" data-unresolved-comment-count="0" data-linked-resource-id="3276833" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 15.12.19.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="6f77f563-26e6-4b23-a845-80976c76df70" data-media-type="file" width="237" height="340" alt="Screenshot 2025-09-17 at 15.12.19.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9000118107bf074aba637efcaf8f08f6a3a37c2b10cbadc88eff468a4cb3ce0a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.19.42.png?version=1&amp;modificationDate=1758100790176&amp;cacheVersion=1&amp;api=v2" data-height="614" data-width="469" data-unresolved-comment-count="0" data-linked-resource-id="3211384" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.19.42.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="a2964b4b-66f7-401d-8877-2940d8cbfc0b" data-media-type="file" width="319" height="417" alt="Screenshot 2025-09-17 at 17.19.42.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>HzLP交易面板费用明细</p>
<p>save on fees样式&amp;逻辑修改</p></td>
<td class="confluenceTd"><p>LP Fee 和上面的 swap 的算法是一样的，只是 base_bps 使用的另一个配置值 当前取值是30bps<strong>「AddRemoveFee」</strong>，警告阈值变为<strong>5bps</strong>；tax还是同一个，可复用已有计算逻辑，只不过公式改成<strong>原Token数量 ↔︎ 现USD 数量</strong>。即：</p>
<ol>
<li><p>Fees展示与计算：<em>（Fig1）</em></p>
<ol>
<li><p>Fees原字段 → Price Impact/LP Fee Rate</p></li>
<li><p><strong>LP Fee Rate</strong> = （-1）*<code>add_remove_fee_bps</code></p></li>
<li><p><strong>Price Impact Rate</strong> = （-1 ）* （<code>Fee_Amount</code> -<code> LP Fee</code>) /</p>
<p><code> Input Deposit或Withdraw Size_usd</code></p>
<ol>
<li><p><code>Fee_Amount</code>为原合约返还的计算后总值</p></li>
<li><p><code>LP Fee </code>与 <code>Price Impact</code>为新增的前端计算</p></li>
<li><p><code>base_bps</code>取配置<strong>「AddRemoveFee」而不是「Swap」这里记得区分nonstable与stable</strong></p></li>
<li><p>展示时正数展示加号 负数展示符号</p></li>
</ol></li>
</ol></li>
<li><p>新增Price Impact过高；以及权重偏差比过高警示，放于按钮上方 <em>（Fig1）</em></p>
<ol>
<li><p>若<code>price impact_usd</code> /<code>deposit或withdraw size_usd</code> &lt; <strong>-5bps</strong>, 按钮上方出提示：High Price Impact: [<code>price impact_usd</code> / <code>deposit或withdraw size_usd</code> * <code>100%</code>]；点击关闭按钮提示消失，不记关闭按钮点击状态</p></li>
<li><p><br />
<strong>若Price Impact &lt; 0 且</strong> 购买HzLP所支付的注入流动性<code>Deposit_USD</code>（即<code>CoinIn_USD</code>）或者卖出HzLP所得到的释放流动性<code>Withdraw_USD</code>（即<code>CoinOut_USD</code>）超出下述公式中的<code>MaxDeposit或Withdraw_USD</code>：</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="622a43338dbdebaf8498c1bc04a50462d4ba2fd740d06f764fa700825cdd3d67" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2019.20.23.png?version=1&amp;modificationDate=1758108031435&amp;cacheVersion=1&amp;api=v2" data-height="318" data-width="1249" data-unresolved-comment-count="0" data-linked-resource-id="3211441" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 19.20.23.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="374d9ee4-8bf1-46ea-bd2e-4277e19f423f" data-media-type="file" width="324" height="82" alt="Screenshot 2025-09-17 at 19.20.23.png" /></span></p>
<ol>
<li><p>TVL：HzLP池子总流动性 = ΣPoolAmount_{Token}</p></li>
<li><p>c%_{token}：添加/移除流动性时，为所使用/所获得资产在LP池的当前权重</p></li>
<li><p>t%_{token}：添加/移除流动性时，为</p>
<p>所使用/所获得资产在LP池的目标权重</p></li>
<li><p>δ%_{token}：常量，前端先写死20%，代表 | (c% - t%) / t% | 这个变量的最大阈值，即可接受权重偏差百分比<br />
<br />
则：按钮上方出提示：High Swap Impact on Weightage<code> [权重偏差比；保留符号；计算公式如下</code>]：</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2dd37bef9560a12869c267a98950cac9c35646e5c63ae7ca60c001d46cbc3eec" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2019.13.08.png?version=2&amp;modificationDate=1758108877565&amp;cacheVersion=1&amp;api=v2" data-height="316" data-width="640" data-unresolved-comment-count="0" data-linked-resource-id="3276893" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 19.13.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="792c1414-34b7-439b-ab3a-20e72cf6b135" data-media-type="file" width="300" height="148" alt="Screenshot 2025-09-17 at 19.13.08.png" /></span></p>
<p>点击关闭按钮提示消失，不记关闭按钮点击状态;<br />
按钮disable并展示Max Deposit或Withdraw Size: <code>Max{0, </code></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9f2d07cbd0dc77cd090bcaa5e38e5e21ade82aa006f47c147ff38ade73f8bd32" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2017.50.31.png?version=2&amp;modificationDate=1758108064444&amp;cacheVersion=1&amp;api=v2" data-height="133" data-width="599" data-unresolved-comment-count="0" data-linked-resource-id="3211403" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 17.50.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="8508b3fb-66ef-4749-8a6c-a3363c1e0162" data-media-type="file" width="300" height="66" alt="Screenshot 2025-09-17 at 17.50.31.png" /></span></p>
<p><code>}</code></p></li>
</ol></li>
</ol></li>
<li><p>提示样式变换<em>（Fig2）</em></p>
<ol>
<li><p>鼠标hover费率展示tooltip明细：</p>
<p><strong>LP Fee</strong> = （-1）*<code> Deposit或Withdraw_usd </code>* <code>base_bps</code></p></li>
<li><p><strong>Price Impact</strong> = （-1 ）* （<code>Fee_Amount</code> -<code> LP Fee</code>)</p></li>
<li><p><u>Save ~23.23% on fees with SUI</u></p>
<p><strong>修改</strong>已有逻辑，文案变一下（<strong>修改部分标红</strong>）：</p>
<ol>
<li><p><strong>文案</strong>：<u>Save</u> <code>~[price difference]%</code> <u>on fees with</u> <code>[Token Name]</code>.</p>
<ol>
<li><p><code>[Token Name]</code> 取同InputSize内<code>费率最优</code>token；<br />
i. 若多个最优，则取添加/移除对池子平衡影响更小者，即：多个最优资产的<code>c%</code>与<code>t%</code>分别代入该公式算偏差比，选<strong>绝对值</strong>最小的资产为<code>[token name]</code></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="2dd37bef9560a12869c267a98950cac9c35646e5c63ae7ca60c001d46cbc3eec" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2019.13.08.png?version=2&amp;modificationDate=1758108877565&amp;cacheVersion=1&amp;api=v2" data-height="316" data-width="640" data-unresolved-comment-count="0" data-linked-resource-id="3276893" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 19.13.08.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="792c1414-34b7-439b-ab3a-20e72cf6b135" data-media-type="file" width="276" height="136" alt="Screenshot 2025-09-17 at 19.13.08.png" /></span></p>
<p><br />
ii.若无更优fee rate则不展示这部分。</p></li>
<li><p><strong>[price difference]%</strong> 为与最优token手续费相差比值 精确至2dp</p>
<ol>
<li><p>合约返还fee amount 不为0时: <strong></strong><br />
<strong>= (fee amount - 最优fee amount) / 最优fee amount</strong></p></li>
<li><p>合约返还fee amount为0: <strong>= 100%</strong></p></li>
</ol></li>
<li><p>点击<u>Save ~[price difference]% on fees with [Token Name]</u> 超链接交易面板添加流动性的coinlist变为所选token symbol，输入框自动填充<code>Input_{current token} = Input_{last token} * Price_{last token}/Price_{current token}</code>; 即同等美元价值下的token数量；移除流动性一样，点击超链接交易面板Receive的coinlist变为所选token symbol，输入框保留<code>Input_{HzLP}</code></p></li>
</ol></li>
</ol></li>
</ol></li>
</ol></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="88d47badebfd3f10570f937669ae163d23cac0f10556fe60d4a7684fa6b7643e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2018.40.16.png?version=1&amp;modificationDate=1758105623042&amp;cacheVersion=1&amp;api=v2" data-height="548" data-width="681" data-unresolved-comment-count="0" data-linked-resource-id="3244113" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 18.40.16.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="5b5d000d-4bf0-4c20-87e1-34c2af96fad0" data-media-type="file" width="186" height="149" alt="Screenshot 2025-09-17 at 18.40.16.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="169508cb2f2279073c99a1d9d242fb32d0576a03b0c111869419f2ce6b84cd7c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2490433/Screenshot%202025-09-17%20at%2018.39.06.png?version=1&amp;modificationDate=1758105555819&amp;cacheVersion=1&amp;api=v2" data-height="148" data-width="655" data-unresolved-comment-count="0" data-linked-resource-id="3244106" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-17 at 18.39.06.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2490433" data-linked-resource-container-version="14" data-media-id="5e9ebafa-cd97-4c63-af68-7b5034137e89" data-media-type="file" width="348" height="78" alt="Screenshot 2025-09-17 at 18.39.06.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

------------------------------------------------------------------------

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

下面这部分不涉及产研，只是帮助理解

</div>

</div>

## 基本计算逻辑

**逻辑：**

- `next_diff < init_diff` → Rebate（回扣，降低手续费，最低 0）。

- `next_diff ≥ init_diff` → Tax（惩罚，增加手续费，有封顶）。

### 1. Swap Fee 定义

- **Base Fee Rate (base_bps)**：每笔 swap 固定收取的基础费用。

  - 非稳定币：`swap_fee_bps = 30` (0.30%)

  - 稳定币：`stable_swap_fee_bps = 4` (0.04%)

### 2. Price Impact Fee Rate定义

- **Dynamic Impact Fee (Rebate/Tax,** `tax_bps`**)**：根据交易是否让池子更平衡而调整。

  - 非稳定币：`tax_bps = 150` (1.50%)

  - 稳定币：`stable_tax_bps = 20` (0.20%)

### 3. LP Fee Rate定义

### 4. LP Price Impact Fee Rate定义

### 3. 计算公式

- **Rebate 情况**：

  <div class="code panel pdl" style="border-width: 1px;">

  <div class="codeContent panelContent pdl">

  ``` syntaxhighlighter-pre
  rebate_bps = tax_bps * init_diff / t%
  final_fee_bps = max(0, base_bps - rebate_bps)
  （t% = 该资产在池子中目标权重; 奖励最大上限base_bps，即加和总fee amount永远不为正数）
  ```

  </div>

  </div>

- **Tax 情况**：

  <div class="code panel pdl" style="border-width: 1px;">

  <div class="codeContent panelContent pdl">

  ``` syntaxhighlighter-pre
  avg_diff = (init_diff + next_diff) / 2
  capped_diff = min(avg_diff, target_amount_usd)
  tax_bps_adj = tax_bps * capped_diff / t%
  final_fee_bps = base_bps + tax_bps_adj
    （惩罚最大上限为tax_bps）
  ```

  </div>

  </div>

## 产品文档改动(tax取值待确定)

### Non-tech

#### Swap Fee

Swaps between assets inside the Hertzflow LP (HzLP) pool incur a **dynamic swap fee** to protect liquidity providers (LPs) and to keep the pool weights aligned with their targets. Swaps apply two layers of fees:

- **Base Fee Rate (base_bps)** – a flat fee applied to every swap.

  - Non-stables: `swap_fee_bps = 30` (0.30%)

  - Stables: `stable_swap_fee_bps = 4` (0.04%)

- **Dynamic Impact Fee Rate (Rebate or Tax, tax_bps)** – adjusts depending on whether your swap moves the pool **toward** or **away from** the target weights. 

  - Non-stables: `tax_bps = 150` (1.5%)

  - Stables: `stable_swap_fee_bps = 20` (0.2%)

The **dynamic impact fee rate** is calculated as follows. The protocol measures the difference between the **current weightage** and the **target weightage**:

- **Initial Deviation (**`init_diff = ｜c% - t%｜`**)**\
  For instance, BTC target weight is 20%. If the pool currently holds only 15%, then `init_diff = 5%`.

- **Next Deviation (**`next_diff =｜c%‘ - t%‘｜`**)**\
  After your swap, the deviation is recalculated. For instance, if your swap pushes BTC weight to 28%, then `next_diff = 8%`.

Then the **dynamic impact fee** adjusts to reward behaviors that rebalances pool and :

- **If next_diff \< init_diff → Rebate**\
  Your swap brings the pool closer to balance. In this case, part of the fee is refunded. The rebate is capped so that the final fee never becomes negative.

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
FORMULA:
rebate_bps = tax_bps * init_diff / t%
final_fee_bps = max(0, base_bps - rebate_bps)
```

</div>

</div>

- **If next_diff ≥ init_diff → Tax**\
  Your swap makes the pool less balanced, so an extra tax is charged. If you help rebalance the pool, you get cheaper fees (rebate). If you push the pool further out of balance, you pay more (tax).

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
FORMULA:
avg_diff = (init_diff + next_diff) / 2
capped_diff = min(avg_diff, t%)
tax_bps_adj = tax_bps * capped_diff / t%
final_fee_bps = base_bps + tax_bps
The maximum loss is capped at (FEE_BPS_POWER - final_bps) / FEE_BPS_POWER.
```

</div>

</div>

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

**EXAMPLE：**

- BTC target = 20%.

- Pool initially has 0% BTC → `init_diff = 20%`.

- After swap, pool goes to 80% BTC → <span class="inline-comment-marker" ref="4bf543e4-f3b8-4704-991a-99bb0cf126b2">`next_diff = 60%`</span>.

- Average deviation = 40%.

`final_bps = base_bps + 1.5% * (20% / 20%) = 1.8%`

So the fee is **much higher** than the base fee — a strong penalty for unbalancing the pool.

</div>

</div>

#### LP Fee

Adding or removing liquidity (minting or burning HzLP) uses **the same weight-balance logic** as swaps. The final fee depends on whether the action moves pool weights toward or away from their targets.

- **Base Fee:** `add_remove_fee_bps = 30` (0.30%)

- **Deviation Threshold (δ%):** Each asset has a configured max deviation from its target weight:

<div class="table-wrap">

|       |                            |
|-------|----------------------------|
| Asset | δ% (Max Allowed Deviation) |
| BTC   | 20%                        |
| ETH   | 20%                        |
| SUI   | 20%                        |
| USDC  | 20%                        |

</div>

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

**EXAMPLE:** TVL = \$1,000,000; δ% = 20%; user tries to add \$150,000 ETH.

- Target weight of ETH = 40% → \$400,000

- Current weight of ETH = 30% → \$300,000

- New weight = (300,000 + 150,000) / 1,000,000 = 45%

- Target = 40%, deviation = (45% - 40%) / 40% = 12.5% (\< 20%) - rebate

- `rebate_bps = 1.5% * 10%/ 40%`

- `final_fee_bps = max(0, base_bps - rebate_bps) = 0%`

Fee = **\$0**

</div>

</div>

### Docs (gitbook)

#### Swap Fee

When you swap tokens inside the Hertzflow LP (HzLP) pool, you pay a **dynamic swap fee**.\
This fee protects liquidity providers (LPs) and keeps the pool healthy and balanced.

Every swap includes **two layers of fee rates**:

**Base Fee Rate**

A small flat fee applied to every trade:

- **Non-stable pairs** (e.g. BTC/ETH, SUI/USDC): **0.30%**

- **Stable pairs** (e.g. USDC/USDT): **0.04%**

**Impact Fee Rate (Rebate or Tax)**

This part changes depending on how your swap affects the balance of the pool:

- **If your trade helps rebalance the pool → Rebate**

  - You get part of the fee refunded.

  - Example: if the pool doesn’t have enough BTC and your swap adds BTC, your fees will be cheaper.

- **If your trade pushes the pool further out of balance → Tax**

  - You pay extra.

  - Example: if the pool already has too much BTC and your swap adds even more BTC, you’ll be charged more.

The adjustment is capped:

- **Maximum rebate**: capped to the value of base rate.

- **Maximum tax**: capped so you never lose more than the set limit.

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

For Example:

- BTC target weight = 20%

- Current BTC in pool = 0% (very low, underweight)

- After your swap, BTC goes up to 80% (way overweight)

➡️ Since your trade makes the imbalance worse, you pay:

- Base Fee = 0.30%

- Tax = +1.5%

- **Total Fee = 1.8%**

This is a **penalty for unbalancing the pool**.

</div>

</div>

#### LP Fee

When you **add or remove liquidity** (minting or burning HzLP), the system uses the same **weight-balance logic** as swaps. The fee depends on whether your action moves the pool closer to its **target weights** or pushes it further away.

**Deviation Threshold (δ%)**

Each asset has a configured **maximum allowed deviation** from its target weight.\
If the pool weight is pushed too far outside this bound, deposits/withdrawals may be restricted.

<div class="table-wrap">

|       |                            |
|-------|----------------------------|
| Asset | δ% (Max Allowed Deviation) |
| BTC   | 20%                        |
| ETH   | 20%                        |
| SUI   | 20%                        |
| USDC  | 20%                        |

</div>

**Base Fee**

A flat fee is charged on every liquidity action:

- **add_remove_fee_bps = 30** (0.30%)

**Impact Fee (Rebate or Tax)**

- **Rebate**: If your deposit/withdrawal **moves the pool closer** to its target allocation, you get a rebate (your fee is reduced).

- **Tax**: If your action **pushes the pool further away** from its targets, you pay extra (fee is increased).

- **Caps:**

  - Maximum rebate = capped at the value of the base fee.

  - Maximum tax = capped at the configured upper limit.

<div class="panel" style="background-color: #EAE6FF;border-color: #998DD9;border-width: 1px;">

<div class="panelContent" style="background-color: #EAE6FF;">

**EXAMPLE:** TVL = \$1,000,000; δ% = 20%; user tries to add \$150,000 ETH.

- Target weight of ETH = 40% → \$400,000

- Current weight of ETH = 30% → \$300,000

- New weight = (300,000 + 150,000) / 1,000,000 = 45%

- Target = 40%, deviation = 10% / 40% = 12.5% (\< 20%) - rebate

- `rebate_bps = 1.5% * 10% / 40%`

- `final_fee_bps = max(0, base_bps - rebate_bps) = 0%`

Fee = **\$0**

</div>

</div>

</div>
