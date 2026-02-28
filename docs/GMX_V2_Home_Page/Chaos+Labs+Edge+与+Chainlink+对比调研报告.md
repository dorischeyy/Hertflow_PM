# Chaos Labs Edge 与 Chainlink 对比调研报告

<div class="Section1">

## 1. 背景

智能合约无法直接获取链下数据。早期的 DeFi 协议主要依赖单一的价格输入来触发清算或平仓。然而，随着协议复杂度的提升，仅获取当前价格已不足以应对市场风险。协议需要计算在特定流动性深度下的清算滑点，或根据市场波动率动态调整抵押率（LTV）。这种需求推动了预言机功能的分化：基础数据层负责提供可靠的原始市场数据，这是 Chainlink 的主要领域；风险计算层则结合协议状态和市场环境输出决策参数，这是 Chaos Labs 的主要领域。两者在核心功能定位上存在本质区别：

- Chaos Labs 则专注于提供包含风险因素的定价数据。它认为单一的市场价格不足以反映协议面临的实际风险（如流动性不足导致的滑点）\[1, 6\]。Edge 预言机在传输价格时，会结合协议的特定参数（如清算阈值、池子深度）对数据进行调整。其目标是直接输出优化后的决策参数，以降低协议坏账风险并提高资本效率 \[36\]。

- Chainlink 致力于提供标准化的市场数据。其目标是安全地将外部市场价格引入链上，通过聚合多个独立数据源（如 CoinGecko, Kaiko, Binance）的中位数来反映市场价格 \[48, 54\]。这种设计不包含对特定协议风险的判断，输出的是通用的市场公允价格，适用于借贷、衍生品等多种场景。

## 2. Chaos Labs Price Oracle 价格数据来源

Chaos Labs Price Oracle 采用了一种分层级的多源异构数据获取策略。\

### 2.1 数据源的层级分类与选择逻辑

为了确保价格数据的真实性与代表性，Edge 预言机并未简单地接入所有可用数据源，而是根据流动性深度、交易量、监管合规性及技术稳定性，构建了一个严密的“数据源分级体系”（Data Source Hierarchy）。\
\
**对比 Chainlink**：Chainlink 的节点运营商通常依赖专业的第三方数据聚合商（如 Kaiko, BraveNewCoin）作为主要数据来源 \[49, 50\]。这种“聚合器的聚合”模式优势在于稳定性高，屏蔽了单一交易所 API 的不稳定性。然而，这也意味着 Chainlink 节点往往无法直接获取交易所的实时订单簿（Order Book）深度数据。相比之下，Chaos Labs Edge 采用“直连交易所（Direct-to-Exchange）”策略，优先直接接入 CEX 和 DEX 的 WebSocket，仅将聚合器作为三级兜底 \[16, 37\]。这种架构虽然工程复杂度更高，但确保了 Edge 能够获取计算滑点和流动性加权所需的原始微观数据。\
\
**2.1.1 一级数据源：高频中心化交易所（CEX）**\
对于比特币（BTC）、以太坊（ETH）及主流山寨币而言，尽管 DeFi 发展迅猛，但全球定价权的核心依然掌握在头部中心化交易所手中。Edge 预言机优先接入 Binance, Coinbase Pro, OKX, Kraken 等具备极深订单簿厚度的交易所。选择标准不仅基于名义交易量（Volume），更看重“滑点调整后的流动性”（Slippage-Adjusted Liquidity）。这意味着，只有当一个交易所在±2%深度内的挂单量达到特定阈值时，其价格数据才会被纳入一级权重。在连接机制上，Edge 预言机与一级交易所建立持久化的 WebSocket 连接，而非传统的 REST API 轮询（Polling）。WebSocket 允许交易所服务器在订单簿更新的瞬间主动推送数据，将传输延迟降低至 10ms-50ms 级别，远优于 REST API 的 200ms-500ms 延迟。此外，Edge 不仅订阅最新的成交价（Last Traded Price, LTP），更订阅 L2 甚至 L3 级别的订单簿数据（Order Book Data），从而能够计算“买一价”（Best Bid）与“卖一价”（Best Ask）的中间价（Mid-Price），剔除单笔异常成交带来的噪音。\
\
**2.1.2 二级数据源：深流动性去中心化交易所（DEX）**\
对于长尾资产（Long-tail Assets）或链上原生代币，DEX 往往是定价的主战场，主要来源包括 Uniswap V3, Curve, Balancer。DEX 数据面临的最大挑战是矿工可提取价值（MEV）攻击与闪电贷操纵。Edge 预言机在摄取 DEX 数据时，不会直接使用当前区块的瞬时价格（Spot Price），因为这极易被操纵。相反，系统会计算一个极短窗口期（如 1-3 个区块）的时间加权平均价（TWAP），或者利用 Uniswap V3 的 Oracle 接口获取经几何平均处理的价格，以过滤区块内的原子级攻击。\
\
**2.1.3 三级数据源：机构级聚合器**\
作为安全冗余，Edge 预言机还会接入 CoinGecko Enterprise, CCData (CryptoCompare) 等专业数据聚合商的 API。这些数据源通常不直接参与核心定价计算，而是作为“参考汇率”（Reference Rate）。当一级与二级数据源出现巨大偏差（例如 \>5%）时，系统会比对三级数据源，以判断是市场发生了剧烈波动，还是主要数据源出现了技术故障（如 API 冻结）。\

### 2.2 数据清洗与预处理机制

