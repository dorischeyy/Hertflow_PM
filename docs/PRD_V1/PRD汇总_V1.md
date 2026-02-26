# PRD汇总_V1

<div class="Section1">

## 需求

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a9ddba38-6dca-493a-ae8b-153b1e94debc">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>功能实现</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>文档链接</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>官网</p></td>
<td class="confluenceTd"><p><a href="https://www.figma.com/design/WDFgkuyX7PmBUKyjJEPdmB/Untitled?node-id=96-2748&amp;t=ZwyZwKyMRNK9iz2T-4" class="external-link" rel="nofollow">官网优化_P0</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Portfolio_V1</p>
<blockquote>
<p>顶部导航栏</p>
</blockquote>
<ul>
<li><p><strong>「Portfolio」</strong>钱包操作（切换；连接；断开）；钱包余额展示；交易历史记录；HzLP流动性历史记录</p></li>
<li><p><strong>「Settings」</strong>主题色；onboard弹窗展示/隐藏；切换网络；切换/自定义rpc</p></li>
<li><p><strong>「钱包连接」</strong>测试网阶段H5仅展示Slush；PC Slush + Suiet。(原因：okx不支持testnet；Suiet无手机端应用，且不支持H5浏览器插件添加)</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F090ZJ311PG" class="external-link" rel="nofollow">钱包连接功能&amp;个人中心</a><br />
<a href="https://hertzflow.slack.com/docs/T08G35AED17/F098FP8125T" class="external-link" rel="nofollow">PRD_Settings_P1</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Trade_V1</p>
<ul>
<li><p><strong>「Onboarding」</strong>Disclaimer + 引导弹窗</p></li>
<li><p><strong>「交易面板」</strong>市价单（multi-collateral borrow），限价单。</p></li>
<li><p><strong>「历史记录」</strong>持仓、限价、交易的历史记录展示；k线标记；以及过滤筛选功能。其中历史记录包括开平仓，保证金修改，清算记录。功能包含平仓，保证金修改，限价单修改，分享pnl，一键全平及一键取消。</p></li>
<li><p><strong>「费用结构」</strong>Open/Close Fee + Swap + 线性Price Impact + Borrow Fee；MMR&lt;0.2%时收取Liquidation Fee并将剩余保证金返还用户</p></li>
<li><p><strong>「风控机制」</strong>Max OI；Max Position Size；Swap对应的权重偏差比值限制；剩余流动性判断；Open Order数量限制。</p></li>
</ul></td>
<td class="confluenceTd"><p>「Onboarding」</p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F09A65J3138" class="external-link" rel="nofollow">PRD_风险提示</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F09ABEFLHED" class="external-link" rel="nofollow">PRD - 首次引导弹窗（P2）</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F098D3K2207" class="external-link" rel="nofollow">PRD_测试网faucet领取入口（P2）</a></p>
<p>「交易面板」<br />
<a href="https://hertzflow.slack.com/docs/T08G35AED17/F08MGBFDD50" class="external-link" rel="nofollow">交易面板产品文档</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F08QYU18W0H" class="external-link" rel="nofollow">市场选择&amp;订单区</a></p>
<p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2490433/PRD_Swap+Fee+Impact+Fee+_P1?atlOrigin=eyJpIjoiOGZiMTYyMjM1NDdjNDMzNDhiNzNiMDQ3MTVjZTg4NWIiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/2490433/PRD_Swap+Fee+Impact+Fee+_P1?atlOrigin=eyJpIjoiOGZiMTYyMjM1NDdjNDMzNDhiNzNiMDQ3MTVjZTg4NWIiLCJwIjoiYyJ9</a></p>
<p>「历史记录」</p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F09BQTKNFMX" class="external-link" rel="nofollow">PRD_K线图功能优化_P2</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F098W0BN8Q6" class="external-link" rel="nofollow">PRD_交易列表增加排序与筛选功能_Aug05_P2</a><br />
<a href="https://www.figma.com/design/AmguvHz2zBT9YzQgH9AVB8/HertzFlow?node-id=2582-28668&amp;t=Idif13lp572exnuK-4" class="external-link" rel="nofollow">设计稿</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F099SBFGY69" class="external-link" rel="nofollow">receive in优化+activity优化</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F09A4RGRHN1" class="external-link" rel="nofollow">PRD_改单&amp;流动性面板增加修改滑点功能</a></p>
<p><a href="https://www.figma.com/design/AmguvHz2zBT9YzQgH9AVB8/HertzFlow?node-id=3134-45" class="external-link" rel="nofollow">Share</a></p>
<p>「其他」</p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F09AV6VTP46" class="external-link" rel="nofollow">PRD_toast提示</a></p>
<p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F0998L67DRP" class="external-link" rel="nofollow">404页面规范</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>HzLP_V1</p>
<blockquote>
<p>单一多资产流动池</p>
</blockquote>
<ul>
<li><p><strong>「交易面板」</strong>添加/移除流动性；滑点设置</p></li>
<li><p><strong>「费用结构」</strong> Base Fee + 线性 Price Impact</p></li>
<li><p><strong>「数据展示」</strong>TVL；Supply；Price；APY；Pool Composition；Utilization；APR</p></li>
<li><p><strong>「风控机制」</strong></p>
<ul>
<li><p><strong>前端限制：</strong>权重偏差比超过20% → 不可添加/移除</p></li>
<li><p><strong>合约限制：（测试网阶段）</strong>maxAUM 超过$500k → revert</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/19398688/PRD_HzLP_V1?atlOrigin=eyJpIjoiYzA2MDhmMzkxNjg4NDI1MWJkYmUyYmYwZmU4Yjc0MTgiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/19398688/PRD_HzLP_V1?atlOrigin=eyJpIjoiYzA2MDhmMzkxNjg4NDI1MWJkYmUyYmYwZmU4Yjc0MTgiLCJwIjoiYyJ9</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Dashboard_V1</p></td>
<td class="confluenceTd"><p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F08TQV03UBH" class="external-link" rel="nofollow">Dashboard</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>H5</p></td>
<td class="confluenceTd"><p><a href="https://www.figma.com/design/AmguvHz2zBT9YzQgH9AVB8/HertzFlow?node-id=3713-8112" class="external-link" rel="nofollow">H5</a></p></td>
</tr>
</tbody>
</table>

