# Docs底稿

<div class="Section1">

> <a href="https://hertzflow.slack.com/files/U09837G5FB3/F09DNE8S80Z/docs_v1_______.zip" class="external-link" data-card-appearance="inline" rel="nofollow">https://hertzflow.slack.com/files/U09837G5FB3/F09DNE8S80Z/docs_v1_______.zip</a>

## Welcome to Hertzflow

`[figure1] `

**Redefining On-Chain Perpetuals & Liquidity**

HertzFlow is a high-performance perpetual DEX on Sui, purpose-built for high-performance perpetual trading and efficient liquidity provision. We combine deep liquidity, robust mechanism design, and crypto-native innovation to deliver a trading experience that is **transparent, permissionless, and capital-efficient,** all fully on-chain. Whether you're a trader or a liquidity provider, HertzFlow empowers you to seamlessly engage in perpetual markets with diverse order types and various market choices, leveraging cutting-edge risk management and liquidity optimization.\
**What You Can Do With Hertzflow**\

1.  **Trade Perpetuals Across Multiple Asset Classes**\
    Borrow from a deep pool of XBTC, ETH, SUI, or USDC to power your trades. Access leveraged, perpetual exposure with various supported tokens through oracle-secured pricing.

2.  **Provide Liquidity & Earn Real Yield**\
    Deposit various supported tokens into our dynamic liquidity pools, earning real yield from every trade - perp swaps, position opens/closes, borrowing interest, trader losses, and more. Your capital stays productive 24/7, and stay flexible with instant withdrawals.

3.  **Build & Integrate**\
    Leverage our SDKs, APIs, and composable smart contracts to create your own strategies, integrate liquidity into dApps, or launch new markets permissionlessly.

**The Hertzflow Stack**\

1.  **The Protocol**\
    Smart contracts with a capital-efficient Hertzflow Liquidity Pool model design enabling trades using **any supported asset as collateral**, with up to **100× leverage;** dynamic rebalancing adjustments, and oracle-driven pricing.

2.  **The Interface**\
    An intuitive, high-speed trading front-end designed for both pro traders and DeFi newbies.

3.  **The Liquidity Layer**\
    Optimized capital allocation via adaptive pool architecture, reducing slippage while protecting LPs from excessive volatility exposure.

**Why Hertzflow**\

1.  **High-Performance On-Chain Execution:** Trade with asset-flexible margin, up to 100× leverage, and near-instant confirmation with Layer 2 scalability.

2.  **Risk-Optimized Liquidity:** Earn capital-efficient yield with risk-adjusted returns.

3.  **CEX-like, Seamless:** Experience an intuitive, high-performance trading interface that mirrors the familiarity of centralized exchanges while delivering complete on-chain transparency.

## **TRADE ON HERTZFLOW**

### Overview

> Purpose-build for traders who demand execution precision, fee transparency, and capital efficiency

`[figure2] `

Hertzflow is a capital-efficient, fully on-chain perpetual DEX designed for transparency, speed, and composability. Built with a robust Hertzflow Liquidity Pool (HzLP) model, our system empowers traders to open, manage, and close leveraged positions with minimal friction — while providing liquidity providers with sustainable, risk-adjusted returns.

**Key Highlights**\

- **Any Collateral, Any Market:** Borrow from supported assets and instantly swap into the desired leveraged exposure, all within one transaction.

- **Dynamic Risk Controls:** Margin-based liquidation thresholds adapt to leverage used, ensuring predictable risk boundaries.

- **CEX-like Order Execution** – Full range of market, limit, and trigger orders with instant, seamless UX matching the familiarity and precision of centralized exchanges.

- **Predictable & Fair Fees:** A simple, transparent fee model balances LP incentives with trader cost predictability, avoiding hidden slippage or opaque settlement deductions.

- **Trusted by Pros, Powered by SUI:** SUI’s object-based concurrency model enables instantaneous execution of margin trading operations while preventing conflicts in high-concurrency scenarios, as all dependent objects involved in the position are locked and updated atomically during execution.

### Position Management

> Effortless, transparent handling of your open positions.

Hertzflow uses a capital-efficient HzLP model design that includes:\

1.  **Choice of Collateral**: Traders may borrow from any supported asset to swap and use as collateral when opening leveraged positions in a selected market. Each trade is fully isolated from the rest of the portfolio.

2.  **Instant Borrow & Swap:** On order execution, traders borrow from Hertzflow Liquidity Pool (HzLP) using their collateral as margin, and open the position in a single **SUI Programmable Transaction Block (PTB).** The PTB mechanism allows multiple operations - borrowing, swapping, and position creation - to be executed atomically within one transaction block, ensuring **state consistency**: either all steps succeed, or none are applied.Borrowing and swapping is automatically performed against the selected collateral asset at position open, and a borrow fee accrues for the duration of the trade.

3.  **Decoupled Exposure**: There is no separate margin account. Instead, collateral and exposure sit symmetrically in a single position object. This avoids cross-margin spillover while maintaining composability.

4.  **Liquidation Criteria & Keeper Network Execution**: Hertzflow implements continuous **on-chain collateral monitoring** through its **Keeper Network**. Built-in checks continuously evaluate the current Margin Rate (MR) vs. Maintenance Margin Rate (MMR). If MR \< MMR, keeper bots trigger an on-chain liquidation - automated, safe, and transparent.

When placing orders in a selected market, the following parameters are set:\

1.  **Side:** Open Long; Open Short; Close Long; Close Short; Increase Long; Increase Short; Decrease Long; Decrease Short

2.  **Order Type:** Market/Limit/Trigger (Coming Soon)

3.  **Collateral Asset & Amount: Minimum: 10 USD.** Any asset in the collateral whitelist, deposited into the position contract. Collaterals can be adjusted real time when managing positions.

4.  **Exposure & Leverage:** Leverage can be set between **1.1x and 100x.** Position size is calculated automatically from the leverage set and collateral amount.

5.  **Slippage:** All market and swap orders are executed against Hertzflow Liquidity Pool (HzLP). Slippage tolerance can be set per trade — orders that breach this tolerance will revert to protect the trader.

6.  **Entry Price:** Market price for market orders, a limit price set by traders for limit orders. Meanwhile, liquidation price is estimated and updated automatically.

7.  **Exit Price:** For tigger orders, exit price can be set to stop loss or take profit. For market orders, exit price is the executed price at which positions are closed.

### Close Position

> Closed manually, via automated triggers, or through liquidation.

Positions may be settled via market or limit order:\

- **Market:** Trader manually initiates a full or partial settlement for market positions.