原始数据往往充满了噪音、异常值甚至恶意伪造的交易。在数据进入聚合引擎之前，必须经过严格的清洗流程。\
\
**2.2.1 清洗交易（Wash Trading）过滤**\
某些二线交易所为了刷量，会通过自成交制造虚假的交易量。Edge 预言机利用专有的反欺诈算法，通过分析成交单的时间间隔分布（Time-Interval Distribution）与买卖单大小的本福德定律（Benford's Law）符合度，识别并剔除疑似刷量的数据源。如果某交易所被判定存在大量清洗交易，其在聚合算法中的权重（Weight）将被降级为零。\
\
**2.2.2 跨市场套利检测与延迟对齐**\
不同交易所的物理服务器位置不同（如 AWS 东京与 AWS弗吉尼亚），导致数据到达预言机节点的时间存在差异。所有传入的数据包不仅包含“接收时间”（Ingestion Time），还强制要求包含“生成时间”（Exchange Timestamp）。系统设定了一个动态的“最大容忍延迟”（Max Tolerable Latency）。对于波动率较低的资产，容忍度可能为 1 秒；而对于高波动的 Meme 代币，容忍度可能缩紧至 200ms。任何超过此时间窗口的数据包将被直接丢弃，防止“幽灵价格”（Ghost Price）干扰。

## 3. Chaos Labs Price Oracle 聚合机制

Edge 预言机采用具有更高拜占庭容错能力（BFT）的统计学聚合算法。\

### 3.1 **对比 Chainlink**

\
\
Chainlink 的 OCR（Off-Chain Reporting）协议采用的是标准的“简单中位数”（Simple Median）聚合 \[54, 56, 57\]。每个节点提交一个价格，系统取中间值。这种方法对单点故障有很好的防御性，且去中心化程度高，因为它假设所有节点/数据源的权重是平等的。Chaos Labs Edge 则认为不同交易所的定价权不同，因此引入了“流动性加权中位数（Liquidity-Weighted Median）”算法 \[39, 48\]。Binance 的价格权重自然应高于流动性较差的二线交易所，这种机制不仅考虑了价格的位置，还考虑了该价格背后的资金深度，能更准确地反映市场的真实成交成本。\

### 3.2 流动性加权中位数算法详解

该算法的核心思想是：定价权应与市场深度成正比。一个在 100 万美元深度下成交的价格，其可信度远高于一个在 1000 美元深度下成交的价格。\
\
**3.2.1 权重的计算**\

对于每一个数据源 *Si*，系统计算其权重 *Wi*：

*Wi = α · Depth_2% + β · Volume_24h + γ · TrustScore*

其中 *Depth_2%* 为订单簿在当前价格 ±2% 范围内的挂单总额，*Volume_24h* 为过去 24 小时的有效成交量，*TrustScore* 为基于历史表现（在线率、准确率）的信誉评分。*α, β, γ* 是由 Chaos Labs 模拟引擎动态调整的系数，通常 *α*（深度）占比最高，因为深度代表了操纵成本。

\
**3.2.2 聚合过程**\
聚合过程首先将所有有效数据源的价格 *Pi* 从低到高排序。然后，对应每个价格 *Pi*，关联其权重 *Wi*。接着，寻找满足累积权重条件的 *k* 值，使得前 *k* 个权重的和以及后 *n - k + 1* 个权重的和均大于等于总权重的一半。最终，*Pk*即为最终的聚合价格。这种机制意味着，攻击者若想操纵预言机价格，不仅需要攻破单一交易所的 API，还需要在市场上真金白银地买入/卖出巨额资产以改变订单簿深度，从而获得足够的权重 *Wi*。这极大地提高了攻击成本（Cost of Attack）。\

### 3.3 异常值检测与修剪（Outlier Detection & Trimming）

即使使用了加权中位数，为了进一步提高精度，Edge 预言机在计算前会进行一轮“修剪”（Trimming）。系统利用四分位距（Interquartile Range, IQR）来识别离群值。首先计算第一四分位数 *Q1* 和第三四分位数 *Q3*，进而得出 *IQR = Q3 - Q1*。定义正常区间为 *\[Q1 - k · IQR, Q3 + k · IQR\]*。系数 *k* 通常设为 1.5，但在高波动市场下，风险模型会自动调大 *k* 值（例如调至 3.0），以避免将正常的剧烈波动误判为异常值。任何落在该区间之外的价格点被标记为“异常”，并在当次聚合中剔除。\

### 3.4 置信区间的生成

与大多数预言机仅输出单一价格不同，Edge 预言机计算并输出一个置信度分数（Confidence Score）或价格区间。

*P_oracle = { P_agg, σ_agg }*

其中 *σ_agg* 代表聚合价格的标准差或不确定性。下游协议可以利用这一数据进行防御性编程。例如，在借贷协议中，当 *σ_agg* 很大（即各交易所价格分歧严重）时，协议可以暂停借贷功能，或者降低抵押率（LTV），直到市场恢复共识。

## 4. 风险调整算法：Chaos Labs 的核心优势

数据溯源和聚合构成了预言机的基础架构，而风险调整算法则是其核心逻辑。这是 Chaos Labs Edge 与竞品 Chainlink最大的区别所在。传统的预言机是被动的（Passive），仅反映市场价格；而 Edge 预言机是主动的（Active）和风险感知的（Risk-Aware），它将风险模型直接嵌入到定价流程中。\

### 4.1 基于代理的模拟（Agent-Based Simulation, ABS）

