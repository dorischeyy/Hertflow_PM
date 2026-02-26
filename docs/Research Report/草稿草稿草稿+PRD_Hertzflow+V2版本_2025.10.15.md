# 草稿草稿草稿 PRD_Hertzflow V2版本_2025.10.15

<div class="Section1">

<style>[data-colorid=sb6qbn1x7d]{color:#ff5630} html[data-color-mode=dark] [data-colorid=sb6qbn1x7d]{color:#cf2600}</style>版本号：V.2.0.0

需求人：cen

<style type="text/css">/**/
div.rbtoc1772008161896 {padding: 0px;}
div.rbtoc1772008161896 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772008161896 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772008161896">

- [一、需求概述](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-一、需求概述)
  - [1.1 交付产出](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-1.1交付产出)
- [二、竞品架构调研](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-二、竞品架构调研)
  - [2.1 模块分层(tech spec)](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.1模块分层(techspec))
  - [2.2 多隔离 LP 池（Multi-Isolated Liquidity Pools)](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.2多隔离LP池（Multi-IsolatedLiquidityPools))
    - [1. 资金流](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-1.资金流)
    - [2. GLV Router 分配逻辑](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.GLVRouter分配逻辑)
    - [3. GLV 的收益机制 & APR 说明](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.GLV的收益机制&APR说明)
    - [建池参数列表TODO：](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-建池参数列表TODO：)
    - [PnL 限制公式及取值](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-PnL限制公式及取值)
      - [逻辑：](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-逻辑：)
      - [公式：](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-公式：)
      - [实现：](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-实现：)
    - [风险管理（以avantis为例）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-风险管理（以avantis为例）)
      - [核心参数规律（按风险梯度）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-核心参数规律（按风险梯度）)
      - [风险层级](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-风险层级)
  - [2.3 RWA 资产市场逻辑](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.3RWA资产市场逻辑)
    - [RWA Oracle 数据来源](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-RWAOracle数据来源)
    - [市场开放与冻结规则](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-市场开放与冻结规则)
    - [收费明细](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-收费明细)
    - [风险管理（以avantis为例）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-风险管理（以avantis为例）.1)
  - [2.4 Curator / Market Creation 机制（参考 Morpho Curate）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.4Curator/MarketCreation机制（参考MorphoCurate）)
  - [2.5 Fee Structure / Key Params](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.5FeeStructure/KeyParams)
- [三、产品需求 (按协议+vault的情况来分类)](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-三、产品需求(按协议+vault的情况来分类))
  - [3.1 LP Pool](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.1LPPool)
    - [收益指标体系](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-收益指标体系)
    - [反映 LP Token 相对于基准（Uniswap V2 模式再平衡的 backing tokens）的收益差异。](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-反映LPToken相对于基准（UniswapV2模式再平衡的backingtokens）的收益差异。)
    - [每个 LP Vault 独立记录资产净值、未实现收益、PnLCap 限制：](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-每个LPVault独立记录资产净值、未实现收益、PnLCap限制：)
  - [3.2 自主建池（Curated Market Creation）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.2自主建池（CuratedMarketCreation）)
  - [3.3 Referral / 交易挖矿 / Leaderboard](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.3Referral/交易挖矿/Leaderboard)
  - [3.4 风险与边界处理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.4风险与边界处理)
- [二、竞品架构调研](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-二、竞品架构调研.1)
  - [2.1 模块分层](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.1模块分层)
  - [2.2 多隔离 LP 池（Multi-Isolated Vaults）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.2多隔离LP池（Multi-IsolatedVaults）)
    - [数据结构](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-数据结构)
    - [PnL 限制公式](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-PnL限制公式)
    - [风险管理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-风险管理)
  - [2.3 RWA 资产市场逻辑](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.3RWA资产市场逻辑.1)
    - [RWA Oracle 数据来源](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-RWAOracle数据来源.1)
    - [市场开放与冻结规则](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-市场开放与冻结规则.1)
    - [收费明细](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-收费明细.1)
  - [2.4 Curator / Market Creation 机制（参考 Morpho Curate）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.4Curator/MarketCreation机制（参考MorphoCurate）.1)
    - [流程](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-流程)
    - [Curator 权限](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-Curator权限)
    - [质押与惩罚](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-质押与惩罚)
  - [2.5 激励与费用系统](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.5激励与费用系统)
- [三、产品需求](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-三、产品需求)
  - [LP Pool](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-LPPool)
    - [三、收益指标体系](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-三、收益指标体系)
    - [四、📐 Ann. Performance 计算公式（年化表现）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-四、📐Ann.Performance计算公式（年化表现）)
    - [五、结算与风险机制](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-五、结算与风险机制)
  - [五、后端数据需求](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-五、后端数据需求)
    - [5.1 Indexer 事件监听](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-5.1Indexer事件监听)
    - [5.2 指标与统计字段](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-5.2指标与统计字段)
    - [5.3 API (GraphQL / REST)](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-5.3API(GraphQL/REST))
  - [六、前端功能与交互](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-六、前端功能与交互)
    - [三、核心模块设计](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-三、核心模块设计)
      - [1. 多隔离 LP 池架构](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-1.多隔离LP池架构)
      - [2. RWA 市场机制（参考 Avantis）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-2.RWA市场机制（参考Avantis）)
      - [3. 自主建池（Curated Market Creation）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-3.自主建池（CuratedMarketCreation）)
      - [4. Curator 权限与治理层级](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-4.Curator权限与治理层级)
      - [5. Referral / 交易挖矿 / Leaderboard](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-5.Referral/交易挖矿/Leaderboard)
      - [6. 费用模型（Fee Mechanics）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-6.费用模型（FeeMechanics）)
    - [四、关键公式举例](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-四、关键公式举例)
  - [6. LP & Funding Mechanism（流动性与资金费率机制）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-6.LP&FundingMechanism（流动性与资金费率机制）)
    - [6.1 LP 流动性管理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-6.1LP流动性管理)
      - [资金流向](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-资金流向)
    - [6.2 Funding 费率机制](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-6.2Funding费率机制)
      - [Funding Fee 分配逻辑](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-FundingFee分配逻辑)
    - [6.3 LP 风险敞口与监控](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-6.3LP风险敞口与监控)
  - [7. Liquidation Mechanism（清算机制）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-7.LiquidationMechanism（清算机制）)
    - [7.1 清算条件](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-7.1清算条件)
  - [9. Referral & Incentive（推荐与激励体系）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-9.Referral&Incentive（推荐与激励体系）)
    - [9.1 Referral 系统](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-9.1Referral系统)
    - [9.2 交易挖矿积分公式](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-9.2交易挖矿积分公式)
    - [9.3 奖励池来源](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-9.3奖励池来源)
  - [风险与边界处理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-风险与边界处理)
- [一、统一前提与命名约定](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-一、统一前提与命名约定)
- [Deposit（用户入金） — Trace Diagram（文本版）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-Deposit（用户入金）—TraceDiagram（文本版）)
  - [各方职责（按步骤）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-各方职责（按步骤）)
  - [关键失败场景与处理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-关键失败场景与处理)
  - [主要接口与事件（建议）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-主要接口与事件（建议）)
- [三、Withdraw（用户赎回） — Trace Diagram（文本版）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-三、Withdraw（用户赎回）—TraceDiagram（文本版）)
  - [各方职责（按步骤）](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-各方职责（按步骤）.1)
  - [关键失败场景与处理](#id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-关键失败场景与处理.1)

</div>

V2 Draft<a href="https://hertzflow.slack.com/team/U09837G5FB3" class="external-link" rel="nofollow">@cen</a> Todo：

- GLV机制（V2）

- RWA市场休市时间，以及休市跳空处理方式 验证avnt的k线图 （V2）

- Referral 积分系统机制 & Leaderboard梳理 （V2）

- 自主建池 产品层面参数自定义；协议层面 LP池，usdc - vault；GLV 关系梳理以及聚合/收入分配机制 （V3）

- Morpho Curate竞品调研 （V3）

- 其他细节填充

<a href="https://hertzflow.slack.com/team/U08H180TJ1J" class="external-link" rel="nofollow">@kayce</a> Todo：

- 2.1 部分的tech spec

- 2.2 部分跑代码刷风控参数 给出表格

# 一、需求概述

<div class="panel" style="background-color: #DEEBFF;border-width: 1px;">

<div class="panelContent" style="background-color: #DEEBFF;">

**版本目标：**V2 是基于 GMX V2 架构演化的多资产衍生品交易协议，目标是打造一个既能承载链上 DeFi 高杠杆衍生品，又能容纳链下 RWA（如美债、黄金、ETF）做市的混合型 DEX 平台。融合：

- **GMX V2 的多隔离池机制**（风险隔离 + 流动性聚合）

- **Avantis 的 RWA 交易**

- **GMX的动态费用调节**

- **Morpho Curate 的自主市场创建与治理体系（自主建池）**

- **结合 Jupiter/GMX/Avantis的 Referral、交易挖矿激励**

</div>

</div>

## 1.1 交付产出

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="642657ff-6389-4c13-9c42-c2a42d7e5314">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>模块</p></td>
<td class="confluenceTd"><p>核心功能</p></td>
<td class="confluenceTd"><p>关键参考</p></td>
<td class="confluenceTd"><p>是否包含</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/18710556/PRD_Hertzflow+V2+_2025.10.15#2.2-%E5%A4%9A%E9%9A%94%E7%A6%BB-LP-%E6%B1%A0%EF%BC%88Multi-Isolated-Vaults%EF%BC%89" rel="nofollow">多隔离池 LP</a></p></td>
<td class="confluenceTd"><p>每个市场单独池、风险隔离、个别清算，USDC池子支持。</p></td>
<td class="confluenceTd"><p>GMX V2</p></td>
<td class="confluenceTd"><p>✅</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>RWA 市场</p></td>
<td class="confluenceTd"><p>绑定真实资产 Oracle、开市时间与PnL约束、RWA-backed markets 链下收益同步与断层清算逻辑、</p></td>
<td class="confluenceTd"><p>Avantis</p></td>
<td class="confluenceTd"><p>✅</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>费用模型梳理</p></td>
<td class="confluenceTd"><p>Funding、Impact、Borrow、Swap<br />
<a href="https://hertzflow.slack.com/team/U08H180TJ1J" class="external-link" rel="nofollow">@kayce</a></p></td>
<td class="confluenceTd"><p>GMX / Jupiter</p></td>
<td class="confluenceTd"><p>✅ 合约主导，基于当前优化/新增<br />
修改：开单时前端权重偏差相关限制<br />
新增：funding fee新增；OI Imbalance相关的指数 Price Impact 奖惩</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>激励系统</p></td>
<td class="confluenceTd"><p>Referral ← 积分系统 ← 交易竞赛（leaderboard）等</p></td>
<td class="confluenceTd"><p>Jupiter / GMX Leaderboard</p></td>
<td class="confluenceTd"><p>✅ V2 出机制<br />
❌ V3出原型</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>自主建池 （V3）</p></td>
<td class="confluenceTd"><p>USDC 第三方策略LP池 - <strong>合作方</strong>自主创建市场 + Curator 白名单治理（合作方）</p></td>
<td class="confluenceTd"><p>Morpho Curate</p></td>
<td class="confluenceTd"><p>❌ V3再交付</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Curator 管理 （V3）</p></td>
<td class="confluenceTd"><p>多层权限：提案、审核、协议费用抽水分配</p></td>
<td class="confluenceTd"><p>Morpho Governance</p></td>
<td class="confluenceTd"><p>❌ V3再交付</p></td>
</tr>
</tbody>
</table>

</div>

# 二、竞品架构调研

## 2.1 模块分层(tech spec)

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | 功能 | 参考机制 |
| **VaultManager** | LP 池与资产管理 | GMX V2 |
| **MarketManager** | 市场参数与撮合控制 | GMX V2 |
| **RWAOracle （Offchain？）** | 真实资产价格与收益同步，与RWA托管方（Ondo, Maple等）对接 | Avantis |
| **CuratorRegistry** | 市场白名单与投票治理 | Morpho Curate |
| **RewardDistributor** | Referral 与挖矿奖励分发 | Jupiter |
| **RiskEngine** | PnL Cap 限制与资金费率计算 | GMX + Avantis |

</div>

## 2.2 多隔离 LP 池（Multi-Isolated Liquidity Pools)

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
                ┌─────────────────────────┐
                │        User Wallet      │
                │ (BTC / USDC / GM token) │
                └────────────┬────────────┘
                             │ deposit/Withdraw
                             │ mint/Burn GLV （ERC-4626)
                             ▼
                     ┌───────────────────────┐
                     │   GLV Vault           │
                     │ Long Collateral BTC   │
                     │ Short Collateral USDC │
                     └──────┬────────────────┘
                            │
            ┌───────────────┴──────────────────────────┐
            │                                          │
      ┌──────────────────────┐                  ┌────────────┐
      │ GM Router            │                  │ GLV Keeper │
      │ swap BTC/USDC <-> GM │◄──────trigger────│ (执行SHIFT)│
      └────┬─────────────────┘                  └────┬───────┘
           │                                         │
   ┌───────┴───────────────┐                ┌────────┴──────────────┐
   │ GM Pool A - Market A  │                │ GM Pool B - Market B  │
   │  Long Collateral BTC  │                │ Long Collateral BTC   │
   │ Short Collateral USDC │                │ Short Collateral USDC │
   └───────────────────────┘                └───────────────────────┘
  
