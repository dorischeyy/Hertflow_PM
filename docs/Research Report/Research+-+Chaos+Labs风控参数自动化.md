# Research - Chaos Labs风控参数自动化

<div class="Section1">

<div class="confluence-information-macro confluence-information-macro-information">

<style>[data-colorid=p2132iyc2i]{color:#bf2600} html[data-color-mode=dark] [data-colorid=p2132iyc2i]{color:#ff6640}[data-colorid=uuqj8vt20g]{color:#bf2600} html[data-color-mode=dark] [data-colorid=uuqj8vt20g]{color:#ff6640}[data-colorid=p8e9ipf42j]{color:#bf2600} html[data-color-mode=dark] [data-colorid=p8e9ipf42j]{color:#ff6640}</style><span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**调研人：**<a href="https://hertzflow.atlassian.net/wiki/people/712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:d48dd58c-bb1b-4c50-94db-2cabaaa6b6a3" target="_blank" data-linked-resource-id="360623" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">novax 0x</a>

**调研背景：**

1.  <a href="https://chaoslabs.xyz/posts/gmx-v2-risk-portal-product-launch" class="external-link" rel="nofollow">GMX</a>跟<a href="https://chaoslabs.xyz/posts/chaos-labs-partners-with-jupiter-protocol" class="external-link" rel="nofollow">Jupite</a>r还有<a href="https://chaoslabs.xyz/posts/chaos-labs-partners-with-avantis#e16611c70c2a" class="external-link" rel="nofollow">avantis</a>都跟chaoslabs有不同程度的合作（其中GMX&JUP接了risk oracle，AVNT的话是参与了risk para的风控参数评估与推荐）

2.  流程：<a href="https://docs.chaoslabs.xyz/integration-guides/risk-integration/overview" class="external-link" rel="nofollow">Risk Oracle → Keeper → Config Updates</a>； <a href="https://github.com/ChaosLabsInc/chaos-agents" class="external-link" rel="nofollow">github相关链接1</a>； <a href="https://github.com/ChaosLabsInc/chaos-agents-factory" class="external-link" rel="nofollow">链接2</a>

3.  责任：负责参数根据市场响应自动化更新。即动态更新funding，max OI，tvl cap等市场/池子/vaults的风控参数。<a href="https://community.chaoslabs.xyz/gmx-v2-arbitrum/risk/markets" class="external-link" rel="nofollow">可视化dashboard</a>；<a href="https://community.chaoslabs.xyz/gmx-v2-arbitrum/risk/alerts" class="external-link" rel="nofollow">风险监控&amp;实时推送</a>

**结论：**

1.  Chaos Labs 的 Risk Oracle 并不是通用型 SaaS，而是Chaos Labs量化团队根据合作方体量针对性的 **链下模拟 + 链上推荐值** 的系统。

2.  Chaos Labs 本身不会改动我们的合约，也不会理解我们所有内部逻辑。他们只负责在链上写入“推荐参数值”；是否采用、如何验证、何时生效，都需要我们在协议层自行实现。

3.  HertzFlow必须构建自己的 Oracle 读取逻辑、Keeper 执行模块、挑战窗口机制，以及参数有效性验证流程。

</div>

</div>

# 合作模式选择

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="78d1bcad-4994-4890-ac8e-68b01d22a7ec">
<tbody>
<tr>
<th class="confluenceTh"><p>方案</p></th>
<th class="confluenceTh"><p>能力</p></th>
<th class="confluenceTh"><p>成本</p></th>
<th class="confluenceTh"><p>适用性</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>一次性初始风险框架（Avantis 用的）</strong></p></td>
<td class="confluenceTd"><p>初始参数建议，无自动化</p></td>
<td class="confluenceTd"><p>中</p></td>
<td class="confluenceTd"><p><strong>适用测试网</strong></p>
<p>快速起步，但后续要自己调</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>全自动 Risk Oracle（GMX 用的）</strong></p></td>
<td class="confluenceTd"><p>自动推荐 + 持续更新</p>
<ul>
<li><p><strong>已实现：</strong>只有两部分已经自动化<strong>Long/Short OI Cap</strong> 和 <strong>Dynamic Price Impact</strong>。</p></li>
<li><p><strong>计划中：</strong>根据 GMX 的治理提案，未来还会逐步开放<strong>Funding、Borrow、Vault 流动性分配等更多风险参数</strong>。</p></li>
</ul></td>
<td class="confluenceTd"><p><strong><span data-colorid="uuqj8vt20g">高</span></strong></p>
<ul>
<li><p>GMX 的合同费用约为 <strong>18,333 美元/月</strong></p></li>
<li><p>Aave 的合作金额接近 <strong>85 万美元</strong></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>一定规模后<span data-colorid="p2132iyc2i">【需上层决策具体体量】</span>适用主网</strong></p>
<p>最安全，但投入最大</p></td>
</tr>
</tbody>
</table>

</div>

1.  **可信度：**综合来看，Chaos Labs 当前是最成熟的 DeFi 风险建模与自动化参数管理服务商。可靠性方面，Chaos Labs 已经获得 GMX 社区的高度认可：GMX DAO 投票以 100% 支持其接入；他们也负责 GMX V2 启动时的 Genesis Risk Framework，并为 **Aave、Jupiter、Pendle、dYdX** 等多个大型协议提供建模服务。相较之下，Gauntlet 更偏向“写报告 + 提案”，自动化能力弱，是一种不同路线。

2.  **成本投入：**Chaos Labs 的价格体系较高。Chaos Labs 没有轻量订阅版，唯一低成本选择是一锤子买卖的“初始风险框架”咨询，只提供**初始参数**，不包含自动化更新和持续监控。如果我们希望长期使用动态 Risk Oracle，则成本需要充分考虑。

3.  **技术投入：**从当前代码仓库情况来看，我们暂时无法直接对接 Risk Oracle。现有仓库仅有配置占位，没有实际实现：缺少 Risk Oracle 读取逻辑、正式 Keeper 实现，以及参数挑战/确认机制。同时要理解 Chaos Labs 输出的参数含义，也需要团队具备完整的风险建模背景。总体估算，实现对接至少需要 **<span colorid="p8e9ipf42j">【产品确认合作方式后技术评估】 </span>周的工程量**。

# Q&A

### Q1：Risk Oracle 是通用产品吗？Chaos Labs 不懂我们合约怎么智能调参数？

**A1**\

- Risk Oracle 只是链上推荐引擎：Chaos Labs 在链下做模拟，写入推荐值；执行权在协议的 Keeper。Chaos Labs 不会直接改我们合约。

- 如果我们希望使用这些推荐值，就要自行编写读取 Risk Oracle 的合约或脚本、自主的 Keeper、以及挑战窗口逻辑。Chaos Labs 只提供推荐值、允许的调节范围和否决流程说明。

- Risk Oracle 的能力靠深入理解客户协议（例如 GMX V2 的 market config、impact 公式、资金费率模型），再由量化团队建模。不是一个套模板的通用 SaaS。

### Q2：GMX 只开放 OI Cap，Chaos Labs 还能管理哪些参数？

**A2**\

- 已经自动化的参数：Long/Short OI Cap、Dynamic Price Impact。截图里的 Recommended Value 对应这两类参数。

- 规划中的参数：GMX 治理提案写明会逐步开放 Funding、Borrow、Vault 流动性分配等。Chaos Labs 在 Aave 已经试运行类似的借贷上限、清算阈值、利率等参数。

### Q3：**我们能否直接照搬 Chaos Labs 给 GMX 的推荐值？**

**A3**\

- Chaos Labs 在 Public Risk Hub 公布推荐值，任何人都能查看。这些数值包含市场最大未平仓金额（OI Cap）、价格冲击系数等核心安全阈值。

- 不能照搬：Chaos Labs 给 GMX 的推荐值建立在 GMX 自有的流动性规模、手续费结构、清算深度、Keeper 响应速度以及风险参数之间的联动关系之上。我们的仓位规模、LP 资金池、订单执行流程与 GMX 并不相同，需要结合自己的流动性状况和清算模型重新设置。

- 还会带来社区形象风险：参数名或数值完全一致，容易被认为缺乏自主风控能力。

### Q4：Chaos Labs 的服务费用是多少？是否存在免费版？

**A4**\

- 持续服务价格高：GMX 付费约 18,333 美元/月，Aave 的合同金额约 850,000 美元。

- 没有轻量订阅版。唯一的低成本方案是一次性咨询（例如 Avantis 的创世风险框架），该方案只给初始参数，不包含持续更新与自动化。

- 公共仪表盘属于营销层的免费服务，真正适合协议的安全参数需要付费定制。

### Q5：与现有仓库对接需要多少工程量？

**A5**\

- 需要在合约或脚本里完成 Risk Oracle 读取功能。`contracts-v2/config/riskOracle.ts` 只有配置占位，没有实际读取逻辑。

- 需要构建 Keeper：在 `config/general.ts` 中配置执行 gas、挑战窗口等参数，并写 Keeper 执行代码。目前仓库缺乏正式 Keeper 实现。

- 需要团队理解每个参数的含义，才能判断 Chaos Labs 的推荐值是否符合本协议的风险边界。

### Q6：Chaos Labs 是否可靠？与 GMX 的合作深度如何？

**A6**\

- GMX DAO 在 2024 年 9 月发起的治理投票中，以 100% 的赞成票决定让 Chaos Labs 的 Risk Oracle 进入 GMX 协议。此前，Chaos Labs 已经为 GMX V2 写过风险规则总集（被 GMX 称作“Genesis Risk Framework”），这一步当时用于定义 GMX V2 启动时的初始参数。

- 当前双方合作范围包含两项自动化：最大未平仓头寸上限（Long/Short OI Cap）和价格冲击参数（Dynamic Price Impact）。在同一份治理说明里，GMX 表示下一阶段会把资金费率（Funding）和借币利率（Borrow）也交给 Chaos Labs 来计算推荐值。

- Chaos Labs 公开列出的付费客户还包括 Jupiter、Aave、dYdX、Pendle 等。Avantis 目前只付费购买了 Chaos Labs 的初始参数咨询服务，没有启用自动化更新。

- 主要竞争对手 Gauntlet 仍主要提供“写报告＋提交治理提案”的服务模式，缺乏直接的自动化推送。2024 年初 Aave 社区因为合作沟通问题解约了 Gauntlet，并由 Chaos Labs 接手部分风险建模工作。

评估 Gauntlet 等备选服务时，应重点比较自动化能力、响应速度和协同体验。

</div>
