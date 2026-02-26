# Developer Documentation_初稿

<div class="Section1">

# 测试网 开发者文档 - 框架大纲

# HertzFlow Developer Documentation

## Overview

### Introduction

\[PROTOCOL_NAME\] is a \[brief description of what the protocol does\]. This documentation provides technical details for developers integrating with or building on the protocol.

**Key Features:**

- \[Feature 1\]

- \[Feature 2\]

- \[Feature 3\]

**Contract Addresses:**

- Network: \[CHAIN_NAME\]

- Main Contract: `[CONTRACT_ADDRESS]`

- \[Additional contract addresses as needed\]

------------------------------------------------------------------------

## Architecture

### System Design

The protocol follows a modular architecture separating concerns into distinct contract types:

**Core Components:**

- **Bank Contracts** - Hold protocol funds and assets

- **Data Storage** - Persistent state management via DataStore pattern

- **Logic Contracts** - Stateless business logic execution

- **Handler Contracts** - Request processing and execution

**Design Principles:**

- Separation of state and logic enables upgradeability

- EnumerableSets provide efficient on-chain querying

- Event emission through centralized EventEmitter for consistent indexing

### Contract Structure

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
[Diagram or text description of contract hierarchy]
```

</div>

</div>

**Key Contracts:**

- `[CoreContract1]` - \[Purpose\]

- `[CoreContract2]` - \[Purpose\]

- `[CoreContract3]` - \[Purpose\]

------------------------------------------------------------------------

## Getting Started

### Prerequisites

- Solidity ^0.8.0

- Node.js \>= 16.0

- Hardhat or Foundry

### Installation

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
npm install @[protocol]/contracts
```

</div>

</div>

### Quick Start

\[CODE_EXAMPLE: Basic integration example\]

------------------------------------------------------------------------

## Core Concepts

### \[Concept 1: e.g., Markets, Vaults, etc.\]

\[Description of the core concept\]

**How it works:**

1.  \[Step 1\]

2.  \[Step 2\]

3.  \[Step 3\]

**Key Parameters:**

- `[parameter1]` - \[Description\]

- `[parameter2]` - \[Description\]

**Example:** \[CODE_EXAMPLE\]

### \[Concept 2: e.g., Liquidity Provision\]

\[Description\]

**Process Flow:**

1.  User approves token spending via Router

2.  Creates request through \[HandlerContract\]

3.  Keepers execute request with oracle prices

4.  Tokens minted/burned accordingly

**Important Notes:**

- \[Note 1\]

- \[Note 2\]

------------------------------------------------------------------------

## Request-Response Pattern

### Two-Step Execution Model

All state-changing operations follow a two-step pattern to prevent front-running:

**Step 1: Request Creation**

- User submits transaction with request parameters

- Request stored on-chain with timestamp

- Gas estimation and execution fees calculated

**Step 2: Keeper Execution**

- Keepers monitor pending requests

- Fetch signed oracle prices for execution block

- Bundle prices with request and execute

**Request Types:**

- Deposits

- Withdrawals

- Orders

- \[Additional types\]

### Request Lifecycle

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
Creation → Pending → Execution/Cancellation → Finalized
```

</div>

</div>

**Cancellation Rules:**

- Minimum delay: `[TIME]` seconds

- Cancellable by: Original submitter

- Refund policy: \[Details\]

------------------------------------------------------------------------

## Oracle System

### Price Feed Architecture

The protocol uses an off-chain oracle system with on-chain verification:

**Components:**

1.  **Oracle Keepers** - Fetch prices from reference exchanges

2.  **Price Signing** - Cryptographic signing of min/max prices

3.  **Archive Nodes** - Store and serve signed prices

4.  **On-chain Validation** - Verify signatures and timestamp

### Price Representation

Prices stored with 30 decimals precision:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
price_stored = price_actual / (10^token_decimals) * (10^30)
```

</div>

</div>

**Examples:**

*ETH (18 decimals, \$5000):*

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
5000 / (10^18) * (10^30) = 5000 * (10^12)
```

</div>

</div>

*BTC (8 decimals, \$60,000):*

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
60,000 / (10^8) * (10^30) = 60,000 * (10^22)
```

</div>

</div>

*USDC (6 decimals, \$1):*

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
1 / (10^6) * (10^30) = 1 * (10^24)
```

</div>

</div>

### Price Precision Configuration

**Decimal Multiplier Formula:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
decimals = 30 - token_decimals - desired_precision
```

</div>

</div>

**Gas Optimization:**

- Prices compressed using uint8 multiplier + uint32 value

- Reduces calldata costs while maintaining precision

\[LINK_TO_ORACLE_CONTRACT_DETAILS\]

------------------------------------------------------------------------

## Fee Structure

### Fee Types

**Trading Fees:**

- Swap fees: `[PERCENTAGE]%` of swap amount

- Position fees: `[PERCENTAGE]%` of position size change

- Execution fees: Dynamic based on gas costs

**Protocol Fees:**

- Funding fees: Paid by imbalanced side to balanced side

- Borrowing fees: Prevents zero-cost capacity occupation

- Price impact: Incentivizes pool balance

### Funding Fees

Formula:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
funding_per_second = (funding_factor) * (OI_imbalance^exponent) / total_OI
```

</div>

</div>

**Parameters:**

- `fundingFactor` - Base funding rate

- `fundingExponent` - Non-linearity factor

- `OI_imbalance` - Difference between long/short open interest

**Dynamic Adjustment:**

- Increases when imbalance \> `thresholdForStableFunding`

- Stable when within threshold range

- Decreases when \< `thresholdForDecreaseFunding`

### Borrowing Fees

**Curve Model:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
borrowing_per_second = borrowingFactor * (reservedUSD^exponent) / poolUSD
```

</div>

</div>

**Kink Model:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
rate = baseBorrowingFactor * usageFactor

if (usageFactor > optimalUsageFactor):
    additionalRate = (aboveOptimalFactor - baseRate) * excess / (1 - optimal)
    rate += additionalRate
```

</div>

</div>

**Configuration Options:**

- `skipBorrowingFeeForSmallerSide` - Exempts smaller OI side

### Price Impact

Calculated as delta in imbalance:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
impact = (initial_diff^exponent * factor) - (next_diff^exponent * factor)
```

</div>

</div>

**Purposes:**

1.  Incentivize token balance in pools

2.  Balance long/short open interest

3.  Mitigate price manipulation risk

**Impact Types:**

- Negative: Charged when worsening imbalance

- Positive: Rebated when improving imbalance

