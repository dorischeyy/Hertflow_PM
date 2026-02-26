# swap - error mapping

<div class="Section1">

<div class="table-wrap">

|  |  |  |
|----|----|----|
| **合约/sdk报错关键字段** | 问题 | **报错** |
| `SlippageTooSmall`, `slippage`, `price impact` | 滑点/price impact | Slippage tolerance is too low. Please increase your slippage and try again. |
| `InsufficientLiquidity`, `liquidity` | 流动性不足 | Not enough liquidity to complete this trade. Try reducing your trade size. |
| `MoveAbort`, `execution reverted`, `revert` | revert | Transaction execution failed. Please try again or adjust your parameters. |
| `Invalid return values`, `null price` | 返还为空 | Failed to fetch a valid swap quote. Please adjust your amount or try again later. |
| `BalanceTooLow`, `insufficient funds` | 可用资金不足 | Your balance is too low to perform this action. Please add more funds. |

</div>

</div>
