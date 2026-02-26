# Research - Leaderboard & Referral 竞品机制调研

<div class="Section1">

### 设计目标 & 原则 <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-current">待确认</span>

> **目前处于 testnet 阶段**，因此激励机制要**轻量**（强反馈但轻奖励）、**敏捷**（框架方便后续mainnet扩展）、**低通胀**（投入产出比适量）、**可追踪（**观察用户行为）

1.  **目标行为**：交易 / 质押获取HzLP / 费用贡献 / 推荐 → 量化成 `Referral XP`（持续性）+ `Trading XP`（阶段性）

2.  **跨赛季切换 / 损耗**：赛季周期为？赛季结束时，测试网XP 如何处理？清零/badge / discord role / NFT？

3.  **防作弊 / 防刷机制**：设计门槛、频率限制、最小交易额、滑点 / 手续费考量等。（小额高频交易、刷单、频繁 deposit/withdraw 等）

4.  **奖励预算** ：每赛季设定一个固定奖励池（代币 / 奖品 /空投 /权益等），按积分比例分配；保证预算可控。重视新用户和老用户、公平性、边际回报曲线不要太极端。

5.  **阶梯 / 等级 / 加成机制**：

6.  **~~Testnet阶段设计原则：~~ 于Oct 15 收到上游优先级调整通知，这套机制主网再上，测试网阶段仅做数据上的测试**

    1.  **轻奖励**：不发币，以 XP、徽章、WL 替代。

    2.  **强反馈**：每周榜单与称号即时更新，提升参与感。

    3.  **快循环**：每月一赛季，测试不同激励参数。

    4.  **可追踪**：XP 与钱包绑定，形成“用户成长轨迹”，为未来主网分配提供可信数据。

    5.  **优化空间大**：不同赛季可调整权重、加成、奖励池等，使机制能灵活适配市场与用户行为。

    6.  **去中心**：XP 本身不可交易、不可转移、非代币，避免被滥用或套利。

### Hertzflow Testnet Voyage 机制

> - 设计目标： **收集高质量数据 + 建立用户习惯 + 建立pointfi系统基础**
>
> - 激励目标： **Trade + Swap + LP + Referral** 多维度参与
>
> - 奖励形式：不直接发代币，而是以 **现金池奖励**、**XP、Badge、Season榜单、未来空投Multiplier预留位** 的形式进行
>
> 参考 Avantis 的赛季结构、GMX 的返佣激励、Jupiter 的治理分层设计，融合为一套 **质量验证 + 行为分析 + 可快速上线 + 可后期延展** 的 XP 机制体系。

1.  **XP 基础机制**

<div class="table-wrap">

|  |  |  |  |  |
|----|----|----|----|----|
| 模块 | 行为 | 基础XP | 加权系数（w） | 备注 |
| Swap | 成功交易 1 笔 | 10 XP | w = log₁₀(成交额/5 USDC) | 小额交易权重低 |
| Perp | 开/平仓 1 次 | 20 XP | w = √持仓时长 × 收益率因子 | 长期持仓更高 |
| LP | 添加/移除流动性 | 15 XP | w = 持续天数/7 | 长期LP更优 |
| Referral | 新增1名有效推荐用户 | 25 XP | w = 被推荐人活跃度系数 | 参考 Avantis |
| Leaderboard | 排名前10/100 | +200 / +50 XP | 固定奖励 | 周榜激励 |

</div>

**公式示例：**

XP\_{user} = \sum_i (XP\_{base,i} × w_i × boost\_{season})

其中 boost 为赛季加成（默认1，活动期最高1.5）。

2.  **赛季结构**

<div class="table-wrap">

|  |  |
|----|----|
| 项目 | 内容 |
| **周期长度** | 4–6 周 / 赛季 |
| **赛季循环** | XP清零，保留“累计贡献值”用于长期声誉榜 |
| **奖池分配** | XP比例分配「测试激励（NFT徽章 / WL / mainnet XP Multiplier）」 |
| **层级奖励** | Tier 1–5，对应 XP 区间 |
| **赛季称号** | Explorer / Trader / Strategist / LP Master / Champion |

</div>

<div class="table-wrap">

|        |           |                         |
|--------|-----------|-------------------------|
| Tier   | XP门槛    | 奖励                    |
| Tier 1 | 0–200     | 参与徽章                |
| Tier 2 | 200–800   | XP Multiplier +1.1      |
| Tier 3 | 800–2000  | 限定NFT徽章 + WL资格    |
| Tier 4 | 2000–5000 | Beta邀请 / Partner role |
| Tier 5 | \>5000    | 核心用户称号 + 特殊奖励 |

</div>

3.  **推荐体系**

<div class="table-wrap">

|          |                                                         |
|----------|---------------------------------------------------------|
| 元素     | 机制设计                                                |
| 推荐关系 | 一级绑定（推荐人 + 被推荐人）                           |
| 奖励逻辑 | 推荐人获得被推荐人 XP 的 10%，被推荐人获得 +5% XP Boost |
| 限制条件 | 每人最多推荐 30 人；被推荐人需达 Tier 2 方为“有效”      |
| 排行榜   | 周榜前10可额外获得 +300 XP / WL 资格                    |