- Capped: Max values prevent extreme scenarios

**Virtual Inventory:**

- Tracks imbalance across similar markets

- Reduces arbitrage opportunities

- Must configure same-decimals markets in groups

\[LINK_TO_FEE_CALCULATOR_TOOL\]

------------------------------------------------------------------------

## Integration Guide

### Depositing Liquidity

**Process:**

1.  Approve token spending on Router contract

2.  Call `createDeposit()` on ExchangeRouter

3.  Wait for keeper execution

4.  Receive minted tokens

**Function Signature:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createDeposit(
    address market,
    uint256 longTokenAmount,
    uint256 shortTokenAmount,
    uint256 minMarketTokens
) external returns (bytes32 depositKey);
```

</div>

</div>

**Parameters:**

- `market` - Target market address

- `longTokenAmount` - Amount of long collateral

- `shortTokenAmount` - Amount of short collateral

- `minMarketTokens` - Minimum acceptable output

**Callbacks:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function afterDepositExecution(
    bytes32 key,
    Deposit.Props memory deposit,
    EventUtils.EventLogData memory eventData
) external;

function afterDepositCancellation(
    bytes32 key,
    Deposit.Props memory deposit,
    EventUtils.EventLogData memory eventData
) external;
```

</div>

</div>

**Important Considerations:**

- First deposit per market sent to `RECEIVER_FOR_FIRST_DEPOSIT`

- PnL factor affects token pricing

- Price impact applies

- Cancellation delay: `[TIME]` seconds

\[CODE_EXAMPLE: Complete deposit flow\]

### Withdrawing Liquidity

**Process:**

1.  Approve market token spending

2.  Call `createWithdrawal()` on ExchangeRouter

3.  Specify long/short token amounts

4.  Receive underlying tokens after execution

**Function Signature:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createWithdrawal(
    address market,
    uint256 marketTokenAmount,
    uint256 minLongTokenAmount,
    uint256 minShortTokenAmount
) external returns (bytes32 withdrawalKey);
```

</div>

</div>

**Output Considerations:**

- Two separate minimum amounts required

- Both tokens may be received

- Price impact and fees apply

- Withdrawal may fail if above MAX_PNL_FACTOR

\[CODE_EXAMPLE: Complete withdrawal flow\]

### Trading (Swaps)

**Swap Types:**

- Market swaps: Immediate execution

- Limit swaps: Execute at target price

**Creating Swap Orders:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createOrder(
    CreateOrderParams memory params
) external returns (bytes32 orderKey);
```

</div>

</div>

**Parameters:**

- `initialCollateralToken` - Input token

- `swapPath` - Array of markets to route through

- `minOutputAmount` - Slippage protection

- `orderType` - MarketSwap or LimitSwap

**Price Impact:**

- Based on pool imbalance

- Virtual inventory affects pricing

- Positive impact possible but capped

\[CODE_EXAMPLE: Swap execution\]

### Position Trading

#### Opening Positions

**Market Orders:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
CreateOrderParams({
    orderType: OrderType.MarketIncrease,
    initialCollateralToken: collateral,
    swapPath: [market],
    sizeDeltaUsd: positionSize,
    isLong: true/false,
    // ... additional params
})
```

</div>

</div>

**Limit Orders:**

- Long: Triggers when price ≤ acceptablePrice

- Short: Triggers when price ≥ acceptablePrice

**Key Considerations:**

- Leverage = sizeDelta / collateral

- Minimum collateral enforced

- Price impact affects entry price

- Borrowing fees accrue immediately

#### Closing Positions

**Market Decrease:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
CreateOrderParams({
    orderType: OrderType.MarketDecrease,
    sizeDeltaUsd: sizeToClose,
    initialCollateralDeltaAmount: collateralToWithdraw,
    // ... additional params
})
```

</div>

</div>

**Stop-Loss Orders:**

- Long: Triggers when price ≤ acceptablePrice

- Short: Triggers when price ≥ acceptablePrice

**Outputs:**

- May receive two tokens if swap occurs

- Collateral + PnL - fees

- Possible negative price impact cap

#### Position Management

**Auto-Adjustments:**

- `sizeDelta` reduced if exceeds available

- `collateralDelta` capped at position collateral

- Zero-size positions automatically closed

**Liquidations:**

- Triggered when collateral insufficient

- Keeper executes liquidation

- Callback to saved contract address

- Referral rewards still distributed

\[CODE_EXAMPLE: Complete position lifecycle\]

------------------------------------------------------------------------

## Advanced Topics

### Callback Contracts

Implement custom logic triggered by protocol events:

**Interface:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
interface IDepositCallbackReceiver {
    function afterDepositExecution(...) external;
    function afterDepositCancellation(...) external;
}

interface IOrderCallbackReceiver {
    function afterOrderExecution(...) external;
    function afterOrderCancellation(...) external;
    function afterOrderFrozen(...) external;
}
```

</div>

</div>

**Security Requirements:**

- Validate msg.sender has CONTROLLER role

- Verify event matches expected execution

- Handle multiple handler versions

- Ensure sufficient gas for callback

- Execution continues even if callback reverts

**Best Practices:**

- Use RoleStore for handler validation

- Don't assume fixed event structure

- Test with old and new handlers

- Plan for parameter additions

\[CODE_EXAMPLE: Safe callback implementation\]

### Subaccounts

Delegate trading permissions without full account access:

**Capabilities:**

- Create, update, cancel orders

- Spend WNT and collateral

- Cannot withdraw to different address

**Use Cases:**

- Trading bots

- Strategy automation

- Managed accounts

\[LINK_TO_SUBACCOUNT_SETUP\]

### Market Token Pricing

Price calculation:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
price = pool_worth / totalSupply
```

</div>

</div>

**Pool Worth Components:**

- Deposited token values

- Pending trader PnL (capped)

- Pending borrow fees

- Impact pool adjustments

**PnL Factor Caps:**

- `MAX_PNL_FACTOR_FOR_DEPOSITS` - Deposit pricing

- `MAX_PNL_FACTOR_FOR_WITHDRAWALS` - Withdrawal pricing

- `MAX_PNL_FACTOR_FOR_TRADERS` - Position closing

**Risk Management:**

- Different caps create deposit incentives

- Prevents extreme price movements

- Protects LP interests during volatility

\[LINK_TO_PRICE_CALCULATOR\]

### Gas Optimization

**Batching:**

- Multiple operations in single transaction

- Reduced approval transactions

- Shared execution fees

**Calldata Optimization:**

- Compressed price feeds

- Efficient parameter encoding