Chaos Labs 的核心竞争力在于其庞大的链下模拟环境。该环境复刻了主网的完整状态，并运行着成千上万个智能代理（Agents），模拟套利者、清算人、巨鲸和黑客的行为。\
\
**4.1.1 仿真引擎（The Simulation Engine）**\
Chaos Labs 的仿真引擎在云端运行 DeFi 协议。该引擎不仅模拟协议代码，还通过创建每个资产（如WBTC, USDC）的市场深度模型以及每个用户（特别是巨鲸）的借贷行为模型，完整复刻了链上状态。系统会运行成千上万次蒙特卡洛模拟（Monte Carlo Simulations），测试在各种极端市场条件下（如ETH单日下跌50%、USDC脱锚、Gas费飙升至1000 gwei）协议的表现。模拟的最终目标是找到一组最优的风险参数（如LTV, Liquidation Threshold, Supply Cap），这组参数能在保证协议坏账率低于特定阈值（如0.1%）的前提下，最大化资本效率。\
\
**4.1.2 参数的离线优化与在线应用**\
预言机的关键参数并非凭空设定，而是通过 ABS 模拟推导出的。这些经过压力测试的参数会被定期（如每日或每周）推送到链上的 Edge 预言机合约中，使其能够根据最新的市场环境自我进化。\

### 4.2 波动率感知的动态更新机制

**对比 Chainlink**：Chainlink 的价格更新机制通常基于静态的“偏差阈值”（Deviation Threshold），例如固定为 0.5% 或 1% \[48\]。无论市场处于横盘还是剧烈波动，这一阈值通常保持不变（除非通过治理流程手动调整）。这种机制在低波动时可能浪费 Gas，而在极端高波动时可能更新不够及时。

Edge 预言机引入了波动率调整的更新逻辑（Volatility-Adjusted Update Logic）。

*T_update = T_base / (1 + λ · Vol_realized)*

其中 *T_update* 为实际触发更新的价格偏差阈值，*T_base* 为基准阈值（如 0.5%），*Vol_realized* 为资产的实际波动率，*λ* 为敏感度系数。当市场波动率飙升时，分母增大，*T_update* 减小。这意味着预言机变得更加灵敏，哪怕价格只移动了 0.1%，也会触发更新。这确保了在暴跌行情中，链上价格能够紧跟链下市场，由于清算线通常非常敏感，这种高频更新能有效防止清算失败导致的协议坏账。

### 4.3 流动性调整估值（Liquidity-Adjusted Valuation, LAV）

对于大额持仓的巨鲸用户，单一的“现货价格”是具有误导性的。如果用户持有价值 1 亿美元的 ETH，他不可能按现价全部卖出，必须承受巨大的滑点（Slippage）。Edge 预言机为协议提供了一种分层估值模型。

*P_LAV(Size) = P_spot · (1 - Slippage(Size, Liquidity))*

Edge 预言机实时监控各级交易所的订单簿深度，构建一个函数 *f(x)* 表示卖出数量 *x* 时对应的平均成交价。当 DeFi 协议查询价格时，可以传入待评估的头寸大小（Position Size），预言机随即返回经滑点调整后的价格。例如，对于持有 \$10,000 的小用户，预言机返回 \$2000（现价）；而对于持有 \$10,000,000 的巨鲸，预言机可能返回 \$1950（考虑滑点后的价格）。这种机制使得巨鲸用户会被更早地触及清算线，虽然看似残酷，实则公平，因为它反映了真实的退出流动性，保护了协议不因巨鲸穿仓而破产。

### 4.4 延迟感知的断路器（Latency-Aware Circuit Breakers）

DeFi 历史上多次黑客攻击利用了“预言机延迟套利”。如果链上价格滞后于链下价格 10 秒，攻击者可以在链下看到价格上涨，然后在链上做多，必赚无疑。Edge 预言机内置了微观结构断路器。系统计算价格变化的速度（Velocity）和加速度（Acceleration），如果 *ΔP / Δt* 超过了物理市场可能的极限（例如 1 秒内上涨 50%，且无重大利好），断路器即被触发。在防御模式（Defensive Mode）下，预言机不会停止报价（这会导致协议停摆），而是会人为扩大买卖点差（Spread）。例如，正常报价为 \$2000，断路器触发后，报价变为买入 \$2010 / 卖出 \$1990。这种扩大的点差吞噬了套利者的潜在利润空间，使得攻击在经济上无利可图，从而在不暂停协议的情况下防御了延迟攻击。\

### 4.5 案例分析：Aave 中的 Cap Guardian 机制

在Aave V3中，Chaos Labs利用Edge Oracle实现了自动化的风险管理流程，这是风险调整算法的典型应用 \[17, 35\]。Edge持续监控链上数据，一旦发现某资产的大户持仓集中度突然上升且链下流动性变薄，风险模型便会计算出当前的Supply Cap已构成潜在的清算风险。随后，Edge Oracle自动发起链上交易，调用Aave的setSupplyCap函数，收紧该资产的存入额度 \[13\]。这一过程阻止了更多高风险资金进入，保护了现有用户的资金安全，且无需人工干预或漫长的DAO投票。为了防止Edge Oracle作恶，合约通常会设置硬性限制（如单次调整幅度限制），这种“防御性编程”确保了即使风险模型出错，协议也不会瞬间崩溃。

## 5. 比较分析：Edge vs. Chainlink的架构设计与实现

### 5.1 链下计算与链上验证架构

