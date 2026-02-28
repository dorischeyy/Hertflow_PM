# GMX V2 精度说明

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270879363 {padding: 0px;}
div.rbtoc1772270879363 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270879363 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270879363">

- [1. Token 数量](#GMXV2精度说明-1.Token数量)
- [2. USD 价值](#GMXV2精度说明-2.USD价值)
- [3. Token 价格](#GMXV2精度说明-3.Token价格)
- [4. Factor](#GMXV2精度说明-4.Factor)
  - [4.1 常规因子](#GMXV2精度说明-4.1常规因子)
  - [4.2 速率 / per-size 项](#GMXV2精度说明-4.2速率/per-size项)

</div>

## **1. Token 数量**

精度和 token 本身的精度一致。比如 USDC 的 Decimal 是 6，那么 GMX 中 1 USDC 会表示为 10^6 = 1,000,000；

WETH 的 Decimal 是 18，所以 1 WETH 会表示为 1,000,000,000,000,000,000。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 / Key | 精度 | 示例 |
| poolAmount, MarketPoolValueInfo.longTokenAmount, MarketPoolValueInfo.shortTokenAmount | ERC20 最小单位（USDC=1e6，USDT=1e6，DAI=1e18，WETH=1e18，WBTC=1e8，GMX=1e18，ARB=1e18） | `100 USDC → 100 × 1e6 = 1e8`；`2 WETH → 2 × 1e18 = 2e18` |
| maxPoolAmount | ERC20 最小单位（USDC=1e6，WETH=1e18，GMX=1e18 等） | `maxPoolAmount = 5,000,000 USDC` 存成 `5e6 × 1e6 = 5e12`；若为单币市场则再除 2 → `2.5e12` |
| swapImpactPoolAmount | 抵押物 Token 最小单位（与抵押物 Token decimals 相同：USDC=1e6，DAI=1e18，WETH=1e18 等） | `+50 USD` 的正向影响在 USDC (1e24 价格精度) 上换算成 `50 × 1e30 / 1e24 = 5e7`最小单位 (=0.05 USDC) |
| positionImpactPoolAmount / lentPositionImpactPoolAmount | 指数 Token 最小单位（WETH=1e18，WBTC=1e8，ARB=1e18 等） | `增加 0.1 WETH` → `0.1 × 1e18 = 1e17`单位；`借出 0.05 WETH` → `-5e16`；`增加 0.2 WBTC` → `0.2 × 1e8 = 2e7` |
| claimableCollateralAmount / claimedCollateralAmount | 抵押物 Token 最小单位（USDC=1e6，DAI=1e18，WETH=1e18） | `用户可领取 250 USDC` → `250 × 1e6 = 2.5e8`；`已领取 1.5 WETH` → `1.5 × 1e18 = 1.5e18` |
| claimableFundingAmount | 抵押物 Token 最小单位（DAI=1e18，USDC=1e6 等） | `资金费 12 DAI (18 位)` → 写入 `12 × 1e18 = 1.2e19`，领取时按该值扣减 |
| openInterestInTokens | 指数 Token 最小单位（WETH=1e18，WBTC=1e8） | `多头 3 WETH + 空头 1 WETH`（双币市场）→ `4 × 1e18 = 4e18`；若指数 Token 是 WBTC，`1 WBTC`就是 `1 × 1e8 = 1e8` |
| virtualInventoryForSwaps | ERC20 最小单位（GMX=1e18，USDC=1e6，ARB=1e18） | `库存 +75 GMX (18 位)` → `75 × 1e18 = 7.5e19`；库存变成 0 时不会出现负值 |
| virtualInventoryForPositions | 指数 Token 最小单位（可为负；WETH=1e18，WBTC=1e8） | `-0.3 WBTC`（8 位）→ `-0.3 × 1e8 = -3e7`；`+2 WBTC`→ `2e8`；`+1.25 WETH` → `1.25 × 1e18 = 1.25e18` |
| collateralSum | 抵押物 Token 最小单位（USDC=1e6，DAI=1e18，GMX=1e18） | `USDC 抵押 400 + 600` → `1000 × 1e6 = 1e9`；单币市场折半成 `5e8` |
| claimableFeeAmount / claimableUiFeeAmount / affiliateRewardAmount | ERC20 最小单位（GMX=1e18，WETH=1e18，USDC=1e6） | `claimableFeeAmount = 250 GMX` → `250 × 1e18 = 2.5e20`；`affiliateReward = 80 WETH` → `8e19` |
| totalPendingImpactAmount | 指数 Token 最小单位（可正可负；WETH=1e18，WBTC=1e8） | `待结算 +0.02 WETH` → `0.02 × 1e18 = 2e16`；`待结算 -0.05 WETH` → `-5e16`；`待结算 +0.1 WBTC` → `0.1 × 1e8 = 1e7` |
| impactAmount (swap/position) | ERC20 最小单位（按成交 Token：WETH=1e18，USDC=1e6，GMX=1e18） | `-120 USD` 的价格影响在 WETH (价格精度 1e12) 上换算为 `-120 × 1e30 / 1e12 = -1.2e20` (≈-0.12 WETH) |
| initialCollateralDeltaAmount / inputTokenAmount | ERC20 最小单位（跟 `initialCollateralToken.decimals()`相同） | `Order.Numbers.initialCollateralDeltaAmount`直接记录原生 Token 数；增仓=用户打入抵押，减仓=提取抵押，Swap=待兑换 Token。 |
| minOutputAmount | Swap / Withdrawal 时为目标 Token 最小单位；Decrease Order 校验时转成 USD 1e30 | `Order.Numbers.minOutputAmount`：Keeper 在减仓场景把预期领取值换算成 USD 校验，其余场景直接与 Token 数比较。 |
| executionFee | 原生 WNT（Wrapped Native）最小单位，EVM 主网 1e18 | `Order.Numbers.executionFee` 与 `msg.value`一致，由 Keeper 领取执行费。 |
| sizeInTokens / size_delta_in_tokens | 指数 Token 最小单位 | 例如增仓 300 USDC → `300 × 1e6 = 3e8`；提取 0.5 WETH → `0.5 × 1e18 = 5e17` |

</div>

------------------------------------------------------------------------

## 2. USD 价值

GMX 中，所有对 USD 的数值精度是 30，也就是 1 USD 会表示为 10^30。

例如: `BorrowingFeeUsd` = 10,871,208,629,470,217,267,549,284,842，则可知实际数量应该是

0.010,871,208,629,470,217,267,549,284,842

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 / Key | 精度 | 示例 |
| openInterest (long/short/total) | `1e30`（1 USD = 10^30） | `15,000 USD` 的多头敞口 → `1.5e4 × 1e30 = 1.5e34`；单币市场除 2 得 `7.5e33` |
| maxOpenInterest | `1e30` | `maxOpenInterest = 50M USD` → `5e7 × 1e30 = 5e37` |
| poolUsdWithoutPnl | `1e30` | `poolAmount = 2,000 WETH`，`price = 1,800 USD` → `2,000 × 1,800 × 1e30 = 3.6e36` |
| MarketPoolValueInfo.longTokenUsd / shortTokenUsd / poolValue | `1e30` | `longTokenUsd = 8M USD` → `8e6 × 1e30 = 8e36`；`poolValue = 20M USD`→ `2e37` |
| totalBorrowingFees / totalBorrowing | `1e30` | `positionSize = 100k USD`、`cumulativeBorrowingFactor = 0.02 × 1e30 = 2e28` → 费用 `100k × 0.02 × 1e30 = 2e33` |
| longPnl / shortPnl / netPnl | `1e30` | `long PnL = +1,200 USD` → `1.2e3 × 1e30 = 1.2e33`；`netPnl = -800 USD`→ `-8e32` |
| impactPoolUsd / lentImpactPoolUsd | `1e30` | `impactPoolUsd = 3,500 USD` → `3.5e3 × 1e30 = 3.5e33` |
| maxPoolUsdForDeposit | `1e30` | `阈值 = 10M USD` → `1e7 × 1e30 = 1e37`；若当前入金 2M USD → `2e36` |
| reservedUsd / maxReservedUsd | `1e30` | `reservedUsd = 4M USD` → `4e6 × 1e30 = 4e36`；`maxReservedUsd = 10M USD` → `1e37` |
| maxLendableUsd | `1e30` | `poolValue = 25M USD`、`maxLendableImpactFactor = 0.1 × 1e30` → `2.5e36` |
| priceImpactUsd / cappedDiffUsd | `1e30` | `priceImpactUsd = -900 USD` → `-9e32`；超额部分 `cappedDiffUsd = 200 USD` → `2e32` |
| fundingUsd / fundingUsdForLongCollateral / fundingUsdForShortCollateral | `1e30` | `duration=3600s`、`fundingFactorPerSecond=2e25 (≈2e-5)`、`openInterest=5M USD` → `fundingUsd ≈ 3600 × 2e25 × 5e6 ≈ 3.6e35` |
| usdValue / totalUsd | `1e30` | `usdValue = 12,345 USD` → `1.2345e4 × 1e30 = 1.2345e34`；`totalUsd = 50M USD` → `5e37` |
| sizeDeltaUsd / size_delta / inputUsd | `1e30` | 调整 10,000 USD 仓位 → `1e4 × 1e30 = 1e34` |

</div>

------------------------------------------------------------------------

## 3. Token 价格

根据公式:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
price = (usd_value) / amount

或者这样理解: price * amount = value 再倒推
```

</div>

</div>

可以看到价格精度为 10^30 / 10^token_decimal

即价格精度 = 30 - token_decimal

比如对于 USDC，精度为 30 - 6 = 24，阅读合约时需要除以 10^24 得到人类可读的价格。

对于 WETH，精度为 30 - 18 = 12。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 / Key | 精度 | 示例 |
| Price.Props.min / max | USD 精度 1e30 ÷ Token 最小单位 | USDC (`dec=6`) → 价格精度 `1e30 / 1e6 = 1e24`，`1.002 USD` 记为 `1.002 × 1e24`; WETH (`dec=18`) → 精度 `1e30 / 1e18 = 1e12`，`1800 USD` 记为 `1.8e3 × 1e12 = 1.8e15` |
| indexTokenPrice / longTokenPrice / shortTokenPrice | USD 精度 1e30 ÷ Token 最小单位 | `longToken=WETH` → `price = 2000 USD` 记成 `2e3 × 1e12 = 2e15`; `shortToken=USDC`→ `price = 1 USD` 记成 `1 × 1e24 = 1e24` |
| tokenPrice（函数参数） | USD 精度 1e30 ÷ Token 最小单位 | `poolAmount = 5000 GMX`、`tokenPrice = 35 USD` → `35 × (1e30 / 1e18) = 35 × 1e12 = 3.5e13` |
| marketTokenPrice | `1e18` (WEI) | `poolValue = 80M USD` (`8e7 × 1e30 = 8e37`)、`supply = 10M GM` → `price ≈ 8e37 / 1e7 = 8e30`，再转成 WEI → `8e30 × 1e18 / 1e30 = 8e18` |
| Precision.floatToWei / weiToFloat | `1e30 ↔ 1e18` | `floatToWei(1,250 USD)` → `1.25e3 × 1e18 / 1e30 = 1.25e-9`（再乘 supply 得整数）；`weiToFloat(5e21)` → `5e21 × 1e30 / 1e18 = 5e33` (≈`5,000 USD`) |
| triggerPrice / acceptablePrice | USD 精度 1e30 ÷ Token 最小单位 | 触发价 1,900 USD（ETH）→ `1.9e3 × 1e12 = 1.9e15`；USDC 限价 1.002 USD → `1.002 × 1e24` |

</div>

## 4. Factor

GMX 把所有“因子类”配置分成两类：一类是直接乘在 USD/Token 数值上的常数型比例（典型精度就是 \`1e30\`），例如抵押率、价格影响因子、UI 手续费等；另一类是带“每秒 / 每 size”语义的速率型或 per-size 因子，需要再乘以时间或 size 才能回到 \`1e30\` 或 Token 最小单位。

### 4.1 常规因子

常规因子就是“直接乘在 1e30 USD 或 Token 数上的比例”，没有额外除以秒或 size，合约里把它们当作纯 \`1e30\` 浮点数（或其平方根）来比较与相乘。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 / Key | 精度 | 示例 |
| Precision.FLOAT_PRECISION / FLOAT_PRECISION_SQRT | `1e30 / 1e15` | `1 USD` 记成 `1 × 1e30 = 1e30`；`FLOAT_PRECISION_SQRT`代表 `sqrt(1e30)=1e15`，平方后回到 1e30 |
| borrowingFeePoolFactor | `1e30` | 费率 `0.25` → 写成 `0.25 × 1e30 = 2.5e29`；与 `10M USD`pool 相乘得 `2.5e29 × 1e37 / 1e30 = 2.5e36` |
| swapImpactFactor (正/负) | `1e30` | `swapImpactFactorPositive = 5e-5` → 存成 `5e-5 × 1e30 = 5e25`；若负向为 `1e-4` → `1e26` |
| positionImpactFactor (正/负) | `1e30` | `positionImpactFactorNegative = 0.001` → `1e-3 × 1e30 = 1e27` |
| maxPositionImpactFactor (正/负) / maxPositionImpactFactorForLiquidations | `1e30` | `maxPositionImpactFactorForLiquidations = 0.02` → `2e-2 × 1e30 = 2e28` |
| reserveFactor / openInterestReserveFactor | `1e30` | `reserveFactor = 0.5` → `0.5 × 1e30 = 5e29`，与 `20M USD` 池相乘得到 `1e37` |
| maxPnlFactor / minPnlFactorAfterAdl | `1e30` | `maxPnlFactor = 0.3` → `3e-1 × 1e30 = 3e29`；`minPnlFactorAfterAdl = 0.05` → `5e28` |
| maxLendableImpactFactor | `1e30` | 因子 `0.1` → `1e29`；impact pool = `5M USD` → `0.1 × 5e6 × 1e30 = 5e35` |
| minCollateralFactor / minCollateralFactorForLiquidation / minCollateralFactorForOpenInterestMultiplier | `1e30` | `minCollateralFactor = 0.1` → `1e29`；`minCollateralFactorForLiquidation = 0.06` → `6e28` |
| thresholdForStableFunding / thresholdForDecreaseFunding | `1e30` | `thresholdForStableFunding = 0.15` → `1.5e29`；`thresholdForDecreaseFunding = 0.07` → `7e28` |
| claimableCollateralFactor / claimableReductionFactor | `1e30` | `claimableCollateralFactor = 0.2` → `2e29`；`claimableReductionFactor = 0.01` → `1e28` |
| uiFeeFactor / MAX_UI_FEE_FACTOR | `1e30` | `uiFeeFactor = 0.005` → `5e-3 × 1e30 = 5e27`；`MAX_UI_FEE_FACTOR = 0.1` → `1e29` |
| usageFactor | `1e30` | `reservedUsd=6M`、`maxReservedUsd=12M` → 用 1e30 表示即 `0.5 × 1e30 = 5e29` |
| pnlToPoolFactor | `±1e30` | `netPnl = -4M USD`、`poolValue = 20M USD` → `-0.2 × 1e30 = -2e29` |
| optimalUsageFactor / borrowingExponentFactor | `1e30` | `optimalUsageFactor = 0.7` → `7e29`；`borrowingExponentFactor = 1.3` → `1.3 × 1e30 = 1.3e30` |
| callbackGasLimit | Gas 单位 (原始整数) | 传 300,000 gas 就写入 `300000` |

</div>

### 4.2 速率 / per-size 项

这些字段本质仍是因子或 Token 数量，只是附带“每秒 / 每 size”含义。

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 字段 / Key | 精度 | 示例 |
| fundingFactorPerSecond / nextSavedFundingFactorPerSecond | `1e30 / 秒` | `fundingFactorPerSecond = 2e-6` → `2e-6 × 1e30 = 2e24 / 秒`；存的负值 `-1e-6` → `-1e24 / 秒` |
| fundingIncreaseFactorPerSecond / fundingDecreaseFactorPerSecond / minFundingFactorPerSecond / maxFundingFactorPerSecond | `1e30 / 秒` | `fundingIncreaseFactorPerSecond = 5e-7` → `5e23 / 秒`；`maxFundingFactorPerSecond = 4e-6` → `4e24 / 秒` |
| borrowingFactor / baseBorrowingFactor / aboveOptimalUsageBorrowingFactor | `1e30 / 秒` | `baseBorrowingFactor = 1e-6` → `1e24 / 秒`；`aboveOptimalUsageBorrowingFactor = 3e-6` → `3e24 / 秒` |
| borrowingFactorPerSecond | `1e30 / 秒` | `usageFactor = 0.8` (`8e29`) 与 `borrowingFactor = 2e24 / 秒` 相乘 → `1.6e54 / 秒 / 1e30 = 1.6e24 / 秒` |
| fundingFeeAmountPerSize / claimableFundingAmountPerSize | `Token 数量 / 1e-15 USD size` | `资金费 = 0.5 WETH`（18 位）分摊到 `1 USD` size → 结果 `0.5 × 1e18 / 1e15 = 5e2`，即每 `1e-15 USD` 可领取 `500`最小单位 (=5e-16 WETH) |
| positionImpactPoolDistributionRate | 指数 Token 最小单位 / 秒 | rate = `0.001 WETH/s` → `0.001 × 1e18 = 1e15`；发放 600 秒 → `6e17` (≈0.6 WETH) |

</div>

</div>
