# Non-tech Docs底稿

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772007956741 {padding: 0px;}
div.rbtoc1772007956741 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772007956741 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772007956741">

- [1.1 Mainstream Asset Oracle](#Non-techDocs底稿-1.1MainstreamAssetOracle)
- [1.2 Collateral Management](#Non-techDocs底稿-1.2CollateralManagement)
  - [Long Positions](#Non-techDocs底稿-LongPositions)
  - [Short Positions](#Non-techDocs底稿-ShortPositions)
- [1.3 Leverage Management](#Non-techDocs底稿-1.3LeverageManagement)
  - [Understanding Leverage on Hertzflow](#Non-techDocs底稿-UnderstandingLeverageonHertzflow)
  - [Setting Leverage](#Non-techDocs底稿-SettingLeverage)
  - [Margin and Maintenance Margin](#Non-techDocs底稿-MarginandMaintenanceMargin)
  - [Risks of Using Leverage](#Non-techDocs底稿-RisksofUsingLeverage)
- [1.4 Fee Structure](#Non-techDocs底稿-1.4FeeStructure)
  - [Core Parameter Summary](#Non-techDocs底稿-CoreParameterSummary)
  - [Open / Close Fee](#Non-techDocs底稿-Open/CloseFee)
  - [Swap Fee](#Non-techDocs底稿-SwapFee)
  - [Liquidation Fee](#Non-techDocs底稿-LiquidationFee)
  - [Target and Current Weightage](#Non-techDocs底稿-TargetandCurrentWeightage)
  - [LP Add / Remove Fees](#Non-techDocs底稿-LPAdd/RemoveFees)
- [1.5 Limit Order](#Non-techDocs底稿-1.5LimitOrder)
  - [Quick Reference Table](#Non-techDocs底稿-QuickReferenceTable)
- [1.6 How Hertzflow Executes Trades](#Non-techDocs底稿-1.6HowHertzflowExecutesTrades)
  - [Order Execution Flow](#Non-techDocs底稿-OrderExecutionFlow)
  - [Example of a Perpetual Trade on Hertzflow](#Non-techDocs底稿-ExampleofaPerpetualTradeonHertzflow)
- [1.7 liquidation](#Non-techDocs底稿-1.7liquidation)
  - [How Liquidation Works](#Non-techDocs底稿-HowLiquidationWorks)
  - [Factors Affecting Liquidation Price](#Non-techDocs底稿-FactorsAffectingLiquidationPrice)
  - [Monitoring Margin and Liquidation](#Non-techDocs底稿-MonitoringMarginandLiquidation)
  - [Liquidation Execution](#Non-techDocs底稿-LiquidationExecution)
  - [2.1 Hertzflow Liquidity Pool (HzLP) Overview](#Non-techDocs底稿-2.1HertzflowLiquidityPool(HzLP)Overview)
  - [2.2 \$HzLP Token](#Non-techDocs底稿-2.2$HzLPToken)
  - [2.3 How the HzLP Pool Works](#Non-techDocs底稿-2.3HowtheHzLPPoolWorks)
  - [2.4 Custodies](#Non-techDocs底稿-2.4Custodies)
  - [2.5 Assets Under Management (AUM)](#Non-techDocs底稿-2.5AssetsUnderManagement(AUM))
  - [2.6 Virtual Price, Market Price, and AUM Limits](#Non-techDocs底稿-2.6VirtualPrice,MarketPrice,andAUMLimits)
  - [2.7 Calculating Global Unrealized PnL](#Non-techDocs底稿-2.7CalculatingGlobalUnrealizedPnL)
  - [2.8 Exposure & Risks](#Non-techDocs底稿-2.8Exposure&Risks)
- [1. Account & Funds Management](#Non-techDocs底稿-1.Account&FundsManagement)
  - [Q1: How do I fund my Hertzflow account?](#Non-techDocs底稿-Q1:HowdoIfundmyHertzflowaccount?)
  - [Q2: What are “native tokens” and “contract tokens”?](#Non-techDocs底稿-Q2:Whatare“nativetokens”and“contracttokens”?)
  - [Q3: Can I withdraw my liquidity at any time?](#Non-techDocs底稿-Q3:CanIwithdrawmyliquidityatanytime?)
- [2. Trading & Leverage Management](#Non-techDocs底稿-2.Trading&LeverageManagement)
  - [Q1: How do I select a market?](#Non-techDocs底稿-Q1:HowdoIselectamarket?)
  - [Q2: What is leverage?](#Non-techDocs底稿-Q2:Whatisleverage?)
  - [Q3: How is the liquidation price calculated?](#Non-techDocs底稿-Q3:Howistheliquidationpricecalculated?)
  - [Q4:How to Calculate PnL？](#Non-techDocs底稿-Q4:HowtoCalculatePnL？)
  - [Q5: What is the Maintenance Margin Requirement (MMR)?](#Non-techDocs底稿-Q5:WhatistheMaintenanceMarginRequirement(MMR)?)
  - [Q6: How can I avoid liquidation?](#Non-techDocs底稿-Q6:HowcanIavoidliquidation?)
  - [Q7: What happens if my position is liquidated?](#Non-techDocs底稿-Q7:Whathappensifmypositionisliquidated?)
- [3. Liquidity Provision & Earnings](#Non-techDocs底稿-3.LiquidityProvision&Earnings)
  - [Q1: Why provide liquidity?](#Non-techDocs底稿-Q1:Whyprovideliquidity?)
  - [Q2: What is \$HzLP?](#Non-techDocs底稿-Q2:Whatis$HzLP?)
  - [Q3: How to get \$HzLP](#Non-techDocs底稿-Q3:Howtoget$HzLP)
  - [Q4：How to Become a Liquidity Provider](#Non-techDocs底稿-Q4：HowtoBecomeaLiquidityProvider)
  - [Q5: How to Calculate APY?](#Non-techDocs底稿-Q5:HowtoCalculateAPY?)
  - [Q6: How do I withdraw from the liquidity pool?](#Non-techDocs底稿-Q6:HowdoIwithdrawfromtheliquiditypool?)
- [4. Risk Management & Strategy](#Non-techDocs底稿-4.RiskManagement&Strategy)
  - [Q1: How can I manage my trading risk?](#Non-techDocs底稿-Q1:HowcanImanagemytradingrisk?)
  - [Q2: What if market volatility triggers my liquidation?](#Non-techDocs底稿-Q2:Whatifmarketvolatilitytriggersmyliquidation?)

</div>

1.  Core Mechanisms of HertzFlow Perps

#### **1.1 Mainstream Asset Oracle**

Hertzflow aggregates token prices from two primary sources:

- **Pyth Network**

- **CEX Index Feeds** (Binance, OKX, Coinbase)

Pyth Network is the primary oracle for Hertzflow, with CEX index prices acting as a fallback and validation layer. The following describes how the multi-oracle system works:

- If Pyth data is fresh and valid, Hertzflow uses the Pyth price.

- If Pyth data is stale or unavailable, the system switches to an aggregated index price built from top-tier exchanges (Binance, OKX, Bybit).

- When using CEX data, Hertzflow applies a liquidity-weighted scoring system that accounts for order book depth, resilience, and bid/ask balance. Higher-liquidity venues are weighted more heavily in the final price.

- If both Pyth and the fallback CEX feeds fail, no price update will occur.

**NOTE:** Oracle price updates occur during trade execution and through regular keeper updates.

This multi-layer design ensures Hertzflow maintains accurate, low-latency token pricing even during volatile conditions or infrastructure outages.

#### **1.2 Collateral Management**

Hertzflow allows traders to open leveraged long and short positions across supported markets with up to **100x leverage**. Each position is fully isolated, with collateral, borrowing, and exposure tracked independently.

When a trader opens multiple positions in the same market and direction (long / short):

- **Open positions:** Execution automatically increases the size of the existing position. Price, fee, and Profits and Losses (PnL) calculations are based on the current open position.

- **Collateral adjustments and closing:** Deposits, withdrawals, and close actions are applied directly to the existing position object.

Adjusting Collaterals

Collateral is deposited directly into each position, without a separate margin account. Traders can add or remove collateral in real time:

- **Depositing collateral:** Increases margin rate, reducing leverage and lowering liquidation risk.

- **Withdrawing collateral:** Decreases margin rate, increasing leverage and moving liquidation price closer.

- **Collateral Edit Limits:** Must be ≥ 10 USD and cannot reduce leverage below the minimum of 1.1x, and cannot increase leverage beyond the maximum of 100x.

Collateral can be selected from any whitelisted asset (SUI, USDC, xBTC, ETH) and is instantly borrowed and swapped through Hertzflow Liquidity Pool (HzLP)  at position open. A borrow fee accrues for the duration of the trade.

##### Long Positions

- **Exposure:** Trader gains upside exposure to the selected token.

- **Collateral:** Provided by the trader in any whitelisted asset, borrowed and swapped atomically into the long position.

- **Payouts:** Positive PnL and collateral withdrawals are returned to the trader with the option to settle in any whitelisted asset (SUI, USDC, xBTC, ETH).

**EXAMPLE:** a trader can open a long position on ETH with SUI, or USDC, or xBTC, or ETH as collateral, and will receive their profit in SUI, or USDC, or xBTC, or ETH when closing.

##### Short Positions

- **Exposure:** Trader profits if the selected token decreases in price.

- **Collateral:** Provided by the trader in any whitelisted asset, swapped through HzLP to establish the short position.

- **Payouts:** Positive PnL and collateral withdrawals are paid out in the collateral token by default, with the option to settle in any whitelisted asset.

**Example:** a trader shorting SUI  with USDC collateral can choose to settle in SUI if preferred.

#### **1.3 Leverage Management**

##### Understanding Leverage on Hertzflow

Leverage lets traders amplify their exposure by borrowing additional liquidity from the Hertzflow Liquidity Pool (HzLP). This enables positions much larger than the trader’s initial collateral. While leverage increases potential profits, it also magnifies losses and raises the risk of liquidation if the market moves unfavorably.

When a leveraged trade is opened:

1.  The trader deposits collateral (minimum \$10 USD equivalent).

2.  Hertzflow automatically borrows from HzLP to scale the position size.

3.  Exposure and risk are determined by the leverage multiplier selected.

**EXAMPLE:** With 20x leverage and \$100 collateral, a trader opens a \$2,000 position. Profits (or losses) are calculated on the full \$2,000 exposure, not just the \$100 collateral.

##### Setting Leverage 

Hertzflow supports leverage from **1.1x up to 100x** across all supported markets. The amount of leverage chosen directly determines both your potential returns and the distance to your liquidation price.

- **Range:** 1.1x to 100x across all supported assets

- **Adjustment:** Traders select leverage with a slider in the Hertzflow interface. The system automatically recalculates position size, liquidation level, and margin requirements in real time.

- **Rules:** Higher leverage increases profit potential but reduces the margin buffer. Lower leverage provides more stability and reduces liquidation risk.

##### Margin and Maintenance Margin

- **Initial Margin:** The collateral you must deposit to open a position.

- **Maintenance Margin (MMR):** The minimum margin level required to keep the position open.

**NOTE:** If your margin rate (MR) falls below the MMR threshold, your position becomes eligible for liquidation by the Hertzflow Keeper Network.

##### Risks of Using Leverage

While leverage can boost returns, it also significantly increases the risk of liquidation. If the market moves against your position and your collateral falls below the maintenance margin, the Keeper Network will close your position automatically.

**TIPS:** To trade responsibly, it’s critical to:

- **Start small:** Begin with lower leverage until you build confidence and experience.

- **Stay active:** Monitor collateral, liquidation price, PnL and margin ratio in real time.

<!-- -->

- **Use stop-losses:** Always define a downside exit to protect against sudden moves.

#### **1.4 Fee Structure**

##### Core Parameter Summary

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| **Action** | **Fee Type** | **Rate** | **Purpose** |
| Swap | Swap Fee | Dynamic | Protects LPs and keep the current weights aligned with their targets |
| Borrowing | Hourly Borrow Fee | Dynamic | Compensates LPs for capital utilization |
| Position Open / Close | Open/Close Fee | 0.06% | Charged on entry, exit, and collateral edits |
| Forced Closure | Liquidation Fee | 0.2% | Risk mitigation & LP compensation |
| \$HzLP Add / Remove | LP Fee | Dynamic | Risk mitigation & Pool composition balancing |

</div>

**NOTE:** Traders should monitor liquidation prices, as borrow and funding fees reduce collateral over time.

##### Open / Close Fee

A flat percentage of **0.06%** is applied whenever a position is opened or closed, and this fee goes to liquidity providers in HzLP.

This same fee applies to:

- Take Profit / Stop Loss orders.

- Limit orders.

- Forced liquidations (in addition to liquidation fees).

**EXAMPLE:** A position size of \$10,000 will be charged \$6 upon open, close or liquidation.

##### Swap Fee

Swaps between assets inside the Hertzflow LP (HzLP) pool incur a **dynamic swap fee** to protect liquidity providers (LPs) and to keep the pool weights aligned with their targets. Swaps apply two layers of fees:

- **Base Fee Rate (base_bps)** – a flat fee applied to every swap.

  - Non-stables: swap_fee_bps = 30 (0.30%)

  - Stables: stable_swap_fee_bps = 4 (0.04%)

- **Dynamic Impact Fee Rate (Rebate or Tax, tax_bps)** – adjusts depending on whether your swap moves the pool **toward** or **away from** the target weights. 

  - Non-stables: tax_bps = 150 (1.5%)

  - Stables: stable_swap_fee_bps = 20 (0.2%)

The **dynamic impact fee rate** is calculated as follows. The protocol measures the difference between the **current weightage** and the **target weightage**:

- **Initial Deviation (**init_diff = ｜c% - t%｜**)**\
  For instance, BTC target weight is 20%. If the pool currently holds only 15%, then init_diff = 5%.

- **Next Deviation (**next_diff =｜c%‘ - t%‘｜**)**\
  After your swap, the deviation is recalculated. For instance, if your swap pushes BTC weight to 28%, then next_diff = 8%.

Then the **dynamic impact fee** adjusts to reward behaviors that rebalances pool and :

- **If next_diff \< init_diff → Rebate**\
  Your swap brings the pool closer to balance. In this case, part of the fee is refunded. The rebate is capped so that the final fee never becomes negative.

`FORMULA:`

`rebate_bps = tax_bps * init_diff / t%`

`final_fee_bps = max(0, base_bps - rebate_bps)`

- **If next_diff ≥ init_diff → Tax**\
  Your swap makes the pool less balanced, so an extra tax is charged. If you help rebalance the pool, you get cheaper fees (rebate). If you push the pool further out of balance, you pay more (tax).

`FORMULA:`

`avg_diff = (init_diff + next_diff) / 2`

`capped_diff = min(avg_diff, t%)`

`tax_bps_adj = tax_bps * capped_diff / t%`

`final_fee_bps = base_bps + tax_bps`

`The maximum loss is capped at (FEE_BPS_POWER - final_bps) / FEE_BPS_POWER.`

**EXAMPLE：**

- BTC target = 20%.

- Pool initially has 0% BTC → init_diff = 20%.

- After swap, pool goes to 80% BTC → next_diff = 60%.

- Average diff = 40%.

final_bps = base_bps + 1.5% \* (20% / 20%) = 1.8%

So the fee is **much higher** than the base fee — a strong penalty for unbalancing the pool.

##### Liquidation Fee

When a position’s margin falls below maintenance requirements, it is force-closed.

- **Liquidation Fee Rate:** **1%** of collateral.

- The fee is applied **in addition** to the Open/Close fee and any accrued Borrow Fees.

- Remaining collateral (after deductions) is returned to the trader.

**EXAMPLE:**

- Collateral: \$10,000

- Remaining after liquidation: \$1,000

- Liquidation Fee (1%): \$100

- Net returned: \$900

##### Target and Current Weightage

- **Target Weight (t%token):** Desired share of pool TVL for each token.

- **Current Weight (c%token):** Actual share based on live pool balances.

- **Deviation (δ%token):** Maximum allowable relative deviation between target and current weight.

δ%token=∣c%−t%t%∣δ\\\_{token} = \left\|\frac{c\\ - t\\}{t\\}\right\|

**NOTE:** If the new liquidity action would push δ% above the configured limit, the transaction will not be proceeded.

##### LP Add / Remove Fees

Adding or removing liquidity (minting or burning HzLP) uses **the same weight-balance logic** as swaps. The final fee depends on whether the action moves pool weights toward or away from their targets.

- **Base Fee:** `add_remove_fee_bps = 30` (0.30%)

- **Deviation Threshold (δ%):** Each asset has a configured max deviation from its target weight:

<div class="table-wrap">

|       |                            |
|-------|----------------------------|
| Asset | δ% (Max Allowed Deviation) |
| BTC   | 20%                        |
| ETH   | 20%                        |
| SUI   | 20%                        |
| USDC  | 20%                        |

</div>

**EXAMPLE:** TVL = \$1,000,000; δ% = 20%; user tries to add \$150,000 ETH.

- Target weight of ETH = 40% → \$400,000

- Current weight of ETH = 30% → \$300,000

<!-- -->

- New weight = (300,000 + 150,000) / 1,000,000 = 45%

- Target = 40%, deviation = (45% - 40%) / 40% = 12.5% (\< 20%) - rebate

- `rebate_bps = 1.5% * 10% / 40%`

- `final_fee_bps = max(0, base_bps - rebate_bps) = 0%`

- Fee = **\$0**.

#### **1.5 Limit Order**

Limit orders, unlike market orders, are always active until filled or manually cancelled. They execute only at your limit or better, and may not fill in volatile markets.

**NOTE:**

- Limit orders are independent of your current position -  they can open a new position or add to an existing one.

- They remain active even if your current position is closed or liquidated.

- Hertzflow supports up to **20 active limit orders** per market.

⚠️**CAUTION**

- **When Placing Orders Near Liquidation Price:** Execution order is not strictly FIFO (first-in, first-out). If your limit price is near your liquidation threshold, then

  - If the limit order executes first → your position may be saved.

  - If liquidation executes first → your position is closed, but the limit order stays active and may immediately open a new one.

<!-- -->

- **Simulated Liquidation Price Displayed When Setting Up a Limit Order:** The displayed liquidation price is only a simulation at the moment of order placement. When the limit order actually triggers, market conditions may have changed (funding fees, borrowing costs, or price shifts), so the real liquidation level may differ from what was shown on the form.

  - **If you already have a position:** The displayed liquidation price factors in both your current position and the requested limit order.

  - **If you don’t have a position:** The liquidation price is calculated based only on the requested order.

##### Quick Reference Table

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| **Order Type** | **Trigger** | **Execution** | **Use Case** |
| **Market (Open/Close)** | Mark price (immediate) | Instant, with slippage | Fast entry/exit |
| **Limit (Open/Close)** | Price reaches your set limit | Executes at limit or better | Price discipline |
| **Trigger (Open/Close)** *(Coming Soon)* | Price reaches your trigger | Converts to market order with slippage | Stop-loss / Take-profit |
| **Liquidation** | Mark price hits liquidation | Forced closure to protect LP | Protocol safeguard |

</div>

#### **1.6 How Hertzflow Executes Trades**\
\

##### Order Execution Flow

Hertzflow uses a modular request-based architecture for decentralized trading:

1.  Trade Requests

    - Traders submit requests via the Hertzflow dashboard. These include:

      - Open/close positions

      - Increase/decrease position size

      - Deposit/withdraw collateral

      - Set limit orders, take-profit, or stop-loss conditions

    - Requests contain all details: position size, side, leverage, and price limits.

2.  Request Monitoring & Execution

    - Keepers watch submitted requests and current market prices.

    - Once conditions are met (for example, a limit order price is reached), Keepers trigger on-chain execution.

    - The Oracle module provides final prices for settlement, ensuring trades reflect real-time market conditions.

3.  Logical vs Actual Orders

    - Logical Order: Created when the trader submits the request (off-chain or in the smart contract).

    - Actual Order: Executed on-chain by the Keeper when the trigger condition is met.

    - Market orders execute immediately; limit orders wait until the target price is hit; stop-loss orders (trigger close) behave similarly.

##### Example of a Perpetual Trade on Hertzflow

Let’s bring all the concepts together with a concrete example of trading on Hertzflow’s decentralized perpetual futures platform. This will illustrate how positions, fees, and leverage interact in practice.

1.  Trade Setup

Imagine a trader wants to open a 2x long position on SUI. The parameters are:

<div class="table-wrap">

|                   |                 |                                          |
|-------------------|-----------------|------------------------------------------|
| Parameter         | Value           | Notes                                    |
| Position Size     | \$1,000         | Total value of the position              |
| Collateral        | \$500 SUI       | Deposited by trader                      |
| Borrowed Amount   | \$500 SUI       | Provided by Hertzflow’s liquidity pool   |
| Leverage          | 2x              | Total position ÷ collateral              |
| Initial SUI Price | \$2.50          | Market price at position opening         |
| Utilization Rate  | 40%             | Portion of liquidity pool already in use |
| Borrow Rate       | 0.015% per hour | Hourly fee on borrowed amount            |
| Open Fee          | 0.06%           | Charged on position size when opening    |

</div>

2.  What Happens Next

Suppose the trader holds this position for 48 hours, during which SUI price rises by 10%.

1.  Position Value Update

- Final position value: \$1,100

- Final SUI price: \$2.75

2.  Closing Fee

- 0.06% of final position: \$1,100 × 0.06% = \$0.66

3.  Borrow Fee Calculation\
    Hertzflow accrues borrow fees hourly based on pool utilization:

Hourly Borrow Fee = (Tokens Borrowed / Tokens in Pool) × Hourly Borrow Rate × Position Size

- \$500 borrowed / \$1,250 in pool × 0.015% × \$1,000 = \$0.06 per hour

- Over 48 hours: \$0.06 × 48 = \$2.88

3.  Profit Calculation

<div class="table-wrap">

|                        |         |
|------------------------|---------|
| Item                   | Amount  |
| Final Position Value   | \$1,100 |
| Less: Initial Position | \$1,000 |
| Less: Borrow Fees      | \$2.88  |
| Less: Open Fee         | \$0.60  |
| Less: Close Fee        | \$0.66  |
| Net Profit             | \$95.86 |

</div>

**The trader earns \$95.86 after 2 days.**

#### **1.7 liquidation**

The **liquidation price** represents the threshold at which a position will be automatically closed if a trader’s collateral can no longer support the leveraged position. Hertzflow continuously monitors positions and triggers liquidations through its Keeper Network when necessary.

##### How Liquidation Works

- **Long Positions:**\
  Liquidation occurs if the token price **falls below the liquidation price**.\
  *Example:* If the liquidation price is \$2.50, the long position will be closed if the token drops below \$2.50.

- **Short Positions:**\
  Liquidation occurs if the token price **rises above the liquidation price**.\
  *Example:* If the liquidation price is \$2.80, the short position will be closed if the token rises above \$2.80.

##### Factors Affecting Liquidation Price

The liquidation price is influenced by:

1.  **Entry Price** – the average price of the position when opened.

2.  **Collateral Size** – the initial margin deposited minus any opening/closing fees.

3.  **Fees:**

    - **Liquidation Fee** – charged specifically when a position is liquidated.

    - **Close Fee** – combined fees for decreasing a position.

    - **Borrow Fee** – accumulated interest for leveraged positions over time.

4.  **Position Size** – the total value of the position.

5.  **Maximum Leverage** – the highest allowed leverage for the market.

The formula adjusts dynamically as the position evolves, taking into account any changes in collateral, added/removed margin, or partial position adjustments.

##### Monitoring Margin and Liquidation

Hertzflow calculates **Margin Rate (MR)** for each position:

`MR = Collateral * (1 + uPnL% − r_fees) / Position Size * 100%`

- **uPnL%**: Unrealized profit or loss percentage

- **r_fees**: Sum of close fee rate, borrow fee rate, and liquidation fee rate.

If **MR falls below the Maintenance Margin Requirement (MMR)**, keeper bots trigger a liquidation automatically.

##### Liquidation Execution

1.  **Automated:** Keepers continuously monitor positions and execute liquidations without manual intervention.

2.  **Safe:** SUI’s **Programmable Transaction Blocks (PTB)** ensure that closing a position, repaying borrowed assets from the Hertzflow Liquidity Pool (HzLP), and updating relevant objects occur atomically.

3.  **Transparent:** All liquidation transactions are recorded on-chain for full auditability.

<!-- -->

2.  HzLP v1

##### 2.1 Hertzflow Liquidity Pool (HzLP) Overview

The **Hertzflow Liquidity Pool (HzLP)** is the backbone of leveraged trading on Hertzflow. It acts as the counterparty to all traders, providing liquidity for perpetual markets across supported tokens (SUI, ETH, xBTC, USDC).

LPs (Liquidity Providers) deposit assets into the pool and receive **\$HzLP tokens**, representing their share of the pool. As traders open, close, and settle positions, the pool earns fees and traders’ losses, which accrue directly to LPs.\
The JLP token derives its value from:

- An index fund of **SUI, ETH, xBTC, USDC**.

- Trader's **profit and loss**.

- **75%** of the generated fees from swap fees, open/close position fees, borrow fees and liquidation fees

##### 2.2 \$HzLP Token

- **Representation:** \$HzLP tokens mirror your share of the Hertzflow Liquidity Pool.

- **Acquisition:** Deposit supported tokens into the pool, and \$HzLP is minted proportionally.

- **Redemption:** Burn \$HzLP to withdraw your proportional share of underlying assets, plus accrued yield.

- **Yield Mechanism:** \$HzLP grows in value over time through:

  - Swap fees from token conversions

  - Open/close position fees from leveraged trades

  - Borrow and funding fees

  - Liquidation fees from forced position closures

  - Traders’ net losses

##### 2.3 How the HzLP Pool Works

1.  **Deposits & Withdrawals**

    - Deposit tokens → Mint \$HzLP proportionally.

    - Redeem \$HzLP → Burn tokens and receive underlying assets instantly.

    - **Dynamic LP Fees:** Fees adjust based on pool balance relative to target asset weights.

      - Adding scarce assets or removing surplus → Lower fees

      - Adding oversupplied assets or removing scarce → Higher fees

2.  **Liquidity Deployment**

    - The pool automatically serves as counterparty for all trades.

    - Positive trader PnL → Pool pays out

    - Negative trader PnL → Pool earns, increasing TVL

3.  **Earnings & APY**

    - Earnings come primarily from fees and traders’ losses.

    - Projected APY is compounded daily based on accrued fees and weight-adjusted earnings:

`APY_total = (1 + Σ(Daily APR × Token Weight) / 365) ^ 365 − 1`

4.  **Governance & Fee Distribution:**

    - **LP Share:** 75% of all protocol fees accrue to LPs, compensating for counterparty risk.

    - **Protocol Treasury:** 25% is reinvested into protocol growth, liquidity, insurance backstops, and incentive campaigns.

5.  **Risk Management**\
    Hertzflow mitigates LP risks through:

    - **Dynamic Borrowing Rates:** Adjust rates in real-time to discourage OI imbalances

    - **Automated Keeper Liquidations:** Smart-contract-driven, deterministic on-chain liquidations

    - **Dynamic LP Fees:** Incentivize deposits/withdrawals that maintain pool balance

    - **Weightage Tolerance Bands:** Target ±δ% per-asset to prevent concentration risk

    - **Decentralized Keeper Network:** Redundant nodes ensure liquidations and trade execution even under stress

##### 2.4 Custodies

The **Hertzflow Liquidity Pool** manages multiple **custody accounts** for supported tokens, which hold and track the liquidity provided by LPs:

<div class="table-wrap">

|       |                         |
|-------|-------------------------|
| Token | Custody Account         |
| SUI   | … (on-chain account ID) |
| ETH   | …                       |
| xBTC  | …                       |
| USDC  | …                       |

</div>

Each custody account represents the pool’s holdings for that specific token, including deposited assets, locked amounts for traders, and any borrowed assets.

**NOTE: Key Concepts**

1.  Debt

    - Represents the amount of tokens borrowed from the custody.

    - Calculated as:

debt = max(custody.debt - custody.borrowLendInterestsAccrued, 0)

- Provides the **pure debt amount** without accumulated interest.

2.  Theoretically Owned

    - The “true” ownership of tokens in the custody, including borrowed assets:

theoreticallyOwned = custody.assets.owned + debt(custody)

- Borrowed tokens are **not included** in `custody.assets.owned`, so this ensures the actual total value is reflected.

3.  Total Locked

    - Represents the actual amount of tokens locked by the custody, including borrowed assets:

totalLocked = custody.assets.locked + debt(custody)

- Ensures that liquidity obligations toward traders are fully captured.

##### 2.5 Assets Under Management (AUM)

1.  Stablecoins (USDC)

For stablecoins, the AUM is calculated as:

aum = theoreticallyOwned \* currentTokenPrice

2.  Non-stablecoins (SUI, ETH, xBTC)

<!-- -->

1.  Global Short PnL:

unrealizedShortPnl = custody.assets.globalShortSizes \* 

                     (\|custody.assets.globalShortAveragePrices - currentTokenPrice\|) /

                     custody.assets.globalShortAveragePrices

shortTradersInProfit = custody.assets.globalShortAveragePrices \> currentTokenPrice

2.  **AUM Calculation:**

netAssetsToken = max(0, theoreticallyOwned - custody.assets.locked)

netAssetsUsd   = netAssetsToken \* currentTokenPrice

aumUsd        = custody.assets.guaranteedUsd

if shortTradersInProfit:

    aumUsd -= unrealizedShortPnl

else:

    aumUsd += unrealizedShortPnl

- `guaranteedUsd` estimates the total size of all **long positions**.

- Updated only when positions are opened/closed or collateral is adjusted.

- Does **not** update in real-time with token price changes.

3.  Total AUM

The pool’s total AUM is the sum of all custody AUMs:

totalAumUsd = Σ(aumUsd)

##### 2.6 Virtual Price, Market Price, and AUM Limits

- Virtual Price:

Virtual Price = Total HzLP Pool Assets (USD) / Total \$HzLP in circulation

- **Market Price:**

  - When the AUM limit is reached:

Market Price = Virtual Price + Market-assigned Premium

- Minting new \$HzLP is **disabled** once the AUM cap is hit.

- Existing tokens can still be sold on the market; if market price \< virtual price, redemption occurs at **Virtual Price**.

<!-- -->

- APY Update:

  - Estimated daily APY is recalculated every 24 hours using the previous day’s fees.

##### 2.7 Calculating Global Unrealized PnL

**For Long Positions**

guaranteedUsd     = custody.assets.guaranteedUsd

lockedTokensUsd   = custody.assets.locked \* currentTokenPrice

globalUnrealizedLongPnl = lockedTokensUsd - guaranteedUsd

- Provides an estimate of total unrealized PnL for all open long positions.

- Includes traders’ collateral, so the value may **overestimate actual PnL**.

**For Short Positions**

globalUnrealizedShortPnl = custody.assets.globalShortSizes \*

                           (\|custody.assets.globalShortAveragePrices - currentTokenPrice\|) /

                           custody.assets.globalShortAveragePrices

- Gives an estimate of total unrealized PnL for all open short positions.

- For highest accuracy, iterate over **all open positions** and sum individually.

##### 2.8 Exposure & Risks

**Market Exposure:**

- LPs are exposed to price changes of pool assets. Non-stablecoins (SUI, ETH, xBTC) dominate this exposure.

- Gains occur when traders lose; losses occur when traders profit.

- Sideways or bearish markets often benefit LPs as traders typically lose more.

**Primary Risks:**

<div class="table-wrap">

|  |  |  |
|----|----|----|
| **Risk Type** | **Description** | **Mitigation** |
| **Directional Exposure** | LPs can face temporary losses from OI imbalances. | Dynamic borrowing rates, LP fee scaling, OI monitoring |
| **Liquidity Risk** | Withdrawal or trade execution may be delayed during high utilization. | Dynamic Position Limits, Weightage Tolerance Bands |
| **Keeper Risk** | Malfunctioning or malicious keepers may mis-execute trades or liquidations. | Decentralized keeper network, slashing & incentive framework, automated failover |
| **Oracle / Price Deviation Risk** | Misaligned or stale prices could lead to unfair settlements. | Dual-oracle validation (Pyth + CEX fallback), deviation threshold enforcement, retroactive fair execution |

</div>

3.  FAQ

When placing orders, traders configure the following:

- **Side:** Open Long, Open Short, Close Long, Close Short, Increase Long, Increase Short, Decrease Long, Decrease Short

- **Order Type:** Market / Limit / Trigger (coming soon)

- **Collateral Asset & Amount:** Any whitelisted token, minimum \$10 USD equivalent

- **Exposure & Leverage:** From 1.1x up to 100x, automatically calculated based on collateral and leverage chosen

- **Slippage:** Accepted price difference between execution price and entry price

- **Entry Price:** Market price for market orders, or trader-defined price for limit orders

- **Exit Price:** Defined for trigger orders (take profit / stop loss), or the execution price for market closes

#### 1. Account & Funds Management

##### **Q1: How do I fund my Hertzflow account?**

 **A1:**

- **If you already hold SUI / USDC / ETH / XBTC:** Connect your wallet and ensure you have ≥0.05 SUI for gas fees.

- **Assets on other chains:** Use a supported bridge to transfer SUI (for gas) and desired tokens to Sui network.

- **CEX withdrawals:** Make sure to choose the Sui network and native Sui tokens (SUI, USDC, ETH, XBTC), not cross-chain wrapped tokens.

##### **Q2: What are “native tokens” and “contract tokens”?**

 **A2:**

- **Native tokens:** Tokens that exist natively on the Sui network, such as SUI, USDC, ETH, XBTC.

- **Contract tokens:** Tokens issued on other chains, usually bridged to Sui for trading.

##### **Q3: Can I withdraw my liquidity at any time?**

**A3:** Yes, but note:

- Withdrawals may be restricted by pool weight constraints.

- First-time \$HzLP purchases require wallet approval.

- Withdrawals may be queued depending on the pool’s weight adjustments.

#### 2. Trading & Leverage Management

##### Q1: How do I select a market?

**A1:** Choose a trading pair from the market dropdown. You’ll see mark price, 24h change %, high/low, open interest, and indicative borrow rates.

##### Q2: What is leverage?

**A2:** Leverage lets you trade with borrowed funds. For example, 10x leverage means 1 unit of your capital controls 10 units of the asset. It magnifies both profits and losses.

##### Q3: How is the liquidation price calculated?

**A3:** The liquidation price is the market price at which your position will be force-closed. It depends on entry price, leverage, collateral, and the Maintenance Margin Requirement (MMR). Use the platform’s estimated liquidation price tool for guidance.

##### Q4:How to Calculate PnL？

**Unrealized PnL (uPnL%)**

- `uPnL% = (Mark Price - Entry Price) / Entry Price × 100%  (for longs)`

- `uPnL% = (Entry Price - Mark Price) / Entry Price × 100%  (for shorts)`

**Realized PnL**

- **Positive:** Collateral + profit returned from HzLP.

- **Negative:** Remaining collateral returned; losses retained by HzLP.

**Partial Close:** PnL is proportional to the closed portion.

##### Q5: What is the Maintenance Margin Requirement (MMR)?

**A5:** MMR is the minimum collateral required by the protocol. Falling below it triggers liquidation. It accounts for position size, leverage, and unrealized PnL.\
**Margin Rate (MR)**

- `MR = Collateral × (1 + uPnL% - r_fees) / Position Size × 100%`

Where `r_fees` = sum of close fee, accrued borrow fee, liquidation fee.

- **Liquidation occurs** if MR \< Maintenance Margin Requirement (MMR).

##### Q6: How can I avoid liquidation?

- Use conservative leverage.

- Set stop-loss orders.

- Monitor your positions and market trends regularly.

- Maintain sufficient collateral and avoid overexposure.

##### Q7: What happens if my position is liquidated?

**A7:** Your position is force-closed at market price. Losses are deducted from your collateral, which could be your entire margin depending on leverage and market volatility.

#### 3. Liquidity Provision & Earnings

##### Q1: Why provide liquidity?

 **A1:**

- Earn trading fees whenever users trade.

- Receive platform rewards or incentives.

##### Q2: What is \$HzLP?

**A2:** \$HzLP represents your share in the Hertzflow liquidity pool. Holding it entitles you to proportional earnings from the pool.

##### Q3: How to get \$HzLP

\$HzLP tokens represent your **share of the Hertzflow Liquidity Pool (HzLP)**. You can obtain them by:

- Deposit supported tokens (SUI, ETH, XBTC, USDC) into the HzLP pool.

- \$HzLP is minted to your wallet proportional to your contribution.

- Each \$HzLP token represents a share of the pool and entitles you to a portion of fees, liquidation rewards, and traders’ net losses.

You can redeem \$HzLP by:

- Burn \$HzLP to withdraw your proportional share of the pool’s underlying assets.

- Withdrawals are **instant**, subject to pool composition limits to maintain target asset weights.

##### Q4：How to Become a Liquidity Provider

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| **Step** | **Action** | **Description** | **Notes / Considerations** |
| **Preparation** | Prepare wallet & assets | Supported Sui wallets: Suiet, OKX Wallet, Slush; Gas token: ≥ 0.05 SUI; Collateral assets: SUI, ETH, XBTC, USDC | Ensure your wallet is connected to the Sui network |
| **Deposit Liquidity** | Navigate to \$HzLP Vault → Select token → Enter deposit amount → Confirm in wallet | Deposit selected tokens into the liquidity pool and receive \$HzLP tokens | Fees dynamically adjust based on pool target weight (closer to target = lower fee; further = higher fee). Deposits are capped to prevent overshooting target pool weights |
| **Earnings** | LP earnings sources | Swap Fees, Open/Close Fees, Borrow & Funding Fees, Liquidation Fees, LP Deposit/Withdrawal Fees, Traders’ Net Losses | Earnings are distributed proportionally to your share of the pool |
| **Withdraw Liquidity** | Select \$HzLP → Enter amount → Confirm in wallet | Redeem \$HzLP to receive your original tokens | Withdrawals are capped to maintain pool balance and prevent concentration risk; redeemed \$HzLP are burned |

</div>

**\$HzLP Deposit & Withdrawal Flow**

`Preparation`

`   ↓`

`Connect Wallet + Prepare Assets`

`   ↓`

`Deposit Liquidity`

`   ├─ Select token & amount`

`   ├─ Dynamic fee adjustment`

`   └─ Receive $HzLP in wallet`

`   ↓`

`Accumulate Earnings`

`   ├─ Swap Fees`

`   ├─ Open/Close Fees`

`   ├─ Borrow & Funding Fees`

`   ├─ Liquidation Fees`

`   ├─ LP Deposit/Withdrawal Fees`

`   └─ Traders’ Net Losses`

`   ↓`

`Withdraw Liquidity`

`   ├─ Enter $HzLP amount`

`   ├─ Fee & pool weight restrictions`

`   └─ Receive original tokens + $HzLP burned`

##### Q5: How to Calculate APY?

**\$HzLP Value**

- `$HzLP Price = Total Pool AUM / Total $HzLP Supply`

<!-- -->

- Fees, realized traders’ losses, and liquidations accrue to the pool, increasing \$HzLP price.

**APY Calculation**

- `APY_total = (1 + (Σ(APR_day × c%_token) / 365))^365 - 1`

Where `c%_token` = current weightage of the token in the pool.

You can track cumulative earnings and APY on the liquidity page.

##### Q6: How do I withdraw from the liquidity pool?

- **Withdraw liquidity:** Redeem \$HzLP for underlying assets.

- **Burn \$HzLP:** Redeemed tokens are destroyed.

- Pool weight restrictions may temporarily queue withdrawals to maintain balance.

#### 4. Risk Management & Strategy

##### Q1: How can I manage my trading risk?

- Diversify your positions across multiple assets.

- Set stop-loss orders to limit potential losses.

- Regularly monitor positions and adjust leverage.

- Maintain sufficient collateral and avoid using all funds in a single position.

##### Q2: What if market volatility triggers my liquidation?

- Understand hertzflow’s liquidation rules.

- Adjust your positions and leverage proactively.

- Stay calm and analyze the reason for liquidation to improve future strategies.

</div>