- **Limit:** Settles automatically only if mark price reaches or betters limit price.

When a non-liquidated close is executed:\

- **Positive PnL**: Trader receives their initial collateral plus realized trading profit, transferred directly from the liquidity pool.

- **Negative PnL**: Trader receives remaining collateral after losses, with the loss amount retained by the protocol’s liquidity pool.

- **Partial Close**: Proportional PnL is realized based on the closed portion of the position.

### **Liquidation**

> Automated, transparent and precisely risk-managed

Hertzflow implements continuous **on-chain collateral monitoring** through its **Keeper Network**. Built-in checks continuously evaluate a position’s **Margin Rate (MR)** against the **Maintenance Margin Requirement (MMR)**.

For crypto markets, the **MR** is defined as the ratio of **effective collateral** to **position size**, and calculated as:\
MR = Collateral \* (1 + uPnL% − r_fees) / Size \* 100%\
where uPnL% is the unrealized profit and loss rate, and r_fees is the sum of close fee rate, accrued borrow fee rate and liquidation fee rate.

If a position’s MR falls below the MMR, keeper bots trigger an **on-chain liquidation** using SUI’s native **Programmable Transaction Block (PTB)** execution. The PTB ensures that the liquidation - closing the position, repaying borrowed assets from the Hertzflow Liquidity Pool (HzLP), and updating all relevant objects - is executed atomically.\
This approach guarantees that liquidations are:\

- **Automated**: Keeper bots continuously monitor and act without manual intervention.

- **Safe**: PTB execution prevents partial state updates and ensures object ownership consistency.

- **Transparent**: All liquidation transactions are recorded on-chain, providing auditable history for users and auditors.

The liquidation mechanism is coordinated through a decentralized **Keeper Network**, rather than relying on a single liquidator implementation. The Keeper framework will be open-sourced, enabling any participant to operate independent keeper nodes responsible for monitoring margin conditions and executing liquidations. This design distributes responsibility across a wide set of actors, removing single points of failure and enhancing system resilience. When a liquidation is triggered, the executing keeper will be compensated on-chain with **15% of the liquidated collateral** as a liquidation incentive. This reward will be applied consistently, whether the keeper node is operated by the protocol team or by external participants, ensuring proper alignment of incentives and continuous enforcement of margin requirements. Implementation timelines and operational details may evolve, and the final specifications will follow the team’s official roadmap and announcements.

### Order Types

> Supporting dynamic trading needs with clarity and precision

Orders are categorized into three primary execution modes: Market Orders, Limit Orders, and Trigger Orders.

1.  **Market Open**

    1.  **Execution:** At the current mark price, with slippage included.

    2.  **Behavior:** Executes instantly after the transaction is confirmed onchain.

    3.  **Use Case:** Ideal for traders prioritizing speed over price precision.

2.  **Limit Open**

    1.  **Execution:** At the execution price that reaches or betters the trader’s limit.

    2.  **Behavior:** Only fills when the trade can be executed at the limit or better.

    3.  **Use Case:** Ensures price discipline; no slippage beyond the user’s set level.

3.  **Market Close**

    1.  **Execution:** At the current mark price, with slippage included.

    2.  **Behavior:** Immediate closure at prevailing market conditions.

    3.  **Use Case:** Fastest way to exit without price conditions.

4.  **Limit Close**

    1.  **Execution**: Only at the trader’s pre-set limit price or better.

    2.  **Behavior**: Order remains active until filled or canceled.

    3.  **Use Case**: Suitable for take-profit or disciplined exits, but execution is not guaranteed.

5.  **Trigger Open** *(coming soon in Hertzflow)*

    1.  **Execution**: Converts into a market order once the trigger price is hit.

    2.  **Behavior**: Inactive until triggered, then immediately opens a position at the best available market price with slippage included.

    3.  **Use Case:** Standard for stop-loss or take-profit strategies where execution speed is critical.

6.  **Trigger Close** *(coming soon in Hertzflow)*

    1.  **Execution**: Converts into a market order once the trigger price is reached.

    2.  **Behavior**: Prioritizes certainty of exit, but may incur slippage relative to the trigger price.

    3.  **Use Case**: Used for stop-loss and take-profit exits where speed of execution is more important than exact price.

7.  **Liquidation**

    1.  **Execution:** At the current mark price.

    2.  **Behavior:** Automatically executed when margin requirements are breached.

    3.  **Use Case:** Protects liquidity pools from excessive exposure.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="125092a0-5173-4217-8cd1-b56109d4ad26">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>Order Type</p></td>
<td class="confluenceTd"><p>Trigger</p></td>
<td class="confluenceTd"><p>Use Case</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Market</strong><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Mark Price (immediate)</p></td>
<td class="confluenceTd"><p>Entering / Exiting a trade quickly when execution speed is more important than exact price.</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Limit</strong><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Execution price reaches trader’s set limit price</p></td>
<td class="confluenceTd"><p>Opening at a specific target price without compromising on value.</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Trigger</strong> <em>(Coming Soon)</em><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Execution price reaches trader’s set trigger price (immediate)</p></td>
<td class="confluenceTd"><p>Stop-loss or take-profit strategies when you prioritize execution certainty.</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidation</strong></p></td>
<td class="confluenceTd"><p>Mark price hits liquidation threshold</p></td>
<td class="confluenceTd"><p>Platform safeguard to prevent further losses and maintain solvency.</p></td>
</tr>
</tbody>
</table>

</div>

**Note that:** *Trigger orders (Open/Close)* are planned for release soon (subject to roadmap updates), but here’s how they differ from limit orders, as the two concepts are often mixed:\

- **Limit**: Stays active in the order book from placement. Executes only at your set price or better. Great for price discipline, but may never fill in fast markets.

- **Trigger**: Inactive until your trigger price is hit, then becomes a market order. Prioritizes execution over exact price, so slippage is possible.

### Fee Structure

> Transparent, adaptable, and reflective of market conditions, designed for fairness and risk alignment

Hertzflow fee structure is designed to make fees predictable, transparent, and directly tied to the actual cost of trading and liquidity provisioning.\

1.  **Swap Fee:** A flat percentage applied to token swaps, credited to liquidity providers.

2.  **Hourly Borrow Fee:** A time-based fee applied to the notional borrowed when using leverage. This accrues from position open until close on an hourly basis and compensates LPs for capital utilization. The borrow rate is asset-specific and **dynamically adjusts** with utilization.