由于上述的风险算法（如加权中位数、波动率计算、LAV 模型）计算量巨大，直接在以太坊虚拟机（EVM）上运行成本过高且受限于区块 Gas Limit。因此，Edge 采用**链下计算（Off-Chain Computation） + 链上验证（On-Chain Verification）**的模式。\
\
**对比 Chainlink**：Chainlink 的 OCR 协议同样是链下聚合，但其计算逻辑相对轻量（主要是中位数排序）\[54, 59\]。Chainlink 的核心优势在于其去中心化网络（DON）的规模，通常包含 31 个或更多节点，强调抗审查和去中心化 \[51\]。Chaos Labs Edge 的架构则更侧重于高性能计算能力，其节点需要运行复杂的风险模型和仿真引擎。因此，Edge 的节点网络通常更精简、专业化，采用门限签名方案（如 BLS 签名或 Schnorr 签名）对计算结果达成共识 \[47\]。只有当超过阈值（如 2/3）的节点对同一价格数据包签名时，该数据包才有效。链上合约仅负责验证签名的有效性，不再重复复杂的数学计算，从而极大地降低了 Gas 消耗。Chainlink的架构经历了从简单的请求-响应模型到复杂的OCR（Off-Chain Reporting）共识网络的演进。OCR (Off-Chain Reporting) 协议是Chainlink实现大规模扩展性的核心技术，它将数据的聚合过程转移到链下，实现了 O(1) 的链上交互成本 \[54, 57, 58\]。OCR协议主要包含Pacemaker（起搏器）、Report Generation（报告生成）和Transmission（传输）三个阶段。Leader节点收集Follower节点的观察值，计算中位数并生成聚合签名。OCR严格采用中位数而非平均值，具有很好的鲁棒性，只要超过半数的节点是诚实的，中位数就一定落在诚实节点的取值范围内。

### 5.2 拉取（Pull）与推送（Push）的混合模式

传统的 Push 模型由预言机节点按固定频率或偏差阈值主动将价格写入链上，适用于需要全局状态感知的协议（如 Aave, Compound）。而 Pull 模型（按需）则要求用户在发起交易（如开仓）时，先从链下节点获取最新的签名价格包，并将其作为参数附带在交易中提交上链。\
\
**对比 Chainlink**：Chainlink 长期以来主导了 Push 模型（Data Feeds），为大多数 DeFi 协议提供了标准化的价格服务 \[48\]。近期 Chainlink 推出的 Data Streams 则转向了 Pull 模型以支持高频衍生品交易 \[27, 60, 61\]。Chaos Labs Edge 从设计之初就构建了混合架构，灵活支持双模式：对于永续合约交易所（如 dYdX），它倾向于 Pull 模型，因为这能提供毫秒级的最新价格，消除抢跑（Front-running）风险；对于借贷池，它维持低频的 Push 更新以维持系统活性。此外，面向低延迟与高频交易，Chainlink推出了Data Streams。与传统的Push模式不同，Data Streams采用Pull模式，预言机节点在链下持续生成高频签名报告，用户在发起交易时将最新的签名报告作为Payload一同提交上链 \[27, 62\]。结合Commit-and-Reveal机制，有效防止了抢跑和MEV攻击。

### 5.3 预言机可提取价值（OEV）与 SVR 机制

OEV是目前DeFi基础设施领域竞争最激烈的战场。Chainlink SVR（Smart Value Recapture）的推出，标志着预言机从单纯的成本中心转向了利润创造中心。Chaos Labs 在此过程中扮演了风险校准的关键角色。\
\
**对比 Chainlink**：Chainlink SVR 侧重于提供基础设施，通过重新设计交易流（如通过 Flashbots MEV-Share 拍卖更新权）将 OEV“回收”给协议 \[24, 65, 67\]。它解决了“如何捕获价值”的问题。Chaos Labs 则侧重于解决“捕获价值带来的风险”问题 \[26, 40\]。OEV 拍卖引入了必然的延迟（等待出价）。Chaos Labs 的研究表明，如果延迟过长（例如超过 5 个区块），在极端行情下，资产价格可能进一步下跌，导致清算后的抵押品不足以覆盖债务（坏账）。因此，Chaos Labs 建立了 OEV 监控平台，实时跟踪 SVR 的表现。如果启用 SVR，Chaos Labs 建议协议必须调整清算奖励（Liquidation Bonus）和 LTV \[9, 68, 69\]。具体而言，必须增加清算奖励以吸引搜索者在存在时间不确定性的情况下依然愿意参与竞标；同时降低 LTV 以留出更多的价格缓冲空间。Chaos Labs 通过量化分析，确保协议在追逐 OEV 利润的同时，不会因为预言机延迟而遭受更大的本金损失。\
\
\

## 6. 结论

Edge 认为价格并非单一数值，而是流动性的分布。通过流动性加权和置信区间，它更准确地描述了市场状态。利用链下的大规模代理模拟来动态调整链上参数，是 Edge 区别于静态预言机的核心竞争优势。这种主动防御机制使其能够适应黑天鹅事件。

Chainlink 提供了基础数据传输设施，解决了数据上链的可靠性问题；Chaos Labs 提供了应用层的风险控制逻辑，解决了数据使用的有效性问题。Chainlink 侧重于标准化产品以覆盖更多市场，Chaos Labs 侧重于定制化服务以优化特定协议的风险参数。\

------------------------------------------------------------------------

下面是 **聚焦“预言机服务设计人员真正关心的技术点”** 的**总结版结论表格**（**数据来源、数据质量、聚合算法、风险模型、链上集成模式、延迟策略、安全性、适用场景**等角度切入）

