# Product Docs

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772008356434 {padding: 0px;}
div.rbtoc1772008356434 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772008356434 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772008356434">

- [Welcome to HertzFlow](#ProductDocs-WelcometoHertzFlow)
  - [Introduction](#ProductDocs-Introduction)
  - [Protocol Architecture](#ProductDocs-ProtocolArchitecture)
  - [Why Choose HertzFlow](#ProductDocs-WhyChooseHertzFlow)
  - [Getting Started](#ProductDocs-GettingStarted)
- [Trade On HertzFlow](#ProductDocs-TradeOnHertzFlow)
  - [Market Structure](#ProductDocs-MarketStructure)
  - [Order Types](#ProductDocs-OrderTypes)
  - [Position Management](#ProductDocs-PositionManagement)
  - [Risk Management](#ProductDocs-RiskManagement)
- [Liquidity Provision](#ProductDocs-LiquidityProvision)
  - [Yield](#ProductDocs-Yield)
  - [Risk Management](#ProductDocs-RiskManagement.2)
- [Tutorials](#ProductDocs-Tutorials)
  - [Get Started](#ProductDocs-GetStarted)
  - [Trading](#ProductDocs-Trading)
  - [Select a market](#ProductDocs-Selectamarket)
  - [Fill in order form](#ProductDocs-Fillinorderform)
  - [Track order status](#ProductDocs-Trackorderstatus)
  - [Manage Positions](#ProductDocs-ManagePositions)
  - [Liquidity](#ProductDocs-Liquidity)
  - [Selecting a Pool/Vault](#ProductDocs-SelectingaPool/Vault)
  - [Liquidity Operations](#ProductDocs-LiquidityOperations)
  - [Monitor Positions](#ProductDocs-MonitorPositions)
  - [Trading Terms](#ProductDocs-TradingTerms)
  - [Liquidity Provision Terms](#ProductDocs-LiquidityProvisionTerms)

</div>

# Welcome to HertzFlow

## Introduction

HertzFlow is a decentralized perpetual exchange on BNB Chain that enables leverage trading on crypto, FX, commodities, and stocks with up to 1000x leverage. Built with 100% self-custodial architecture, HertzFlow delivers institutional-grade trading performance with 24/7 uninterrupted oracle-validated pricing and zero-fee trading pairs.

### Key Features

Universal Market Access Trade perpetuals across multiple asset classes—crypto, forex, commodities, and stocks—or permissionlessly create new markets for any oracle-supported asset. Bootstrap liquidity in minutes and access 24/7 continuous pricing secured by multi-oracle validation.

Powerful Leverage Engine with Capital Efficiency Access up to 1000x leverage with flexible collateral options. Use any supported asset as margin to maximize capital efficiency and capture market opportunities with minimal capital requirements.

Advanced Trading Terminal Experience CEX-quality execution with features including zero-fee trading pairs, loss protection mechanisms, and advanced order types. The platform eliminates traditional institutional advantages, creating a level playing field for all traders.

Composable Liquidity Layer HertzFlow's modular vault architecture enables one-click liquidity provision across all markets or targeted exposure through isolated pools. The protocol empowers curators to manage pool-level strategies while third-party developers can create optimized capital efficiency strategies through the open SDK.

### How It Works

#### For Traders

**Trade Perpetuals Across Multiple Asset Classes.**

Connect your wallet and trade perpetuals with self-custodial security. Execute leveraged positions using USDC, with real-time oracle pricing ensuring fair execution at all times. The platform's multi-oracle validation system provides robust risk management, while features like hyper leverage and loss protection enhance trading outcomes.

#### For Liquidity Providers

**Vault System** Provide liquidity through automated vaults that diversify exposure across all markets with a single deposit. Earn fees from trading activity, strategy yield, and trader losses while the protocol manages rebalancing and risk.

**Isolated Pools** Alternatively, provide liquidity directly to specific asset markets for more targeted exposure and potentially higher returns. Each isolated pool operates independently with its own risk parameters.

**Curator-Managed Strategies** Advanced users can leverage HertzFlow's curator system to access professionally managed liquidity strategies or create their own pools with custom parameters optimized for specific market conditions.

#### For Developers

**Build & Integrate** Leverage our SDKs, APIs, and composable smart contracts to create your own strategies, integrate liquidity into dApps, or launch new markets permissionlessly.

## Protocol Architecture

HertzFlow operates through three core layers:

**Smart Contract Layer** Capital-efficient liquidity pool design enabling perps trading via USDC, up to 1000x leverage, and dynamic rebalancing. Oracle-driven pricing ensures accurate market execution while automated risk management protects both traders and liquidity providers.

**Liquidity Optimization Layer** Adaptive pool architecture that allocates capital efficiently across markets, minimizing slippage and protecting LPs from excessive volatility exposure through auto-rebalancing mechanisms.

**Trading Interface** Institutional-grade terminal delivering seamless UX with advanced order types, real-time analytics, and performance optimization. The interface abstracts blockchain complexity while maintaining full on-chain transparency.

## Why Choose HertzFlow

**Self-Custodial Security** Your assets remain in your wallet at all times. Trade with the confidence that only you control your funds—no intermediaries, no custody risk.

**Capital-Efficient Global Market Access** Extreme leverage options and flexible collateral maximize your trading capital's potential. Access global markets with minimal capital requirements.

**Real Yield for LPs** Liquidity providers earn from multiple revenue streams: trading fees, strategy yield, borrowing interest, and trader losses. Capital stays productive 24/7 with instant withdrawal capability.

**Permissionless Innovation** Build on HertzFlow's leverage engine using robust SDKs and composable smart contracts. Create custom markets, integrate liquidity into dApps, or develop new trading strategies without permission.

## Getting Started

Ready to trade? Connect your wallet and start trading on hertzflow.xyz.

Want to provide liquidity? Explore our pool and vault options to start earning yield from global market activity.

Building something new? Check out our Developer Documentation to integrate HertzFlow into your application.

### Contact Us

X Telegram Discord Medium Media Kit

------------------------------------------------------------------------

**Disclaimer**: Trading with leverage involves substantial risk of loss. This documentation does not constitute investment advice. Always trade responsibly and only risk capital you can afford to lose.

# Trade On HertzFlow

## Market Structure

### Universal Market Access

HertzFlow provides access to perpetual markets across multiple asset classes including cryptocurrencies, forex pairs, commodities, equities, and indices. Markets are permissionlessly created for any oracle-supported asset, enabling traders to bootstrap liquidity and access 24/7 continuous pricing secured by multi-oracle validation. Each market displays real-time data including mark price, 24-hour price change, trading volume, open interest separated by direction, and available liquidity for both long and short positions.

### Leverage Limits

Maximum leverage varies by asset class to balance capital efficiency with risk management. Forex markets support up to 1000x leverage given their relatively lower volatility. Major cryptocurrencies including ETH, BNB, and SOL allow up to 500x leverage. Altcoins and commodities are capped at 50x, while equities and indices permit up to 25x leverage. These limits ensure traders can maximize capital efficiency while maintaining appropriate risk boundaries for each asset type.

### Market Hours

HertzFlow aligns its trading availability with the operating schedules of its underlying price oracle infrastructure, which mirrors the standard trading hours of each asset class in traditional markets. While cryptocurrency and forex markets trade continuously, certain real-world asset markets follow traditional trading schedules. Equity markets align with stock exchange hours, and commodity markets maintain hours specific to each asset class.

During market closure, all trading operations including opening, closing, editing, and canceling positions are disabled. Existing positions remain open, and active take profit or stop loss orders continue to monitor for trigger conditions when markets reopen.

Trading availability by asset type is outlined below:

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

<div class="table-wrap">

|  |  |  |
|----|----|----|
| Asset Type | Trading Schedule | Notes |
| **Cryptocurrencies** | Continuous (24/7) | Markets remain open at all times |
| **Foreign Exchange** | Sunday 5:00 PM ET – Friday 5:00 PM ET | Generally open during U.S. public holidays |
| **Precious Metals** | Sunday 5:00 PM ET – Friday 5:00 PM ET | Gold and silver observe CME holiday closures |
| **Commodities** | WTI: Sunday 6:00 PM ET – Friday 5:00 PM ET | Includes a daily maintenance pause from 5:00–6:00 PM ET; CME holidays apply |
| **U.S. Indices (SPY, QQQ)** | Weekdays, 9:30 AM – 4:00 PM ET | Closed on weekends and NYSE holidays |
| **U.S. Equities** | Weekdays, 9:30 AM – 4:00 PM ET | Closed on weekends and NYSE holidays |

</div>

## Order Types

Orders are categorized into three primary execution modes: Market Orders, Limit Orders, and Trigger Orders, excluding liquidations.

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="ac181ca7-3d34-4dd5-ae06-98299f51775a">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr data-local-id="9dcbd2fe-1ae8-43d1-982b-fcbbfc662872">
<td class="confluenceTd" data-local-id="6cdbb8de-bd5c-4c44-95eb-701229cdd6b7"><p><strong>Market</strong></p>
<p><strong>Open / Close</strong></p></td>
<td class="confluenceTd" data-local-id="b615170e-028e-4b96-83a7-1bed7ab7fe54"><p>Mark Price (immediate)</p></td>
<td class="confluenceTd" data-local-id="d36ce52e-46f3-4332-a787-8af07228f972"><p>Entering / Exiting a trade quickly when execution speed is more important than exact price.</p></td>
</tr>
<tr data-local-id="f9dc3504-a28c-466c-ba4b-0a1e58c97bd4">
<td class="confluenceTd" data-local-id="c42b524e-c3fb-44cd-82c2-a7dae411ae43"><p><strong>Limit</strong></p>
<p><strong>Open</strong></p></td>
<td class="confluenceTd" data-local-id="3c4d6fe9-a2a3-4dd3-be8c-77b7799eaeb4"><p>Execution price reaches trader’s set limit price</p></td>
<td class="confluenceTd" data-local-id="33f69d92-a877-489a-b17d-d4e190740d2e"><p>Opening at a specific target price without compromising on value.</p></td>
</tr>
<tr data-local-id="cc872db9-d382-493e-83e0-b61280a5ad4f">
<td class="confluenceTd" data-local-id="ff0b3c34-e8c7-4853-ad48-2778bbb396ea"><p><strong>Trigger</strong></p>
<p><strong>Close</strong></p></td>
<td class="confluenceTd" data-local-id="c660e500-5a40-4c03-8fe7-4c485ef99428"><p>Execution price reaches trader’s set trigger price (immediate)</p></td>
<td class="confluenceTd" data-local-id="d0dc65ba-b4c5-452f-8145-3b8cd75b5fa6"><p>Stop-loss or take-profit strategies when you prioritize execution certainty.</p></td>
</tr>
<tr data-local-id="052bfbc8-748b-4317-8fc8-fdb8d62686d5">
<td class="confluenceTd" data-local-id="b380dbaf-467b-409b-9b21-45d34016fb1b"><p><strong>Liquidation</strong></p></td>
<td class="confluenceTd" data-local-id="67a8437d-33b8-43b3-87a1-f319218660bd"><p>Mark price hits liquidation threshold</p></td>
<td class="confluenceTd" data-local-id="3febace8-6c5d-4f43-a811-321d948c1545"><p>Platform safeguard to prevent further losses and maintain solvency.</p></td>
</tr>
</tbody>
</table>

</div>

Change hint type

**Note that:** *Trigger orders* differ from *limit orders*:

- **Limit**: Stays active in the order book from placement. Executes only at your set price or better. Great for price discipline, but may never fill in fast markets.

- **Trigger**: Inactive until your trigger price is hit, then becomes a market order. Prioritizes execution over exact price, so slippage is possible.

### Price Impact Mechanism

Price impact reflects the cost of pool imbalance when trades skew the long-short ratio. Unlike traditional systems that charge impact fees at entry, HertzFlow applies a deferred impact model. When opening positions, the entry price equals the oracle mark price with no immediate impact charge. Throughout the position lifecycle, price impact accrues as open interest imbalance fluctuates, but fees are not assessed until closing.

At position closure, the net price impact from entry to exit settles as part of the final position accounting. This approach allows traders to benefit from favorable market movements that reduce imbalance. Price impact is capped at **50 basis points (0.5%)** with excess amounts converting to rebates for traders. Positions that close into reduced imbalance receive positive price impact as a rebate, incentivizing liquidity balancing.

### Guaranteed Take Profit and Stop Loss

HertzFlow implements guaranteed execution for take profit and stop loss orders across all leverage tiers. Given the platform's reliance on oracle pricing for execution, a trader's TP or SL request is always filled at the requested price, regardless of how far market price moves beyond the trigger level.

For example, if oracle prices gap below a trader's requested stop loss for a long position due to extreme volatility, HertzFlow closes the position at the requested SL price rather than the worse market price. This guarantee applies to all stop loss orders set within valid boundaries, ensuring traders have sophisticated risk management tools even during high market volatility or when trading with extreme leverage.

#### Take Profit Orders

Take profit orders automatically close positions when price reaches a favorable level, securing gains without requiring active monitoring. Long positions set TP trigger prices above current mark price and entry price, while short positions set TP triggers below these benchmarks. The platform accepts two input methods: traders can specify exact trigger prices or target profit percentages, with the system automatically calculating the corresponding values.

TP prices are capped at +2500% PnL to protect liquidity provider solvency. This boundary ensures the system can honor guaranteed execution while maintaining sustainable risk parameters. When market price reaches the trigger level, a market order executes immediately to close the position at the specified price, with no slippage tolerance required due to the guaranteed execution mechanism.

#### Stop Loss Orders

Stop loss orders protect capital by automatically closing positions when price moves adversely. Long positions place SL triggers below current mark price and entry price, while short positions place triggers above these levels. Similar to take profit functionality, stop losses accept both price and loss percentage inputs with automatic conversion between formats.

SL prices are capped at -80% PnL to prevent catastrophic liquidations while ensuring keeper bots can execute orders reliably. At extreme leverage levels approaching 1000x, this boundary provides critical protection against slippage and execution delays. Stop loss orders trigger as market orders when price hits the specified level, executing with priority to ensure position closure even during high volatility.

The guaranteed execution mechanism ensures stop losses execute at the requested price even if oracle feeds gap significantly beyond the trigger level. This protection is particularly valuable at high leverage where small price movements can generate large percentage losses.

### Combined TP/SL Strategies

Traders can set both take profit and stop loss orders simultaneously, creating bracketed exit strategies that automatically manage positions in either direction. When both orders are active, whichever trigger price is reached first executes and closes the position, automatically canceling the remaining order.

These orders remain attached to their positions and can be modified independently while positions remain open. Adding or removing collateral from positions adjusts the valid price boundaries for TP and SL orders, potentially requiring traders to update trigger prices to maintain compliance with the -80% to +2500% PnL range.

## Position Management

### Position Lifecycle

Positions display comprehensive metrics including notional size, net value incorporating unrealized PnL after fees, entry price, current mark price, liquidation price, and any active TP/SL trigger prices. Net value calculates as collateral plus net unrealized PnL minus accrued fees, providing real-time position valuation.

The platform supports flexible position adjustments throughout the lifecycle. Traders can increase positions by opening additional orders in the same direction, causing entry prices to recalculate as weighted averages and leverage to adjust based on new collateral-to-size ratios. Existing TP/SL orders automatically checks for validity of existing parameters.

### Position Reduction

Reducing positions provides two distinct modes to accommodate different trading strategies. The default mode - Keep Leverage Off - reduces position size while maintaining collateral, effectively deleveraging the position. This approach locks collateral in place and returns only realized PnL to the trader's wallet, allowing profit-taking while maintaining exposure at lower leverage.

The alternative mode - Keep Leverage On - reduces both position size and collateral proportionally, maintaining the same leverage ratio. This mode returns both realized PnL and proportional collateral to the trader, similar to traditional perpetual platforms. The calculation for received funds accounts for fees and realized PnL, with any shortfall deducting from remaining position collateral.

### Collateral Adjustment

Traders can modify position margin without changing size through collateral editing. Adding collateral improves liquidation price, increases leverage headroom, and widens the valid price boundaries for TP/SL orders. Removing collateral moves liquidation price closer to mark price and may invalidate existing TP/SL orders if they fall outside the valid boundaries.

When collateral removal narrows TP/SL caps, take profit orders beyond the new maximum update automatically to the new cap price. Stop loss orders that fall outside the new -80% boundary are marked invalid with visual warnings, requiring traders to either restore collateral or modify the orders to valid levels. The system prevents collateral removal that would leave positions below the 10 USDC minimum or exceed maximum leverage limits.

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

When placing orders in a selected market, the following parameters are set:

Side: Open Long; Open Short; Close Long; Close Short; Increase Long; Increase Short; Decrease Long; Decrease Short

Order Type: Market/Limit/Trigger/Liquidated

Collateral Asset & Amount: Collaterals are in USDC, limited at a 10 USDC minimum, and can be adjusted real time when managing positions.

Exposure & Leverage: Leverage can be set between 1.1x and 1000x. Position size is calculated automatically from the leverage set and collateral amount.

Slippage: All market and swap orders are executed against Hertzflow Liquidity Pools (HzLP). Slippage tolerance can be set per trade — orders that breach this tolerance will revert to protect the trader.

Entry Price: Market price for market orders, a limit price set by traders for limit orders. Meanwhile, liquidation price is estimated and updated automatically.

Exit Price: For tigger orders, exit price can be set to stop loss or take profit. For market orders, exit price is the executed price at which positions are closed.

Positions may be settled via market or TP/SL order:

Market: Trader manually initiates a full or partial settlement for market positions.

TP/SL: Settles automatically at mark price only if mark price reaches or betters limit price.

When a non-liquidated close is executed:

Positive PnL: Trader receives their initial collateral plus realized trading profit, transferred directly from the liquidity pool.

Negative PnL: Trader receives remaining collateral after losses, with the loss amount retained by the protocol’s liquidity pool.

Partial Close: Proportional PnL is realized based on the closed portion of the position.

</div>

</div>

### Fee Structure

#### **Trading Fees**

Open Fee - Charged when opening positions (varies by market)

Close Fee - Charged when closing positions (varies by market)

Price Impact - Dynamic fee based on pool imbalance (can be positive or negative)

#### **Holding Fees (per hour)**

- **Funding Fee** - Paid between long and short traders based on market skew.

- **Borrow Fee** - Paid to liquidity providers for borrowed liquidity

- **Net Funding Rate -** The 1-hour net rate combines funding and borrow fees into a single annualized percentage. Hover over the net rate in Market Info to view:

  - **8-hour rate** - Projected rate over 8 hours

  - **24-hour rate** - Projected daily rate

  - **365-day rate** - Projected annual rate (APR)

  - **Hourly breakdown** - Separate funding fee and borrow fee components

#### Price Impact

Price impact reflects the cost of pool imbalance when your trade skews the long/short ratio:

- **Opening positions** - Entry price equals oracle mark price (no immediate impact)

- **During position** - Price impact accrues as OI imbalance changes (not charged immediately)

- **Closing positions** - Net price impact from open to close settles at execution

- **Impact cap** - Maximum 50 basis points (0.5%) with excess converting to rebates

- **Positive impact** - You may receive rebates if closing reduces pool imbalance

#### Slippage Tolerance

Market orders incorporate configurable slippage tolerance to accommodate price movement during execution. The acceptable price boundary for market orders combines mark price, price impact, and slippage tolerance: `Mark Price × (1 ± Price Impact) × (1 ± Slippage)`. Limit orders use only price impact without slippage: `Limit Price × (1 ± Price Impact)`. Take profit and stop loss orders execute at trigger prices with no slippage component, relying on guaranteed execution mechanisms.

Higher slippage tolerance increases execution probability during volatility at the cost of allowing larger price deviations from the expected price. The default 0.5% tolerance balances execution certainty with price precision for most market conditions.

### Liquidation Mechanics

#### Leverage Limits

Maximum leverage varies by asset class:

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the item. Press space again to drop the item in its new position, or press escape to cancel.

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="c5019903-2086-47b4-9a88-95f6ff95962b">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr data-local-id="92014456-41fd-46c7-9b4d-d3f339dc122d">
<th class="confluenceTh" data-highlight-colour="color-mix(in srgb, var(--sp-color-bg-muted) 100%, transparent)" data-local-id="0f87a618-7a38-4df7-b852-71fe7e40eb71"><p>Asset Class</p>
<p>Asset Class</p></th>
<th class="confluenceTh" data-highlight-colour="color-mix(in srgb, var(--sp-color-bg-muted) 100%, transparent)" data-local-id="7d678551-97fa-419b-96b2-5bec613cdac6"><p>Max Leverage</p>
<p>Max Leverage</p></th>
</tr>
&#10;<tr data-local-id="4514e911-cda0-4721-8f40-77c80a37a7ba">
<td class="confluenceTd" data-local-id="e762d725-487f-4a41-b0ac-fe07718dfa0a"><p>Forex (FX)</p></td>
<td class="confluenceTd" data-local-id="997d753c-cfde-4e5b-9501-38ceb9b09443"><p>1000x</p></td>
</tr>
<tr data-local-id="4fa2a4ad-0c29-4a4f-9997-975388f5eac3">
<td class="confluenceTd" data-local-id="4d1723c9-4c27-4720-9d51-71310c012958"><p>ETH/BNB/SOL</p></td>
<td class="confluenceTd" data-local-id="ec50f548-cd08-4977-97c4-9faf702e3298"><p>500x</p></td>
</tr>
<tr data-local-id="601d00cc-a487-4ff4-b3a7-1bfa39371fd7">
<td class="confluenceTd" data-local-id="9323fc05-16fb-4c39-b0b7-7c5965a95965"><p>Altcoins</p></td>
<td class="confluenceTd" data-local-id="bfc1b050-31c7-4f69-b343-5a091b5fd397"><p>50x</p></td>
</tr>
<tr data-local-id="96a80a21-71df-4456-8087-023a6a19a5ef">
<td class="confluenceTd" data-local-id="c383f070-8d5a-42af-8245-7ae915396da5"><p>Commodities</p></td>
<td class="confluenceTd" data-local-id="dcff6b92-6f2a-47b8-abe6-cdd619e35a3c"><p>50x</p></td>
</tr>
<tr data-local-id="497214dd-ce4e-4c01-bc5f-5ca0ae39c5b7">
<td class="confluenceTd" data-local-id="56f30c84-73c3-4cdd-bca2-b071ccf807a5"><p>Equities &amp; Indices</p></td>
<td class="confluenceTd" data-local-id="cafbd594-1111-4681-8583-6d6c16bf6133"><p>25x</p></td>
</tr>
</tbody>
</table>

</div>

Leverage is calculated as: `Leverage = Position Size / Collateral`

#### Liquidation

Positions liquidate automatically when mark price reaches your liquidation price, preventing negative account balances.

**Liquidation Price Formula:**

Long positions:

​

Liq Price = Entry Price × (1/Max_Leverage - 1/Leverage - Fees/Size + 1)

Plain TextCopyMore options

Short positions:

​

Liq Price = Entry Price × (1 - (1/Max_Leverage - 1/Leverage - Fees/Size))

Plain TextCopyMore options

Where `Fees` includes close fee, borrow fee, funding fee, price impact, and liquidation fee.

**Liquidation Process:**

1.  Position automatically closes at market price

2.  Remaining collateral (if any) returns to your wallet

3.  Liquidation fee (0.5% - 1% of position size) is charged

4.  Any active TP/SL orders on the liquidated position cancel

Monitor your liquidation price closely, especially during high volatility.

## Risk Management

### Best Practices

#### Risk Management

- **Never risk more than you can afford to lose** - Leverage magnifies both gains and losses

- **Use stop losses** - Protect capital by setting automatic exit points

- **Monitor liquidation prices** - Keep adequate margin buffer especially above 50x leverage

- **Start small** - Test strategies with lower leverage before scaling up

- **Diversify** - Avoid concentrating risk in a single market or position

#### Order Strategy

- **Limit orders for entries** - Get better prices during volatile markets

- **Market orders for exits** - Ensure execution when closing positions quickly

- **Bracket orders** - Always set both TP and SL for automated risk management

- **Edit over cancel** - Modify existing orders instead of canceling and recreating to save gas

#### Fee Optimization

- **Check price impact** - Large orders in low liquidity markets pay higher impact fees

- **Monitor funding rates** - High negative rates increase position holding costs

- **Claim fees regularly** - Don't let accrued rebates sit unclaimed

- **Time your entries** - Wait for favorable funding rate flips when holding multi-day positions

#### Liquidation Avoidance

- **Maintain margin buffer** - Keep liquidation price at least 5-10% away from mark price

- **Add collateral preemptively** - Don't wait until liquidation is imminent

- **Reduce leverage** - Lower leverage = greater safety margin

- **Close partials** - Take profits and reduce size to improve liquidation price

### Advanced Features

#### Position Compounding

Compound realized gains back into positions for exponential growth:

1.  Close a portion of your winning position

2.  Receive PnL + proportional collateral (Keep Leverage On)

3.  Immediately reopen a larger position with realized profits as additional collateral

4.  Repeat to grow position size using market gains

This strategy maximizes capital efficiency but increases risk exposure - use strict stop losses.

#### Hedging

Open opposing positions across markets to manage risk:

- **Cross-asset hedging** - Long crypto, short correlated equity indices

- **Spread trading** - Long one commodity, short a related commodity

- **Basis trading** - Capture funding rate differentials between markets

Note that each position incurs independent fees and margin requirements.

#### Multi-Market Strategies

Execute sophisticated strategies across HertzFlow's diverse markets:

- **Macro plays** - Trade forex pairs based on economic data and central bank policies

- **Correlation plays** - Exploit relationships between crypto and traditional markets

- **Volatility trading** - Short VIX or similar indices during calm markets

- **Commodity cycles** - Position in gold, oil, or agriculture based on seasonal patterns

Access to traditional markets 24/7 enables crypto traders to apply DeFi principles to TradFi assets.

------------------------------------------------------------------------

**Risk Warning**: Trading with leverage carries substantial risk of loss and is not suitable for all investors. You should carefully consider whether trading is appropriate for you in light of your experience, objectives, financial resources, and other relevant circumstances. The possibility exists that you could sustain losses in excess of your deposited funds. Only trade with capital you can afford to lose.

# Liquidity Provision

### Providing Liquidity

### Overview

HertzFlow's liquidity infrastructure operates through isolated market pools that serve as counterparties to leveraged perpetual traders. Liquidity providers deposit USDC to earn yield from trading fees, borrow fees, and trader losses while maintaining exposure to specific market dynamics. The protocol implements a single-token deposit model with automatic 1:1 long-short rebalancing, eliminating complexity while ensuring capital efficiency.

Unlike traditional AMMs that rely on continuous buyer-seller matching, HertzFlow employs pooled virtual liquidity capable of absorbing open interest imbalances and directional exposure. This architecture ensures trade settlement remains robust even during extreme market movements, while sophisticated risk controls protect liquidity providers from excessive drawdowns.

### Liquidity Options

#### HzLP: Market-Specific Pools

HzLP is the liquidity provider token minted when assets are deposited into an individual HertzFlow Liquidity Pool. HzLP tokens represent proportional ownership of isolated liquidity pools, each dedicated to a single perpetual market. When depositing USDC, providers receive HzLP tokens reflecting their pool share. These tokens accrue value as the pool collects trading fees and realizes profits from trader losses.

Each market operates independently with isolated risk parameters, allowing liquidity providers to select exposure based on their risk preferences. A BTC/USD pool's performance remains unaffected by ETH/USD pool dynamics, providing granular control over capital allocation and risk management.

Key characteristics:

Direct exposure to a single pool / market

Value reflects pool performance and fee accrual

Redeemable for the underlying pool assets

#### Vault Aggregation

HzV is the vault share token issued for deposits into HertzFlow Vaults. Each vault aggregates liquidity across multiple markets that share the same strategy, optimizing capital efficiency by shifting liquidity between markets based on utilization rates and fee opportunities.

Key characteristics:

Indirect exposure across multiple markets

Capital allocated dynamically based on pool utilization and risk

Returns reflect aggregate vault performance rather than individual pool fees

### Deposits

Depositing USDC into a market pool mints HzLP tokens representing your proportional share, and into a vault mints HzV tokens representing your share. The protocol automatically splits deposits equally between long and short collateral reserves, maintaining a 1:1 balance regardless of current open interest skew.

**Token Pricing:**

​

Liquidity Token Price = AUM / Total Supply

Plain TextCopyMore options

Assets Under Management (AUM) includes deposited USDC, accrued fees, and net unrealized PnL from open trader positions. As traders pay fees and realize losses, pool AUM increases, raising the value of each liquidity token. Conversely, trader profits decrease pool value.

**Deposit Capacity Limits:**

Maximum deposit amounts are constrained by risk parameters designed to prevent over-concentration:

​

Max USDC In = Max AUM - Current AUM

Plain TextCopyMore options

Where `Max AUM` represents the protocol-configured ceiling for each market's total liquidity. This hard cap maintains balance across markets by preventing unlimited growth in popular pools that would drain liquidity from others. Each market's cap is calibrated based on trading volume, volatility, and oracle reliability.

### Withdrawals

Withdrawing liquidity burns HzLP or HzV tokens and returns USDC at the current price. Withdrawals settle instantly on-chain without waiting periods, though maximum withdrawal amounts are subject to real-time risk checks ensuring sufficient liquidity remains for open positions.

**Withdrawal Capacity Constraints:**

Two separate limits govern withdrawal availability.

**PnL Factor Constraint:**

​

Max USDC Out (PnL) = (Current AUM - Max(Unrealized PnL Long, Unrealized PnL Short, 0)) / Max PnL Factor for Withdrawals

Plain TextCopyMore options

This constraint protects remaining LPs when trader unrealized profits are high. If traders hold large winning positions, withdrawals are restricted to prevent the remaining pool from becoming undersized relative to obligations. The `Max PnL Factor for Withdrawals` parameter determines how much pool value can be at risk from unrealized trader profits.

**Reserve Factor Constraint:**

​

Max USDC Out (Reserve) = Current AUM - Max(Reserved USD Long, Reserved USD Short) / Reserve Factor

Plain TextCopyMore options

Reserved USD represents total open interest (notional value of all open positions) on each side. The `Reserve Factor` ensures sufficient liquidity remains to cover potential position closures. This prevents LPs from withdrawing capital currently backing active trades.

The effective withdrawal limit is the minimum of these two constraints:

​

Max USDC Out = Min(Max USDC Out (PnL), Max USDC Out (Reserve))

Plain TextCopyMore options

### Automatic Rebalancing

The protocol maintains equal long and short collateral pools through automatic rebalancing during deposits and withdrawals. When you deposit USDC, the contract allocates 50% to long collateral reserves and 50% to short reserves, regardless of current open interest distribution. This ensures the pool can service both long and short traders without bias.

Price impact fees are eliminated at the contract level for liquidity operations. Unlike trading actions, deposits and withdrawals do not charge dynamic price impact, simplifying the LP experience and removing penalty mechanisms that would discourage healthy liquidity flow.

## Yield

### Yield Sources

#### Fee Income

Liquidity providers earn from multiple fee streams generated by trading activity:

**Trading Fees:**

- Open position fees charged when traders establish positions

- Close position fees charged when positions are exited or liquidated

- Fee rates vary by market based on liquidity depth and volatility

**Borrowing Fees:**

- Hourly fees paid by traders for borrowing liquidity to establish leveraged positions

- Calculated as a percentage of position size based on pool utilization

- Higher utilization increases borrow rates, incentivizing additional liquidity provision

**Liquidation Fees:**

- Penalties charged when trader positions are force-closed due to insufficient margin

- Compensates LPs for bearing liquidation execution risk

All fees settle continuously into the pool, increasing AUM and raising HzLP/HzV token value. Fee distribution occurs automatically without requiring manual claims.

### APY Calculation

Annual Percentage Yield represents projected returns from fee income, displayed as an annualized rate with compounding. The platform presents APY derived from trailing APR data:

**Fee APR** isolates annualized returns from trading activity fees only (open, close, borrow, liquidation), excluding price impact, PnL, and funding. This metric provides a conservative baseline yield expectation independent of market direction.

**Total APY** incorporates all yield sources including trader PnL over the measurement period. This metric is more volatile due to PnL variance but reflects comprehensive returns.

APYtotal=(1+APRDay365)365−1APY\_{total} = \left( 1 + \frac{APR\_{Day}}{365} \right)^{365} - 1APYtotal​=(1+365APRDay​​)365−1

### **Fee Distribution**

**Liquidity Providers** LPs receive 60% of all protocol revenues. This compensates them for supplying liquidity and bearing counterparty risk against traders.

**Protocol Treasury** The remaining 40% of revenues accrue to the protocol treasury. These funds are reinvested into protocol growth and resilience — including protocol-owned liquidity, gas subsidies, trading competitions, trader rebates, insurance backstops for LPs, and incentive campaigns. The overarching objective is to ensure that treasury revenues ultimately flow back to benefit LPs and traders directly or indirectly.

Change hint type

**Note that**: APY is variable and not guaranteed.

## Risk Management

### Risk Considerations

#### Counterparty Exposure

As the counterparty to all trades, LPs bear inverse correlation to trader performance. Extended periods of trader profitability decrease pool value, while trader losses increase it. Over long horizons, this exposure tends toward neutrality as winners and losers offset, but short-to-medium term variance can be significant.

Highly skilled or algorithmic traders may generate consistent profits, creating persistent headwinds for pool performance. The PnL factor caps provide some protection, but LPs should expect periods of negative returns from trader PnL.

#### Liquidity Constraints

During extreme market conditions, withdrawal capacity may become limited. While deposits and withdrawals typically settle instantly, temporary restrictions can prevent exits when trader unrealized profits are elevated or pool utilization is high.

Plan for potential illiquidity during stress periods. Maintain a diversified portfolio beyond LP positions to avoid forced exits during restricted periods. Review historical withdrawal cap patterns to assess typical liquidity availability.

### Best Practices

#### Market Selection

Choose markets aligned with your risk tolerance and market outlook. High-volatility assets (meme tokens, altcoins) generate higher trading fees but expose LPs to greater PnL variance. Stable markets (major forex pairs, established cryptocurrencies) offer more consistent fee income with lower directional risk.

Review historical APY charts and trader PnL patterns before depositing. Pools with stable, positive fee APR and balanced win/loss ratios indicate healthy market dynamics. Extreme APY spikes often correlate with temporary PnL windfalls that may reverse.

#### Capacity Monitoring

Check remaining deposit and withdrawal caps before committing capital. Deposits into pools near maximum AUM may have limited exit liquidity if trader activity increases utilization. Similarly, pools with restricted withdrawal capacity signal elevated trader PnL or reserve requirements.

Monitor utilization rates and open interest distribution. High utilization (\>70%) increases borrow fees paid to LPs but also constrains withdrawal availability. Balanced long-short OI reduces directional exposure risk.

#### Timing Considerations

Deposit during periods of low trader PnL. Entering when traders hold large unrealized profits means buying HzLP at inflated prices that may decline when profits realize. Conversely, depositing after trader losses or during low volatility periods may capture better entry prices.

Avoid large deposits or withdrawals immediately before or after major market events (economic data releases, protocol updates) that may cause temporary volatility spikes affecting HzLP pricing.

#### Diversification

Even within isolated pools, consider diversifying across multiple markets to spread risk. Concentrate positions in markets with:

- Established trading volume and liquidity depth

- Stable historical fee generation

- Moderate utilization rates

- Balanced long-short open interest

Avoid over-concentrating in correlated markets (e.g., multiple altcoin pools) where directional moves affect all positions simultaneously.

------------------------------------------------------------------------

**Risk Warning**: Providing liquidity involves substantial risk including potential loss of capital from trader profits. Past performance of pool APY does not guarantee future results. Liquidity may become restricted during periods of high trader PnL or pool utilization. Only provide liquidity with capital you can afford to lose.

# Tutorials

## Get Started

1

Insert a new step

**What you need**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="56b6a17a397f80bf3d3e38be3816e880fad693973613860ca13d8fb977628c45" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FgFoHxdZA8qEbd2g09fMX%25252FScreenshot%2525202026-01-21%252520at%25252018.55.29.png%253Falt%253Dmedia%2526token%253D8bf59e9d-c881-4642-9d4a-c39e548a?version=1&amp;modificationDate=1768998541101&amp;cacheVersion=1&amp;api=v2" data-height="794" data-width="662" data-unresolved-comment-count="0" data-linked-resource-id="74874909" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FgFoHxdZA8qEbd2g09fMX%252FScreenshot%25202026-01-21%2520at%252018.55.29.png%3Falt%3Dmedia%26token%3D8bf59e9d-c881-4642-9d4a-c39e548a" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="71bf30e9-c6d4-470d-9b11-dbf1702f2280" data-media-type="file" width="250" height="300" /></span>

Image options

- **Wallet Requirements:**

  - A supported BNB Chain wallet (Binance Wallet, MetaMask, or any WalletConnect-compatible wallet)

  - BNB for gas fees (recommend ≥ 0.01 BNB buffer at all times)

- **Trading Assets:** USDC on BNB Chain for collateral. Bridge or on-ramp assets from other chains if needed

- **System Requirements:**

  - Modern browser (Chrome, Brave, Edge, or Safari)

  - Wallet browser extension or mobile in-app browser

2

Insert a new step

**Access & connect**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="239f45079b5a24c1fc51045dccae3d095211f4b56d10780816f8c78e121fe049" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FaGsXbWXu5Cl2UJmQgqa7%25252FScreenshot%2525202026-01-21%252520at%25252018.57.52.png%253Falt%253Dmedia%2526token%253De590f541-9e98-4dad-a1f2-8ab0c084?version=1&amp;modificationDate=1768998541119&amp;cacheVersion=1&amp;api=v2" data-height="72" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74874915" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FaGsXbWXu5Cl2UJmQgqa7%252FScreenshot%25202026-01-21%2520at%252018.57.52.png%3Falt%3Dmedia%26token%3De590f541-9e98-4dad-a1f2-8ab0c084" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="6dd8bcb3-6fbd-478a-b3d4-27479ca98be3" data-media-type="file" width="250" height="7" /></span>

Image options

- **Open HertzFlow dapp** and click **Connect** (top right).

- **Select network:** For testing, you will be connected to **BNB** **Testnet** by default.

- **Claim Faucets:** For testing, you can claim faucets on the top right corner by clicking the Claim Faucet button.

*Your wallet connection persists across sessions. HertzFlow never requests your private keys or seed phrase.*

3

Insert a new step

**Funding your account**

- **If you already hold USDC on BNB Chain:** You're ready to trade or provide liquidity. Ensure you maintain sufficient BNB for gas fees (≥ 0.01 BNB recommended).

- **If transferring from another chain or CEX:**

  - **Bridge assets**: Use your preferred bridge service to transfer USDC to BNB Chain

  - **Withdraw from CEX**: When withdrawing, select BNB Chain (BSC) as the network

  - **Verify network**: Ensure you're sending to BNB Chain, not Ethereum or other networks

  - **Check contract addresses**: USDC contract addresses differ across chains—verify you're receiving the correct BNB Chain USDC

*Cross-chain transfers require time and may involve swap fees. Always verify token symbols and destination networks before sending.*

## Trading

1

Insert a new step

## **Select a market**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="48f8fa0a265eadb4c7aa5f98c3e945ab494bb9cceac6c52e5075328034908eb3" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FxH8VRzMbtrVkK9K3qS4x%25252FScreenshot%2525202026-01-21%252520at%25252019.08.22.png%253Falt%253Dmedia%2526token%253D5e6be949-8438-4d32-bb8e-c3f2b57c?version=1&amp;modificationDate=1768998424229&amp;cacheVersion=1&amp;api=v2" data-height="826" data-width="1870" data-unresolved-comment-count="0" data-linked-resource-id="74580022" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FxH8VRzMbtrVkK9K3qS4x%252FScreenshot%25202026-01-21%2520at%252019.08.22.png%3Falt%3Dmedia%26token%3D5e6be949-8438-4d32-bb8e-c3f2b57c" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="25d477e5-56cf-4f11-b7b7-c7f7e836709d" data-media-type="file" width="250" height="110" /></span>

Image options

- Click the **Market dropdown** in the top navigation. Browse available markets or use the search function. Filter by asset class: Crypto, Forex, Equities, Indices, Commodities, or Meme. Click on a market to view its market info.

### **Market Information:**

- **Mark Price**: Current oracle price with 24-hour change percentage

- **24h High/Low**: Last traded price range over the last 24 hours

- **Available Liquidity (L/S)**: Remaining capacity for long and short positions

- **Open Interest (L/S)**: Total notional value of active positions per side

- **1h Net Rate (L/S)**: Combined funding and borrow rate per hour

*Markets with a red dot label indicates **Market** **Closed**, and are temporarily unavailable during off-market hours (applies to certain real world assets).*

2

Insert a new step

## **Fill in order form**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="3181013df4311bd889931e750994ac36b62ae54c60d9faef3905d1e0925719c4" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252F8HDX2RNUJvI7mIGLKrhp%25252FScreenshot%2525202026-01-21%252520at%25252019.16.12.png%253Falt%253Dmedia%2526token%253Def104dbe-dc5b-4fbc-9c51-20b8a11f?version=1&amp;modificationDate=1768998424248&amp;cacheVersion=1&amp;api=v2" data-height="1040" data-width="754" data-unresolved-comment-count="0" data-linked-resource-id="74580029" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252F8HDX2RNUJvI7mIGLKrhp%252FScreenshot%25202026-01-21%2520at%252019.16.12.png%3Falt%3Dmedia%26token%3Def104dbe-dc5b-4fbc-9c51-20b8a11f" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="3b6da6a3-0d29-4b4c-8651-73ca6ca2bb3f" data-media-type="file" width="250" height="345" /></span>

Image options

- **Side**: **Long** (expect price to rise) or **Short** (expect price to fall).

- **Order type**:

  - **Market**: Execute now at best available price.

  - **Limit**: Execute at your price or better.

  - **Take Profit and Stop Loss:** Enter either your desired exit price, or your target PnL%. Entry are limited such that **PnL% is capped between** **-80% and +2500%**.

  - **Collateral, Leverage, and Size：**

    - **Collateral:** Minimum 10 USDC

    - **Leverage:** 1.1x to 1000x

    - **Size:** Collateral × Leverage

*Your market position opens immediately. Your limit and TP/SL orders remain active in the **Orders** tab until filled or cancelled. Edit trigger prices or cancel orders anytime from the Orders interface. Monitor execution status via the toast notification.*

### **Review Order Details**

- **Entry Price**: Live mark price for market orders, can be set for limit orders

- **Est. Liq. Price:** The estimated market price at which your position will be forcibly closed by the protocol to prevent your collateral from falling below the maintenance margin requirement.

- **Fee Breakdown (hover for details):**

  - **Open Fee**: Charged on position notional value

  - **Borrow Fee**: Accrues hourly based on position size

  - **Funding Fee**: Paid/received based on market imbalance

  - **Price Impact**: Zero at entry, settles at position closure

- **Slippage Tolerance**: Accepted price difference between execution price and entry price

*Higher slippage tolerance increases execution probability during volatility but allows larger price deviations.*

3

Insert a new step

## **Track order status**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="6e49b6137fab1a60726bc033e6f76082c9afa83087588029e9a767473781bea8" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FHcfGksQ3O45euDhEBy2X%25252FScreenshot%2525202026-01-21%252520at%25252019.43.51.png%253Falt%253Dmedia%2526token%253D161cbaf8-1b1a-4977-8dbc-fd0e6ff5?version=1&amp;modificationDate=1768998424280&amp;cacheVersion=1&amp;api=v2" data-height="410" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74580035" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FHcfGksQ3O45euDhEBy2X%252FScreenshot%25202026-01-21%2520at%252019.43.51.png%3Falt%3Dmedia%26token%3D161cbaf8-1b1a-4977-8dbc-fd0e6ff5" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="49d4c15d-bce8-490a-90f8-0fe5bf87783a" data-media-type="file" width="250" height="43" /></span>

Image options

- **Positions:** View market position details, edit collaterals, close or share current position details

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="31c9ff209b20bed2d1d8b25e4cf93460c80623137a99ab88cee5149e455c34cb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252F8UGCVfNiGptmcnERSNTi%25252FScreenshot%2525202026-01-21%252520at%25252019.45.25.png%253Falt%253Dmedia%2526token%253D49f3b4e7-27e4-428f-a710-35fef681?version=1&amp;modificationDate=1768998424294&amp;cacheVersion=1&amp;api=v2" data-height="427" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74580041" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252F8UGCVfNiGptmcnERSNTi%252FScreenshot%25202026-01-21%2520at%252019.45.25.png%3Falt%3Dmedia%26token%3D49f3b4e7-27e4-428f-a710-35fef681" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="0db47759-a085-4a82-8fcd-6fb28598c8a5" data-media-type="file" width="250" height="45" /></span>

Image options

- **Orders:** Any open orders that have not yet been executed. You can also adjust limit/trigger price or cancel (all) orders in this tab.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="efcee6cc32baba8731393ed0bad6e7e53ac486682c72c15f050e754162ae8cf9" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252F7RKBsYYklYR9yXzACSAl%25252FScreenshot%2525202026-01-21%252520at%25252019.44.28.png%253Falt%253Dmedia%2526token%253D0198502d-7269-4a6c-9727-c9fce33b?version=1&amp;modificationDate=1768998424308&amp;cacheVersion=1&amp;api=v2" data-height="485" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74580047" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252F7RKBsYYklYR9yXzACSAl%252FScreenshot%25202026-01-21%2520at%252019.44.28.png%3Falt%3Dmedia%26token%3D0198502d-7269-4a6c-9727-c9fce33b" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="e8f1db1c-071b-4551-a3e4-6c06f2b951e5" data-media-type="file" width="250" height="51" /></span>

Image options

- **History:** Archive of all trades that have been fully executed.

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="1390b103d6d8ebf80edbae4f60fa72099d5925d5e5aacd1195b75b121dd5bacb" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FXcIB5iAFo0QeZtO0Rq12%25252FScreenshot%2525202026-01-21%252520at%25252019.44.38.png%253Falt%253Dmedia%2526token%253Db3b786aa-e44f-4e30-8167-a9a94a34?version=1&amp;modificationDate=1768998424322&amp;cacheVersion=1&amp;api=v2" data-height="326" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74580053" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FXcIB5iAFo0QeZtO0Rq12%252FScreenshot%25202026-01-21%2520at%252019.44.38.png%3Falt%3Dmedia%26token%3Db3b786aa-e44f-4e30-8167-a9a94a34" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="3856a88e-012a-4850-b6e7-6288a4f70c05" data-media-type="file" width="250" height="34" /></span>

Image options

- **Claim:** Funding fees and price impact rebates accumulate during trading and become claimable after position closure. Click **Claim All** to claim all fees at once, or click individual **Claim** buttons for specific fee types

4

Insert a new step

## **Manage Positions**

### **Edit Collateral**

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="57efd304cb82fe8f086efd8df98d27cdd7b8f16992e6220a2d379283c531a831" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252F430UfGc2Xpd3n5HBW64x%25252FScreenshot%2525202026-01-21%252520at%25252019.57.43.png%253Falt%253Dmedia%2526token%253D7cefa2f3-fcbc-4f6d-b37a-d564d9d2?version=1&amp;modificationDate=1768998424336&amp;cacheVersion=1&amp;api=v2" data-height="1016" data-width="910" data-unresolved-comment-count="0" data-linked-resource-id="74580059" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252F430UfGc2Xpd3n5HBW64x%252FScreenshot%25202026-01-21%2520at%252019.57.43.png%3Falt%3Dmedia%26token%3D7cefa2f3-fcbc-4f6d-b37a-d564d9d2" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="7bbf83e9-fc18-44e3-b6a6-a862f784d5e0" data-media-type="file" width="250" height="279" /></span>

Image options

- **Adjust Collateral:** Add or remove collateral without changing size

- **Collateral Edit Limit:** Collaterals are bounded such that

  - **Deposit:** 10 USDC ≤ Deposit \< The collateral size that reduces leverage below **Min Leverage 1.1x**

  - **Withdraw:** Residual remains above 10 USDC, and Withdrawal \< The collateral size that pushes leverage above **Max Leverage 100x**

*Adding collateral improves liquidation price and expands TP/SL price boundaries. Vice versa for remocing collateral.*

### **Position Increase**

- Open an additional order in the same direction on the same market. The system merges positions, recalculating entry price as a weighted average and adjusting leverage based on new total collateral.

### **Position Decrease**

Click Close on the position row. Choose Market or Trigger Price close.

Market Close: Partial or full exposure reduction. Fees apply only to the closed notional; funding/borrow accrual adjusts pro-rata.

Trigger Close (TP/SL): Partial or full exposure reduction only when market price reaches or betters set TP/SL price. Price is bounded by PnL% cap.

Liquidation: If triggered by keepers, a liquidation fee is applied and remaining collateral settles per protocol rules.

Keep Leverage:

Off (default): Reduces size while maintaining collateral (deleverages)

On: Reduces size and collateral proportionally (maintains leverage)

Edit Orders

Click the edit icon next to the order to modify limit order or TP/SL trigger prices without cancelling.

Limit / Trigger Price Edit Limit:

Limit orders: favorable to current mark price

TP orders: within +2500% PnL cap

SL orders: within -80% PnL cap

Cancelling Orders: Remove unwanted pending orders in the Orders tab. Click the cancel icon on the order row, or click Cancel All to remove all active orders.

Cancelled limit orders return reserved collateral. Cancelled TP/SL orders simply remove triggers without affecting positions.

## Liquidity

1

Insert a new step

## Selecting a Pool/Vault

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="89ca7a94791c63eb5b2d163df7a558016fe7fa079baf0b85a9ab21dbd497a644" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FmP0XggqMdZbAsc2AuyOh%25252FScreenshot%2525202026-01-21%252520at%25252020.30.45.png%253Falt%253Dmedia%2526token%253D78a57f22-57f9-4233-9054-e2930e47?version=1&amp;modificationDate=1768999480971&amp;cacheVersion=1&amp;api=v2" data-height="787" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74874925" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FmP0XggqMdZbAsc2AuyOh%252FScreenshot%25202026-01-21%2520at%252020.30.45.png%3Falt%3Dmedia%26token%3D78a57f22-57f9-4233-9054-e2930e47" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="27e34b95-b55b-47e7-a4e3-e7c820f71fd1" data-media-type="file" width="250" height="84" /></span>

Image options

- Browse the pool/vault list or use search to find specific markets

- Filter by asset class: Crypto, Forex, Equities, Indices, Commodities, or Meme

- Toggle **In Wallet** to show only pools where you hold HzLP tokens

- Click on a pool row to view its detail page

2

Insert a new step

## Liquidity Operations

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="eb98910f6a511c9585e26c9b36c5c8f5f82896f10816f42a9a8ee74f40afe88b" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FlBWyNpftQIpYqeipJ0S9%25252FScreenshot%2525202026-01-21%252520at%25252020.35.15.png%253Falt%253Dmedia%2526token%253D800050f4-a27b-413d-afd2-a932f743?version=1&amp;modificationDate=1768999480989&amp;cacheVersion=1&amp;api=v2" data-height="1122" data-width="768" data-unresolved-comment-count="0" data-linked-resource-id="74874931" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FlBWyNpftQIpYqeipJ0S9%252FScreenshot%25202026-01-21%2520at%252020.35.15.png%3Falt%3Dmedia%26token%3D800050f4-a27b-413d-afd2-a932f743" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="7214dd76-254a-498c-97ee-438c63dd6df0" data-media-type="file" width="250" height="365" /></span>

Image options

### Depositing Liquidity

- Navigate to the desired market pool and select the Deposit tab. Enter your USDC amount, with the interface displaying:

  - **HzLP Amount**: Calculated as `Input USDC / HzLP Price`, showing tokens you will receive

  - **HzLP Price**: Current price per token in USDC

  - **Remaining Deposit Cap**: Available capacity before hitting maximum AUM

  - **Approval Status**: Whether USDC spending is approved for the contract

- **Deposit Limit:**

  - Deposit value must not exceed remaining pool capacity (Max AUM - Current AUM)

  - Post-deposit PnL factor must remain compliant with configured threshold

### Withdrawing Liquidity

- Access the Withdraw tab and specify your HzLP token amount. The interface calculates:

  - **USDC Amount**: Calculated as `Input HzLP × HzLP Price`, showing USDC you will receive

  - **Remaining Withdrawal Cap**: Available liquidity considering PnL and reserve constraints

  - **Current HzLP Price**: Token value in USDC at withdrawal

- **Withdrawal Limit:**

  - Withdrawal value must not violate PnL factor constraint

  - Post-withdrawal pool must maintain minimum liquidity thresholds

3

Insert a new step

## Monitor Positions

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="8306261616bbb0ab8950ea011846d9709e1efcc7dafcd81c9b545621943e9822" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/74743814/https%253A%252F%252Ffiles.gitbook.com%252Fv0%252Fb%252Fgitbook-x-prod.appspot.com%252Fo%252Fspaces%25252FhOhbsStDwzyOGMriEWAP%25252Fuploads%25252FVt7dc3SITbULkIX3Ehmi%25252FScreenshot%2525202026-01-21%252520at%25252020.34.26.png%253Falt%253Dmedia%2526token%253D92c52511-9724-476d-99a8-f8d769c8?version=1&amp;modificationDate=1768999481003&amp;cacheVersion=1&amp;api=v2" data-height="1005" data-width="2336" data-unresolved-comment-count="0" data-linked-resource-id="74874937" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="https%3A%2F%2Ffiles.gitbook.com%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FhOhbsStDwzyOGMriEWAP%252Fuploads%252FVt7dc3SITbULkIX3Ehmi%252FScreenshot%25202026-01-21%2520at%252020.34.26.png%3Falt%3Dmedia%26token%3D92c52511-9724-476d-99a8-f8d769c8" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/jpeg" data-linked-resource-container-id="74743814" data-linked-resource-container-version="1" data-media-id="7b9f0258-ba0e-477e-8256-f14a03be747b" data-media-type="file" width="250" height="107" /></span>

Image options

- **Pool Info:** displays critical metrics for assessing pool health:

  - **qTVL (Total Value Locked)**: Current pool AUM in USD

  - **Total Earned Fees**: Cumulative fee income since pool inception

  - **Remaining Deposit Cap**: Available capacity for new deposits

  - **Remaining Withdrawal Cap**: Maximum liquidity available for withdrawal

  - **Your Deposits**: Value of your HzLP holdings in USDC

  - **Your Earned Fees**: Your proportional share of total pool fees

- **Historical Charts:** track TVL and Fee APR over configurable time periods (30d, 90d, 180d), allowing analysis of pool growth and yield trends. Fee APR charts display annualized rate projections from trailing fee income, excluding PnL variance.

- **Liquidity History:** This section records all deposit and withdrawal events with timestamps, token amounts, USD values, and transaction hashes linking to blockchain explorers. Filter between "My Activity" to view personal transactions or "Pool Activity" to monitor overall pool flows.

## **Trading Terms**

**Market Order**: Order type that executes immediately at current mark price, prioritizing speed over price precision.

**Limit Order**: Order type that executes only when market reaches specified price, guaranteeing entry price.

**Take Profit (TP)**: Automated order that closes positions when price reaches favorable level, securing gains. Capped at +2500% PnL.

**Stop Loss (SL)**: Automated order that closes positions when price moves adversely, limiting losses. Capped at -80% PnL.

**Collateral**: USDC deposited to back a leveraged position. Minimum 10 USDC per position.

**Leverage**: Multiplier applied to collateral to determine position size. Range: market-specific, up to 1000x for forex.

**Position Size**: Notional value of position calculated as Collateral × Leverage.

**Entry Price**: Price at which position opens. Market orders use mark price; limit orders use specified price.

**Mark Price**: Current oracle-validated market price used for position valuation and liquidation calculations.

**Liquidation Price**: Price threshold where position automatically closes to prevent negative balance. Calculated based on leverage, fees, and maintenance margin.

**Maintenance Margin Requirement (MMR)**: Minimum collateral required to keep position open, calculated as Size / Max Leverage + Accrued Fees.

**Net Rate**: Combined hourly funding fee and borrow fee, displayed as annualized percentage. Positive = you receive; negative = you pay.

**Funding Fee**: Periodic payment between long and short traders based on market imbalance. Net long pays net short, or vice versa.

**Borrow Fee**: Hourly fee paid by traders to liquidity providers for borrowed capital, based on pool utilization.

**Price Impact**: Fee based on pool imbalance when opening/closing positions. Deferred model: zero at entry, settles at exit. Capped at 50 bps.

**Open Interest (OI)**: Total notional value of all open positions on each side (long and short separately).

**Available Liquidity**: Remaining pool capacity available for new positions on each side.

**Slippage Tolerance**: Maximum acceptable price deviation between expected and execution price for market orders. Default 0.5%, adjustable 0.1%-5%.

**Keep Leverage**: Toggle for position reduction. Off = reduces size while maintaining collateral (deleverages). On = reduces size and collateral proportionally.

**Guaranteed Execution**: TP and SL orders execute at requested trigger price regardless of market gaps, protecting traders from slippage during volatility.

## **Liquidity Provision Terms**

**HzLP**: HertzFlow Liquidity Provider token representing proportional pool ownership. Minted on deposit, burned on withdrawal.

**Pool AUM**: Assets Under Management—total value of pool including deposited USDC, accrued fees, and net unrealized trader PnL.

**HzLP Price**: Token value calculated as Pool AUM / Total HzLP Supply. Increases as fees accrue and traders realize losses.

**TVL (Total Value Locked)**: Current pool AUM in USD, representing all liquidity available for trading.

**Fee APY**: Annualized yield projection from trading fees only (open, close, borrow, liquidation), excluding PnL and funding.

**Total APY**: Comprehensive yield including all sources: fees, trader PnL, and funding. More volatile than Fee APY.

**Max AUM**: Protocol-configured ceiling for each pool's total liquidity, preventing over-concentration and maintaining market balance.

**PnL Factor**: Risk parameter limiting trader unrealized profit as percentage of pool AUM. Three types:

- Max PnL Factor for Deposits (strictest)

- Max PnL Factor for Withdrawals (looser)

- Max PnL Factor for Traders (caps trader exposure)

**Reserve Factor**: Risk parameter ensuring sufficient liquidity remains for open positions. Calculated as Reserved USD / Pool AUM.

**Reserved USD**: Total notional value of open positions (OI) on each side requiring pool backing.

**Remaining Deposit Cap**: Available capacity for new deposits, calculated as Max AUM - Current AUM.

Remaining Withdrawal Cap: Maximum USDC withdrawable, constrained by PnL and reserve factors:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
​Min(
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
​  (AUM - Max(uPnL Long, uPnL Short, 0)) / Max PnL Factor for Withdrawals,
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
​  AUM - Max(Reserved USD Long, Reserved USD Short) / Reserve Factor
```

</div>

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
​)
```

</div>

</div>

Utilization: Percentage of pool liquidity actively backing open positions. High utilization (\>70%) increases borrow fees but constrains withdrawals.

Isolated Pool: Market-specific liquidity with independent risk parameters. Each pool's performance is unaffected by other markets.

Automatic Rebalancing: Contract-level mechanism maintaining 1:1 long-short collateral split regardless of deposit direction or OI imbalance.

Keeper Execution: Automated bot system executing deposits, withdrawals, and position settlements on-chain. Ensures gas efficiency and fast settlement (\<10s typically).

Troubleshooting

Common Issues

"Insufficient Liquidity"

Available liquidity for your direction is depleted. Solutions:

Reduce position size to fit available capacity

Wait for liquidity to replenish as positions close

Trade a different market with deeper liquidity

Check Available Liquidity (L/S) in market info before sizing orders

"Above Max Position Size"

Order exceeds maximum allowed position size for this market. Solutions:

Split into multiple smaller positions

Trade a different market with higher limits

Reduce leverage to lower notional size

"Below Min Collateral"

Collateral must be ≥10 USDC. Solutions:

Increase collateral input to meet minimum

Reduce leverage if trying to maintain specific position size

"Above Deposit Limit \[Amount\]"

Pool at maximum AUM capacity. Solutions:

Wait for pool capacity to increase as traders close positions

Deposit smaller amount within remaining cap

Try a different pool

Check Remaining Deposit Cap in pool info

"Above Withdraw Limit \[Amount\]"

Withdrawal exceeds available capacity due to PnL or reserve constraints. Solutions:

Withdraw smaller amount within remaining cap

Wait for trader PnL to decrease or positions to close

Check Remaining Withdrawal Cap in pool info

"TP Price Below Mark Price" (Long) / "TP Price Above Mark Price" (Short)

Take profit price not favorable to current market. Solutions:

Long positions: increase TP price above mark price

Short positions: decrease TP price below mark price

Verify you're setting profit target in correct direction

"Above Max TP Price" / "Below Min TP Price"

Take profit exceeds +2500% PnL cap. Solutions:

Click tooltip to auto-fill maximum allowed TP price

Manually adjust TP price to valid range

Consider closing position earlier at lower profit target

"SL Price Above Mark Price" (Long) / "SL Price Below Mark Price" (Short)

Stop loss price not unfavorable to current market. Solutions:

Long positions: decrease SL price below mark price

Short positions: increase SL price above mark price

Verify you're setting stop in correct direction

"Invalid Stop Loss"

Stop loss exceeds -80% PnL cap, often after collateral removal. Solutions:

Add collateral back to expand valid SL range

Edit SL price to valid range within -80% cap

Cancel invalid order if protection no longer needed

"Request Rejected by User"

Wallet confirmation cancelled. Solutions:

Review transaction details carefully

Approve transaction in wallet if parameters acceptable

Check wallet isn't locked or disconnected

"Transaction Failed. Please Try Again Later"

Transaction reverted on-chain. Common causes:

Insufficient gas fees (BNB balance too low)

Price moved beyond slippage tolerance (market orders)

Pool capacity changed between quote and execution

Network congestion causing timeout

Solutions:

Verify ≥0.01 BNB balance for gas

Increase slippage tolerance if market is volatile

Refresh quote and retry

Wait a few minutes if network is congested

"Transaction Pending. Please Check Again Later"

Transaction submitted but not confirmed within 30 seconds. Solutions:

Wait for network confirmation (may take 1-5 minutes during congestion)

Check transaction status on BSCScan using hash from toast

Do not resubmit—this creates duplicate transactions

Contact support if pending beyond 5 minutes

Transaction Shows Success but Balance Unchanged

Interface data may be cached. Solutions:

Refresh the page manually

Wait 10-30 seconds for automatic data refresh

Check wallet directly to verify balance changed

Verify transaction on BSCScan shows success

Getting Help

Contact **support@hertzflow.xyz** for account issues, bug reports, or other technical problems.

</div>
