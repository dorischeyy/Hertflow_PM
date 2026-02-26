# Trade Page新机制引入_PRD

<div class="Section1">

## <style>[data-colorid=lwgfe1fswi]{color:#bf2600} html[data-color-mode=dark] [data-colorid=lwgfe1fswi]{color:#ff6640}[data-colorid=bxxwi11nyw]{color:#bf2600} html[data-color-mode=dark] [data-colorid=bxxwi11nyw]{color:#ff6640}[data-colorid=pwmv1xitby]{color:#36b37e} html[data-color-mode=dark] [data-colorid=pwmv1xitby]{color:#4cc994}[data-colorid=bk838w30v0]{color:#ff991f} html[data-color-mode=dark] [data-colorid=bk838w30v0]{color:#e07a00}[data-colorid=zqb034tsc8]{color:#36b37e} html[data-color-mode=dark] [data-colorid=zqb034tsc8]{color:#4cc994}[data-colorid=zwunrtnpt7]{color:#bf2600} html[data-color-mode=dark] [data-colorid=zwunrtnpt7]{color:#ff6640}[data-colorid=nfdoar4sxs]{color:#bf2600} html[data-color-mode=dark] [data-colorid=nfdoar4sxs]{color:#ff6640}[data-colorid=imtqihlg15]{color:#bf2600} html[data-color-mode=dark] [data-colorid=imtqihlg15]{color:#ff6640}</style>1. 背景与目标

### 1.1 背景

基于 GMX V2 合约能力，引入 Avantis 风格的高杠杆与风险控制机制，以提升平台对高杠杆偏好的tradfi迁徙过来的交易者们的吸引力，同时通过差异化收费、风控约束与 OI 重平衡补偿机制，维持系统级风险可控与 LP 收益稳定。产品层面尽量规避过高相似性。

### 1.2 目标

1.  **模式区分：**常规杠杆模式（下面称为**Normal**），超高模式（下面称为**Hyper**）

    1.  合约新增市场配置：Max Lev Normal（已有mincollateralfactor）；`Min Lev Hyper`；`Max Lev Hyper` 不同资产用不同数值。

        1.  **合规范围：**Normal - 杠杆倍数为**1.1x - Max Lev Normal**；Hyper - 杠杆倍数为 **Min Lev Hyper - Max Lev Hyper**。**不合规** → **revert**

        2.  **配置规则：**参考avantis 12个超高杠杆市场的<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/55312675/Trade+Page+_PRD#2.1.1-%E6%9D%A0%E6%9D%86%E5%8C%BA%E9%97%B4%E5%AE%9A%E4%B9%89" rel="nofollow">实际参数</a>

        3.  **⚠️ 注意：**<span style="background-color: rgb(254,222,200);">Max Lev Normal 不一定等于Min Lev Hyper。比如：PEPE/USD Normal 1x - </span>**<span style="background-color: rgb(254,222,200);">20x</span>**<span style="background-color: rgb(254,222,200);">；Hyper</span>**<span style="background-color: rgb(254,222,200);">75x</span>**<span style="background-color: rgb(254,222,200);"> - 100x。</span>

    2.  合约需区分两种收费模型：

        1.  **收费模型：Normal -** 不变。Hyper - **不收开平仓，funding与借贷费**（强平 ~~&<span class="inline-comment-marker" ref="8154149d-77e5-46d8-bd35-7bf94cc31f83"> funding</span>~~仍收）。同时需制定**盈利抽成函数 Fee_Hyper = f(PnL%包含费用计算) 先收费再抽成**

        2.  **Hyper Mode 盈利抽成规则：**

            - 生效于：仅针对PnL \> 0的超高杠杆模式下的盈利仓位

            - 规则：详解见下方<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/55312675/Trade+Page+_PRD#2.1.2-%E8%B6%85%E9%AB%98%E6%9D%A0%E6%9D%86%E6%A8%A1%E5%BC%8F%E4%B8%8B%EF%BC%9A%E7%9B%88%E5%88%A9%E6%8A%BD%E6%88%90%E5%87%BD%E6%95%B0%E6%A8%A1%E5%9E%8B%E8%A7%A3%E6%9E%90" rel="nofollow">机制细节</a>

              - 函数需根据**资产类型分别定制**

              - 分段线性函数

              - PnL%越高，盈利抽成越低。

              - x轴的PnL%到达强制止盈的PnL%时，y轴的**盈利抽成占比** = **强平费率**

    3.  合约需实现**Hyper**模式下特殊**功能限制**：

        1.  同市场同方向的Hyper 与 Normal**不可以自动合并** 必须独立仓位 - **Mode 一旦确定，仓位生命周期内不可变。**

        2.  **仅市价单可选超高杠杆下单，限价只有Normal**

        3.  止盈止损与position id绑定时，**必须包含 Mode 维度（Normal / Hyper），**否则会出现normal被误平，hyper裸奔

        4.  **超高杠杆仓位不可移除保证金**

        5.  **超高杠杆仓位不参与损失补偿**

