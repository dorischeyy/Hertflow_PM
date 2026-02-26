# PRD_HzLP_V1

<div class="Section1">

# 一、修订记录

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 描述 | 修订人 | 修订内容 |
| 流动性交易面板新增滑点 | andy | <a href="https://hertzflow.slack.com/docs/T08G35AED17/F09A4RGRHN1" class="external-link" rel="nofollow">https://hertzflow.slack.com/docs/T08G35AED17/F09A4RGRHN1</a> |
| 流动性新增风控系数 - 池子权重偏差比delta% | cen | <a href="https://hertzflow.slack.com/docs/T08G35AED17/F099U6TMA2U" class="external-link" rel="nofollow">https://hertzflow.slack.com/docs/T08G35AED17/F099U6TMA2U</a> |
|  |  |  |

</div>

# 二、相关文档

埋点文档：\

## **原型文档：**

<a href="https://www.figma.com/design/I0O8W51oxPQOWBrKXOWApM/HertzFlow?node-id=1066-2" class="external-link" data-card-appearance="inline" rel="nofollow">https://www.figma.com/design/I0O8W51oxPQOWBrKXOWApM/HertzFlow?node-id=1066-2</a>\
<a href="https://www.figma.com/design/I0O8W51oxPQOWBrKXOWApM/HertzFlow?node-id=1985-3" class="external-link" data-card-appearance="inline" rel="nofollow">https://www.figma.com/design/I0O8W51oxPQOWBrKXOWApM/HertzFlow?node-id=1985-3</a>\
<a href="https://www.figma.com/design/WDFgkuyX7PmBUKyjJEPdmB/Untitled?node-id=201-274&amp;t=FjptwfOx3DybNpeK-4" class="external-link" data-card-appearance="inline" rel="nofollow">https://www.figma.com/design/WDFgkuyX7PmBUKyjJEPdmB/Untitled?node-id=201-274&amp;t=FjptwfOx3DybNpeK-4</a>\
测试用例文档：\

# 三、需求方案

### \
修订2:新增权重偏差比风控

PRD_HzLP页面优化需求 (P2)

#### 基础信息

1.  产品经理： cen 6 August

2.  需求背景：优先级P2

    1.  数据展示区：新增字段HzLP APR

    2.  交易面板：Token = SUI时 Max回填逻辑；Rate前端展示精度；Fees更优路径提示

    3.  Save on Fees去冗余

    4.  Liquidity Allocation新增hover引导

3.  相关参考：

    1.  hyperliquid：<a href="https://app.hyperliquid-testnet.xyz/vaults/0xa15099a30bbf2e68942d6f4c43d70d04faeab0a0" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.hyperliquid-testnet.xyz/vaults/0xa15099a30bbf2e68942d6f4c43d70d04faeab0a0</a>

    2.  GMX：<a href="https://app.gmx.io/#/pools/details?market=0x528A5bac7E746C9A509A1f4F6dF58A03d44279F9" class="external-link" data-card-appearance="inline" rel="nofollow">https://app.gmx.io/#/pools/details?market=0x528A5bac7E746C9A509A1f4F6dF58A03d44279F9</a>

    3.  Ostium：<a href="https://ostium.app/vaultx" class="external-link" rel="nofollow">https://ostium.app/vaultx</a>