```

</div>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="4a4772e0-b1f9-40ef-81d4-5beb446bad17">
<tbody>
<tr>
<th class="confluenceTh"><p>名称</p></th>
<th class="confluenceTh"><p>说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>GM Pool</strong></p></td>
<td class="confluenceTd"><p>针对某个市场的单池（比如 BTC/USD Pool)。用户质押 BTC（多头资产）+ USDC（空头资产），为交易者提供杠杆交易流动性, 获得 <strong>GM token</strong>。</p>
<ul>
<li><p>比如，GM Pool 1的token为：GM_BTC[BTC-USDC]，代表为BTC市场提供<strong>reserve token long = BTC；reserve token short = USDC</strong>的流动性池</p></li>
<li><p>比如，GM Pool 2的token为：GM_BTC[BTC-BTC]，代表为BTC市场提供<strong>reserve token long = BTC；reserve token short = BTC</strong>的流动性池</p></li>
<li><p>比如，GM Pool 3的token为：GM_BTC[tBTC-tBTC]，代表为BTC市场提供<strong>reserve token long = tBTC；reserve token short = tBTC</strong>的流动性池</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>GLV (GM Liquidity Vault)</strong></p></td>
<td class="confluenceTd"><p>由同样reserve token long（比如，ETH） 与short （USDC）的 <strong>GM Pool LP Token</strong>组成的聚合池，GLV 自动在这些 GM Pools 之间分配流动性。</p>
<ul>
<li><p><strong>GLV[BTC-USDC] = α × GM_BTC[BTC-USDC] + β GM_SOL[BTC-USDC] × GM_ETH[BTC-USDC] + γ × GM_SUI[BTC-USDC] + ...</strong><br />
其中 α、β、γ 是权重，由第三方动态调整。</p></li>
<li><p>权重调整逻辑：</p>
<ul>
<li><p>根据 <strong>各池收益率（APR）</strong>、<strong>利用率（utilization）</strong>、<strong>风险暴露（long/short imbalance）</strong> 等指标；</p></li>
<li><p>借助 GMX 的新功能 <strong>SHIFT()</strong>，GLV 可以在池子之间<strong>自动移动流动性</strong>（即卖掉部分 GM_BTC，买入 GM_ETH）。</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
用户（LP） 
   ├── 提供流动性到 GM Pool （Single market）  
   │       └─> GM Pool [long token A – short token B]  
   ├── 或 提供流动性到 GLV 池  
   │       └─> GLV Vault (long token A – short token B)  
   │             ├─> 底层 GM Pool 1  (market1, long A – short B)  
   │             ├─> 底层 GM Pool 2  (market2, long A – short B)  
   │             └─> 底层 GM Pool 3  (market3, long A – short B)  
   │             └─> 自动 Shift 机制：在 Pool1／Pool2／Pool3 之间再分配流动性  
   │  
   └── 第三方 USDC 本位 LP 池（Curator 管理）  
           └─> 池子向 GLV 或某 GM Pool 提供 USDC 流动性  
                   └─> 铸造 GLV Token 或 GM Token  
                         └─> Curator 管理、参与 收益／风险分配  
                         └─> 用户通过 Earn 参与该 策略池  
交易者 (Trader)
   ├── 在 某市场（GM Pool）开仓／平仓／Swap → 用此 GM Pool 的流动性  
   └── 交易产生的手续费、资金费、清算费等 

流动性池（GM Pool / GLV）  
   └─> 收益分配给 GM Token 持有人或 GLV Token 持有人  
  
协议／后台  
   ├── 定价机制（Token Price = 池子价值 ÷ 总供应）  
   ├── 再平衡机制（Shift）  
   └── 风险参数（如 maxPnlFactorForDeposits、glvMaxMarketTokenBalanceUsd）   
```

</div>

</div>

### 1. 资金流

- **入金（deposit）**：

  - 支持两种入金路径：直接 marketToken (直接计入目标 market 份额) 或 用基础 token（long/short）并在执行时通过 swap 路径兑换成 market token / 按策略分配。

  - Router：一个“分配模块”决定将 deposit 分配到 GLV 管理的哪些 market（按权重/策略/容量/实时深度）。分配逻辑通常基于：

    - 市场权重 (target allocation)

    - 当前市场利用率 / liquidity

    - 风险预算（每 market max exposure）

    - 资本效率（收益率、收益预测）

- **执行（executeGlvDeposit）**：

  - Keeper 读取 Deposit 请求并执行：可能包含多个 swap（根据 long/short path），或直接 mint marketToken -\> GLV份额给 receiver。

  - Router 会把实际收到的资金在多个 market 之间做拆分并调用各 market 的 deposit/mint 接口。

  - 执行延迟 & 异步：因为 deposit 是 “存储为请求，off-chain keeper 执行” 模式，UI 必须明确显示状态（Pending -\> Executed -\> Completed / Cancelled）。

  - Fee 透明度：executionFee 及任何 protocol fee（如 GLV mint fee、withdraw fee）需要在 UI 显示，并在事件中可追踪。

  - 风控展示：market exposure、maxPnlFactor、withdraw cooldown、队列长度、当前 oracle staleness 信息。

- **收益/再平衡（shift）**：

  - GLV 会定期或触发式对市场权重进行 shift（reallocate）以优化收益或降低风险（例如把过多暴露从高波动市场挪到稳健市场）。

- **赎回（withdraw）**：

  - 用户赎回 GLV -\> GLV 按比例从 underlying markets 收回资产，可能要跨多个市场 unwind 并执行 swap；使用 queue/epoch 模式可以缓解瞬时流动性冲击。

### 2. GLV Router 分配逻辑

> <a href="https://gov.gmx.io/t/implementation-of-gmx-liquidity-vaults-glv-for-enhancing-liquidity/3860?utm_source=chatgpt.com" class="external-link" rel="nofollow">GMX</a>官方文档与提案（事实可查但没有全部公式细节）

- 根据不同池子的：剩余可借；费用贡献；OI 自动调整:

  - 若某个 GM Pool 在该 GLV 组合中表现（例如交易量／手续费／借贷率／利用率）较低，则 GLV 可以将一部分流动性 “Shift” 到另一个表现更佳的 GM Pool（long/short token 相同前提下）。

  - Shift 时成本包括价格冲击（price impact）、手续费、滑点等。官方也提示存在攻击面（利用 Shift 机制、低利用率市场等）需通过配置 fees 和 price impact 等防范。 <a href="https://github.com/gmx-io/gmx-synthetics?utm_source=chatgpt.com" class="external-link" rel="nofollow">GitHub</a>

- 用户在 GLV 中存入 long 或 short token（或Long/Short Pair）后，其代币会被 GLV 用来铸造底层 GM Token（对应某个 GM Pool）或将其流动性提供给底层 GM Pools。用户收到 GLV 代币，代表其在 GLV 整体中的份额。

- 撤回时，用户选择GM池并赎回 GLV 代币， GLV 协议会从底层 GM Pools 移出相对应流动性并返回 long/short token 或 Token Pair。

- 存入/撤回收到max tvl cap，max buyable/sellable影响，同时sellable时的退回pair比例遵循池子long short token的pool size比例

- **Target weights + Dynamic caps**：

  - 每 market 定义 `targetWeight` 和 `maxCap`（以美元计）。

  - 新 deposit 按 targetWeight 尝试分配，若某个 market 达到 maxCap，则按剩余权重重分配。

- **Liquidity-aware routing**：

  - 在分配时查询 market depth & expected price impact（调用 on-chain 或 off-chain price feed），避免把大额 deposit 直接推向深度不足市场。

- **Emergency mode**：

  - 若 oracle staleness或某 market 被标记异常 -\> 暂停对该 market 分配（glv market disabled），并进入保护模式（freeze shift/withdraw 限制）。

### 3. GLV 的收益机制 & APR 说明

关于 GLV 收益（APR）的公开资料并不提供一个完整数学公式，但我们可以通过文档得出以下可查事实：

- GLV Virtual Price：GLV 代币价值随着其底层资产，以及其所持有的 GM Token（底层市场流动性份额）的总价值变化而变化。

  - GLV Token Price = GLV Pool Value / GLV Total Supply

  - GLV Pool Value = Sum of (USD Value of each Market Token owned by GLV)

- 衡量参数

  - `APR`: APR_pool ​= (Fees_pool_PeriodT/AvgTVL_PeriodT)×365/T​\
    其中，`AvgTVL_PeriodT` 为**加权平均**TVL

  - `APY`: APY_pool​ = (1+APR_pool_PeriodT)<sup>365/T</sup>​−1

  - `Ann. Perf`: Ann. Perf = (1 + APR_Pool) / (1 + APR_Bench) -1

    - 相比于一个 **Uniswap V2 风格的 LP（50/50，恒定乘积）,** 在价格从 p_0​ 变到 p_T​ 的过程中，**其资产总价值（以 quote token 计）** 会随价格变化的平方根增长, APR_bench_PeriodT = √(p_0​/p_T) - 1, APY_bench​=(1+R_bench_PeriodT)<sup>365/T​</sup>−1

