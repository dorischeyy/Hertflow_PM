# Hertzflow V1 产品文档总览

<div class="Section1">

<div class="panel" style="background-color: #E6FCFF;border-width: 1px;">

<div class="panelContent" style="background-color: #E6FCFF;">

**版本目标**：\
V1 聚焦于完成核心PC与H5端交易闭环，以及测试网相关准备（Trade / HzLP / Swap Dashboard / Risk Control），确保从用户连接钱包 → 划转/下单 → 结算 → 流动性添加/移除 → 查看平台可视化数据分析的完整链路可验证。

</div>

</div>

## 一、总体结构

**组成模块：**

1.  **前端（Web / H5）**

    - 钱包连接、资产展示、交易交互层。

    - 提供市价/限价交易、仓位管理、历史记录与Portfolio聚合。

2.  **合约层（SUI Testnet）**

    - 包含LP池、头寸仓位（Position）、交易撮合、清算逻辑。

    - 数据来源通过Oracle（Pyth + Chainlink），确保报价精准与去中心化。

3.  **中间层（API + Indexer）**

    - 负责同步链上事件、计算实时PnL与仓位状态。

    - 对接Mixpanel埋点与Leaderboard逻辑。

4.  **监控与数据层**

    - 通过Dashboard展示Volume、PnL、Fee、Liquidation等核心指标。

    - 默认时区 UTC。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="04d7b373e1421a6b6718a47a8232aa32381ae07a2fa5c7588b9d55ef3e3efceb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Fig2_Light.png?version=2&amp;modificationDate=1760604147357&amp;cacheVersion=1&amp;api=v2" data-height="850" data-width="1364" data-unresolved-comment-count="0" data-linked-resource-id="19431696" data-linked-resource-version="2" data-linked-resource-type="attachment" data-linked-resource-default-alias="Fig2_Light.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="00cac43a-55c2-4320-83c2-90412e349647" data-media-type="file" width="468" height="291" alt="Fig2_Light.png" /></span>

<div class="table-wrap">

|  |  |
|----|----|
| 模块 | 核心功能 |
| **预言机** | 聚合多源价格数据（Pyth + CEX）用于结算 |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.1-%E4%BF%9D%E8%AF%81%E9%87%91%E7%AE%A1%E7%90%86" rel="nofollow"><strong>保证金管理</strong></a> | 独立仓位抵押、分离风险 |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.2-%E4%BB%93%E4%BD%8D%E7%AE%A1%E7%90%86" rel="nofollow"><strong>仓位管理</strong></a> | 由合约的Custody Account进行多资产独立托管，追踪借贷头寸，管理杠杆倍数与仓位风险 |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.3-%E8%B4%B9%E7%94%A8%E7%BB%93%E6%9E%84" rel="nofollow"><strong>费用结构</strong></a> | 动态费调节OI与流动池权重，保护 LP |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.4-%E8%AE%A2%E5%8D%95%E6%92%AE%E5%90%88%E5%BC%95%E6%93%8E" rel="nofollow"><strong>订单撮合引擎</strong></a> | 原子执行 （PTB）市价单、限价单，保证状态一致 |
| **合约执行层** | 核心链路：Trade → Keeper → Oracle → On-chain PTB |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.5-%E6%B8%85%E7%AE%97%E6%9C%BA%E5%88%B6" rel="nofollow"><strong>清算机制</strong></a> | 自动清算高风险仓位 |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.6-HzLP-%E5%A4%9A%E8%B5%84%E4%BA%A7%E6%B5%81%E5%8A%A8%E6%80%A7%E6%B1%A0" rel="nofollow"><strong>HzLP Pool 多资产流动池</strong></a> | 永续合约对手方资金池 |
| <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#3.7-%E9%A3%8E%E6%8E%A7%E6%8E%AA%E6%96%BD" rel="nofollow"><strong>风控措施</strong></a> | 防范系统性风险 |