2.  **止盈止损（TP/SL）- 新增跳变保护；下单校验；执行校验。**

    1.  保证止盈止损：

        1.  **实际成交的执行价格：**严格使用**等于或优于**用户设置的 TP / SL 价格

        2.  **预言机跳变保护：**预言机价格瞬时跳变的情景下，合约在清算判断前，必须先评估 SL 是否已触发。当仓位同时满足触发清算与触发SL条件时，**优先执行止损**逻辑。

    2.  止盈上限：**由合约测约束最大收益限制。超出该区间的止盈单，则提交时revert。超出该区间的仓位，强平。**

        1.  适用于：**所有订单，**不限模式或类型。属于强平的逻辑。

        2.  上限：实际 PnL% ≤`Profit% Cap`

        3.  合约参数配置：`Profit% Cap` ，**市场级参数**

    3.  止损上下限：**由合约测约束条件单的最小/最大亏损限制。超出该区间的止损单，则提交时revert。**

        1.  适用于：**仅条件单，不同模式下参数不同。**属于条件单才有的减仓逻辑。

        2.  上下限：`Max Loss%` ≤ 止损单实际PnL% ≤`Min Loss%`

        3.  合约参数配置：**前期可设置全局参数，不分资产类型，只分是否为超高杠杆。**

            1.  Normal模式下：只有单边`Max Loss%`。avantis设置为常量-80%，相当于强平线上留5%的缓冲来保证keeper执行成功。

            2.  Hyper 模式下：双边。`Max Loss%` = -80%，Min Loss% = -30%。

3.  **激励制度 - 普通杠杆情况下： OI 重平衡损失补偿（Loss Rebate）**

    1.  适用：模式 - **普通杠杆，**方向 - **开仓执行时，OI弱势方，名义价值（不论市价或限价）小于OI差值**

    2.  合约参数配置：市场级参数 `Loss Rebate Rate`，<a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/55312675/Trade+Page+_PRD#Avantis%E9%85%8D%E7%BD%AE" rel="nofollow">可参考avantis实际配置</a>

    3.  计算逻辑：仅对 **已实现亏损部分** 计算，**Loss Rebate = Loss Rebate Rate \* Loss**

    4.  ⚠️ <span style="background-color: rgb(254,222,200);">补偿路径：</span>**<span style="background-color: rgb(254,222,200);">来源于池子收入，</span>**<span style="background-color: rgb(254,222,200);">补偿在仓位结算时一次性发放。</span>

## 2. 附录

### 2.1 超高杠杆 & 激励机制

#### **2.1.1 杠杆区间定义**

> 灰色部分为正常模式，橙色部分为超高杠杆模式。

<div class="table-wrap">

|  |  |  |  |  |
|----|----|----|----|----|
| **<span class="legacy-color-text-inverse">Category</span>** | **<span class="legacy-color-text-inverse">Symbol</span>** | **<span class="legacy-color-text-inverse">Max Lev Normal</span>** | **<span class="legacy-color-text-inverse">Min Lev Hyper</span>** | **<span class="legacy-color-text-inverse">Max Lev Hyper</span>** |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">BLUECHIP CRYPTO</span> | ETH/USD | 75 | 75 | 500 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">BLUECHIP CRYPTO</span> | BTC/USD | 75 | 75 | 500 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">BLUECHIP CRYPTO</span> | SOL/USD | 75 | 75 | 500 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">CRYPTO</span> | XRP/USD | 75 | 75 | 500 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">CRYPTO</span> | HYPE/USD | 20 | 75 | 250 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-complete">CRYPTO</span> | DOGE/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-error">MEME</span> | FARTCOIN/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-error">MEME</span> | BONK/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-error">MEME</span> | PEPE/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-error">MEME</span> | SHIB/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-error">MEME</span> | WIF/USD | 20 | 75 | 100 |
| <span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-success">FX</span> | USD/JPY | 500 | 200 | 1000 |

