# HertzFlow Release Notes

<div class="Section1">

> 对外发版记录。需review。

# Release History

<div class="table-wrap">

|  |  |  |  |
|----|----|----|----|
| Version | Date | Type | Status |
| <a href="https://claude.ai/chat/RELEASE_v1.0.1.md" class="external-link" rel="nofollow">v1.0.1</a> | 2026-02-13 | Minor Release | Published |
| <a href="https://claude.ai/chat/RELEASE_v1.0.0.md" class="external-link" rel="nofollow">v1.0.0</a> | 2026-02-10 | Major Release | Published |

</div>

# Release v1.0.1

**Release Date:** February 13, 2026

## Overview

This release addresses issues identified after the v1.0.0 launch, including fixes for take-profit and stop-loss calculations, tooltip displays, mobile interface issues, and 24-hour change data during market closure periods. A network monitoring indicator has also been added to the bottom navigation.

## Bug Fixes

### Trading

- Fixed take-profit and stop-loss calculations to properly include fees (<a href="https://linear.app/hertzflow/issue/HZFL-338" class="external-link" rel="nofollow">HZFL-338</a>)

- Added tooltips for TP/SL calculations showing fee breakdown

- Resolved limit order execution failures (<a href="https://linear.app/hertzflow/issue/HZFL-329" class="external-link" rel="nofollow">HZFL-329</a>)

- Fixed issue allowing users to close positions on markets not yet opened on mobile (<a href="https://linear.app/hertzflow/issue/HZFL-328" class="external-link" rel="nofollow">HZFL-328</a>)

### Data Display

- Corrected 24-hour change calculation errors (<a href="https://linear.app/hertzflow/issue/HZFL-339" class="external-link" rel="nofollow">HZFL-339</a>)

- Fixed missing 24-hour change data for US stock indices (<a href="https://linear.app/hertzflow/issue/HZFL-330" class="external-link" rel="nofollow">HZFL-330</a>)

- Resolved token border background color display issues (<a href="https://linear.app/hertzflow/issue/HZFL-340" class="external-link" rel="nofollow">HZFL-340</a>)

### Charts

- Fixed display issues for hourly market charts on specific markets (<a href="https://linear.app/hertzflow/issue/HZFL-336" class="external-link" rel="nofollow">HZFL-336</a>)

- Corrected display issues when switching between K-line daily levels (<a href="https://linear.app/hertzflow/issue/HZFL-327" class="external-link" rel="nofollow">HZFL-327</a>)

### UI/UX

- Adjusted spacing in Market List display (<a href="https://linear.app/hertzflow/issue/HZFL-337" class="external-link" rel="nofollow">HZFL-337</a>)

- Fixed toolbar overlapping order information on mobile devices (<a href="https://linear.app/hertzflow/issue/HZFL-325" class="external-link" rel="nofollow">HZFL-325</a>)

### Search

- Fixed Pool List search functionality where "/usd" was incorrectly participating in symbol matching (<a href="https://linear.app/hertzflow/issue/HZFL-331" class="external-link" rel="nofollow">HZFL-331</a>)

## Enhancements

- Added network monitoring indicator to bottom navigation bar for improved connectivity awareness

## Known Issues

The following items are currently in development and will be addressed in v1.0.2:

**Performance Optimizations**

- Component optimization and duplicate code removal (<a href="https://linear.app/hertzflow/issue/HZFL-335" class="external-link" rel="nofollow">HZFL-335</a>)

- First screen resource loading optimization with dynamic imports (<a href="https://linear.app/hertzflow/issue/HZFL-334" class="external-link" rel="nofollow">HZFL-334</a>)

- Third-party package import optimization to avoid full imports (<a href="https://linear.app/hertzflow/issue/HZFL-333" class="external-link" rel="nofollow">HZFL-333</a>)

- Font format optimization using woff2 compression (<a href="https://linear.app/hertzflow/issue/HZFL-332" class="external-link" rel="nofollow">HZFL-332</a>)

**Features**

- Favorites functionality for Trade and Pool pages (<a href="https://linear.app/hertzflow/issue/HZFL-326" class="external-link" rel="nofollow">HZFL-326</a>)

## Technical Details

**Changes**

- 15 files modified

- 347 lines added

- 189 lines removed

- Net change: +158 lines

**Testing**

- Test coverage: 96%

- All regression tests passing

- Manual testing completed on desktop and mobile

## Compatibility

- BNB Chain Testnet (97)

- Browsers: Chrome 90+, Safari 14+, Firefox 88+, Edge 90+

- Mobile: iOS Safari 14+, Android Chrome 90+

## Upgrade Instructions

This update is deployed automatically. Users should refresh their browser to receive the latest version. No action is required for existing positions, orders, or liquidity.

For optimal performance, users may clear browser cache if experiencing issues.

## Breaking Changes

None. All changes are backward compatible.

## What's Next

**Version 1.0.2**

Planned improvements:

- Performance optimizations (4 items)

- Favorites functionality

- Additional bug fixes based on user feedback

## Build Information

**Version:** v1.0.1\
**Network:** BNB Chain (Testnet: 97)\
**Deployment Date:** February 13, 2026

# Release v1.0.0

**Release Date:** February 10, 2026

## Overview