3.  **Hourly Funding Fee:** A periodic payment between long and short positions to keep open interest balance between longs and shorts, which indirectly keeps perpetual contract prices anchored to the underlying index. Funding rates are recalculated continuously and settle hourly. Positive Rate - Longs pay shorts. Negative Rate - Shorts pay longs.

4.  **Open / Close Fee:** A fixed percentage charged once at position creation/closure. Note that for collateral edits, this is called ‘**deposit/withdraw fee**’.

5.  **Liquidation Fee:** Applied when a position is force-closed due to insufficient margin. The liquidation fee, along with close position fee and accrued borrow fee will be deducted from the remaining collateral. After deduction, remaining fund will be returned back to traders.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="72abf211-4df5-4a4e-aff7-8f7d8ddc6c84">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p><strong>Action</strong></p></td>
<td class="confluenceTd"><p><strong>Fee Type</strong></p></td>
<td class="confluenceTd"><p>Fee Rate</p></td>
<td class="confluenceTd"><p><strong>Purpose</strong></p></td>
</tr>
<tr>
<td rowspan="2" class="confluenceTd"><p><strong>Leverage Trading</strong><br />
</p></td>
<td class="confluenceTd"><p>Swap Fee</p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"><p>Hertzflow differentiates fees depending on the type of asset swap (stable vs. general assets) and applies a separate protocol “tax” in addition to base fees.</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>Hourly Borrow Fee</p></td>
<td class="confluenceTd"><p>Dynamic</p></td>
<td class="confluenceTd"><p>Applied once per position to compensate LPs for capital utilization.<br />
= \frac{\text{tokens borrowed}}{\text{tokens in the pool}}<br />
\times \text{hourly borrow rate} \times \text{PositionSize}</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Position Open / Close</strong></p></td>
<td class="confluenceTd"><p>Open / Close Fee</p></td>
<td class="confluenceTd"><p>0.06%</p></td>
<td class="confluenceTd"><p>Fixed percentage charged on position creation/closure; for collateral adjustments, referred to as <strong>deposit/withdraw fee</strong>.</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidation</strong></p></td>
<td class="confluenceTd"><p>Liquidation Fee</p></td>
<td class="confluenceTd"><p>1%</p></td>
<td class="confluenceTd"><p>Extra fee applied on involuntary closures to mitigate systemic risk.</p></td>
</tr>
</tbody>
</table>

</div>

## LIQUIDITY PROVISION

### Liquidity Strategy

> Designed for liquidity providers who value risk management and long-term yield stability

Our protocol’s liquidity model is built to efficiently serve leveraged perpetual trading while minimizing risk concentration for liquidity providers (LPs). Instead of relying on constant order matching between buyers and sellers, we use a **pooled virtual HzLP architecture** capable of handling **Open Interest (OI) imbalances** and directional exposure, while ensuring trade settlement remains robust even during extreme market moves.

`[figure4] `

1.  **\$HzLP:** Hertzflow Liquidity Provider tokens that represent shares of the liquidity pool.

2.  **Deposits:** LPs contribute supported tokens like SUI, ETH, XBTC and receive \$HzLP representing their share.

3.  **Withdrawals:** LPs maintain on-chain proof of ownership and can exit instantly.

4.  **Fees:** When providing or withdrawing liquidity, a dynamic fee is charged for pool composition rebalancing.

5.  **Earnings:** LPs receive a proportional share of:

    1.  Opening/closing trade fees

    2.  Traders’ losses

    3.  Liquidation fees

    4.  LP deposit/withdraw fees

    5.  Borrow and swap fees (when applicable)

6.  **Risk Management:** Hertzflow’s liquidity is managed against a target weightage per asset. For each token we configure a positive tolerance δ% that bounds how far the current weight c% may deviate from the target weight t% when deposits/withdrawals are executed.

### \$HzLP

> The backbone of Hertzflow with predictability, fairness, and traceable real yield

\$HzLP is the LP token that mirrors liquidity providers’ shares of the Hertzflow Liquidity Pool. Its value evolves over time as fees accrue and the pool earn traders’ losses as their counterparty.

1.  **How the \$HzLP Pool Works**

The \$HzLP Pool aggregates deposits from LPs and deploys them to provide liquidity for all markets on the platform. The liquidity automatically serves as the counterparty to every trade:\

- When traders win (positive PnL): Profits are paid out from the pool to the trader.

- When traders lose (negative PnL): Losses are credited to the pool, increasing its TVL.

1.  **Deposit & Withdraw**

When you add liquidity, the Liquidity Pool mints \$HzLP to your wallet; when you redeem, \$HzLP is burned and you instantly receive equal value of underlying asset. Withdrawals can be made at any time and settled instantly.\

1.  **Dynamic LP Fees**

When providing or withdrawing liquidity, fees are calculated based on the deviation from the pool’s **target token weight** before and after your action. It adjusts dynamically for liquidity actions to reward behaviors that improve pool balance and penalize those that increase imbalance.\

- If your deposit or withdrawal moves the pool **closer to its target weightage** (e.g., adding scarce assets or withdrawing surplus assets), you pay a **lower fee**.

- If your action **increases imbalance** (e.g., adding oversupplied assets or withdrawing scarce ones), the fee will be **higher**.

1.  **Limits**

We cap deposits by a pool-share limit to prevent outsized single-tx growth so that post-trade weightage is kept within a certain band. Similarly, withdrawals are also capped by a per-tx pool shrink limit.\

1.  **Earnings**

Fees (swap, open/close, borrow/funding net, liquidation rewards) and traders’ PnL accrue into the LP pool and are reflected in the **\$HzLP price**.\

### Yield Mechanism

Liquidity Providers (LPs) are the backbone enabling all leveraged trading activity on Hertzflow. By depositing assets into the Liquidity Pool, LPs act as the counterparty to traders — earning yield from fees while bearing controlled market risk. \$HzLP yields come primarily from **fees.** This is due to the fact that over the long term, trading PnL tends to net out (delta-neutral), meaning LP returns are driven mostly by steady fee income.

**Yield Composition**\
Unless otherwise announced by governance, LP earnings include:\

- **Swap Fees** from token conversions.

- **Open/Close Position Fees** from leveraged trades.

- **Borrow & Funding Fees** from capital utilization and open interest balancing.

- **Liquidation Fees** from forced position closures.

- **LP Fees** from LP deposit/withdrawal

- Traders’ net losses.

**Annual Percentage Yield (APY)**\
APY is used to ** estimate the projected annual return based on compounding earnings. It factors in Swap, Close and Borrow Fees, Traders’ Net PnL, LP Deposit/Withdrawal.\
APY\_{total} = \left( 1 + \frac{\sum \left( APR\_{Day} \times c\\\_{\text{token}} \right)}{365} \right)^{365} - 1\
, where c% represents the current weightage of the token in the liquidity pool.