## **🔵 总览表：两类预言机核心差异（技术架构视角）**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 维度 | Chaos Labs Edge Oracle（风险感知型） | Chainlink Data Feeds（通用价格型） |
| **目标定位** | 价格 + 风险参数（主动防御） | 市场公允价（被动提供） |
| **数据源架构** | CEX/DEX 直连 WebSocket + 聚合器兜底 | 数据聚合商聚合 + 节点拉取 |
| **深度数据** | 获取 L2/L3 orderbook | 通常不获取 orderbook |
| **DEX 处理方式** | 使用短窗 TWAP / V3 内置 Oracle 防 MEV | 视为补充来源 |
| **洗量 & 噪声过滤** | 内置清洗交易检测（行为模型、Benford） | 依赖聚合商本身 |
| **跨市场延迟对齐** | 强制 timestamp 校验 + 拒绝超时包 | 较弱（稀疏更新） |
| **聚合算法** | 流动性加权中位数 + IQR 修剪 | 简单中位数 |
| **输出内容** | (价格, σ 不确定性, 风险参数) | 单一价格 |
| **动态更新机制** | 基于波动率动态调节更新阈值 | 固定偏差阈值 |
| **大额滑点模型** | 支持 LAV (Liquidity-Adjusted Valuation) | 不支持 |
| **断路器** | 延迟感知 + 自动扩大买卖价差 | 不支持 |
| **链上计算模式** | 重计算链下、链上仅验签 | OCR 链下聚合 + 链上验签 |
| **签名机制** | 门限签名（BLS/Schnorr） | OCR 多签 |
| **Push/Pull 模型** | 原生混合模式（高频用 Pull） | 传统 Push + Data Streams Pull |
| **OEV 角色** | 负责延迟/风险评估 | 负责 OEV 价值回收基础设施 |

</div>

# 📘 **核心技术点总结（工程视角）**

## **1. 数据源架构与获取方式**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 模块 | Chaos Labs Edge | Chainlink |
| **数据源类型** | CEX（WS）+ DEX（TWAP）+ Aggregator | Aggregator（Kaiko / BNC 等） |
| **连接方式** | CEX WebSocket（10–50ms） | Aggregator API（100–300ms） |
| **是否有 OrderBook** | ✔ L2/L3 深度数据 | ✘ 无深度 |
| **是否执行数据源分级** | ✔（一级 CEX、二级 DEX、三级聚合器） | ✘（节点内部自行决定） |
| **数据质量过滤** | 洗量检测、Benford、延迟过滤 | 信任聚合商本身 |

</div>

👉 **Chaos 适用于需要深度信息、滑点计算、巨鲸风险评估的协议。**

## **2. 聚合层算法**

<div class="table-wrap">

|            |                                 |                          |
|------------|---------------------------------|--------------------------|
| 算法点     | Chaos Labs Edge                 | Chainlink                |
| 聚合方式   | 流动性加权中位数（LWM）         | 简单中位数               |
| 权重依据   | Depth ±2% / Volume / TrustScore | 无权重，节点同权         |
| 异常值过滤 | IQR 修剪（k 动态）              | 不做（仅靠中位数鲁棒性） |
| 输出       | 价格 + σ（不确定性）            | 价格                     |

</div>

👉 **Chaos 更像“价格 + 风险系统”；Chainlink 更像“价格 API”。**

## **3. 风险建模（Chaos 核心差异化能力）**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 风险组件 | Chaos Labs Edge | Chainlink |
| ABS 模拟器 | ✔（推导参数） | ✘ |
| 风险参数上链 | ✔（动态更新 LTV、Caps 等） | ✘ |
| 滑点调整估值（LAV） | ✔ | ✘ |
| 波动率自适应更新 | ✔ | ✘（静态 deviation threshold） |
| 延迟感知断路器 | ✔（自动扩点差） | ✘ |

</div>

👉 **这一部分是 Chaos 的杀手功能，与价格获取无关，而是风险防御。**

## **4. 链上集成与架构**

<div class="table-wrap">

|          |                          |                     |
|----------|--------------------------|---------------------|
| 架构点   | Chaos Labs Edge          | Chainlink           |
| 计算位置 | 链下重计算 → 链上验签    | 链下聚合 → 链上验签 |
| 签名方案 | 门限签名（提高抗作弊性） | OCR 多签            |
| Push     | ✔                        | ✔（主模式）         |
| Pull     | ✔（特别永续场景）        | ✔（Data Streams）   |
| Gas 成本 | 较低（只验签）           | OCR 式正常开销      |

</div>

## **5. 延迟 / MEV / OEV 防御**

<div class="table-wrap">

|                |                              |                   |
|----------------|------------------------------|-------------------|
| 机制           | Chaos Labs                   | Chainlink         |
| 价格延迟监控   | ✔（timestamp 强校验）        | 弱                |
| 高速行情断路器 | ✔（自动扩大买卖点差）        | ✘                 |
| OEV 集成       | 侧重风险（延迟窗口风险建模） | SVR 主导 OEV 流程 |

</div>

# 📌 **整体结论（给预言机系统设计者）**

<div class="table-wrap">

|  |  |
|----|----|
| 结论类型 | 内容 |
| **Chaos Labs Edge 是“风险感知 + 深度感知 + 动态防御”的价格系统** | 在永续、保证金、清算敏感协议中提供真实可执行价格（adjusted, risk-aware）。 |
| **Chainlink 是标准化高可用数据基础设施** | 适合大多数借贷、资产定价、简单清算场景。 |
| **两者定位完全不同，不是功能竞品，而是应用层级不同** | Chainlink = 基础数据层；Chaos = 风险计算层。 |

</div>

------------------------------------------------------------------------

## Reference List