### <span colorid="sb6qbn1x7d">建池参数列表TODO：</span>

任何人都能创建新市场，只要提供 **oracle feed、Base/Quote**，并设定 fee/leverage/funding 等参数。LP 也可 permissionless 提供流动性。

- 市场基础参数：base/quote、oracle、payoff provider

- 交易行为参数：可设 **fees、fundingInterval、settlementFee** 等，协议设 max 上限。

- 流动性启动：**virtualTaker** 缓冲，市场 operator 可自带初始 LP

- 费用参数：可设多类 fee（fundingFee、interestFee、positionFee、settlementFee, liquidation fee），但受 maxFee 限制。

- 风控参数：risk coordinator/operator 有权限管控，协议 enforce **maxFee、skew limits**。

- 权限：每个市场有独立 **operator** 以及**risk coordinator**( multisig+timelock)

新市场必须通过 **治理提案 (Proposal)**，需提供 **Base/Quote、oracle、IMR/MMR、funding params**。市场由 LP 提供流动性，但创建权不对用户开放。

- 市场基础参数：base/quote、oracle、reference price（oracle要求通过特定校验）

- 交易行为参数：可设**IMR**、**max lev**、**fees、impact notional**等，协议设 max 上限。

- 流动性启动：**预设模版，可选liquidity tier**

- 费用参数：funding fee、funding interval可通过proposal提议，其余走预设模版。

- 风控参数：根据liquidity tier自动计算，不可更改

- 权限：需lock治理代币 & 等批准

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a33ffca298d819a27ddee5493dd715e8e2f7be46fe998b7b8d5566f544d98e28" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/18710556/Screenshot%202025-09-12%20at%2014.28.31.png?version=2&amp;modificationDate=1761028723481&amp;cacheVersion=1&amp;api=v2" data-height="1690" data-width="842" data-unresolved-comment-count="0" data-linked-resource-id="21430324" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-12 at 14.28.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="18710556" data-linked-resource-container-version="4" data-media-id="c3e5cae8-ee3e-4a67-ac13-d3b75ccd18c2" data-media-type="file" width="468" height="936" alt="Screenshot 2025-09-12 at 14.28.31.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a33ffca298d819a27ddee5493dd715e8e2f7be46fe998b7b8d5566f544d98e28" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/18710556/Screenshot%202025-09-12%20at%2014.28.31.png?version=2&amp;modificationDate=1761028723481&amp;cacheVersion=1&amp;api=v2" data-height="1690" data-width="842" data-unresolved-comment-count="0" data-linked-resource-id="21430324" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-12 at 14.28.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="18710556" data-linked-resource-container-version="4" data-media-id="c3e5cae8-ee3e-4a67-ac13-d3b75ccd18c2" data-media-type="file" width="468" height="936" alt="Screenshot 2025-09-12 at 14.28.31.png" /></span>

### PnL 限制公式及取值

> 本质上是使Trader 的兑现能力受限，LP质押/移除流动性时LP token价格动态调整，给出时间窗口让市场恢复或给池子留缓冲。详解见 <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#GMX-maxPnlFactor%E8%AF%A6%E8%A7%A3" data-linked-resource-id="6324231" data-linked-resource-version="38" data-linked-resource-type="page">Research_竞品功能 &amp; 关键参数</a>

#### 逻辑：

以下三个操作时对应的参数，在实现上常对正向（盈利）与负向（亏损）采取不同策略：为了保护 LP，常对盈利更严格 cap，而对亏损允许更快释放（以保障亏损能真正补偿池子）。\

- `maxPnlFactorForTraders`：

  - 定义：限制单个 Trader 在仓位上“能从未实现收益里立刻兑现/影响池子估值”的**比例上限**。\
    eg：你赚了 100%，合约只允许把其中的一部分（比如 50%）算到可兑现价值里，让系统更稳健。

  - 保护市场GM代币估值免受仓位波动的瞬时冲击。

  - 防止某些极端未实现盈利在交易者平仓时造成池中代币短期暴涨暴跌（会伤害 LP）。

- `maxPnlFactorForDeposits`：（≤`maxPnlFactorForTraders` ）

  - 定义：限制在 deposit 时，LP/GLV 能把“未实现的价格波动带来的账面利润”以多大比例计入池子价值。目的是避免 deposit 时因为短期极端 PnL 导致 LP 把价格定得太高／低。

  - 更保守（常小于等于 traders）以避免进场资金在恶劣短期波动下被高估。

  - 能被用作激励参数（比如把 deposit 更严格设置，短期吸引人以更低价格进入或抑制不合理入金）。

- `maxPnlFactorForWithdrawals`：

  - 定义：限制在 withdrawal 时，LP/GLV 能兑现多少未实现利润，防止暴跌/暴涨时大规模提款导致不公平结算或被操纵。

  - 用来在极端波动下防止挤兑或短期套利。通常设置比 deposits 更宽松或相近，取决治理偏好（保护退出者还是保护池子长期健康）。

> 如果 `maxPnlFactorForDeposits > maxPnlFactorForTraders` 会发生的结构性套利：
>
> 1.  Trader 实际 pendingPnl = +1000。`maxPnlFactorForTraders = 0.5` → Trader 只能兑现 500
>
> 2.  假设 `maxPnlFactorForDeposits = 1.0`（即没有 cap）。
>
> 3.  GLV 在 deposit 时把全部 1000 计入池价值。于是 GLV 存款人账面上获得 1000，而实际能兑现的对手（Trader）只能兑现 500。差额 500 出自 Trader 的“受限兑现”——可能导致套利机会或不对称损益转移。

#### **公式：**\

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
maxPnlFactorForTraders        // 交易者限制
maxPnlFactorForDeposits       // 存入流动性限制
maxPnlFactorForWithdrawals。  // 移除流动性限制
 
 （下面只是举例）
 
                              // 1. 读取当前 positionNotional 与 pendingPnl（按仓位/aggregated）。
                              // 2. 根据操作类型选择相应 factor（trader/deposit/withdraw）。
                              // 3. recognizedPnl = sign(pendingPnl) * min(|pendingPnl|, factor * positionNotional)（或依据合约对负向 PnL 的特殊规则）。
                              // 4. 把 recognizedPnl 计入 poolWorth（或用于计算 mint/burn / token price）。
                              // 5. 执行剩余的结算逻辑（transfer、mint/burn GLV 等）。