</div>

## 二、技术栈概览

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="87207a74e9adef811629f572bcf60af48dc1f9353121b6e9565dc57aa5e55de5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Fig19_Light.png?version=1&amp;modificationDate=1760598237582&amp;cacheVersion=1&amp;api=v2" data-height="823" data-width="1778" data-unresolved-comment-count="0" data-linked-resource-id="19366033" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Fig19_Light.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="f5ebc8f9-74f2-467c-985f-091432885149" data-media-type="file" width="468" height="216" alt="Fig19_Light.png" /></span>

- **核心依赖**：Pyth Oracle / Chainlink / CEX Backup

- **钱包支持**：Slush (primary), Suiet (PC-only)，OKX (Mainnet-only)

- **独立部署：**Testnet 与 Mainnet 使用完全独立的 Oracle Feed、Vault 对象与 Cap 权限，确保测试与主网安全隔离。

- **系统架构：**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="bb82c420-e7cd-4fa3-9a61-f67a77c40947">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>合约名称</p></th>
<th class="confluenceTh"><p>职责</p></th>
<th class="confluenceTh"><p>核心参数</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><code>TradeManager.move</code></p></td>
<td class="confluenceTd"><p>管理交易开平仓、保证金结算</p></td>
<td class="confluenceTd"><p>min_collateral_ratio, max_leverage, funding_rate</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Vault.move</code></p></td>
<td class="confluenceTd"><p>管理资金池资产与盈亏分配</p></td>
<td class="confluenceTd"><p>base_fee_bps, funding_rate_bps, target_weights</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>HzLPPool.move</code></p></td>
<td class="confluenceTd"><p>LP 资产份额与动态权重调整</p></td>
<td class="confluenceTd"><p>add_remove_fee_bps, deviation_threshold</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>OracleCore.move</code></p></td>
<td class="confluenceTd"><p><strong>聚合并喂价</strong></p>
<ul>
<li><p>Pyth 低延迟价格源（&lt; 1s 更新）</p></li>
<li><p>Chainlink 去中心化价格聚合</p></li>
<li><p>Fetcher / Aggregator / Publisher 三层结构</p></li>
<li><p>包括价格精度与容错机制</p></li>
</ul></td>
<td class="confluenceTd"><p>price_update_interval, feed_source</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Keeper.move</code></p></td>
<td class="confluenceTd"><p>定时执行喂价、结算任务</p></td>
<td class="confluenceTd"><p>keeper_cap_address, reward_rate</p></td>
</tr>
</tbody>
</table>

</div>

## 三、核心模块分述

### 3.1 保证金管理

> **设计目标：** 每个仓位独立计息、独立清算，降低交叉爆仓风险。

<div class="table-wrap">

|                  |                                                   |
|------------------|---------------------------------------------------|
| 模块             | 说明                                              |
| **独立仓位模型** | 每个 position 拥有独立 collateral、借贷、PnL 记录 |
| **支持资产**     | SUI / USDC / xBTC / ETH                           |
| **最小抵押额**   | ≥ 10 USD                                          |
| **最大杠杆**     | ≤ 100x                                            |
| **抵押编辑约束** | 不得低于 1.1x 或超过 100x                         |

</div>

**保证金操作：**

- Deposit → 增加 margin，降低杠杆与清算风险

- Withdraw → 减少 margin，提高杠杆，接近清算价

**逻辑公式：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f985d0ac3208537acef1695c8c855d400a0f91e524b8cdfd6a29a7d0b75292ac" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.50.22.png?version=1&amp;modificationDate=1760604643201&amp;cacheVersion=1&amp;api=v2" data-height="67" data-width="696" data-unresolved-comment-count="0" data-linked-resource-id="19366135" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.50.22.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="70c9f1f0-7254-406e-8eaf-5395dbfe20dc" data-media-type="file" width="468" height="45" alt="Screenshot 2025-10-16 at 16.50.22.png" /></span>