\[1\] Chaos Labs Website - Edge Oracle & Risk Management. <a href="https://chaoslabs.xyz/" class="external-link" rel="nofollow">https://chaoslabs.xyz/</a>\
\[2\] Chaos Labs Blog - Edge AI Alpha Release. <a href="https://chaoslabs.xyz/posts/edge-ai-alpha-release" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/edge-ai-alpha-release</a>\
\[3\] Decrypt - Edge Emerges from Stealth. <a href="https://decrypt.co/249123/edge-the-new-decentralized-oracle-protocol-by-chaos-labs-emerges-from-stealth-with-jupiter-30b-volume-secured-over-the-last-2-months" class="external-link" rel="nofollow">https://decrypt.co/249123/edge-the-new-decentralized-oracle-protocol-by-chaos-labs-emerges-from-stealth-with-jupiter-30b-volume-secured-over-the-last-2-months</a>\
\[4\] Chaos Labs Blog - Introducing Pendle PT Risk Oracle. <a href="https://chaoslabs.xyz/posts/introducing-pendle-pt-risk-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-pendle-pt-risk-oracle</a>\
\[5\] Chaos Labs - Jupiter Integration Details. <a href="https://chaoslabs.xyz/" class="external-link" rel="nofollow">https://chaoslabs.xyz/</a>\
\[6\] Chaos Labs Blog - Introducing Edge: The Next Generation Oracle. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[7\] Chaos Labs Blog - From Messenger Oracles to Intelligent Risk Management. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[8\] Chaos Labs Blog - Edge Oracle Whitepaper/Post. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[9\] Reddit - Aave Integrates Chainlink SVR. <a href="https://www.reddit.com/r/CryptoCurrency/comments/1jmsb2t/aave_integrates_chainlink_svr_to_recapture/" class="external-link" rel="nofollow">https://www.reddit.com/r/CryptoCurrency/comments/1jmsb2t/aave_integrates_chainlink_svr_to_recapture/</a>\
\[10\] Chaos Labs Blog - Edge Advantage. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[11\] GitHub - Aave Proposals Reports (Chaos Labs x Aave). <a href="https://github.com/aave-dao/aave-proposals-reports" class="external-link" rel="nofollow">https://github.com/aave-dao/aave-proposals-reports</a>\
\[12\] Chaos Labs Blog - Oracle Data Replicability Pt.4 (First vs Third Party). <a href="https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4</a>\
\[13\] Aave Governance - Pendle Principal Token Risk Oracle. <a href="https://governance.aave.com/t/arfc-pendle-principal-token-risk-oracle/20962" class="external-link" rel="nofollow">https://governance.aave.com/t/arfc-pendle-principal-token-risk-oracle/20962</a>\
\[14\] Aave Governance - Chaos Labs Risk Oracles. <a href="https://governance.aave.com/t/chaos-labs-risk-oracles/17216" class="external-link" rel="nofollow">https://governance.aave.com/t/chaos-labs-risk-oracles/17216</a>\
\[15\] Chaos Labs Blog - Oracle Risk Portal Features. <a href="https://chaoslabs.xyz/posts/oracle-risk-portal" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-risk-portal</a>\
\[16\] Chaos Labs Blog - Oracle Data Replicability Pt.4 (Methodology). <a href="https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4</a>\
\[17\] Chaos Labs Blog - Aave Integrates Chaos Labs Edge Risk Oracles. <a href="https://chaoslabs.xyz/posts/aave-integrates-chaos-labs-edge-risk-oracles" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/aave-integrates-chaos-labs-edge-risk-oracles</a>\
\[18\] Aave Governance - Pendle PT Risk Oracle Methodology. <a href="https://governance.aave.com/t/arfc-pendle-principal-token-risk-oracle/20962" class="external-link" rel="nofollow">https://governance.aave.com/t/arfc-pendle-principal-token-risk-oracle/20962</a>\
\[19\] Chaos Labs Blog - Oracle Risk Portal Deep Dive. <a href="https://chaoslabs.xyz/posts/oracle-risk-portal" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-risk-portal</a>\
\[20\] Chaos Labs Blog - Edge Proofs: AI-Powered Prediction Market Oracles. <a href="https://chaoslabs.xyz/posts/edge-proofs-ai-powered-prediction-market-oracles" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/edge-proofs-ai-powered-prediction-market-oracles</a>\
\[21\] Chaos Labs Blog - Oracle Data Freshness & Latency. <a href="https://chaoslabs.xyz/posts/oracle-data-freshness-accuracy-latency-pt-5" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-freshness-accuracy-latency-pt-5</a>\
\[22\] Chaos Labs Blog - Edge AI Architecture. <a href="https://chaoslabs.xyz/posts/edge-ai-alpha-release" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/edge-ai-alpha-release</a>\
\[23\] GMX Governance - Implementation of Chaos Labs Risk Oracles. <a href="https://gov.gmx.io/t/implementation-of-chaos-labs-risk-oracles/3861" class="external-link" rel="nofollow">https://gov.gmx.io/t/implementation-of-chaos-labs-risk-oracles/3861</a>\
\[24\] Chainlink Docs - Smart Value Recapture (SVR) Feeds. <a href="https://docs.chain.link/data-feeds/svr-feeds" class="external-link" rel="nofollow">https://docs.chain.link/data-feeds/svr-feeds</a>\
\[25\] GMX Governance - Risk Oracle Integration Details. <a href="https://gov.gmx.io/t/implementation-of-chaos-labs-risk-oracles/3861" class="external-link" rel="nofollow">https://gov.gmx.io/t/implementation-of-chaos-labs-risk-oracles/3861</a>\
\[26\] Chaos Labs Blog - SVR Monitoring Platform. <a href="https://chaoslabs.xyz/posts/svr-monitoring-platform" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/svr-monitoring-platform</a>\
\[27\] Chainlink Docs - Data Streams Architecture. <a href="https://docs.chain.link/data-streams" class="external-link" rel="nofollow">https://docs.chain.link/data-streams</a>\
\[28\] Chaos Labs Blog - Introducing Aave Slope2 Risk Oracle. <a href="https://chaoslabs.xyz/posts/introducing-the-aave-slope2-risk-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-the-aave-slope2-risk-oracle</a>\
\[29\] Chainlink Today - Aave DAO Approves Expanded Use of Chainlink SVR. <a href="https://chainlinktoday.com/aave-dao-unanimously-approves-expanded-use-of-chainlink-svr/" class="external-link" rel="nofollow">https://chainlinktoday.com/aave-dao-unanimously-approves-expanded-use-of-chainlink-svr/</a>\
\[30\] Chaos Labs Blog - Edge vs Simplistic Price Feeds. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[31\] Chaos Labs Blog - First-Party Data Definition. <a href="https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4</a>\
\[32\] Jupiter Forum - Chaos Labs Partnership. <a href="https://discuss.jup.ag/t/chaos-labs-jupiter-partnership/15856" class="external-link" rel="nofollow">https://discuss.jup.ag/t/chaos-labs-jupiter-partnership/15856</a>\
\[33\] Chainlink Docs - Data Streams Push vs Pull. <a href="https://docs.chain.link/data-streams" class="external-link" rel="nofollow">https://docs.chain.link/data-streams</a>\
\[34\] Chaos Labs Blog - Data Freshness (200ms). <a href="https://chaoslabs.xyz/posts/oracle-data-freshness-accuracy-latency-pt-5" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-freshness-accuracy-latency-pt-5</a>\
\[35\] Unchained Crypto - Aave Using Chaos Labs Oracles. <a href="https://unchainedcrypto.com/aave-is-using-new-oracles-by-chaos-labs-to-automate-its-risk-management-system/" class="external-link" rel="nofollow">https://unchainedcrypto.com/aave-is-using-new-oracles-by-chaos-labs-to-automate-its-risk-management-system/</a>\
\[36\] Chaos Labs Blog - The Modern Role of Crypto Oracles. <a href="https://chaoslabs.xyz/posts/the-modern-role-of-crypto-oracles-from-price-messengers-to-intelligent-feeds" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/the-modern-role-of-crypto-oracles-from-price-messengers-to-intelligent-feeds</a>\
\[37\] Chaos Labs Blog - Data Replicability Challenges. <a href="https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-data-replicability-pt-4</a>\
\[38\] Chaos Labs Blog - Edge Powering Jupiter. <a href="https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/introducing-edge-the-next-generation-oracle</a>\
\[39\] Chaos Labs Blog - Liquidity Weighted Pricing Methodology. <a href="https://chaoslabs.xyz/posts/oracle-price-composition-methodologies-pt-3" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-price-composition-methodologies-pt-3</a>\
\[40\] Chaos Labs Blog - SVR Metrics. <a href="https://chaoslabs.xyz/posts/svr-monitoring-platform" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/svr-monitoring-platform</a>\
\[41\] CoinDCX Blog - Chainlink SVR Revolutionizes MEV Recapture. <a href="https://coindcx.com/blog/coindcx-news/chainlink-svr-revolutionizes-mev-recapture-for-defi-protocols-24-december-2024/" class="external-link" rel="nofollow">https://coindcx.com/blog/coindcx-news/chainlink-svr-revolutionizes-mev-recapture-for-defi-protocols-24-december-2024/</a>\
\[42\] Chaos Labs Docs - Architecture. <a href="https://chaoslabs-c6cb6984.mintlify.app/getting-started/architecture" class="external-link" rel="nofollow">https://chaoslabs-c6cb6984.mintlify.app/getting-started/architecture</a>\
\[43\] LangChain Blog - How Chaos Labs Built Multi-Agent System. <a href="https://blog.langchain.com/how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets/" class="external-link" rel="nofollow">https://blog.langchain.com/how-chaos-labs-built-a-multi-agent-system-for-resolution-in-prediction-markets/</a>\
\[44\] LayerZero Ecosystem - Wintermute & Edge Oracle. <a href="https://medium.com/layerzero-ecosystem/industry-leaders-are-building-with-lzread-adf0ce0ff71a" class="external-link" rel="nofollow">https://medium.com/layerzero-ecosystem/industry-leaders-are-building-with-lzread-adf0ce0ff71a</a>\
\[45\] Decrypt - Jupiter Upgrades to Edge. <a href="https://decrypt.co/249123/edge-the-new-decentralized-oracle-protocol-by-chaos-labs-emerges-from-stealth-with-jupiter-30b-volume-secured-over-the-last-2-months" class="external-link" rel="nofollow">https://decrypt.co/249123/edge-the-new-decentralized-oracle-protocol-by-chaos-labs-emerges-from-stealth-with-jupiter-30b-volume-secured-over-the-last-2-months</a>\
\[46\] Chainlink Docs - DataLink. <a href="https://docs.chain.link/datalink" class="external-link" rel="nofollow">https://docs.chain.link/datalink</a>\
\[47\] Chaos Labs - Oracle Risk and Security Standards: Network Architectures and Topologies (Pt. 2). <a href="https://chaoslabs.xyz/posts/oracle-risk-and-security-standards-network-architectures-and-topologies-pt-2" class="external-link" rel="nofollow">https://chaoslabs.xyz/posts/oracle-risk-and-security-standards-network-architectures-and-topologies-pt-2</a>\
\[48\] Chainlink Docs - Price Feeds. <a href="https://docs.chain.link/data-feeds" class="external-link" rel="nofollow">https://docs.chain.link/data-feeds</a>\
\[49\] Chainlink Ecosystem - Node Operator. <a href="https://chainlinkecosystem.com/ecosystem/node-operators/" class="external-link" rel="nofollow">https://chainlinkecosystem.com/ecosystem/node-operators/</a>\
\[50\] LinkWell Nodes - Chainlink Node Operators. <a href="https://docs.linkwellnodes.io/" class="external-link" rel="nofollow">https://docs.linkwellnodes.io/</a>\
\[51\] Chainlink FAQs. <a href="https://chain.link/faqs" class="external-link" rel="nofollow">https://chain.link/faqs</a>\
\[52\] Cryptohopper - Chainlink (LINK). <a href="https://www.cryptohopper.com/" class="external-link" rel="nofollow">https://www.cryptohopper.com/</a>\
\[53\] Medium - Chainlink 2.0: Impossible to Exploit? <a href="https://medium.com/@reubenyang/chainlink-2-0-impossible-to-exploit-85688c942933" class="external-link" rel="nofollow">https://medium.com/@reubenyang/chainlink-2-0-impossible-to-exploit-85688c942933</a>\
\[54\] Chainlink Docs - Offchain Reporting. <a href="https://docs.chain.link/architecture-overview/off-chain-reporting" class="external-link" rel="nofollow">https://docs.chain.link/architecture-overview/off-chain-reporting</a>\
\[55\] LinkRiver Blog - How to Run a Chainlink Node. <a href="https://blog.linkriver.io/how-to-run-a-chainlink-node-understanding-ocr-rpc-nodes-78646067064e" class="external-link" rel="nofollow">https://blog.linkriver.io/how-to-run-a-chainlink-node-understanding-ocr-rpc-nodes-78646067064e</a>\
\[56\] <a href="http://mmapped.blog/" class="external-link" rel="nofollow">mmapped.blog</a> - The off-chain reporting protocol. <a href="https://mmapped.blog/posts/01-off-chain-reporting.html" class="external-link" rel="nofollow">https://mmapped.blog/posts/01-off-chain-reporting.html</a>\
\[57\] Chainlink Research - Off-chain Reporting Protocol. <a href="https://research.chain.link/whitepaper-v2.pdf" class="external-link" rel="nofollow">https://research.chain.link/whitepaper-v2.pdf</a>\
\[58\] Chainlink Research - Offchain Reporting Protocol 3.0. <a href="https://research.chain.link/whitepaper-v2.pdf" class="external-link" rel="nofollow">https://research.chain.link/whitepaper-v2.pdf</a>\
\[59\] Medium - Chainlink Part \#4 Off-Chain Reporting. <a href="https://medium.com/" class="external-link" rel="nofollow">https://medium.com/</a>\
\[60\] Chainlink Today - Chainlink Data Streams Live On Scroll Mainnet. <a href="https://chainlinktoday.com/chainlink-data-streams-live-on-scroll-mainnet/" class="external-link" rel="nofollow">https://chainlinktoday.com/chainlink-data-streams-live-on-scroll-mainnet/</a>\
\[61\] Chainlink - Data Streams: Low-Latency Market Data. <a href="https://chain.link/data-streams" class="external-link" rel="nofollow">https://chain.link/data-streams</a>\
\[62\] Chainlink Blog - Chainlink Data Streams Launch on Mainnet. <a href="https://blog.chain.link/chainlink-data-streams-mainnet-launch/" class="external-link" rel="nofollow">https://blog.chain.link/chainlink-data-streams-mainnet-launch/</a>\
\[63\] Chainlink Blog - Leveling the DeFi Playing Field. <a href="https://blog.chain.link/leveling-the-defi-playing-field/" class="external-link" rel="nofollow">https://blog.chain.link/leveling-the-defi-playing-field/</a>\
\[64\] Medium - APX Finance Is Integrating Chainlink Data Streams. <a href="https://medium.com/" class="external-link" rel="nofollow">https://medium.com/</a>\
\[65\] Chainlink Blog - Chainlink SVR Analysis. <a href="https://blog.chain.link/chainlink-svr-analysis/" class="external-link" rel="nofollow">https://blog.chain.link/chainlink-svr-analysis/</a>\
\[66\] Medium - Oracle Extractable Value (OEV). <a href="https://medium.com/" class="external-link" rel="nofollow">https://medium.com/</a>\
\[67\] Chainlink Blog - Introducing SVR. <a href="https://blog.chain.link/introducing-svr/" class="external-link" rel="nofollow">https://blog.chain.link/introducing-svr/</a>\
\[68\] Aave Governance - \[ARFC\] Aave \<\> Chainlink SVR v1. Phase 1 activation. <a href="https://governance.aave.com/t/arfc-aave-chainlink-svr-v1-phase-1-activation/" class="external-link" rel="nofollow">https://governance.aave.com/t/arfc-aave-chainlink-svr-v1-phase-1-activation/</a>\
\[69\] Aave Governance - \[TEMP CHECK\] Aave \<\> Chainlink SVR v1 integration. <a href="https://governance.aave.com/t/temp-check-aave-chainlink-svr-v1-integration/" class="external-link" rel="nofollow">https://governance.aave.com/t/temp-check-aave-chainlink-svr-v1-integration/</a>\
\[70\] GMX Governance - GMX Listing Committee Season 3. <a href="https://gov.gmx.io/t/gmx-listing-committee-season-3-proposals/" class="external-link" rel="nofollow">https://gov.gmx.io/t/gmx-listing-committee-season-3-proposals/</a>

</div>