```

</div>

</div>

#### 实现：\

- Trader 盈利出现 → 该盈利最初是` uPnL`（未实现盈亏）。

- 如果 Trader 选择平仓 → 合约会按 `maxPnlFactorForTraders` 的机制影响价格/池值（即会被 cap）。

- 若在 Trader 尚未平仓时出现外部操作（deposit/withdraw）：池子价值不把 Trader 的全部uPnl 直接当成可用资金。→ deposit/withdraw 时分别用 `maxPnlFactorForDeposits` / `maxPnlFactorForWithdrawals` 去衡量该 uPnl 在该操作场景下的“可被计入/兑现”比例。

<!-- -->

- GMX配置初始值（需 <a href="https://hertzflow.slack.com/team/U08H180TJ1J" class="external-link" rel="nofollow">@kayce</a> 辅助补充）：

  - `maxPnlFactorForTraders`：0.4 ~ 0.6（中性偏保守）

  - `maxPnlFactorForDeposits`：0.2 ~ 0.5（通常 ≤ traders）

  - `maxPnlFactorForWithdrawals`：0.4 ~ 0.8（根据要不要保护出金者）

- 动态调优建议：

  - 在波动性高时临时降低 depositFactor（减少新入资金承受的短期 PnL 风险）。

  - 在市场平稳时提高，改善流动性效率。

- 关键监控指标：（需 <a href="https://hertzflow.slack.com/team/U08FT22ST3M" class="external-link" rel="nofollow">@Easton 0x</a> 确认）

1.  `recognizedPnl / pendingPnl` 比例（按时间窗口、按 token）。

2.  deposit/withdraw 历史时序与对应 poolWorth 变动（看是否有套利痕迹）。

3.  平均持仓时间与平仓时的 recognizedPnl 与 pendingPnl 差距（衡量 cap 对 trader 的影响）。

4.  大额 deposit/withdraw 与市场波动的相关性（检测操纵）。

5.  GLV net inflow/outflow 在高 pendingPnl 时的行为。

### 风险管理（以avantis为例）

> <a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765" class="external-link" data-card-appearance="inline" rel="nofollow">https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765</a>

#### **核心参数规律（按风险梯度）**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="3c7f12fc-a05f-49b2-a662-761484d27ad9">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>参数</p></td>
<td class="confluenceTd"><p>高风险端</p></td>
<td class="confluenceTd"><p>低风险端</p></td>
<td class="confluenceTd"><p>备注</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_gain_percentage</strong></p></td>
<td class="confluenceTd"><p>2500（BTC/ETH/Meme）</p></td>
<td class="confluenceTd"><p>500（主流、山寨、RWA）</p></td>
<td class="confluenceTd"><p>止盈限制与市场信任度正相关。BTC/ETH/Meme 获高收益上限用于吸引活跃交易。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_sl_percentage</strong></p></td>
<td class="confluenceTd"><p>固定 80</p></td>
<td class="confluenceTd"><p>固定 80</p></td>
<td class="confluenceTd"><p>止损不能小于-80%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_long/short_oi_percentage</strong></p></td>
<td class="confluenceTd"><p>多为 50，少数 75–100</p></td>
<td class="confluenceTd"><p>多为 50，少数 75–100</p></td>
<td class="confluenceTd"><p>OI 统一口径设计，避免单边积聚；极个别FET、USD/TRY 等特例允许更高OI（100%）。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>group_open_interest_percentage</strong></p></td>
<td colspan="2" class="confluenceTd"><p>1–5（山寨） → 10–15（主流） → 30–100（RWA、大资产）<br />
-</p></td>
<td class="confluenceTd"><p>越高说明资产越被允许集中配置；体现对高流动性市场更高容忍度。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_wallet_oi_percentage</strong></p></td>
<td colspan="2" class="confluenceTd"><p>15（常规限制） → 50（高信任资产 / meme）<br />
-</p></td>
<td class="confluenceTd"><p>max positin size 低市值资产限制更严格</p></td>
</tr>
</tbody>
</table>

</div>

- **风险参数呈现单调规律：**

  - 从 “BTC/ETH → 主流 → 山寨 → RWA” 风险逐层下降，

  - 而 `max_gain_percentage`、`groupOI` 呈对应递减或分段。

- **特殊资产：**

  - **FET/USD**、**DELISTED_32/47**：设定为 `max_gain 500, OI 100%` → 内部特殊用途或测试市场。

  - **TRUMP/USD**、**BERA/USD** 等新兴政治/新链代币：保持 moderate 参数（max_gain 1000，groupOI 2–5）。

#### **风险层级**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="3957324c-e5de-4ed5-97f6-3daaa39076d0">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>风险层级</p></td>
<td class="confluenceTd"><p>包含资产</p></td>
<td class="confluenceTd"><p>参数特征</p></td>
<td class="confluenceTd"><p>层级逻辑</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L1：高流动性资产层</strong></p></td>
<td class="confluenceTd"><p>BTC, ETH</p></td>
<td class="confluenceTd"><p><code>max_gain 2500</code>, <code>groupOI 100</code>, <code>walletOI 50</code></p></td>
<td class="confluenceTd"><p>风险容忍高，高杠杆 + 高TP + 高敞口</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L2：主流资产层</strong></p></td>
<td class="confluenceTd"><p>SOL, SUI, BNB</p></td>
<td class="confluenceTd"><p><code>max_gain 500–2500</code>, <code>groupOI 2–15</code></p></td>
<td class="confluenceTd"><p>稳定流动性，中等风险。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L3：山寨资产层</strong></p></td>
<td class="confluenceTd"><p>ATOM, LINK, AVAX, OP 等</p></td>
<td class="confluenceTd"><p><code>max_gain 500</code>, <code>groupOI ≤5</code>, <code>walletOI 15</code></p></td>
<td class="confluenceTd"><p>风控最保守：TP与敞口都下调；适用于低流动性与波动资产。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L4：Meme 投机层</strong></p></td>
<td class="confluenceTd"><p>DOGE, PEPE, BONK, WIF, PUMP 等</p></td>
<td class="confluenceTd"><p><code>max_gain 2500</code>, <code>groupOI 5–10</code>, <code>walletOI 50</code></p></td>
<td class="confluenceTd"><p>波动极高，但Max Position 单户头寸限制收紧；群体敞口略小，偏向短线投机类资产。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L5：RWA 层</strong></p></td>
<td class="confluenceTd"><p>SPY, FX, GOLD 等</p></td>
<td class="confluenceTd"><p><code>max_gain 500–1000</code>, <code>groupOI 30–100</code>, <code>walletOI 15–50</code></p></td>
<td class="confluenceTd"><p>稳定收益，配置灵活；<br />
</p>
<ul>
<li><p>Equities &amp; Indices TP较高，敞口中等</p></li>
<li><p>FX 整体TP区间宽，部分USD/JPY 等高流动币对设更高groupOI。</p></li>
<li><p>Commod 属于对冲类资产，收益限制低但容许较高总仓敞口（便于跨市场套利）。</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

- `「Crypto」`**分层风险模型**

  - BTC/ETH等蓝筹 为 **顶层流动性层**：极高收益上限与最大OI限额。

  - Top10这种主流币为 **中层稳定层**：低收益上限、受限组OI。

  - 山寨币为 **底层高风险层**：严格敞口上限，收益受限。

  - Meme 为 **高波动特例层**：收益上限高，但通过 groupOI 控制总体暴露。

- `RWA` **体系分成三组：**

  - `Equity & Indices`（SPY, QQQ 等）：1000% 收益上限，中等 groupOI；

  - `FX`：分布 30–70%，说明流动性强、波动低；

  - `Commod`：groupOI 高达 100%，视作风险中性资产。

## 2.3 RWA 资产市场逻辑

### RWA Oracle 数据来源

- Chainlink + Pyth双源，\>5%偏差时合约拒绝交易。

- 更新频率：市场开放时间内，一般13:30 - 19:59 UTC （ET + 4），每60s/次。

- k线x轴不间断，无数据时间段隐藏。\

### 市场开放与冻结规则

<a href="https://docs.avantisfi.com/trading/market-hours" class="external-link" rel="nofollow">market open time跟着pyth network来</a> **（仅盘中，无盘前）**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a811fa32-d71c-437d-8a09-61b048fb119b">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>状态</p></td>
<td class="confluenceTd"><p>行为</p></td>
<td class="confluenceTd"><p>描述</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>marketOpen=true</p></td>
<td class="confluenceTd"><p>允许交易与清算</p></td>
<td class="confluenceTd"><p>正常交易窗口</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>marketOpen=false</p></td>
<td class="confluenceTd"><p>收盘后进入 “冻结结算” 状态，暂停下单与强平，PnL结算延后到下个开放窗口</p></td>
<td class="confluenceTd"><p>对应 TradFi 休市时间<br />
（包括盘前交易时间）</p></td>
</tr>
</tbody>
</table>

</div>

### 收费明细

> 详见: <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#%E5%8F%82%E6%95%B0%E8%A1%A8.2" data-linked-resource-id="6324231" data-linked-resource-version="38" data-linked-resource-type="page">Research_竞品功能 &amp; 关键参数</a>

<div class="table-wrap">

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| 类别 | 开仓费 (Opening Fee) | 平仓费 (Closing Fee) | 动态保证金费 (Dynamic Margin Fee) | 价差 (Spread) | 说明 |
| **Crypto (BTC/ETH)** | 4.5 bps | 4.5 bps | 基于 skew 与 utilization 动态计算 | Zero (BTC 无滑点) | 动态 Spread = 常数 + Price Impact + Skew Impact |
| **Forex** | 1–5 bps（取决于 skew） | 无 | 基于 skew 与利用率 | 0–1 bps | EUR-USD、USD-JPY、GBP-USD 为零价差 |
| **Metals (Gold, Silver)** | 6–8 bps | 无 | 目标 15% 年化（30% 利用率下） | 1–3 bps 固定 | 按波动率与 skew 调整 |
| **Commodities** | 6–8 bps | 无 | 与 Metals 相同 | 1–3 bps | 固定价差模式 |
| **Indices (SPY, QQQ)** | 6 bps | 无 | 目标 5% 年化（50% 利用率下） | 1 bp 平均 | 固定 Spread 0.01% |
| **Equities (MAG7, COIN)** | 6 bps | 无 | 目标 10% 年化（50% 利用率下） | 2.5 bps 平均 | 固定 Spread 0.025% |

</div>

### 风险管理（以avantis为例）

1.  **核心参数规律**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="37611d08-33d8-4e26-bbe3-b3ec12fa32c4">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>参数</p></td>
<td class="confluenceTd"><p>高风险端</p></td>
<td class="confluenceTd"><p>低风险端</p></td>
<td class="confluenceTd"><p>备注</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_gain_percentage</strong></p></td>
<td class="confluenceTd"><p>2500（BTC/ETH/Meme）</p></td>
<td class="confluenceTd"><p>500（主流、山寨、RWA）</p></td>
<td class="confluenceTd"><p>止盈限制与市场信任度正相关。BTC/ETH/Meme 获高收益上限用于吸引活跃交易。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_sl_percentage</strong></p></td>
<td class="confluenceTd"><p>固定 80</p></td>
<td class="confluenceTd"><p>固定 80</p></td>
<td class="confluenceTd"><p>止损不能小于-80%</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_long/short_oi_percentage</strong></p></td>
<td class="confluenceTd"><p>多为 50，少数 75–100</p></td>
<td class="confluenceTd"><p>多为 50，少数 75–100</p></td>
<td class="confluenceTd"><p>OI 统一口径设计，避免单边积聚；极个别FET、USD/TRY 等特例允许更高OI（100%）。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>group_open_interest_percentage</strong></p></td>
<td colspan="2" class="confluenceTd"><p>1–5（山寨） → 10–15（主流） → 30–100（RWA、大资产）<br />
-</p></td>
<td class="confluenceTd"><p>越高说明资产越被允许集中配置；体现对高流动性市场更高容忍度。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>max_wallet_oi_percentage</strong></p></td>
<td colspan="2" class="confluenceTd"><p>15（常规限制） → 50（高信任资产 / meme）<br />
-</p></td>
<td class="confluenceTd"><p>max positin size 低市值资产限制更严格</p></td>
</tr>
</tbody>
</table>

</div>

- **风险参数呈现单调规律：**

  - 从 “BTC/ETH → 主流 → 山寨 → RWA” 风险逐层下降，

  - 而 `max_gain_percentage`、`groupOI` 呈对应递减或分段。

- **特殊资产：**

  - **FET/USD**、**DELISTED_32/47**：设定为 `max_gain 500, OI 100%` → 内部特殊用途或测试市场。

  - **TRUMP/USD**、**BERA/USD** 等新兴政治/新链代币：保持 moderate 参数（max_gain 1000，groupOI 2–5）。

2.  **风险层级**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="856617e8-87b2-471f-9d07-f74557b1cfa6">
<tbody>
<tr>
<td class="confluenceTd"><p>风险层级</p></td>
<td class="confluenceTd"><p>包含资产</p></td>
<td class="confluenceTd"><p>参数特征</p></td>
<td class="confluenceTd"><p>层级逻辑</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L1：高流动性资产层</strong></p></td>
<td class="confluenceTd"><p>BTC, ETH</p></td>
<td class="confluenceTd"><p><code>max_gain 2500</code>, <code>groupOI 100</code>, <code>walletOI 50</code></p></td>
<td class="confluenceTd"><p>风险容忍高，高杠杆 + 高TP + 高敞口</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L2：主流资产层</strong></p></td>
<td class="confluenceTd"><p>SOL, SUI, BNB</p></td>
<td class="confluenceTd"><p><code>max_gain 500–2500</code>, <code>groupOI 2–15</code></p></td>
<td class="confluenceTd"><p>稳定流动性，中等风险。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L3：山寨资产层</strong></p></td>
<td class="confluenceTd"><p>ATOM, LINK, AVAX, OP 等</p></td>
<td class="confluenceTd"><p><code>max_gain 500</code>, <code>groupOI ≤5</code>, <code>walletOI 15</code></p></td>
<td class="confluenceTd"><p>风控最保守：TP与敞口都下调；适用于低流动性与波动资产。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L4：Meme 投机层</strong></p></td>
<td class="confluenceTd"><p>DOGE, PEPE, BONK, WIF, PUMP 等</p></td>
<td class="confluenceTd"><p><code>max_gain 2500</code>, <code>groupOI 5–10</code>, <code>walletOI 50</code></p></td>
<td class="confluenceTd"><p>波动极高，但Max Position 单户头寸限制收紧；群体敞口略小，偏向短线投机类资产。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L5：RWA 层</strong></p></td>
<td class="confluenceTd"><p>SPY, FX, GOLD 等</p></td>
<td class="confluenceTd"><p><code>max_gain 500–1000</code>, <code>groupOI 30–100</code>, <code>walletOI 15–50</code></p></td>
<td class="confluenceTd"><p>稳定收益，配置灵活；</p>
<ul>
<li><p>Equities &amp; Indices TP较高，敞口zhong deng</p></li>
<li><p>FX 整体TP区间宽，部分USD/JPY 等高流动币对设更高groupOI。</p></li>
<li><p>Commod 属于对冲类资产，收益限制低但容许较高总仓敞口（便于跨市场套利）。</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

- `「Crypto」`**分层风险模型**

  - BTC/ETH等蓝筹 为 **顶层流动性层**：极高收益上限与最大OI限额。

  - Top10这种主流币为 **中层稳定层**：低收益上限、受限组OI。

  - 山寨币为 **底层高风险层**：严格敞口上限，收益受限。

  - Meme 为 **高波动特例层**：收益上限高，但通过 groupOI 控制总体暴露。

- `RWA` **体系分成三组：**

  - `Equity & Indices`（SPY, QQQ 等）：1000% 收益上限，中等 groupOI；

  - `FX`：分布 30–70%，说明流动性强、波动低；

  - `Commod`：groupOI 高达 100%，视作风险中性资产。

## 2.4 Curator / Market Creation 机制（参考 Morpho Curate）

流程

1.  用户提交 createMarketProposal

2.  Curator节点投票（\>⅔同意） → 调用 approveMarket()

3.  系统部署新Vault & Market合约

Curator 权限\

<div class="table-wrap">

|                |                                    |
|----------------|------------------------------------|
| 权限等级       | 能力                               |
| Admin Curator  | 批准/冻结市场，修改全局参数        |
| Senior Curator | 审核提案，调整PnL Cap或Funding参数 |
| Junior Curator | 提供Oracle评审与数据签名           |

</div>

质押与惩罚\

- 创建者需质押 \$CURATE token\$

- 若市场出现Oracle操纵、异常PnL超限，则扣除质押

## 2.5 Fee Structure / Key Params

> 详见：<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#Table2---%E7%AB%9E%E5%93%81%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE%E8%A1%A8%E6%A0%BC" data-linked-resource-id="6324231" data-linked-resource-version="38" data-linked-resource-type="page">Research_竞品功能 &amp; 关键参数</a>

协议层（Gmx V2） + Vault层（Morpho）\

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="bf593943-bc54-45da-8fb2-dd86627ae23f">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>参数类型</p></td>
<td class="confluenceTd"><p>计算方式</p></td>
<td class="confluenceTd"><p>调整逻辑</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Open/Close Fee Rate</strong></p></td>
<td class="confluenceTd"><p><strong>4 bps / 6bps</strong></p></td>
<td class="confluenceTd"><p><strong>多空头寸偏差 ｜OI_diff｜动态调节或选取</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Swap Fee</p></td>
<td class="confluenceTd"><p>基础费率 + 动态滑点<br />
<strong>GMX</strong><br />
</p>
<ul>
<li><p><strong>nst：5 / 7bps</strong></p></li>
<li><p><strong>st：0.5 / 2bps</strong><br />
</p></li>
</ul>
<p><strong>JUP</strong><br />
</p>
<ul>
<li><p><strong>nst_swap：10 bps; st_swap：2 bps</strong></p></li>
<li><p><strong>nst_tax：500 bps; st_tax：50 bps</strong></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>池子权重偏差 |weight_diff| 动态调节或选取 -</strong> <a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/calculate-swap-amount-and-fee.ts?utm_source=chatgpt.com" class="external-link" rel="nofollow"><strong>代码实现</strong></a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Price Impact Fee</p></td>
<td class="confluenceTd"><ul>
<li><p>指数模型 （GMX）<br />
<strong>Δ^exp × factor</strong> 形式，exp=2</p></li>
<li><p>分段线性 + 指数模型 （JUP）</p></li>
<li><p>TODO：<br />
<strong>Δ^exp × factor</strong> 形式</p></li>
<li><p>Price Impact Cap：<strong>50bps</strong></p></li>
</ul></td>
<td class="confluenceTd"><p><strong>根据多空头寸偏差｜OI_diff｜动态调节 - JUP</strong><a href="https://github.com/julianfssen/jupiter-perps-anchor-idl-parsing/blob/main/src/examples/price-impact-fee.ts" class="external-link" rel="nofollow"><strong>代码实现</strong></a></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Funding/Borrow Fee</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Funding/Borrow (Jup 无funding）</strong></p></li>
<li><p>Borrow：根据利用率分段线性模型</p></li>
<li><p>Funding：指数模型 <strong>Δ^exp × factor</strong> 形式<strong>（根据多空头寸偏差｜OI_diff｜动态调节 - GMX）</strong></p></li>
<li><p>Funding：不收费，针对<code>OI Skew &gt;= 55%</code>时返还 <a href="https://docs.avantisfi.com/rewards/loss-rebates" class="external-link" rel="nofollow">0%~20% Loss Rebate</a> （Avnt）</p></li>
</ul></td>
<td class="confluenceTd"><p>多空不平衡度 × funding_rate_window；根据 pool imbalance 实时调节</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidation Fee</p></td>
<td class="confluenceTd"><p>固定 + 动态（随杠杆）</p></td>
<td class="confluenceTd"><p>向LP池返还</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>RWA Carry Fee（）</p></td>
<td class="confluenceTd"><p>若LP资产配置RWA，收益分成x%</p></td>
<td class="confluenceTd"><p>自动复投或回购代币</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Max Lev</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>100×</strong> (SOL)<br />
<strong>150×</strong> (ETH &amp; wBTC)<br />
<strong>5-500x</strong> (Crypto)<br />
<strong>25x</strong> (Equities)<br />
<strong>100x</strong> (Indices)<br />
<strong>50-1000x</strong> (FX)<br />
<strong>50-100x</strong> (Commod)</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>清算机制</p></td>
<td class="confluenceTd"><p>GMX<br />
</p>
<ul>
<li><p>清算价格：通过保证金率计算 <code>(C + PnL - F) / S &lt; MMR；</code><strong>MMR: 0.4%-1%</strong> 根据市场不同配置</p></li>
<li><p><strong>清算后：</strong>剩余<strong>返还</strong></p></li>
<li><p><strong>清算费：</strong><br />
非合成（多仓储备即标的资产）：<strong>0.2%</strong><br />
合成（多仓储备非标的资产）：<strong>0.3%</strong><br />
高波动 / 新上市：<strong>0.45%</strong></p></li>
<li><p><strong>ADL：</strong><br />
<strong>全额储备：无ADL</strong>。因为有<code>Max OI = 90% Avlb Liq</code>的hard cap<br />
<strong>非全额储备：</strong><code>Total PnL / TVL &gt; maxPnlFactor</code>时针对盈利仓位</p></li>
</ul>
<p>AVNT<br />
</p>
<ul>
<li><p>清算价格：通过保证金变化比例 (Collateral Health Ratio) 计算 <code>(C + PnL - F) / C ≤ 80%</code></p></li>
<li><p><strong>MMR: 动态</strong> <code>80% / L</code>。L为当前仓位lev，而非max lev</p></li>
<li><p><strong>清算后：</strong>剩余<strong>全部</strong>添加至Insurance Vault，用于支付交易者盈利。不算做LP收益，同时风险LP不必承担。</p></li>
<li><p><strong>清算费：15%给keeper</strong><br />
</p></li>
</ul></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>风控参数</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

Zokyo

# 三、产品需求 (按协议+vault的情况来分类)

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="ae0f8d59-9453-4319-9a85-d0a306593f43">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>模块</p></td>
<td class="confluenceTd"><p>功能</p></td>
<td class="confluenceTd"><p>对应机制</p></td>
<td class="confluenceTd"><p>收益来源</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Isolated Pool（隔离池）</strong><br />
GMX v2</p></td>
<td class="confluenceTd"><p>单一市场对应的 GM Pool（如 ETH/USD）</p></td>
<td class="confluenceTd"><p>独立 Vault，独立风险与资金利用率</p></td>
<td class="confluenceTd"><p>Funding、Borrow、Trading Fee</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Aggregated Pool（聚合池 / GLV）</strong></p></td>
<td class="confluenceTd"><p>自动聚合多个 GM Pool，按风险权重动态平衡</p></td>
<td class="confluenceTd"><p>GLV Vault（GMX v2 原生结构）</p></td>
<td class="confluenceTd"><p>各 GM Pool 的平均年化</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Curator Whitelist Pool</strong></p></td>
<td class="confluenceTd"><p>由第三方策略管理（需白名单许可）</p></td>
<td class="confluenceTd"><p>独立 USDC Vault，执行 RWA/DeFi 策略</p></td>
<td class="confluenceTd"><p>RWA Coupon + GMX LP收益</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>RWA-backed Reserve Vault</strong></p></td>
<td class="confluenceTd"><p>低风险国债等实物资产抵押</p></td>
<td class="confluenceTd"><p>可抵押稳定币 (USDC / tBill / sDAI)</p></td>
<td class="confluenceTd"><p>外部固定收益</p></td>
</tr>
</tbody>
</table>

</div>

## 3.1 LP Pool

### 收益指标体系

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="4c856011-634f-44b1-998c-9909eb81c96d">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>指标</p></td>
<td class="confluenceTd"><p>含义</p></td>
<td class="confluenceTd"><p>计算逻辑</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Fee APY</strong></p></td>
<td class="confluenceTd"><p>实际基于协议费用（swap + funding + borrow）的年化收益</p></td>
<td class="confluenceTd"><p>来自链上 fee accruals</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Ann. Performance</strong></p></td>
<td class="confluenceTd"><h3 id="id-草稿草稿草稿PRD_HertzflowV2版本_2025.10.15-反映LPToken相对于基准（UniswapV2模式再平衡的backingtokens）的收益差异。">反映 LP Token 相对于基准（Uniswap V2 模式再平衡的 backing tokens）的收益差异。</h3></td>
<td class="confluenceTd"><p>?</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>LP Price</strong></p></td>
<td class="confluenceTd"><p>Pool 份额单价，反映资产与负债变化</p></td>
<td class="confluenceTd"><p>LP Price = (Total Assets - Liabilities) / Supply</p></td>
</tr>
</tbody>
</table>

</div>

### 每个 LP Vault 独立记录资产净值、未实现收益、PnLCap 限制：

资金流向\

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 事件 | LP 行为 | 资产变化 |
| Deposit | 增加流动性 | totalLiquidity += amount |
| Withdraw | 减少流动性 | 触发结算（若有未实现PnL） |
| Swap/Borrow |  |  |
| RWA Yield | RWA 收益分配 | vault.totalLiquidity += vault.rwaExposure \* yield |

</div>

## 3.2 自主建池（Curated Market Creation）

**流程（类似 Morpho Curate）**：\

1.  用户申请新市场（指定标的、抵押、杠杆、Oracle源）。

2.  系统进入 “Proposal” 状态，Curator 节点投票或白名单批准。

3.  若批准，自动部署对应 Vault + MarketConfig 合约。

4.  Pool 初始化时需：

- 设置初始 Target Weight

- 配置 Oracle 数据源

- 绑定 Fee 模型与风险参数

**参数约束：**\

- 初始池需 ≥ 100K USD TVL

- 标的需在 whitelisted_oracles 内

- Creator 需抵押 Curator Token 或质押治理代币

Curator 权限与治理层级\

<div class="table-wrap">

|                   |                            |                        |
|-------------------|----------------------------|------------------------|
| 角色              | 权限                       | 示例                   |
| **Admin Curator** | 审批/撤销市场              | 官方治理委员会         |
| **Curator Node**  | 评审市场风险，提议参数变更 | DAO 节点或专业做市机构 |
| **Creator**       | 发起市场创建提案           | 用户或机构             |
| **Reviewer**      | 提供数据/Oracle验证        | 白名单数据提供方       |

</div>

**激励：**\

- 审核奖励（按交易量分配）

- Curator Token 奖励与声誉值增长

- 违规或错误决策将扣除质押

## 3.3 Referral / 交易挖矿 / Leaderboard

- **Referral 结构**：二级分润，支持绑定UID。

- **交易挖矿模型**：

  - 每日交易量积分计算：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
score = volume_usd * weight_asset * fee_multiplier
```