4.  log：（当天修改记录已高亮）

    1.  `Aug15 `添加/移除最小值 \$0.1 → \$0.05 (~0.01SUI)

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="f4c750de-0e6b-48ba-9bf3-834ee650d8cc">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p><strong>需求</strong></p></td>
<td class="confluenceTd"><p>功能项</p></td>
<td class="confluenceTd"><p>原型图</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>HzLPPage_数据展示区</p></td>
<td class="confluenceTd"><ol>
<li><p>Holdings中的24h价格变化删（6Aug群里定的）</p></li>
<li><p>新增带下划线APY字段，hover展示引导文案 ‘<code>Annual Percentage Yield estimates the projected annual return based on compounding earnings. It factors in Swap, Close and Borrow Fees, Traders' Net PnL, LP Deposit/Withdrawal. Note: APY is variable and not guaranteed.</code>‘</p></li>
<li><p>计算规则<a href="https://hertzflow.slack.com/docs/T08G35AED17/F099U6TMA2U?focus_section_id=temp:C:BJI1b9d49db539747c1ad7b8de9f" class="external-link" rel="nofollow">见下表</a></p></li>
<li><p>展示规则：<br />
a. 0&lt;APY&lt;0.01% 展示<code>&lt;0.01%</code><br />
b. -0.01%&lt;APR&lt;=0 展示<code>0%</code><br />
c. 其余正常<code>2dp</code>展示，数值正不带符号，数值负带符号<br />
d. 缺省态 <code>-</code><br />
e.g. 23.33%; 2.33%; &lt;0.01%; 0%; -9.34%</p></li>
<li><p>更新频率：每日0点（EST）更新一次</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><h3 id="PRD_HzLP_V1-交易面板_逻辑优化">交易面板_逻辑优化</h3></td>
<td class="confluenceTd"><ol>
<li><p>合约新增可配参数<code>δ%_{token}</code>，代表不同资产对应可容许current weightage 与target weightage的偏差的比值，δ% 与｜c% - t%｜/ t% * 100%做比较<br />
<strong>注：</strong><code>δ%_{token}</code><strong>永远为正。</strong></p></li>
<li><p>添加<code>MaxDepositInput</code>与移除<code>MaxWithdrawInput</code>流动性阈值计算<a href="https://hertzflow.slack.com/docs/T08G35AED17/F099U6TMA2U?focus_section_id=temp:C:BJI1b9d49db539747c1ad7b8de9f" class="external-link" rel="nofollow">见下表</a>。</p></li>
<li><p><strong>BuyLP回填</strong> - 新增阈值判断 ，更新SUI特殊处理规则：</p>
<p>a. 未连接钱包 → 按钮<code>Connect Wallet</code></p>
<p>b. 已连接钱包，<code>c% ≥ t% * (1 + δ%)</code>→ 输入框禁用，按钮[]不可点击态，<code>Max Target Weightage Limit Excceeded</code></p>
<p>c. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>余额百分比%*WalletTokenAmount &lt; $0.05/TokenPrice</code> <em></em> → 按钮不可点击态提示 <em></em> <code>Min Order: 0.05 USD</code></p>
<p>d. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ， <em></em> <code>$0.05/TokenPrice ≤ 余额百分比%**WalletTokenAmount ≤ MaxDepositInput</code> <em></em> → 按钮可点击态</p>
<p>e. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>$0.05/TokenPrice ≤ 余额百分比%**WalletTokenAmount</code><em>，且</em><code> 余额百分比%*WalletTokenAmount &gt; MaxDepositInput</code> <em></em> → 按钮不可点击态提示<code>Exceeds Max Input [MaxDepositInput具体数值]</code></p>
<p>f. 所选token为SUI时，c至e特殊处理：回填数值为<code>余额百分比%*钱包SUIAmount - 0.05 0.01</code><em>；其他边界条件判断时均为</em> <code>余额百分比%*WalletSUIAmount - 0.05 0.01</code><br />
<em>（注意：两侧边界阈值</em><code>$0.05/TokenPrice </code><em>与</em><code> [MaxDepositInput]</code><em>不受影响）</em></p></li>
<li><p><strong>SellLP回填</strong> - 新增阈值判断:</p>
<p>a. 未连接钱包 → 按钮<code>Connect Wallet</code></p>
<p>b. 若<code>c% ≤ t% * (1 - δ%)</code>：输入框禁用，按钮[]不可点击态，<code> Below Min Target Weightage Limit</code></p>
<p>c.已连接钱包，<code>c% &gt; t% * (1 - δ%)</code> ，<code>余额百分比%*HzLPAmount &lt; $0.05/HzLPPrice</code> <em></em> → 按钮不可点击态提示 <em></em> <code>Min Order: 0.05 USD</code></p>
<p>d. 已连接钱包，<code>c% &gt; t% * (1 - δ%)</code> ， <em></em> <code>$0.05/HzLPPrice ≤ 余额百分比%*HzLPAmount ≤ MaxWithdrawInput</code>→ 按钮可点击态</p>
<p>e. 已连接钱包，<code>c% &gt; t% * (1- δ%)</code> ，<code>$0.05/HzLPPrice ≤ 余额百分比%*HzLPAmount</code><em>，且</em><code> 余额百分比%*HzLPAmount &gt; MaxWithdrawInput</code> <em></em> → 按钮不可点击态提示<code>Exceeds Max Input [MaxWithdrawInput具体数值]</code><br />
</p></li>
<li><p><strong>BuyLP输入框</strong> - 新增阈值判断 ，更新SUI特殊处理规则同3相似，即：<br />
a. 未连接钱包 → 按钮<code>Connect Wallet</code></p>
<p>b. 已连接钱包，<code>c% ≥ t% * (1 + δ%)</code>→ 输入框禁用，按钮[]不可点击态，<code>Max Target Weightage Limit Excceeded</code></p>
<p>c. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>Input &lt; $0.05/TokenPrice</code> <em></em> → 按钮不可点击态提示 <em></em> <code>Min Order: 0.05 USD</code></p>
<p>d. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ， <em></em> <code>$0.05/TokenPrice ≤ Input ≤ Min（WalletTokenAmount，MaxDepositInput）</code> <em></em> → 按钮可点击态</p>
<p>e. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>$0.05/TokenPrice ≤ Input </code><em>且</em><code>Input &gt; WalletTokenAmount</code> <em>→ 按钮不可点击态</em> <code>Insufficient Wallet Balance</code></p>
<p><em>f. 已连接钱包，</em><code>c% &lt; t% * (1 + δ%)</code> <em>，</em><code>$0.05/TokenPrice ≤ Input </code><em>且</em><code>Input &gt; MaxDepositInput</code> <em></em> → 按钮不可点击态提示<code>Exceeds Max Input [MaxDepositInput具体数值]</code></p>
<p>g. 所选token为SUI时，a至c同，d至f特殊处理：<br />
i. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ， <em></em> <code>$0.05/TokenPrice ≤ Input ≤ Min（WalletTokenAmount - 0.05，MaxDepositInput）</code> <em></em> → 按钮可点击态<br />
ii. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>$0.05/SUIPrice ≤ Input </code><em>且</em><code>Input &gt; WalletSUIAmount</code> <em>→ 按钮不可点击态</em> <code>Insufficient Wallet Balance</code><br />
iii. 已连接钱包，<code>c% &lt; t% * (1 + δ%)</code> ，<code>$0.05/SUIPrice ≤ Input </code><em>且</em><code>WalletSUIAmount - 0.05 &lt; Input &lt; WalletSUIAmount</code> <em>→ 按钮不可点击态</em> <code>Remaining SUI for Gas &lt; 0.05</code><br />
<em>iv. 已连接钱包，</em><code>c% &lt; t% * (1 + δ%)</code> <em>，</em><code>$0.05/TSUIPrice ≤ Input </code><em>且</em><code>WalletSUIAmount - 0.05 ≥ Input </code><em>且</em> <code>Input &gt; MaxDepositInput</code> <em>→ 按钮不可点击态提示</em><code>Exceeds Max Input [MaxDepositInput具体数值]</code></p></li>
<li><p><strong>SellLP输入框</strong> - 新增阈值判断 ，更新SUI特殊处理规则同5相似，即：<br />
a. 未连接钱包 → 按钮<code>Connect Wallet</code></p>
<p>b. 已连接钱包，<code>c% ≤ t% * (1 - δ%)</code>→ 输入框禁用，按钮[]不可点击态，<code>Below Min Target Weightage Limit</code></p>
<p>c. 已连接钱包，<code>c% &gt; t% * (1 - δ%)</code> ，<code>Input &lt; $0.05/HzLPPrice</code> <em></em> → 按钮不可点击态提示 <em></em> <code>Min Order: 0.05 USD</code></p>
<p>d. 已连接钱包，<code>c% &gt; t% * (1 - δ%)</code> ， <em></em> <code>$0.05/HzLPPrice ≤ Input ≤ Min（WalletHzLPAmount，MaxWithdrawInput）</code> <em></em> → 按钮可点击态</p>
<p>e. 已连接钱包，<code>c% &gt; t% * (1 - δ%)</code> ，<code>$0.05/HzLPPrice ≤ Input </code><em>且</em><code>Input &gt; WalletHzLPAmount</code> <em>→ 按钮不可点击态</em> <code>Insufficient HzLP Balance</code></p>
<p><em>f. 已连接钱包，</em><code>c% &gt; t% * (1 - δ%_</code> <em>，</em><code>$0.05/HzLPPrice ≤ Input </code><em>且</em><code>Input &gt; MaxWithdrawInput</code> <em></em> → 按钮不可点击态提示<code>Exceeds Max Input [MaxWithdrawInput具体数值]</code><br />
</p></li>
<li><p>Rate展示精度：<br />
a. 数值 ≥100：千分符，2dp<br />
e.g. ETH:HzLP = 3629.12; WBTC:HzLP = 114,830.052</p>
<p>b. 1≤ 数值 &lt;100：4dp<br />
e.g. SUI:HzLP = 4.1234</p>
<p>c. 0.0001≤ 数值 &lt;1：展示4sf<br />
e.g. HzLP:SUI = 0.0001234</p>
<p>d. 数值 &lt;0.0001：展示小尾巴 5sf<br />
e.g. HzLP: BTC = 0.0₅12345</p>
<p>e. 特殊处理：稳定币，外汇类波动性小的汇率展示：4dp；<br />
e.g. USDC:HzLP = 1.1234<br />
</p></li>
<li><p><strong>Save on Fees隐藏，改为交易面板明细提示：</strong>fee rate&gt;0.5%时，fees字段加<strong>下划线</strong>与<strong>警告icon</strong>，鼠标hover展示tooltip：<br />
标题：<code>Warning: Fees Too High</code><br />
文案：<code>Lowest cost via [Token Name1] - Save ~[price difference]% vs [chosen token]. </code><br />
<code>Buy with/Sell for [Token Name2] instead.</code><br />
a.<code> [Token Name1]</code> 取同InputSize内<code>费率最优</code>token<br />
i. 若多个最优，则取添加/移除对池子平衡影响更小者，即：添加则取<code>Min｜Current -Target + Input｜</code>的token，移除则取<code>Min｜Target-Current + Input｜</code>的token<br />
ii.若无更优fee rate则不展示文案，仅展示标题。<br />
b. <code>[price difference]% = （当前rate - 最优rate）/当前rate *100%</code> ，为与最优token手续费相差比值 精确至2dp<br />
c.<code> [chosen token]</code> 为当前选择购入/移除HzLP所用/所得资产<br />
d.<code> Buy with/Sell for [Token Name2] instead.</code> ：<br />
i. 添加流动性文案为Buy with...，点击超链接交易面板Pay的coinlist变为所选token symbol，输入框自动填充<code>Input_{current token} = Input_{last token} * Price_{last token}/Price_{current token}</code>; 即同等美元价值下的token数量<br />
ii. 移除流动性文案为Sell for...，点击超链接交易面板Receive的coinlist变为所选token symbol，输入框保留<code>Input_{HzLP}</code><br />
iii. <code>[Token Name2]</code>: a中计算出的最优的token name</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>Liquidity Allocation</p></td>
<td class="confluenceTd"><ol>
<li><p>0&lt;权重&lt;0.01% 展示<code>&lt;0.01%</code>，数值为0时再展示<code>0%</code></p></li>
<li><p>每列数字加下划线，鼠标hover显示可借/可移除最大流动性文案：<br />
<code>Available for Borrow: $234.12M </code><br />
<code>Max Deposit: $2,123.12B</code><br />
<code>Max Withdrawal: &lt;$0.01</code><br />
a.<code> Available for Borrow = (1-utilization%)*TVL_{token} </code>剩余可借<br />
b. <code>Remaining Deposit Limit = MaxDepositInput</code>可增流动性上限<br />
c. <code>Remaining Withdrawal Limit = MaxWithdrawInput</code>可减流动性上限</p></li>
<li><p>新增column APR +filter 选择24h/7d/1m，更新&amp;展示方式同APY，计算方式<code>见下表</code></p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

#### 字段定义与计算公式

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="3c1aa946-6fea-4a21-812e-0b31428d154b">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>类型</p></td>
<td class="confluenceTd"><p>最大操作输入公式</p></td>
<td class="confluenceTd"><p>备注</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>APY_Total</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p><code>c%_{token}</code>：当前 token 权重</p></li>
<li><p><code>APR_Day</code> 24h年化</p></li>
<li><p>不含额外奖励，如 LP Staking</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>APR_Day_{Token}</code><br />
<code>APR_Week_{Token}</code><br />
<code>APR_Month_{Token}</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><ol>
<li><p><code>F_{Day/Week/Month} = 1d/w/m内总手续费 - 1d/w/m内平台总抽成</code></p></li>
<li><p><code>TVL_avg24h</code>：LP Pool24小时内，每分钟加权平均值</p></li>
<li><p><code>TVL_avg7d</code>：LP Pool7天内，每小时加权平均值</p></li>
<li><p><code>TVL_avg30d</code>：LP Pool30天内，每天加权平均值</p></li>
<li><p><code>总手续费</code>包含：perpSwap手续费；trade开仓平仓手续费；借款利息；trade交易亏损部分；LP <strong></strong> Deposit / Withdrawal</p></li>
<li><p>注意：上线不满7天/30天时，计算手续费均值按实际天数计</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>MaxDepositInput</code></p></td>
<td class="confluenceTd"><p>条件： c%&lt;t% * (1+δ%）<br />
</p></td>
<td rowspan="2" class="confluenceTd"><ol>
<li><p><code>TVL</code>：总锁仓价值，以 USD 计价的当前流动性池总资产</p></li>
<li><p><code>c%_{token}</code>：当前权重，资产在池中当前占比（如 0.42 表示 42%）</p></li>
<li><p><code>t%_token</code>：目标权重，资产理想配置占比（如 40%）</p></li>
<li><p><code>δ%_{token}</code>：权重偏差容忍度，允许偏离的上下阈值，是一个正数（如容忍±3% 则为 3%）</p></li>
<li><p><code>P_{token}</code>：当前资产美元价格，单位为 USD/token，对于withdraw来说，是HzLP的美元价格</p></li>
<li><p>上述公式<strong>未考虑fee%</strong>，相当于设置额外缓冲（如 fee rate = 0.8%时，相当于0.992 × MaxDepositInput），可防止精度误差执行失败。</p></li>
<li><p>✅ 已确认：HzLP数值限制 上限（<strong>通过引入</strong><code>δ%_{token}</code><strong>可接受偏差）</strong>&amp;下限（<strong>0.05$写死？）</strong></p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>MaxWithdrawInput</code></p></td>
<td class="confluenceTd"><p>条件： c%&gt;t%*(1−δ%)</p></td>
</tr>
</tbody>
</table>

</div>

#### API Query （APR & APY计算）

已确认：\

1.  APR数据需求

    1.  更新频率：每日0点（EST）更新一次

    2.  计算公式：注意时长不满单位时长时 按实际天数计算。\
        （ie 刚上线20天，不满30天时，Apr_Month中的 Fee = 20天之和，TVL_avg取20天内以天为单位的加权平均，x12倍数变为x18.25 （即，365/timeperiod）

<!-- -->

1.  合约新增配置`δ%_{token}`

    1.  定义：LP池子中，权重偏差容忍度，允许偏离的上下阈值，是一个正数（如容忍±3% 则为 3%）

    2.  最大可添加/移除公式计算：

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="baab9077-69bd-499f-8cdb-81df579f7e3c">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>请求参数名</p></td>
<td class="confluenceTd"><p>必填</p></td>
<td class="confluenceTd"><p>描述</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>token</p></td>
<td class="confluenceTd"><p><code>APR</code> - 是<br />
</p></td>
<td class="confluenceTd"><p><code>APR_{token}</code>计算局部的，<code>APY</code>计算所有的<br />
<strong>更新频率：每日EST零点刷新</strong></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>period</p></td>
<td class="confluenceTd"><p>否</p></td>
<td class="confluenceTd"><p>APR 时间周期，<code>24h</code> / <code>7d</code> / <code>1m</code>，默认 <code>24h</code><br />
<strong>周期内未满则按实际天数计算</strong></p></td>
</tr>
</tbody>
</table>

</div>

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="f5fd0bad-ca96-4c31-8eb3-135ca7b115be">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>返还字段名</p></td>
<td class="confluenceTd"><p>更新频率</p></td>
<td class="confluenceTd"><p>说明</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>symbol</code></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>合约标的符号</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>apr_day_{token}</code></p></td>
<td rowspan="10" class="confluenceTd"><p>每日EST零点</p></td>
<td class="confluenceTd"><p>24h 年化收益率（%），按 <code>(F_24h - Fee_24h) × 365 / TVL_avg_24h × 100%</code><br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>apr_week_{token}</code></p></td>
<td class="confluenceTd"><p>7d 年化收益率（%）<br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>apr_month_{token}</code></p></td>
<td class="confluenceTd"><p>30d 年化收益率（%），按 <code>(F_30d - Fee_30d) × 12 / TVL_avg_30d × 100%</code><br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>apy_total</code></p></td>
<td class="confluenceTd"><p>APY 总收益率（%）<br />
</p>
<ol>
<li><p>未满一年，按实际时间计算。即，分母变为实际天数<code>n</code>，次方变为周期数量<code>365/n</code></p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>tvl_avg_24h</code></p></td>
<td class="confluenceTd"><p>LP 池 24 小时内以分钟为单位的加权平均 TVL<br />
</p>
<ol>
<li><p><code>t_i = 1min</code>; <code>N =1440</code><br />
</p></li>
<li><p>未满24h按实际时间计算</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>tvl_avg_7d</code></p></td>
<td class="confluenceTd"><p>LP 池 7 天内以小时为单位的加权平均 TVL<br />
</p>
<ol>
<li><p><code>t_i = 1h</code>; <code>N =168</code><br />
</p></li>
<li><p>未满7d按实际时间计算</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>tvl_avg_30d</code></p></td>
<td class="confluenceTd"><p>LP 池 30 天内以天wei dan wei de加权平均 TVL<br />
</p>
<ol>
<li><p><code>t_i = 1d</code>; <code>N =30</code><br />
</p></li>
<li><p>未满30d按实际时间计算</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>F_24h - F_fee_24h</code></p></td>
<td class="confluenceTd"><p>扣除平台抽成的 24 小时总收入<br />
</p>
<ol>
<li><p>收入包括perpSwap手续费；trade开仓平仓手续费；借款利息；trade交易亏损部分；LP <strong></strong> Deposit / Withdrawal</p></li>
<li><p>未满24h按实际时间计算</p></li>
</ol></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>F_7d - F_fee_7d</code></p></td>
<td class="confluenceTd"><p>扣除平台抽成的 7天总收入</p></td>
</tr>
<tr>
<td class="confluenceTd"><p><code>F_30d - F_fee_30d</code><br />
</p></td>
<td class="confluenceTd"><p>扣除平台抽成的 一个月总收入</p></td>
</tr>
</tbody>
</table>

</div>

### 修订1：流动性面板增加滑点

- 功能概述：允许用户在流动性池面板查看和修改注入/提取流动性的交易滑点。

- 功能入口：流动性面板下方。

- 默认状态：：初始滑点值默认显示为***2%（参考jupiter）***，展示在交易面板滑点设置区域

- 弹窗：

  - **触发条件**：用户点击交易面板中的滑点设置按钮。

  - **弹窗内容**：显示四个选项：1%、2%、3%、自定义。

  - **用户选择“自定义”** ：弹窗保持开启状态，用户可以手动输入框。

  - **输入规则**：

    - 合法范围：滑点值必须大于0%且小于5%（即0.01% ≤ 输入值 ≤ 4.99%）。如输入值不在此区间，则按钮置灰，提示：Slippage value must be within 0% to 5%

    - 精度限制：最多允许输入两位小数（如1.25%）

    - 

### HLP页面

- 页面分区：HLP页面一共分为两个部分，分别是：左侧的HLP信息展示区、右侧的交易操作区

  - 信息展示区

    - 模块分区：一共分为三个模块，从上到下分别是：HLP概念展示区、HLP数据展示区、HLP流动性展示区

  - 交易操作区

    - 模块分区：一共分为三个模块，从上到下分别是：个人HLP数据展示、操作面板、手续费面板

### HLP概念展示区

- 基础概念：展示HLP的具体概念，帮助用户理解HLP的含义

- 展示字段：固定字段：The HertzFlow Liquidity Pool (HLP) acts as a counterparty for leveraged traders, lending them assets. The HLP token’s value reflects:

  · A basket of BTC, ETH, SUI, USDC;\
  · Traders’ net profits/losses;\
  · fees from trading, borrowing, and position adjustments.

- 点击按钮：

  - 点击交互：点击后跳转到docs中介绍HLP的相关页面

  - 跳转链接：待补充

### HLP数据展示区

- 基础概念：展示HLP的基础数据内容

- 字段

  - HLP Price

    - 基础概念：展示HLP的价格

    - 展示规范：单位为USD、小数保留两位

    - 被动更新：当HLP价格变动时更新

    - 计算方式：HLP总价值/ HLP总供应

  - HLP Supply

    - 基础概念：展示HLP的流通中的数量

    - 数值格式化：

      - k：千，如 12.23k= 12,230

      - m：百万（million），如 12.23m = 12,230,000

### HLP流动性展示区

- Liquidity展示

  - Total Liquidity

    - 基础概念：展示当前的HLP的总liquidity

    - 计算方式：HLP中的币种\*价格然后相加

    - 展示规范：单位为USD、小数保留两位

  - Limit

    - 基础概念：展示当前HLP所设置的最大可接受的流动性

    - 数据获取：从HLP中取设置的Limit

    - 展示规范：单位为USD、小数保留两位

    - 解释字段：The pool is only accepting new funds up to \$1,750,000,000 at the moment.

  - Liquidity Allocation

    - 基础概念：展示每个单个币种的流动性数据

    - 字段

      - Token

        - 基础概念：展示这一条所对应的token名称

        - 白名单：展示白名单中支持的币种，包括：BTC、ETH、SUI、USDC

        - 展示规则：币种缩写+币种全称

      - Pool Size

        - 基础概念：展示该token在HLP中的Size

        - 展示规范：单位为USD、小数保留两位

        - 计算方式：该币种在HLP中的数量\*价格（价格从预言机获取

        - 更新频率：size变动时触发

      - Current / Target Weightage

        - 基础概念：展示该token所对应的current和target比例

        - 展示规范：「current weightage / target weightage」；用百分比表示，保留两位小数 例如：22.32% / 12.32%

        - 计算方式

          - current weightage：该token在HLP的价值/HLP总价值

          - target weightage：从HLP中读取该token所配置的target weightage

        - 解释字段：Fees are determined by the pool's current weight distribution, so LPs are incentivized to rebalance to their target allocations.

      - Utilization

        - 基础概念：展示该token在prep交易中被借出的比例

        - 展示规范：用百分比表示，保留两位小数 例如：22.32%

        - 计算方式：该token被借出占用的数量/该token在HLP中的总数量

### 个人HLP数据展示

- 基础概念：展示该用户钱包的HLP数据信息

- 字段：

  - Wallet

    - 基础概念：展示该用户钱包中的HLP数量

    - 展示规范：「HLP数量」（「估值」） HLP数量精度为四位，估值单位为USD，精度两位 例如：23.3234 HLP (\$23.34)

    - 特殊情况：如果没有链接钱包，则展示为“—”

  - Rewards

    - 基础概念：展示该用户通过HLP所获得到了收益

    - 展示规范：

      - 基础规范：「rewards」（「百分比」）

      - 展示规范：rewards单位为USD，精度两位；百分比精度两位；例如：\$23.34(23.34%) ；百分比上涨时为绿色，下跌时为红色，百分比为0时为黑色

      - 计算公式：

        - rewards：HLP当前价格\*wallet中HLP数量 - HLP平均购入价格\* wallet中HLP数量

        - 百分比：（HLP当前价格\*wallet中HLP数量 - HLP平均购入价格\* wallet中HLP数量）/HLP平均购入价格\* wallet中HLP数量

      - 特殊情况

        - 未链接钱包：展示为“—”

        - 没有收入：暂时0.00（0%）

### 操作面板

- 基础概念：在此处用户可以使用自己的资产来购买/铸造和出售/销毁HLP

- buy/sell交互：默认为buy，点击可以切换sell。不记录切换

- 输入框

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="a8a4ac4a-d339-4134-a2e3-c1da1151738c">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>规则项</p></td>
<td class="confluenceTd"><p>说明</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>默认值</p></td>
<td class="confluenceTd"><p>0.00（灰色显示）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>输入限制</p></td>
<td class="confluenceTd"><p>仅允许数字(0-9)和小数点(.)，禁止多个小数点</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>最大长度</p></td>
<td class="confluenceTd"><p>50个字符</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>精度处理</p></td>
<td class="confluenceTd"><p>HLP输入框精度限制为四位<br />
币种输入框精度按照币种在合约中配置的精度</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>单位规则</p></td>
<td class="confluenceTd"><p>如果是buy，则pay输入框默认为SUI；receive 输入框固定为HLP<br />
如果是Sell，则pay输入框固定为HLP；receive输入框默认为SUI</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>单位切换</p></td>
<td class="confluenceTd"><p>精度规则：新精度≥原精度时保留原值，新精度&lt;原精度时截断至新精度（例：12.345→12.34）<br />
切换规则：如果是buy，则pay输入框可切换单位；如果是sell，则receive输入框可切换单位</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>USD折算显示</p></td>
<td class="confluenceTd"><p><strong>实时公式</strong>：输入值 × 最新价格<br />
<strong>显示位置</strong>：输入内容下方<br />
<strong>格式要求</strong>：保留2位小数（去尾）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>余额展示</p></td>
<td class="confluenceTd"><p><strong>未连接钱包</strong>：显示：--<br />
<strong>余额为0</strong>：显示:0.00<br />
<strong>有余额</strong>：显示具体数值<br />
<strong>50%/100%按钮</strong>：点击回填对应比例数值</p></td>
</tr>
</tbody>
</table>

</div>

- fees

  - 基础概念：展示当前输入框中输入的内容所对应的手续费

  - 展示规则：默认为0.00%，灰色显示

  - 获取来源：从HLP中获取

  - 触发更新：根据输入框中输入的内容实时更新

  - 特殊情况：

    - 未链接钱包：展示为“—”

    - fee rate大于0.5%时：fees字段变更为“Warning：High Fees”

- 按钮

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="dde73fdc-6472-45fa-b28a-ee3c72f58139">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>状态/场景</p></td>
<td class="confluenceTd"><p>行为/显示规则</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>未输入任何内容</p></td>
<td class="confluenceTd"><p>置灰，展示字段：Enter an amount</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>交易过程中</p></td>
<td class="confluenceTd"><p>置灰<br />
如果是buy，展示字段：Buying<br />
如果是sell，展示字段：Selling</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>pay输入框中输入的数量大于钱包余额</p></td>
<td class="confluenceTd"><p>置灰，展示字段：Insufficient BTC balance</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>buy时，receive输入框中输入的价值大于系统设置的最大可接受的交易量时<br />
sell时，pay输入框中输入的价值大于系统设置的最大可接受的交易量时</p></td>
<td class="confluenceTd"><p>置灰，展示字段： MAX ：XXXX HLP</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>所有信息输入正确</p></td>
<td class="confluenceTd"><p>亮起<br />
如果是buy，展示字段：Buy GLP<br />
如果是sell，展示字段：Sell GLP</p></td>
</tr>
</tbody>
</table>

</div>

- 交易刷新：每次交易完成后，刷新一遍钱包余额

### 手续费面板

- 基础概念：展示每个token所对应的手续费，方便用户寻找交易成本最低的token

- 字段

  - token

    - 基础概念：展示这一条所对应的token名称

    - 白名单：展示白名单中支持的币种，包括：BTC、ETH、SUI、USDC

    - 展示规则：币种缩写+币种全称

  - Fees

    - 基础概念：展示当前上方操作面板输入框中输入的内容所对应的手续费

    - 展示规则：默认为0.00%，灰色显示

    - 获取来源：从HLP中获取

    - 触发更新：根据输入框中输入的内容实时更新

    - 交互规则：币种中手续费率最低的token的高亮显示

  - 按钮

    - 固定字段：“buy with 「token name」” 例如：Buy with BTC

    - 交互规则：点击按钮，则回填该token单位到上方操作面板之中，如果是buy，则回填到pay 输入框；如果是sell，则回填到receive输入框

## 接口文档

<div class="table-wrap">

<table class="confluenceTable" style="width:100%;" data-table-width="760" data-layout="default" data-local-id="14528192-2158-47e6-b5df-d8c4c4566d80">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td class="confluenceTd"><p>序号</p></td>
<td class="confluenceTd"><p>模块</p></td>
<td class="confluenceTd"><p>位置</p></td>
<td class="confluenceTd"><p>后端对应接口</p></td>
<td class="confluenceTd"><p>后端</p></td>
<td class="confluenceTd"><p>前端</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>01</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
传输当前HLP总铸造数量<br />
预言机获取各个币种最新价格传输前端</p></td>
<td class="confluenceTd"><p>HLP price = （各个币种数量*对应最新价格加合）/HLP总铸造数量</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>02</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP总铸造数量</p></td>
<td class="confluenceTd"><p>展示后端数据<br />
</p>
<ul>
<li><p>数值格式化：</p></li>
<li><p>k：千，如 12.23k= 12,230</p></li>
<li><p>m：百万（million），如 12.23m = 12,230,000</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd"><p>03</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
预言机获取各个币种最新价格传输前端</p></td>
<td class="confluenceTd"><p>total liquidity = 各个币种数量* 对应最新价格加合</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>04</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输HLP中设置的最大可接受的liquidity</p></td>
<td class="confluenceTd"><p>展示后端数据</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>05</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输币种白名单列表</p></td>
<td class="confluenceTd"><p>展示白名单中的币种数据（目前白名单百包括：BTC、ETH、SUI、USDC</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>06</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
预言机获取各个币种最新价格传输前端</p></td>
<td class="confluenceTd"><p>pool size = 币种数量* 对应最新价格</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>07</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
预言机获取各个币种最新价格传输前端<br />
传输HLP设置的 target weightage</p></td>
<td class="confluenceTd"><p>current weightage = （单个币种数量*最新价格）/HLP总价值<br />
target weightage：直接展示后端数据</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>08</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
预言机获取各个币种最新价格传输前端<br />
传输HLP中被用户持仓借款占用的数量</p></td>
<td class="confluenceTd"><p>utilization = （币种被借贷占用数量*最新价格）/（币种在HLP中的总数量* 最新价格）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>09</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>--</p></td>
<td class="confluenceTd"><p>直接读取用户的钱包地址中的HLP数量，然后展示</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>10</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输当前HLP的各个币种数量<br />
传输当前HLP总铸造数量<br />
预言机获取各个币种最新价格传输前端</p></td>
<td class="confluenceTd"><p>读取用户钱包地址中的HLP数量，然后计算平均购入均价<br />
计算当前HLP价格<br />
</p>
<ul>
<li><p>展示规范：rewards单位为USD，精度两位；百分比精度两位；例如：$23.34(23.34%) ；百分比上涨时为绿色，下跌时为红色，百分比为0时为黑色</p></li>
<li><p>计算公式：</p></li>
<li><p>rewards：HLP当前价格*wallet中HLP数量 - HLP平均购入价格* wallet中HLP数量</p></li>
<li><p>百分比：（HLP当前价格*wallet中HLP数量 - HLP平均购入价格* wallet中HLP数量）/HLP平均购入价格* wallet中HLP数量</p></li>
</ul>
<p>HLP 当前价格 = （各个币种数量*对应最新价格加合）/HLP总铸造数量<br />
</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>11</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>--</p></td>
<td class="confluenceTd"><p>直接读取用户的钱包地址中的对应币种数量，然后展示</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>13</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输HLP所有币种的费率</p></td>
<td class="confluenceTd"><p>展示该币种交易费率</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>14</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输币种白名单列表</p></td>
<td class="confluenceTd"><p>展示白名单中的币种数据（目前白名单百包括：BTC、ETH、SUI、USDC</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>15</p></td>
<td class="confluenceTd"><p>HLP页面</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"><p>传输HLP所有币种的费率</p></td>
<td class="confluenceTd"><p>展示对应币种交易费率</p></td>
</tr>
</tbody>
</table>

</div>

</div>