**Fee Distribution**\

- **Liquidity Providers (60%)**\
  LPs receive 60% of all protocol revenues. This compensates them for supplying liquidity and bearing counterparty risk against traders.

- **Protocol Treasury (40%)**\
  The remaining 40% of revenues accrue to the protocol treasury. These funds are reinvested into protocol growth and resilience — including protocol-owned liquidity, gas subsidies, trading competitions, trader rebates, insurance backstops for LPs, and incentive campaigns. The overarching objective is to ensure that treasury revenues ultimately flow back to benefit LPs and traders directly or indirectly.

**Note that**: APY is variable and not guaranteed.\

### Risk Management & Rebalancing

> Hertzflow‘s robust risk mitigation mechanisms

Hertzflow employs several safeguards to protect LP capital：\

1.  **Dynamic Borrowing Rates**

**Utilization ratios** are monitored continuously for Liquidity Pool health. The hourly settled borrow rate is set dynamic to discourage imbalances between long and short open interest.\

1.  **Automatic Keeper-based Liquidation**

Liquidation is triggerred on-chain via smart contracts - no manual intervention needed, saving LPs from catastrophic exposure and keeping traders’ expectations clear.\

1.  **LP Fee Optimization**

Hertzflow uses dynamic fees as a rebalancing tool — it rewards behavior that fixes imbalances and charges more for behavior that worsens them. This keeps the pool composition healthier, improves execution for traders, and makes your LP returns more stable. Multi-asset pool composition and dynamic LP fee also allow LPs to self-select their risk profile.\

1.  **Weightage Deviation Tolerance**

The LP pool targets a **per-asset weightage** t% ∈\[0,1\] and tracks the **current weight** c% ∈\[0,1\]. A **dynamic tolerance band** δ% ≥ 0 is introduced to allow operation around the target. These bands are enforced **per asset** to keep the pool balanced and to limit concentration risk. In high-vol / large OI skew periods, the configurable deviation between current weightage and target weightage can be adjusted timely to prevent extreme imbalance.\

## TUTORIALS

### **Quick Start**

`[Figure 5]`

1.  **What you need**

- **A supported Sui wallet:** <a href="https://suiet.app/install" class="external-link" rel="nofollow"><strong>Suiet</strong></a>**;** <a href="https://www.okx.com/en-sg/download" class="external-link" rel="nofollow"><strong>OKX Wallet</strong></a>**;** <a href="https://slush.app/download" class="external-link" rel="nofollow"><strong>Slush</strong></a>.

- **Gas token:** **SUI**. Keep a small buffer for fees (we recommend **≥ 0.05 SUI** at all times).

- **Collateral / swap assets: SUI / ETH / XBTC / USDC on Sui** and other supported tokens listed in the app.

- A modern browser (Chrome/Brave/Edge) with your wallet extension or mobile in-app browser.

> **Tips:** On Sui, coins are *objects*. If your balance shows as multiple small “coin objects,” your wallet may auto-merge them for spending. If a transaction fails with “insufficient coin,” try hitting **Merge** (most wallets expose this) or reduce the input amount.

`[Figure 6 - 8]`

1.  **Access & connect**

- **Open Hertzflow dapp** and click `Connect` (top right).

- **Select network:** For testing, you will be connected to `Sui Testnet` by default.

- **Claim Faucets:** For testing, you can claim faucets on the top right corner by clicking the `Claim Faucet` button.

- **Settings**: You can change your `Theme`, `Network` and `RPC Settings`.

1.  **Funding your account (Mainnet coming soon)**

- You already hold SUI / USDC / XBTC / ETH on Sui: You’re set. **Keep ≥ 0.05 SUI for gas**, then proceed to Trade or Provide Liquidity.

- Assets on another chain or CEX: **Bridge / On-ramp** with your preferred bridge or on-ramp services to send **SUI** (for gas) and supported tokens **(Sui)** to your connected wallet address.

- **CEX withdrawal:** When withdrawing to Sui, ensure the **network is Sui** (not Ethereum/Solana/etc.), and that the token is native SUI / **USDC / ETH / XBTC on Sui** (contract addresses differ across chains).

> **Note that:** Transfers between chains are **not** instantaneous and may require a swap after bridging. Always verify token symbols and networks before sending.

### Trading

`[Figure 9]`\

1.  **Select a Market**

- Use the **Market dropdown** to choose a pair

- View market info including mark price, 24h CHG%, 24h high, 24h low, open interest, and indicative hourly borrow rates.

`[Figure 10]`\

1.  **Fill in Order Form**

- **Side**: **Long** (expect price to rise) or **Short** (expect price to fall).

- **Order type**:

  - **Market**: Execute now at best available price.

  - **Limit**: Execute at your price or better.

- **Collateral, Leverage, and Size：**

  - **Collateral:** Minimum 10 USD, supported tokens - SUI, USDC, XBTC, ETH

  - **Leverage:** 1.1x to 100x

  - **Size:** Collateral × Leverage

- **Price & Slippage**

  - **Entry Price**: Live mark price for market orders, can be set for limit orders

  - **Slippage Tolerance**: Accepted price difference between execution price and entry price

1.  **Review Order Details and Confirm**

- **Fees:** Hover for a precise breakdown:

  - **Open Fee:** Fixed 0.06% of notional

  - **Swap Fee:** If using a different token as collateral

- **Est. Liq. Price:** The estimated market price at which your position will be forcibly closed by the protocol to prevent your collateral from falling below the **maintenance margin requirement**. It’s calculated in real time based on your **Entry Price**, **Collateral**, **Position Size**, **Leverage**, and **Maintenance Margin Requirement (MMR)**. Maintenance Margin Requirement (MMR) is a set protocol level, which, for crypto markets, is size/max_leverage + accrued fees.

- **Place & Confirm:** Approve in your Sui wallet, and you will be notified your execution status through a toast.

`[Figure 11 - 13]`\

1.  **Track Order Status**

- **Positions:** View market position details, edit collaterals, close or share current position details

- **Orders:** Any open orders that have not yet been executed. You can also adjust limit price or cancel (all) orders in this tab.

- **History:** Archive of all trades that have been fully executed.

`[Figure 14]`\

1.  **Manage Positions**

- **Add Collateral:** Lowers leverage → pushes liquidation further away.

- **Remove Collateral:** Increases leverage → brings liquidation closer.