</div>

</div>

- 每周排行榜发奖（参考 Jupiter 的 Leaderboard）

- **奖励形式**：

  - 平台代币

  - Vault Fee Rebate

  - NFT 徽章或治理权投票权

## **3.4 风险与边界处理**

<div class="table-wrap">

|                   |                    |
|-------------------|--------------------|
| 场景              | 处理方式           |
| Oracle断层 \>120s | 暂停市场，冻结清算 |
| RWA 市场关闭      | 延迟PnL结算        |
| PnL超Cap          | 强制裁剪并记录事件 |
| Funding异常       | 回退至上次有效值   |
| Curator滥权       | DAO投票回滚提案    |

</div>

# 二、竞品架构调研

## 2.1 模块分层

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | 功能 | 参考机制 |
| **VaultManager** | LP 池与资产管理 | GMX V2 |
| **MarketManager** | 市场参数与撮合控制 | GMX V2 |
| **RWAOracle （Offchain？）** | 真实资产价格与收益同步，与RWA托管方（Ondo, Maple等）对接 | Avantis |
| **CuratorRegistry** | 市场白名单与投票治理 | Morpho Curate |
| **RewardDistributor** | Referral 与挖矿奖励分发 | Jupiter |
| **RiskEngine** | PnL Cap 限制与资金费率计算 | GMX + Avantis |