</div>

## 2. 相关文档

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="0f3b0eac-7cc8-4716-b73c-e8c8a3f7fe28">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>文档</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>Last Update</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/10518529?atlOrigin=eyJpIjoiYzk2NzA2NDc5MmY3NDgzZGFhNzcyODRjM2ZkOTQ4NTYiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/10518529?atlOrigin=eyJpIjoiYzk2NzA2NDc5MmY3NDgzZGFhNzcyODRjM2ZkOTQ4NTYiLCJwIjoiYyJ9</a></p></td>
<td class="confluenceTd"><p>每周一更新并同步产品群</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/embed/4063267?atlOrigin=eyJpIjoiZmY4YWIyMmU1MDE3NGIwZGExYzkxMGNiZGFiMDM1M2YiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/embed/4063267?atlOrigin=eyJpIjoiZmY4YWIyMmU1MDE3NGIwZGExYzkxMGNiZGFiMDM1M2YiLCJwIjoiYyJ9</a></p></td>
<td class="confluenceTd"><p>页面链接</p>
<p>参数配置</p>
<p>埋点（前后端 整理中）</p>
<p>全局公式</p>
<p>Error Mapping （语义化toast整理中）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/x/tIAoAQ" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/x/tIAoAQ</a></p></td>
<td class="confluenceTd"><ul>
<li><p>22 August 更正：PnL这类仍为+$0.00 -$0.00 颜色区分 不用&lt;$0.01展示</p></li>
</ul>
<p>26 August 更新币本位价格展示规范：</p>
<ol>
<li><p>BTC 6dp 特殊处理：&lt;0.000001BTC ；ETH HzLP SUI 4dp USDC 2dp</p></li>
<li><p>小额隐藏：<code>&lt;0.000001 BTC</code>； <code>&lt;0.0001 ETH</code>；<code>&lt;0.01 SUI/HzLP</code></p></li>
<li><p>特殊处理：稳定币，按美元视觉习惯展示：<code>2dp</code> e.g. 1.12 USDC</p></li>
<li><p>若后续添加资产，价格10k - 100k按BTC来；价格1k- 10k的按ETH；价格1-1k的按SUI；meme相关的直接2dp</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457917/Docs?atlOrigin=eyJpIjoiNmQ1MmJiMTc0ZWFhNGVmZTgwNmNkMWFjMzUwMTNmY2MiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457917/Docs?atlOrigin=eyJpIjoiNmQ1MmJiMTc0ZWFhNGVmZTgwNmNkMWFjMzUwMTNmY2MiLCJwIjoiYyJ9</a></p>
<p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/19365953/Non-tech+Docs?atlOrigin=eyJpIjoiOGUzZDE2Y2E5NzdhNGQ2ZTg0MDFiZTA5Mjc0MmFhY2QiLCJwIjoiYyJ9" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/19365953/Non-tech+Docs?atlOrigin=eyJpIjoiOGUzZDE2Y2E5NzdhNGQ2ZTg0MDFiZTA5Mjc0MmFhY2QiLCJwIjoiYyJ9</a></p></td>
<td class="confluenceTd"><p>Gitbook 产品文档 （包括tech for dev）<br />
Google Doc 技术说明文档 （<strong>non</strong>-tech for dev）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F097W3YGJ4V" class="external-link" rel="nofollow">多语言文档</a></p></td>
<td class="confluenceTd"><p><code>Aug01 暂仅支持英文</code><br />
上周prd新文案待同步 <a href="https://hertzflow.slack.com/team/U09837G5FB3" class="external-link" rel="nofollow">@cen</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.slack.com/docs/T08G35AED17/F092B7LPJUX" class="external-link" rel="nofollow">api接口文档</a></p></td>
<td class="confluenceTd"><p>新接口需求同步 <a href="https://hertzflow.slack.com/team/U09837G5FB3" class="external-link" rel="nofollow">@cen</a></p></td>
</tr>
</tbody>
</table>

</div>

</div>