- **Collateral Edit Limit:** Collaterals are bounded such that

  - **Deposit:** 10 USD ≤ Deposit \< The collateral size that reduces leverage below **Min Leverage 1.1x**

  - **Withdraw:** 10 USD ≤ Withdrawal \< The collateral size that pushes leverage above **Max Leverage 100x**

`[Figure 15]`\

1.  **Close Positions**

- **Market Close:** Partial or full exposure reduction. Fees apply only to the closed notional; funding/borrow accrual adjusts pro-rata.

- **Limit Close:** Partial or full exposure reduction only when market price reaches or betters set limit price. Limit price is bounded by Mark Price ±10%.

- **Liquidation:** If triggered by keepers, a liquidation fee is applied and remaining collateral settles per protocol rules.

**Note that:** For Limit Orders, Hertzflow enforces a price range around the current **Mark Price** (0.9×–1.1×) to ensure safe and reliable execution.\

- **Prevent Unfillable Orders:** Orders with extreme prices may never execute, remaining pending indefinitely and wasting system resources.

<!-- -->

- **Reduce Execution Risk:** Excessively low (for longs) or high (for shorts) prices can trigger failures on-chain, margin shortfalls, or dead orders.

<!-- -->

- **Chain Performance & Concurrency Safety:** Extreme orders increase computational load in high-concurrency environments, potentially causing conflicts or failed transactions.

<!-- -->

- **User Experience:** This also prevent accidental mispricing due to typos or misclicks.Ensures orders remain meaningful for profit-taking or stop-loss purposes.

### Liquidity Providing

`[Figure 16]`

1.  **\$HzLP Overview**

\

- Navigate to the **\$HzLP Vault** page in the app to see its performance.

- **HzLP Price:** This price fluctuates based on supply and demand dynamics of \$HzLP, fee income, and the perceived value of the underlying liquidity pool.

- **APY:** An estimate of the projected annual return based on compounding earnings. It factors in Swap, Close and Borrow Fees, Traders’ Net PnL, LP Deposit/Withdrawal.

- **HzLP Supply:** The total number of tokens that have been minted through liquidity provision.

- **Market Cap:** Calculated by multiplying the current \$HzLP price by supply. It provides an estimate of the total value of \$HzLP in the market.

- **Total liquidity:** The aggregate value of assets within . It represents the total amount of funds available for trading or borrowing within the pool.

- **Composition:** The respective proportions of SUI, USDC, ETH and XBTC within Hertzflow Liquidity Pool.

`[Figure 17]`\

1.  **Liquidity Deposit & Withdrawal**

- Select a token you would like to buy \$HzLP with or sell \$HzLP for.

- Enter the pay amount, or click on balance percentage for shortcut, and the receive token amount will be automatically updated.

  - **Max Deposit:** Capped by the increase in TVL that pushes the current weightage above max allowed deviation from target weightage.

  - **Max Withdrawal:** Capped by the decrease in TVL that reduces the current weightage below max allowed deviation from target weightage.

  - Deposits and withdrawals will be queued until settlement events release capital if current weightage reaches its allowed maximum/minimum.

- **Review Details:** Check slippage and liquidity provision fee. If applicable, an optimal token with a better fee option will be suggested to purchase/receive with.

- **Confirm transaction:** Approve the deposit in your connected Sui wallet.

- **Receive tokens:** First-time purchase of \$HzLP will need an approval in order to be added into your wallet, representing your liquidity position.

`[Figure 18]`\

1.  **Performance Tracking**

- **Pool Size:** Total value of assets currently deposited into Hertzflow Liquidity Pool. Larger pool size generally indicates better trade stability, deeper liquidity, and lower slippage. Traders’ net profit is negative in a market → Asset pool size reduces. Vice versa.

- **Current/Target Weightage:** Current Weightage describes the **present proportion** of each asset in the pool, while Target Weightage defines the **desired or planned proportion** set by Hertzflow. A max allowed deviation is also set to protect LPs from concentration risks.

- **Utilization:** Refers to the extent to which the pool's liquidity is actually being used for trades or borrows. High utilization implies a **larger share of active liquidity**, meaning more assets are frequently traded or borrowed, which result in higher potential earnings for LPs. Low utilization indicates idle assets, signaling potential inefficiencies or under-used capital within the pool.

## **HERTZFLOW RESOURCES**

### Glossary

> 建议用hover tooltip代替 - 这样用户每次hover到一个词语都会看到解释，不用去查找。

1.  **Position Management Terms**

- **Isolated Position:** Each position tracks its own collateral and exposure independently. No cross-margin blending between positions.

- **Collateral Asset:** Any supported token (e.g. SUI, USDC, ETH, XBTC) used by a trader to back a leveraged position.

- **Atomic Borrow & Swap**: When opening positions in Hertzflow perpetual swap markets, traders can open positions via a single on-chain transaction that deposits collateral, allocates margin, borrows against it, and swaps into the desired asset. This atomic process streamlines entry into a perpetual swap contract.

- **Leverage & Exposure:** Leverage defines the multiplier on collateral to determine position size (range: 1.1× to 100×). Exposure = Collateral × Leverage. Adjusting collateral dynamically post-trade adjusts leverage accordingly.

- **Liquidation:** Automated protocol-triggered position closure occurs when collateral + unrealized PnL falls below Maintenance Margin Requirement (MMR), which, for crypto markets, is size/max_leverage + accrued fees.

1.  **Order Types**

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="92f9a649-a252-463c-8514-00e2829e80c4">
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>Order Type</p></td>
<td class="confluenceTd"><p>Activation Trigger</p></td>
<td class="confluenceTd"><p>Behavior</p></td>
<td class="confluenceTd"><p>Best Use Case</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Market</strong><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Execution at the current mark price</p></td>
<td class="confluenceTd"><p>Immediate execution with built-in slippage control</p></td>
<td class="confluenceTd"><p>Fast entry or exit when speed is prioritized</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Limit</strong><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Match or exceed limit price</p></td>
<td class="confluenceTd"><p>Executes only at or better than specified price</p></td>
<td class="confluenceTd"><p>Price-sensitive entries</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Trigger</strong> <em>(Coming Soon)</em><br />
<strong>Open / Close</strong></p></td>
<td class="confluenceTd"><p>Mark price reaches trigger level</p></td>
<td class="confluenceTd"><p>Becomes a market order when activated — executes despite slippage</p></td>
<td class="confluenceTd"><p>Exit strategies based on price action</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidation</strong></p></td>
<td class="confluenceTd"><p>Collateral under MMR set by protocol rules</p></td>
<td class="confluenceTd"><p>Force-close to protect LPs and protocol integrity</p></td>
<td class="confluenceTd"><p>Protocol-enforced systemic safeguard</p></td>
</tr>
</tbody>
</table>