</div>

## 2.2 多隔离 LP 池（Multi-Isolated Vaults）

### 数据结构

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
struct VaultConfig {           // 每个市场对应一个/多个独立LP Vault
    address baseAsset;         // 标的资产，如BTC, GOLD, FX
    address collateralToken;   // 抵押资产, 如USDC, USDT, BTC, SUI
    uint256 pnlCapRatio;       // 最大可分配PnL上限（如20%）
    uint256 fundingRateK;      // Funding费率参数
    uint256 imbalanceThreshold;// Funding触发阈值
    bool isRWA;                // 是否为RWA池
    address rwaOracle;         // 若为RWA，关联的Oracle
    uint256 rwaCarryRate;      // RWA收益年化
}
```

</div>

</div>

### PnL 限制公式

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 最大盈利上限 = LP净值 * pnlCapRatio
maxPnL = vault.totalValue * vault.pnlCapRatio;
if (traderPnL > maxPnL) traderPnL = maxPnL;
updateBalances(trader, pnl);
```

</div>

</div>

> **Rationale**：防止Oracle延迟或极端波动下LP净值被单一交易榨干。

### 风险管理

- 每个池的持仓方向独立计算 Funding。

- 若多空持仓失衡度超过 10%，动态上调 Funding 费率。

<div class="table-wrap">

|                    |                |         |
|--------------------|----------------|---------|
| 参数               | 示例值         | 来源    |
| fundingRateK       | 0.0001 (0.01%) | GMX v2  |
| pnlCapRatio        | 0.20 (20%)     | Avantis |
| imbalanceThreshold | 0.10 (10%)     | GMX v2  |

</div>

## 2.3 RWA 资产市场逻辑

### RWA Oracle 数据来源

1.  Chainlink + Pyth双源，\>5%偏差时合约拒绝交易。

2.  仅针对盘中

### 市场开放与冻结规则

<a href="https://docs.avantisfi.com/trading/market-hours" class="external-link" rel="nofollow">market open time跟着pyth network来</a>

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 状态 | 行为 | 描述 |
| `marketOpen=true` | 允许交易与清算 | 正常交易窗口 |
| `marketOpen=false` | 收盘后进入 “冻结结算” 状态，暂停下单与强平，PnL结算延后到下个开放窗口 | 对应 TradFi 休市时间 |

</div>

### 收费明细

<div class="table-wrap">

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| 类别 | 开仓费 (Opening Fee) | 平仓费 (Closing Fee) | 动态保证金费 (Dynamic Margin Fee) | 价差 (Spread) | 说明 |
| **Crypto (BTC/ETH)** | 4.5 bps | 4.5 bps | 基于 skew 与 utilization 动态计算 | Zero (BTC 无滑点) | 动态 Spread = 常数 + Price Impact + Skew Impact |
| **Forex** | 1–5 bps（取决于 skew） | 无 | 基于 skew 与利用率 | 0–1 bps | EUR-USD、USD-JPY、GBP-USD 为零价差 |
| **Metals (Gold, Silver)** | 6–8 bps | 无 | 目标 15% 年化（30% 利用率下） | 1–3 bps 固定 | 按波动率与 skew 调整 |
| **Commodities** | 6–8 bps | 无 | 与 Metals 相同 | 1–3 bps | 固定价差模式 |
| **Indices (SPY, QQQ)** | 6 bps | 无 | 目标 5% 年化（50% 利用率下） | 1 bp 平均 | 固定 Spread 0.01% |
| **Equities (MAG7, COIN)** | 6 bps | 无 | 目标 10% 年化（50% 利用率下） | 2.5 bps 平均 | 固定 Spread 0.025% |

</div>

## 2.4 Curator / Market Creation 机制（参考 Morpho Curate）

#### 流程

1.  用户提交 `createMarketProposal`

2.  Curator节点投票（\>⅔同意） → 调用 `approveMarket()`

3.  系统部署新Vault & Market合约

#### Curator 权限

<div class="table-wrap">

|                |                                    |
|----------------|------------------------------------|
| 权限等级       | 能力                               |
| Admin Curator  | 批准/冻结市场，修改全局参数        |
| Senior Curator | 审核提案，调整PnL Cap或Funding参数 |
| Junior Curator | 提供Oracle评审与数据签名           |

</div>

#### 质押与惩罚

- 创建者需质押 \$CURATE token\$

- 若市场出现Oracle操纵、异常PnL超限，则扣除质押

## 2.5 激励与费用系统

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 类型 | 说明 | 计算逻辑 |
| Funding Fee | 防止多空失衡 | ( FR = k \times \frac{OI\_{long}-OI\_{short}}{OI\_{total}} ) |
| Price Impact Fee | 大额滑点费 | ( F = base + α×(\frac{Δpos}{liq})^2 ) |
| Liquidation Fee | 强平补偿 | 固定 + 动态（杠杆相关） |
| Referral 奖励 | 二级结构（L1/L2） | 交易费 × rebate% |
| RWA Carry Fee | RWA池年化收益分成 | vault配置 × rwaCarryRate |

</div>

# 三、产品需求

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 模块 | 功能 | 对应机制 | 收益来源 |
| **Isolated Pool（隔离池）** | 单一市场对应的 GM Pool（如 ETH/USD） | 独立 Vault，独立风险与资金利用率 | Funding、Borrow、Trading Fee |
| **Aggregated Pool（聚合池 / GLV）** | 自动聚合多个 GM Pool，按风险权重动态平衡 | GLV Vault（GMX v2 原生结构） | 各 GM Pool 的平均年化 |
| **Curator Whitelist Pool** | 由第三方策略管理（需白名单许可） | 独立 USDC Vault，执行 RWA/DeFi 策略 | RWA Coupon + GMX LP收益 |
| **RWA-backed Reserve Vault** | 低风险国债等实物资产抵押 | 可抵押稳定币 (USDC / tBill / sDAI) | 外部固定收益 |

</div>

## LP Pool

### 三、收益指标体系

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 指标 | 含义 | 计算逻辑 |
| **Fee APY** | 实际基于协议费用（swap + funding + borrow）的年化收益 | 来自链上 fee accruals |
| **Ann. Performance** | 池子净值变化的年化表现（含 unrealized PnL） | 见下方公式 |
| **LP Price** | Pool 份额单价，反映资产与负债变化 | LP NAV = (Total Assets - Liabilities) / Supply |

</div>

------------------------------------------------------------------------

### 四、📐 Ann. Performance 计算公式（年化表现）

**定义：**\
Annualized Performance 反映 LP Token 相对于基准（Uniswap V2 模式再平衡的 backing tokens）的收益差异。

\[\
AnnPerformance = \left( \frac{NAV\_{t} / NAV\_{0}}{Benchmark\_{t} / Benchmark\_{0}} - 1 \right) \times \frac{365}{Days}\
\]

其中：

- ( NAV\_{t} )：当前 LP Pool 的净资产值；

- ( Benchmark\_{t} )：模拟 Uniswap V2 50/50 再平衡组合；

- ( Days )：所选时间周期（30/90/180D）。

该指标 ≠ Fee APY。\
👉 Fee APY 仅计费收益（swap、funding、borrow）；\
👉 Ann Performance 则计入 LP 的实际价格变化与交易者 PnL 暴露。

------------------------------------------------------------------------

### 五、结算与风险机制

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 场景 | 机制描述 | 合约逻辑 |
| **Close Market** | 市场停盘或下架时，LP 资产按最后结算价清算并分配 | `closePosition()` & `settleMarket()` |
| **Gap / 跳空结算** | 使用 oracle 的 TWAP 保护价，LP 先行承担 PnL，再由保险基金补偿 | 参考 GMX `PriceImpactReserve` |
| **Liquidation** | 若交易者头寸亏损超过抵押比，LP 池获得清算溢价 | `executeLiquidation()` 自动结算 |
| **Funding & Borrow 调整** | 定时更新长短仓平衡，计算资金费与借款费 | Keeper 每小时更新 Funding Index |

</div>

## 五、后端数据需求

### 5.1 Indexer 事件监听

<div class="table-wrap">

|                     |                                 |          |
|---------------------|---------------------------------|----------|
| 事件                | 字段                            | 用途     |
| `VaultCreated`      | poolId, asset, oracle           | 新池索引 |
| `PositionOpened`    | trader, size, entryPrice        | 交易统计 |
| `PositionClosed`    | trader, pnl, fees, block        | 收益计算 |
| `OracleUpdated`     | asset, price, yield, marketOpen | RWA监控  |
| `RewardDistributed` | address, amount, reason         | 激励统计 |

</div>

### 5.2 指标与统计字段

<div class="table-wrap">

|                        |                       |
|------------------------|-----------------------|
| 指标                   | 含义                  |
| `pool_imbalance_ratio` | 多空持仓比例          |
| `funding_fee_accrued`  | 当前Funding累积值     |
| `rwa_yield_annualized` | LP端RWA收益年化       |
| `trader_pnl_capped`    | 已应用PnL上限后的收益 |
| `curator_vote_ratio`   | 市场提案投票通过率    |

</div>

### 5.3 API (GraphQL / REST)

- `GET /pools/{id}`\
  → 返回池状态、PnLCap、FundingRate、RWA参数