</div>

#### 2.1.2 超高杠杆模式下：盈利抽成函数模型解析

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="cd3e558772fc052eb9de810ae3709a8916344831547599bb3f2426a1392b38e7" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/55312675/Screenshot%202025-12-16%20at%2015.05.40.png?version=1&amp;modificationDate=1765870358044&amp;cacheVersion=1&amp;api=v2" data-height="909" data-width="1553" data-unresolved-comment-count="0" data-linked-resource-id="56557680" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-16 at 15.05.40.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="55312675" data-linked-resource-container-version="8" data-media-id="d9f3b4d6-9774-4697-8963-078d51db8cad" data-media-type="file" width="468" height="274" alt="Screenshot 2025-12-16 at 15.05.40.png" /></span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5528dc5ab4ffbdf39361c1eacb56ed38bf3c1da791844da73afabbff69eecf40" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/55312675/Screenshot%202025-12-16%20at%2015.53.37.png?version=1&amp;modificationDate=1765871635707&amp;cacheVersion=1&amp;api=v2" data-height="63" data-width="1315" data-unresolved-comment-count="0" data-linked-resource-id="56655936" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2025-12-16 at 15.53.37.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="55312675" data-linked-resource-container-version="8" data-media-id="27f4342e-b97e-4b0a-bda0-7560f09355b5" data-media-type="file" width="468" height="22" alt="Screenshot 2025-12-16 at 15.53.37.png" /></span>

1.  **定义：**橙色部分为avantis盈利结余函数，红色部分为推荐的hertflow函数设计。

2.  x轴：**<span colorid="bk838w30v0">经推断，</span>**代表**不计费用**的**Gross PnL 净值**。（推断根据为图2，gross pnl% = 95.97%，结余pnl% = 69.6%，平台抽成（95.97% - 69.6%）/ 95.97% = 27.48%，对应图中y = 72.52%，x 约100%）

3.  y轴：代表用户留下的盈利，占初始保证金的比例。

4.  计算逻辑：**Fee_Hyper = f(PnL%)** = **(1 - y) \* PnL% \* 初始保证金。Fee Hyper**代表平台抽走的手续费。**f(PnL%)** 代表需要设计的分段线形函数，变量为x轴的**PnL%**

5.  ⚠️ **边界值设定：**橙色标点（2500%，85%）是针对所有仓位的最大止盈线。相当于**未实现盈亏率** = 2500%时，会触发强平。此时 y = 85%，平台抽成 **Fee_Hyper** = **(1 - y) \* PnL% \* 初始保证金 = 15% \* 25 \* 初始保证金。强平费为15% \* 初始保证金。**不知是否有意为之，y这里抽成比例跟强平费率是同一个值。

6.  ⚠️ **资产类型不同，函数模型不同：**很明显，同样的条件下，同一名用户下单BTC，盈利2500%，对应在JPY上可能就盈利500%。所以不同资产的x轴会有不同程度的缩放，因此函数模型需根据不同资产类型去定制，而不是用同一个。

### 2.2 TP / SL 与 Guaranteed TP/SL

#### 2.2.1 Guaranteed TP/SL

当预言机价格发生瞬时闪崩 / 跳变时：

- 不触发非预期强平

- **严格**按用户设置的 止盈止损价格减仓