当 (MR \< MMR) → 触发清算。

### 3.2 仓位管理

<div class="table-wrap">

|  |  |
|----|----|
| 参数 | 定义 |
| **杠杆 (L)** | <span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8149f3c7e843f7027f8a5443dc768694d5c2885b61f4f9909300e21d5958ce15" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.52.31.png?version=1&amp;modificationDate=1760604773796&amp;cacheVersion=1&amp;api=v2" data-height="54" data-width="198" data-unresolved-comment-count="0" data-linked-resource-id="19366142" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.52.31.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="75e51476-9eca-4990-a7e7-5a62168d67db" data-media-type="file" width="198" height="54" alt="Screenshot 2025-10-16 at 16.52.31.png" /></span> |
| **维持保证金率 (MMR)** | 协议维持仓位的最低保证金要求 |

</div>

**关键逻辑：**

- 所有杠杆流动性均来自 HzLP

- 借贷利率与池子利用率 (Utilization Rate) 动态挂钩

### 3.3 费用结构

<div class="table-wrap">

|                 |                |             |                        |
|-----------------|----------------|-------------|------------------------|
| 类型            | 费率           | 收益归属    | 说明                   |
| 开平仓费用      | 0.06%          | LP          | 所有仓位开关均收取     |
| 划转费用        | 动态           | LP          | 调整池权重、保护流动性 |
| 借贷费用        | 动态，按小时计 | LP          | 借用 HzLP 资金         |
| 清算费用        | 1% collateral  | LP + Keeper | 清算补偿               |
| 流动性添加/移除 | 动态           | LP池        | 按权重偏差收税或返利   |

</div>

#### 逻辑公式：详见<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/2457938/Hertzflow+V1#%E5%9B%9B%E3%80%81%E5%85%B3%E9%94%AE%E6%9C%BA%E5%88%B6%E6%91%98%E8%A6%81" rel="nofollow">关键机制摘要</a>

### 3.4 订单撮合引擎

**流程：**

1.  **逻辑订单下单** — 用户通过前端交易面板提交交易请求（开仓、平仓、限价等）

2.  **Keeper 网络** — 监听触发条件（价格、PnL、MMR）

3.  **预言机报价** — 提供最终结算价

4.  **实际订单的原子性执行(PTB)** — 执行仓位更新、抵押变化与清算逻辑

**执行分层：**

- 逻辑订单：Off-chain 请求创建

- 实际订单：On-chain Keeper请求合约执行

### 3.5 清算机制

**触发条件：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="f16733b0bfcfa5dbcf10fa1ef1df2a644df96cec431739f5e2de008a62ac0e5f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2017.01.09.png?version=1&amp;modificationDate=1760605309495&amp;cacheVersion=1&amp;api=v2" data-height="84" data-width="755" data-unresolved-comment-count="0" data-linked-resource-id="19431729" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 17.01.09.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="8ade0986-98e5-403c-a578-64b85d0e3d5f" data-media-type="file" width="468" height="52" alt="Screenshot 2025-10-16 at 17.01.09.png" /></span>

\
清算由 Keeper 执行，自动偿还借款、销毁仓位并返还剩余抵押。

<div class="table-wrap">

|            |                              |
|------------|------------------------------|
| 参数       | 含义                         |
| Collateral | 剩余抵押资产                 |
| MMR        | 最低维持保证金               |
| Fees       | 借贷 / 开关仓 / 清算费用总和 |

</div>

### 3.6 HzLP 多资产流动性池

HzLP 作为 **永续合约的对手方**，承担所有杠杆借贷与对冲。

<div class="table-wrap">

|          |                                  |
|----------|----------------------------------|
| 功能     | 描述                             |
| 资金来源 | 用户存入 SUI / ETH / xBTC / USDC |
| 收益来源 | 交易者亏损 + 75% 协议费用        |
| 代币表示 | \$HzLP — 按虚拟价格兑换池中资产  |