</div>

1.  **Fee Structure**

- **Swap Fee:** A flat percentage applied to token swaps when swapping or opening positions where swapping is involved. Returned to LPs as revenue.

- **Hourly Borrow Fee:** A time-based utilization charge that accrues per hour of active leveraged exposure. Compensates LPs for locked capital.

- **Open / Close Fee:** A fixed 0.06% charge on position opening or closing. For collateral-only changes, this is referred to as a “deposit/withdraw fee.”

- **Liquidation Fee:** A 1% fee imposed when a position is force-closed via liquidation. Serves to deter aggressive leverage and protect the liquidity pool.

1.  **Liquidity Provision**

- **\$HzLP Token:** Represents an LP’s share in Hertzflow Liquidity Pool. Minted on deposit and burned on withdrawal, tracking equity and accrued yield.

- **Deposit / Withdrawal:** Instantly mint or burn \$HzLP against the supported asset. Caps are enforced to control post-trade token weightage relative to target weightage.

- **Dynamic LP Fee:** Fees scale based on deviation from target asset weights. Rebalance gains **→** pay lower fees. Increased imbalance → face higher fees.

- **APY (Annual Percentage Yield):** An estimate of the projected annual return based on compounding earnings. It factors in Swap, Close and Borrow Fees, Traders’ Net PnL, LP Deposit/Withdrawal, and Liquidation Penalties.

- **Weightage Tolerance (δ%):** Each asset has a current weightage (c%), a target weightage (t%) and an allowed deviation (δ%). Pool composition is dynamically guarded within \[t% – δ, t% + δ\] to manage concentration risk.

### Media Kit →

### <a href="https://x.com/Hertzflow_xyz" class="external-link" rel="nofollow"><strong>X →</strong></a>

### <a href="https://t.me/hertzflow_xyz" class="external-link" rel="nofollow"><strong>TG →</strong></a>

### <a href="https://discord.gg/sBQqf2H7ts" class="external-link" rel="nofollow">DC →</a>

### <a href="https://medium.com/@hertzflow" class="external-link" rel="nofollow"><strong>Medium →</strong></a>

## **TEHCNICAL DOCS**

### Overview

`[Figure 19]`\
Hertzflow implements a modular, upgrade-friendly design for decentralized perpetual futures and liquidity management on Sui. At the center lies the **Hub**, a lightweight registry that anchors all user interaction addresses while enabling seamless upgrades of underlying modules. Core logic - funds custody, perps execution, risk controls, and governance - resides in dedicated contracts that can evolve independently without disrupting external integrations.\
The architecture balances **security**, **composability**, and **low-latency execution**:\

- **Security:** All assets are custodied in a single **Vault**, with isolated accounting for liquidity providers and margin traders. Permissioned updates are tightly scoped through capability objects (AdminCap, KeeperCap).

- **Composability:** A shared **Oracle module** provides normalized, manipulation-resistant price feeds to all consumers (Perps Engine, Vault, risk checks).

- **Execution flow:** Users submit requests to the Trade module; Keepers monitor the mempool, trigger execution, and fetch oracle data; execution modules resolve the request using final prices from the Oracle.

The price pipeline leverages **Pyth Network** and **Chainlink** as primary high-frequency source and falls back to **CEX index prices** (Binance, OKX, Bybit, etc.) when necessary. Advanced slippage protection and anomaly handling ensure continuous availability even under oracle failure or market stress.

### Smart Contracts

1.  **List And Responsibilities**

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="7fb8b9a7-31ee-4f2b-87d2-c8e72d4d7f9a">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p><strong>Contract</strong></p></td>
<td class="confluenceTd"><p><strong>Role / Description</strong></p></td>
<td class="confluenceTd"><p><strong>Key Responsibilities</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Hub</strong></p></td>
<td class="confluenceTd"><p>Entry point and registry of the protocol</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Module Registery:</strong> Stores latest addresses of all critical modules (Vault, Perps Engine, etc.)</p></li>
<li><p><strong>Update Control:</strong> Does not execute business logic, enabling upgrades without altering user-facing addresses</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Vault</strong></p></td>
<td class="confluenceTd"><p>Custodian of all assets within the protocol</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Asset Custody</strong>: Holds HzLP liquidity pool and user margin securely.</p></li>
<li><p><strong>PnL Settlement</strong>: Calculates &amp; settles profit/loss per trade.</p></li>
<li><p><strong>Fee Management</strong>: Computes open/close, borrow, and swap fees, allocates to LPs &amp; treasury.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Hertzflow Liquidity Pool (HzLP)</strong></p></td>
<td class="confluenceTd"><p>Minting &amp; burning of HzLP tokens, managing liquidity</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Mint HzLP</strong>: Issues tokens proportional to deposits.</p></li>
<li><p><strong>Burn HzLP</strong>: Burns tokens and returns underlying assets + yield.</p></li>
<li><p><strong>Valuation</strong>: Computes real-time NAV for \$HzLP.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Perps Engine</strong></p></td>
<td class="confluenceTd"><p>Core trading engine for perpetual positions</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Position Management</strong>: Handles Open, Increase, Decrease, Close.</p></li>
<li><p><strong>Margin Checks</strong>: Validates collateral before execution.</p></li>
<li><p><strong>Liquidation</strong>: Monitors maintenance margin; triggers forced closure.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Governance</strong></p></td>
<td class="confluenceTd"><p>DAO-controlled contract to manage protocol parameters</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Parameter Management</strong>: Voting to adjust fees, margins, risk parameters, new assets.</p></li>
<li><p><strong>Protocol Upgrades</strong>: Authorizes upgrades to core contracts.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Oracle</strong></p></td>
<td class="confluenceTd"><p>On-chain price information interface</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Price Verification</strong>: Validates timestamps, confidence intervals, and volatility to prevent manipulation.</p></li>
<li><p><strong>Price Provision</strong>: Supplies trusted real-time prices to Vault and Perps Engine.</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