</div>

4.  **防刷机制与质量控制**

<div class="table-wrap">

|              |                               |
|--------------|-------------------------------|
| 策略         | 说明                          |
| 最小交易额   | 单笔 \<\$5 不计入 XP          |
| 周期参与率   | 需连续活跃 ≥3 周才计入奖励榜  |
| 重复行为检测 | 循环交易（A→B→A）权重下降 80% |
| 失败率过滤   | 失败率 \>50% 的钱包不计入统计 |

</div>

5.  **奖励闭环与未来衔接**

<div class="table-wrap">

|               |                             |                                |
|---------------|-----------------------------|--------------------------------|
| 阶段          | 激励形式                    | 目标                           |
| Testnet       | XP + 徽章 + 排行榜          | 建立用户画像与行为基线         |
| Mainnet Early | XP Multiplier / WL / NFT    | 激励迁移与社区留存             |
| Post-Mainnet  | XP → Token Allocation Boost | 治理权重 / 空投比例 / 声誉层级 |

</div>

### 竞品调研

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="64e1306e-a5b0-4cec-be54-9353faa64285">
<tbody>
<tr>
<th class="confluenceTh"><p>维度 / 项目</p></th>
<th class="confluenceTh"><p><strong>Avantis</strong></p></th>
<th class="confluenceTh"><p><strong>GMX</strong></p></th>
<th class="confluenceTh"><p><strong>Jupiter</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>激励核心目标</strong></p>
<blockquote>
<ul>
<li><p>共性： <code>行为数据 → XP → 分配权</code></p></li>
<li><p>特性：GMX分层；Avantis节奏感最强，Jupiter生态闭环最强。</p></li>
</ul>
</blockquote></td>
<td class="confluenceTd"><p>强调活跃用户留存与任务化成长：XP→等级→空投资格）</p></td>
<td class="confluenceTd"><p>通过交易量与推荐返佣驱动长期活跃</p></td>
<td class="confluenceTd"><p>通过 Swap Score 与治理参与扩展生态治理</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>激励形式</strong></p>
<blockquote>
<p>testnet阶段推荐 XP → discord role / badge NFT 为主要奖励，未来可平滑过渡空投逻辑。</p>
</blockquote></td>
<td class="confluenceTd"><p>赛季XP（不可交易）+ 徽章 + 排行榜</p>
<p>XP 计算与 referrals计算详见文档(<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>)</p></td>
<td class="confluenceTd"><p>Referral（链上推荐码、返佣与折扣）+ 定期交易竞赛 + esGMX staking 长期收益。(<a href="https://docs.gmx.io/docs/referrals/" class="external-link" rel="nofollow">docs.gmx.io</a>)<br />
</p></td>
<td class="confluenceTd"><p>年度 airdrop + Carrots后置增长基金）+ 开发者/集成 Referral 程序 + Staking/time-weighted stake 用于治理权重。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>)</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>奖励逻辑</strong></p>
<blockquote>
<p>季度性多维XP + 权重加成 + 周期榜单</p>
</blockquote></td>
<td class="confluenceTd"><p>每个交互类型累积XP（Swap / Perp / LP / Referral）→ 赛季排名→ 奖励池</p></td>
<td class="confluenceTd"><p>交易量比例 + 推荐返佣 + esGMX再质押</p></td>
<td class="confluenceTd"><p>Swap Score + Trade Scare + 社区核心贡献者（申请制）+ 时间加权</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Boost机制</strong></p></td>
<td class="confluenceTd"><p>Staking、XP Multiplier（多行为联动）</p></td>
<td class="confluenceTd"><p>esGMX 锁仓时间越久收益越高</p></td>
<td class="confluenceTd"><p>Staking Time-weight + Voter Bonus</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>推荐体系</strong></p></td>
<td class="confluenceTd"><p>二级推荐：推荐人得被推荐人XP的10%</p></td>
<td class="confluenceTd"><p>链上绑定返佣关系（5–20%）</p></td>
<td class="confluenceTd"><p>API级开发者分润体系（Referral SDK）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>防刷策略</strong></p></td>
<td class="confluenceTd"><p>冷却期 + 最小交易额限制 + 上限</p></td>
<td class="confluenceTd"><p>量化活跃度 + 洗量剔除</p></td>
<td class="confluenceTd"><p>Score权重修正 - 小额/循环交易权重减半 + 失败率剔除</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>赛季周期</strong></p>
<blockquote>
<p>Testnet阶段周期 1-2m，持续迭代至测试网交易数据满意</p>
</blockquote></td>
<td class="confluenceTd"><p>固定Season（6–8周）+ XP清零+徽章留存</p></td>
<td class="confluenceTd"><p>不定期竞赛（2周）+ 长期返佣</p></td>
<td class="confluenceTd"><p>年度空投 + 分季治理激励</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>奖励闭环</strong></p>
<blockquote>
<p>Testnet可先 XP →等级/称号/徽章 → 未来Multiplier</p>
</blockquote></td>
<td class="confluenceTd"><p>XP → 空投权 → 角色等级</p></td>
<td class="confluenceTd"><p>返佣 → esGMX复利 → 治理权</p></td>
<td class="confluenceTd"><p>空投 → 治理 → 质押倍增</p></td>
</tr>
</tbody>
</table>

