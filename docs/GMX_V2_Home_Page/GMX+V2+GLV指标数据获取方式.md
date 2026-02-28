# GMX V2 GLV指标数据获取方式

<div class="Section1">

# 1. 指标与源码

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="197f6d70-3af5-4fc2-95e7-cef82377f605">
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<th class="confluenceTh"><p>指标</p></th>
<th class="confluenceTh"><p>主体</p></th>
<th class="confluenceTh"><p>入口源码</p></th>
<th class="confluenceTh"><p>主要方法 / Key</p></th>
<th class="confluenceTh"><p>说明</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><code>TVL_USD</code></p></td>
<td class="confluenceTd"><p>GLV Vault</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/glv/GlvUtils.sol</code></p></td>
<td class="confluenceTd"><p><code>getGlvValue</code> / <code>getGlvTokenPrice</code></p></td>
<td class="confluenceTd"><p>读取 GLV 管理的每个 GM 市场的 <code>poolValue</code>，按持仓比例折算 USD。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Supply_amount</code></p></td>
<td class="confluenceTd"><p>GLV Token</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/glv/GlvToken.sol</code></p></td>
<td class="confluenceTd"><p><code>ERC20.totalSupply()</code></p></td>
<td class="confluenceTd"><p>直接读取 GLV ERC20 的总供应。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Price</code></p></td>
<td class="confluenceTd"><p>GLV Token</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/reader/GlvReader.sol</code></p></td>
<td class="confluenceTd"><p><code>getGlvTokenPrice</code></p></td>
<td class="confluenceTd"><p>返回 <code>(price, glvValue, supply)</code>，精度 1e30。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>buyableHzV_USD / amount</code></p></td>
<td class="confluenceTd"><p>GLV + Market Cap</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/data/Keys.sol</code> + <code>GlvUtils.validateGlvMarketTokenBalance</code></p></td>
<td class="confluenceTd"><p><code>glvMaxMarketTokenBalanceUsdKey</code> / <code>glvMaxMarketTokenBalanceAmountKey</code> + 实时余额 (<code>GlvToken.tokenBalances</code>)</p></td>
<td class="confluenceTd"><p>限制每个市场可分配 TVL，需逐市场算 <code>max - current</code>。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>sellableHzV_USD / amount</code></p></td>
<td class="confluenceTd"><p>GLV Vault</p></td>
<td class="confluenceTd"><p><code>GlvUtils.glvTokenAmountToUsd</code></p></td>
<td class="confluenceTd"><p>-</p></td>
<td class="confluenceTd"><p>90% * TVL 即可赎；金额转供应量需用实时 <code>glvValue</code>/<code>glvSupply</code>。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Market Open Interest</code> / <code>Pool Reserve</code></p></td>
<td class="confluenceTd"><p>GM 市场</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/market/MarketUtils.sol</code>+ <code>contracts-v2/contracts/reader/Reader.sol</code></p></td>
<td class="confluenceTd"><p> <code>collater</code></p>
<p><code>openInterestKey</code>, <code>collatealSumKey</code>, <code>getMarketInfoList</code></p></td>
<td class="confluenceTd"><p>需要 <code>MarketPrices</code> 以 USD 展示，Long/Short 方向拆分</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Total Earned Fees_usd</code></p></td>
<td class="confluenceTd"><p>Fee 模块</p></td>
<td class="confluenceTd"><p><code>contracts-v2/contracts/fee/FeeUtils.sol</code> + <code>Keys.claimableFeeAmountKey</code></p></td>
<td class="confluenceTd"><p><code>incrementClaimableFeeAmount</code> 事件，或直接读取 <code>DataStore.getUint( claimableFeeAmountKey )</code></p></td>
<td class="confluenceTd"><p>不含未实现 PnL，支持按市场、token 聚合。</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>Fee APR_24h</code></p></td>
<td class="confluenceTd"><p>业务衍生</p></td>
<td class="confluenceTd"><p>事件 + 历史数据</p></td>
<td class="confluenceTd"><p>过去 24h fee / 当前 TVL</p></td>
<td class="confluenceTd"><p>需要事件或 Dune。</p></td>
</tr>
</tbody>
</table>