#### 2.2.2 Avantis配置的TP / SL 边界限制

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="598a6c6f-e016-4e5b-a0f2-a1b2ae164fd4">
<tbody>
<tr data-local-id="e9c95965-0a9d-4247-9d81-0083c12320fe">
<th class="confluenceTh" data-local-id="d0f6b234-d664-488e-900c-8d36948eee8f"><p>类型</p></th>
<th class="confluenceTh" data-local-id="332868b8-01c1-487d-aa7c-c3abaf3aa611"><p>限制</p></th>
</tr>
&#10;<tr data-local-id="7e1ccc5f-ca80-49ef-912d-a0c5307b552a">
<td class="confluenceTd" data-local-id="be6a2af4-991c-45e7-b769-d2c9631b03fb"><p>常规杠杆</p></td>
<td class="confluenceTd" data-local-id="719aa1c5-e1c5-40b5-afd0-ddb62f64d6c4"><ol>
<li><p>所有仓位PnL &lt;= MaxPnL%</p></li>
<li><p>条件单PnL &gt;= -80%</p></li>
<li><p>MaxPnL% = 1000% <span class="status-macro aui-lozenge aui-lozenge-visual-refresh">美股</span> 或 500%<span class="status-macro aui-lozenge aui-lozenge-visual-refresh">其他非超高杠杆资产类型</span></p></li>
</ol></td>
</tr>
<tr data-local-id="9b9ea4d3-818a-4392-8e93-17bbec229ad3">
<td class="confluenceTd" data-local-id="20de2f8c-ba89-4030-95dc-ff9010b8c196"><p>超高杠杆</p></td>
<td class="confluenceTd" data-local-id="e8d9e55f-fae1-4e69-aaf8-92000fe63f39"><ol>
<li><p>所有仓位PnL &lt;= 2500%</p></li>
<li><p>条件单 -80% &lt;= PnL &lt;= -30%</p></li>
</ol></td>
</tr>
</tbody>
</table>

</div>

### 2.3 普通杠杆情况下： OI 重平衡损失补偿

#### Avantis配置

<div class="table-wrap">

|                    |                  |
|--------------------|------------------|
| **Market类型**     | **Loss Rebate%** |
| 指数               | 10%              |
| 蓝筹               | 8%               |
| 外汇，山寨币，美股 | 5%               |
| Meme               | 3%               |

</div>

#### 举例

假设 long OI是 1.1m，short oi是1m。OI Imbalance =｜OI Long - OI Short｜= 0.1m。此时：

1.  用户A下单，正常杠杆，市价单，开多：强势方向，无补偿

2.  用户B下单，超高杠杆，市价单，开空：Hyper Mode，无补偿

3.  用户C下单，正常杠杆，市价单，开空，size = 1m：size \> OI imbalance，无补偿

4.  用户D下单，正常杠杆，限价单，开空，0.1m。keeper成功执行时 long OI变成1.09m：size \> OI imbalance，无补偿

5.  用户E下单**指数**，正常杠杆，限价单，开空，0.1m。（**假设用户的指数仓位初始保证金 = 10k，lev = 10x**）keeper成功执行时OI Imbalance \> 0.1m, 且空方仍为弱势：**有补偿。合约根据市场类型返还其Loss Rebate% = 10%，并标记该仓位绑定了10%的损失补偿。**

    1.  用户E执行部分平仓或被清算：假设其RPnL% = -70%，用户减仓1/2。

    2.  执行时，用户E的损失补偿**Loss Rebate = Loss Rebate% \* -1 \* RPnL = 10% \* (1/2 \* 70% \* 100k) = 3.5k**

### 2.4 参数调优

我们定义一下参数：初始保证金 - C<sub>Init</sub>，总盈亏（率） - PnL(%)，MMR - 维持保证金率，f<sub>Liq</sub>% - 强平费率，r<sub>loss</sub>% - 正常杠杆的损失补偿比例。

1.  MMR：要么改定义，要么调参。 0.2% → 0.01%，相当于1000x杠杆，维持保证金10%（avantis不分杠杆倍数，永远维持保证金15%）

2.  f<sub>Liq</sub>%：Liq Fee = f<sub>Liq</sub>% \* C<sub>Init</sub>，肯定要\<10%，不然1000x仓位被强平时，剩的10%保证金不够支付费用会坏账。

3.  r<sub>loss</sub>%：Loss Rebate = r<sub>loss</sub>% \* PnL% \* C<sub>Init</sub>