- `GET /leaderboard`\
  → 排名、积分、奖励

- `POST /proposal`\
  → 提交自主建池提案

- `GET /oracle/{asset}`\
  → 实时RWA价格与收益率

## 六、前端功能与交互

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | 功能 | 描述 |
| **Trading Interface** | 交易、开平仓、杠杆设定、PnL实时显示 | 动态展示Funding/Impact费率、RWA收益提示 |
| **Liquidity Panel** | 添加/移除流动性，查看Vault净值、PnL上限 | 支持RWA池年化收益展示 |
| **Curator Dashboard** | 审核市场提案、投票、查看声誉积分 | 拟用Table + Modal交互 |
| **Referral / Leaderboard** | 绑定推荐关系、查看积分与排名 | 对接后端积分系统 |
| **RWA Oracle Monitor** | 实时显示RWA资产价格与状态（open/close） | 提示清算冻结状态 |
| **Analytics Dashboard** | 汇总资金曲线、PnL分布、Funding历史 | 可导出CSV |

</div>

### 三、核心模块设计

#### 1. 多隔离 LP 池架构

**逻辑：**\
每个交易市场（BTC/USD、ETH/USD、Gold/USD、USDC/T-Bill等）对应独立的 **Isolated LP Vault**。\
LP在池内提供流动性，并独立承担该市场的PnL风险。

**关键参数：**

<div class="table-wrap">

|                       |                            |
|-----------------------|----------------------------|
| 参数                  | 含义                       |
| `pool_id`             | 唯一市场ID                 |
| `base_asset`          | 标的资产（BTC/ETH/Gold等） |
| `collateral_token`    | 抵押资产（USDC/USDT/RWA）  |
| `max_pnl_cap`         | 单池可分配最大PnL限制      |
| `funding_rate_window` | Funding计算周期            |
| `price_impact_curve`  | 动态滑点与费率模型         |

</div>

**风控机制：**

- 每个池单独跟踪 `long_short_imbalance_ratio`

- 超过阈值时动态上调 `funding_fee_bps`

- LP 端可查看风险敞口热力图

------------------------------------------------------------------------

#### 2. RWA 市场机制（参考 Avantis）

<div class="table-wrap">

|  |  |
|----|----|
| 模块 | 设计细节 |
| **Oracle 来源** | 优先使用 Chainlink / Pyth / 专有 API；对于RWA类（如T-Bills、Gold），采用带签名的 TradFi 数据源。 |
| **价格更新频率** | 至少每分钟更新一次；价格间断时交易冻结。 |
| **PnL 结算** | 若市场关闭时仍有持仓，采用最近可得价格进行结算；若价格断层 \>2σ，PnL 按滑点折减系数计算。 |
| **市场开放时间** | 遵守对应标的的现实交易时间（例如美债09:30–16:00 EST）。 |
| **清算逻辑** | 断价期间不得清算；复盘后以Oracle平滑值清算。 |
| **RWA 托管** | 对接合规RWA协议（Maple, Backed, Ondo）；LP 池资产可部分配置至真实收益资产。 |

</div>

------------------------------------------------------------------------

#### 3. 自主建池（Curated Market Creation）

**流程（类似 Morpho Curate）**：

1.  用户申请新市场（指定标的、抵押、杠杆、Oracle源）。

2.  系统进入 “Proposal” 状态，Curator 节点投票或白名单批准。

3.  若批准，自动部署对应 `Vault + MarketConfig` 合约。

4.  Pool 初始化时需：

    - 设置初始 Target Weight

    - 配置 Oracle 数据源

    - 绑定 Fee 模型与风险参数

**参数约束：**

- 初始池需 ≥ 100K USD TVL

- 标的需在 `whitelisted_oracles` 内

- Creator 需抵押 Curator Token 或质押治理代币

------------------------------------------------------------------------

#### 4. Curator 权限与治理层级

<div class="table-wrap">

|                   |                            |                        |
|-------------------|----------------------------|------------------------|
| 角色              | 权限                       | 示例                   |
| **Admin Curator** | 审批/撤销市场              | 官方治理委员会         |
| **Curator Node**  | 评审市场风险，提议参数变更 | DAO 节点或专业做市机构 |
| **Creator**       | 发起市场创建提案           | 用户或机构             |
| **Reviewer**      | 提供数据/Oracle验证        | 白名单数据提供方       |

</div>

**激励：**

- 审核奖励（按交易量分配）

- Curator Token 奖励与声誉值增长

- 违规或错误决策将扣除质押

------------------------------------------------------------------------

#### 5. Referral / 交易挖矿 / Leaderboard

- **Referral 结构**：二级分润，支持绑定UID。

- **交易挖矿模型**：

  - 每日交易量积分计算：

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
    score = volume_usd * weight_asset * fee_multiplier
    ```

    </div>

    </div>

  - 每周排行榜发奖（参考 Jupiter 的 Leaderboard）

- **奖励形式**：

  - 平台代币

  - Vault Fee Rebate

  - NFT 徽章或治理权投票权

------------------------------------------------------------------------

#### 6. 费用模型（Fee Mechanics）

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 费用类型 | 计算方式 | 调整逻辑 |
| Funding Fee | 多空不平衡度 × funding_rate_window | 根据 pool imbalance 实时调节 |
| Price Impact Fee | Δ仓位 × impact_curve(Δ) | 防止大额交易操纵 |
| Liquidation Fee | 固定 + 动态（随杠杆） | 向LP池返还 |
| Swap Fee | 基础费率 + 动态滑点 | 0.02–0.3%区间 |
| RWA Carry Fee | 若LP资产配置RWA，收益分成x% | 自动复投或回购代币 |

</div>

------------------------------------------------------------------------

### 四、关键公式举例

**Funding Rate**：\
\[\
FR = k \times \frac{OI\_{long} - OI\_{short}}{OI\_{total}}\
\]\
其中 `k` 为可调系数（默认 0.01%/h）

**Price Impact**：\
\[\
ImpactFee = baseFee + \alpha \times (\Delta position / poolLiquidity)^2\
\]

**PnL Cap 限制**：\
\[\
PnL\_{max} = min(PnL, cap \times LP\_{value})\
\]

## **6. LP & Funding Mechanism（流动性与资金费率机制）**

### 6.1 LP 流动性管理

每个 LP Vault 独立记录资产净值、未实现收益、PnLCap 限制：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
struct VaultState {
    uint256 totalLiquidity;
    uint256 totalPnL;
    uint256 totalFeeAccrued;
    uint256 rwaExposure;
    uint256 pnlCapRatio;
}
```

</div>

</div>

#### 资金流向

<div class="table-wrap">

|           |              |                                                     |
|-----------|--------------|-----------------------------------------------------|
| 事件      | LP 行为      | 资产变化                                            |
| Deposit   | 增加流动性   | `totalLiquidity += amount`                          |
| Withdraw  | 减少流动性   | 触发结算（若有未实现PnL）                           |
| RWA Yield | RWA 收益分配 | `vault.totalLiquidity += vault.rwaExposure * yield` |

</div>

> \[Quote: GMX V2 Docs – Liquidity Provider Flows\]

------------------------------------------------------------------------

### 6.2 Funding 费率机制

Funding Rate 用于调节多空不平衡。\
基础模型：\
\[\
FR = k × \frac{OI\_{long} - OI\_{short}}{OI\_{total}}\
\]\
其中：

<div class="table-wrap">

|            |              |              |
|------------|--------------|--------------|
| 参数       | 含义         | 示例值       |
| `k`        | Funding 系数 | 0.01%/hour   |
| `OI_long`  | 多头未平仓量 | 来自持仓索引 |
| `OI_short` | 空头未平仓量 | 同上         |

</div>

Funding 计算与分配：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function updateFundingRate() external {
    int256 imbalance = OI_long - OI_short;
    int256 fr = fundingRateK * imbalance / OI_total;
    fundingRate = clamp(fr, -maxFR, +maxFR);
}
```

</div>

</div>

#### Funding Fee 分配逻辑

- 多空差额的资金费用在周期末清算；

- 多头支付空头；

- RWA 市场在休市期间冻结 Funding。

<div class="table-wrap">

|              |                |                 |
|--------------|----------------|-----------------|
| 参数         | 值             | 来源            |
| fundingRateK | 0.0001         | GMX v2          |
| maxFR        | ±0.005 (±0.5%) | GMX v2          |
| interval     | 1h             | GMX Funding周期 |

</div>

> \[Quote: GMX V2 – Funding Rate Specification\]

------------------------------------------------------------------------

### 6.3 LP 风险敞口与监控

系统需实时计算：

- `open_interest_ratio = OI_long / (OI_long + OI_short)`

- `delta_exposure = |OI_long - OI_short| / liquidity`

当 `delta_exposure > 20%` 时，触发告警。

Backend 指标：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "pool_id": "BTC-USD",
  "oi_long": 1250000,
  "oi_short": 950000,
  "funding_rate": 0.00012,
  "delta_exposure": 0.18
}
```

</div>

</div>

前端展示：资金费率动态条 + LP风控图表。

------------------------------------------------------------------------

## **7. Liquidation Mechanism（清算机制）**

### 7.1 清算条件