- Minimal storage reads

**Recommended Patterns:** \[CODE_EXAMPLE: Gas-efficient integration\]

------------------------------------------------------------------------

## Configuration & Parameters

### Market Parameters

<div class="table-wrap">

|                       |                                |                |
|-----------------------|--------------------------------|----------------|
| Parameter             | Description                    | Typical Range  |
| `minCollateralFactor` | Min collateral / position size | 0.01 - 0.05    |
| `maxPoolAmount`       | Max tokens in pool             | Token-specific |
| `maxOpenInterest`     | Max total OI                   | USD amount     |
| `reserveFactor`       | Reserved / pool cap            | 0.5 - 0.95     |
| `maxPnlFactor`        | Max PnL / pool                 | 0.3 - 0.6      |

</div>

### Fee Parameters

<div class="table-wrap">

|                     |                         |                    |
|---------------------|-------------------------|--------------------|
| Parameter           | Description             | Typical Range      |
| `positionFeeFactor` | Position open/close fee | 0.0005 - 0.001     |
| `swapFeeFactor`     | Swap fee rate           | 0.0005 - 0.002     |
| `fundingFactor`     | Funding rate base       | 1/50000 per second |
| `borrowingFactor`   | Borrow rate base        | 1/50000 per second |

</div>

### Price Impact Parameters

<div class="table-wrap">

|                           |                            |                 |
|---------------------------|----------------------------|-----------------|
| Parameter                 | Description                | Notes           |
| `positionImpactFactor`    | Position impact multiplier | Market-specific |
| `swapImpactFactor`        | Swap impact multiplier     | Market-specific |
| `positionImpactExponent`  | Non-linearity factor       | Typically 1-2   |
| `maxPositionImpactFactor` | Cap on negative impact     | Safety limit    |

</div>

\[LINK_TO_PARAMETER_REFERENCE\]

------------------------------------------------------------------------

## Security

### Role-Based Access Control

**Core Roles:**

- `ROLE_ADMIN` - Grant/revoke permissions (Timelock only)

- `CONTROLLER` - Execute state changes (Handlers)

- `CONFIG_KEEPER` - Update configuration

- `ORDER_KEEPER` - Execute orders

- `FROZEN_ORDER_KEEPER` - Handle frozen orders

**Security Model:**

- No EOA should have CONTROLLER role

- Config changes via timelock only

- Keeper network prevents single-point control

- Multisig can revoke compromised accounts

### Known Risks

**Token Compatibility:**

- Rebasing tokens not supported

- Transfer fee tokens incompatible

- ERC-777 callbacks disallowed

- Requires whitelisting with gas limits

**Keeper Risks:**

- Transaction ordering exploitation

- Delayed execution possibility

- Price selection in limit orders

- Mitigation via keeper network

**Price Impact Gaming:**

- Cross-market arbitrage possible

- High-leverage impact reduction

- Mitigation via virtual inventory

- Min collateral multipliers

**Blockchain Dependencies:**

- Sequencer downtime affects L2s

- Block reorg risks on some chains

- Timestamp manipulation considerations

- Oracle keeper coordination required

**Market Token Risks:**

- Negative pool value possible (rare)

- Impact pool accumulation

- Liquidity provider exposure

- Proper parameter configuration essential

\[LINK_TO_SECURITY_AUDIT_REPORTS\]

------------------------------------------------------------------------

## Integration Checklist

### Pre-Integration

- \[ \] Review contract addresses for target network

- \[ \] Verify contract source code

- \[ \] Understand two-step execution model

- \[ \] Plan for request cancellations

- \[ \] Design callback contract if needed

- \[ \] Test on testnet environment

### Token Handling

- \[ \] Check token compatibility (no rebasing, no transfer fees)

- \[ \] Implement proper approval patterns

- \[ \] Handle both token outputs for decreases

- \[ \] Account for execution fee refunds

- \[ \] Plan for ETH/WETH conversions

- \[ \] Consider multiple token decimals

### Order Management

- \[ \] Validate minimum output amounts

- \[ \] Set appropriate acceptable prices

- \[ \] Handle order cancellations gracefully

- \[ \] Monitor frozen order states

- \[ \] Implement retry logic for failures

- \[ \] Track pending requests

### Callback Implementation

- \[ \] Whitelist multiple handler versions

- \[ \] Validate msg.sender role

- \[ \] Handle execution and cancellation

- \[ \] Ensure sufficient gas allocation

- \[ \] Test with old and new handlers

- \[ \] Never assume fixed event structure

### Risk Management

- \[ \] Monitor position collateral ratios

- \[ \] Track funding fee accumulation

- \[ \] Account for price impact caps

- \[ \] Plan for market disabling

- \[ \] Handle liquidation scenarios

- \[ \] Implement slippage protection

### Testing

- \[ \] Test deposit flow end-to-end

- \[ \] Test withdrawal with two outputs

- \[ \] Test swap through multiple markets

- \[ \] Test position lifecycle

- \[ \] Test callback contract integration

- \[ \] Test failure and cancellation paths

- \[ \] Load test with realistic volumes

------------------------------------------------------------------------

## API Reference

### ExchangeRouter

Primary entry point for user interactions.

#### `createDeposit`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createDeposit(
    CreateDepositParams memory params
) external returns (bytes32);
```

</div>

</div>

\[Detailed parameter documentation\]

#### `createWithdrawal`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createWithdrawal(
    CreateWithdrawalParams memory params
) external returns (bytes32);
```

</div>

</div>

\[Detailed parameter documentation\]

#### `createOrder`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function createOrder(
    CreateOrderParams memory params
) external returns (bytes32);
```

</div>

</div>

\[Detailed parameter documentation\]

#### `claimFundingFees`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function claimFundingFees(
    address[] memory markets,
    address[] memory tokens
) external returns (uint256[]);
```

</div>

</div>

\[Detailed parameter documentation\]

#### `claimCollateral`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function claimCollateral(
    address[] memory markets,
    address[] memory tokens
) external returns (uint256[]);
```

</div>

</div>

\[Detailed parameter documentation\]

### Reader

Query protocol state without transactions.

#### `getMarketInfo`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getMarketInfo(
    address market
) external view returns (MarketInfo memory);
```

</div>

</div>

\[Return value documentation\]

#### `getPosition`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getPosition(
    address account,
    address market,
    address collateralToken,
    bool isLong
) external view returns (Position.Props memory);
```

</div>

</div>

\[Return value documentation\]

#### `getMarketTokenPrice`

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getMarketTokenPrice(
    address market,
    bool maximize
) external view returns (uint256);
```