4.  普通杠杆模式下，我们增加了强平费收入，确同时增加了损失补偿的支出。制定参数时，仅能参照avantis，因此按其r<sub>loss</sub>% 与 f<sub>Liq</sub>%的比例关系对应反推：avantis<span colorid="pwmv1xitby">收入的强平费15% \* C<sub>Init</sub></span> → 强平时用户亏损85% \* C<sub>Init</sub> → 损失返还按平均r<sub>loss</sub>% = 10%算，<span colorid="lwgfe1fswi">支出的Loss Rebate = 8.5% \* C<sub>Init</sub></span> → 假设我们市场行情，OI，损失补偿，爆仓概率都差不多，<span colorid="zqb034tsc8">收入的强平费8% \* C<sub>Init</sub></span> ，用户亏损90% \* C<sub>Init</sub> ，r<sub>loss</sub>% = **5%**时，<span colorid="bxxwi11nyw">支出的Loss Rebate = 4.5% \* C<sub>Init</sub></span>。差不多都是收入：支出 = 1.76x

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="81f9ca86-a295-4508-a533-1fc59680ef24">
<tbody>
<tr data-local-id="92b46895-9c5d-4667-a797-ff9b237b1906">
<th class="confluenceTh" data-local-id="09085961-ec51-4867-89b9-ad512aec21a5"></th>
<th class="confluenceTh" data-local-id="42495296-ce4f-4148-b69d-4edf3102867a"><p><strong>avantis</strong></p></th>
<th class="confluenceTh" data-local-id="0b348568-c0c1-4007-9d04-046e6bf3a674"><p><strong>hzfl</strong></p></th>
</tr>
&#10;<tr data-local-id="f74e3ae3-e47e-4591-ae59-9bc4c40f5bf2">
<td class="confluenceTd" data-local-id="612ebbe8-f844-4d41-ab72-59a5e7f5797d"><p>维持保证金率 MMR</p></td>
<td class="confluenceTd" data-local-id="5de89f67-bf1b-4412-9bd0-64468b4f1a24"><p>= net value / collateral = 15%</p></td>
<td class="confluenceTd" data-local-id="5729d000-e110-4a7c-a813-ca7f2ad8cfe5"><p>= net value / size = 0.2%</p>
<p><strong><span data-colorid="imtqihlg15">最大杠杆100x → 1000x; MMR也需要调参; 假设我们调到0.01%</span></strong></p></td>
</tr>
<tr data-local-id="84eca27d-d019-4cbf-87cd-667025dcf0a0">
<td class="confluenceTd" data-local-id="d5ce0fb3-7e84-4cb8-80b0-3919391f353c"><p>强平费 Liq Fee</p></td>
<td class="confluenceTd" data-local-id="169245a6-f2fd-4365-a16d-9e259abe0e56"><p>= collateral * 15%</p></td>
<td class="confluenceTd" data-local-id="a6a14427-4ee1-48bb-b0e4-4fc0f34d3b98"><p>= collateral * 0.2%</p>
<p><strong><span data-colorid="zwunrtnpt7">这里建议调到8%</span></strong></p></td>
</tr>
<tr data-local-id="cc37aa57-270e-4f72-a7db-5d76039d74fc">
<td class="confluenceTd" data-local-id="0d4e37f3-c0dc-4d91-884b-2b7f7563faae"><p>损失补偿 Loss Rebate</p></td>
<td class="confluenceTd" data-local-id="66b3bc8b-c029-45c6-9cc1-32317b3587e7"><p>= (net value - coll) * 10%</p></td>
<td class="confluenceTd" data-local-id="ab095098-317b-4162-b9fb-1d4131cb925f"><p>= (net value - coll) * 5%</p>
<p><strong><span data-colorid="nfdoar4sxs">前期建议统一5%或以下</span></strong></p></td>
</tr>
<tr data-local-id="d1c28b21-9da2-433a-9008-f8a6681e84c4">
<td class="confluenceTd" data-local-id="4f8b0681-342f-4424-9ccd-7055ba73dcf0"><p>二者关系</p></td>
<td class="confluenceTd" data-local-id="88ffc559-71b9-4b7d-a59e-4e7cffdad17f"><p>强平线限制了net value &gt;= 15% coll；因此 <strong>loss rebate &lt;= 8.5% * col</strong>l</p></td>
<td class="confluenceTd" data-local-id="1a966a67-11e6-4da3-83be-c37ca704202f"><p>强平线限制了net value &gt;= 0.01% * Lev * coll；当 Lev = 1000x时，被强平仓位的<strong>Loss Rebate &lt;= 4.5% * coll</strong></p></td>
</tr>
</tbody>
</table>

</div>

## 3. 技术实现