1.  **Core Parameters**

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="251408a8-50a7-490a-8fab-0c6edaca1154">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>Parameter</p></td>
<td class="confluenceTd"><p>Summary</p></td>
<td class="confluenceTd"><p>Details</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Trading Fees</strong></p></td>
<td class="confluenceTd"><p>Fee structure across all trading activities</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Base Fee Rate</strong>: Percentage fee on open, close, and decrease operations.</p></li>
<li><p><strong>Funding Fee Rate</strong>: Time-based fee to balance long/short OI.</p></li>
<li><p><strong>Liquidation Fee Rate</strong>: Extra fee charged on forced liquidations.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Slippage Tolerance</strong></p></td>
<td class="confluenceTd"><p>Price deviation safeguard</p></td>
<td class="confluenceTd"><ul>
<li><p>Maximum allowed deviation between expected and executed price.</p></li>
<li><p>Exceeding threshold → automatic transaction revert.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Initial Margin Ratio (IMR)</strong></p></td>
<td class="confluenceTd"><p>Minimum collateral to open positions</p></td>
<td class="confluenceTd"><ul>
<li><p>Ratio of collateral-to-position size required.</p></li>
<li><p>Formula: Initial Margin = 1 / Max Leverage.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Max Leverage</strong></p></td>
<td class="confluenceTd"><p>Upper bound on leverage usage</p></td>
<td class="confluenceTd"><ul>
<li><p>Maximum leverage per position.</p></li>
<li><p>mpacts margin requirements &amp; liquidation thresholds.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Token Weights</strong></p></td>
<td class="confluenceTd"><p>Asset allocation in HzLP pool</p></td>
<td class="confluenceTd"><ul>
<li><p>Target weights for SUI, ETH, BTC, USDC.</p></li>
<li><p>Determines swap pricing, liquidity balancing, and pool risk profile.</p></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

1.  **Price Oracle Architecture**

> Accurate and tamper-resistant price discovery is a cornerstone of the Hertzflow protocol. Our oracle design balances **decentralization, reliability, and latency requirements** to serve both trading and risk management functions.

The Hertzflow oracle design ensures:\

- **Primary reliance** on decentralized, manipulation-resistant feeds (Pyth).

- **Automatic degradation** to high-quality CEX index prices when needed.

- **Liquidity-aware weighting** for fallback aggregation.

- **Multi-layer resiliency** with redundancy at both the runtime and infrastructure levels.

**3.1 Aggregator Strategy**\

- **Primary Source – Pyth Network**\
  Hertzflow prioritizes high-frequency decentralized price streams from **Pyth Network**. Pyth aggregates prices and confidence intervals from multiple independent publishers, applying a PoS-weighted mechanism to produce manipulation-resistant reference prices.

- **Fallback Source – CEX Index Prices**\
  If Pyth data is unavailable or stale beyond **3 seconds**, the system degrades gracefully to an **index price feed** aggregated from leading centralized exchanges (Binance, OKX, Bybit).

**3.2 Update Frequency**\

- **Latency Guarantees**\
  **p99 latency**: ≤ 1–2 seconds, ensuring keepers‘ liquidation and settlement logic remains real-time.\
  **p999 latency**: bounded by a stricter upper limit (configurable) to guarantee global stability under stress conditions.

**3.3 Oracle Node Selection**\

- **Decentralized Path (Preferred)**: Pyth Network for resilient, publisher-aggregated price feeds. To eliminate reliance on third-party APIs and avoid rate limits, we self-host Pyth’s core infrastructure components including `pythnet-rpc`, `wormhole-spy`, and `hermes`.

- **Centralized Path (Fallback)**: CEX feeds selected strictly from venues with top-tier depth and reputation (Binance, OKX, Bybit). Feeds are consumed via WebSocket subscriptions to minimize latency. Redundancy across exchanges ensures continuity even if individual feeds degrade.

**3.4** **Slippage Protection Mechanism**\
When fallback aggregation relies on CEX data, Hertzflow enforces a **liquidity-weighted scoring system** to prioritize healthier order books:\

- **Depth Score (a):** Sum of bid/ask liquidity within ±1% of current price.

- **Support Ratio (b):** Ratio of near-book (top 3 levels) to mid-book liquidity, measuring order book resilience.

- **Balance Score (c):** Relative balance of total bids vs. asks, reflecting buy/sell symmetry.

The composite score is calculated as:\
`Score_{exchange} = w_1 × a + w_2 × b + w_3 × c`\
Scores are used as weights in the final aggregated index, ensuring **high-liquidity venues contribute more heavily** to the effective oracle price.

**3.5 Exception Handling & Failover**\
To maintain uninterrupted pricing, the system implements **multi-layered resiliency mechanisms**:\

- **Real-Time Failover**: Wait up to **3s** for Pyth updates. If data remains stale, immediately switch to the fallback CEX index.

- **Continuity Assurance**:

  - **Quick Fixer**: Patches short-term gaps detected at runtime.

  - **Gap Fixer**: Scheduled process validating DB continuity and repairing missed intervals.

  - **Lazy Filler**: On-demand backfill during query time for external consumers.

- **Architecture-Level Redundancy**: Fetcher and Aggregator services run in **active-active multi-instance mode**, eliminating single points of failure.

This architecture delivers a **highly available, low-latency, manipulation-resistant oracle service**, supporting both normal trading and stress scenarios with predictable guarantees.

1.  **Move Modules & Interfaces**

**4.1 Core Price Module (**`oracle_core`**)**\
**Purpose:** Store and provide authoritative price data.\
**Key Object:** `PriceStore`\

- Mapping: `Symbol -> Price`

- `Price` struct fields:

  - `value: u64` – latest price

  - `timestamp: u64` – Unix timestamp

  - `keeper_signature: vector<u8>` – signature from Keeper

**Access Control:**\

- Only `KeeperCap` holders can write (`update_price`).

- Public read-only access via `get_price`.

**Interfaces:**\

- `update_price`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
entry fun update_price(cap: &KeeperCap, symbol: vector<u8>, price: u64, timestamp: u64, signature: vector<u8>)
```

</div>

</div>

- **Purpose**: Allows an authorized Keeper to update the price of a trading pair.

- **Workflow**:

  - Off-chain aggregation services produce a new price point.

  - The aggregator signs the price data with its private key.

  - The Keeper submits an on-chain transaction carrying the `KeeperCap` as proof of authorization.

  - The smart contract verifies both the signature and the `KeeperCap` before writing to `PriceStore`.

- `get_price`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
public fun get_price(store: &PriceStore, symbol: vector<u8>): (u64, u64)
```

</div>

</div>

- **Purpose**: Provides a read-only interface for other on-chain modules (e.g., DEXs, lending protocols) to access the latest price and timestamp.

- **Use Case**: Essential for accurate trade settlement, margin calculations, and liquidation logic.

**4.2 Permission Management Module (**`oracle_admin`**)**\
**Purpose:** Manage access to price updates; decouples governance from price logic.\
**Capability Objects:**\

- `AdminCap`: Unique authority, held by protocol owner.