This is the initial production release of HertzFlow, a perpetual futures trading platform on BNB Chain. The platform includes three core modules: Pools for liquidity provision, Trade for perpetual contract trading, and Vaults for automated multi-pool strategies.

## New Features

### Pools

**Liquidity Management**

- Deposit and withdraw functionality with approve flow and capacity validation

- Real-time risk precheck before transactions

- Support for 30+ market liquidity pools across Crypto, Forex, Equities, and Commodities

**Analytics**

- Historical TVL and APR charts with 30d/90d/180d timeframes

- Pool activity tracking with cursor pagination

- Remaining capacity display with real-time updates

**Discovery**

- Filter by 7 asset categories

- Search by symbol

- Sort by TVL, APY, and supply

### Trade

**Take Profit and Stop Loss**

- Dual input system supporting both price and PnL percentage

- Automatic boundary validation with +2500% and -80% caps

- Auto-fill from existing orders with same market and direction

- Keeper-based automatic execution

- Dynamic recalculation when collateral changes

**Position Management**

- Keep Leverage toggle for proportional vs non-proportional position reduction

- Optimized receive calculation including all fees and PnL

- Real-time liquidation price updates

- Collateral editing in USDC with 10 USDC minimum residual requirement

**Order Management**

- Market and limit order support

- Type filtering for All/Limit/TP/SL orders

- Liq Price After Execution display

- Invalid price alerts

**Fee Collection**

- View accumulated Funding Fee and Price Impact

- Individual or batch claim via multicall aggregation

- Complete claim transaction history

**Market Interface**

- Top 20 market carousel

- Filter by 7 categories plus "Newly Listed"

- Search by ticker symbol

- Sort by Price, 24h Change, Volume, Open Interest, and Liquidity

- Net Rate breakdown for 1h/8h/24h/365d periods

- 24h High/Low prices

- Separate Long/Short Open Interest and Liquidity display

- Market status with Closed tag and countdown for RWA assets

**Charts and Analysis**

- Trade markers on price chart showing entry/exit points

- Position PnL tracking

- TradingView integration

**Global Settings**

- Unified slippage control for market orders

- Standardized 10 USDC minimum collateral across all markets

- Portfolio view with balance in USDC and unrealized PnL with percentage

### Vaults

**Auto-distribution Engine**

- Intelligent capital allocation by TVL Cap with large to small distribution

- 10% safety buffer for capacity management

- Multi-pool deposit and withdraw in single transaction

**Discovery**

- Auto-sorted vault cards by RankKey formula: 0.6 × APY + 0.4 × TVL

- Visual display of logo, curator name, Net APY, and top 3 market exposures

- Real-time capacity aggregation across all pools

**Analytics**

- TVL, Net APR, and Market Exposure charts with 30d/90d/180d timeframes

- Net APY calculation: Fee APY × (1 - Performance Fee Rate)

- Total fees and performance fee breakdown

- Market exposure list sorted by capacity

- Vault and user liquidity history

### Universal Features

**Data Presentation**

- Unified precision for USD display: 2 decimal places with k/m/b suffixes

- Consistent percentage formatting with sign and color coding

- Price precision table for all 30 markets

**User Experience**

- Enhanced toast notifications with Pending/Success/Failed/Timeout states

- Real-time allowance check with smooth approve flow

- Detailed error messages and action guidance

## Technical Specifications

**Performance**

- API response time under 500ms (P95)

- Keeper execution under 10s for orders, under 5s for liquidations

- Chart rendering optimized for 90-day historical data

**Quality Assurance**

- Over 200 comprehensive functional test cases

- 50+ calculation accuracy tests with error margin under 0.01%

- Stress tested with 100 concurrent users

**Compatibility**

- BNB Chain Testnet

- 30+ markets: Crypto, Forex, Equities, Commodities

- Desktop, tablet, and mobile responsive design

- Browser support: Chrome, Safari, Firefox, Edge (latest versions)

## Security

**High-Risk Features**

The following features involve direct contract interactions and have undergone extensive security review:

1.  Take Profit and Stop Loss with +2500%/-80% boundary validation

2.  Keep Leverage non-proportional position reduction

3.  Funding Fee and Price Impact multicall claiming

4.  Vault and Pool deposit/withdraw with contract-aligned risk controls

All smart contracts have been audited and tested extensively before deployment.

## Breaking Changes

None. This is the initial production release.

## Bug Fixes

- Fixed TP/SL calculation edge cases

- Improved order execution reliability during network congestion

- Enhanced error handling for failed transactions

- Optimized chart rendering performance

## Documentation

- User Guide for Pools, Trade, and Vaults

- Take Profit and Stop Loss strategy guide

- Vault strategy documentation

- Complete API reference

- Trading best practices and risk management guide

## What's Next

Planned for upcoming releases:

- Advanced charting with technical indicators

- Portfolio analytics and PnL reports

- Hyper Leverage Mode

- Additional market listings

- Mobile application

## Build Information

**Version:** v1.0.0\
**Network:** BNB Smart Chain (Testnet: 97)\
**Deployment Date:** February 10, 2026

------------------------------------------------------------------------

**Questions?** Join our <a href="https://discord.com/invite/sBQqf2H7ts" class="external-link" rel="nofollow">Discord</a> or contact support@hertzflow.xyz

</div>
