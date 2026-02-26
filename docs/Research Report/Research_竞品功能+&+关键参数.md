# Research_竞品功能 & 关键参数

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772008141285 {padding: 0px;}
div.rbtoc1772008141285 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772008141285 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772008141285">

- [需求背景](#Research_竞品功能&关键参数-需求背景)
- [结论](#Research_竞品功能&关键参数-结论)
  - [战略差异洞察](#Research_竞品功能&关键参数-战略差异洞察)
  - [功能，机制，与参数配置](#Research_竞品功能&关键参数-功能，机制，与参数配置)
- [竞品调研](#Research_竞品功能&关键参数-竞品调研)
  - [一、GMX](#Research_竞品功能&关键参数-一、GMX)
    - [协议模型](#Research_竞品功能&关键参数-协议模型)
    - [功能](#Research_竞品功能&关键参数-功能)
    - [参数表](#Research_竞品功能&关键参数-参数表)
    - [Roadmap摘录](#Research_竞品功能&关键参数-Roadmap摘录)
  - [二、Jupiter Perps](#Research_竞品功能&关键参数-二、JupiterPerps)
    - [协议模型](#Research_竞品功能&关键参数-协议模型.1)
    - [功能](#Research_竞品功能&关键参数-功能.1)
    - [参数表](#Research_竞品功能&关键参数-参数表.1)
    - [Roadmap摘录](#Research_竞品功能&关键参数-Roadmap摘录.1)
  - [三、Avantis](#Research_竞品功能&关键参数-三、Avantis)
    - [协议模型](#Research_竞品功能&关键参数-协议模型.2)
    - [功能](#Research_竞品功能&关键参数-功能.2)
    - [参数表](#Research_竞品功能&关键参数-参数表.2)
      - [1. 费率](#Research_竞品功能&关键参数-1.费率)
      - [2. 风控](#Research_竞品功能&关键参数-2.风控)
    - [Roadmap摘录](#Research_竞品功能&关键参数-Roadmap摘录.2)
  - [四、AsterDex](#Research_竞品功能&关键参数-四、AsterDex)
    - [协议模型](#Research_竞品功能&关键参数-协议模型.3)
- [To Do](#Research_竞品功能&关键参数-ToDo)
- [附录](#Research_竞品功能&关键参数-附录)
  - [Table1 - 竞品战略洞察表格](#Research_竞品功能&关键参数-Table1-竞品战略洞察表格)
  - [Table2 - 竞品参数配置表格](#Research_竞品功能&关键参数-Table2-竞品参数配置表格)
  - [GMX maxPnlFactor详解](#Research_竞品功能&关键参数-GMXmaxPnlFactor详解)
    - [定义](#Research_竞品功能&关键参数-定义)
    - [MaxPnLFactor 施加 不同上限目的](#Research_竞品功能&关键参数-MaxPnLFactor施加不同上限目的)
    - [为什么MAX_PNL_FACTOR_FOR_DEPOSIT \<=MAX_PNL_FACTOR_FOR_TRADERS](#Research_竞品功能&关键参数-为什么MAX_PNL_FACTOR_FOR_DEPOSIT%3C=MAX_PNL_FACTOR_FOR_TRADERS)
  - [JPL Loan 计算规则](#Research_竞品功能&关键参数-JPLLoan计算规则)
    - [符号与约定（单位均为 USD 除非另注明）](#Research_竞品功能&关键参数-符号与约定（单位均为USD除非另注明）)
    - [关键计算公式](#Research_竞品功能&关键参数-关键计算公式)
    - [逐步流程](#Research_竞品功能&关键参数-逐步流程)
    - [逐步数值示例](#Research_竞品功能&关键参数-逐步数值示例)
  - [Avantis ZFP机制详解](#Research_竞品功能&关键参数-AvantisZFP机制详解)
    - [交易生命周期 & 具体机制](#Research_竞品功能&关键参数-交易生命周期&具体机制)
    - [交易者 & LP的风险与权衡](#Research_竞品功能&关键参数-交易者&LP的风险与权衡)
    - [量化示例（对应pnl calculator功能）](#Research_竞品功能&关键参数-量化示例（对应pnlcalculator功能）)

</div>

# 需求背景

1.  **竞品：** <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E4%B8%80%E3%80%81GMX" rel="nofollow">GMX（V2）</a>、<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E4%BA%8C%E3%80%81Jupiter-Perps" rel="nofollow">Jupiter Perps</a>、<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E4%B8%89%E3%80%81Avantis" rel="nofollow">Avantis</a>、<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%9B%9B%E3%80%81AsterDex%EF%BC%88Simple-1001x-%2F-Pro-CLOB%EF%BC%89" rel="nofollow">Aster</a>产品级调研报告

2.  **目标：**功能核心差异 & 各项费用以及风控参数配置 & 流动性池模型机制

3.  **重点：**

    - 分章节对比 GMX / Jupiter / Avantis 以下部分：

      - 产品矩阵

      - 协议模型

      - 参数取值与合约风控（收费结构与收益路径；风控机制）

      - 资金效率（GLV vs JLP vs Tranche）

      - 代币经济与激励

    - 附录：

      - 关键机制详解

4.  **方法论：**

    - gpt&手动抓取：优先官方 docs、support、repo、audit PDF、gov posts、官方 blog、重大安全事件分析报告。

    - 目标字段（每个协议均尝试收集）：协议模型、最大杠杆、费率（maker/taker、open/close、swap、stable vs non-stable）、费率分配、管理员 & 可升级性、订单类型、审计情况与重大事件、风控/限额类（max PnL 上限、AUM 上限、weight tolerance、utilization/kink 模型等）。

    - 原则：每项参数手动验证并证实；未公开的项标注缺失 - **建议走合约字段抽取**

5.  **可供复核的ref:**

    - <a href="https://docs.gmx.io/docs/intro" class="external-link" rel="nofollow">GMX docs</a>

    - <a href="https://github.com/gmx-io/gmx-synthetics" class="external-link" rel="nofollow">GMX github</a>

    - <a href="https://gov.gmx.io/t/gmx-v2-2-v2-3/4223/6" class="external-link" rel="nofollow">GMX proposal1</a> <a href="https://gov.gmx.io/t/gmx-v2-x-zero-slippage-max-liquidity-unlimited-open-interest-virtual-order-book/3763" class="external-link" rel="nofollow">proposal2</a>

    - <a href="https://community.chaoslabs.xyz/gmx-v2-arbitrum/risk/overview" class="external-link" rel="nofollow">GMX Dashboard</a> - ChaosLabs Risk Oracle引入 <a href="https://chaoslabs.xyz/posts/gmx-dynamic-price-impact-powered-by-edge-risk-oracles" class="external-link" rel="nofollow">自动对风控参数实时调优</a>并监控

    - <a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees" class="external-link" rel="nofollow">Jupiter docs</a>

    - <a href="https://dev.jup.ag/docs/perp-api/pool-account" class="external-link" rel="nofollow">Jupiter dev</a>

    - <a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/price-impact-fee.ts" class="external-link" rel="nofollow">Jupiter github</a>

    - <a href="https://community.chaoslabs.xyz/jupiter/risk/overview" class="external-link" rel="nofollow">Jupiter Dashboard</a> - ChaosLabs Risk Oracle引入 作为首选 & 实时监控

    - <a href="https://docs.avantisfi.com/liquidity-providers/avantis-lp-vault-avusdc" class="external-link" rel="nofollow">Avantis docs</a>（docs有点杂乱）

    - <a href="https://sdk.avantisfi.com/introduction.html" class="external-link" rel="nofollow">Avantis SDK</a>（并无有用信息）

    - <a href="https://dune.com/restaji/avantis-base-perpetual-dex" class="external-link" rel="nofollow">Avantis Dashboard</a>

# 结论

> 从战略定位；功能实现；参数 & 风控 三方面总结

## 战略差异洞察

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="97af15e5a84df542fa49fd40b086ea64b1aa3884f25e1d5705c81b8098e1e2eb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-10%20at%2015.30.11.png?version=1&amp;modificationDate=1760081563133&amp;cacheVersion=1&amp;api=v2" data-height="765" data-width="1359" data-unresolved-comment-count="0" data-linked-resource-id="15564816" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-10 at 15.30.11.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="e17943ec-99fc-445e-bc33-d58f6c2535a9" data-media-type="file" width="468" height="263" alt="Screenshot 2025-10-10 at 15.30.11.png" /></span>

## 功能，机制，与参数配置

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="00199fd1de08942f5ce79d7ea6bf84dfe6c3239600327d347528f1df2cdd3393" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-10%20at%2015.44.17.png?version=1&amp;modificationDate=1760082282330&amp;cacheVersion=1&amp;api=v2" data-height="862" data-width="995" data-unresolved-comment-count="0" data-linked-resource-id="15695895" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-10 at 15.44.17.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="96c38e25-ed2e-440e-be9b-77aba5adfcfc" data-media-type="file" width="468" height="404" alt="Screenshot 2025-10-10 at 15.44.17.png" /></span>

# 竞品调研

## 一、GMX

### 协议模型

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

- **战略目标：**做去中心化的Binance Futures，主打低费用、深流动性、风控全面的交易。

- **战略重点：**依赖 GLP 流动性池模型，V2 扩展多资产对冲机制；逐步增加多链布局（Arbitrum、Avalanche、Solana、Botanix ）。

- **长远目标：**成为 **DeFi 永续合约领域的核心交易所**，抢占中心化交易所的合约交易市场。

而调研涉及的产品部分，主要由GM Pools (multi-asset pools) 支撑 swap + Perp；可用 GLV聚合 vault 提高 capital efficiency。GMX V2在**市场 token 估值、price impact、PnL cap**等处使用了一套可调“**风险参数集合**”（exponent、factor、maxPnlFactor、reserveFactor 等），参数既在合约中体现也有外部风险建议（Chaos Labs 报告）。这些参数设计是“把市场规模 / 不平衡 / PnL”映射成对 **LP 的即时价值变化**与**手续费**，以保护 LP、抑制操纵并鼓励在需要时的流动性流入。

</div>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="4886bd4c-2470-41f0-8af1-d9498d1863a8">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>类别</strong></p></th>
<th class="confluenceTh"><p><strong>描述</strong></p></th>
<th class="confluenceTh"><p><strong>奖励公式</strong></p></th>
<th class="confluenceTh"><p><strong>关键说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>Staking: GMX</p></td>
<td class="confluenceTd"><p>质押 GMX 以获得协议手续费回购（GMX）的奖励。奖励按质押比例分配。</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="18a1b2d173c93a8da066de15259c2f7ec48bd168b7720f54c01a5781628b91df" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2022.13.14.png?version=3&amp;modificationDate=1758723475970&amp;cacheVersion=1&amp;api=v2" data-height="148" data-width="512" data-unresolved-comment-count="0" data-linked-resource-id="6947206" data-linked-resource-version="3" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 22.13.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="c392744a-e7f4-4322-b683-14dcd74c413d" data-media-type="file" width="147" height="42" alt="Screenshot 2025-09-24 at 22.13.14.png" /></span></td>
<td class="confluenceTd"><p>用户奖励 = (UserStakedGMX / TotalStakedGMX) * GMXBuybackDistributions</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Staking: esGMX</p></td>
<td class="confluenceTd"><p>质押 esGMX 获得与 GMX 相同的奖励。esGMX 本身不可转让。</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="18a1b2d173c93a8da066de15259c2f7ec48bd168b7720f54c01a5781628b91df" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2022.13.14.png?version=3&amp;modificationDate=1758723475970&amp;cacheVersion=1&amp;api=v2" data-height="148" data-width="512" data-unresolved-comment-count="0" data-linked-resource-id="6947206" data-linked-resource-version="3" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 22.13.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="c392744a-e7f4-4322-b683-14dcd74c413d" data-media-type="file" width="147" height="42" alt="Screenshot 2025-09-24 at 22.13.14.png" /></span></td>
<td class="confluenceTd"><ol>
<li><p><strong>Stake esGMX</strong> → 持续获得和 GMX 一样的奖励</p></li>
<li><p><strong>Vesting</strong> → 线性 1 年转成 GMX</p>
<ul>
<li><p>vesting 时需要锁定一部分 GMX 或 GLP 作为抵押</p></li>
<li><p>转换比例和个人账户的平均 staking 历史有关</p></li>
</ul></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Vesting: esGMX</p></td>
<td class="confluenceTd"><p>将 esGMX → GMX，周期为 365 天。需要抵押 GMX/GLP 作为支撑。解锁期间奖励暂停。</p></td>
<td class="confluenceTd"><p>每秒解锁 = esGMX / 365天；可领取 = 解锁累计总额</p></td>
<td class="confluenceTd"><p>解锁需同时锁定 GMX/GLP。解除质押会取消解锁。完整解锁周期 = 365 天。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidity: GLV Pool<br />
<strong>(curated)</strong></p></td>
<td class="confluenceTd"><p>向 GLV 池（由curator管理的vault）提供流动性。赚取来自杠杆交易、兑换与借贷手续费。流动性会自动分配到支持的市场。</p></td>
<td class="confluenceTd"><p>池子奖励 = (用户流动性份额 / 总流动性) × (交易手续费 + 借贷费 + 兑换费)</p></td>
<td class="confluenceTd"><p>市场由 Chaos Labs 策略选择。池子会自动平衡多空资产。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidity: GM Pool</p>
<p><strong>(isolated)</strong></p></td>
<td class="confluenceTd"><p>向 GM 市场池（隔离池）提供流动性。赚取交易、兑换与借贷手续费。回报受价格冲击与利用率影响。</p></td>
<td class="confluenceTd"><p>池子奖励 = (用户流动性份额 / 总流动性) × (交易手续费 + 借贷费 + 兑换费)</p></td>
<td class="confluenceTd"><p>每个市场单独隔离。可在相同支撑资产的 GM 池子之间转换 GM 代币。</p></td>
</tr>
</tbody>
</table>

</div>

1.  **GM**

    1.  GM 是 GMX V2 的 **单一市场 LP Token**。（高度相关于**单一**市场，有集中性风险）

    2.  每个市场（例如 ETH/USD perp）对应一个独立的 GM 池，LP 提供流动性后拿到该市场的 GM token。

    3.  GM token 的价值直接跟随这个市场的仓位盈亏、资金费、交易费用等。

2.  **GLV (GMX Liquidity Vault)**

    1.  GLV 是一个 **组合包装层**，把多个市场的 GM token 组合在一起。（相当于一个 **index fund**，把多个 GM 的风险池合并。）

    2.  设计目的：

        - **风险分散**：不是单押某个市场，而是把资金拆分到多个 GM 市场。

        - **自动再平衡**：GLV 内部 keeper 会根据各市场的 utilization（利用率）在市场间迁移流动性。

        - **简化用户体验**：用户只要存进 GLV，不需要自己挑选/管理各个 GM 池子。

3.  **质押与收益**

    1.  奖励规则：本质上是协议费回购 GMX 再分配，按质押比例（GMX+esGMX）来算。

        1.  esGMX的效果等同 GMX，但如果要转化成真正 GMX，需要走 1 年的 vesting，且要锁定 GMX/GLP 作为支撑**。**

        2.  Stakers 只拿 **GMX token**，可选择复利质押、投入高收益池或在协议中作为抵押物使用。

        3.  由FeeHandler.sol 合约负责费用提取、分配和 GMX token 回购。

    2.  奖励组成：

        1.  V2协议费用分成 27% → 回购 GMX 分给 stakers。计算规则：每个区块累计 pending fees → FeeHandler.sol 执行回购 → 按用户质押占比分配 GMX。

        2.  esGMX 奖励**（**vesting token**）**

    3.  奖励计算公式：

        <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1e4c245d8df9134d64489b29b034091dd953339e474b7adf577a8957513b0cb5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2022.22.12.png?version=1&amp;modificationDate=1758723757988&amp;cacheVersion=1&amp;api=v2" data-height="260" data-width="760" data-unresolved-comment-count="0" data-linked-resource-id="6783122" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 22.22.12.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="95a8c962-646d-4e96-81b1-e1379f67b21a" data-media-type="file" width="468" height="160" alt="Screenshot 2025-09-24 at 22.22.12.png" /></span>

    4.  奖励的 Claim & 管理逻辑（Earn 页面）：

        1.  Claim GMX Rewards → 提取当前 pending 的 GMX

        2.  Stake GMX Rewards → 自动复投

        3.  Claim esGMX Rewards → 提取 esGMX

        4.  Stake esGMX Rewards → esGMX 继续赚收益

4.  **风险：**

    1.  **Illiquidity risk**：GLV 可能积累过多在单一 illiquid GM token 上，导致提款风险。

5.  **参数和治理：**

    1.  GM 市场有自己的：

        - `maxPnlFactorForTraders`

        - `maxPnlFactorForDeposits`

        - `reservedUsd`

        - 用于直接控制单市场 LP 风险。

    2.  GLV 额外多了一些参数来对冲系统性风险：

        - `glvMaxMarketTokenBalanceUsd`

        - `glvMaxMarketTokenBalanceAmount`

        - 限制 GLV 内单个 GM token 占比，避免过度集中。

### 功能

> <a href="https://docs.gmx.io/docs/trading/v2#express-trading-and-one-click-trading" class="external-link" rel="nofollow">https://docs.gmx.io/docs/trading/v2#express-trading-and-one-click-trading</a>

1.  **账户与资金模式**

<div class="table-wrap">

|             |                              |                                  |
|-------------|------------------------------|----------------------------------|
| 模式        | 特点                         | 使用场景                         |
| Wallet      | 链上原生资产，可直接用于交易 | 连接结算链时可直接交易           |
| GMX Account | 统一余额，可跨链交易         | 从非结算链交易，或跨链操作时使用 |

</div>

- 资金差异：

- Wallet 内资金：本链原生，可直接交易

- GMX Account 内资金：可在任何支持链交易

- 交易方式：

  - 结算链：Wallet 或 GMX Account

  - 其他支持链：仅能使用 GMX Account

2.  **交易模式**

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 模式 | 签名方式 | RPC基础设施 | Gas支付 |
| Classic | 链上签名弹窗 | 自己钱包RPC | ETH/AVAX/BTC |
| Express | 离线本地签名，GMX广播 | GMX高可靠RPC（Gelato） | USDC/WETH/WAVAX/PBTC |
| Express + One-Click | 本地存储子账户密钥自动签名 | GMX高可靠RPC | USDC/WETH/WAVAX/PBTC |

</div>

- One-Click Trading 安全策略：

  - 仅限授权数量的即时交易，超出授权次数后需重新签名

  - 资金只能返回到钱包

- 风险：

  - 本地存储的子账户密钥可能泄露

3.  **市场与仓位管理**

- 方向：Long / Short

- 市场选择：不同标的资产（Defi, Meme, L1, L2)

- 高杠杆借贷时流动性池选择：多池可选（ETH-USDC, ETH-USDT等）

- 抵押物选择：支持 ETH、USDC 等不同抵押形式

- 最大杠杆：**动态。随着池子 open interest 增加，最大杠杆会下降**

- 订单类型：Limit，Stop Market，TWAP，TP/SL。其中TP / SL默认可选择**自动取消**，受1**0/position**数量上限。

4.  **清算与市场类型**

- 清算价格通过保证金率计算 (collateral - losses - fees) / Size \< MMR (0.4%-1%)

- 使用 oracle 价格计算，不考虑价格冲击

- 清算后剩余抵押返还钱包

- 清算费：

  - 非合成市场：0.2%

  - 合成市场：0.3%

  - 高波动 / 新上市市场：0.45%

- **市场类型**

<div class="table-wrap">

|              |                        |                                       |
|--------------|------------------------|---------------------------------------|
| 类型         | 特点                   | 风控机制                              |
| Fully Backed | 仓位可完全覆盖池中资产 | Open interest ≤ pool token数量        |
| Synthetic    | 仓位可能大于池中资产   | 超额利润触发 ADL（Auto-Deleveraging） |

</div>

### 参数表

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="center" data-local-id="66ee5677-8713-4460-ab0b-70459b0a3e10">
<tbody>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>参数</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>实测/文档</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>来源</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>最大杠杆</p></td>
<td class="confluenceTd"><p><strong>100×</strong></p>
<p><strong>随池子 OI动态调整。OI增加，Max Lev下降。</strong></p></td>
<td class="confluenceTd"><p><a href="https://docs.gmx.io/docs/intro/" class="external-link" rel="nofollow">GMX docs / product intro.</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Open/Close fee rate</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>0.04% / 0.06%</strong><br />
<strong>根据｜OI_diff｜动态选取。</strong></p></li>
<li><p>实测：<br />
OI diff：-4% → +6.24% 收6bps</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.gmx.io/docs/trading/v2/#open--close-fees" class="external-link" rel="nofollow">Trading on V2</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Swap fee Rate<br />
</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>nst：5 / 7bps; st：0.5 / 2bps</strong><br />
<strong>根据｜weightage_diff｜动态选取。</strong></p></li>
<li><p>实测:<br />
weightage_diff：0.26% → -0.83%时，fee rate变为~7bps的常数;<br />
maxout_usd = 75% avlb liquidity_usd？</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.gmx.io/docs/trading/v2/#swap-fees" class="external-link" rel="nofollow">GMX docs</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price Impact<br />
<strong>（Max 50bps）</strong></p></td>
<td class="confluenceTd"><p><a href="https://github.com/gmx-io/gmx-synthetics?tab=readme-ov-file#price-impact" class="external-link" rel="nofollow">文档：</a>（已实现）</p>
<ul>
<li><p><strong>理念： Δ<sup>exp</sup> × factor</strong> 的形式（exp=2）实现<strong>非线性impact</strong>：小变动 impact 很小，big imbalance 的惩罚迅速放大，从而抑制操纵和鼓励平衡。factor 常常按“基准池规模”归一（比如 pool中有 $50k short token USDC，$50k long token ETH, 所以用 <code>0.01/50_000</code>）以把数值量级变成美元级别的百分数。</p></li>
<li><p><strong>公式：</strong>(Initial USD Difference<sup>PriceImpactExponent</sup> − Next USD Difference<sup>PriceImpactExponent</sup>) × priceImpactFactor ；其中，priceImpactExponent取2，priceImpactFactor取</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e88a7d4af50f4a1688721b79cea8dbece35306fb2dcfdcfc8178a19c950f62e7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2017.21.42.png?version=1&amp;modificationDate=1758705708870&amp;cacheVersion=1&amp;api=v2" data-height="451" data-width="733" data-unresolved-comment-count="0" data-linked-resource-id="6947128" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 17.21.42.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="38ce6776-693f-4cc0-b6de-95cba9eef4d5" data-media-type="file" width="347" height="213" alt="Screenshot 2025-09-24 at 17.21.42.png" /></span></p></li>
<li><p><strong>价格冲击返利机制：</strong>price impact只会在减/平仓时收取。超出50bps的部分正常收取，并在5天后，若通过审核，则可手动领取。</p></li>
</ul>
<p><a href="https://chaoslabs.xyz/resources/chaos_gmx_genesis_risk_framework_methodology.pdf?utm_source=chatgpt.com" class="external-link" rel="nofollow">第三方推荐</a>（未实现）</p>
<p>在 Chaos Labs 为 GMX V2 做的 “Genesis Risk Framework &amp; Methodology” 报告中，有他们为 price impact 参数做模拟、拟合、建议值的部分。 </p>
<ul>
<li><p>在那份报告里，他们对 “理想池子平衡状态下” 的交易规模 vs 允许 price impact 的关系做了拟合，得到：</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6587d7d0bbcf8ff6c08ed9714931dab6be45017924e6ffec96f9917570bea3d3" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2014.55.35.png?version=1&amp;modificationDate=1758696959790&amp;cacheVersion=1&amp;api=v2" data-height="54" data-width="410" data-unresolved-comment-count="0" data-linked-resource-id="6946837" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 14.55.35.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="0b970245-4617-4b96-a40c-307a04db5677" data-media-type="file" width="316" height="41" alt="Screenshot 2025-09-24 at 14.55.35.png" /></span></p>
<p>其中，piFactor=2×10<sup>-13</sup>, piExponent=2.41</p>
<p>这是为了让在某些交易规模下的滑点 / 影响曲线更符合他们的设计目标。</p></li>
<li><p>他们也提到，如果将 exponent 固定为 2（GMX当下默认值），那么 factor 可以设置为 1×10<sup>-10</sup>，以得到一种更线性的滑点增长与“软偏斜”行为。 </p></li>
<li><p>为了控制对池子的扭曲和攻击成本，他们建议 <strong>negative price impact factor = 2 × positive price impact factor</strong>，即对造成更大不平衡的行为惩罚更重。</p></li>
</ul>
<p><a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?usp=sharing" class="external-link" rel="nofollow">实测</a></p></td>
<td class="confluenceTd"><ul>
<li><p><a href="https://chaoslabs.xyz/resources/chaos_gmx_genesis_risk_framework_methodology.pdf?utm_source=chatgpt.com" class="external-link" rel="nofollow">price impact</a></p></li>
<li><p><a href="https://gov.gmx.io/t/chaos-labs-gmx-v2-genesis-risk-parameter-recommendations/2311" class="external-link" rel="nofollow">参数取值proposal（不知道在哪儿看投票结果）</a></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>Funding Fee</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><ul>
<li><p><strong>理念： OI Imbalance<sup>exp</sup> × factor</strong> 的形式（exp，factor未知=2）实现按 long/short OI比例自动调整；在市场行情与borrow合并显示net rate，并需要手动领取。</p></li>
<li><p><strong>公式：</strong></p></li>
</ul>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3bb93f5ecdb8caef656ae0f64dccfeab993ec11feefd913eff77d9bb1d70dda5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2020.34.29.png?version=1&amp;modificationDate=1758717290804&amp;cacheVersion=1&amp;api=v2" data-height="426" data-width="851" data-unresolved-comment-count="0" data-linked-resource-id="6947155" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 20.34.29.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="b58b4502-84e1-46a5-b528-78101f524654" data-media-type="file" width="394" height="197" alt="Screenshot 2025-09-24 at 20.34.29.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><a href="https://github.com/gmx-io/gmx-synthetics?tab=readme-ov-file#funding-fees" class="external-link" rel="nofollow">github</a></p>
<p><strong>exp以及factor 未在公共 docs 公开</strong>；需要合约查找取值。</p></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>Borrow Fee</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>有借用费（防止 liquidity 被占用攻击），基于 utilization 模型（kink/dual slope 型逻辑在讨论/实现中可见）。</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9ca4e3c641702410eb97595a03270b4e29c3417e1a3aa4f26eb9e1e42498b58d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2021.43.09.png?version=1&amp;modificationDate=1758721664453&amp;cacheVersion=1&amp;api=v2" data-height="364" data-width="742" data-unresolved-comment-count="0" data-linked-resource-id="6750307" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 21.43.09.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="82a1e66e-a1ac-4e7c-aa63-2d136ffcfc23" data-media-type="file" width="394" height="193" alt="Screenshot 2025-09-24 at 21.43.09.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e7f4dc61d486bc788296cd35a61b2c9c730ea80c01375e188ac067daf0dd00cb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2021.43.59.png?version=2&amp;modificationDate=1758721702920&amp;cacheVersion=1&amp;api=v2" data-height="403" data-width="1541" data-unresolved-comment-count="0" data-linked-resource-id="6783101" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 21.43.59.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="d2bec47d-49d9-4ca7-aade-9067594f8a30" data-media-type="file" width="394" height="103" alt="Screenshot 2025-09-24 at 21.43.59.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="21353e77167394dfe1933bcd154bd2efc21a3a24ddb65705b56d26d98a5625b5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-24%20at%2021.44.11.png?version=1&amp;modificationDate=1758721849519&amp;cacheVersion=1&amp;api=v2" data-height="174" data-width="671" data-unresolved-comment-count="0" data-linked-resource-id="6914281" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-24 at 21.44.11.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="217606a4-bd6c-4c2e-a419-9cd364fca66b" data-media-type="file" width="394" height="102" alt="Screenshot 2025-09-24 at 21.44.11.png" /></span></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><a href="https://github.com/gmx-io/gmx-synthetics?tab=readme-ov-file#borrowing-fees" class="external-link" rel="nofollow">github</a></p>
<p><strong>未在官方 docs 明确公开取值与方案选择</strong>，<a href="https://github.com/gmx-io/gmx-synthetics/releases" class="external-link" rel="nofollow">需要合约查找取值。</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee split（LP / Treasury / others）</p></td>
<td class="confluenceTd"><p><strong>V2 费用</strong>：63% 给 GM LPs，27% 用于回购 GMX并分配给stakers，10% 给国库。</p></td>
<td class="confluenceTd"><p><a href="https://gmxio.substack.com/p/the-distribution-of-protocol-rewards" class="external-link" rel="nofollow">GMX gov / substack</a></p></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>其他风控参数</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><ul>
<li><p><code>maxPnlFactor</code>：PnL / pool worth 的最大比率上限<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#GMX-maxPnlFactor%E8%AF%A6%E8%A7%A3" rel="nofollow">（场景化：traders / deposits / withdrawals）</a>。</p>
<ul>
<li><p>限制uPnL 对LP token即时估值的冲击</p></li>
<li><p>合约计算时把 net pending PnL * 相关 maxPnlFactor 作为可计入值上限。</p></li>
<li><p>调参时<code>maxPnlFactorForDeposits &lt;= maxPnlFactorForTraders</code> 以免 GLV 被滥用。</p></li>
<li><p>e.g. 把 <code>MAX_PNL_FACTOR_FOR_DEPOSITS</code> 设低会让 deposit 时的 market token 估值偏低，从而<strong>激励</strong> deposit，当 pending PnL 高时通过差价鼓励流入流动性。</p></li>
</ul></li>
<li><p><code>minCollateralFactor</code>：最低抵押率，position collateral / size 的最小比率。合约要求 collateral &gt;= size * minCollateralFactor否则拒单。</p></li>
<li><p><code>reserveFactor</code>：pool 中必须保留作支付 PnL 的比例，决定可供用作结算/借贷给头寸的余额 vs swap/withdraw 的可用余额。</p></li>
<li><p><code>maxPoolAmount</code>：单市场可存入 token 的硬上限以控制池风险暴露。防止单一市场过度集中 LP 资金。</p>
<ul>
<li><p>调参时按市场流动性、TVL 与策略来定；新市场设低，成熟市场可加大。</p></li>
</ul></li>
<li><p><code>maxOpenInterest</code>：单市场单边允许存在的最大 open interest（USD）。硬上限。控制最大未平仓头寸总量以保护 LP 免于过度集中风险。</p>
<ul>
<li><p>合约在开仓前校验 <code>market.openInterest + newSize &lt;= maxOpenInterest</code>。</p></li>
<li><p><code>MaxOpen Interest = reserveFactor * Pool Size</code>：pool 中必须保留作支付 PnL 的比例，控制可被借用的池资金量。</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><ul>
<li><p>这些 factor 是百分比/系数（比如 0.9 = 90%）形式，具体值由治理/部署配置。</p></li>
<li><p>docs 未明确；建议：合约扫描 + audit pdf 查找变量。</p></li>
</ul>
<p><a href="https://github.com/gmx-io/gmx-synthetics?tab=readme-ov-file#market-token-price" class="external-link" data-card-appearance="inline" rel="nofollow">https://github.com/gmx-io/gmx-synthetics?tab=readme-ov-file#market-token-price</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Admin / 可升级性</p></td>
<td class="confluenceTd"><p>timelock + multisig / role 管理（治理提案控制关键参数），合约可升级 surface 有治理路径。</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>审计 &amp; 重大事件</p></td>
<td class="confluenceTd"><p>多家第三方审计（Quantstamp / Dedaub / others 列表）；<strong>2025-07 V1 出现重大 reentrancy exploit（≈$42M，后部分返回）</strong>，已被多家安全团队（CertiK、Halborn、SlowMist）分析。<strong>这一点对 AUM/GLP 会计逻辑与 reentrancy guard 极具参考价值。</strong></p></td>
<td class="confluenceTd"><p><a href="https://blog.solidityscan.com/gmx-v1-hack-analysis-ed0ab0c0dd0f?utm_source=chatgpt.com" class="external-link" rel="nofollow">SolidityScan</a></p></td>
</tr>
</tbody>
</table>

</div>

### \
Roadmap摘录

> <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%5BhardBreak%5D" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%5BhardBreak%5D</a>

- **Gasless Transactions（免 gas 交易）**：用户可以只签名，不用自己付 gas，让 keeper 网络（如 Gelato）代发交易。

- **Network Cost Subsidies（网络费补贴机制）**：用部分开/关/交换手续费池，用来补贴用户在网络高峰期的 gas 费。

- **Multichain 支持 + 虚拟账户**：让用户跨链交易更便捷，不需要在每条链都部署新的 GMX 实例。

- **Cross-collateral（交叉抵押）**：允许用一种资产作为抵押，交易不同市场合约。

- **Capped Price Impact / Price Impact Rebates 的变更**：将 price impact 从开仓立刻扣改为“post-position”（先执行，closing 时核算净 impact），并优化 rebate 机制。

- **净 OI 限制 (Net OI Cap)**：在开仓的时候限制 net long vs short 的最大差额，以控制极端风险。

- **引入 Kink Borrowing Rate**：提案中提到用“kink borrowing rate”模型，让日常借费较低，高需求时借费上升。

- **减少借贷 / 资金费率（Borrowing & Funding Rates Reduction）**：提案中有工作方向是 “reduce the borrowing and funding rates” 以改善交易成本。

## 二、Jupiter Perps

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

- **战略目标：**成为 Solana 上的去中心化binance，覆盖**基础设置层** → **流动性聚合执行层** → **Superapp产品矩阵**。

- **战略重点：协议矩阵 + 入口流量。**通过 Jupiter Terminal、Limit Order、DCA、Perps、Loan、Lend、Launchpad 等扩展，打造收入多元化，代币实用，多模态的全栈superapp。但多模态产品矩阵仍需验证真实用户数量vs bot数量，因重点在superapp流量入口，UX没花心思打磨，很容易多而不精，能拉新但无法留存。

  - **To C** 能让用户享受到最优路由的同时满足基本需求（借贷、交易、撸毛、发币、投票）。

  - **To B** 能让项目方用 **Ultra API / Swap API**，直接接入 Jupiter 的聚合流动性，把“最优报价、路由”嵌入自己应用。

  - **To MM** 可以接入 Jupiter Z，成为流动性提供方，直接给用户报价，赚手续费差。

- **长远目标：**巩固其作为 Solana 生态主导的地位，强化 **JUP 代币的实用性**（抵押品、治理、质押 boost、空投条件），从而形成正反馈飞轮。

而调研中涵盖的**Jupiter Perps** 基于 GMX V1的多资产聚合LP池 trader↔LP 对赌模型，用“oracle 价格 + price-impact 模拟费用”实现**零滑点**体验。LP 通过 JLP 持有池中价值并享受**75%**平台收入分成。

</div>

</div>

### 协议模型

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="d3fe6695-c08f-43da-a906-4e40a917e4eb">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>类别</strong></p></th>
<th class="confluenceTh"><p><strong>描述</strong></p></th>
<th class="confluenceTh"><p><strong>奖励公式</strong></p></th>
<th class="confluenceTh"><p><strong>关键说明</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Staking: SOL</strong></p></td>
<td class="confluenceTd"><p>LST玩法。用户质押SOL获得JupSol，质押的SOL会到 Jupiter 指定 validator（Catzo），将质押奖励与 Jito MEV 奖励计入收益，从而提高 LST持有者的回报率。</p></td>
<td class="confluenceTd"><ul>
<li><p>JLP Pool 闲置的 SOL+<a href="https://discuss.jup.ag/t/jupsol-jupiter-staked-sol/14666" class="external-link" rel="nofollow">团队投入100k SOL</a> + 用户质押，约7%-11% APY</p></li>
<li><p>平台收取0.1% SOL deposit fee防套利攻击</p></li>
<li><p><a href="https://support.jup.ag/hc/en-us/articles/21760554651548-JLP-SOL-Staking" class="external-link" rel="nofollow">平台抽成25% 用户分成75%</a></p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>仅委托给 Jupiter validator（非多 validator stake pool）。</p></li>
<li><p>会创建单独 stake account 和 stake info account 记账。</p></li>
<li><p>解除质押需等待 Solana 2–3 天。</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Earn: JLP</strong></p></td>
<td class="confluenceTd"><p>GMX V1 模型</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="98fd527cd240df3848883a6134b5b5e8f688d31634368823d9476b191b4d28aa" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-25%20at%2018.06.02.png?version=1&amp;modificationDate=1758795053318&amp;cacheVersion=1&amp;api=v2" data-height="905" data-width="596" data-unresolved-comment-count="0" data-linked-resource-id="7340093" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-25 at 18.06.02.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="db453dee-c22e-4033-8413-978c1722b2fb" data-media-type="file" width="149" height="225" alt="Screenshot 2025-09-25 at 18.06.02.png" /></span></td>
<td class="confluenceTd"><ul>
<li><p>JLP 收益 = 75% × Protocol Revenue</p></li>
<li><p>APY ≈ 18%</p></li>
<li><p>协议收益包含以下4项：</p></li>
<li><p>JLP 的APY来源：</p>
<ul>
<li><p><strong>交易手续费</strong>（Open/Close Fees; Price Impact; Borrow Fees; Liquidated Collaterals; LP Fees）</p></li>
<li><p><strong>借贷利息 &amp; 清算罚金</strong>（来自 JLP Loans）</p></li>
<li><p><strong>对手盘 Net Loss</strong></p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>AUM未超限：<code>VirtualPrice = ΣAUM_usd / TotalSupply</code></p></li>
<li><p>AUM超限：mint行为被disable，二级市场JUP溢价至<code>Market Price</code>，burn行为按溢价算。</p></li>
<li><p><code>MarketPrice = VirtualPrice + Premium</code></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Loans: JLP</strong></p>
<p>质押JLP → 借贷USDC</p></td>
<td class="confluenceTd"><p>把 JLP 的“闲置” USDC 释放出来，提供给用户借贷 (over-collateralize)，从而提高 JLP 持有人整体收益</p>
<p>利率随借用代币利用率动态变化（jump-rate 模型）。</p></td>
<td class="confluenceTd"><ul>
<li><p>Initial LTV: 借款者需维持 LTV ≤ 83%</p></li>
<li><p>Maintenance LTV：当 LTV ≥ 86% 触发清算。利息按利用率计算并回流池子。<br />
</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p><a href="https://support.jup.ag/hc/en-us/articles/21129961805084-JLP-Loans" class="external-link" rel="nofollow"><strong>关键约束/保护</strong></a>：<br />
最大 LTV：<strong>83%</strong>，清算 LTV：<strong>86%</strong>，Borrow Cap：<strong>50%</strong> jump-rate 曲线<br />
清算罚金：<strong>6%</strong>（从抵押品中扣除并归入 JLP 池）。</p></li>
<li><p>只有白名单的 keeper 可做清算（非任意外部 liquidator）</p></li>
</ul>
<p><a href="https://discuss.jup.ag/t/jlp-loan-initial-parameter-recommendations-and-yield-projections/38428" class="external-link" rel="nofollow">ChaosLabs推荐参数</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Lend(Earn; Borrow; Multiply)</strong></p>
<p><a href="https://fluid.io/" class="external-link" rel="nofollow">第三方integration</a></p></td>
<td class="confluenceTd"><ol>
<li><p><strong>Earn</strong></p></li>
</ol>
<ul>
<li><p>存入闲置资产赚取被动收益（USDC、USDT、SOL、EURC 等）</p></li>
<li><p>收益来源为借款人支付的利息/清算罚金。其中利率随借用代币利用率动态变化</p></li>
</ul>
<ol start="2">
<li><p><strong>Borrow</strong></p></li>
</ol>
<ul>
<li><p>存入抵押资产，借出 Vault 的借贷资产(over-collateralize)</p></li>
<li><p>借款额受 <strong>LTV</strong>限制。<strong>Initial LTV：</strong>超过会禁止新增借款。<strong>Maintenance LTV：</strong>低于则触发清算</p></li>
<li><p><strong>清算罚金：</strong>每个vault不等 0.1% - 5%之间</p></li>
</ul>
<ol start="3">
<li><p><strong>Multiply</strong></p></li>
</ol>
<ul>
<li><p>基于 Borrow 的扩展功能。用户通过<strong>自动借贷 + Swap + 循环存入</strong>来放大抵押资产的收益或风险敞口。类似 Aave 的 <strong>Looping</strong> 或 Maker 的 <strong>Multiply Vault</strong></p></li>
<li><p>e.g.：用户存SOL进入SOL-USDC Vault → 协议自动借出 USDC → 将借贷收自动 Swap 成 SOL，再次存入抵押 → 重复循环，直到达到用户选择的杠杆倍数</p></li>
<li><p><strong>可调参数</strong>：杠杆范围：1x ~ 3.8x（取决于 Vault LTV 限制）最大可借额度：受即时 Vault 流动性约束Slippage 容忍度</p></li>
</ul></td>
<td class="confluenceTd"><p>Multiply APY <strong></strong> = (Supply APR × Collateral – Borrow APR × Debt) / Deposit × 100%</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Swap</strong></p></td>
<td class="confluenceTd"><p><strong>聚合路由 + 多源流动性调度</strong>：普通用户前端 swap，开发者用 API 调流动性，做市商用 RFQ 吃订单流，背后由 Juno 统一调度路由引擎</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p><strong>链上聚合</strong>（Metis） → 算法路由，多路径最优执行，比如用户换 BTC→SOL→USDC，会在一众AMM/DEX找最优价格。</p></li>
<li><p><strong>链下/做市商 RFQ</strong>（Jupiter Z） → 直连做市商拿报价，大单用户拿更优价格。</p></li>
<li><p><strong>多引擎统一调度</strong>（Juno） → 把 Metis、JupiterZ、Hashflow、DFlow 等统合，用 AI自学习机制挑最优来源。</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

### 功能

1.  **交易模式**

- **Request Fulfillment Model（keeper-driven）**：Jupiter 使用一种“请求-执行”模型（trader 在前端提交请求，keeper 或专门 executor 执行链上操作），这使得可实现 **gasless** 下单、limit orders 的 keeper 执行以及更灵活的执行策略。

- **Oracle-priced execution**：Perps 基于多源 oracle（Edge by Chaos Labs 为主，Chainlink + Pyth 为 backup）在交易执行或由 keeper 定期更新时读取价格，从而实现零滑点。

- **Limit & Gasless Orders**：

  1.  **单仓模式**：每个用户最多可打开 **6 个 position**（Long/Short for SOL, wETH, wBTC）

  2.  **限价单上限**：用户可提交 limit order（最多 20 个/币对/侧），在市场 utilization 超过 80% 时禁止新 limit order。相当于提交限价单时，有MaxGlobalOI = 80% Pool Size这一限制。

  3.  **Gasless 下单：**由 keeper 代为提交并执行，用户仅提交请求并可免 gas。

2.  **市场与仓位管理**

- 方向：Long / Short

- 市场选择：SOL, ETH, WBTC

- 抵押物选择：可用平台支持的任何现货资产作为抵押

- 最大杠杆：SOL **100×**；ETH & wBTC **150×**

- 订单类型：Limit，Market，TP/SL。其中Limit Order有**20/pair/side**数量上限，以及max Global OI上限

4.  **清算**

- **清算触发**：清算时全部剩余抵押物都计入 JLP，作为池内收益。

### 参数表

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="bf59476e-16f5-4318-bd01-6b460d213422">
<tbody>
<tr>
<th class="confluenceTh"><p>参数</p></th>
<th class="confluenceTh"><p><strong>实测/文档</strong></p></th>
<th class="confluenceTh"><p><strong>来源</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>最大杠杆</p></td>
<td class="confluenceTd"><ul>
<li><p>SOL <strong>100×</strong></p></li>
<li><p>ETH &amp; wBTC <strong>150×</strong></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/18734981395356-Leverage-Management#h_01JN4PV1NBMMNY0CYT38466MB7" class="external-link" rel="nofollow">docs</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Open/Close Fee Rate</p>
<p><strong>(Max Trade Size ≈ 10% Avlb Liquidity)</strong></p></td>
<td class="confluenceTd"><p><strong>6bps</strong>（含 liquidations / TP/SL / limit）</p></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees#h_01JN4Q2JMW2KQTGT419R62FYKX" class="external-link" rel="nofollow">docs</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Swap Fee Rate<br />
</p></td>
<td class="confluenceTd"><p><strong>参数：</strong></p>
<ul>
<li><p><strong>nst_swap：10 bps; st_swap：2 bps</strong></p></li>
<li><p><strong>nst_tax：500 bps; st_tax：50 bps</strong></p></li>
<li><p><strong>根据｜weightage_diff｜动态加减。</strong><br />
</p></li>
</ul>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="58a947d82ff0abb54a7433164ca8025b4a0883e398b57a6c89fe178d840bb7a0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-27%20at%2013.42.28.png?version=1&amp;modificationDate=1758951771022&amp;cacheVersion=1&amp;api=v2" data-height="218" data-width="767" data-unresolved-comment-count="0" data-linked-resource-id="8814617" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-27 at 13.42.28.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="2b94e6e9-a79f-4d39-adfb-6a6aa55fecb7" data-media-type="file" width="468" height="132" alt="Screenshot 2025-09-27 at 13.42.28.png" /></span></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees" class="external-link" rel="nofollow">fees</a><br />
<a href="https://discuss.jup.ag/t/price-impact-parameter-recommendations-june-3rd-2025/38497" class="external-link" rel="nofollow">20250603 discussion</a></p>
<p><a href="https://discuss.jup.ag/t/additive-on-imbalance-price-impact-model/38562" class="external-link" rel="nofollow">20250605 proposal</a></p>
<p><a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/calculate-swap-amount-and-fee.ts?utm_source=chatgpt.com" class="external-link" rel="nofollow">代码</a></p>
<p><a href="https://discuss.jup.ag/t/chaos-labs-jupiter-swap-fee-recommendation/28558?utm_source=chatgpt.com" class="external-link" rel="nofollow">chaoslabs</a></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e673bc05ea158cdff76af6c5a384fce1f54a252716866a8e7943619c158e918a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-27%20at%2013.46.04.png?version=2&amp;modificationDate=1758952037774&amp;cacheVersion=1&amp;api=v2" data-height="162" data-width="690" data-unresolved-comment-count="0" data-linked-resource-id="8716317" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-27 at 13.46.04.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="766bf458-a3cd-41bc-8512-3f4aa3e907d9" data-media-type="file" width="195" height="45" alt="Screenshot 2025-09-27 at 13.46.04.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price Impact</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Price Impact 机制</strong>：对大单或严重 OI 失衡收取两层 price impact fee</p>
<ol>
<li><p><strong>线性 Linear price impact fee</strong>：trade_size / <code>pricing.tradeImpactFeeScalar</code></p></li>
<li><p><strong>指数性 Additive penalty</strong>：当 open interest imbalance 超过 custody-specific threshold 时，额外按不平衡比例计收，最终被 <code>maxPriceImpact</code> 限制</p></li>
</ol></li>
<li><p><strong>Max Price Impact = 44bps</strong></p></li>
<li><p><strong>Warning Price Impact = 20bps</strong></p></li>
</ul>
<p><strong>公式：</strong></p>
<ul>
<li><p>OI Imbalance &lt;= threshold部分线性收费，费率为配置的常数</p></li>
<li><p>OI Imbalance &gt; threshold部分指数性收费，费率为 factor × ( 新的OI Imbalance / Threshold )^exp，其中factor及exp为配置的常数</p></li>
<li><p>总费用 PriceImpact_USD = min(linear + additive, max price impact),其中max代表上限，当前配置的是<strong>44bps</strong><br />
</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6b9ca9dabe88ed823cecb0cabe57c41cfa95c2bf01563198f99fe9cc87020bd0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-09%20at%2018.59.11.png?version=1&amp;modificationDate=1760007583262&amp;cacheVersion=1&amp;api=v2" data-height="252" data-width="607" data-unresolved-comment-count="0" data-linked-resource-id="14811199" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-09 at 18.59.11.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="4fbe53d2-fb5c-4a94-bd10-671ef7625eee" data-media-type="file" width="294" height="122" alt="Screenshot 2025-10-09 at 18.59.11.png" /></span></p></li>
</ul>
<p><strong>实测:</strong></p>
<ul>
<li><p>weightage_diff -1.04% → -1.32%时，price impact = 20bps</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees#h_01K49FNTP7AXVVQB5AEKS4Q2ZR" class="external-link" rel="nofollow">Fees 页面</a></p>
<p><a href="https://discuss.jup.ag/t/chaos-labs-jupiter-price-impact-fee-borrowing-rate-recommendations/17725?utm_source=chatgpt.com" class="external-link" rel="nofollow">custody</a></p>
<p><a href="https://discuss.jup.ag/t/chaos-labs-price-impact-mechanism-proposal/25407" class="external-link" data-card-appearance="inline" rel="nofollow">https://discuss.jup.ag/t/chaos-labs-price-impact-mechanism-proposal/25407</a></p></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>Borrow fee</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><ul>
<li><p><strong>Borrow Fees（替代 funding）机制</strong>：Jupiter 对持仓的资金成本按小时计算（hourly borrow fee），计算公式依赖 custody 的 <code>fundingRateState.hourlyFundingDbps</code> 与 utilization（locked / owned）。借贷费用持续影响仓位的净 collateral / liquidation price。</p></li>
<li><p><strong>公式：</strong>Hourly Borrow Fee = Total Tokens Locked / Tokens in Pool × Hourly Borrow Rate × Position Size</p></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><a href="https://support.jup.ag/hc/en-us/articles/18735045234588-Fees#h_01JN4Q49TH2V7W4HSDQKJ2ZEF9" class="external-link" rel="nofollow">Fees 页面</a></p>
<p>hourlyRate参数配置在 custody 的 <code>fundingRateState.hourlyFundingDbps</code> 查看</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Limit order cap</p></td>
<td class="confluenceTd"><ul>
<li><p>除 limit order 创建数量上限20外，仍有一个locked/total池子利用率相关的阈值。</p></li>
<li><p><strong>当 market utilization &gt; 80% 时禁止新 limit orders</strong>。</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/19209043643036-How-limit-orders-work-on-Jupiter-Perps" class="external-link" rel="nofollow">Limit Orders</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Fee split（LP / Protocol）</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>75% → 回流 JLP 池；25% → 协议</strong></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://support.jup.ag/hc/en-us/articles/19356216696860-JLP-Economics" class="external-link" rel="nofollow">JLP</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Admin</p></td>
<td class="confluenceTd"><p>许多 global 参数（如 max global long/short sizes）由admin管理并修改</p></td>
<td class="confluenceTd"><p><a href="https://dev.jup.ag/assets/files/Jupiter-Perpetuals-Feb-2024-66183264a9656eef393cedfb0e2d5db1.pdf?utm_source=chatgpt.com" class="external-link" rel="nofollow">audit</a></p></td>
</tr>
</tbody>
</table>

</div>

### Roadmap摘录

- **JLP SOL Staking 扩展**：（Q4 25 已实现）将 JLP 池中闲置 SOL 更多地质押以获得更多收益。

- **Perps & JLP升级：**（Q4 25 已实现）增强借贷上限、多抵押支持（非仅 USDC）、优化风险参数 / 借贷的清算阈值等。

- <a href="https://coinmarketcap.com/cmc-ai/jupiter-perps-lp/latest-updates/" class="external-link" rel="nofollow"><strong>跨链 / 多链流动性网络（Jupnet / Omnichain Liquidity）</strong></a>：推出 “Jupnet Testnet” 或跨链网络，把 JLP 的流动性打通多条链（Solana → Ethereum / Base / Blast 等）

- **更多 API / 基础设施扩展：**基于 Metropolis API 平台继续向 Wallet / DeFi 应用开放更多接口。

- **UX：**提高移动端体验 / 钱包接入便捷性 / UI 流畅度，长期方向。

- <a href="https://feedback.jup.ag/roadmap" class="external-link" rel="nofollow"><strong>DAO提案推动优化：</strong></a>Roadmap 页面本身就是社区反馈平台，未来很多功能可能由社区票选 / 提案触发。

## 三、Avantis

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

- **战略目标：去中心化kraken。**提供比 GMX 更灵活、更模块化的多品类**RWA衍生品市场**，允许更丰富的交易对（加密、外汇、大宗、美股等）。定位高杠杆/厌恶风险 的交易者，并使用 **可风险分层的单一 USDC 流动性池**设计来控制风险。

- **战略重点：**打造**高资本效率**的保证金交易系统，通过接入morpho支持多资产抵押，构建更广泛的 RWA 衍生品生态。

  - **Zero-Fee Perpetuals (ZFP)**：即只在盈利时收取（或从盈利中提取费用/回购）。

  - **高杠杆（最高 500x）**，通过合成资产（synthetic）和优化清算机制实现。

  - **风险参数化 LP 机制**：LP 可以选择风险分层（tranche）与锁仓时间，主动表达风险偏好。

  - **创新机制**：Zero-Fee Perpetuals（利润分成型永续）、正滑点奖励、亏损返利（loss rebate）、RWA接入

- **长远目标：**定位为“链上衍生品交易所”，拓展到 TradFi 市场，切入更广泛的用户与机构。既服务**高杠杆**投机者，也能让 LP 有更细化的风险设置。

与前两者不同，Avantis是vAMM + Skew-based Incentive + External Hedge的机制，LP 只提供usdc用来承受 PnL 波动。池子里没有标的资产，Trader 盈亏 = vAMM 记账 + 预言机价格撮合交易。关键机制差异在于：

- **Loss Protection（损失保护）**

  - 如果你站在OI过小的一方，亏损时有 10~20% rebate。激励交易者自动去做 skew balancing。

- **Positive Slippage（正滑点）**

  - 如果你下单方向缓解了 skew，系统给更好的成交价。

  - 相当于奖励“帮忙均衡市场”的交易者。

- **外部做市商对冲**

  - 像 Keyrock 这样的机构，会在 skew 明显时在外部市场反向下单，把风险转移走。

  - 协议可补贴其成本，或和其分享收益。

</div>

</div>

### 协议模型

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="b8af6d89-16b7-44e0-9932-5229ef0ad29a">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>类别</p></th>
<th class="confluenceTh"><p>描述</p></th>
<th class="confluenceTh"><p>奖励公式</p></th>
<th class="confluenceTh"><p>关键说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Staking: AVNT</strong></p></td>
<td class="confluenceTd"><p>相当于insurance vault，质押 AVNT 进入SM（security module）</p></td>
<td class="confluenceTd"><p>yield + zfp利润分成 + 手续费折扣 + 空投xp</p></td>
<td class="confluenceTd"><ul>
<li><p>LP 即时亏损 &gt;5%，直接动用 AVNT 的质押的资金去事后补偿</p></li>
<li><p>slashing上限cap在20% 质押资产。</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidity: avUSDC Pool</strong></p></td>
<td class="confluenceTd"><p>LP 存 USDC，为所有合约市场提供流动性</p>
<ol>
<li><p><strong>Liquidity Buffer:</strong> 爆仓时，15%奖励keeper结算，剩余全部collateral被收入协议的liquidity buffer ，用于坏账处理/支付已实现盈亏。同时当liquidity buffer比例减少超过 5%时，会从SM这里扣，最大扣除不超过质押的20%。</p></li>
<li><p><strong>avUSDC Vault：</strong>LP mint <strong>USDC</strong>获得<strong>avUSDC</strong> (ERC-4626)<strong>。</strong>作为vault底层资产可以用于各种策略（借贷、staking、交易对冲等），vault 暂时没对外暴露策略细节。交易者盈利不算做LP收益，同时风险LP不必承担。LP收入来源仅为手续费收入，以及后续vault的策略收入。</p></li>
<li><p><strong>SM：</strong>空投获得AVNT, 鼓励用户质押到SM。质押者奖励为 AVNT 通胀奖励 + XP Boost + 费率折扣。仅在极端亏损时（buffer 比例 &lt; 0.95）被动分担损失（最大 20% 被削减）</p></li>
</ol></td>
<td class="confluenceTd"><p>奖励 = (LP份额 / 总池) × (交易费 + Trader净亏损 ± 激励)</p></td>
<td class="confluenceTd"><ol>
<li><p>交易者 &lt;-&gt; Vault (avUSDC) 之间对赌。</p></li>
<li><p>当交易者亏钱 → 损益进入 <strong>liquidity buffer</strong>（利润缓冲池）。</p></li>
<li><p>当交易者赚钱 → 从 buffer 支付给交易者。</p></li>
<li><p><strong>LP 收益</strong> 来自交易费，而非交易者亏损。</p></li>
<li><p><strong>Vault 保持近似 delta-neutral</strong>，通过 buffer 缓冲短期偏移。</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ul>
<li><p><strong>Tranches</strong> 把风险集中到愿意承受的人群（Junior），使 Senior 更安全，从而吸引保守资金（提升 TVL）。</p></li>
<li><p><strong>VBR + 提现费</strong> 则在宏观层面监控整个池子的即时安全边际：当未实现 PnL 侵蚀 buffer 时，收紧退出并触发费用，防止流动性雪崩。</p></li>
</ul></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1c3200611352aa408ae734e5ef7f67afbe3449f50430b731ec8d7fbc375db7b9" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2011.34.36.png?version=1&amp;modificationDate=1759203312908&amp;cacheVersion=1&amp;api=v2" data-height="295" data-width="831" data-unresolved-comment-count="0" data-linked-resource-id="10846209" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 11.34.36.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="905c60b8-5125-42e5-aa01-3ab582317a43" data-media-type="file" width="149" height="52" alt="Screenshot 2025-09-30 at 11.34.36.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="e5bb160fb3109f3df11b65951906de66d4b8ea9aeddcef519b6585978e746f60" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2011.38.18.png?version=1&amp;modificationDate=1759203517321&amp;cacheVersion=1&amp;api=v2" data-height="197" data-width="721" data-unresolved-comment-count="0" data-linked-resource-id="10911748" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 11.38.18.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="0bec90ad-053a-40c3-a7c6-f1fd56edeacf" data-media-type="file" width="149" height="40" alt="Screenshot 2025-09-30 at 11.38.18.png" /></span></td>
<td class="confluenceTd"><ul>
<li><p><strong>收益分配</strong>：Junior 拿 65% 的交易费/收益；Senior 拿 35%。（Gov）</p></li>
<li><p><strong>损失分配：</strong>与收益比例一致</p></li>
</ul>
<ol>
<li><p><strong>资金预留</strong>：开仓时，协议先按“目标比例”（例如 65/35）尝试从两池预留杠杆/容量；若某一池余额不足，则按实际池余额比例进行分配</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Trading: Zero-Fee Perps (ZFP)</strong></p></td>
<td class="confluenceTd"><ul>
<li><p>针对<strong>Lev&gt;75x</strong>的仓位，不收开仓费/平仓费/借贷费；只有当<strong>平仓获利</strong>时，按盈利百分比抽成</p></li>
<li><p>比例随ROI 滑动，低至 <strong>2.5%高至80%</strong></p></li>
</ul></td>
<td class="confluenceTd"><p>Fee = Profit × （1 -ShareRatio）</p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="30cc3ccc0be7b4d5e1c72a9f00cf2f73d24f1d4686171904cf7cc43ee2c27b95" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2012.15.04.png?version=1&amp;modificationDate=1759205977505&amp;cacheVersion=1&amp;api=v2" data-height="630" data-width="825" data-unresolved-comment-count="0" data-linked-resource-id="10911758" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 12.15.04.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="ffac3b78-19e5-4ce2-87eb-5f2fb3e4b526" data-media-type="file" width="149" height="113" alt="Screenshot 2025-09-30 at 12.15.04.png" /></span></td>
<td class="confluenceTd"><p><strong>目标人群</strong></p>
<ul>
<li><p><strong>高频/短线交易者（scalpers）：</strong>他们常做小利润、频繁进出，ZFP 降低了开平和借贷门槛。</p></li>
<li><p><strong>短期 alpha 策略：</strong>想把更多毛利留给策略的人。</p></li>
<li><p><strong>想避免 funding流失的投机者：</strong>尤其在长期持仓会因 funding 被侵蚀的市场。</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

### 功能

1.  **账户与资金模式**

- **EOA钱包**：原生链上资金管理，USDC 作为唯一抵押。

- **账户抽象 (AA)**：支持原生钱包账户抽象，实现一键交易功能。

2.  **市场与仓位管理**

- **交易模式：**多仓，isolated margin

- **最大杠杆：**

  - **标准合约**：**5-500x（**Crypto）、**25x**（Equities）、**100x**（Indices）、**50-1000x**（FX）、**50-100x**（Commodities）、**50-100x**（Commodities）

  - **ZFP合约：**min **75x** ；max **250-1000x**

- **抵押物选择：**只支持USDC

- **订单类型：**Market，Limit，TP/SL。其中TP / SL受限于：

  - SL Price劣于current price 。**有min与max限制。max不能超过80%，min随杠杆动态调整。**

  - TP Price优于current price 。**有max限制，随杠杆动态调整：500x - 2125%；1000x - 2000%；57x - 2500%。**

  - Avantis 提供 **Guaranteed SL/TP（保证止损/止盈）**：对“处于亏损方向”的 SL（即保护本金的 SL）会被保证按你设置的价格成交（即使 oracle 当时有跳空）。但**TP 或在盈利内的 SL 是 limit 行为，不保证**。为保障高杠杆下keeper能及时执行，ZFP 在极高杠杆时对 SL 有最小允许深度（文档示例：**最小 SL 强制为 -30%（或依杠杆而变更）**），以确保 keeper 有“缓冲空间”执行。

  - UX：用户点击TPSL开关会自动填充max-1%。

  - <a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?usp=sharing" class="external-link" rel="nofollow">实测无法推断具体公式</a>

4.  **清算机制**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="50f30db273e49a869410dc0cf2694da20e99c8d6751389f0357f735bffee9187" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2015.05.02.png?version=1&amp;modificationDate=1759215926124&amp;cacheVersion=1&amp;api=v2" data-height="133" data-width="745" data-unresolved-comment-count="0" data-linked-resource-id="11010071" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 15.05.02.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="eaee855b-3463-4b4c-a823-b16a6e9f1f87" data-media-type="file" width="468" height="83" alt="Screenshot 2025-09-30 at 15.05.02.png" /></span>

- 没有MMR的概念。有效保证金比例掉到初始保证金80%以下触发清算。（动态。差不多相当于最大杠杆400x时，MMR跟我们相同1/500）。清算时keeper拿到15%的collateral作为激励。

### 参数表

#### **1. 费率**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="01b011a7-f7e8-4429-8746-36c15c053ff4">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>资产类别</strong></p></th>
<th class="confluenceTh"><p><strong>Open/Close Fee</strong></p></th>
<th class="confluenceTh"><p><strong>Loss Rebate</strong></p></th>
<th class="confluenceTh"><p><strong>Price Impact</strong></p></th>
<th class="confluenceTh"><p><strong>Borrow Fee</strong></p></th>
<th class="confluenceTh"><p><strong>备注 / 特性</strong></p></th>
<th class="confluenceTh"></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><a href="https://docs.avantisfi.com/trading/trading-fees-fixed-fee-perpetuals/crypto#dynamic-margin-fee" class="external-link" rel="nofollow">Crypto</a></p></td>
<td class="confluenceTd"><ul>
<li><p>Open： 4.5 bps</p></li>
<li><p>Close： 4.5 bps</p></li>
</ul></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="824026fbe3281f12a650f1d5f5b1f5fb7dc2b6cf218a6abfa212ccbbb70bed0b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2015.43.39.png?version=1&amp;modificationDate=1759218227848&amp;cacheVersion=1&amp;api=v2" data-height="81" data-width="454" data-unresolved-comment-count="0" data-linked-resource-id="10911795" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 15.43.39.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="3bc4f90c-20e2-4b18-9f26-3d4e017103fb" data-media-type="file" width="165" height="29" alt="Screenshot 2025-09-30 at 15.43.39.png" /></span>
<p>5% - 20% 的 net PnL</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="91c8dc9503771a2b0ecb507f7e6b05ce213111ac7ded82323c631166788303dd" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2015.50.42.png?version=1&amp;modificationDate=1759218670434&amp;cacheVersion=1&amp;api=v2" data-height="331" data-width="687" data-unresolved-comment-count="0" data-linked-resource-id="10944555" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 15.50.42.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="b4907c17-942e-4564-8df6-dcc9a310bac3" data-media-type="file" width="133" height="64" alt="Screenshot 2025-09-30 at 15.50.42.png" /></span>
<ul>
<li><p>BTC：0 spread</p></li>
</ul></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6224afecc79fb8d5485ae98c0f40e0899bbfc7fc701dc7c93fe84cf5a81c1515" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-30%20at%2015.52.21.png?version=1&amp;modificationDate=1759218842448&amp;cacheVersion=1&amp;api=v2" data-height="153" data-width="658" data-unresolved-comment-count="0" data-linked-resource-id="11010094" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-30 at 15.52.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="1d16ec66-e47a-4220-85bb-9b842f45c259" data-media-type="file" width="184" height="42" alt="Screenshot 2025-09-30 at 15.52.21.png" /></span>
<p>BaseFee 基于标的变动<br />
基于OI skew 与资产占用率utilization调整</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://docs.avantisfi.com/trading/trading-fees-fixed-fee-perpetuals/forex" class="external-link" rel="nofollow">FX</a></p></td>
<td class="confluenceTd"><ul>
<li><p>Open： 1 - 5 bps根据skew factor动态调整</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>USD-JPY: 10%</p></li>
<li><p>其他：0%</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>EUR-USD, USD-JPY, GBP-USD：0</p></li>
<li><p>其他对：1bps</p></li>
</ul></td>
<td class="confluenceTd"><p>BaseFee = 0.0015%/hr</p>
<p>公式同上</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://docs.avantisfi.com/trading/trading-fees-fixed-fee-perpetuals/commodities#dynamic-margin-fee" class="external-link" rel="nofollow">大宗</a></p></td>
<td class="confluenceTd"><ul>
<li><p>Open：6 - 8 bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><p>无</p></td>
<td class="confluenceTd"><ul>
<li><p>Open：2bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>BaseFee: Gold 0.0025%/hr；Silver 0.005%/hr；</p></li>
<li><p>波动性较高，margin fee 目标年化约 15%（30% util）</p></li>
</ul></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Indices (SPY, QQQ)</p></td>
<td class="confluenceTd"><ul>
<li><p>Open：6 bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><ul>
<li><p>Open：2bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>BaseFee 依据波动性设定</p></li>
<li><p>目标 5% APR（50% util）</p></li>
</ul></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Equities</p></td>
<td class="confluenceTd"><ul>
<li><p>Open：6 bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><p>10%</p></td>
<td class="confluenceTd"><ul>
<li><p>Open：5bps</p></li>
<li><p>Close：0</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>BaseFee 依据波动性设定</p></li>
<li><p>目标 5% APR（50% util</p></li>
</ul></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

#### **2. 风控**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="48c2a292-5899-4b6b-80b9-7149a1b15142">
<tbody>
<tr>
<th class="confluenceTh"><p>参数</p></th>
<th class="confluenceTh"><p><strong>实测/文档</strong></p></th>
<th class="confluenceTh"><p><strong>来源</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>Max Leverage</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>标准合约</strong>：<strong>5-500x（</strong>Crypto）、<strong>25x</strong>（Equities）、<strong>100x</strong>（Indices）、<strong>50-1000x</strong>（FX）、<strong>50-100x</strong>（Commodities）、<strong>50-100x</strong>（Commodities）</p></li>
<li><p><strong>ZFP合约：</strong>min <strong>75x</strong> ；max <strong>250-1000x</strong></p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max OI</p></td>
<td class="confluenceTd"><p><strong>Max OI = TVL × 90%</strong></p>
<ul>
<li><p>Max OI_{Crypto} = 70% × Max OI</p></li>
<li><p>Max OI_{Forex} = 15% × Max OI</p></li>
<li><p>Max OI_{Metals} = 15% × Max OI</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.avantisfi.com/trading/limitations" class="external-link" rel="nofollow">docs</a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Position Size</p></td>
<td class="confluenceTd"><ul>
<li><p>Max Position Size_{Crypto} = 15% × OI_{Crypto}</p></li>
<li><p>Max Position Size_{FX} = 15% × OI_{FX}</p></li>
<li><p>Max Position Size_{Metals} = 15% × OI_{Metals}</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Profit</p></td>
<td class="confluenceTd"><ul>
<li><p>根据不同市场有不同配置，1500%<a href="https://docs.avantisfi.com/trading/limitations" class="external-link" rel="nofollow">文档示例</a> 限制单仓最大盈利倍数</p></li>
<li><p><a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?usp=sharing" class="external-link" rel="nofollow">实测为随杠杆 &amp; 资产种类动态调整，非1500% 无法推断具体公式</a></p></li>
</ul></td>
<td class="confluenceTd"><p>合约没写具体参数</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Trades per Pair <strong></strong></p></td>
<td class="confluenceTd"><ul>
<li><p>单市场总订单数量 10（market + limit）</p></li>
<li><p>防 spam/DDOS，保护执行机器人</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Min Collateral</p></td>
<td class="confluenceTd"><ul>
<li><p>$10</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>Min Duration</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><ul>
<li><p>蓝筹，Meme，FX，贵金属没有，个别altcoin &amp; RAW受限</p></li>
<li><p>默认3 min, 头寸$5k+则10 mins，头寸50k+ 则 15min</p></li>
</ul></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"></td>
</tr>
<tr>
<td class="confluenceTd"><p>审计 &amp; 重大事件</p></td>
<td class="confluenceTd"><ul>
<li><p>未披露，但主打 <strong>无历史 LP 亏损</strong>（自 2024-08 起 LP share price 线性增长）。</p></li>
<li><p>当前运行数据：最大单日回撤仅 0.30%，无极端事件。</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

### Roadmap摘录

- **Zero-Fee Perps 扩容**：扩大到更多市场（目前仅 BTC、ETH、SOL）。

- **RWA 进一步接入**：更多外汇与商品。

- **风险分层机制完善**：提供更多 tranche 策略，吸引专业做市商。

- **跨链扩展**：与 GMX 类似，部署到多链，降低单链拥堵风险。

- **XP → AVNT 奖励**：Season 3 启动，未来空投和分配与 staking 强绑定。

- **提升 LP 资本效率**：更多资金再利用设计（composability）。

## 四、AsterDex

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

- **战略目标：永续合约版Polymarket。**通过自创**预测模型驱动高风险市场**（1001x），探索超高杠杆交易与**概率定价**机制。

- **战略重点：**通过创新的市场定价方式，吸引风险偏好高的用户，差异化竞争。

- **长远目标：**模型仍在验证阶段，可能发展为预测市场和合约市场的混合体，做到CEX做不到的高风险差异化路线，而不是单纯和 GMX/Avantis竞争。若验证失败，可能会是下一个pumpfun。

- **差异化竞争**：GMX、Avantis 走的是“稳健流动性 + 永续合约市场”的路线，Aster 则走更极端、更小众的玩法，形成生态差异化，而不是直接正面竞争。

</div>

</div>

### **协议模型**

**双模式**：Simple（AMM/ALP，极高杠杆 up to **1001×** 的一键订单）和 Pro（on-chain CLOB，低 maker/taker fee，丰富订单类型，支持 hidden orders、trailing stop、grid、post-only、TIF 等等）。Aster 强调以 Pro 吸引做市与机构，以 Simple 抓取高频散户流量。

Aster为CLOB模式，仅在功能上总结可参考点：

- **产品分层**（Simple vs Pro）能同时服务流量端与机构端；Pro 的低 maker fee + 丰富订单类型能吸引做市者，配套恰当的清算 / ADL（自动去杠杆）策略与市场容量限制。

- **押注性 /高风险预测 /短线博弈：**无开仓费，按盈亏收取平仓费（最低 0.03%），有 ROI 上限且不可追加保证金。 **Dumb 模式** 有固定时长交易（5–60 分钟），无开 & 平仓费，收益时才收费用。

- **FOMO情绪驱动型动线+投机式视觉语言：***1001x* 页面将极端杠杆展示、限时交易入口、跳动的数据通过视觉强化和即时反馈，引导用户快速进入交易行为。参与记录动态小窗设计强调 “紧迫感 + 投机感”，既展示市场活跃度，又能刺激用户模仿参与。**高风险交易场景界面游戏化**做的比Avantis好。

# To Do

1.  **Contract Spec**：确定 fee split比例、初始 open/close fee 档位（0.05/0.07），确定 funding period（hourly）。

2.  **HzLP Mechanism**：实现 isolated GM pool 模型 + borrow rate dual-slope 模块 + funding calculation（cumulative factors）。HzLP池设计 - 风险分层/隔离；可组合性；收益模块。

3.  **第三方合作：**建议机制跑通后与**ChaosLabs**谈合作，作为主要Risk Dashboard & 风控 & proposal review的第三方支持。

4.  **Governance**：治理提案权限（e.g. 调整 fee split，多链支持等）

5.  **M&O：**时间表，交易竞赛与referral具体规则，给出产品相关的运营需求等

6.  **细化参数：（如有需）**

    1.  **公开 docs 中常见情况**：很多项目（GMX / Jupiter / Aster / Avantis）会在 docs/whitepaper 中说明计算方法或宏观风控原则，但**具体的合约常数 / 限额（例如** maxPnlRateBPS**、**maxAUMPerMarket**、**weightToleranceBps**）通常是写在合约或 market config 中，而非高层说明文档**。所以要拿到确切数值需要做**合约字段抽取（repo grep + deployed address lookup）**或直接**从官方 audit PDF / repo releases 查找**。如果有这方面需求需要合约小伙伴配合。

    2.  **建议流程**：

        1.  **合约字段抽取（优先级高）** — 对 GMX、Aster、Avantis、Jupiter 的 repo / 或者已部署地址做逐行 grep，导出 CSV（字段：file,line,var_name,default_value,deployed_address,source_url）。

# 附录

## Table1 - 竞品战略洞察表格

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="34b267dd-8f7b-4f72-8639-cc6a2d33e3f1">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>项目</strong></p></th>
<th class="confluenceTh"><p><strong>战略 &amp; 定位</strong></p></th>
<th class="confluenceTh"><p><strong>产品矩阵</strong></p></th>
<th class="confluenceTh"><p><strong>关键量化指标</strong></p></th>
<th class="confluenceTh"><p><strong>Roadmap</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>Jupiter</p></td>
<td class="confluenceTd"><p>代表入口型协议，通过 「<strong>流动性聚合 + 多模态产品矩阵」</strong>，吸引大规模用户与项目方接入，但风控模型相对轻。</p>
<ul>
<li><p><strong>定位：</strong>Dex 中 Binance</p></li>
<li><p><strong>战略重点</strong>：</p>
<ul>
<li><p><strong>流动性模型：</strong>聚合流动性（RFQ + 路由）</p></li>
<li><p><strong>横向扩展策略：</strong>To C（用户）、To B（API）、To MM（做市）以多元化收入，生态孵化，降低对单一产品线依赖</p></li>
</ul></li>
<li><p><strong>USP：</strong></p>
<ul>
<li><p><strong>用户端和开发端双入口：</strong>零滑点最优路由 + 多模态产品 + 生态孵化<br />
-&gt; 把流量、发行方、留存绑在一起；增强 JUP 代币效用; liquidity flywheel</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>Swap、Perps、Lend、Loan、Launchpad、Stake、Portfolio、Mobile、Airdrop Checker、API</p></li>
<li><p>详见<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.1" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.1</a></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://community.chaoslabs.xyz/jupiter/risk/overview" class="external-link" rel="nofollow"><strong>TVL 2.4b, APR 13.2%, 30d liq volume 1.5b, 24h vol 640m</strong></a></p>
<ul>
<li><p><strong>资金-流量闭环：</strong>把 JLP 做成可持有的 <strong>收益 token</strong>，并且通过 staking / SOL staking / JLP Loans 等功能扩展收益路径；与 Solana 生态（做市商、RFQ、Jupiter Aggregator）深度绑定</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>横向扩展 增强风控 增强JUP代币效用</strong></p>
<ul>
<li><p><a href="https://coinmarketcap.com/cmc-ai/jupiter-perps-lp/latest-updates/" class="external-link" rel="nofollow"><strong><u>跨链 / 多链流动性网络（Jupnet / Omnichain Liquidity）</u></strong></a>：推出 “Jupnet Testnet” 或跨链网络，把 JLP 的流动性打通多条链（Solana → Ethereum / Base / Blast 等）</p></li>
<li><p><strong>更多 API / 基础设施扩展：</strong>基于 Metropolis API 平台继续向 Wallet / DeFi 应用开放更多接口。</p></li>
<li><p><strong>UX：</strong>提高移动端体验 / 钱包接入便捷性 / UI 流畅度，长期方向。</p></li>
<li><p><a href="https://feedback.jup.ag/roadmap" class="external-link" rel="nofollow"><strong><u>DAO提案推动优化：</u></strong></a>Roadmap 页面本身就是社区反馈平台，未来很多功能可能由社区票选 / 提案触发。</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p>GMX</p></td>
<td class="confluenceTd"><p>代表老牌成熟，精细风控协议<strong>「高流动性 + 动态费用 + 强治理」</strong> 模式，以 LP 安全为首。</p>
<ul>
<li><p><strong>定位</strong>：去中心化的 Binance Futures 替代品。</p></li>
<li><p><strong>战略重点</strong>：</p>
<ul>
<li><p><strong>流动性模型：</strong>GM (Isolated LP Pool) 隔离风险, PnL冲击限制 + GLV 聚合(multi-GM token Vault)</p>
<p>策略性流动性迁移, 集中度限制</p></li>
<li><p><strong>市场份额扩张：</strong>UX 优化 + 扩链 + 参数自治</p>
<p>+ 多链部署 (Arb, Sol, Botanix, Avax)</p></li>
<li><p>以深流动性、低费用、强风控在 DeFi 永续市场中占据主导地位</p></li>
</ul></li>
<li><p><strong>USP</strong>：</p>
<ul>
<li><p><strong>稳健的永续合约模型：</strong>动态风险控制 + 去中心化的参数治理<br />
-&gt; 精细风控</p></li>
<li><p>简化操作的Cross-collateral灵活抵押；高频友好的Gasless 交易；跨链流动性复用<br />
-&gt; 强资本效率</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>GLP (curated vault) + GM Pool (Isolated LP Pool)、Perps、治理/质押</p></li>
<li><p>详见<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B</a></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://community.chaoslabs.xyz/gmx-v2-arbitrum/risk/overview" class="external-link" rel="nofollow"><strong>TVL 470m, 24h fee income 13k, 24h Vol 18m.</strong></a></p>
<ul>
<li><p><strong>稳健式拉新：</strong>Referral program分 tier 的返佣/折扣，能带来持续的用户拉新，长期的 <strong>staking / esGMX vesting</strong> 机制把奖励锁在协议内。</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>优化UX 降低交易成本</strong></p>
<ul>
<li><p><strong>Gasless Transactions：</strong>用户免gas，由keeper 网络代发。</p></li>
<li><p><strong>Network Cost Subsidies</strong>：用部分平台收入补贴网络高峰期的 gas。</p></li>
<li><p><strong>Multichain 支持 + 虚拟账户</strong>：让用户跨链交易更便捷，不需要在每条链都部署新的 GMX 实例。</p></li>
<li><p><strong>Cross-collateral（交叉抵押）</strong>：允许用一种资产作为抵押，交易不同市场合约。</p></li>
<li><p><strong>Price Impact 收取变更</strong>：将 price impact 从开仓立刻扣改为平仓结算。</p></li>
<li><p><strong>净 OI 限制 (Net OI Cap)</strong>：在开仓的时候限制 net long vs short 的最大差额，以控制极端风险。</p></li>
<li><p><strong>引入 Kink Borrowing Rate</strong>：用“kink borrowing rate”模型，让日常借费较低，高需求时借费上升。</p></li>
<li><p><strong>风险分层GHV（仅社区提议）：</strong>仅收益于对手方亏损。自动反向建仓，对冲 Net OI。GM/GLV仅收益于手续费收入。</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p>Avantis</p></td>
<td class="confluenceTd"><p>代表新型衍生品设计，突出 「<strong>高杠杆交易激励+ LP 100%收入 + RWA市场</strong>」；吸引不同市场，保守以及激进用户</p>
<ul>
<li><p><strong>定位</strong>：去中心化 Kraken，聚焦 RWA 衍生品与高杠杆交易。</p></li>
<li><p><strong>战略重点</strong>：</p>
<ul>
<li><p>聚焦base链的RWA 市场拓展（外汇、大宗、股票）</p></li>
<li><p><strong>可扩展性：</strong>以费率差异化 (ZFP)以及100%分成 &amp; 可组合性yield吸引不同风险偏好的用户与 LP，同时逐步向多链 &amp; 多资产方向扩张。</p></li>
<li><p><strong>可组合性：</strong>LP mint <strong>USDC</strong>获得<strong>avUSDC</strong> (ERC-4626)<strong>。</strong>作为vault底层资产可以用于各种策略（借贷、staking、交易对冲等），vault 作为抽象层不对外暴露策略细节。</p></li>
</ul></li>
<li><p><strong>USP：</strong></p>
<ul>
<li><p>超高杠杆 + 差异化盈利抽成模型 + vAMM定价BTC大单零滑点 + LP 风险分层 + 损失返利 / 正滑点奖励<br />
-&gt; 成本优势吸引活跃的巨鲸/中长期用户</p></li>
<li><p>高杠杆＋多品类 + 灵活可组合收益的衍生品平台<br />
-&gt; 扩大市场边界，让不同风控偏好的资金流入</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>Perps (杠杆75+ ZFP &amp; 杠杆75- 正常) <strong>、</strong>vUSDC流动池、质押、Security Module（质押avnt至Liquidity Buffer）</p></li>
<li><p>详见<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.2" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.2</a></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://dune.com/restaji/avantis-base-perpetual-dex" class="external-link" rel="nofollow">Avantis - Dune</a></p>
<ul>
<li><p><strong>激进式拉新：</strong>binance alpha TGE；同时紧跟Trading XP、Liquidity XP 与 “Season” 制度，Claim Day 提供 Claim only 和 Claim + Stake（12小时内 35% boost） 两种选项来诱导 Day-1 锁仓。</p></li>
<li><p><strong>精准激励：</strong>交易，提供流动性，社区互动，生态互动，质押加成。<a href="https://x.com/AvantisFdn/status/1964176294997901733" class="external-link" rel="nofollow">线性模型且设有反洗交易限制。</a></p></li>
<li><p><strong>Day-1 流动性保证：</strong>与 CEX 上线时间同步释放一部分（9.25% 立即可交易 + 3.25% 可选 staking boost），短期造市成交与 TVL 放量。</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>扩大市场边界 完善机制 拉新留存活动</strong></p>
<ul>
<li><p><strong>avUSDC转变（ERC-4626）：</strong>战略层面靠向JUP，优化 LP 架构、收益来源、以及外部可组合性。<br />
-&gt; <a href="https://blog.bcas.io/ethereum-vaults-erc4626-under-mica" class="external-link" rel="nofollow">策略vault图示（非avantis）</a></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9187316785f647676885ff5fd77feba5c5bac513808a3ecb25957680a8250c56" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-09%20at%2018.12.00.png?version=1&amp;modificationDate=1760004799110&amp;cacheVersion=1&amp;api=v2" data-height="462" data-width="1069" data-unresolved-comment-count="0" data-linked-resource-id="14581965" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-09 at 18.12.00.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="6d0ccaee-5b22-4f60-baa2-b5694eed567e" data-media-type="file" width="236" height="102" alt="Screenshot 2025-10-09 at 18.12.00.png" /></span></p></li>
<li><p><strong>Zero-Fee Perps 扩容</strong>：扩大到更多市场（目前仅 BTC、ETH、SOL）。</p></li>
<li><p><strong>风险分层机制完善</strong>：提供更多 tranche 策略，吸引专业做市商。</p></li>
<li><p><strong>跨链扩展</strong>：与 GMX 类似，部署到多链，降低单链拥堵风险。</p></li>
<li><p><strong>XP → AVNT 奖励</strong>：Season 3 启动，未来空投和分配与 staking 强绑定。</p></li>
<li><p><strong>提升 LP 资本效率</strong>：更多资金再利用设计（composability）。</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p>Aster</p></td>
<td class="confluenceTd"><p>代表新型衍生品设计，突出 「<strong>双产品模式 + 隐私 + 多资产衍生 + RWA市场</strong>」；以趋近CEX体验的Pro吸引做市与机构，同时以极高杠杆，预测模型驱动的高风险Simple 抓高频散户流量。</p>
<ul>
<li><p><strong>定位：</strong>从构建基础设施(L1 + zk)及资本效率入手，建立一个底层生态与交易基础设施。</p></li>
<li><p><strong>战略重点：</strong></p>
<ul>
<li><p><strong>双模式</strong>：</p>
<ul>
<li><p>Simple（极高杠杆<strong>1001×</strong>的一键订单）</p></li>
<li><p>Pro（on-chain CLOB，低 maker/taker fee，支持 hidden orders、trailing stop、grid、post-only、TIF 等丰富订单类型）。</p></li>
</ul></li>
<li><p><strong>Trade &amp; Earn：</strong>Collateral Productive via asBNB / USDF 质押可用作抵押物交易，同时赚取被动收益</p></li>
</ul></li>
<li><p><strong>USP：</strong></p>
<ul>
<li><p><strong>差异化交易体验：</strong></p>
<ul>
<li><p>Simple：通过自创<strong>预测模型驱动高风险市场</strong>，探索超高杠杆交易与<strong>概率定价</strong>机制。<br />
-&gt; Degen及高频投机者</p></li>
<li><p>Pro： <strong>安全隐秘</strong>执行环境，多种类型订单支持。支持股票、指数、跨市场资产。<br />
-&gt; 大额 &amp; 机构 &amp; 隐私敏感交易者</p></li>
</ul></li>
<li><p><strong>自建高性能基础链：</strong>更低的交易成本、更灵活的衍生品支持 &amp; 协议控制权</p>
<p>→ 高资本效率, 隐私安全</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>Perps（1001x 极端杠杆的Simple模式 &amp; 近似中心化体验的Pro模式）、质押、现货</p></li>
<li><p>详见<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.3" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8D%8F%E8%AE%AE%E6%A8%A1%E5%9E%8B.3</a></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://dune.com/asterdex/aster-overview" class="external-link" rel="nofollow"><strong>370m</strong>首日交易量；<strong>330k</strong>新用户</a></p>
<ul>
<li><p><strong>爆发性拉新：</strong>TGE+高杠杆+强事件营销</p></li>
<li><p><strong>长期增长待验证：</strong>面临监管与用户损失舆情风险。需避免像pumpfun一样短期爆款后用户流失</p></li>
</ul></td>
<td class="confluenceTd"><p>机制与协议层面非竞品，调研部分未涵盖</p></td>
</tr>
</tbody>
</table>

</div>

## Table2 - 竞品参数配置表格

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="05141d88-255f-4dfc-bff5-e903106740b0">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p><strong>维度</strong></p></th>
<th class="confluenceTh"><p><strong>GMX V2</strong></p></th>
<th class="confluenceTh"><p><strong>Jupiter Perps</strong></p></th>
<th class="confluenceTh"><p><strong>Avantis</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>池子结构</strong></p></td>
<td class="confluenceTd"><p>多 GM 隔离池 + GLV聚合curated vault</p></td>
<td class="confluenceTd"><p>单 JLP 聚合池</p></td>
<td class="confluenceTd"><p>avUSDC单一LP池</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>交易模式</strong></p></td>
<td class="confluenceTd"><ul>
<li><p><strong>「账户」</strong>三种可选，由<a href="https://docs.gelato.cloud/relay/introduction/overview" class="external-link" rel="nofollow">Gelato Relay</a>第三方实现：</p>
<ul>
<li><p>Classic：链上签名，ETH付gas</p></li>
<li><p><a href="https://gelato.cloud/blog/how-gmx-eliminated-trading-friction-with-gelato-relay-a-case-study-in-next-gen-de-fi-ux" class="external-link" rel="nofollow">Express</a>：链下签名，链上keeper广播，gelato付费rpc</p></li>
<li><p>Express+1CT：多了一个账户抽象，能一键交易</p></li>
</ul></li>
<li><p><strong>「抵押」</strong>多资产抵押</p></li>
<li><p><strong>「执行模式」</strong>付gas Request → Keeper fulfill → Onchain execution</p></li>
<li><p><strong>「预言机」</strong>Chainlink （其他未表明）</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p><strong>「抵押」</strong>多资产抵押</p></li>
<li><p><strong>「执行模式」gasless</strong> Request → Keeper fulfill 并代付gas → Onchain execution</p></li>
<li><p><strong>「预言机」</strong>首选Edge by Chaos Labs + Chainlink &amp; Pyth辅助校验/回滚</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p><strong>「账户」</strong>两种可选，由Coinbase Smart Wallet实现：</p>
<ul>
<li><p>Classic</p></li>
<li><p>Smart Wallet：可支持一键交易</p></li>
</ul></li>
<li><p><strong>「抵押」</strong>USDC 单一资产抵押</p></li>
<li><p><strong>「执行模式」</strong><a href="https://docs.avantisfi.com/trading/trading-fees-fixed-fee-perpetuals/keeper-fees" class="external-link" rel="nofollow">付gas</a> Request → <strong>社区白名单</strong> Keeper fulfill → Onchain execution</p></li>
<li><p><strong>「预言机」</strong><a href="https://academy.binance.com/ru/articles/what-is-avantis-avnt" class="external-link" rel="nofollow">首选Pyth + Chainlink 辅助校验/回滚</a></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>最大杠杆</strong></p></td>
<td class="confluenceTd"><p><strong>100×</strong></p>
<ul>
<li><p>展示杠杆默认为<code>L = S / C</code>；可在设置中更改为浮动杠杆 <code>L = (S + PnL) / C</code></p></li>
<li><p>随池子 OI动态调整。OI增加，Max Lev下降。</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>100×</strong> (SOL)</p>
<p><strong>150×</strong> (ETH &amp; wBTC)</p></td>
<td class="confluenceTd"><p><strong>5-500x</strong> (Crypto)</p>
<p><strong>25x</strong> (Equities)</p>
<p><strong>100x</strong> (Indices)</p>
<p><strong>50-1000x</strong> (FX)</p>
<p><strong>50-100x</strong> (Commod)</p>
<ul>
<li><p><strong>ZFP</strong> (&gt;= 75x): <strong>250-1000x</strong></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Open/Close</strong></p></td>
<td class="confluenceTd"><p><strong>根据｜OI_diff｜动态选取，参数如下：</strong></p>
<p><strong>4 bps / 6bps</strong></p></td>
<td class="confluenceTd"><p><strong>6 bps</strong></p></td>
<td class="confluenceTd"><p><strong>4.5 bps</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Swap Fee Rate</strong></p></td>
<td class="confluenceTd"><p><strong>根据 |weight_diff| 动态选取。参数如下：</strong></p>
<p><strong>nst：5 / 7bps</strong><br />
<strong>st：0.5 / 2bps</strong></p></td>
<td class="confluenceTd"><p><strong>根据 |weight_diff| 动态加减。参数如下：</strong></p>
<p><strong>nst_swap：10 bps; st_swap：2 bps</strong></p>
<p><strong>nst_tax：500 bps; st_tax：50 bps</strong></p>
<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0281cece84cca0291eddbe6d472458a26172d8df6db05aa6f369b2829a1ae507" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-09%20at%2019.48.30.png?version=1&amp;modificationDate=1760010549926&amp;cacheVersion=1&amp;api=v2" data-height="435" data-width="1552" data-unresolved-comment-count="0" data-linked-resource-id="14974991" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-09 at 19.48.30.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="d65aa7ad-39ce-45dc-bad1-9ed214dc321a" data-media-type="file" width="173" height="48" alt="Screenshot 2025-10-09 at 19.48.30.png" /></span>
<ul>
<li><p><a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/calculate-swap-amount-and-fee.ts?utm_source=chatgpt.com" class="external-link" rel="nofollow">代码实现</a></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>单一抵押资产USDC；不涉及划转</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Price Impact</strong></p></td>
<td class="confluenceTd"><ul>
<li><p>指数模型<br />
<strong>Δ<sup>exp</sup> × factor</strong> 形式，exp=2</p></li>
<li><p>Price Impact Cap：<strong>50bps</strong></p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>分段线性 + 指数模型<br />
<strong>Δ<sup>exp</sup> × factor</strong> 形式</p></li>
<li><p>PriceCap：<strong>44bps</strong></p></li>
<li><p><a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/price-impact-fee.ts" class="external-link" rel="nofollow">代码实现</a></p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>指数 + 线性混合模型</p></li>
<li><p><code>Dynamic Spread = Constant Spread + Price Impact Spread + Skew Impact Spread</code></p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5d41c70499bbfb2e4d432312fec121dcdad91f8cdd1217a901d8a9c5856878fa" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-09%20at%2019.05.03.png?version=1&amp;modificationDate=1760008051993&amp;cacheVersion=1&amp;api=v2" data-height="841" data-width="807" data-unresolved-comment-count="0" data-linked-resource-id="14581975" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-09 at 19.05.03.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="e163b688-e796-4724-b46e-262e102c03ab" data-media-type="file" width="149" height="155" alt="Screenshot 2025-10-09 at 19.05.03.png" /></span></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Funding/Borrow</strong></p></td>
<td class="confluenceTd"><ul>
<li><p>Borrow：根据利用率分段线性模型</p></li>
<li><p>Funding：指数模型<br />
<strong>OI Imbalance<sup>exp</sup> × factor</strong></p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>Borrow：根据利用率线性收取<br />
<code>Hourly Borrow Fee = Total Tokens Locked / Tokens in Pool × Hourly Borrow Rate × Position Size</code></p></li>
<li><p>Funding：无。仅通过Price Impact激励OI重新平衡</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>Borrow：根据利用率及OI skew的分段曲线模型</p>
<p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1974471f91cf8bd23e0960ca2ee40ea0147c567b6905093343e071afad95aa84" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-10-09%20at%2019.28.11.png?version=1&amp;modificationDate=1760009339002&amp;cacheVersion=1&amp;api=v2" data-height="189" data-width="679" data-unresolved-comment-count="0" data-linked-resource-id="14811212" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-09 at 19.28.11.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="5f351849-6c3e-4efe-840b-762598964be7" data-media-type="file" width="149" height="41" alt="Screenshot 2025-10-09 at 19.28.11.png" /></span></p></li>
<li><p>Zero-fee + Rebate</p></li>
<li><p>Funding：不收费，针对<code>OI Skew &gt;= 55%</code>时返还 <a href="https://docs.avantisfi.com/rewards/loss-rebates" class="external-link" rel="nofollow">0%~20% Loss Rebate</a></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>清算机制</strong></p></td>
<td class="confluenceTd"><p>清算价格：通过保证金率计算 <code>(C + PnL - F) / S &lt; MMR</code></p>
<ul>
<li><p><strong>MMR: 0.4%-1%</strong> 根据市场不同配置</p></li>
<li><p><strong>清算后：</strong>剩余<strong>返还</strong></p></li>
<li><p><strong>清算费：</strong></p>
<ul>
<li><p>非合成（多仓储备即标的资产）：<strong>0.2%</strong></p></li>
<li><p>合成（多仓储备非标的资产）：<strong>0.3%</strong></p></li>
<li><p>高波动 / 新上市：<strong>0.45%</strong></p></li>
</ul></li>
<li><p><strong>ADL：</strong></p>
<ul>
<li><p><strong>全额储备：无ADL</strong>。因为有<code>Max OI = 90% Avlb Liq</code>的hard cap</p></li>
<li><p><strong>非全额储备：</strong><code>Total PnL / TVL &gt; maxPnlFactor</code>时针对盈利仓位</p></li>
<li><p>自动减仓。</p></li>
</ul></li>
</ul></td>
<td class="confluenceTd"><p>清算价格：通过保证金率计算 <code>(C + PnL - F) / S &lt; MMR</code></p>
<ul>
<li><p><strong>MMR：0.2%</strong></p></li>
<li><p><strong>清算后：</strong>剩余<strong>全部</strong>添加至JLP流动池，算作JLP收益</p></li>
<li><p><strong>清算费：100%</strong></p></li>
<li><p><strong>ADL：无</strong></p></li>
</ul></td>
<td class="confluenceTd"><p>清算价格：通过保证金变化比例 (Collateral Health Ratio) 计算 <code>(C + PnL - F) / C ≤ 80%</code></p>
<ul>
<li><p><strong>MMR: 动态</strong> <code>80% / L</code>。L为当前仓位lev，而非max lev</p></li>
<li><p><strong>清算后：</strong>剩余<strong>全部</strong>添加至Insurance Vault，用于支付交易者盈利。不算做LP收益，同时风险LP不必承担。</p></li>
<li><p><strong>清算费：15%给keeper</strong></p></li>
<li><p><strong>ADL：无</strong></p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>LP 收益 &amp; 风险</strong></p></td>
<td class="confluenceTd"><ul>
<li><p><strong>「收益」63%</strong> 协议收入</p></li>
<li><p><strong>「风险」</strong>隔离/组合可选</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p><strong>「收益」75%</strong> 协议收入</p></li>
<li><p><strong>「风险」</strong>单池共享</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p><strong>「收益」100%</strong> 协议收入 + 外部收益</p></li>
<li><p><strong>「风险」</strong>由vault buffer承担，超出部分由staker承担</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>LP保护</strong></p></td>
<td class="confluenceTd"><p><code>maxPnLFactor</code></p>
<ul>
<li><p><strong>「事前」</strong>限制 Trader 盈利上限</p></li>
<li><p>「<strong>Trader承担</strong>」由合约参数限制<strong>Trader</strong>最大计入AUM的盈利部分</p></li>
</ul></td>
<td class="confluenceTd"><ul>
<li><p>仅靠资金曲线和费用调节，协议层面<strong>没有</strong>引入额外保护机制，</p></li>
<li><p><strong>「LP</strong>直接承担」</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>Slashing</strong></p>
<ul>
<li><p><strong>「事后」</strong> LP 即时亏损 &gt;5%时，直接动用 AVNT 的质押资金事后补偿</p></li>
<li><p>「<strong>Staker承担</strong>」上限<code>Slashing Cap</code> = 20% 质押资产</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p>风控参数</p></td>
<td class="confluenceTd"><p><strong>“被动防御型”风控。限制单市场风险暴露与单用户风险集中，同时保护 LP免受大规模波动和集中化交易行为冲击。</strong></p>
<ul>
<li><p><strong>max OI：</strong><code>max OI = reserveFactor × poolSize</code></p></li>
<li><p><strong>reserveFactor：</strong>控制池中可借出/可交易占pool size比例。</p></li>
<li><p><strong>maxPnlFactor：</strong>控制 <code>PnL / Pool Worth</code> 的最大可计入比率上限（适用于 Traders / Deposits / Withdrawals）。限制未实现盈亏（uPnL）对 LP token 即时估值的冲击。</p></li>
<li><p><strong>minCollateralFactor：</strong>最低抵押率（<code>collateral / position size</code> 的最小比率）。防止过度杠杆与极端价格波动导致即时穿仓。</p></li>
<li><p><strong>maxPoolAmount：</strong>单市场可存入 token 的硬上限。防止单一资产在池中占比过高导致系统性风险。</p></li>
</ul></td>
<td class="confluenceTd"><p><strong>“动态平衡型”风控</strong>。仅<strong>维持池子健康权重</strong>，<strong>防止流动性单边流失,，以及防止执行队列阻塞</strong>。</p>
<ul>
<li><p><strong>Max OI：未表明</strong></p></li>
<li><p><strong>Max Position Size：2.5m</strong></p></li>
<li><p><strong>Limit Order Cap：</strong>数量上限20个，当池<code>utilization = locked / total &gt;=80%</code>时，限制新限价单</p></li>
<li><p><strong>MaxAUMusd: 3B</strong> JLP总计可存入 token美元价值的硬上限。</p></li>
<li><p><strong>tokenWeightageBufferBps：20%</strong> <a href="https://dev.jup.ag/docs/perp-api/pool-account" class="external-link" rel="nofollow">超出后不可添加/移除流动性</a></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>“主动约束型”风控</strong>。<strong>限制单市场风险暴露与单用户风险集中，同时防止价格操纵、滥用流动性与执行队列拥堵</strong></p>
<ul>
<li><p><strong>Max OI</strong></p>
<ul>
<li><p>Max OI = TVL × <strong>90%</strong></p></li>
<li><p>分配比例：</p>
<ul>
<li><p>Crypto：70% × Max OI</p></li>
<li><p>Forex：15% × Max OI</p></li>
<li><p>Metals：15% × Max OI</p></li>
</ul></li>
</ul></li>
<li><p><strong>Max Position Size</strong></p>
<ul>
<li><p>Crypto：15% × OI_Crypto</p></li>
<li><p>FX：15% × OI_FX</p></li>
<li><p>Metals：15% × OI_Metals</p></li>
</ul></li>
<li><p><strong>Max Profit</strong></p>
<ul>
<li><p>文档示例为 <strong>1500%</strong> 上限</p></li>
<li><p>实际为<strong>随杠杆与资产类型动态调整</strong>（非固定值）</p></li>
</ul></li>
<li><p><strong>Max Trades per Pair</strong></p>
<ul>
<li><p>每交易对最多 <strong>10 单</strong>（含 market + limit）用于防止 <strong>spam / DDOS</strong>，保护执行机器人</p></li>
</ul></li>
<li><p><strong>Min Collateral: $10</strong></p></li>
<li><p><strong>Min Duration</strong></p>
<ul>
<li><p>蓝筹、Meme、FX、贵金属：<strong>无下限</strong></p></li>
<li><p>个别 altcoin / RWA：有时间限制</p></li>
<li><p>规则：</p>
<ul>
<li><p>&lt; $5k：3 分钟</p></li>
<li><p>≥ $5k：10 分钟</p></li>
<li><p>≥ $50k：15 分钟</p></li>
</ul></li>
</ul></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>审计</strong></p></td>
<td class="confluenceTd"><ul>
<li><p><a href="https://raw.githubusercontent.com/gmx-io/gmx-contracts/master/audits/Quantstamp_Audit_Report.pdf" class="external-link" rel="nofollow">Quantstamp</a> ;</p></li>
<li><p><a href="https://github.com/gmx-io/gmx-synthetics/tree/main/audits" class="external-link" rel="nofollow">ABDK, Certora, Sherlock Dedaub, Guardian</a> 等</p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://dev.jup.ag/docs/misc/audits" class="external-link" rel="nofollow">每个产品线都有多重审计</a>，其中perps audit包含：</p>
<ul>
<li><p><a href="https://dev.jup.ag/assets/files/perpetual-offside-66183264a9656eef393cedfb0e2d5db1.pdf" class="external-link" rel="nofollow">Offside Labs</a></p></li>
<li><p><a href="https://dev.jup.ag/assets/files/perpetual-ottersec-573977253c463e70541dda93ac533d0b.pdf" class="external-link" rel="nofollow">OtterSec</a></p></li>
<li><p><a href="https://dev.jup.ag/assets/files/perpetual-sec3-cfbe25c6ce179ab95a84c2ffe93b5ac5.pdf" class="external-link" rel="nofollow">Sec3</a></p></li>
</ul></td>
<td class="confluenceTd"><p><a href="https://docs.avantisfi.com/security/audits" class="external-link" rel="nofollow">多家 audit：</a></p>
<ul>
<li><p>Zellic</p></li>
<li><p>Sherlock</p></li>
<li><p>Zokyo</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

## GMX **maxPnlFactor详解**

### 定义

- **maxPnlFactorForTraders**\
  → 限制 Trader 在仓位上最多能兑现多少未实现利润。\
  （比如设为 0.5，就算他赚了 100%，也只能兑现 50%）

- **maxPnlFactorForDeposits**\
  → 限制 LP / GLV 存入的资金在「价格剧烈波动」时，最多能累积多少未实现利润

- **maxPnlFactorForWithdrawals**\
  → 限制 LP / GLV 提出的资金在「价格剧烈波动」时，最多能兑现多少未实现利润

### MaxPnLFactor 施加 不同上限目的

- **目的 1（保护 LP 免受短期波动/操纵）**：未实现的、但非常大的 trader PnL（尤其是负向 PnL）会直接影响 market token 的即刻估值。如果按全量计价，LP 在 deposit 时可能因短期极端 PnL 被低估或高估。通过 cap，可以避免 deposit/withdraw 触发过度不利的估值移动。

- **目的 2（引导市场行为 / 激励）**：设置 `MAX_PNL_FACTOR_FOR_DEPOSITS` \< `MAX_PNL_FACTOR_FOR_WITHDRAWALS`（即 deposit 时对负面 PnL 施加更严格的 cap，使得 deposit 时价格更低）可以**人为制造“更便宜的入场吸引力”**，在高 pending PnL 时吸引存款来补偿风险。反之，withdrawals 用更宽松的 cap，能保护出金者。

- **目的 3（对交易者的制约）**：`MAX_PNL_FACTOR_FOR_TRADERS` 用来计算开/平仓时对市场代币的影响（例如当交易者的 PnL 被限制时，市场代币不会因为某些未实现收益立刻暴涨暴跌）。

合约不是“把全部 pending PnL 写进 pool worth”，而是 “先把 PnL 按场景施加系数上限，再计入池价值。这保证了在不同操作时，同一个 pending PnL 对价格的影响不同，从而达成上面的激励/保护目的。

### 为什么MAX_PNL_FACTOR_FOR_DEPOSIT \<=MAX_PNL_FACTOR_FOR_TRADERS

- 这个限制的作用是 **保证 GLV 和 Trader 的利润上限保持一致或更低，防止 GLV 存款人通过结构性差异薅 Trader 的羊毛**。

- 如果 `maxPnlFactorForDeposits > maxPnlFactorForTraders`：

  - Trader 的利润被限制住了（比如 50%）。

  - 但 GLV（资金池）却能在账面上记满利润（比如 100%）。

  - 这会造成「GLV 存款人」能套出超额利润，而这些利润的对手盘其实是 **Trader 的亏损**。

  - 但因为 Trader 的兑现受限 → 亏损并没有完全释放 → 可能形成不公平套利。

所以协议规定：必须保证`maxPnlFactorForDeposits <= maxPnlFactorForTraders`。这样GLV（资金池）最多只能拿到和 Trader 相同甚至更少的 PnL 因子。

## JPL Loan 计算规则

### 符号与约定（单位均为 USD 除非另注明）

- CC：用户当前抵押物 **JLP** 的美元价值（Collateral，USD）

- JJ：用户持有的 JLP token 数量（token）

- p_JLP：JLP 虚拟价格（virtual price，USD / JLP），p_JLP = AUM_usd / JLP_supply

- DD：用户当前未偿还债务（Debt，USD），包含本金与已计但未结算的利息

- LTV：Loan-to-Value，比值 LTV=D / C（无单位，0.83 表示 83%）

- LTV_max⁡：最大可借 LTV（launch 参数：0.83）

- LTV_liq：触发清算的 LTV（launch 参数：0.86）

- f_liq：清算罚金比例（launch：0.06）

- P\_{pool,USDC}：池中 USDC 的“理论可用总量 / 所有权”（用于计算 borrow cap）

- locked：被 Perps 锁定用于交易的 USDC（或“locked for trading”）

- borrowed_direct：已经被 JLP Loans 借走的 USDC 总量（direct borrows）

- u：利用率（utilization），定义见下

- 参数（利率曲线）：

  - r_min：最低年利率（decimal，例 0.00）

  - r_target：目标年利率（例 0.085）

  - r_max：最高年利率（例 0.15）

  - u_t：线性/跳跃阈值（示例使用 launch 推荐值 60%作例子）

### 关键计算公式

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ce36fef0c0ab79565d39e3a4fce65fa0bafbdd045d5fb1a58d997c51ad8a321c" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-26%20at%2011.38.32.png?version=1&amp;modificationDate=1758857996811&amp;cacheVersion=1&amp;api=v2" data-height="820" data-width="453" data-unresolved-comment-count="0" data-linked-resource-id="8126474" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-26 at 11.38.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="c04c51ac-7455-4d09-b37a-492c4dabc32e" data-media-type="file" width="468" height="847" alt="Screenshot 2025-09-26 at 11.38.32.png" /></span>

### **逐步流程**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4db2e7478196ac0ac44890efcfe2d92a2ab5c8ba8f053d1d8bd6163f8482776a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-26%20at%2011.39.04.png?version=1&amp;modificationDate=1758858092797&amp;cacheVersion=1&amp;api=v2" data-height="944" data-width="455" data-unresolved-comment-count="0" data-linked-resource-id="8257543" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-26 at 11.39.04.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="edbce7c8-1a8e-41dd-b7cc-44d4e5d4ba35" data-media-type="file" width="468" height="975" alt="Screenshot 2025-09-26 at 11.39.04.png" /></span>

### 逐步数值示例

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="42fdc82cf8f81c286cc321cc4c4401f7190b0c23db281637a5f5a19f852da7b6" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/6324231/Screenshot%202025-09-26%20at%2011.39.23.png?version=1&amp;modificationDate=1758858121122&amp;cacheVersion=1&amp;api=v2" data-height="948" data-width="418" data-unresolved-comment-count="0" data-linked-resource-id="8093719" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-26 at 11.39.23.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="6324231" data-linked-resource-container-version="38" data-media-id="2b3fb3b2-d253-4838-8eb4-b0f41ac3ffc3" data-media-type="file" width="468" height="1063" alt="Screenshot 2025-09-26 at 11.39.23.png" /></span>

## Avantis ZFP机制详解

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

传统模型（GMX、Gains、CEX）用**固定开/平/借贷/ funding** 收入来补偿 LP/做市方并覆盖尾部风险；

ZFP 则把收入从「固定即时费用」转为「**绩效型分成 + 动态价差 + （必要的）keeper/保障机制补偿**」。

</div>

</div>

### 交易生命周期 & 具体机制

1.  **开仓**

    - 你用 USDC 做抵押（Avantis 的 USDC vault 做为对手方/流动性来源）；开仓时没有固定开仓费/借贷费。开仓会受**动态价差 (dynamic spreads)** 的影响（与固定费模型一样存在价差/滑点）。

2.  **持仓期间**

    - **没有传统的借贷利息或持续 funding**：因为没有借贷费，持仓不会因时间产生“借贷腐蚀”从而改变清算价（对高杠杆尤为重要）。这也是 ZFP 强调“持仓时间不会改变清算价”的基础优点。

3.  **平仓 / 收费**

    - 平仓时如果**净亏损或零利润**：不收任何固定费用。

    - 平仓时如果**净盈利**：按“profit-sharing”抽成（滑动费率，ROI 越高你留得越多；文档示例最低可到 **2.5%**，并宣称平均交易者保留 **~80%+** 的利润）。换言之协议把盈利的一小部分作为服务费/LP 补偿。

4.  **止损 / 执行**

    - Avantis 提供 **Guaranteed SL/TP（保证止损/止盈）**：对“处于亏损方向”的 SL（即保护本金的 SL）会被保证按你设置的价格成交（即使 oracle 当时有跳空）。但**TP 或在盈利内的 SL 是 limit 行为，不保证**。为保障高杠杆下keeper能及时执行，ZFP 在极高杠杆时对 SL 有最小允许深度（文档示例：**最小 SL 强制为 -30%（或依杠杆而变更）**），以确保 keeper 有“缓冲空间”执行。

### **交易者 & LP的风险与权衡**

- **开仓/平仓/借贷费 = 0 减少跳空/滑点风险；保障止损（对亏损仓）**

  - 如果最终毛 PnL \< 0（你亏损），平台不收开平/借贷类固定费用 —— 也就是说亏损时只损失方向性亏损本身，不再被借贷费/开平手续费“蚕食”坏到更快爆仓。

  - Guaranteed SL 平仓或触发止损时使用链上 oracle + keeper 执行，极高杠杆（≥75x，最高 250x）本身放大了爆仓风险；ZFP 针对这类杠杆会强制最小 SL（例如 -30%），以增加keeper执行止损订单成功率。

- **只在盈利时抽成（win-fee）**

  - 平台在平仓盈利时按“毛利润”的比例抽取（文案中最低可到 **2.5%**，随 ROI 递减）。

- **LP风险控制**\
  当大量成功交易者持续盈利时，LP 收益依赖于 profit-sharing 与动态价差，可能承受“长期赢家”聚集带来的尾部风险。因此 Avantis 有分层/锁仓、周期分发等 LP 风控工具。

  - 目前只支持市场单（Limit later）。

  - 允许加保证金但禁止提取（防止滥用）。

  - 推荐通过 staking（\$AVNT）或后续策略减免 win-fee。

  - Beta 阶段随风险反馈可动态改参数（有可能恢复借贷费、时间后收费、force-close 等）。

### 量化示例（对应pnl calculator功能**）**

- 抵押（collateral） = \$100；杠杆 = 100x → 仓位规模 = \$10,000。

- 持仓时间 = 7 天。

- 固定费假设（Fixed-fee model）：开仓 0.06%、平仓 0.06%（合计 0.12% 的仓位规模） → 开平手续费合计 = \$12（\$10,000 \* 0.0012）。

- 借贷费 = 10% APR → 7 天借贷费 ≈ \$19.1781（\$10,000 \* 0.10 \* 7/365 ≈ \$19.1781）。

- 因此固定费用合计（开/平 + borrow） ≈ **\$31.1781**（这是 fixed model 在 7 天里对该仓位的全部成本示例）。

下面列出不同价格变动（对标仓位的 price move）下，ZFP 与 Fixed-fee 的净收益对比（ZFP 按不同 win-fee 比例算：2.5%、10%、20%）：

<div class="table-wrap">

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| Price move | Gross profit (@\$10,000 pos) | Fixed-fee net (Gross − \$31.1781) | ZFP net @2.5% | ZFP net @10% | ZFP net @20% |
| 0.10% | \$10.00 | −\$21.1781 | \$9.75 | \$9.00 | \$8.00 |
| 0.50% | \$50.00 | \$18.8219 | \$48.75 | \$45.00 | \$40.00 |
| 1.00% | \$100.00 | \$68.8219 | \$97.50 | \$90.00 | \$80.00 |
| 5.00% | \$500.00 | \$468.8219 | \$487.50 | \$450.00 | \$400.00 |

</div>

**解读：**

- 对于 **小幅波动（例如 0.1%–0.5%）**，ZFP 几乎总是优于固定费模型（即使 win-fee 是 20% 也仍显著更好），因为固定模型的借贷 + 开平费把小盈利吃掉甚至让交易亏损。

- 只有当你能实现非常大的单次收益，或者平台的 win-fee很高时，固定费模型在绝对数值上可能优于 ZFP（见下节的“break-even”计算）。

**Break-even（何时固定费比 ZFP 更划算）**\
设固定总成本 = C（此处≈ \$31.1781），gross profit = G，win-fee 率 = r，ZFP 净收益 = G\*(1−r)，Fixed-fee 净收益 = G − C。两者相等时：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
G*(1 − r) = G − C  →  G = C / r
```

</div>

</div>

代入我们数值，得到对不同 r 的临界 gross profit 与对应价格变动：

- r = 2.5% → 需要 **gross ≈ \$1,247.12** ⇒ price move ≈ **12.47%**

- r = 10% → gross ≈ \$311.78 ⇒ price move ≈ **3.12%**

- r = 20% → gross ≈ \$155.89 ⇒ price move ≈ **1.56%**

**含义**：如果 win-fee 低（例如 2.5%），你需要非常大的单笔收益（\>12%）才会被传统固定费用模型优于 ZFP。若 win-fee 高（20%），仅 ~1.56% 的价格移动就可能让固定费更好。

</div>
