# Part 3. GMX V2 技术细节

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270869851 {padding: 0px;}
div.rbtoc1772270869851 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270869851 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270869851">

- [1. 合约架构图 Contract Architecture](#Part3.GMXV2技术细节-1.合约架构图ContractArchitecture)
- [2. 架构概览](#Part3.GMXV2技术细节-2.架构概览)
  - [2.1. 核心设计原则](#Part3.GMXV2技术细节-2.1.核心设计原则)
  - [2.2. 核心组件与合约类型](#Part3.GMXV2技术细节-2.2.核心组件与合约类型)
  - [2.3. 核心流程示例](#Part3.GMXV2技术细节-2.3.核心流程示例)
  - [2.4. 关键架构要点总结](#Part3.GMXV2技术细节-2.4.关键架构要点总结)
- [3. 代码细节](#Part3.GMXV2技术细节-3.代码细节)

</div>

## 1. 合约架构图 Contract Architecture

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="93cbe1a0322f1e474fa3009c3c8bcfee71aa97bf3d84348d4050755b82bddc36" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/32571481/image-20251104-080015.png?version=1&amp;modificationDate=1762328385016&amp;cacheVersion=1&amp;api=v2" data-height="2968" data-width="5186" data-unresolved-comment-count="0" data-linked-resource-id="32604236" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251104-080015.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="32571481" data-linked-resource-container-version="5" data-media-id="fc772e78-bbe6-4e8f-b56c-f5b4c09deb49" data-media-type="file" width="468" height="267" alt="image-20251104-080015.png" /></span>

> 你可以在这里获取 <img src="504944c74cf89ccc369d8d64a19333c38097c35b54f1a62a38746b8efc42d281" style="margin: 2px; border: 1px solid #ddd; box-sizing: border-box; vertical-align: text-bottom;" width="250" height="250" /> 然后在你本地打开 <a href="https://excalidraw.com" class="external-link" rel="nofollow">excalidraw</a> 观看。

------------------------------------------------------------------------

## 2. 架构概览

### 2.1. 核心设计原则

GMX V2 的设计基于两个核心原则：

- **模块化设计**

  - `Router`（路由器）

  - `Handler`（处理器）

  - `Utils`（逻辑工具）

  - `Vault`（资金仓）

  - `DataStore`（数据存储）

  - `Token`（代币）

这种职责分离使得系统更易于维护和审计

- **异步执行**

大多数用户操作（如开仓、加/减流动性）不会立即执行，而是创建一个挂单。

链下的 **Keeper** 会监控这些订单，并在条件满足时（如价格或时间触发）执行操作，并提供执行时所需的价格数据。

------------------------------------------------------------------------

### 2.2. 核心组件与合约类型

- **Routers** 是用户与 GMX V2 协议交互的主要入口，接收用户请求并发起订单创建流程。

  - **ExchangeRouter** 是与单个 GM 流动性池交互的主入口，主要功能包括：

    - `sendWnt`：发送包装的原生代币（如 WETH）到 `Vault`，通常用于 deposit 或 execution fee。

    - `sendTokens`：发送 ERC20 代币到 `Vault`。

    - `createDeposit`：创建添加流动性的订单。

    - `createWithdrawal`：创建移除流动性的订单。

    - `createShift`：创建跨池转移流动性的订单。

    - `createOrder`：创建开仓、平仓、加仓、减仓或现货兑换的订单。

    - `claimFundingFees`：领取未结算的资金费。

  - **GlvRouter** 是专门用于 GLV（GMX Liquidity Vault）池的路由器，它管理由多个 GM 池组成的代币篮子。

    - `createGlvDeposit`：创建向 GLV 池添加流动性的订单。

    - `createGlvWithdrawal`：创建从 GLV 池提取流动性的订单。

> 在调用上述函数前，用户必须通过 `sendWnt` 或 `sendTokens` 向 `GlvVault` 预存代币和执行费。存代币和执行费。

‌

- **Handlers**：连接用户、Keeper 与逻辑的桥梁\*\*，\*\*扮演验证和访问控制的中间层角色：

  - **订单创建阶段**：由 `Router` 调用，负责验证输入并调用对应的 `Utils` 创建订单。

  - **订单执行阶段**：由 `Keeper` 调用，触发待执行订单的执行逻辑。

  - 常见的 `Handler`：

    - `DepositHandler`

    - `WithdrawalHandler`

    - `ShiftHandler`

    - `OrderHandler`

    - `LiquidationHandler`

    - `GlvHandler`

‌

- **Utils：**核心逻辑引擎，`Utils` 合约包含 GMX V2 的核心业务逻辑，负责计算、状态更新，以及与其他组件（`Vault`、`Token`、`DataStore`）的交互。

  - **Storage Utils**（创建订单数据）

    示例：`DepositUtils`、`WithdrawalUtils`、`OrderUtils`、`GlvDepositUtils` 等。

  - **Execution Utils**（执行逻辑）

    示例：`ExecuteDepositUtils`、`ExecuteWithdrawalUtils`、`ExecuteOrderUtils`。

  - **Position/Swap Utils**

    - `IncreasePositionUtils`：处理开仓/加仓。

    - `DecreasePositionUtils`：处理平仓/减仓。

    - `SwapUtils`：处理代币兑换。

  - **Calculation/State Utils**

    提供价格、PnL、费用等计算逻辑，常被 `Execution Utils` 调用。

    示例：`MarketUtils`、`PositionUtils`、`SwapPricingUtils`、`PositionPricingUtils`。

‌

- **Vaults：临时资金存储**，用于在异步执行流程中临时存放用户资金（保证金、deposit、执行费等）。

  - `OrderVault`

  - `DepositVault`

  - `WithdrawalVault`

  - `GlvVault`

> 当订单被执行时，相关的 `Execute...Utils` 合约会从相应的 `Vault` 中提取所需的资金。比如保证金用于开仓，然后 `keeper` 会赚走执行费用。

‌

- **DataStore：**持久化状态管理，是 GMX V2 的核心状态存储。

  - 存储用户创建的挂单；

  - 维护当前持仓状态；

  - 被各类 `Utils` 合约在创建和执行阶段读写。

‌

- **Tokens：**代表流动性与资产，GMX V2 使用多种代币合约：

  - **MarketToken**：代表特定市场池（如 ETH/USD）的流动性。流动性提供者在存入资产时获得 `MarketToken`，在取出时销毁。

  - **GlvToken**：代表 GLV 池份额的 ERC20 代币，持有一篮子 `MarketToken`。

  - **Underlying Tokens**：底层资产（如 WETH、WBTC、USDC），在 `MarketToken` 合约中作为抵押或交换资产。

‌

- **Keepers 与 Oracles：链下执行核心**

  - **Keepers**：链下机器人，监控 `DataStore` 中的订单。当触发条件满足时，它们获取最新价格并调用合约执行。

  - **Oracles**：在 `Keeper` 执行时由 `Keeper` 临时写入价格，供 `Utils` 合约计算使用。执行结束后价格会被清除。

‌

- **GasUtils：**管理执行费用支付，当 `Keeper` 成功执行订单后：

  - 从 `Vault` 中提取用户预付的执行费；

  - 支付给 `Keeper`；

  - 退还多余部分给用户。

------------------------------------------------------------------------

### **2.3. 核心流程示例**

1.  **添加流动性到 GM 池**

    1.  用户调用 `sendWnt` 或 `sendTokens` → 资金进入 `DepositVault`。

    2.  用户调用 `createDeposit` → 创建订单。

    3.  `ExchangeRouter` → `DepositHandler` → `DepositUtils` → 存储订单到 `DataStore`。

    4.  `Keeper` 监控到订单后获取价格并调用执行函数。

    5.  执行阶段：

        - 从 `Vault` 提取资金；

        - 计算价格、铸造 `MarketToken`；

        - 通过 `GasUtils` 支付 `Keeper` 费用；

        - 删除订单并将新代币转给用户。

2.  **开仓 / swap 流程**

    1.  用户向 `OrderVault` 存入资金。

    2.  调用 `createOrder`。

    3.  `Keeper` 执行订单时：

        - 通过 `Oracle` 设置价格；

        - `ExecuteOrderUtils` 调用 `IncreasePositionUtils` / `DecreasePositionUtils` / `SwapUtils`。

        - 更新仓位或完成兑换；

        - 处理费用并清理订单。

3.  **添加流动性到 GLV 池**

    1.  用户调用 `sendWnt` / `sendTokens` → 资金进入 `GlvVault`。

    2.  调用 `createGlvDeposit`。

    3.  `GlvRouter` → `GlvHandler` → `GlvDepositUtils` 创建订单。

    4.  `Keeper` 执行时：

        - 获取价格并执行逻辑；

        - 存入底层 `MarketToken` 池；

        - 铸造 `GlvToken`；

        - 支付 `Keeper` 费用并将代币转给用户。

------------------------------------------------------------------------

### **2.4. 关键架构要点总结**

- **异步执行是核心**：用户操作只是创建订单，执行由 Keeper 触发。

- **Routers 面向用户，Handlers 面向 Keeper**。

- **Utils 为系统引擎**：核心逻辑和计算均在其中实现。

- **Vault 做缓冲层**：隔离资金与执行过程。

- **Keepers 执行**：负责监控与执行。

- **模块化设计**：提升系统安全性与可维护性。

------------------------------------------------------------------------

## 3. 代码细节

<span style="background-color: rgb(254,222,200);">见 Part 2 的子文档。</span>

</div>