</div>

</div>

\[Return value documentation\]

\[LINK_TO_COMPLETE_API_REFERENCE\]

------------------------------------------------------------------------

## Testing

### Local Development

**Setup:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
git clone [REPOSITORY_URL]
cd [project]
npm install
```

</div>

</div>

**Run Tests:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
npx hardhat test
npx hardhat coverage
```

</div>

</div>

**Measure Contracts:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
npx hardhat measure-contract-sizes
```

</div>

</div>

### Test Networks

<div class="table-wrap">

|              |         |          |          |
|--------------|---------|----------|----------|
| Network      | RPC URL | Chain ID | Faucet   |
| \[Testnet1\] | \[URL\] | \[ID\]   | \[LINK\] |
| \[Testnet2\] | \[URL\] | \[ID\]   | \[LINK\] |

</div>

**Deployed Contracts:**

- ExchangeRouter: `[ADDRESS]`

- Reader: `[ADDRESS]`

- DataStore: `[ADDRESS]`

\[LINK_TO_TESTNET_GUIDE\]

------------------------------------------------------------------------

## Deployment

### Contract Verification

**Hardhat:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
npx hardhat verify --network [network] [address] [constructor-args]
```

</div>

</div>

**Foundry:**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
forge verify-contract [address] [contract] --chain-id [id]
```

</div>

</div>

**Notes:**

- MarketToken contracts share source code

- Verify one, others auto-verify

- Use `scripts/verifyFallback.ts` for batch verification

### Configuration Steps

1.  Deploy core contracts (DataStore, RoleStore)

2.  Deploy factory contracts

3.  Deploy handler contracts

4.  Configure oracle system

5.  Set initial parameters

6.  Create markets

7.  Transfer roles to timelock

8.  Verify all contracts

\[LINK_TO_DEPLOYMENT_SCRIPTS\]

------------------------------------------------------------------------

## Upgrade Guide

### Contract Upgrades

**Critical Considerations:**

- Disable old contracts before enabling new

- Check for pricing calculation changes

- Notify integrations of struct modifications

- Publish detailed changelog

- Maintain callback compatibility where possible

**Breaking Changes:**

- EventData ordering changes

- Struct field additions/removals

- Function signature modifications

- New role requirements

**Migration Process:**

1.  Announce upgrade timeline

2.  Deploy new contracts

3.  Test on staging environment

4.  Disable old contracts via timelock

5.  Enable new contracts

6.  Monitor closely for 48 hours

7.  Update documentation

### Integration Updates

**When to Update:**

- ExchangeRouter address changes

- Oracle contract updates

- Reader contract improvements

- New handler deployments

**Backward Compatibility:**

- Callback structs carefully managed

- EventData keys maintained when possible

- Function signatures avoid breaking changes

- Deprecated functions clearly marked

\[LINK_TO_CHANGELOG\]

------------------------------------------------------------------------

## Troubleshooting

### Common Issues

**Deposit Fails:**

- Check token approval amounts

- Verify market is not disabled

- Ensure below MAX_PNL_FACTOR_FOR_DEPOSITS

- Confirm min output achievable with current impact

**Withdrawal Fails:**

- Check both min output amounts

- Verify below MAX_PNL_FACTOR_FOR_WITHDRAWALS

- Ensure sufficient market token balance

- Account for price impact and fees

**Order Not Executing:**

- Verify acceptable price still valid

- Check if market is disabled

- Confirm keeper network operational

- Review frozen order status

**Position Liquidated:**

- Monitor collateral ratio continuously

- Account for funding fee accrual

- Consider borrowing fee impact

- Set appropriate stop-loss orders

**Callback Not Triggered:**

- Ensure handler whitelisted

- Check callback gas limits

- Verify contract implements interface

- Review event logs for errors

### Error Messages

<div class="table-wrap">

|  |  |  |
|----|----|----|
| Error | Cause | Solution |
| `InsufficientCollateral` | Position undercollateralized | Add collateral or reduce size |
| `MaxPnlExceeded` | PnL cap reached | Wait for rebalancing |
| `PriceImpactTooHigh` | Excessive impact | Reduce order size |
| `OrderNotExecutable` | Price conditions not met | Adjust acceptable price |

</div>

\[LINK_TO_ERROR_REFERENCE\]

------------------------------------------------------------------------

## Examples

### Complete Deposit Flow

\[CODE_EXAMPLE: Full implementation with error handling\]

### Complete Trading Bot

\[CODE_EXAMPLE: Automated position management\]

### Multi-Market Strategy

\[CODE_EXAMPLE: Cross-market trading\]

### Custom Callback Handler

\[CODE_EXAMPLE: Event-driven automation\]

------------------------------------------------------------------------

## Resources

### Official Links

- Website: \[URL\]

- GitHub: \[URL\]

- Discord: \[URL\]

- Twitter: \[URL\]

### Developer Tools

- SDK: \[LINK\]

- Subgraph: \[LINK\]

- Price API: \[LINK\]

- Analytics Dashboard: \[LINK\]

### Documentation

- Contract Reference: \[LINK\]

- Integration Examples: \[LINK\]

- Video Tutorials: \[LINK\]

- Community Guides: \[LINK\]

### Audits & Security

- Audit Report 1: \[LINK\]

- Audit Report 2: \[LINK\]

- Bug Bounty Program: \[LINK\]

- Security Contact: \[EMAIL\]

------------------------------------------------------------------------

## Support

### Getting Help

**For Integration Support:**

- Developer Discord: \[LINK\]

- GitHub Issues: \[LINK\]

- Email: \[developer@example.com\]

**For Bug Reports:**

- GitHub Security Advisory: \[LINK\]

- Bug Bounty: \[LINK\]

**For General Questions:**

- Documentation: \[LINK\]

- Community Forum: \[LINK\]

- FAQ: \[LINK\]

------------------------------------------------------------------------

## Changelog

### Version \[X.X.X\] - \[Date\]

- \[Change description\]

- \[Breaking change warning\]

- \[Migration guide link\]

### Version \[X.X.X\] - \[Date\]

- \[Change description\]

\[LINK_TO_FULL_CHANGELOG\]

------------------------------------------------------------------------

## License

\[License information\]

## Contributors

\[Attribution and thanks\]

------------------------------------------------------------------------

*Last Updated: \[DATE\]* *Documentation Version: \[VERSION\]*

# 主网 开发者文档 - 框架大纲

## 第一部分：基础文档

### 1. 简介

- 1.1 概述

- 1.2 核心特性

- 1.3 前置要求

### 2. 快速开始

- 2.1 安装

  - 包管理器安装

  - 系统要求

- 2.2 快速开始示例

  - 最小化配置示例

  - 第一个 API 调用

- 2.3 身份验证与配置

### 3. 核心概念

- 3.1 架构概述

- 3.2 数据模型

- 3.3 状态管理

- 3.4 错误处理

## 第二部分：API 与 SDK

### 4. API 参考

- 4.1 REST API

  - 端点概览

  - 端点：健康检查

  - 端点：\[资源名称\]

- 4.2 WebSocket API

  - 连接

  - 订阅事件

  - 消息格式

- 4.3 GraphQL API

  - 端点

  - 查询示例

### 5. SDK 参考

- 5.1 初始化

  - 配置接口

  - 初始化 SDK

- 5.2 市场模块

  - 获取市场列表

  - 获取市场信息

- 5.3 交易模块

  - 创建订单

  - 平仓

- 5.4 仓位模块

  - 获取用户仓位

  - 仓位接口

- 5.5 工具模块

  - 计算费用

  - 格式化单位

## 第三部分：实战指南

### 6. 代码示例

- 6.1 完整交易流程

- 6.2 监控仓位

- 6.3 实时价格推送

- 6.4 代币兑换

### 7. 集成指南

- 7.1 Web3 钱包集成

  - 使用 wagmi

  - 使用 ethers.js

- 7.2 自定义 RPC 提供者

- 7.3 交易签名

  - 本地签名器

  - AWS KMS 集成

### 8. 智能合约

- 8.1 合约地址

  - 主网

  - 测试网

- 8.2 合约接口

  - 核心方法

- 8.3 直接合约交互

### 10. 数据索引

- 10.1 Subgraph 查询

  - 端点

  - 查询历史数据

- 10.2 Subsquid 集成

### 11. 故障排除

- 11.1 常见问题

  - 问题：交易回滚

  - 问题：RPC 连接失败

  - 问题：价格推送延迟

- 11.2 调试模式

- 11.3 网络状态检查

### 12. API 速率限制

- 12.1 REST API 限制

- 12.2 处理速率限制

### 13. 支持与资源

- 13.1 文档链接

- 13.2 社区渠道

- 13.3 开发者支持

- 13.4 更新与变更日志

### 14. 常见问题

- Q: 支持哪些网络？

- Q: 如何获取测试网代币？

- Q: 最小订单量是多少？

- Q: 费用如何计算？

- Q: 可以用于生产环境吗？

## 必备结构说明

**API**

- **REST / RPC 接口**：列出主要端点（例如订单获取、交易提交、池状态查询）、请求/响应 schema。明确所有 API 路径、参数、响应示例。

- **链上数据同步机制**：如何构建索引器（indexer）或后端服务同步事件、提取交易、LP 数据等支持 API 查询。

- <a href="https://sdk.avantisfi.com/api_reference.html" class="external-link" rel="nofollow"><strong>平台接口设计</strong>：REST/WebSocket 接口模块设计</a>

- **缓存与性能优化**：数据延迟 SLA 目标（例如 ≤ 500ms）、缓存策略、批量查询与分页。

**SDK**

- 给出 JS/TS SDK 的 `npm install`、示例代码。

- 前端 Demo（可以直接跑）+ 集成最佳实践。

- **SDK 架构**：提供易用的交易调用、行情数据获取、参数查询、SDK 示例和文档结构

- <a href="https://github.com/Reya-Labs/reya-python-sdk#" class="external-link" rel="nofollow">github</a>跳链接或<a href="https://cetus-1.gitbook.io/cetus-developer-docs/developer/via-sdk-v2/getting-started" class="external-link" rel="nofollow">docs列举</a>或<a href="https://sdk.avantisfi.com/introduction.html" class="external-link" rel="nofollow">第三方文档</a>形式无所谓，文档结构清晰即可

- **类型定义与文档**：TypeScript / Rust SDK 的类型定义、错误处理、连接管理等。

- **SDK 架构**：提供易用的交易调用、行情数据获取、参数查询、SDK 示例和文档结构 (<a href="https://sdk.avantisfi.com/introduction.html?utm_source=chatgpt.com" class="external-link" rel="nofollow">Avantis Trader SDK</a>)。

# 文档部分

## 1. Introduction

### 1.1 Overview

Brief introduction to the protocol/platform, its purpose, and core value proposition. Establish what developers can build and achieve using the tools provided.

### 1.2 Key Features

- List primary capabilities

- Highlight unique technical advantages

- Identify target developer use cases

### 1.3 Prerequisites

- Required technical knowledge

- Supported chains/networks

- Development environment requirements

------------------------------------------------------------------------

## 2. Getting Started

### 2.1 Installation

#### Package Manager Installation

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# npm
npm install [PACKAGE_NAME]

# yarn
yarn add [PACKAGE_NAME]

# pip (if Python SDK)
pip install [PACKAGE_NAME]
```