</div>

# 2. 查询方式

### 2.1 `TVL_USD`

1.  通过 `GlvReader.getGlvInfo(DataStore, glv)` 拿到 GLV Token 地址（`glv.glvToken`）以及所跟踪的市场 `marketToken` 列表。

2.  为每个市场准备价格输入：

`text`\
`indexTokenPrice = { min, max }`\
`longTokenPrice = { min, max }`\
`shortTokenPrice = { min, max }`\
\
价格可以从 GMX Infra API（参照 `scripts/helpers.ts#getApiEndpoint`）抓取。

1.  调用 `GlvReader.getGlvTokenPrice(dataStore, marketAddresses, indexPrices[], longTokenPrice, shortTokenPrice, glv, maximize=false)`，该函数内部会触发 `GlvUtils.getGlvValue`，将每个市场的 `poolValue` 乘以 GLV 的持仓权重后求和，返回的 `glvValue` 即 GLV 当前管理的 USD 总额（单位 1e30）。

2.  展示层将 `glvValue / 1e30` 即可得到 `TVL_USD`。

### 2.2 `Supply_amount`

1.  通过 `GlvReader.getGlvInfo` 返回的 `glv.glvToken` 地址实例化 `GlvToken`（`contracts-v2/contracts/glv/GlvToken.sol`）。

2.  使用标准 ERC20 接口 `totalSupply()`（或 `GlvToken.totalSupply()`）读取总提供量，默认精度为 1e18。

3.  在 UI 或 API 端计算 `Supply_amount = totalSupply / 1e18`。

### 2.3 `Price`

1.  与 TVL 相同的输入，直接调用 `GlvReader.getGlvTokenPrice(...)`。

2.  返回值 `glvTokenPrice` 为 1e30 精度的 GLV 价格，其计算过程为 `glvValue / glvSupply`。

3.  展示时将 `glvTokenPrice / 1e30` 作为单价输出，或保留 1e30 精度在链下继续计算。

### 2.4 `buyableHzV_USD / amount`

1.  逐个市场查询上限：

    1.  `capUsd = DataStore.getUint(Keys.glvMaxMarketTokenBalanceUsdKey(glv, marketToken))`

    2.  若 `capUsd == 0`，则读取 `capAmount = DataStore.getUint(Keys.glvMaxMarketTokenBalanceAmountKey(glv, marketToken))`

2.  调用 `GlvToken.tokenBalances(marketToken)`（底层由 `StrictBank` 持有），获取当前该市场中 GLV 已配置的 `marketToken`数量。

3.  借助 `MarketUtils.getPoolValueInfo` 和 `MarketUtils.marketTokenAmountToUsd` 将 `tokenBalances` 折算成 USD，即 `currentUsd`。

4.  按市场计算可新增额度 `buyableUsdPerMarket = max(0, capUsd - currentUsd)`；如果只有 `capAmount`，先转换成 USD 再比较。

5.  汇总 USD：`buyableHzV_USD = Σ buyableUsdPerMarket`。

6.  再利用 `glvTokenPrice` 将 USD 转为能铸造的 GLV 数量：`buyableHzV_amount = buyableHzV_USD / glvTokenPrice`。

7.  逻辑可参考 `GlvUtils.validateGlvMarketTokenBalance`（`contracts-v2/contracts/glv/GlvUtils.sol`）。

### 2.5 `sellableHzV_USD / amount`

1.  业务限制：允许赎回的资金为当前 TVL 的 90%，所以 `sellableHzV_USD = TVL_USD * 0.9`。

2.  赎回时按照 `GlvUtils.glvTokenAmountToUsd(glvAmount, glvValue, glvSupply)` 把想赎回的 GLV 数量转换成 USD，或使用 `glvTokenPrice` 粗略估算。

3.  反向换算赎回额度：`sellableHzV_amount = sellableHzV_USD / glvTokenPrice`。

4.  上述接口都在 `contracts-v2/contracts/glv/GlvUtils.sol` 中，结合第 2.1 节的 TVL 结果即可求得。