> **ZFP 改的是“仓位模式”，Guaranteed SL 改的是“清算优先级”，OI 补偿改的是“结算阶段的分润逻辑”。**
>
> **Keeper 本质从“被动清算者”升级为“仓位状态机执行者”，只做四件事：**
>
> 1.  监听合约事件
>
> 2.  维护 off-chain 状态（DB / Redis）
>
> 3.  按合约已定义规则触发 execute
>
> 4.  在多个可执行路径中，**选择合约已经允许的那条**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="1c0e32e9-1638-412a-b599-9ac8ef3d7bd2">
<tbody>
<tr data-local-id="7394dc31-e71b-451f-9051-158283ad2332">
<th class="confluenceTh" data-local-id="1ec182d7-66f0-4f11-b65f-850902f46039"></th>
<th class="confluenceTh" data-local-id="e8a9f263-9d16-4d06-a310-89e5a38ec504"><p><strong>Keeper</strong></p></th>
<th class="confluenceTh" data-local-id="91e1e960-4384-45ef-b6af-d6d0cefe5506"><p><strong>合约</strong></p></th>
</tr>
&#10;<tr data-local-id="790f512f-f0f7-40f9-bb77-1503b96752ff">
<td class="confluenceTd" data-local-id="aaafe317-0013-426b-99fa-93acfafea5d9"><p><strong>数据模型</strong></p></td>
<td class="confluenceTd" data-local-id="e3d10991-25b9-4fa7-8bf3-12368af035c2"><p>追踪 ZFP 仓位状态</p>
<ul>
<li><p>新增 <code>isZFP</code>字段，标记仓位是否为超高杠杆，用于后续费用、补偿、利润抽成、清算分支</p></li>
<li><p>平仓 / 强平时，调用 ZFP 对应的合约执行路径</p></li>
</ul>
<p>追踪 Guaranteed TP/SL 状态</p>
<ul>
<li><p>需要存储 TP/SL 价格用于触发判断</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="5551e132-8511-4d0c-88ce-a6307c24d602"></td>
</tr>
<tr data-local-id="2d9b74ea-f15e-4172-8115-f0f8847a3b81">
<td class="confluenceTd" data-local-id="c88d645f-d1a6-4b7d-80b6-ae42775c0537"><p><strong>事件处理</strong></p></td>
<td class="confluenceTd" data-local-id="ea0afb2a-9648-4453-9014-82cc250861c9"><ul>
<li><p>从链上事件中提取 ZFP 标记</p></li>
<li><p>从链上事件中提取 Guaranteed SL/TP 状态</p></li>
<li><p>同步到数据库和 Redis</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="b3b068cc-c696-46dd-99a7-2c51605309fd"></td>
</tr>
<tr data-local-id="5a1a896a-a4dd-48ba-8904-e57e0d28436b">
<td class="confluenceTd" data-local-id="ab60455c-4eb2-400d-b3f0-940b6137ce46"><p><strong>清算计算器</strong></p></td>
<td class="confluenceTd" data-local-id="985404e3-1be8-4aaa-84e0-59d70dd25f09"><ul>
<li><p>ZFP 仓位不收fee，清算价格计算公式不同</p></li>
<li><p>Guaranteed TP/SL 仓位使用 TP/SL 价格作为"清算触发价格"</p></li>
<li><p>需要同步更新 Redis 中的清算价格</p></li>
</ul></td>
<td class="confluenceTd" data-local-id="418d1210-b12c-49fe-9f8d-1970aa99c2cf"></td>
</tr>
<tr data-local-id="1ffab553-ad53-4beb-8538-2461b1bfb94a">
<td class="confluenceTd" data-local-id="6740bbfd-7734-4b72-98c4-c2885a68f4b4"><p><strong>清算触发逻辑修改</strong></p></td>
<td class="confluenceTd" data-local-id="9c7c9497-6706-40bf-a016-cee59720d4e8"><ul>
<li><p>Guaranteed TP/SL 仓位：优先触发 TP/SL，不触发清算</p></li>
<li><p>需要监控 TP/SL 价格条件</p></li>
</ul>
<p>清算逻辑需要很大的修改。</p></td>
<td class="confluenceTd" data-local-id="0d16f6ff-2741-4682-9006-59daf9a02d7f"></td>
</tr>
</tbody>
</table>

</div>

</div>