</div>

</div>

#### System Requirements

- Node.js version: \[VERSION\]

- Python version: \[VERSION\] (if applicable)

- Required dependencies

### 2.2 Quick Start

#### Minimal Setup Example

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Initialize client
import { Client } from '[PACKAGE]';

const client = new Client({
  chainId: [CHAIN_ID],
  rpcUrl: '[RPC_URL]',
  // Additional config
});
```

</div>

</div>

#### First API Call

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Example: Fetch market data
const data = await client.markets.getInfo();
console.log(data);
```

</div>

</div>

### 2.3 Authentication & Configuration

- API keys (if required)

- Wallet connection methods

- Network configuration

- Environment variables setup

------------------------------------------------------------------------

## 3. Core Concepts

### 3.1 Architecture Overview

Explain the system's fundamental design patterns and component relationships.

### 3.2 Data Models

Define key data structures, types, and their relationships.

### 3.3 State Management

How data flows through the system and best practices for state handling.

### 3.4 Error Handling

- Common error types

- Error codes and meanings

- Recommended error handling patterns

------------------------------------------------------------------------

## 4. API Reference

### 4.1 REST API

#### Endpoints Overview

Organized by resource type with base URLs for each supported network.

#### Endpoint: Health Check

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET [BASE_URL]/ping
```

</div>

</div>

**Description**: Verify API availability

**Response**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "status": "ok",
  "timestamp": 1234567890
}
```

</div>

</div>