清算触发条件与 GMX V2 保持一致：\
\[\
Collateral + PnL \< (PositionSize × MaintenanceMargin)\
\]\
当满足该条件时，触发强平。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function checkLiquidation(address trader) public view returns (bool) {
    uint256 equity = collateral + unrealizedPnL;
    uint256 threshold = positionSize * maintenanceMargin;
    return equity < threshold;
}
```

</div>

</div>

<div class="table-wrap">

|                   |              |        |
|-------------------|--------------|--------|
| 参数              | 示例值       | 来源   |
| maintenanceMargin | 0.005 (0.5%) | GMX V2 |
| liquidationFee    | 0.10%–0.30%  | GMX V2 |

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

------------------------------------------------------------------------

### 9.3 奖励池来源

<div class="table-wrap">

|                  |               |
|------------------|---------------|
| 来源             | 分配          |
| Protocol Fee 20% | 挖矿奖励      |
| DAO Treasury 10% | Referral 回扣 |
| LP Fee 70%       | LP 持有人     |

</div>

------------------------------------------------------------------------

## **风险与边界处理**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="53a89bd5-7458-4714-908a-f5c1ea219d34">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>标的资产</strong></p></th>
<th class="confluenceTh"><p>maxGainP</p></th>
<th class="confluenceTh"><p>maxSlP</p></th>
<th class="confluenceTh"><p>maxLongOiP</p></th>
<th class="confluenceTh"><p>maxShortOiP</p></th>
<th class="confluenceTh"><p>groupOpenInterestPecentage</p></th>
<th class="confluenceTh"><p>maxWalletOI</p></th>
<th class="confluenceTh"><p>isUSDCAligned</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>Crypto</strong></p>
<p>BTC/SOL/</p></td>
<td class="confluenceTd"><p>2500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>100</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Defi</strong></p>
<p>HYPE</p></td>
<td class="confluenceTd"><p>2500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>8</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Defi</strong></p>
<p>BERA</p></td>
<td class="confluenceTd"><p>1000</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>8</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Crypto</strong></p>
<p>BNB</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>MEME</strong></p>
<p>PENGU</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>20</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>MEME</strong></p>
<p>FARTCOIN</p></td>
<td class="confluenceTd"><p>2500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>20</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>MEME</strong></p>
<p>TRUMP</p></td>
<td class="confluenceTd"><p>1000</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>20</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L1</strong><br />
XRP</p></td>
<td class="confluenceTd"><p>2500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>AI?</strong></p>
<p>VIRTUAL/EIGEN/TAO</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>5</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>MEME</strong></p>
<p>CHILLGUY</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>2</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Defi/L1/L2</strong></p>
<p>ARB/AVNT/PUMP</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Defi/L1/L2</strong></p>
<p>XPL/ASTER/ZORA</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>8</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Crypto/NFT</strong></p>
<p>KAITO/APE/GOAT/BRETT</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>2</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>L1</strong></p>
<p>APT</p>
<p><strong>MEME</strong></p>
<p>POPCAT</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Equity</strong></p>
<p>GOOG/TSLA/META/MSFT/AMZN/APPL/NVDA/COIN/</p></td>
<td class="confluenceTd"><p>1000</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>5</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Indicies</strong></p>
<p>QQQ/SPY</p></td>
<td class="confluenceTd"><p>1000</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>30</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>TRY</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>100</p></td>
<td class="confluenceTd"><p>100</p></td>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>TWD/IDR/BRL</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>T</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>ZAR/MXN</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>KRW</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>20</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>INR</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>75</p></td>
<td class="confluenceTd"><p>75</p></td>
<td class="confluenceTd"><p>30</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>FX</strong></p>
<p>CNH</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>30</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Commodities</strong><br />
WTI(<strong>USOILSPOT</strong>)</p></td>
<td class="confluenceTd"><p>500</p></td>
<td class="confluenceTd"><p>80</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>50</p></td>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>F</p></td>
</tr>
</tbody>
</table>

</div>

<div class="table-wrap">

|                   |                    |
|-------------------|--------------------|
| 场景              | 处理方式           |
| Oracle断层 \>120s | 暂停市场，冻结清算 |
| RWA 市场关闭      | 延迟PnL结算        |
| PnL超Cap          | 强制裁剪并记录事件 |
| Funding异常       | 回退至上次有效值   |
| Curator滥权       | DAO投票回滚提案    |

</div>

# 一、统一前提与命名约定

- `User`：钱包持有人（LP 或 Trader）。

- `GLV Vault`：聚合 vault（ERC-4626 风格），对外发行 GLV Token / VaultShare。

- `GM Pool`：单市场流动性池（long token / short token）。

- `GM Router`：路由层，负责在 pools / tokens 间 swap 与最优分配。

- `Keeper`：离线/守护进程，执行异步任务（execute deposits, shifts, rebalance, liquidations）。

- `Oracle`：价格与 RWA 净值来源（Pyth / Chainlink / Custodian feed）。

- 事件（On-chain）：`DepositEvent`, `WithdrawEvent`, `ShiftEvent`, `MintEvent`, `BurnEvent`。

# Deposit（用户入金） — Trace Diagram（文本版）

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
User Wallet (签名)
  ↓ （1）调用前端 UI：选择 vault / asset / amount
Frontend
  ↓ （2）前端校验与预估（gas, fees, estimatedShares）
  ↓ （3）用户签名 approve（ERC20 approve 或 EIP-712）
Backend API Server (可选：构造交易 / 提交)
  ↓ （4）如果为 synchronous deposit: 前端直接调用 GlvVault.deposit(amount)
  ↓ （4b）如果为 async deposit: 前端发起 deposit request 到 Backend（保存请求，返回 txId）
Keeper / Backend（若 async）
  ↓ （5）Keeper 调用 GlvVault.executeDeposit(requestId)
On-chain: GlvVault.deposit/executeDeposit
  ↳ validateVaultState(), checkMaxTVL(), checkMaxPnlFactorForDeposits()
  ↳ transferFrom(user, vault, amount)
  ↳ if needed -> GM Router swap to underlying market tokens
  ↳ calculateShares = amount / virtualPrice
  ↳ mintVaultShares(user, shares)
  ↳ emit DepositEvent(user, asset, amount, shares, vaultId)
Backend / Keeper
  ↓ （6）监听 DepositEvent -> 更新状态（Pending→Executed）
Frontend
  ↓ （7）刷新 UI：显示新的 GLV 余额与累计收益
```

</div>

</div>

## 各方职责（按步骤）

1.  **Frontend**

    - 提供 deposit UI（选择 vault、asset、amount、预估 shares & fees & tx cost）。

    - 校验输入（资产类型、最小入金、wallet balance、approval 状态）。

    - 发起 approve（ERC20）并引导用户签名交易或向 Backend 提交异步请求。

    - 显示 tx 状态（Pending / Executed / Failed）与事件（DepositEvent）。

    - 必须显示 `maxPnlFactorForDeposits`、`currentSharePrice`、`estimated slippage`。

2.  **Backend API Server**

    - （可选）构建并签名或转发交易（托管场景或 meta-tx）。

    - 持久化 deposit 请求（若采用异步模式），生成 requestId。

    - 提供查询接口：`GET /deposits/:requestId/status`。

    - 通知 Keeper 执行（if async）。

3.  **Keeper（后台守护进程）**

    - 轮询或监听新 deposit requests。

    - 在最佳时点调用合约 `executeDeposit`（合并多笔、做 slippage 控制）。

    - 调用前检查 Oracle、Vault caps、TVL caps、maxPnlFactor。

    - 在失败时重试或回退：发出 `DepositFailed` 记录并通知前端/用户。

4.  **GlvVault 合约（合约层）**

    - `deposit()` / `executeDeposit()`：校验、接收资产、计算并 mint vault shares。

    - 计算 `shares = amount / virtualPrice`，使用 `maxPnlFactorForDeposits` 限制计入未实现 PnL。

    - 若需要跨 token：调用 `GM Router` 做 swap 并支付相关 swap fee。

    - 触发 `DepositEvent(user, asset, amount, shares, vaultId)`。

5.  **GM Router**

    - 若 deposit 需将单一资产分配到多个 GM Pool：计算最优拆分（基于 targetWeights、utilization、priceImpact）。

    - 返回拆分与预估 cost 给 Keeper（用于确认）。

6.  **Oracle / RWA Custodian**

    - 提供当前 price / RWA NAV，Keeper 在执行前必须确认 oracle freshness（staleness \< threshold）。

## 关键失败场景与处理

- Oracle stale → Keeper 不执行，标注 `OracleStale` 并通知用户。

- 超出 Vault TVL cap / market max -\> 合约 revert；Keeper 需要回退 request 并提示用户。

- swap price impact 超限 → Keeper abort 并 reschedule。

- ERC20 approve 未完成 → 前端阻止提交并弹提示。

## 主要接口与事件（建议）

- Backend: `POST /api/v1/deposits { user, vaultId, asset, amount }` → returns `requestId`

- Contract events: `DepositEvent(address user, uint256 amount, uint256 shares, bytes32 vaultId)`

# 三、Withdraw（用户赎回） — Trace Diagram（文本版）

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
User Wallet
  ↓ (1) 前端：选择 vault, redeem shares / desiredAsset
Frontend
  ↓ (2) 查询可赎回资产（onchain sharePrice, withdrawCooldown, pendingPnl）
  ↓ (3) 用户签名 withdraw tx 或提交 withdraw request
Backend / Keeper
  ↓ (4) buildWithdrawTx -> optionally queue (if async exit / epoch)
GlvVault.withdraw/executeWithdraw
  ↳ validateWithdrawalAllowed(), apply maxPnlFactorForWithdrawals
  ↳ burnVaultShares(user, shares)
  ↳ calculate underlying amounts (可能跨多个 GM Pools)
  ↳ if need -> GM Router unwind swaps -> transfer underlying asset to user
  ↳ emit WithdrawEvent(user, underlyingAmounts, shares, vaultId)
Backend / Keeper
  ↓ (5) listen WithdrawEvent, update status, notify frontend
Frontend
  ↓ (6) show final balances & fees
```

</div>

</div>

## 各方职责（按步骤）

1.  **Frontend**

    - 提供 Withdraw UI（输入份额或金额，选择目标兑付资产，如 long/short/USDC）。

    - 显示 `withdrawCooldown`、`maxWithdrawable`、`estimated fees` 与 `estimated pro-rata slippage`。

    - 提交签名或 withdraw request。

2.  **Backend / Keeper**

    - 校验用户持有份额（onchain）。

    - 若采用异步退出（epoch / queue）模式，加入队列并在 epoch 执行时调用 `executeWithdraw`。

    - 若部分底层市场流动性不足，Keeper 可选择分批提现或触发回退/partial fill，并通知用户。

3.  **GlvVault 合约**

    - `withdraw()` / `executeWithdraw()`：Burn shares、计算用户应得资产并转账。

    - 在计算时使用 `maxPnlFactorForWithdrawals` 去限定可兑现的未实现 PnL。

    - 可能会调用 `GM Router` 在底层 Pools 间卸载流动性（产生 price impact cost）。

    - 触发 `WithdrawEvent`.

4.  **GM Router**

    - 配合 unwind：检查目标 market liquidity，计算 swap 路径与 price impact。

    - 提供 `maxSellable` / `maxBuyable` 量校验（用来拒绝过大 withdraw 引发池子异常）。

5.  **Oracle**

    - 提供用于计算 sharePrice 的最新 price（同 deposit 场景）。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 合约 | 功能类别 | 职责说明 |
| `GlvRouter.sol` | Interface Layer | 统一入口，路由用户请求至 Vault/Market 模块 |
| `GlvVault.sol` | Liquidity Layer | 管理 LP 资产、计算净值、铸造 GLV token |
| `MarketPool.sol` | Market Layer | 单一市场做市资金与持仓追踪 |
| `ShiftController.sol` | Risk & Balancing | 执行跨池再平衡（Shift）逻辑 |
| `FeeCalculator.sol` | Dynamic Pricing | 动态费率计算（Maker/Taker/Funding） |
| `RwaOracleAdapter.sol` | Integration | 获取链下 RWA 资产价格 |
| `CurateFactory.sol` | Governance | 策略 LP 市场创建与参数治理 |
| `ReferralManager.sol` | Incentive | 推荐人返佣逻辑 |
| `TradingIncentive.sol` | Incentive | 基于交易量的挖矿奖励计算 |
| `Keeper.sol` | Automation | 定期触发 Shift、NAV 更新、清算操作 |

</div>

## 关键失败场景与处理

- 底层流动性不足（liquidity shortfall）：Keeper 返回 partial fill，并生成 `WithdrawPartialEvent`；前端告知用户等待或接受滑点。

- 用户请求与合约状态冲突（例如已被清算/冻结）：合约 revert 并 emit `WithdrawFailed`。

- 大额赎回导致 TVL 突变 → 触发 Protocol Safety（pause withdraw 或 raise fees）。

</div>