</div>

**关键逻辑：**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c28284b161e9f3fe76747b290a3610de9dd5c5c46e3a8dbe05175908a380a288" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2017.05.32.png?version=1&amp;modificationDate=1760605557249&amp;cacheVersion=1&amp;api=v2" data-height="283" data-width="989" data-unresolved-comment-count="0" data-linked-resource-id="19366165" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 17.05.32.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="e290e17c-21a0-4751-92e4-120c1517a506" data-media-type="file" width="468" height="133" alt="Screenshot 2025-10-16 at 17.05.32.png" /></span>

当达到上限 (AUM Cap)：\
→ 禁止新增 Mint，仅可二级市场交易。

### 3.7 风控措施

> 协议层面的风控参数配置详见附录中的相关文档部分。

<div class="table-wrap">

|                      |                     |                         |
|----------------------|---------------------|-------------------------|
| 风险类型             | 描述                | 对策                    |
| Directional Exposure | LP 与交易者为对手盘 | 动态借贷率、OI 监控     |
| Liquidity Risk       | 高频清算或提现      | 动态仓位限制、容差带    |
| Keeper Risk          | Keeper 离线或恶意   | 去中心化节点 + 惩罚机制 |
| Oracle Deviation     | 预言机失效或延迟    | 双源验证 (Pyth + CEX)   |

</div>