#### Endpoint: \[Resource Name\]

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
GET [BASE_URL]/[resource]
```

</div>

</div>

**Description**: \[Brief description\]

**Parameters**:

<div class="table-wrap">

|        |        |          |                 |
|--------|--------|----------|-----------------|
| Name   | Type   | Required | Description     |
| param1 | string | Yes      | \[Description\] |
| param2 | number | No       | \[Description\] |

</div>

**Response**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "field1": "value",
  "field2": 123
}
```

</div>

</div>

**Example**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
curl [FULL_URL_EXAMPLE]
```

</div>

</div>

### 4.2 WebSocket API (if applicable)

#### Connection

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const ws = new WebSocket('[WS_URL]');
```

</div>

</div>

#### Subscribe to Events

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ws.send(JSON.stringify({
  type: 'subscribe',
  channel: '[CHANNEL_NAME]'
}));
```

</div>

</div>

#### Message Format

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  "type": "update",
  "data": {}
}
```

</div>

</div>

### 4.3 GraphQL API (if applicable)

#### Endpoint

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST [GRAPHQL_URL]
```

</div>

</div>

#### Query Examples

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
query {
  markets {
    id
    name
    volume
  }
}
```

</div>

</div>

------------------------------------------------------------------------

## 5. SDK Reference

### 5.1 Initialization

#### Configuration Interface

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
interface ClientConfig {
  chainId: number;
  rpcUrl: string;
  oracleUrl?: string;
  walletClient?: WalletClient;
  publicClient?: PublicClient;
}
```

</div>

</div>

#### Initialize SDK

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { SDK } from '[PACKAGE]';

const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  oracleUrl: '[ORACLE_URL]'
});
```

</div>

</div>

### 5.2 Markets Module

#### Get Markets List

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const markets = await sdk.markets.getMarkets({
  offset?: number,
  limit?: number
});
```

</div>

</div>

**Returns**: `Market[]`

#### Get Market Info

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const { marketsInfoData, tokensData } = await sdk.markets.getMarketsInfo();
```

</div>

</div>

**Returns**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
{
  marketsInfoData: MarketInfoData[];
  tokensData: TokenData;
}
```

</div>

</div>

### 5.3 Trading Module

#### Create Order

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
await sdk.orders.createOrder({
  marketAddress: string;
  size: bigint;
  collateralAddress: string;
  isLong: boolean;
  slippage: number;
  // Additional parameters
});
```

</div>

</div>

**Parameters**:

- `marketAddress`: Contract address of the market

- `size`: Position size in base units

- `collateralAddress`: Token used as collateral

- `isLong`: Direction (true for long, false for short)

- `slippage`: Allowed slippage in basis points

**Returns**: Transaction hash

#### Close Position

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
await sdk.orders.closePosition({
  positionId: string;
  size?: bigint;
  // Partial close parameters
});
```

</div>

</div>

### 5.4 Positions Module

#### Get User Positions

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
sdk.setAccount('[WALLET_ADDRESS]');

const positions = await sdk.positions.getPositions({
  marketsInfoData,
  tokensData,
  start: 0,
  end: 1000
});
```

</div>

</div>

**Returns**: `Position[]`

#### Position Interface

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
interface Position {
  id: string;
  market: string;
  collateral: bigint;
  size: bigint;
  isLong: boolean;
  entryPrice: bigint;
  // Additional fields
}
```

</div>

</div>

### 5.5 Utilities Module

#### Calculate Fees

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const fees = await sdk.utils.calculateFees({
  size: bigint;
  marketAddress: string;
});
```

</div>

</div>

#### Format Units

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const formatted = sdk.utils.formatUnits(value, decimals);
```

</div>

</div>

------------------------------------------------------------------------

## 6. Code Examples

### 6.1 Complete Trading Flow

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { SDK } from '[PACKAGE]';
import { parseUnits } from 'viem';

async function executeTradeExample() {
  // 1. Initialize SDK
  const sdk = new SDK({
    chainId: 42161,
    rpcUrl: process.env.RPC_URL,
    walletClient: walletClient
  });

  // 2. Fetch market data
  const { marketsInfoData, tokensData } = await sdk.markets.getMarketsInfo();
  
  // 3. Select market
  const market = marketsInfoData[0];
  
  // 4. Prepare order parameters
  const orderParams = {
    marketAddress: market.address,
    size: parseUnits('1000', 6), // $1000 USDC
    collateralAddress: '[USDC_ADDRESS]',
    isLong: true,
    slippage: 50 // 0.5%
  };
  
  // 5. Execute order
  const tx = await sdk.orders.createOrder(orderParams);
  
  console.log('Transaction:', tx);
}
```

</div>

</div>

### 6.2 Monitor Positions

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
async function monitorPositions(walletAddress: string) {
  sdk.setAccount(walletAddress);
  
  // Fetch market context
  const { marketsInfoData, tokensData } = await sdk.markets.getMarketsInfo();
  
  // Get all positions
  const positions = await sdk.positions.getPositions({
    marketsInfoData,
    tokensData,
    start: 0,
    end: 100
  });
  
  // Process positions
  for (const position of positions) {
    console.log(`Position: ${position.market}`);
    console.log(`Size: ${position.size}`);
    console.log(`PnL: ${position.unrealizedPnl}`);
  }
}
```

</div>

</div>

### 6.3 Real-time Price Feed

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { FeedClient } from '[PACKAGE]';

async function setupPriceFeed() {
  const feedClient = new FeedClient({
    wsUrl: '[WS_URL]'
  });
  
  // Register callback for specific pair
  feedClient.registerPriceFeedCallback(
    'ETH/USD',
    (priceData) => {
      console.log('ETH Price:', priceData.price);
    }
  );
  
  // Start listening
  await feedClient.listen();
}
```

</div>

</div>

### 6.4 Swap Tokens

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
async function swapExample() {
  const swapParams = {
    fromTokenAddress: '[TOKEN_A]',
    toTokenAddress: '[TOKEN_B]',
    fromAmount: parseUnits('100', 18),
    slippage: 100 // 1%
  };
  
  const tx = await sdk.orders.swap(swapParams);
  return tx;
}
```

</div>

</div>

------------------------------------------------------------------------

## 7. Integration Guides

### 7.1 Web3 Wallet Integration

#### Using wagmi

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { useWalletClient } from 'wagmi';

function App() {
  const { data: walletClient } = useWalletClient();
  
  const sdk = new SDK({
    chainId: 42161,
    rpcUrl: '[RPC_URL]',
    walletClient
  });
}
```

</div>

</div>

#### Using ethers.js

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { ethers } from 'ethers';

const provider = new ethers.providers.JsonRpcProvider('[RPC_URL]');
const signer = provider.getSigner();