</div>

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 维度 | Jupiter | GMX | Avantis |
| **激励类型** |  |  |  |
| **Referral 机制** | 开放源码的 Referral Program，用于项目/集成方向（Project/Referral account、share_bps，可用于 Ultra/Swap 等集成）。详见 dev docs 与 Github。(<a href="https://dev.jup.ag/docs/tool-kits/referral-program/" class="external-link" rel="nofollow">dev.jup.ag</a>) | 用户可创建 ref code 并通过链接分发；推荐关系写入合约并长期绑定；返佣/折扣按 tier 分配（Tier1/2/3），高 tier 有额外 esGMX 奖励。(<a href="https://docs.gmx.io/docs/referrals/" class="external-link" rel="nofollow">docs.gmx.io</a>) | 文档明确推荐分成规则（推荐人可获得被推荐人 XP 的比例等），且在 season 中长期保留为增长杠杆。(<a href="https://docs.avantisfi.com/rewards/referrals" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |
| **Leaderboard / Competition** | Perps leaderboard 产品页面（Jupiter 提供 perpetuals leaderboard），并在社区提案/公告里把 leaderboard/排名与 Jupuary 分配挂钩。(<a href="https://jup.ag/perps-leaderboard" class="external-link" rel="nofollow">Jupiter</a>) | GMX 定期举办短周期交易竞赛（例如 EIP-4844 trading competition），设置 Top PnL (\$) 与 Top PnL (%) 排行并分配大额奖励（ARB等），并有门槛与公平性审查。(<a href="https://app.gmx.io/" class="external-link" rel="nofollow">GMX</a>) | Avantis 在其官网提供 leaderboard 页面，并且其 XP 文档与 reward/airdrop 页面说明了赛季（Season）与排行/奖励机制。(<a href="https://www.avantisfi.com/leaderboard" class="external-link" rel="nofollow">Avantis - Decentralized Trading</a>) |
| **反女巫 / 防刷** | Jupuary 明确使用多维过滤（排除短期钱包、小笔/高失败率/循环交易等），并给出 appeals 机制（被误判可申诉）。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) | GMX 用 tier 升级门槛（活跃用户数 + 周交易量）及竞赛人工复核来减少滥用/多账户行为。(<a href="https://docs.gmx.io/docs/referrals/" class="external-link" rel="nofollow">docs.gmx.io</a>) | Avantis 文档中说明在 Season 内采取多项限制/权重来避免刷分，并可通过 season 设置调整 boost/lock 等设计。(<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |
| **奖励形式（testnet vs mainnet）** | Jupuary 是 mainnet 空投（JUP 代币）为主；同时保留 Carrots 做后续激励与 staking/claim 机制；Profile 用于合并钱包视图（但 allocation 仍按钱包发放）。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) | GMX 既有 V1 周度链上分发（ETH/AVAX 等），V2 的折扣/affiliate rewards 会累积并可 Claim，且引入 esGMX 可质押（Affiliate Vault）。(<a href="https://docs.gmx.io/docs/referrals/" class="external-link" rel="nofollow">docs.gmx.io</a>) | Avantis 用 XP（可在 season 结算为奖励/空投资格）与 foundation/airdrop 页面说明了奖励分配与申领渠道。(<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |

</div>

### Jupiter

- **Referral Program（开源实现）** — Jupiter 在其开发文档中将 Referral Program 作为 Tool Kit 提供，明确说明可为“Jupiter Programs 或其它 programs”创建 Project、设置 `default_share_bps`、并通过 `initialize_referral_account` 创建 Referral account；且在文档中直接给出 GitHub 源码链接与 Referral Dashboard 的入口。

- **Jupuary 2025（空投提案与分配结构）** — 社区提案与公告（Jupiter Research / forum）详细列出 Jupuary 2025 的分配思路（Users 440M JUP、Stakers 60M、Carrots 200M 等分项），并说明 Swap Users / Expert Traders 的 tier 化、Swap Score 与反女巫规则（排除交易期\<3周、失败率\>50%、循环交易等）和 appeals 机制。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>)

### GMX

- **Referral** — GMX 文档明确说明：用户可在 Referrals 页面创建推荐码（区分大小写），并通过链接分享；当被推荐人首次交易时，推荐关系会被写入链上合约并长期绑定；推荐人可获取返佣，被推荐人获得折扣。文档还说明 Tier 制度（Tier1/2/3）与 Tier 升级条件（活跃用户数 + 周交易量），以及 V1/V2 在结算与奖励形式（ETH/AVAX、esGMX）上的差异。

