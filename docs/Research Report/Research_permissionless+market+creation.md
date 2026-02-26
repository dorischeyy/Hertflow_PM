# Research_permissionless market creation

<div class="Section1">

# 参数梳理

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="8cfb626b-1201-4ef3-9abb-7acffdf9f655">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>模块</p></td>
<td class="confluenceTd"><p>数据字段</p></td>
<td class="confluenceTd"><p>定义 / 说明</p></td>
<td class="confluenceTd"><p>备注</p></td>
</tr>
<tr>
<td rowspan="3" class="confluenceTd"><p><strong>市场基础参数</strong></p></td>
<td class="confluenceTd"><p>Base Asset<br />
</p></td>
<td class="confluenceTd"><p>标的资产<br />
cryptos, memes, RWA tokens等</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Quote Asset</p></td>
<td class="confluenceTd"><p>计价资产<br />
USDC/USDT/其他稳定币</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Market Symbol</p></td>
<td class="confluenceTd"><p><code>Base Asset</code>/<code>Quote Asset</code><br />
比如 ETH/USDC</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Oracle</p></td>
<td class="confluenceTd"><p>需要确定：<br />
支持哪些 oracle／预言机<br />
on-chain 校验延迟 /最大偏差<br />
oracle 资金喂价频率要求</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td rowspan="2" class="confluenceTd"><p>交易行为参数</p></td>
<td class="confluenceTd"><p>Max Leverage</p></td>
<td class="confluenceTd"><p>开仓可用最大杠杆倍数</p></td>
<td class="confluenceTd"><p>Max Leverage ≤ 100 (当前产品前端设定限制，实际协议支持的浮动杠杆 ≤ 200）<br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>MMR</p></td>
<td class="confluenceTd"><p>维持保证金率，仓位保证金率低于MMR时会触发keeper强平<br />
= 1/Max Maintenance Leverage</p></td>
<td class="confluenceTd"><p>MMR ≥ 0.2% (协议设定值）<br />
</p></td>
</tr>
<tr>
<td rowspan="4" class="confluenceTd"><p><code>流动性池参数</code><br />
<strong>（假定不与HzLP共用流动性）</strong></p></td>
<td class="confluenceTd"><p>Collateral Tokens</p></td>
<td class="confluenceTd"><p>池子支持的抵押资产<br />
Stable Collaterals &amp; Non Stable Collaterals</p></td>
<td rowspan="4" class="confluenceTd"><p>这里也可以像<a href="https://docs.dydx.exchange/users-governance/functionalities#liquidity-tiers" class="external-link" rel="nofollow">DyDX</a> - 我们给出预设模版，用户去根据资产类别选择<br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Initial Liquidity Amount</p></td>
<td class="confluenceTd"><p>启动资金</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidity Cap</p></td>
<td class="confluenceTd"><p>硬上限 超出将不再支持添加新的流动性</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Target Weightage</p></td>
<td class="confluenceTd"><p>目标权重 <code>t%_{token}</code><br />
启动时Current Weightage <code>c%_{token}</code>初始值配成目标权重</p></td>
</tr>
<tr>
<td rowspan="4" class="confluenceTd"><p><code>费用</code><br />
<strong>（假定不与HzLP共用流动性）</strong></p></td>
<td class="confluenceTd"><p>Swap Fee Rate</p></td>
<td class="confluenceTd"><p>分为 stable swap rate 与 non stable swap rate</p></td>
<td class="confluenceTd"><p>floor &lt; 用户设置值 &lt;ceiling<br />
<em>协议确保数值处于合理范围</em></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Open Position Fee Rate</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>&lt; 协议设置的硬上限</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Close Position Fee Rate</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>&lt; 协议设置的硬上限</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidation Fee Rate</p></td>
<td class="confluenceTd"><p>补偿keeper以及L</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td rowspan="5" class="confluenceTd"><p><code>风控参数</code><br />
<strong>（最好与协议设定的机制绑定，而非用户自定义）</strong></p></td>
<td class="confluenceTd"><p>Max OI</p></td>
<td class="confluenceTd"><p>单个市场单边允许最大未平仓限制</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Skew Limit</p></td>
<td class="confluenceTd"><p>| OI_{Long} - OI_{Short} | / Total OI 可容许的最大偏差比值</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Position Size</p></td>
<td class="confluenceTd"><p>单个独立钱包地址下最大仓位大小</p></td>
<td class="confluenceTd"><p>e.g. Avantis的做法：&lt; 15% OI_{symbol}</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Limit Orders</p></td>
<td class="confluenceTd"><p>单个独立钱包地址下单市场open orders个数上限</p></td>
<td class="confluenceTd"><p>floor &lt; 用户设置值 &lt;ceiling （当前设定20）<br />
<em>协议确保数值处于合理范围</em></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Insurance Fund Size</p></td>
<td class="confluenceTd"><p>比如10% AUM用于cover bad deb</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td rowspan="2" class="confluenceTd"><p>权限</p></td>
<td class="confluenceTd"><p>Operator</p></td>
<td class="confluenceTd"><p>是否可更新已定参数，参数更新范围</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee Recipient</p></td>
<td class="confluenceTd"><p>手续分分成比例<br />
admin，LP，protocol</p></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

# 竞品调研

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="e8b98be2-29de-4a72-b31b-2159e779004d">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>协议</p></td>
<td class="confluenceTd"><p><strong>是否支持用户自行 Launch Market?</strong></p></td>
<td class="confluenceTd"><p><strong>机制/限制</strong></p></td>
<td class="confluenceTd"><p><strong>结论来源</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Perennial</strong><br />
</p>
<ul>
<li><p><strong>Arbitrum</strong></p></li>
<li><p>Hybrid Intent-AMM<br />
相当于clob + lp池兜底的三边市场</p></li>
</ul></td>
<td class="confluenceTd"><p>✅ <strong>完全 permissionless</strong></p></td>
<td class="confluenceTd"><p>任何人都能创建新市场，只要提供 <strong>oracle feed、Base/Quote</strong>，并设定 fee/leverage/funding 等参数。LP 也可 permissionless 提供流动性。<br />
</p>
<ul>
<li><p>市场基础参数：base/quote、oracle、payoff provider</p></li>
<li><p>交易行为参数：可设 <strong>fees、fundingInterval、settlementFee</strong> 等，协议设 max 上限。</p></li>
<li><p>流动性启动：<strong>virtualTaker</strong> 缓冲，市场 operator 可自带初始 LP</p></li>
<li><p>费用参数：可设多类 fee（fundingFee、interestFee、positionFee、settlementFee, liquidation fee），但受 maxFee 限制。</p></li>
<li><p>风控参数：risk coordinator/operator 有权限管控，协议 enforce <strong>maxFee、skew limits</strong>。</p></li>
<li><p>权限：每个市场有独立 <strong>operator</strong> 以及<strong>risk coordinator</strong>( multisig+timelock)</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.perennial.finance/building-on-perennial/guides/creating-a-new-market" class="external-link" rel="nofollow">Docs – Creating a New Market</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>dYdX v4</strong><br />
</p>
<ul>
<li><p><strong>基于Cosmos的自建AppCahin</strong></p></li>
<li></li>
</ul></td>
<td class="confluenceTd"><p>❌ 半自动<strong>permissionless</strong></p></td>
<td class="confluenceTd"><p>新市场必须通过 <strong>治理提案 (Proposal)</strong>，需提供 <strong>Base/Quote、oracle、IMR/MMR、funding params</strong>。市场由 LP 提供流动性，但创建权不对用户开放。<br />
</p>
<ul>
<li><p>市场基础参数：base/quote、oracle、reference price（oracle要求通过特定校验）</p></li>
<li><p>交易行为参数：可设<strong>IMR</strong>、<strong>max lev</strong>、<strong>fees、impact notional</strong>等，协议设 max 上限。</p></li>
<li><p>流动性启动：<strong>预设模版，可选liquidity tier</strong></p></li>
<li><p>费用参数：funding fee、funding interval可通过proposal提议，其余走预设模版。</p></li>
<li><p>风控参数：根据liquidity tier自动计算，不可更改</p></li>
<li><p>权限：需lock治理代币 &amp; 等批准</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.dydx.exchange/users-governance/proposing_a_new_market" class="external-link" rel="nofollow">dYdX Docs – Proposing a New Market</a><br />
</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8e8f005a9fd9f7f2617ffd47f627a50dd19cd64c01eccf5a10b6a56b08494337" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/21463088/Screenshot%202025-09-12%20at%2014.28.31.png?version=1&amp;modificationDate=1761028538147&amp;cacheVersion=1&amp;api=v2" data-height="1690" data-width="842" data-unresolved-comment-count="0" data-linked-resource-id="21364817" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-12 at 14.28.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="21463088" data-linked-resource-container-version="1" data-media-id="1513a6ca-595f-45af-a411-af194269e726" data-media-type="file" width="173" height="346" alt="Screenshot 2025-09-12 at 14.28.31.png" /></span></td>
</tr>
</tbody>
</table>

</div>

</div>