// Convert to viem client if needed
```

</div>

</div>

### 7.2 Custom RPC Provider

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { createPublicClient, createWalletClient, http } from 'viem';
import { arbitrum } from 'viem/chains';

const publicClient = createPublicClient({
  chain: arbitrum,
  transport: http('[CUSTOM_RPC]'),
  batch: {
    multicall: true
  }
});

const sdk = new SDK({
  chainId: arbitrum.id,
  publicClient
});
```

</div>

</div>

### 7.3 Transaction Signing

#### Local Signer

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { privateKeyToAccount } from 'viem/accounts';

const account = privateKeyToAccount('[PRIVATE_KEY]');
sdk.setSigner(account);
```

</div>

</div>

#### AWS KMS Integration (if supported)

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
sdk.setKmsSigner({
  keyId: '[KMS_KEY_ID]',
  region: 'us-east-1'
});
```

</div>

</div>

------------------------------------------------------------------------

## 8. Smart Contracts

### 8.1 Contract Addresses

#### Mainnet

<div class="table-wrap">

|                 |             |
|-----------------|-------------|
| Contract        | Address     |
| Router          | `[ADDRESS]` |
| OrderBook       | `[ADDRESS]` |
| PositionManager | `[ADDRESS]` |

</div>

#### Testnet

<div class="table-wrap">

|                 |             |
|-----------------|-------------|
| Contract        | Address     |
| Router          | `[ADDRESS]` |
| OrderBook       | `[ADDRESS]` |
| PositionManager | `[ADDRESS]` |

</div>

### 8.2 Contract Interfaces

#### Key Methods

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
interface IRouter {
    function createOrder(
        address market,
        uint256 size,
        address collateral,
        bool isLong
    ) external returns (bytes32 orderId);
    
    function cancelOrder(bytes32 orderId) external;
}
```

</div>

</div>

### 8.3 Direct Contract Interaction

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { getContract } from 'viem';

const contract = getContract({
  address: '[CONTRACT_ADDRESS]',
  abi: RouterABI,
  publicClient,
  walletClient
});

const tx = await contract.write.createOrder([
  marketAddress,
  size,
  collateralAddress,
  isLong
]);
```

</div>

</div>

------------------------------------------------------------------------

## 9. Advanced Topics

### 9.1 Gas Optimization

#### Batch Operations

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Execute multiple operations in single transaction
await sdk.batch([
  sdk.orders.approve('[TOKEN]', amount),
  sdk.orders.createOrder(params)
]);
```

</div>

</div>

#### Gas Estimation

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const gasEstimate = await sdk.utils.estimateGas({
  operation: 'createOrder',
  params: orderParams
});
```

</div>

</div>

### 9.2 Price Impact Calculation

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const impact = await sdk.utils.calculatePriceImpact({
  marketAddress: '[MARKET]',
  size: parseUnits('10000', 6),
  isIncrease: true,
  isLong: true
});

console.log(`Price impact: ${impact}%`);
```

</div>

</div>

### 9.3 Custom Token Configuration

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  tokens: {
    '[TOKEN_ADDRESS]': {
      symbol: 'CUSTOM',
      decimals: 18,
      name: 'Custom Token'
    }
  }
});
```

</div>

</div>

### 9.4 Market Filtering

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  markets: {
    '[MARKET_ADDRESS]': {
      isListed: false // Exclude from queries
    }
  }
});
```

</div>

</div>

### 9.5 Event Listening

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Watch for order execution
const unwatch = publicClient.watchContractEvent({
  address: '[CONTRACT_ADDRESS]',
  abi: OrderBookABI,
  eventName: 'OrderExecuted',
  onLogs: (logs) => {
    console.log('Order executed:', logs);
  }
});
```

</div>

</div>

------------------------------------------------------------------------

## 10. Data Indexing

### 10.1 Subgraph Queries (if available)

#### Endpoint

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
POST [SUBGRAPH_URL]
```

</div>

</div>

#### Query Historical Data

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
query {
  trades(
    first: 100,
    where: { user: "[ADDRESS]" },
    orderBy: timestamp,
    orderDirection: desc
  ) {
    id
    market
    size
    price
    timestamp
  }
}
```

</div>

</div>

### 10.2 Subsquid Integration (if available)

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  subsquidUrl: '[SUBSQUID_URL]'
});

const historicalData = await sdk.data.queryHistorical({
  entity: 'positions',
  filters: {
    user: '[ADDRESS]',
    market: '[MARKET]'
  }
});
```

</div>

</div>

------------------------------------------------------------------------

## 11. Testing

### 11.1 Unit Testing

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
import { describe, it, expect } from 'vitest';
import { SDK } from '[PACKAGE]';

describe('SDK Integration', () => {
  it('should initialize correctly', () => {
    const sdk = new SDK({
      chainId: 42161,
      rpcUrl: '[RPC_URL]'
    });
    
    expect(sdk).toBeDefined();
  });
  
  it('should fetch markets', async () => {
    const markets = await sdk.markets.getMarkets();
    expect(markets.length).toBeGreaterThan(0);
  });
});
```

</div>

</div>

### 11.2 Testnet Setup

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const testnetSDK = new SDK({
  chainId: 421614, // Arbitrum Sepolia
  rpcUrl: '[TESTNET_RPC]',
  oracleUrl: '[TESTNET_ORACLE]'
});
```

</div>

</div>

### 11.3 Mock Data for Testing

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Mock price feed for testing
const mockFeedClient = {
  getPrice: async (pair: string) => ({
    price: '2000.00',
    timestamp: Date.now()
  })
};
```

</div>

</div>

------------------------------------------------------------------------

## 12. Best Practices

### 12.1 Error Handling

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
try {
  const tx = await sdk.orders.createOrder(params);
  await tx.wait();
} catch (error) {
  if (error.code === 'INSUFFICIENT_FUNDS') {
    // Handle insufficient balance
  } else if (error.code === 'USER_REJECTED') {
    // Handle user rejection
  } else {
    // Generic error handling
    console.error('Transaction failed:', error);
  }
}
```

</div>

</div>

### 12.2 Rate Limiting

- Implement exponential backoff for failed requests

- Cache frequently accessed data

- Use batch queries when possible

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Example: Simple retry with backoff
async function retryWithBackoff<T>(
  fn: () => Promise<T>,
  maxRetries = 3
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      if (i === maxRetries - 1) throw error;
      await new Promise(resolve => 
        setTimeout(resolve, Math.pow(2, i) * 1000)
      );
    }
  }
  throw new Error('Max retries exceeded');
}
```