## 四、关键机制摘要

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="5343d2bf-a2ee-4821-90cd-289cc1bd6cb4">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>机制</p></th>
<th class="confluenceTh"><p>公式 / 逻辑</p></th>
<th class="confluenceTh"><p>默认参数 &amp; 取值</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>保证金率 MR</strong></p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b4fa93e5304a0ff58b494e36cf3b2e90ade5a843be1b5ef8a3c57fd3f196753e" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.16.15.png?version=1&amp;modificationDate=1760602595433&amp;cacheVersion=1&amp;api=v2" data-height="53" data-width="347" data-unresolved-comment-count="0" data-linked-resource-id="19366109" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.16.15.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="ece39dcb-04bd-4f03-87ea-433130d65514" data-media-type="file" width="173" height="26" alt="Screenshot 2025-10-16 at 16.16.15.png" /></span></td>
<td class="confluenceTd"><ul>
<li><p>r_fees = 累计借费率 + 平仓率 + 清算率</p></li>
<li><p>若 MR &lt; MMR → 触发清算（Keeper）</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>未实现盈亏 uPnL%</strong></p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="c5cf348fee6b005b3e6ecbd87ff5994c7e28baa33c7e861aa0954d6affa16a83" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.17.12.png?version=1&amp;modificationDate=1760602651545&amp;cacheVersion=1&amp;api=v2" data-height="33" data-width="282" data-unresolved-comment-count="0" data-linked-resource-id="19431652" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.17.12.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="12ec0569-b028-415e-9490-efe7dabc208f" data-media-type="file" width="173" height="20" alt="Screenshot 2025-10-16 at 16.17.12.png" /></span></td>
<td class="confluenceTd"><ul>
<li><p>用于 MR 与实时风险展示</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Open/Close Fee</strong></p></td>
<td class="confluenceTd"><p>收取头寸常数比例</p></td>
<td class="confluenceTd"><p><strong>6 bps</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Swap Base Fee</strong></p></td>
<td class="confluenceTd"><p>收取划转部分常数比例</p></td>
<td class="confluenceTd"><p>非稳：<strong>30 bps</strong></p>
<p>稳：<strong>4 bps</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Swap Price Imapct</strong></p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="61322a51ef83f335799808533c4e66e9aa2d0cf74f45dba4cdc9d219550b073d" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.20.25.png?version=1&amp;modificationDate=1760602846685&amp;cacheVersion=1&amp;api=v2" data-height="173" data-width="637" data-unresolved-comment-count="0" data-linked-resource-id="19431661" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.20.25.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="e8d9d453-7933-44b8-b265-e15da26501c4" data-media-type="file" width="173" height="46" alt="Screenshot 2025-10-16 at 16.20.25.png" /></span></td>
<td class="confluenceTd"><p><code>tax_bps </code></p>
<p>非稳：<strong>150 bps</strong></p>
<p>稳：<strong>20 bps</strong></p>
<ul>
<li><p>根据操作后流动池偏移权重收取tax或给予rebate</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Add/Remove LP Fee</strong></p></td>
<td class="confluenceTd"><p>同 Swap Fee 逻辑，base fee + rebate/tax 动态调整</p></td>
<td class="confluenceTd"><p>基础费率：<strong>30 bps</strong></p>
<p>δ_max：<strong>2000 bps</strong></p>
<ul>
<li><p>若增仓导致 δ &gt; δ_max → 拒绝操作</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Hourly Borrow Fee</strong></p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="923c87a9e0e547c287a7cb9ea87d03b0a1607084e44387fe4409f59c56c4256f" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.25.14.png?version=1&amp;modificationDate=1760603197458&amp;cacheVersion=1&amp;api=v2" data-height="68" data-width="414" data-unresolved-comment-count="0" data-linked-resource-id="19366121" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.25.14.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="70cc827b-7e7f-47c6-80ff-d0bb34b4e4f9" data-media-type="file" width="174" height="28" alt="Screenshot 2025-10-16 at 16.25.14.png" /></span></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidation Fee</strong></p></td>
<td class="confluenceTd"><p>MMR &lt; 20bps 时清算</p></td>
<td class="confluenceTd"><p><strong>5 bps</strong></p>
<ul>
<li><p>清算费与开平仓费、借费叠加后扣除，剩余返还用户</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>HzLP Price</strong></p></td>
<td class="confluenceTd"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b1bf3f7a48a4a848888e58f1d85b8f85af6393095e11dd9b3aa7590142c50b2b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/2457938/Screenshot%202025-10-16%20at%2016.25.20.png?version=1&amp;modificationDate=1760603306012&amp;cacheVersion=1&amp;api=v2" data-height="58" data-width="302" data-unresolved-comment-count="0" data-linked-resource-id="19398754" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-10-16 at 16.25.20.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="2457938" data-linked-resource-container-version="7" data-media-id="fffe8a71-a11b-41e0-afa9-37e6048c665a" data-media-type="file" width="149" height="28" alt="Screenshot 2025-10-16 at 16.25.20.png" /></span></td>
<td class="confluenceTd"><ul>
<li><p>当 AUM cap 达到 → 禁止 mint 新 HzLP</p></li>
<li><p>当某标的资产池子中的权重偏差值&gt;20%时 → 禁止使用超出的标的mint HzLP</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Keeper Execution</strong></p></td>
<td class="confluenceTd"><p>用户下单逻辑订单 → Keeper 触发 → Oracle 确认价格 → on-chain execute 实际订单</p></td>
<td class="confluenceTd"><p>保证PTB原子化：close → repay borrow → update position</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>LP分润</strong></p></td>
<td class="confluenceTd"><p>平台收25%，剩余收益LP分成</p></td>
<td class="confluenceTd"><p><strong>7500 bps</strong></p></td>
</tr>
</tbody>
</table>

</div>

## 五、附件索引

- 设计稿汇总：<a href="https://www.figma.com/design/AmguvHz2zBT9YzQgH9AVB8/HertzFlow?node-id=3713-8112&amp;p=f&amp;t=0jMnjK7kYFjuGFcK-0" class="external-link" rel="nofollow">Figma</a>

- PRD汇总：<a href="https://hertzflow.atlassian.net/wiki/x/ooAnAQ" data-card-appearance="inline" rel="nofollow">https://hertzflow.atlassian.net/wiki/x/ooAnAQ</a>

</div>