### 2.6 `Market Open Interest / Pool Reserve`

1.  通过 `Reader.getMarkets(DataStore, start, end)` 或 `Reader.getMarketInfoList(DataStore, marketAddresses, prices)` 枚举所有 GM 市场（入口：`contracts-v2/contracts/reader/Reader.sol`）。

    - 为每个市场构造 `Multicall` 请求，批量读取：

      1.  `openInterestKey(market, collateralToken, isLong)`

      2.  `collateralSumKey(market, collateralToken, isLong)`

      3.  这些 `bytes32` Key 都在 `contracts-v2/contracts/data/Keys.sol` 提供。

    - 根据 `scripts/printMarketInfo.ts`（约 120 行后的 `multicallReadParams`）示例，将返回的 1e30 精度数值拆成 Long/Short：

    <div class="code panel pdl" style="border-width: 1px;">

    <div class="codeContent panelContent pdl">

    ``` syntaxhighlighter-pre
       OI_long = openInterest_longCollateral_isLong + openInterest_shortCollateral_isLong
        OI_short = openInterest_longCollateral_isShort + openInterest_shortCollateral_isShort
        Market_OI = OI_long + OI_short
        
        PoolReserve_Long = collateralSum_longCollateral_isLong + collateralSum_shortCollateral_isLong
        PoolReserve_Short = collateralSum_longCollateral_isShort + collateralSum_shortCollateral_isShort
        
    ```

    </div>

    </div>

    若需要 USD 展示，可用 `MarketUtils.marketTokenAmountToUsd` 或脚本里的 `formatAmount` 进行转换。

### 2.7 `Total Earned Fees_usd`

1.  每个市场与 fee Token 组合都有 `claimableFeeAmountKey(market, token)`（定义于 `Keys.sol`）。

2.  使用 `DataStore.getUint(key)` 拿到尚未被 FeeHandler 领取的累计手续费。

3.  监听 `FeeUtils.incrementClaimableFeeAmount` 发出的 `ClaimableFeeAmountUpdated` 事件可以回放历史，或统计已被提走的部分。

4.  遍历所有 GM 市场及其可分配的 fee Token（参考部署配置或 `Reader.getMarketTokenPrices` 中的 tokens），将当前 claimable 数额与历史领取值求和，即得到 `Total Earned Fees`。

5.  也可辅助参考Dune 仪表盘（`https://dune.com/gmx-io/gmx-analytics`等）校验数据。

### 2.8 `Fee APR_24h`

1.  24 小时内的手续费增量：对所有 `ClaimableFeeAmountUpdated` 事件取 `delta`，限制时间窗口 24h（链上或离线 ETL 均可）。

2.  将增量折为 USD（如果事件以 token 数量计量，需配合当时价格或当前价格做折算）。

3.  `feeApr = fees_24h / TVL_USD`，若要年化则乘以 `365`。

4.  快速实现可依赖 Dune / Satsuma Subgraph 的现成 SQL（链接见 `ref/ref.md`），也可以将第 2.7 节的数据落库后自己计算滑动窗口。

## 3. Reader / DataStore 查询方法

1.  **必要合约地址**：`DataStore`, `Reader`, `GlvReader`, `Multicall3`，在`contracts-v2/deployments/<network>/` 中查找。

2.  **价格输入**：`Reader` 多数方法都需要 `MarketUtils.MarketPrices`，可复用`/cripts/helpers.ts#getApiEndpoint` 中配置的 GMX Infra 价格端点（例如 `https://arbitrum-api.gmxinfra2.io/prices/tickers`）。

3.  **批量读取**：推荐 `Multicall3.aggregate3` 将 `DataStore.getUint/getBool` 请求批量发送（`scripts/printMarketInfo.ts` 即此做法）。

4.  **辅助 Key**：`Keys.sol` 中的 `function xxxKey(...)` 直接返回 `bytes32`，后端可以离线编码缓存，减少链上合约调用。

## 4. 补充

`scripts/printGlvPrices.ts`、`printMarketInfo.ts` 已串好了 `Reader`、价格源、Multicall，直接改造成 API 最快。

- 

</div>