</div>

</div>

### 12.3 Security Considerations

- Never expose private keys in client-side code

- Validate all user inputs

- Use secure RPC endpoints (HTTPS)

- Implement proper transaction confirmation logic

- Set appropriate slippage limits

### 12.4 Performance Optimization

- Reuse SDK instances

- Implement pagination for large datasets

- Use WebSocket connections for real-time data

- Cache static data (contract addresses, token info)

------------------------------------------------------------------------

## 13. Troubleshooting

### 13.1 Common Issues

#### Issue: Transaction Reverts

**Cause**: Insufficient allowance, slippage too low, or market conditions changed

**Solution**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Check and set allowance
const allowance = await sdk.tokens.getAllowance('[TOKEN]');
if (allowance < amount) {
  await sdk.tokens.approve('[TOKEN]', amount);
}

// Increase slippage tolerance
const params = { ...orderParams, slippage: 100 }; // 1%
```

</div>

</div>

#### Issue: RPC Connection Failures

**Cause**: Network issues or rate limiting

**Solution**: Use fallback RPC endpoints

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const rpcUrls = ['[PRIMARY_RPC]', '[FALLBACK_RPC]'];
// Implement failover logic
```

</div>

</div>

#### Issue: Price Feed Delays

**Cause**: WebSocket connection issues

**Solution**: Implement reconnection logic

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
feedClient.on('error', async (error) => {
  console.error('Feed error:', error);
  await feedClient.reconnect();
});
```

</div>

</div>

### 13.2 Debug Mode

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  debug: true // Enable verbose logging
});
```

</div>

</div>

### 13.3 Network Status Check

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
async function checkSystemStatus() {
  try {
    const response = await fetch('[BASE_URL]/ping');
    const status = await response.json();
    console.log('System status:', status);
  } catch (error) {
    console.error('System unavailable:', error);
  }
}
```

</div>

</div>

------------------------------------------------------------------------

## 14. Migration Guides

### 14.1 Upgrading from v1.x to v2.x

Key changes:

- New initialization pattern

- Updated method signatures

- Breaking changes in response formats

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// v1.x (deprecated)
const sdk = new SDK('[RPC_URL]', '[ORACLE_URL]');

// v2.x (current)
const sdk = new SDK({
  chainId: 42161,
  rpcUrl: '[RPC_URL]',
  oracleUrl: '[ORACLE_URL]'
});
```

</div>

</div>

### 14.2 Migration Checklist

- \[ \] Update package version

- \[ \] Review breaking changes in changelog

- \[ \] Update initialization code

- \[ \] Update method calls to new signatures

- \[ \] Test all critical paths

- \[ \] Update error handling

------------------------------------------------------------------------

## 15. API Rate Limits

### 15.1 REST API Limits

<div class="table-wrap">

|               |               |             |
|---------------|---------------|-------------|
| Endpoint Type | Rate Limit    | Time Window |
| Public        | 100 requests  | 1 minute    |
| Authenticated | 1000 requests | 1 minute    |
| WebSocket     | 50 messages   | 1 second    |

</div>

### 15.2 Handling Rate Limits

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Implement request queuing
class RateLimitedClient {
  private queue: Array<() => Promise<any>> = [];
  private processing = false;
  
  async request(fn: () => Promise<any>) {
    this.queue.push(fn);
    if (!this.processing) {
      await this.processQueue();
    }
  }
  
  private async processQueue() {
    this.processing = true;
    while (this.queue.length > 0) {
      const fn = this.queue.shift()!;
      await fn();
      await new Promise(resolve => setTimeout(resolve, 100));
    }
    this.processing = false;
  }
}
```

</div>

</div>

------------------------------------------------------------------------

## 16. Support & Resources

### 16.1 Documentation Links

- Technical Documentation: \[URL\]

- API Reference: \[URL\]

- Contract Addresses: \[URL\]

- GitHub Repository: \[URL\]

### 16.2 Community Channels

- Discord: \[INVITE_LINK\]

- Telegram: \[LINK\]

- Forum: \[URL\]

- Twitter/X: \[HANDLE\]

### 16.3 Developer Support

- Email: dev@\[DOMAIN\]

- GitHub Issues: \[REPO_URL\]/issues

- Technical Announcements: \[CHANNEL\]

### 16.4 Updates & Changelog

Subscribe to technical announcements for:

- API changes and deprecations

- New feature releases

- Contract upgrades

- Network maintenance

------------------------------------------------------------------------

## 17. FAQs

### Q: What networks are supported?

A: Currently supported: \[LIST_NETWORKS\]

### Q: How do I get testnet tokens?

A: Use the following faucets:

- 

### Q: What's the minimum order size?

A: Minimum order sizes vary by market. Check market parameters via API.

### Q: How are fees calculated?

A: Fees include:

- Opening fee: \[FORMULA\]

- Closing fee: \[FORMULA\]

- Borrowing fee: \[FORMULA\]

### Q: Can I use this in production?

A: Yes, but ensure proper testing on testnet first and implement robust error handling.

------------------------------------------------------------------------

## 18. Glossary

<div class="table-wrap">

|            |                                                            |
|------------|------------------------------------------------------------|
| **Term**   | **Definition**                                             |
| Market     | Trading pair with associated liquidity pool                |
| Position   | Open trade with defined entry price and size               |
| Collateral | Asset deposited to secure a leveraged position             |
| Slippage   | Acceptable price deviation during order execution          |
| Oracle     | External price feed provider                               |
| Gas Fee    | Network transaction cost                                   |
| Leverage   | Multiplier applied to position size relative to collateral |

</div>

------------------------------------------------------------------------

## 19. Changelog

### Version 2.0.0 (Latest)

- Added support for \[FEATURE\]

- Improved performance for \[OPERATION\]

- Breaking: Changed \[METHOD\] signature

- Deprecated: \[OLD_METHOD\] (use \[NEW_METHOD\])

### Version 1.5.0

- Added \[FEATURE\]

- Fixed \[BUG\]

- Updated \[DEPENDENCY\]

------------------------------------------------------------------------

## 20. Legal & License

### 20.1 License

\[LICENSE_TYPE\] - See LICENSE file for details

### 20.2 Disclaimer

This SDK is provided "as is" without warranties. Users are responsible for:

- Testing thoroughly before production use

- Managing private keys securely

- Understanding associated risks

- Compliance with local regulations

### 20.3 Audit Reports

Smart contract audits available at: \[AUDIT_LINKS\]

</div>