- `KeeperCap`: Issued by `AdminCap` to off-chain Keeper wallets.The **Permission Management Module** separates access control from core price logic, ensuring modularity and security. Its primary purpose is to manage **authorization capabilities** for price updates.

**Interfaces:**\

- `grant_keeper_cap`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
grant_keeper_cap(admin_cap: &AdminCap, recipient: address)
```

</div>

</div>

- **Purpose:** Grants a new `KeeperCap` to a specified off-chain Keeper wallet.

- `revoke_keeper_cap`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
revoke_keeper_cap(admin_cap: &AdminCap, keeper_cap: KeeperCap)
```

</div>

</div>

- **Purpose:** Revokes a Keeper’s authorization by destroying the associated `KeeperCap`.

*All administrative operations require* `AdminCap` *as the first argument, enforcing centralized governance and security.*

**4.3 Trading Pair Registration Module (**`symbol_registry`**)**\
**Purpose:** The **Symbol Registry Module** manages all trading pair symbols (`Symbol`) supported by the oracle. Its main responsibility is maintaining an **on-chain allowlist** of valid trading pairs.\

- Protocol administrators (AdminCap holders) can dynamically **add, enable, or disable** trading pairs.

- Before accepting a price update, `oracle_core` queries `symbol_registry` to ensure that the trading pair is **officially supported**.

- This validation prevents updates to invalid, deprecated, or unsupported trading pairs, maintaining data integrity across the protocol.

1.  **Independent Deployments**

Mainnet and testnet deploy completely separate contract instances. This ensures that all on-chain objects—including `PriceStore` and `AdminCap` - have distinct Object IDs per environment. Off-chain services must also be configured separately, including connections to different Sui RPC nodes, Kafka topics, and database instances (e.g., InfluxDB or PostgreSQL). This prevents test data from contaminating production and ensures that test workloads do not impact mainnet performance.

**5.1 Key and Permission Management:**\
Keeper wallet addresses and private keys are fully isolated between mainnet and testnet.\

- **Price Signing:**

  - Mainnet keys must be secured using Hardware Security Modules (HSM) or multi-signature schemes.

  - Testnet keys may follow a more relaxed security policy.

- **AdminCap Management:**

  - `AdminCap` addresses are distinct per network.

  - Mainnet` AdminCap` should reside in a highly secure cold wallet or multi-signature wallet.

**5.2 Data Sources and Dependencies:**\
Off-chain services rely on decentralized and centralized price feeds such as Pyth Network and CEX APIs. Data sources are strictly segregated across environments:\

- **Testnet** `Fetcher`**:**

  - Connects to sandbox/test endpoints of CEX APIs.

  - Uses public testnet Hermes API from Pyth.

- **Mainnet** `Fetcher`**:**

  - Connects to production-grade CEX APIs.

  - Uses self-hosted Pythnet RPC and Hermes services.

## **SECURITY**

### Risk Mitigations

While Hertzflow is designed to minimize risk for both traders and liquidity providers through robust risk controls, decentralized leveraged trading carries inherent risks. We recommend participating only with funds you are comfortable risking, and keeping a close eye on your positions during periods of heightened market volatility.\

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="faff8c65-184d-45b6-99e7-cd476f1847d3">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p><strong>Risk Type</strong></p></td>
<td class="confluenceTd"><p><strong>Definition / Impact</strong></p></td>
<td class="confluenceTd"><p><strong>Our Mitigation Mechanisms</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Directional Exposure Risk</strong></p></td>
<td class="confluenceTd"><p>LPs become unintentionally exposed to price movements when there’s a high open interest (OI) imbalance, especially under volatility.</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Dynamic Borrowing Rates:</strong> Utilization ratios are monitored in real time, adjusting hourly borrow rates to discourage extreme OI skew.</p></li>
<li><p><strong>Dynamic LP Fees:</strong> LP deposit and withdraw fees scale with imbalance/volatility to incentivize OI rebalancing.</p></li>
<li><p><strong>OI Monitoring:</strong> Continuous tracking of imbalance metrics to adjust parameters proactively.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Liquidity Risk</strong></p></td>
<td class="confluenceTd"><p>Traders may be unable to open/close positions at desired size or LPs may face withdrawal delays during high utilization.</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Dynamic Position Limits (DPL):</strong> Restricts outsized position openings during extreme market conditions.</p></li>
<li><p><strong>Weightage Deviation Tolerance:</strong> Enforces per-asset balance bands to prevent concentration risk and keep liquidity accessible.</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Keeper Risk</strong></p></td>
<td class="confluenceTd"><p>Losses from inactive, malicious, or underperforming keepers that handle trade execution, liquidations, and price updates.</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Automated Smart Contract–Driven Liquidation:</strong> Liquidations are executed deterministically on-chain, triggered by protocol-defined conditions without manual intervention or discretionary delays.</p></li>
<li><p><strong>Decentralized Keeper Network Operation:</strong> Multiple independent keeper nodes participate in execution. Each operator is required to post collateralized stake, ensuring economic alignment and accountability.</p></li>
<li><p><strong>Slashing &amp; Incentive Layer:</strong> A slashing framework penalizes inactive or malicious keepers, while rewarding timely and accurate execution. This maintains high-quality service across the network.</p></li>
<li><p><strong>Redundant Failover Systems:</strong> Backup keeper nodes and automated failover mechanisms guarantee continuity of liquidation services, even under high network congestion or node outages</p></li>
</ul>
<p>3,4有无？</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>Oracle &amp; Price Deviation Risk</strong></p></td>
<td class="confluenceTd"><p>Settlement prices may deviate from order prices due to latency or oracle feed misalignment.</p></td>
<td class="confluenceTd"><ul>
<li><p><strong>Dual-oracle Validation:</strong> Price feeds are cross-verified using both <strong>Pyth</strong> and <strong>Chainlink</strong>, with an internal keeper-driven index providing additional redundancy.</p></li>
<li><p><strong>Deviation Threshold Enforcement:</strong> Trades are automatically rejected if submitted prices deviate beyond predefined thresholds relative to validated oracle values, protecting the system from manipulation and stale data.</p></li>
<li><p><strong>Time Travel Execution:</strong> In the event of oracle or network outages, eligible delayed orders may be executed retroactively at historically validated fair prices, ensuring fairness and continuity of execution without penalizing traders for infrastructure downtime.</p></li>
</ul>
<p>第三个有无？</p></td>
</tr>
</tbody>
</table>

</div>

### Audits

### Bug Bounties

TBA\

## **LEGAL**

### T&C

### Privacy Policies

</div>
