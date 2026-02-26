# Hertzflow V2 产品设计文档（DFT）

<div class="Section1">

<style>[data-colorid=nsjdljohta]{color:#ff5630} html[data-color-mode=dark] [data-colorid=nsjdljohta]{color:#cf2600}[data-colorid=q5kubbu91g]{color:#bf2600} html[data-color-mode=dark] [data-colorid=q5kubbu91g]{color:#ff6640}</style>版本号：V.2.0.0

需求人：cen

<style type="text/css">/**/
div.rbtoc1772008178451 {padding: 0px;}
div.rbtoc1772008178451 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772008178451 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772008178451">

- [1.文档版本信息](#HertzflowV2产品设计文档（DFT）-1.文档版本信息)
- [2. 产品需求](#HertzflowV2产品设计文档（DFT）-2.产品需求)
  - [1.1 产品概述](#HertzflowV2产品设计文档（DFT）-1.1产品概述)
  - [1.2 需求排期](#HertzflowV2产品设计文档（DFT）-1.2需求排期)
  - [1.2 业务流程简述：](#HertzflowV2产品设计文档（DFT）-1.2业务流程简述：)
    - [GM Pool Deposit / Withdraw / Shift逻辑](#HertzflowV2产品设计文档（DFT）-GMPoolDeposit/Withdraw/Shift逻辑)
    - [RWA 资产市场逻辑](#HertzflowV2产品设计文档（DFT）-RWA资产市场逻辑)
  - [1.3 涉及到的角色定义](#HertzflowV2产品设计文档（DFT）-1.3涉及到的角色定义)
  - [1.4 涉及到的核心方法字段描述：](#HertzflowV2产品设计文档（DFT）-1.4涉及到的核心方法字段描述：)
    - [MaxPnLFactor](#HertzflowV2产品设计文档（DFT）-MaxPnLFactor)
    - [收益机制与 APR 计算](#HertzflowV2产品设计文档（DFT）-收益机制与APR计算)
    - [2. 收益指标](#HertzflowV2产品设计文档（DFT）-2.收益指标)
    - [GLVRouter 再平衡机制逻辑 (待技术补充)](#HertzflowV2产品设计文档（DFT）-GLVRouter再平衡机制逻辑(待技术补充))
- [二、竞品架构调研](#HertzflowV2产品设计文档（DFT）-二、竞品架构调研)
  - [2.1 模块分层(示例，技术产出)](#HertzflowV2产品设计文档（DFT）-2.1模块分层(示例，技术产出))
  - [2.2 多隔离 LP 池（Multi-Isolated Liquidity Pools)](#HertzflowV2产品设计文档（DFT）-2.2多隔离LP池（Multi-IsolatedLiquidityPools))
    - [1. 资金流](#HertzflowV2产品设计文档（DFT）-1.资金流)
    - [2. GLV Router 分配逻辑](#HertzflowV2产品设计文档（DFT）-2.GLVRouter分配逻辑)
    - [3. GLV 的收益机制 & APR 说明](#HertzflowV2产品设计文档（DFT）-3.GLV的收益机制&APR说明)
    - [建池参数列表TODO：](#HertzflowV2产品设计文档（DFT）-建池参数列表TODO：)
    - [PnL 限制公式及取值](#HertzflowV2产品设计文档（DFT）-PnL限制公式及取值)
      - [逻辑：](#HertzflowV2产品设计文档（DFT）-逻辑：)
      - [公式：](#HertzflowV2产品设计文档（DFT）-公式：)
      - [实现：](#HertzflowV2产品设计文档（DFT）-实现：)
    - [风险管理（以avantis为例）](#HertzflowV2产品设计文档（DFT）-风险管理（以avantis为例）)
      - [核心参数规律（按风险梯度）](#HertzflowV2产品设计文档（DFT）-核心参数规律（按风险梯度）)
      - [风险层级](#HertzflowV2产品设计文档（DFT）-风险层级)
  - [2.3 RWA 资产市场逻辑](#HertzflowV2产品设计文档（DFT）-2.3RWA资产市场逻辑)
    - [RWA Oracle 数据来源](#HertzflowV2产品设计文档（DFT）-RWAOracle数据来源)
    - [市场开放与冻结规则](#HertzflowV2产品设计文档（DFT）-市场开放与冻结规则)
    - [收费明细](#HertzflowV2产品设计文档（DFT）-收费明细)
    - [风险管理（以avantis为例）](#HertzflowV2产品设计文档（DFT）-风险管理（以avantis为例）.1)
  - [2.5 Fee Structure / Key Params](#HertzflowV2产品设计文档（DFT）-2.5FeeStructure/KeyParams)
- [2.产品需求](#HertzflowV2产品设计文档（DFT）-2.产品需求.1)
  - [1.1 产品概述](#HertzflowV2产品设计文档（DFT）-1.1产品概述.1)
  - [1.2 业务流程简述](#HertzflowV2产品设计文档（DFT）-1.2业务流程简述)
    - [主要流程](#HertzflowV2产品设计文档（DFT）-主要流程)
    - [角色分层与核心模块](#HertzflowV2产品设计文档（DFT）-角色分层与核心模块)
    - [创建流程 & 初始设置](#HertzflowV2产品设计文档（DFT）-创建流程&初始设置)
    - [参数约束与治理机制](#HertzflowV2产品设计文档（DFT）-参数约束与治理机制)
    - [惩罚／保护机制](#HertzflowV2产品设计文档（DFT）-惩罚／保护机制)
    - [Curated Vault Creation](#HertzflowV2产品设计文档（DFT）-CuratedVaultCreation)
      - [Vault层核心参数](#HertzflowV2产品设计文档（DFT）-Vault层核心参数)
      - [市场参数 （这里不适用于我们V3）](#HertzflowV2产品设计文档（DFT）-市场参数（这里不适用于我们V3）)
      - [Flow层核心参数](#HertzflowV2产品设计文档（DFT）-Flow层核心参数)
      - [收益与激励](#HertzflowV2产品设计文档（DFT）-收益与激励)
      - [质押与惩罚](#HertzflowV2产品设计文档（DFT）-质押与惩罚)
      - [风险与边界管理](#HertzflowV2产品设计文档（DFT）-风险与边界管理)
  - [3.3 Referral / 交易挖矿 / Leaderboard](#HertzflowV2产品设计文档（DFT）-3.3Referral/交易挖矿/Leaderboard)
  - [3.4 风险与边界处理](#HertzflowV2产品设计文档（DFT）-3.4风险与边界处理)
- [二、竞品架构调研](#HertzflowV2产品设计文档（DFT）-二、竞品架构调研.1)
  - [2.1 模块分层](#HertzflowV2产品设计文档（DFT）-2.1模块分层)
  - [2.2 多隔离 LP 池（Multi-Isolated Vaults）](#HertzflowV2产品设计文档（DFT）-2.2多隔离LP池（Multi-IsolatedVaults）)
    - [数据结构](#HertzflowV2产品设计文档（DFT）-数据结构)
    - [PnL 限制公式](#HertzflowV2产品设计文档（DFT）-PnL限制公式)
    - [风险管理](#HertzflowV2产品设计文档（DFT）-风险管理)
  - [2.3 RWA 资产市场逻辑](#HertzflowV2产品设计文档（DFT）-2.3RWA资产市场逻辑.1)
    - [RWA Oracle 数据来源](#HertzflowV2产品设计文档（DFT）-RWAOracle数据来源.1)
    - [市场开放与冻结规则](#HertzflowV2产品设计文档（DFT）-市场开放与冻结规则.1)
    - [收费明细](#HertzflowV2产品设计文档（DFT）-收费明细.1)
  - [一、合约层 Trace Diagram](#HertzflowV2产品设计文档（DFT）-一、合约层TraceDiagram)
  - [三、机制详解（产品逻辑与合约内核）](#HertzflowV2产品设计文档（DFT）-三、机制详解（产品逻辑与合约内核）)
- [三、产品需求](#HertzflowV2产品设计文档（DFT）-三、产品需求)
  - [LP Pool](#HertzflowV2产品设计文档（DFT）-LPPool)
    - [三、收益指标体系](#HertzflowV2产品设计文档（DFT）-三、收益指标体系)
  - [五、后端数据需求](#HertzflowV2产品设计文档（DFT）-五、后端数据需求)
    - [5.1 Indexer 事件监听](#HertzflowV2产品设计文档（DFT）-5.1Indexer事件监听)
    - [5.2 指标与统计字段](#HertzflowV2产品设计文档（DFT）-5.2指标与统计字段)
    - [5.3 API (GraphQL / REST)](#HertzflowV2产品设计文档（DFT）-5.3API(GraphQL/REST))
  - [六、前端功能与交互](#HertzflowV2产品设计文档（DFT）-六、前端功能与交互)
  - [风险与边界管理](#HertzflowV2产品设计文档（DFT）-风险与边界管理.1)

</div>

# **1.文档版本信息**

<div class="table-wrap">

|        |                |          |        |
|--------|----------------|----------|--------|
| 版本号 | 编写/修订日期  | 修订内容 | 状态   |
| v2.21  | 2025/10/21     |          |        |
| v2.2   | 2025/10/20     |          |        |
| v2.1   | 2025/10/10     |          | 待评审 |
| v2.0   | 2025年10月23日 | 产品设计 | 已完成 |

</div>

# 2. 产品需求

## 1.1 产品概述

<div class="panel" style="background-color: #E6FCFF;border-width: 1px;">

<div class="panelContent" style="background-color: #E6FCFF;">

**定位：基于GMX V2 框架的BNB链上多资产衍生品交易平台**

**目标：**在BNB链上构建一个支持链上高杠杆衍生品与 RWA（美债、黄金、ETF）交易的去中心化衍生品交易所，实现多资产统一结算、动态费用调节、与隔离流动性池 & 聚合池的流动性市场体系，让用户能在同一交易协议内获得

- **「高效安全、模块化风控的链上衍生品交易体验」** GMX V2 的多隔离池机制（风险隔离 + 流动性聚合）+ GMX的动态费用调节 + Avantis 的 RWA 交易 + GMX/Avantis的 Referral、交易激励

- **「灵活可组合的收益型与策略型流动性池聚合」** 策略化 LP 收益（引入类似Jupiter Multiply / Morpho Earn的自动复利逻辑）

- **「Permissionless Market Creation」**Morpho Curate 的自主市场创建 **+** 治理体系（自主建池）

</div>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="044a1e0f-c72c-4cbb-98f8-035920cdca45">
<tbody>
<tr>
<th class="confluenceTh"><p>层级</p></th>
<th class="confluenceTh"><p><strong>模块名称</strong></p></th>
<th class="confluenceTh"><p><strong>核心内容 &amp; 功能</strong></p></th>
<th class="confluenceTh"><p><strong>版本规划</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>FE</p></td>
<td class="confluenceTd"><p><strong>Wallet SDK</strong></p></td>
<td class="confluenceTd"><p>用户交互界面，发起逻辑订单、存取流动性、建池操作；调用后端接口签名授权</p></td>
<td class="confluenceTd"><p>V2.0.0</p></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>Trade页面</strong><br />
</p></td>
<td class="confluenceTd"><p>→ <strong>「Market List」</strong> 新增RWA资产支持</p>
<p>→ <strong>「交易面板」</strong>新增tpsl功能；流动性路径选择；一系列相关pre-check</p>
<p>→ <strong>「历史记录」</strong>新增市价单止盈止</p>
<p>损价格编辑，平仓止盈止损价格编辑</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>合约</p></td>
<td class="confluenceTd"><p><strong>Trade Engine 层</strong></p>
<p>→ GlvRouter</p>
<p>→ MarketRouter</p>
<p>→ Controller</p></td>
<td class="confluenceTd"><p>请求入口、风控验证</p>
<p>管理资金流动、状态更新、LP Token 发行、动态费率计算。</p>
<ol>
<li><p>支持合约杠杆交易、资金费率计算、RWA 仿真交易</p></li>
<li><p>按市场偏向实时计算 Dynamic Fee</p></li>
<li><p>每个池维护独立 accounting、risk 参数；聚合层统一结算 token 价值。</p></li>
<li><p>提供杠杆交易、清算、资金费率计算；</p></li>
<li><p>实时监控仓位偏向，动态调整费用系数；</p></li>
<li><p>处理合约层资金流转</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>GLV Vault 层</strong></p>
<p>→ GlvVault</p>
<p>-&gt; MarketPool</p>
<p>-&gt; PoolStore</p></td>
<td class="confluenceTd"><p>主资产托管与流动性核心</p>
<ol>
<li><p>聚合所有 GM Pool 的底层资产</p></li>
<li><p>实现 Shift / Deposit / Withdraw 功能</p></li>
<li><p>实施底层 swap：调用 GM Router 移动流动性自动再平衡</p></li>
<li><p>管理 LP Token发行与赎回</p></li>
<li><p>支持自动复投与收益快照。</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>风控与结算层</strong></p>
<p>→ Keeper</p>
<p>→ Oracle</p>
<p>→ FeeCalc</p></td>
<td class="confluenceTd"><p>自动执行流动性添加移除；订单撮合；清算；与价格、费用更新</p>
<ol>
<li><p>监控指标：各 pool APR、utilization、OI skew、maxMarketTokenBalanceUsd、pendingPnl 比例。</p></li>
<li><p>生成 shift plan（目标、拆分、限价、最大允许 price impact、time window）。</p></li>
<li><p>调度并提交 shift tx</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Incentives &amp; Referral</p>
<p>→ IncentiveDist</p>
<p>→ ReferralMgr</p></td>
<td class="confluenceTd"><p>关系绑定，激励分配与返佣机制</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Governance &amp; Curate</p>
<p>→ CurateFactory</p>
<p>-&gt; Registry</p>
<p>-&gt; Governor</p></td>
<td class="confluenceTd"><p>池创建与治理提案机制</p>
<p><strong>Curate Layer（自主市场层）</strong></p>
<ol>
<li><p>Curator 白名单机制</p></li>
<li><p>发起“市场创建”请求；自主设定资产对、杠杆上限、费用等参数</p></li>
<li><p>采用 Morpho Earn 类似模型，允许托管型 LP 策略</p></li>
</ol></td>
<td class="confluenceTd"><p>V3.0.0</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>后端接口与服务</p></td>
<td class="confluenceTd"><p>Auth Service</p>
<p>→ JWT</p>
<p>→ WalletSign</p>
<p>→ Session</p></td>
<td class="confluenceTd"><p>构建交易请求、签名校验、与合约交互；同步预言机数据，维护 Vault 状态快照。</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>API Gateway</p>
<p>→ Websocket</p></td>
<td class="confluenceTd"><p>聚合数据、风控缓存、任务分发、积分奖励分配</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Indexer</p>
<p>→ BlockScan</p>
<p>→ OnchainSync</p>
<p>→ EventListener</p></td>
<td class="confluenceTd"><p>链上事件索引</p></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

> 参考链接：
>
> - <a href="https://github.com/gmx-io/gmx-synthetics/tree/main/contracts/glv" class="external-link" rel="nofollow">GMX V2聚合池GLV代码</a>：每个市场单独池、风险隔离、个别清算，USDC池子支持。
>
> - <a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765" class="external-link" rel="nofollow">Avantis RWA所有风控参数配置</a>：不同种类的标的市场对应不同的止盈止损上限（包括市价单）；最大杠杆倍数；Max Position Size；Max OI；Max Group OI
>
> - <a href="https://docs.avantisfi.com/trading/market-hours" class="external-link" rel="nofollow">Avantis RWA市场开盘与休市时间</a>：对应Pyth Oracle的开市时间、USDC-backed RWA Markets 不涉及链下收益同步/断层清算逻辑，不涉及盘前逻辑。开盘则可交易，闭盘则禁止任何操作。
>
> - <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/6324231/Research_#Table2---%E7%AB%9E%E5%93%81%E5%8F%82%E6%95%B0%E9%85%8D%E7%BD%AE%E8%A1%A8%E6%A0%BC" data-linked-resource-id="6324231" data-linked-resource-version="38" data-linked-resource-type="page">GMX/AVNT/JUP 费用模型梳理</a>：AVNT费用很乱，不建议作为参考。此处为合约主导，基于当前优化/新增（i.e. funding fee新增；OI Imbalance相关的指数 Price Impact 奖惩）。
>
> - 激励系统调研及机制提案 （待产出）：Referral ← 积分系统 ← 交易竞赛（leaderboard）等
>
> - 自主建池（策略池以及市场创建）；Curator管理 （待理解竞品逻辑后产出）：USDC 第三方策略LP池 - **合作方**自主创建市场 + Curator 白名单治理；角色与多层权限（提案、审核、协议费用抽水分配等）

开发人员分配：

## 1.2 需求排期

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="704554a3-b792-42ed-ae24-7839002db2e3">
<tbody>
<tr>
<td class="confluenceTd"><p><strong>优先级</strong></p></td>
<td class="confluenceTd"><p><strong>新增模块 &amp; 核心功能</strong></p></td>
<td class="confluenceTd"><p><strong>预估所需交付时间</strong></p></td>
<td class="confluenceTd"><p><strong>截图</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p><strong>「Wallet Connect」</strong></p>
<ol>
<li><p>链接BSC测试网，支持白名单钱包地址识别。针对白名单地址，比普通用户多展示一个Launch无准入创建市场页面</p></li>
<li><p>连接成功后Portfoliio新增止盈止损订单展示</p></li>
</ol></td>
<td class="confluenceTd"><p>前端：</p>
<p>后端：</p>
<p>测试：</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="47fb0141b1ea69a9fcbae1f1fd6e9f9cf0007f620e0ebbb4aab54588c1ce2fe8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.28.32.png?version=1&amp;modificationDate=1761901556014&amp;cacheVersion=1&amp;api=v2" data-height="116" data-width="579" data-unresolved-comment-count="0" data-linked-resource-id="28672068" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.28.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="696595b5-b8b1-4310-9e60-d5d41219071f" data-media-type="file" width="250" height="50" alt="Screenshot 2025-10-31 at 15.28.32.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="30d28087b49e80af775b7097e1cd41b9897f06c49d580531e417ef41285e9fd0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.28.20.png?version=1&amp;modificationDate=1761901556048&amp;cacheVersion=1&amp;api=v2" data-height="331" data-width="795" data-unresolved-comment-count="0" data-linked-resource-id="28672075" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.28.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="4cf6873c-99bd-4f62-8e17-b0b00c01dfb5" data-media-type="file" width="174" height="72" alt="Screenshot 2025-10-31 at 15.28.20.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p><strong>「Trade Page_Market Carousel」</strong>&amp; <strong>「Trade Page_Market List」&amp; 「Trade Page_Market Info」</strong></p>
<ol>
<li><p><strong>List</strong> 新增RWA资产支持：～50市场。<a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?usp=sharing" class="external-link" rel="nofollow">见表格标绿。</a>按组分为Newly Listed - 第三方白名单创建的市场；0-1，5：Crypto；2: Forex；3: Commodities；4: Memes；6 row 78-79: Indices；6 其他：Equities</p></li>
<li><p><strong>Carousel：</strong>24h vol 前十（规则待定）市场信息轮播</p></li>
<li><p><strong>List</strong> 新增筛选；查找；排序功能 （分页展示）</p></li>
<li><p><strong>List &amp; Info</strong> 新增市场数据展示（包括tooltip）： max open lev；OI ；24h Vol；24h Liquidation；Market Sentiment；Top Gainers/Losers以及流动性数据Avail Liq</p></li>
<li><p><strong>Info：rwa资产</strong>闭市状态（closed标签）；交易面板不可点</p></li>
</ol></td>
<td class="confluenceTd"><p>前端：</p>
<p>后端：</p>
<p>合约：</p>
<p>测试：</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9d069948df411e6e3ac3977969628c91bc3224c64bd5e2a332bd497599055228" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.31.30.png?version=1&amp;modificationDate=1761901556067&amp;cacheVersion=1&amp;api=v2" data-height="55" data-width="1528" data-unresolved-comment-count="0" data-linked-resource-id="28672081" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.31.30.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="6083fbf5-c04f-4c01-8c06-09127425415a" data-media-type="file" width="295" height="10" alt="Screenshot 2025-10-31 at 15.31.30.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="eb56a767bb3406c731f5826a8d1e05359fad3eeb37c3efabe8eb626e40ee483e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2014.18.38.png?version=1&amp;modificationDate=1761901556086&amp;cacheVersion=1&amp;api=v2" data-height="668" data-width="1198" data-unresolved-comment-count="0" data-linked-resource-id="28672087" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 14.18.38.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="0f33b8aa-4856-4e3c-86cf-c49038945d2c" data-media-type="file" width="295" height="164" alt="Screenshot 2025-10-31 at 14.18.38.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="af2eabf0a24737e7fd7ca563a3f56f90c9e9528066bf8f7d3d6dbe99b43ac6ab" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.32.03.png?version=1&amp;modificationDate=1761901556104&amp;cacheVersion=1&amp;api=v2" data-height="102" data-width="1536" data-unresolved-comment-count="0" data-linked-resource-id="28672093" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.32.03.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="f31f792e-f62d-4835-be00-aa02fe0b7464" data-media-type="file" width="173" height="11" alt="Screenshot 2025-10-31 at 15.32.03.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="239aa347d2ec57655337db2990e91dbeb4900fd14d0d6059d5fa84039915fdc0" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.44.31.png?version=1&amp;modificationDate=1761901556123&amp;cacheVersion=1&amp;api=v2" data-height="252" data-width="351" data-unresolved-comment-count="0" data-linked-resource-id="28672099" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.44.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="32781c01-061f-4eca-9410-12056ab496ca" data-media-type="file" width="173" height="124" alt="Screenshot 2025-10-31 at 15.44.31.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="0bedb26dd4bd257037fb6c31d47ee1206113971b6ec027c551a0db48c8779e49" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.44.35.png?version=1&amp;modificationDate=1761901556143&amp;cacheVersion=1&amp;api=v2" data-height="265" data-width="425" data-unresolved-comment-count="0" data-linked-resource-id="28672105" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.44.35.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="0d33a2a5-f19f-43f2-969c-0db0f93d43d5" data-media-type="file" width="173" height="107" alt="Screenshot 2025-10-31 at 15.44.35.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P2</p></td>
<td class="confluenceTd"><p><strong>「Trade Page_Recent Trades」</strong></p>
<ol>
<li><p><strong>Recent Trades</strong> 全站交易24h内，该标的交易历史展示；以及根据24h Vol比例所计算的Market Sentiment指标展示</p></li>
<li><p><strong>Smart Flows</strong> 全站巨鲸/聪明钱（待定义）24h动向；以及根据规则过滤出的24h Vol比例所计算的Smart Flow指标，与外部API的Fear Greed Index展示（即，Market Sentiment过滤版）</p></li>
<li><p><strong>Smart Flows</strong> 支持一键copy trade</p></li>
</ol></td>
<td class="confluenceTd"><p>前端：</p>
<p>后端：</p>
<p>测试：</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b4ad31dd556ca45184d1ac705254b807ded353ba5ac64400af367dbbaf7dcbd7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.51.43.png?version=1&amp;modificationDate=1761901556162&amp;cacheVersion=1&amp;api=v2" data-height="816" data-width="534" data-unresolved-comment-count="0" data-linked-resource-id="28672111" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.51.43.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="0002d62f-5f96-4215-8816-1e426846c39e" data-media-type="file" width="173" height="263" alt="Screenshot 2025-10-31 at 15.51.43.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c6264c23b22b4190866c9813f3a46eb049fb85b0d529c92ee171ecf4effc69a7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.51.29.png?version=1&amp;modificationDate=1761901556182&amp;cacheVersion=1&amp;api=v2" data-height="834" data-width="528" data-unresolved-comment-count="0" data-linked-resource-id="28672117" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.51.29.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="428cd1c0-cc05-4c03-8d0c-f7c57e35bd2a" data-media-type="file" width="173" height="273" alt="Screenshot 2025-10-31 at 15.51.29.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P2</p></td>
<td class="confluenceTd"><p><strong>「Trade Page_K-line」</strong></p>
<ol>
<li><p><strong>价格K线图</strong> 新增用户交易历史价格打点</p></li>
<li><p><strong>价格K线图</strong> rwa资产闭市状态 k线连续 无价格部分不展示</p></li>
<li><p><strong>深度图</strong>展示 （包括tooltip）</p></li>
<li><p><strong>24h多空funding rate</strong>折线图</p></li>
</ol></td>
<td class="confluenceTd"><p>前端：</p>
<p>后端：</p>
<p>合约：</p>
<p>测试：</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7f4a5f7f5194bf7e61c05a19f4e22328009cb1d3fc2d90df222d170403c9533f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.43.55.png?version=1&amp;modificationDate=1761901556201&amp;cacheVersion=1&amp;api=v2" data-height="580" data-width="838" data-unresolved-comment-count="0" data-linked-resource-id="28672123" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.43.55.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="20657dbd-e71c-46bf-b06e-9cb1a066e6f2" data-media-type="file" width="174" height="120" alt="Screenshot 2025-10-31 at 15.43.55.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="9bd356a5b228b37c6bc890b5be7e4bfec18d8bf7b34fd4e4d658baa6bfd14ff4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.44.27.png?version=1&amp;modificationDate=1761901556219&amp;cacheVersion=1&amp;api=v2" data-height="472" data-width="905" data-unresolved-comment-count="0" data-linked-resource-id="28672129" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.44.27.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="ee70f9c5-c843-4bcf-af31-0969c472281d" data-media-type="file" width="173" height="90" alt="Screenshot 2025-10-31 at 15.44.27.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="ab96c6ca18a55a91d9fd9ec4d0b0f00963a3ada6722d42f3b83b2a7e8fbccedb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.41.27.png?version=1&amp;modificationDate=1761901556239&amp;cacheVersion=1&amp;api=v2" data-height="551" data-width="1342" data-unresolved-comment-count="0" data-linked-resource-id="28672135" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.41.27.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="41b58614-7423-4875-91d5-78b753518e52" data-media-type="file" width="173" height="71" alt="Screenshot 2025-10-31 at 15.41.27.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p><strong>「Trade Panel」</strong></p>
<ol>
<li><p><strong>交易面板</strong> 市价&amp;限价 新增止盈止损价格 &amp; Reduce Only设置（若合约支持非等比加减仓）</p></li>
<li><p><strong>限价下单</strong> 支持保证金资产类型选择</p></li>
<li><p><strong>交易明细</strong> 支持流动池路由选择，并展示路由路径及池明细（第三方创建者，所选预言机）。</p></li>
<li><p><strong>交易明细</strong> 新增funding fee；隔离池可用流动性；非线性price impact 相关校验与提示</p></li>
</ol></td>
<td class="confluenceTd"><p>前端：</p>
<p>后端：</p>
<p>合约：</p>
<p>测试：</p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8518dafe657f63bcc5361f1982c958e24d2207b13ba9c3dbb678ed22b6436642" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2015.57.14.png?version=1&amp;modificationDate=1761901556259&amp;cacheVersion=1&amp;api=v2" data-height="948" data-width="401" data-unresolved-comment-count="0" data-linked-resource-id="28672141" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 15.57.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="ad054da4-fc12-477a-b4ff-80172c9ba5ad" data-media-type="file" width="173" height="408" alt="Screenshot 2025-10-31 at 15.57.14.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="a6ebf9b16a7ae1491ee0835b104b7370684671aaad39cc449a784c696f38c493" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.05.51.png?version=1&amp;modificationDate=1761901556278&amp;cacheVersion=1&amp;api=v2" data-height="914" data-width="978" data-unresolved-comment-count="0" data-linked-resource-id="28672147" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.05.51.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="6cf7144a-9554-4c10-a02d-3f0bb2e4edff" data-media-type="file" width="173" height="161" alt="Screenshot 2025-10-31 at 16.05.51.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f3c02f48fa7ce1140c2804bad4dca85dbd7eabc52539e8cbad6bf3b9e29485d9" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.12.16.png?version=1&amp;modificationDate=1761901556297&amp;cacheVersion=1&amp;api=v2" data-height="939" data-width="1194" data-unresolved-comment-count="0" data-linked-resource-id="28672153" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.12.16.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="9536e239-11cb-42fd-9af7-fd1546bc275a" data-media-type="file" width="174" height="136" alt="Screenshot 2025-10-31 at 16.12.16.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p><strong>「Trade Page_History」</strong></p>
<ol>
<li><p>Position：新增止盈止损价格编辑，与原保证金编辑整合至同一个弹窗；新增TPSL平仓。开单不支持部分止盈止损或多价格设定，平仓支持部分止盈止损，不支持多价格设定。</p></li>
<li><p>Orders：展示TPSL订单，支持价格编辑</p></li>
<li><p>History：新增止盈止损相关展示</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c4b6e896e249997ca242834f3aaf05e97903b0386be3bb8f71eaa86deb11b3b4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.39.26.png?version=1&amp;modificationDate=1761901556316&amp;cacheVersion=1&amp;api=v2" data-height="709" data-width="1043" data-unresolved-comment-count="0" data-linked-resource-id="28672159" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.39.26.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="69a26d6f-3267-4bca-a2bb-c61def84e2c6" data-media-type="file" width="468" height="317" alt="Screenshot 2025-10-31 at 16.39.26.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c630ff00f09d7ca0bc17ab1c76f61d0b53108199360bac2711f54f226cfaafed" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.41.40.png?version=1&amp;modificationDate=1761901556336&amp;cacheVersion=1&amp;api=v2" data-height="816" data-width="1360" data-unresolved-comment-count="0" data-linked-resource-id="28672165" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.41.40.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="0603eea8-0fc1-4f04-bd2f-7f635e9871ca" data-media-type="file" width="173" height="103" alt="Screenshot 2025-10-31 at 16.41.40.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="528a3cc7c61806c7d65387e6707a2b369ddd597aef2f259ad785f8db82452fef" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.44.40.png?version=1&amp;modificationDate=1761901556356&amp;cacheVersion=1&amp;api=v2" data-height="149" data-width="897" data-unresolved-comment-count="0" data-linked-resource-id="28672171" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.44.40.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="c3e62c2b-a2f7-4168-8b8e-83a0acb4cfda" data-media-type="file" width="350" height="58" alt="Screenshot 2025-10-31 at 16.44.40.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="381cc31b865870ef13994d97976f8f8746368ededb6310e003dd2395ec630285" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.47.16.png?version=1&amp;modificationDate=1761901556376&amp;cacheVersion=1&amp;api=v2" data-height="525" data-width="915" data-unresolved-comment-count="0" data-linked-resource-id="28672177" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.47.16.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="89d3970c-f28a-4200-86c6-9d51845bc014" data-media-type="file" width="350" height="200" alt="Screenshot 2025-10-31 at 16.47.16.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P2</p></td>
<td class="confluenceTd"><p><strong>「Refferal &amp; Leaderboard」</strong></p>
<ol>
<li><p>支持不同权重的指标加和映射的积分系统</p></li>
<li><p>推荐体系及返现&amp;手续费折扣</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="cfae9f1747cf24bc7faa6475e52dfd1222213f12c0dd5fe049c5b57b747c284f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.23.05.png?version=1&amp;modificationDate=1761902621344&amp;cacheVersion=1&amp;api=v2" data-height="962" data-width="1486" data-unresolved-comment-count="0" data-linked-resource-id="28704910" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.23.05.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="62d3b89e-48fd-46d1-af0a-1c21ce78f138" data-media-type="file" width="350" height="226" alt="Screenshot 2025-10-31 at 17.23.05.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3606c21a588260d5a48c1311a640bae01f0f127a07bdada8913c322e497e5e3a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.23.15.png?version=1&amp;modificationDate=1761902621339&amp;cacheVersion=1&amp;api=v2" data-height="830" data-width="1496" data-unresolved-comment-count="0" data-linked-resource-id="28770478" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.23.15.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="9a4562ac-0c30-4a17-87d3-2666740afee4" data-media-type="file" width="350" height="194" alt="Screenshot 2025-10-31 at 17.23.15.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P3</p></td>
<td class="confluenceTd"><p><strong>「底部导航栏 高频信息工具展示」</strong></p>
<ol>
<li><p>新闻</p></li>
<li><p>行业热力图</p></li>
<li><p>Leaderboard</p></li>
<li><p>signal （巨鲸&amp;聪明钱动向）</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="dfc5c7e217f168843fd773a370973de9f901d8421be7565d8fcbf4efff9f200b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.17.56.png?version=1&amp;modificationDate=1761902455236&amp;cacheVersion=1&amp;api=v2" data-height="997" data-width="1682" data-unresolved-comment-count="0" data-linked-resource-id="28770471" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.17.56.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="35c75c8c-14c7-4dc3-90fe-4ac102053923" data-media-type="file" width="350" height="207" alt="Screenshot 2025-10-31 at 17.17.56.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p><strong>「Launch Page」</strong></p>
<ol>
<li><p>仅白名单地址可访问</p></li>
<li><p>无准入建池 市场&amp;预言机选择（下拉栏）；参数自定义；</p></li>
<li><p>支付保证金；初始流动性并创建市场</p></li>
<li><p>创建市场成功后 trade页展示</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="fd2ac250c63de51b57e16cdcf2ae0641a248a167439d5c0162f4dd16a0d9bf67" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.53.15.png?version=1&amp;modificationDate=1761901556395&amp;cacheVersion=1&amp;api=v2" data-height="572" data-width="1552" data-unresolved-comment-count="0" data-linked-resource-id="28672183" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.53.15.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="1a59ca76-e9ee-4fee-b01c-42cad288befc" data-media-type="file" width="350" height="129" alt="Screenshot 2025-10-31 at 16.53.15.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="69c6cb53155da35ddde9fd6323b19d90d646720135d793bb2e73076b22a21e62" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2016.59.20.png?version=1&amp;modificationDate=1761901556415&amp;cacheVersion=1&amp;api=v2" data-height="562" data-width="1568" data-unresolved-comment-count="0" data-linked-resource-id="28672189" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 16.59.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="f7db1e29-3655-4f18-9d52-ad8740fb3d0a" data-media-type="file" width="350" height="125" alt="Screenshot 2025-10-31 at 16.59.20.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p>「Pools Page」</p>
<ol>
<li><p><strong>池子列表：</strong>LP池纵览及对应指标展示</p>
<ol>
<li><p>总：池子总tvl &amp; 手续费收入；用户总质押&amp;手续费收入 （不计入pnl）</p></li>
<li><p>分：池子单独tvl &amp; LP token supply &amp; 手续费收入 &amp; APY数据及APR图表；用户对应池子的质押&amp;手续费收入 （不计入pnl）</p></li>
</ol></li>
<li><p><strong>池子列表：</strong>过滤、排序、搜索功能</p></li>
<li><p><strong>二级页面：</strong>新增APR &amp; TVL图表；可用流动性展示 &amp; shift操作（LP token之间的划转） &amp; 对应前端precheck</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="37d476c103be31feb813d6215016b031a5fc496d10aed78af6241439d2d5b15b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.09.17.png?version=1&amp;modificationDate=1761902911294&amp;cacheVersion=1&amp;api=v2" data-height="831" data-width="1332" data-unresolved-comment-count="0" data-linked-resource-id="28770489" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.09.17.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="f24303a7-a604-44c6-894d-10baec75e1af" data-media-type="file" width="350" height="218" alt="Screenshot 2025-10-31 at 17.09.17.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b578395a6e872486b85b96f2468228b2f00ae9dfb84503206ed90a09ee8c0ed6" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.09.21.png?version=1&amp;modificationDate=1761902911058&amp;cacheVersion=1&amp;api=v2" data-height="826" data-width="1331" data-unresolved-comment-count="0" data-linked-resource-id="28672202" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.09.21.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="840010a9-f40c-4ba6-aac3-c18de13752fb" data-media-type="file" width="350" height="217" alt="Screenshot 2025-10-31 at 17.09.21.png" /></span></td>
</tr>
<tr>
<td class="confluenceTd"><p>P0</p></td>
<td class="confluenceTd"><p>「Vault Page」</p>
<ol>
<li><p><strong>聚合池列表：</strong>LP池总览及对应指标展示</p>
<ol>
<li><p>总：池子总tvl &amp; 手续费收入 &amp; 第三方生态合作数量；用户总质押&amp;手续费收入 （不计入pnl）</p></li>
<li><p>分：池子单独tvl &amp; LP token supply &amp; 手续费收入 &amp; 白名单curator &amp; APY数据及APR图表；用户对应池子的质押&amp;手续费收入 （不计入pnl）</p></li>
</ol></li>
<li><p><strong>池子列表：</strong>过滤、排序、搜索功能</p></li>
<li><p><strong>二级页面：</strong>新增APR &amp; TVL &amp; 市场敞口图表；可用流动性展示 &amp; shift操作（LP token之间的划转） &amp; 对应前端precheck</p></li>
</ol></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="7d191a5cd92716032bee7efc3c6472cab00be4db4b93dadaaad8fffe924aa09f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.08.45.png?version=1&amp;modificationDate=1761903305082&amp;cacheVersion=1&amp;api=v2" data-height="916" data-width="1467" data-unresolved-comment-count="0" data-linked-resource-id="28704936" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.08.45.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="93d3159c-b09f-4fdb-9239-d28f9b284a97" data-media-type="file" width="350" height="218" alt="Screenshot 2025-10-31 at 17.08.45.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="99af3105c0f2ba8859a58be72ced850bb02aa4492fbc871eeacfd5099683825e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.08.53.png?version=1&amp;modificationDate=1761903305084&amp;cacheVersion=1&amp;api=v2" data-height="929" data-width="1467" data-unresolved-comment-count="0" data-linked-resource-id="28672212" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.08.53.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="ca068515-dbbd-4e0e-83c9-3a70f6cb00da" data-media-type="file" width="350" height="221" alt="Screenshot 2025-10-31 at 17.08.53.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f5204854a1a5a8ccd1afc17d934d6acd43fed4823645770253f3793804c9ae5d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.08.58.png?version=1&amp;modificationDate=1761903305088&amp;cacheVersion=1&amp;api=v2" data-height="923" data-width="1457" data-unresolved-comment-count="0" data-linked-resource-id="28672218" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.08.58.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="1ed7ad9b-7119-4332-a639-060f8a381741" data-media-type="file" width="350" height="221" alt="Screenshot 2025-10-31 at 17.08.58.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4f8737d095b8cfe454a395d7c521ade1a0ca93356c823ad17ddbe80eb1e52ad2" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-31%20at%2017.09.04.png?version=1&amp;modificationDate=1761903305091&amp;cacheVersion=1&amp;api=v2" data-height="900" data-width="1461" data-unresolved-comment-count="0" data-linked-resource-id="28704942" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-31 at 17.09.04.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="37d4af4b-da98-4fcc-8604-79d38101704b" data-media-type="file" width="350" height="215" alt="Screenshot 2025-10-31 at 17.09.04.png" /></span></td>
</tr>
</tbody>
</table>

</div>

## 1.2 业务流程简述：

<span colorid="q5kubbu91g">改图</span>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="74385b127387ff554e1ff7af3ca6b511905cc3688b0e5d1f76f7017a9064a7c7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-23%20at%2017.02.31.png?version=1&amp;modificationDate=1761210198797&amp;cacheVersion=1&amp;api=v2" data-height="1130" data-width="969" data-unresolved-comment-count="0" data-linked-resource-id="22970541" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-23 at 17.02.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="2d7ae991-51d7-499c-a6b9-498414f2935c" data-media-type="file" width="468" height="546" alt="Screenshot 2025-10-23 at 17.02.31.png" /></span>

### GM Pool Deposit / Withdraw / Shift逻辑

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="d1485275-9f6e-4887-816f-059bc08c9b9c">
<tbody>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>功能</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>行为</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>执行逻辑</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Deposit</p></td>
<td class="confluenceTd"><p>用户将底层资产质押进入 GLV Vault，获得代表整体组合份额的 GLV Token。</p>
<p><strong>两种质押路径：</strong></p>
<ol>
<li><p><strong>Market Token Deposit</strong>：用户直接存入已有的 marketToken（即GM Token），系统直接计入对应市场的 GLV 份额。</p></li>
<li><p><strong>Base Token Deposit</strong>：用户用基础资产（如 USDC / BTC / pair）入金，系统通过 router 自动执行 swap 或按策略分配到不同市场的 marketToken。</p></li>
</ol>
<p><strong>限制条件：</strong></p>
<ul>
<li><p>Deposit 时受到 TVL cap、Max Buyable ratio 的限制；</p></li>
</ul></td>
<td class="confluenceTd"><ol>
<li><p><strong>FE：</strong>用户选择质押路径，前端校验资产类型与 Vault 配置并提交表单。</p></li>
<li><p><strong>Keeper：</strong>读取并生成 DepositTx 请求</p></li>
<li><p><strong>合约</strong></p>
<ol>
<li><p>调用 <code>GLV Router</code>：决定入金资产如何在多个底层 market 中分配。 异步执行，将资产分配给多个GM Pool 并 mint Token。</p></li>
<li><p>调用<code>Deposit()</code>，完成资产转入 Vault；按池份额计算 Mint LP Token；更新 Vault State</p></li>
</ol></li>
<li><p><strong>FE 收益与净值更新：</strong>交易结束后，<code>Vault</code> 更新 token supply 与净值，<code>FeeCalculator</code> 重新计算资金费率。</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p>Withdraw</p></td>
<td class="confluenceTd"><p>用户赎回 GLV Token，选择池子以及对应比例的底层资产。</p>
<p><strong>限制条件：</strong></p>
<ul>
<li><p>Withdraw 时受到 TVL cap、sellable ratio 的限制；</p></li>
<li><p>当 withdraw 涉及 pair 资产时，返回比例依照池子 long/short token 的当前 size 分布。</p></li>
</ul></td>
<td class="confluenceTd"><p>同Deposit，用户发起赎回 LP Token，Keeper构造 WithdrawTx 并校验 Vault 可用性，合约层计算用户可得底层资产并完成转账；异步执行，可能涉及多次 unwind + swap。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Shift</p></td>
<td class="confluenceTd"><p>由第三方Chaoslabs Risk Oracle Edge管理的多个 GM Pool 之间自动再平衡，以优化收益，提高资金利用率，以及降低LP风险。</p>
<p><strong>系统触发</strong>：Keeper/Curator 定期根据市场利用率、收益、风险信号触发；</p>
<p><strong>关键指标：</strong>TVL cap，utilization，OI skew，pendingPnl / recognizedPnl ratio，MaxPnLFactor；realizedShiftCost；oracleLatency</p></td>
<td class="confluenceTd"><ol>
<li><p><strong>FE：</strong>用户选择 BTC/USDC 对，点击 “Deposit/Withdraw/Shift” → 前端 SDK 调用 <code>GlvRouter.deposit/withdraw/shift()</code>。</p></li>
<li><p><strong>Router 调用 Vault：</strong> 将资产转入 <code>GlvVault</code>，触发 mint GLV token。</p></li>
<li><p><strong>Vault 评估池分配：</strong>调用 <code>ShiftController</code> 检查各 GM Pool 的 utilization ratio。</p></li>
<li><p><strong>Keeper自动再分配：</strong>根据池子表现（fee、借贷率、利用率）；迁移成本（price impact、手续费、滑点）；风控考量（防范低利用率或结构性套利）动态管理流动性。</p></li>
<li><p><strong>FE 收益与净值更新：</strong>交易结束后，<code>Vault</code> 更新 token supply 与净值，<code>FeeCalculator</code> 重新计算资金费率。</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

### RWA 资产市场逻辑

1.  **Oracle 数据来源**

- Chainlink + Pyth双源，\>5%偏差时合约拒绝交易。

- 更新频率：市场开放时间内，一般13:30 - 19:59 UTC （ET + 4），每60s/次。

- 仅盘中，无盘前。k线x轴不间断，无数据时间段隐藏。

**2. 市场开放与冻结规则**

> <a href="https://docs.avantisfi.com/trading/market-hours" class="external-link" rel="nofollow">market open time跟着pyth network来</a>，仅有盘中无盘前

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="afcd2561-93ac-4d3e-958b-68d65eab8878">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>状态</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>行为</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#f4f5f7"><p><strong>描述</strong></p></td>
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
（休市时间，包括盘前交易时间么）</p></td>
</tr>
</tbody>
</table>

</div>

## 1.3 涉及到的角色定义

## 1.4 涉及到的核心方法字段描述：

### MaxPnLFactor

> 防止极端波动时 LP 价值或池子估值被短期价格影响操纵。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 参数 | 作用 | 策略 |
| maxPnlFactorForTraders | 限制交易者可兑现未实现收益比例 | 保护池估值稳定 |
| maxPnlFactorForDeposits | 限制入金时可计入池估值的账面收益 | 防止高估进场价格 |
| maxPnlFactorForWithdrawals | 限制出金时可兑现未实现利润 | 避免短期挤兑或套利 |

</div>

- **关键原则：**`Deposit ≤ Trader` 防止出现结构性套利（GLV 高估入金资产、转移损益）。

### 收益机制与 APR 计算

**1. GLV Token 定价**

> GLV 代币的价值随底层资产及其持有的 GM Token 价值波动

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GLV Token Price = GLV Pool Value / GLV Total Supply
GLV Pool Value = Σ (USD Value of each MarketToken held by GLV)
```

</div>

</div>

### 2. 收益指标

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a2494294-4b02-48cf-9a30-9e98c5d90d1e">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>指标</p></th>
<th class="confluenceTh"><p>公式</p></th>
<th class="confluenceTh"><p>说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>APR_pool</p></td>
<td class="confluenceTd"><p>(Fees_pool_Period / AvgTVL_Period) × 365 / T</p></td>
<td class="confluenceTd"><p>年化收益率</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>APY_pool</p></td>
<td class="confluenceTd"><p>(1 + APR_pool)^(365/T) − 1</p></td>
<td class="confluenceTd"><p>复利收益率</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Ann.Perf</p></td>
<td class="confluenceTd"><p>(1 + APR_Pool) / (1 + APR_Bench) − 1</p></td>
<td class="confluenceTd"><p>相对于被动收益的多出比例</p>
<p>与Uniswap V2池子 50:50 收益（价格平方根相关）相比取值</p></td>
</tr>
</tbody>
</table>

</div>

### GLVRouter 再平衡机制逻辑 (待技术补充)

> 连接用户资金与底层 GM Pool 的中间层，负责根据策略与风险参数动态分配流动性。

<div class="table-wrap">

|                  |                      |                   |
|------------------|----------------------|-------------------|
| 参数类型         | 含义                 | 设计目标          |
| targetAllocation | 各 market 的目标权重 | 保持多市场平衡    |
| utilization      | 实际利用率           | 避免过度集中暴露  |
| feeContribution  | 市场贡献度           | 优先高收益池      |
| maxExposure      | 最大风险敞口         | 控制市场风险      |
| liquidityDepth   | 可用深度             | 保证入金/赎回顺畅 |

</div>

- **关键原则：**Router 将 deposit 请求按这些指标动态拆分至多个 market，通过风险参数验证后，调用各自的 deposit/mint 接口。当某市场表现下降或风险上升时，会触发自动 shift，将部分资金迁移至其他表现更好的市场。

------------------------------------------------------------------------

# 二、竞品架构调研

## 2.1 模块分层(示例，技术产出)

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="8a9f4a27-7b45-49e9-84c7-8a19f71f60b6">
<tbody>
<tr>
<td class="confluenceTd"><p>模块</p></td>
<td class="confluenceTd"><p>功能</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>前端层（UI / SDK）</strong></p></td>
<td class="confluenceTd"><ul>
<li><p>WalletConnect、Deposit、Withdraw、Swap、Earn、Curate</p></li>
<li><p>SDK 调用 <code>Router</code> 接口统一访问 GM Pool 与 GLV Vault</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>中间层（Router &amp; Controller）</strong></p></td>
<td class="confluenceTd"><ul>
<li><p><code>GlvRouter.sol</code>：统一入口，处理存取款与仓位操作请求</p></li>
<li><p><code>MarketRouter.sol</code>：撮合并分发至对应 GM Pool</p></li>
<li><p><code>ShiftController.sol</code>：跨池再平衡逻辑</p></li>
<li><p><code>IncentiveDistributor.sol</code>：统一计算与发放奖励</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>后端层（Core Contracts）</strong></p></td>
<td class="confluenceTd"><ul>
<li><p><code>GlvVault.sol</code>：Vault 管理器（ERC-4626 逻辑 + 池价值计算）</p></li>
<li><p><code>MarketPool.sol</code>：单市场隔离池，追踪 long/short collateral</p></li>
<li><p><code>RwaMarket.sol</code>：RWA 资产市场接入</p></li>
<li><p><code>FeeCalculator.sol</code>：动态费率调节</p></li>
<li><p><code>CurateRegistry.sol</code>：策略市场注册与治理</p></li>
<li><p><code>Keeper.sol</code>：自动执行 SHIFT / NAV 更新 / 清算等任务</p></li>
</ul></td>
</tr>
</tbody>
</table>

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

### <span colorid="nsjdljohta">建池参数列表TODO：</span>

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

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="4c3a61cb2ba303e0a58b5a0b09ebcc35cf880c3de832e3ee9beed14ea708b9d2" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-09-12%20at%2014.28.31.png?version=1&amp;modificationDate=1761191699800&amp;cacheVersion=1&amp;api=v2" data-height="1690" data-width="842" data-unresolved-comment-count="0" data-linked-resource-id="23101462" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-09-12 at 14.28.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="006744f6-44e7-4c57-8feb-e3db1446a827" data-media-type="file" width="320" height="640" alt="Screenshot 2025-09-12 at 14.28.31.png" /></span>

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

------------------------------------------------------------------------

# 2.产品需求

## 1.1 产品概述

<div class="panel" style="background-color: #E6FCFF;border-width: 1px;">

<div class="panelContent" style="background-color: #E6FCFF;">

**定位：基于Morpho Earn VaultV2 框架的Infra，提供「Adaptor + id/cap」的通用插件式框架，能让一个 vault 对接任意收益来源（Morpho、Maple等其他协议、RWA 等），并用精细化的风险 id 与hard/soft cap 来控制敞口。**

**目标：**把权限流（timelock/submit/execute）与后端（keeper）流程自动化，并在 UI 层为用户与curator明确展示风险边界（caps、timelock、罚金）；提供**高度灵活**且**可组合的**’Strategy Widget‘：

- **「Strategy Abstraction」策略抽象**；用可复现的自动部署脚本 & 可视化运营面板（Curator / Allocator / Sentinel / Owner 权限视图） & 模块化的的风险分层（清晰 deposit / withdraw 路径与异常处理forceDeallocate），让用户一键完成初始角色分配与 adapter 启用（零 timelock 情况）/ timelock 硬化（有 timelock 情况）

- **「灵活可组合的收益型与策略型流动性池聚合」** 策略化 LP 收益（引入类似Jupiter Multiply / Morpho Earn的自动复利逻辑）

- **「Permissionless Market Creation」**Morpho Curate 的自主市场创建 **+** 治理体系（自主建池）

</div>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="041fd7a1-19e6-4aef-bdb3-92965665a45b">
<tbody>
<tr>
<th class="confluenceTh"><p>层级</p></th>
<th class="confluenceTh"><p><strong>模块名称</strong></p></th>
<th class="confluenceTh"><p><strong>核心内容 &amp; 功能</strong></p></th>
<th class="confluenceTh"><p><strong>版本规划</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>FE</p></td>
<td class="confluenceTd"><p>Vault Dashboard<br />
(Curator)</p></td>
<td class="confluenceTd"><p>展示 Pool id/cap、timelock 状态、提交/执行提案、Adaptor管理</p></td>
<td class="confluenceTd"><p>V3.0.0</p></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Allocator Console</p></td>
<td class="confluenceTd"><p>Allocate/deallocate 操作面板、liquidityAdapter 切换</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>User Interface</p></td>
<td class="confluenceTd"><p>取款 UI、shares 显示、历史收益、in-kind/force withdraw</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>合约</p></td>
<td class="confluenceTd"><p><strong>Vault Layer</strong></p>
<p>→ GlvRouter</p>
<p>→ MarketRouter</p>
<p>→ Controller</p></td>
<td class="confluenceTd"><p>策略池管理核心</p>
<ol>
<li><p>Role/timelock/id-cap/allocate/deallocate/adapter 管理</p></li>
<li><p>聚合所有 GM Pool 的底层资产</p></li>
<li><p>实现 Shift / Deposit / Withdraw 功能</p></li>
<li><p>实施底层 swap：调用 GM Router 移动流动性自动再平衡</p></li>
<li><p>管理 LP Token发行与赎回</p></li>
<li><p>支持自动复投与收益快照。</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>Adaptor Layer</strong></p>
<p>→ Morpho VaultV1 Adapter</p>
<p>→ Morpho MarketV1 Adapter</p></td>
<td class="confluenceTd"><p>策略抽象</p>
<ol>
<li><p>把 VaultV1 抽象成 adaptor，提供 realAssets() 接口</p></li>
<li><p>直接对接 Morpho market，marketParams 编码</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p><strong>Curate Layer</strong></p>
<p>→ CurateFactory</p>
<p>-&gt; Multisig/Timelock Config</p>
<p>-&gt; Governor</p></td>
<td class="confluenceTd"><p>池创建与治理提案机制</p>
<ol>
<li><p>Curator 白名单机制</p></li>
<li><p>发起“市场创建”请求；自主设定资产对、杠杆上限、费用等参数</p></li>
<li><p>采用 Morpho Earn 类模型，允许托管型 LP 策略</p></li>
<li><p>Owner/Curator multisig 配置与 timelock 策略</p></li>
</ol></td>
<td class="confluenceTd"><p>V3.0.0</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>后端接口与服务</p></td>
<td class="confluenceTd"><p>Auth Service</p>
<p>→ Offchain Keeper/Agent</p></td>
<td class="confluenceTd"><p>监控可执行提案、触发 execute、health checks</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Deployment Orchestrator</p></td>
<td class="confluenceTd"><p>接 Foundry 脚本，记录部署 tx、验证合约地址</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>Indexer</p>
<p>→ BlockScan</p>
<p>→ OnchainSync</p>
<p>→ EventListener</p></td>
<td class="confluenceTd"><p>监听合约事件、构建索引、提供查询 API（cap、allocation）</p></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

> 参考链接：
>
> - <a href="https://github.com/morpho-org/vault-v2-deployment/blob/main/script/DeployVaultV2.s.sol" class="external-link" rel="nofollow">Morpho V2策略池代码</a>：每个市场单独池、风险隔离、个别清算，USDC池子支持。
>
> - <a href="https://docs.google.com/spreadsheets/d/12l9DbHXYjSQa0KJcDymeHG2VPni29eOCCmG8lpQF9Gc/edit?gid=240279765#gid=240279765" class="external-link" rel="nofollow">Avantis RWA所有风控参数配置</a>：不同种类的标的市场对应不同的止盈止损上限（包括市价单）；最大杠杆倍数；Max Position Size；Max OI；Max Group OI
>
> - <a href="https://docs.morpho.org/curate/tutorials-v2/vault-creation/" class="external-link" rel="nofollow">Morpho Earn产品文档</a>：对应Pyth Oracle的开市时间、USDC-backed RWA Markets 不涉及链下收益同步/断层清算逻辑，不涉及盘前逻辑。开盘则可交易，闭盘则禁止任何操作。
>
> - 自主建池（策略池以及市场创建）；Curator管理 （待理解竞品逻辑后产出）：USDC 第三方策略LP池 - **合作方**自主创建市场 + Curator 白名单治理；角色与多层权限（提案、审核、协议费用抽水分配等）

## 1.2 业务流程简述

### 主要流程

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f7cbe17cfb2b3b17936d150472eb73b8052a017eac0b0db97c14a2ddda7b7dcf" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-23%20at%2019.26.22.png?version=1&amp;modificationDate=1761218809991&amp;cacheVersion=1&amp;api=v2" data-height="898" data-width="1544" data-unresolved-comment-count="0" data-linked-resource-id="23330865" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-23 at 19.26.22.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="e4695904-d2c5-4950-b79b-adf41de7e67a" data-media-type="file" width="468" height="272" alt="Screenshot 2025-10-23 at 19.26.22.png" /></span>

- **流动性操作：**用户 ↔ VaultV2 是存取款通道。

  - 用户将资产（基础资产） **存入 (deposit / mint)** Vault → Vault 铸造对应份额（shares）给用户。

  - 用户可以 **赎回 (withdraw / redeem)**：销毁份额，Vault 返回其比例的基础资产。

- **资金流：**VaultV2 ↔ Adapter ↔ Market

  - Vault 将闲置资产分配至各市场／Adapter 以赚取收益。

  - 在赎回时，如果部分资金在市场中且流动性不足，可能先从 **WithdrawQueue** 中市场撤回。

- **策略池管理：**（Owner/Curator/Allocator/Sentinel）& VaultV2

  - Allocator／Curator 管理。

  - 在极端情况（坏账、市场关闭、强制清盘）下，恶劣市场可被强制移除，可能影响份额价值。

### 角色分层与核心模块

<div class="table-wrap">

|               |                                     |                  |
|---------------|-------------------------------------|------------------|
| 角色          | 权限                                | 操作场景         |
| **Owner**     | 最高权限，可更换 Curator / Sentinel | 部署或紧急治理时 |
| **Curator**   | 策略治理，添加 adapter、调整 cap    | 策略更新周期     |
| **Allocator** | 资金分配（在多个 adapter 间调仓）   | 日常运营         |
| **Sentinel**  | 紧急暂停，防护机制                  | 异常事件         |
| **User**      | 存取资金                            | 正常操作         |

</div>

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5dc1d95f3cd2ecf4ad10949c76a3267be7a84ed577e4d9f59f4a8db29dc0348d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-23%20at%2018.41.59.png?version=1&amp;modificationDate=1761216169670&amp;cacheVersion=1&amp;api=v2" data-height="389" data-width="1661" data-unresolved-comment-count="0" data-linked-resource-id="23494672" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-23 at 18.41.59.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="f485635d-3d67-4901-bc00-b6d31ef46296" data-media-type="file" width="468" height="109" alt="Screenshot 2025-10-23 at 18.41.59.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8c0f5d9ce81ab21c53afbc842371c54c45d7d14193e13225230749b9d553089e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-23%20at%2018.33.10.png?version=1&amp;modificationDate=1761216169704&amp;cacheVersion=1&amp;api=v2" data-height="513" data-width="1187" data-unresolved-comment-count="0" data-linked-resource-id="23494678" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-23 at 18.33.10.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="42b85eb1-353a-4d45-a5d4-3e2a75c229f0" data-media-type="file" width="468" height="202" alt="Screenshot 2025-10-23 at 18.33.10.png" /></span>

> 插件式设计：让 VaultV2 可以快速支持新的策略类型，只需部署新的 Adapter 即可，不影响主 Vault。

1.  **VaultV2:** 不直接生成收益，而是像GLV一样，将资金路由到已授权 Adapter，Adapter 再与真实的策略合约（如 Morpho Vault V1）打交道。其关键逻辑为：

- **聚合多个 Adapter**（每个代表一个底层 Vault / 策略）

- 维护每个 Adapter 的 **absolute cap（绝对额度）** 与 **relative cap（比例限额）**；

- 由 **Curator 管理** 策略切换；

- 支持 **Sentinel 暂停机制** 保证安全。

2\. **MorphoVaultV1Adapter:** 协议桥梁，把 VaultV2 的标准化指令转译成底层协议的特定操作。

- 每个 Adapter 对应一个独立策略（如 Morpho ETH Pool、Aave USDC Pool 等）；

- Curator 可动态启用/禁用 adapter；

- 用户的 share 价值由所有 adapter 的加权资产价值决定。收益分配同HzLP：价格上升代表收益积累；withdraw 时按比例领取资产。

### 创建流程 & 初始设置

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="27a4de9d061b35b51913a12bf7a70a308907f7f78a88ca1ec1481ee678e021a8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/23101441/Screenshot%202025-10-23%20at%2021.44.01.png?version=1&amp;modificationDate=1761227078055&amp;cacheVersion=1&amp;api=v2" data-height="959" data-width="803" data-unresolved-comment-count="0" data-linked-resource-id="23396414" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-23 at 21.44.01.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="23101441" data-linked-resource-container-version="17" data-media-id="d07b01d2-5dff-4cf6-b60c-051d6cc919ad" data-media-type="file" width="468" height="559" alt="Screenshot 2025-10-23 at 21.44.01.png" /></span>

- 使用 Curator App 或通过 Etherscan（Factory）创建新的 Vault。

- 创建时需要填写或配置：

  - `asset`：Vault 所接受的基础资产（ERC-20）地址。

  - `name` ：Vault 的显示名称。

  - `symbol`：Vault 凭证代币的符号。

  - `initialOwner`：初始拥有者地址。

  - `initialTimelock`：初始的 timelock 时长（秒）。Vault V1.1 以及 V2 支持在部署时设为 0 以便快速初始化。

  - `salt`（可选）：用于 CREATE2 确定 Vault 地址。

- 初始创建后，Curator／Owner 还需做以下初始配置：角色分配（Owner、Curator、Allocator、Sentinel）、适配器部署（V2 情况下用于接入外部协议/Adapter 模型）等。

- 创建之后，可以（且推荐）立即进行 **防止通胀前置 (inflation front-running) 攻击** 的保护措施。 《风险文档》指出：在 Vault 刚创建、几乎为空的情况下，攻击者可能先小额入金 + 大额捐赠，从而抬升 share price，后续用户被极端稀释。

### 参数约束与治理机制

**Timelock 机制**

> 策略变更保护。Curator 的操作不是立即生效，而是先 `submit()` 再 `execute()`。这让用户能提前看到策略变动，防止权限滥用。

- 在 V2 中，可以为每一类敏感操作设定不同的 timelock。 常见敏感的策略变更操作包括：调整 Adapter 权限；提高/降低 cap；修改流动性入口；切换 Sentinel。

- 一旦 timelock 从 0 上调，则最低不得低于 24 小时或官方设定的最小值。

- 在 timelock 期间，Sentinel（或 Guardian）有权撤销 pending 操作。

**角色权限与操作约束**

- **Owner**：最高权限，设定 Curator、Sentinel、费率、名称等。

- **Curator**：定义策略、设定风险边界（caps）、启用/禁用 Adapter／市场。多数操作须经过 timelock。

- **Allocator**：在既定风险边界内执行资金分配、再平衡。不能新增风险类别。

- **Sentinel (Guardian)**：安全角色，可立刻降低风险、撤销待处理操作。

- **Gates**（在 V2 中引入）：控制谁能存入资产、谁能接收份额、谁能提取、谁能转账。可作为合规／权限控制。

**风险与限额参数（caps/队列）**

- 在 Vault V1 中，Curator 为每个市场设定 **supply cap**（上限）以控制 Vault 对该市场的敞口。

- 在 V2 中，风险管理更细粒度：不仅有绝对 cap，还有相对 cap（如“不能超过 Vault 总资产的 X%”）以及风险 id 系统。

- 队列机制：

  - **SupplyQueue**：定义新资金优先流入哪些市场。

  - **WithdrawQueue**：定义当用户赎回时，先从哪些市场撤回。

### 惩罚／保护机制

- **Bad Debt（坏账）机制**：

  - 在 Vault V1.0 中，当 underlying 市场发生坏账且被清算时，该损失会立即通过 share price 的下降分摊到所有存款人。

  - 在 Vault V1.1 中，移除了自动 realization 坏账机制，改为记录 `lostAssets`，避免 share price 突降，从而提升整合与兼容性。

- **通胀前置攻击保护**：如前所述，在 Vault 刚建且几乎空仓时，需防止攻击者通过捐赠+抢先入金方式操纵 share price。建议初期入金保护。

### Curated Vault Creation

> 策略池创建涉及三层配置：`Vault Parameters` + `Markets[]` + `Flow [Caps`,`Allocations/Queues`, `Roles` , `Fees]`
>
> 1.  **Vault 层**：定义资产、权限、费用与 timelock；
>
> 2.  **Market 层**：定义借贷市场参数（资产、预言机、清算阈值、利率模型）；
>
> 3.  **Flow 层**：定义资金流动、cap、reallocation、队列策略。

#### Vault层核心参数

1.  资产

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 参数名 | 类型 / 示例 | 说明 | 可修改性 |
| **asset** | address (ERC20) | Vault 的基础资产（如 WETH / USDC）——所有存取款单位 | ❌ 不可修改 |
| **name** | string | Vault 名称（如 “WETH Yield Vault”） | ✅ 可修改 |
| **symbol** | string | Vault 的凭证代币符号（如 “mWETH”） | ❌ 不可修改 |
| **initialOwner** | address | Vault 创建者或 Multisig 控制者 | ✅ 可转移 |
| **initialTimelock** | uint256 (秒) | Timelock（0~2周）控制风险变更延迟 | ✅ 可上调，不可重设为0 |
| **salt** | bytes32 (可选) | 用于 CREATE2 地址确定性生成 | ✅ 可选参数 |

</div>

2.  权限

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| 角色 | 权限说明 | 关键函数 | 特点 |
| **Owner** | 拥有最高权限，可修改角色、参数、费用 | `transferOwnership()` | 建议使用 multisig |
| **Curator** | 配置市场（add/remove market），设置 caps，reallocations 策略 | `setCurator(address)` | 核心策略操盘手 |
| **Allocator** | 负责执行 reallocate（重新分配流动性） | `setIsAllocator(address, true)` | 可多地址并行 |
| **Guardian** | 审核、延迟或撤销危险操作 | `submitGuardian(address)` / `acceptGuardian()` | 延迟生效；安全层 |
| **Fee Recipient** | 收取 Vault 的 performance fee | `setFeeRecipient(address)` | 通常为 treasury |
| **Skim Recipient** | 接收奖励或溢出 token | `setSkimRecipient(address)` | 收集多余收益 |

</div>

3.  费用与Timelock

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="d4491371-4971-4f89-9a72-462ee61d25dc">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>参数</p></th>
<th class="confluenceTh"><p>类型 / 示例</p></th>
<th class="confluenceTh"><p>说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>feeRecipient</strong></p></td>
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>收取 Vault performance fee 的地址</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>fee</strong></p></td>
<td class="confluenceTd"><p>uint256 (1e18 精度)</p></td>
<td class="confluenceTd"><p>收益费率，例如 1% = 10¹⁶</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>timelock</strong></p></td>
<td class="confluenceTd"><p>uint256 (秒)</p></td>
<td class="confluenceTd"><p>风险参数修改延迟期</p>
<p>所有关键风险／配置变更（如启用 Adapter、提升 cap）多为 <strong>须 timelock 延迟</strong> 的操作。</p>
<blockquote>
<ul>
<li><p>初始阶段 <code>timelock=0</code> → 快速配置；</p></li>
<li><p>之后增加至 ≥1 day。</p></li>
</ul>
</blockquote></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>skimRecipient</strong></p></td>
<td class="confluenceTd"><p>address</p></td>
<td class="confluenceTd"><p>多余资产接收地址</p></td>
</tr>
</tbody>
</table>

</div>

#### 市场参数 （这里不适用于我们V3）

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 参数名 | 类型 / 示例 | 说明 |
| **marketId** | bytes32 | 唯一市场标识，可通过 `CreateMarket` 事件获取 |
| **marketParams** | struct | 包含以下字段：`loanToken`, `collateralToken`, `oracle`, `irm`, `lltv` |
| **loanToken** | address | 借出资产（quote asset） |
| **collateralToken** | address | 抵押资产（base asset） |
| **oracle** | address | 定价预言机（Pyth / Chainlink 等） |
| **irm (InterestRateModel)** | address | 利率模型参数合约 |
| **lltv (Liquidation LTV)** | uint256 | 清算阈值，如 0.85 = 85% |

</div>

#### Flow层核心参数

1\. **风险与限额参数**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 参数 | 示例 | 说明 |
| **supplyCap** | 1,000,000e18 | 允许 Vault 在该市场最大可提供资产量 |
| **flowCap** | {maxIn, maxOut} | 限制 reallocation 的每次流动规模 |
| **maxIn** | 500e18 | 每次最大可注入资金 |
| **maxOut** | 300e18 | 每次最大可提取资金 |
| **timelock on cap change** | ≥1 day | 增加 cap 时需等待 timelock |

</div>

2.  **队列策略**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 队列类型 | 函数 | 说明 |
| **SupplyQueue** | `setSupplyQueue([marketIds])` | 决定资金优先流入市场顺序 |
| **WithdrawQueue** | `updateWithdrawQueue([indexes])` | 决定提款优先顺序 |
| **IdleMarket** | 特殊市场 | 置于 supplyQueue 最后、withdrawQueue 最前。捕捉多余资金，提升提款流动性 |

</div>

#### 收益与激励

1.  **利息收益（Interest Yield）**

> 存入资金的用户会获得来自 Vault 投资策略的收益，来源于底层 Adapter（如 Aave、Compound、或 RWA 收益源）。收益会自动复利在 Vault 中，用户无需手动操作，份额价值会随着资产增长而提升。

- 收益计算：基于真实资产价值增长（realized yield）自动计算。

- 收益体现：用户持有的 Vault 份额（shares）随资产净值上升而增值。

- 特点：Vault 资产增值 → 自动复利 → 存款者增加收益

2.  **Curator 收益（Curator Revenue）**

> Vault 管理者（Curator）通过两种费用机制获得激励：**Performance Fee** 业绩分成& **Management Fee**管理费，用于激励 Curator 优化投资策略与风控，以保持高收益和稳定 AUM。

- **Performance Fee**：随 Vault 产生的真实收益而增长。

- **Management Fee**：按总资产年化计算，提供持续收入。

- 特点：费用调整通过timelock延迟执行。\

#### 质押与惩罚

1.  **Early Withdrawal Penalty**

> 防止频繁套利

- 某些 Curator 可以设定短期资金锁定期（lock period）。若用户在未满足最短质押周期前撤出，则可能被收取小额惩罚费用。

- 若 Vault 设有锁定期，用户提前取出可能被收取少量手续费，用于防止频繁套利、保持资金稳定。

- 惩罚去向：可能分配给留存者或 Vault 的管理金库。

- 特点：在锁定期前取出 → 存款者扣除小额费用 → penalty fee流入vault分配给剩余LP

#### 风险与边界管理

<div class="table-wrap">

|  |  |
|----|----|
| 场景 | 处理方式 |
| **角色被攻破风险** | Owner/Curator 建议使用 multisig/enterprise MPC；使用审计与签名门槛。 |
| **Curator滥权** | DAO投票回滚提案 |
| **Timelock 配置失误** | 上线时保守设置 timelock（如 1-3 天）并逐步放开；重要操作增加多签要求。 |
| **Adapter 错误/资金损失** | 启用 adapter 前必须审计，limits（绝对 cap）应设为保守值，Sentinel 可即时减 cap。 |
| **流动性短缺导致提款阻塞** | 设置高优先级 liquidityAdapter（流动性高、安全）并提供 forceDeallocate（带罚金）机制作为兜底。同时前端清晰展示「可能需要等待的时间」、「force withdraw 罚金」与「即时 vs 非即时提取」状态 |
| **事件/索引延迟** | 后端 indexer 与 keeper 需要容灾设计（多节点、重试机制）。 |
| **Oracle断层 \>120s** | 暂停市场，冻结清算 |
| **RWA 市场关闭** | 延迟PnL结算 |
| **PnL超Cap** | 强制裁剪并记录事件 |
| **Funding异常** | 回退至上次有效值 |

</div>

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

## 一、合约层 Trace Diagram

*(逻辑路径 + 状态变更 + 调用关系)*

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
┌──────────────────────────────┐
│          User (EOA)          │
└──────────────┬───────────────┘
               │ deposit() / withdraw()
               ▼
┌──────────────────────────────┐
│          VaultV2.sol         │
│  - manages shares, caps      │
│  - holds adapters + configs  │
└──────────────┬───────────────┘
               │ via setLiquidityAdapterAndData()
               ▼
┌──────────────────────────────┐
│  MorphoVaultV1Adapter.sol    │
│  - bridge between V2 & V1    │
│  - executes deposit/withdraw │
│  - formats calls to V1 API   │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│          VaultV1.sol         │
│  - ERC4626 underlying logic  │
│  - manages yield strategy    │
│  - holds asset pool          │
└──────────────┬───────────────┘
               ▼
┌──────────────────────────────┐
│      External Protocols      │
│ (Morpho Blue, Aave, etc.)    │
│  - Real yield generation     │
│  - Lending, borrowing, etc.  │
└──────────────────────────────┘
```

</div>

</div>

------------------------------------------------------------------------

## 三、机制详解（产品逻辑与合约内核）

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
|  |  |  |
| **Analytics Dashboard** | 汇总资金曲线、PnL分布、Funding历史 | 可导出CSV |

</div>

## 风险与边界管理

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

</div>