- **Trading Competition / Leaderboard** — GMX 举办过（并在公告中说明）短期 trading competition（例如 EIP-4844 相关活动），设置 Top PnL (\$) 与 Top PnL (%) 两类排行榜并按名次发放奖池（ARB 等），且对竞赛有最低资本门槛与公平性复核（人工审查以防多账户/对敲等）。

<div class="table-wrap">

|  |  |
|----|----|
| 你的条目 | 三家中的对应实践或事实（来源） |
| **Swap / Perp / LP 等多维行为计分** | Avantis 的 XP 文档即是“按行为（Liquidity / Trading / Referral）分别计算 XP 并在赛季里分配”。你的多维加权思路与 Avantis 官方实践一致。(<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |
| **Referral: 被推荐人活跃触发/推荐人获部分 XP** | Avantis 文档有“推荐人可获被推荐人 XP 的比例”说明；GMX 则用链上 code 写入并返佣（不同形式但同逻辑：推荐给予推荐人收益）。Jupiter 的 Referral program 则是面向集成/项目级的收益分配（也有 share bps 的概念）。你的 referral 设计可分别映射三者策略（个人邀请/链上绑定/项目集成）。(<a href="https://docs.avantisfi.com/rewards/referrals" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |
| **Leaderboard / 周榜激励** | GMX 与 Jupiter 都有 leaderboard/竞赛产品页面，并在实践中用短周期竞赛来拉活跃与传播；Avantis 也有 leaderboard 页面。你的“周榜激励 + 周榜 XP 奖励”与他们的短周期竞赛逻辑一致。(<a href="https://app.gmx.io/" class="external-link" rel="nofollow">GMX</a>) |
| **赛季长度 4–6 周、XP 清零但保留历史声誉/徽章** | Avantis 使用赛季化 XP（多季迭代）；Jupiter 则使用年度大空投（Jupuary）但也保留长期声誉/时间加权 stake 概念。你的短赛季思路在 testnet 阶段比起 Jupiter 的年度空投更轻量，也更接近 Avantis/GMX 的短期活动实践。(<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) |
| **反女巫（排除短期钱包/循环交易/高失败率）** | Jupiter 的 Jupuary 文档明确列出了这类过滤规则（交易时间 \<3 周、失败率\>50%、循环交易等）；Avantis/GMX 也都有各自的防刷/分层门槛措施（GMX用 tier 条件，Avantis 用任务/阈值与 boost 调整）。你的防刷规则直接借鉴了 Jupiter + Avantis 的做法。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) |

</div>

### To-do

1.  **反女巫策略**（例如：剔除交易期 \<3 周、剔除循环交易、考虑交易失败率），Jupiter 在 2025 Jupuary 已公开采用这些规则作为可检验事实。把 appeals 流程放入运营流程以降低误判投诉成本。(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>)

2.  **Referral**：用户邀请 （GMX & AVNT）+ 项目集成 referral（详见JUP开源代码），两者结合可同时达到拉新与生态集成目的。

3.  **Leaderboard ：**适合testnet期间刺激短期增长 & 熟悉产品 & bug bounty

### ref

- Jupiter:

  - Referral dev docs & source code: <a href="https://dev.jup.ag/docs/tool-kits/referral-program/" class="external-link" data-card-appearance="inline" rel="nofollow">https://dev.jup.ag/docs/tool-kits/referral-program/</a> <a href="https://github.com/TeamRaccoons/referral" class="external-link" data-card-appearance="inline" rel="nofollow">https://github.com/TeamRaccoons/referral</a>

  - Airdrop Proposal:<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" data-card-appearance="inline" rel="nofollow">https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573</a><a href="https://discuss.jup.ag/t/jupuary-legacy-rewards-airdrop-2025-2026/39264" class="external-link" data-card-appearance="inline" rel="nofollow">https://discuss.jup.ag/t/jupuary-legacy-rewards-airdrop-2025-2026/39264</a>

  - Leaderboard product page: <a href="https://jup.ag/perps-leaderboard" class="external-link" data-card-appearance="inline" rel="nofollow">https://jup.ag/perps-leaderboard</a>

- GMX：

  - Referral docs & product page: <a href="https://docs.gmx.io/docs/referrals/" class="external-link" data-card-appearance="inline" rel="nofollow">https://docs.gmx.io/docs/referrals/</a> <a href="https://app.gmx.io/#/referrals" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.gmx.io/#/referrals</a>

  - Leaderboard product page: <a href="https://app.gmx.io/#/competitions/march_20-27_2024" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.gmx.io/#/competitions/march_20-27_2024</a>

- Avantis：

  - referrals docs & product pages：<a href="https://docs.avantisfi.com/rewards/referrals" class="external-link" data-card-appearance="inline" rel="nofollow">https://docs.avantisfi.com/rewards/referrals</a> <a href="https://www.avantisfi.com/referral" class="external-link" data-card-appearance="inline" rel="nofollow">https://www.avantisfi.com/referral</a>

  - leaderboard & airdrop product pages：<a href="https://www.avantisfi.com/leaderboard" class="external-link" data-card-appearance="inline" rel="nofollow">https://www.avantisfi.com/leaderboard</a> <a href="https://foundation.avantisfi.com/airdrop" class="external-link" data-card-appearance="inline" rel="nofollow">https://foundation.avantisfi.com/airdrop</a>

  - XP docs：<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" data-card-appearance="inline" rel="nofollow">https://docs.avantisfi.com/rewards/avantis-xp</a>

<div class="table-wrap">

|  |  |  |  |  |
|----|----|----|----|----|
| 项目 | Avantis（事实 & quote） | GMX（事实 & quote） | Jupiter（事实 & quote） | 你的 Testnet（示例值） |
| **Swap / Trading XP 计量** | **事实**：按成交额累积 Trading XP；“每美元交易最多得 1 XP（fixed-fee trades）”。**Quote**: “Every dollar traded gets at-most 1 XP.” (<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) | **事实**：GMX 以交易量/手续费驱动激励（竞赛按 PnL/\$ 或 PnL% 排名）；平台文档以交易量计入排行榜。**Quote**: “all trades on GMX V2 on Arbitrum… qualify”. (<a href="https://www.coingecko.com/learn/gmx-trading-competition?utm_source=chatgpt.com" class="external-link" rel="nofollow">CoinGecko</a>) | **事实**：Jupiter 将交易行为计入 Swap Score（综合 volume、频率、交易类型），并在 Jupuary 中用 Swap Score 做分配。**Quote**: “All transactions over \$5 are counted towards your Swap Score.” (<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) | **示例（testnet）**：**Swap** — 基础 **10 XP/笔**；`w = log10(成交额/5 USDC)`（小额权重低）。 |
| **Perp / 永续行为 XP** | **事实**：Trading XP 考虑“交易时长 / 市场 / 仓位大小”；长时持仓得更多 XP（文档指出“longer duration trades get more XP”）。**Quote**: “Longer duration trades get more XP.” (<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) | **事实**：GMX 竞赛与 leaderboard 以 PnL（\$ 或 %）为主，衡量开平仓表现。**Quote**: “Top PnL (\$) … Top PnL (%)”. (<a href="https://www.coingecko.com/learn/gmx-trading-competition?utm_source=chatgpt.com" class="external-link" rel="nofollow">CoinGecko</a>) | **事实**：Jupiter 的 Expert Traders（Perps 等）被单独纳入 Jupuary Expert Traders 池，按 trade sizing / volume 分层。**Quote**: “Expert Traders … tiers created by looking at a combination of volume and individual trade sizing.” (<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) | **示例（testnet）**：**Perp** — 基础 **20 XP/开平仓**；`w = √持仓时长 × 收益率因子`。 |
| **LP / Liquidity XP** | **事实**：Avantis 明确：**“one dollar invested as an LP gives 1 point a day.”**（Liquidity XP = \$1/day）。**Quote**: “one dollar invested as an LP gives 1 point a day.” (<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) | **事实**：GMX 有 LP / GLP 激励、swap incentives，与竞赛/earn 模块并存（文档展示 GLP/LP 激励结构）。**Quote**: GMX 文档展示 LP / GLP 激励页面（见 docs & app）。 (<a href="https://app.gmx.io/" class="external-link" rel="nofollow">GMX</a>) | **事实**：Jupiter 在 Jupuary 的分配中对“Stakers（质押者）”做 time-weighted stake 计算（质押按时间加权），LP 类似长期质押被重视。**Quote**: “we took 2 snapshots every month of the past year, averaged your amount of stake … time-weighted stake.” (<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>) | **示例（testnet）**：**LP** — 基础 **15 XP**，`w = 持续天数/7`（鼓励长期 LP）。 |
| **Referral／推荐计入** | **事实**：Avantis：**推荐人得被推荐人 XP 的 10%**（明确写在 docs）。**Quote**: “Referrers: Get 10% of any referred LPs XP.” (<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>) | **事实**：GMX：链上 referral code，返佣/折扣按 Tier（5%/10%/15%等）分配，且推荐关系写入合约长期绑定。**Quote**: “Tier 1: 5% discount … Tier 2: 10% … Tier 3: …” (<a href="https://docs.gmx.io/docs/referrals/" class="external-link" rel="nofollow">docs.gmx.io</a>) | **事实**：Jupiter：提供开源 Referral Program（dev docs + GitHub），用于项目集成 & 收益分配（`default_share_bps` 等）。**Quote**: “Create a Project … set a default_share_bps … initialize_referral_account.” (<a href="https://dev.jup.ag/docs/tool-kits/referral-program/" class="external-link" rel="nofollow">dev.jup.ag</a>) | **示例（testnet）**：**Referral** — 基础 **25 XP/有效邀**；推荐人得被推荐人 XP 的 **10%**，被推荐人享 **+5% XP Boost**（门槛：被推荐人达 Tier2 才视为“有效”）。 |
| **Leaderboard 奖励（周榜）** | **事实**：Avantis 有 leaderboard 页面用于赛季排行展示与奖励（官网 leaderboards）。**Quote**: “Leaderboard” product page available. (<a href="https://www.avantisfi.com/leaderboard" class="external-link" rel="nofollow">Avantis - Decentralized Trading</a>) | **事实**：GMX 用短周期竞赛（例如 EIP-4844）设 Top PnL (\$/% ) 双榜并按名次发奖（具体奖金额度见公告）。**Quote**: “The total prize pool … is 280,000 ARB … Top PnL (\$) … 1st: 50,000 ARB …” (<a href="https://gmxio.substack.com/p/the-gmx-eip4844-trading-competition?utm_source=chatgpt.com" class="external-link" rel="nofollow">gmxio.substack.com</a>) | **事实**：Jupiter 有 Perps Leaderboard 页面并将 leaderboard 与 Jupuary 激励 / 排名关联（perps leaderboard 产品）。**Quote**: “Perps leaderboard” (product page). (<a href="https://jup.ag/perps-leaderboard" class="external-link" rel="nofollow">Jupiter</a>) | **示例（testnet）**：**Leaderboard** — 周榜 **前10 +200 XP / 前100 +50 XP**（固定周榜奖励）。 |

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="4a10b478-aaec-4f08-8730-21731999b9fa">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>项目</p></th>
<th class="confluenceTh"><p>Avantis（事实 &amp; quote）</p></th>
<th class="confluenceTh"><p>GMX（事实 &amp; quote）</p></th>
<th class="confluenceTh"><p>Jupiter（事实 &amp; quote）</p></th>
<th class="confluenceTh"><p>你的 Testnet（示例）</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>赛季周期 / 长度</strong></p></td>
<td class="confluenceTd"><p><strong>事实</strong>：Avantis 使用 Season 制度（S1 / S2 / S3），S3 明确给出起止时间（S3 示例）。<strong>Quote</strong>: “Season 3 began on September 3rd 2025 … end on February 28th 2026.” (<a href="https://docs.avantisfi.com/rewards/avantis-xp" class="external-link" rel="nofollow">docs.avantisfi.com</a>)</p></td>
<td class="confluenceTd"><p><strong>事实</strong>：GMX 以短周期竞赛为主（1–2 周为单次竞赛窗口，见 EIP-4844 活动）。<strong>Quote</strong>: “Two consecutive one-week contests.” (<a href="https://gmxio.substack.com/p/the-gmx-eip4844-trading-competition?utm_source=chatgpt.com" class="external-link" rel="nofollow">gmxio.substack.com</a>)</p></td>
<td class="confluenceTd"><p><strong>事实</strong>：Jupiter 的 Jupuary 为年度空投（2025 为一次性大规模 airdrop），同时保留 Carrots 做年度分配。<strong>Quote</strong>: “Jupuary 2025 … Users 440M / Stakers 60M / Carrots 200M.” (<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>)</p></td>
<td class="confluenceTd"><p><strong>示例（testnet）</strong>：<strong>4–6 周 / 赛季</strong>（短赛季，快速迭代适合 testnet）。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>奖池 &amp; 分配</strong></p></td>
<td class="confluenceTd"><p>Avantis S3 声明“Season 3 reward pool = 4% of token supply; 3% to Traders, 1% to Liquidity Providers.”</p></td>
<td class="confluenceTd"><p>GMX 大竞赛由 GMX / Arbitrum DAO / STIP 提供来资助奖池。竞赛奖金由具体活动决定并按名次分配。 (<a href="https://gmxio.substack.com/p/the-gmx-eip4844-trading-competition?utm_source=chatgpt.com" class="external-link" rel="nofollow">gmxio.substack.com</a>)</p></td>
<td class="confluenceTd"><p>Jupiter Jupuary 给出 700M JUP 的总体分配（Users 440M / Stakers 60M / Carrots 200M）并细化用户子类（Swap / Expert）。</p>
<p>Jupiter 将 Stakers 通过 time-weighted stake 进行分配，同时给 Super Voters / Super Stakers 额外 bonus(<a href="https://discuss.jup.ag/t/jupiter-jup-airdrop-balanced-proposal-for-jupuary-2025/26573" class="external-link" rel="nofollow">Jupiter Research</a>)</p></td>
<td class="confluenceTd"><p><strong>示例（testnet）</strong>：<strong>奖池分配</strong>：以 XP 比例分配“测试激励”（NFT徽章 / WL / mainnet XP multiplier），避免测试期代币发放。</p></td>
</tr>
</tbody>
</table>

</div>

## Referral 对比

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a8afa4cc-f448-4715-bc21-d2f40cba7455">
<tbody>
<tr>
<th class="confluenceTh"><p>项目</p></th>
<th class="confluenceTh"><p><strong>运行机制</strong></p></th>
<th class="confluenceTh"><p><strong>激励层级</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>GMX</strong></p>
<blockquote>
<p><strong>激励：</strong>交易费折扣 + 返佣激励</p>
<p><strong>机制：</strong>链上绑定与持续收益；分层机制防止自刷行<strong>为</strong></p>
</blockquote></td>
<td class="confluenceTd"><p><strong>创建方式</strong>：用户创建任意字母、数字或下划线组合的 referral code（区分大小写）。ARB的referral code可跨链共享，但需多链创建。</p>
<p><strong>分享形式：</strong>系统生成专属链接（如 <code>https://gmx.io/#/?ref=your-code</code>）；或直接一键分享twitter</p>
<p>‘Trying out trading on @GMX_IO, up to 100x leverage on $BTC, $ETH 📈</p>
<p>For fee discounts use: <a href="https://app.gmx.io/#/trade/?ref=yc888" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.gmx.io/#/trade/?ref=yc888</a> ’</p>
<p><strong>绑定 &amp; 转移：</strong>当他人首次通过该链接进入并完成交易时，推荐关系永久存储在 <code>Referral Storage</code> 合约中，且跨设备保持有效）。推荐码可通过 <code>setCodeOwner</code> 方法在链上转移所有权。</p>
<p><strong>使用场景：</strong></p>
<ul>
<li><p>适用于 GMX V1 与 V2。V1 以 ETH/AVAX 发放返佣；V2 直接在交易时自动扣减手续费。</p></li>
<li><p><strong>机构适配。</strong>钱包或其他协议账户也可参与 Tier 2 / 3 激励。</p></li>
</ul>
<p><strong>发放周期：</strong>V1 奖励每周三发放；V2 奖励实时累积，可在 Referrals 页面手动领取。所有交易量、返佣、esGMX 发放记录可公开查询。</p>
<p><strong>奖励形式：</strong></p>
<ul>
<li><p>折扣 - 交易者</p></li>
<li><p>返佣 - 推荐人</p></li>
<li><p>esGMX 奖励 - 推荐人</p>
<p>可在 Earn 页的 Affiliate Vault 中质押/解锁</p></li>
</ul></td>
<td class="confluenceTd"><p>Jupiter 提供开源 Referral Program（repo + dev docs），用于项目集成，可设置 <code>default_share_bps</code> 并初始化 referral accounts。<strong>Quote</strong>: “set a default_share_bps … initialize_referral_account.” (<a href="https://dev.jup.ag/docs/tool-kits/referral-program/" class="external-link" rel="nofollow">dev.jup.ag</a>)</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Avantis</p></td>
<td class="confluenceTd"><p><strong>创建方式</strong>：用户创建任意字母、数字组合的 referral code（区分大小写），与钱包永久绑定。</p>
<p><strong>分享形式：</strong>系统生成专属链接（如 <code>https://gmx.io/#/?ref=your-code</code>）；或直接一键分享twitter</p>
<p>‘Trying out trading on @GMX_IO, up to 100x leverage on $BTC, $ETH 📈</p>
<p>For fee discounts use: <a href="https://app.gmx.io/#/trade/?ref=yc888" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.gmx.io/#/trade/?ref=yc888</a> ’</p>
<p><strong>绑定 &amp; 转移：</strong>推荐码创建后直接与钱包地址关联，无法修改。交易者输入推荐码后，其后续交易将自动计算折扣与返佣。</p>
<p><strong>发放周期：</strong>奖励实时累积，可随时手动领取。返佣单位为 USDC。</p>
<p><strong>奖励形式：</strong></p>
<ul>
<li><p><strong>Referrer</strong> 可查看直接分配至钱包的累计收益（XP）与可领取收益（Rebates），同时查看当前所属 Tier。</p></li>
<li><p><strong>Trader</strong>可查看在交易时直接享受到的手续费折扣（Discounts）适用于 GMX V1 与 V2。V1 以 ETH/AVAX 发放返佣；V2 直接在交易时自动扣减手续费。</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="55f52d26-5c4c-4a86-bfba-ebb458ef79f7">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>项目</p></th>
<th class="confluenceTh"><p>说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>创建方式</strong></p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>分享形式</strong></p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>绑定逻辑</strong></p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>适用场景</strong></p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>发放周期</strong></p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>奖励形式</strong></p></td>
<td class="confluenceTd"><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

### 三、奖励与层级体系（Tiers）

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="d18cae80-1032-4b0d-a9f8-d20ab08b32b4">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>层级</p></th>
<th class="confluenceTh"><p>交易者折扣</p></th>
<th class="confluenceTh"><p>推荐人返佣</p></th>
<th class="confluenceTh"><p>升级条件</p></th>
<th class="confluenceTh"><p>奖励形式</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Tier 1</strong></p></td>
<td class="confluenceTd"><p>5%</p></td>
<td class="confluenceTd"><p>5%</p></td>
<td class="confluenceTd"><p>任意用户可创建</p></td>
<td class="confluenceTd"><p>返佣以 ETH / AVAX 发放</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Tier 2</strong></p></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><p>≥15 活跃用户/周 + ≥$5M 周交易量</p></td>
<td class="confluenceTd"><p>同上</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Tier 3</strong></p></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><p>15%（ETH / AVAX）+ 5%（esGMX）</p></td>
<td class="confluenceTd"><p>≥30 活跃用户/周 + ≥$25M 周交易量</p></td>
<td class="confluenceTd"><p>双币奖励</p></td>
</tr>
<tr>
<td colspan="5" class="confluenceTd"><ul>
<li><p><strong>活跃用户定义</strong>：每周使用该推荐码进行交易的独立账户。</p></li>
<li><p><strong>上限限制</strong>：每周最多分配 5,000 枚 esGMX。</p></li>
<li><p><strong>防滥用机制</strong>：通过层级门槛限制自刷及内部循环推荐。</p></li>
<li><p><strong>协议主体控制权</strong>：具体比例与规则由 GMX Token 持有者治理决定。</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

------------------------------------------------------------------------

### 三、奖励与层级体系（Tiers）

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="95812a7f-8ab0-4bf3-84c4-dac6e7001b10">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>层级</p></th>
<th class="confluenceTh"><p>活跃交易者数量</p></th>
<th class="confluenceTh"><p>累计交易手续费（referred fees）</p></th>
<th class="confluenceTh"><p>推荐人返佣</p></th>
<th class="confluenceTh"><p>交易者折扣</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Tier 1</strong></p></td>
<td class="confluenceTd"><p>&lt; 5</p></td>
<td class="confluenceTd"><p>&lt; $2.5K</p></td>
<td class="confluenceTd"><p>5%</p></td>
<td class="confluenceTd"><p>5%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Tier 2</strong></p></td>
<td class="confluenceTd"><p>&lt; 25</p></td>
<td class="confluenceTd"><p>$2.5K – $50K</p></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><p>10%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Tier 3</strong></p></td>
<td class="confluenceTd"><p>&gt; 50</p></td>
<td class="confluenceTd"><p>&gt; $50K</p></td>
<td class="confluenceTd"><p>15%</p></td>
<td class="confluenceTd"><p>15%</p></td>
</tr>
<tr>
<td colspan="5" class="confluenceTd"><ul>
<li><p><strong>定义说明</strong></p>
<ul>
<li><p><em>Active Trader</em>：在统计周期内进行过交易的独立被推荐用户。</p></li>
<li><p><em>Referred Fees</em>：被推荐用户所产生的总交易手续费（基础指标）。</p></li>
</ul></li>
<li><p><strong>升级逻辑</strong><br />
Referrer 可通过完成两类成长任务（quests）升级：</p>
<ol>
<li><p>增加活跃推荐交易者数量</p></li>
<li><p>提高被推荐交易者的累计手续费总额<br />
升级判定需通过反女巫（anti-sybil）验证后生效。</p></li>
</ol></li>
<li><p><strong>治理机制</strong><br />
Avantis 团队将根据社区反馈动态调整 Tier 阈值与奖励比例。</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

------------------------------------------------------------------------

### 四、设计特征与机制亮点

<div class="table-wrap">

|      |          |
|------|----------|
| 方向 | 设计亮点 |
|      |          |
|      |          |
|      |          |
|      |          |
|      |          |
|      |          |

</div>

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 对比项 | **GMX** | **Avantis** |
| 创建门槛 | 任意用户（但需分别在 Arbitrum / Avalanche 创建） | 完全 permissionless，一键创建 |
| 奖励资产 | ETH / AVAX / esGMX | USDC |
| 链上绑定 | 通过 `ReferralStorage` 合约永久记录 | 推荐码与钱包地址永久绑定 |
| Tier 条件 | 活跃用户数 + 周交易量 | 活跃用户数 + 累计手续费 |
| 奖励比例 | 5%–20%（含 esGMX 奖励） | 5%–15% |
| 防自刷机制 | 分层门槛 + 周期考核 | Anti-sybil 校验 + 任务成长模型 |
| 发放周期 | 每周或实时 | 实时可领取 |

</div>

## **9. Referral & Incentive（推荐与激励体系）**

### 9.1 Referral 系统

二级邀请结构：

<div class="table-wrap">

|         |          |
|---------|----------|
| 级别    | 分润比例 |
| Level 1 | 10%      |
| Level 2 | 3%       |

</div>

合约事件：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
event ReferralReward(address indexed referrer, address indexed trader, uint256 amount);
```

</div>

</div>

### 9.2 交易挖矿积分公式

\[\
score = volume\_{usd} × assetWeight × feeMultiplier\
\]

- 每周重置积分；

- 前100用户发放奖励（代币或 fee rebate）。

> \[Quote: Jupiter Leaderboard – Rewards Model\]

</div>
