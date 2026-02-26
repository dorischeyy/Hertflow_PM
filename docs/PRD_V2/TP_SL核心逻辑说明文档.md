# TP/SL核心逻辑说明文档

<div class="Section1">

# <style>[data-colorid=j6wsval9sf]{color:#bf2600} html[data-color-mode=dark] [data-colorid=j6wsval9sf]{color:#ff6640}[data-colorid=emi6h2ft0o]{color:#bf2600} html[data-color-mode=dark] [data-colorid=emi6h2ft0o]{color:#ff6640}[data-colorid=jltott2k8x]{color:#bf2600} html[data-color-mode=dark] [data-colorid=jltott2k8x]{color:#ff6640}[data-colorid=nd4c5alm39]{color:#bf2600} html[data-color-mode=dark] [data-colorid=nd4c5alm39]{color:#ff6640}</style>**一、核心问题列表**

以下问题聚焦四个方面：\
**系统级强制 PnL 限制 → TP/SL 与 Position 的绑定 → 参数合法性更新 → Keeper 行为。**

### **A｜系统级强制 PnL 机制（+2500% TP / –80% SL）**

+2500% TP 为针对**所有仓位**的强制止盈，相当于强平线。-80%SL为**提交止损单**才有的限制，相当于止损价格边界。

1.  **触发方式**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="c9a95b1d-6db9-4135-8e4e-9b64fb9d6f30">
<tbody>
<tr>
<th class="confluenceTh"><p>方案</p></th>
<th class="confluenceTh"><p>描述</p></th>
<th class="confluenceTh"><p><strong>已确认</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><strong>✅ 实时检查当前 PnL → 直接平仓</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>Keeper 每次执行任务时检查 PnL，止损走的 order decrease，而止盈是类似清算式接管</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>无额外订单结构，由keeper进行判断：</p>
<ul>
<li><p><strong>全部仓位：</strong>pnl 2500%，或到达强平线 → 全部强平</p></li>
<li><p><strong>带有止损单的仓位：</strong>按止盈止损线来。<strong>多仓 SL Price = max{ 用户设置，价格边界} ; 空仓 SL Price = min {用户设置，价格边界}</strong> → 执行触发单止损</p></li>
</ul></td>
</tr>
<tr>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><strong>❌ 2：生成隐式系统 TP或SL 订单</strong></p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p>前端提交/为每个 position 写入一个 internal TP order，Keeper 对 order 触发</p></td>
<td class="confluenceTd" data-highlight-colour="#ffffff"><p><strong>SL（TP） Price自动更新确认：</strong> entry/size/collateral 变化 → 系统级 –80% SL price 也会变化。是否每次仓位变化都要同步刷新该边界？ gas消耗是否会过大？<strong>不自动更新并提交，无额外 gas 消耗。前端重新计算并展示更新后价格即可，order里无需展示修改历史。</strong></p></td>
</tr>
</tbody>
</table>

</div>

### **B｜TP/SL 的绑定模型 & 死单清理**

1.  **TP/SL 的绑定方式**

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="6e6d5d99-b66d-405b-a43a-4a55ca2d827d">
<tbody>
<tr>
<th class="confluenceTh"><p>方式</p></th>
<th class="confluenceTh"><p>描述</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p><strong>✅ position id</strong></p></td>
<td class="confluenceTd"><p>一个 position 只能有<strong>一组</strong> TP/SL</p>
<blockquote>
<p>按size比例可挂多个触发单，但此版本不支持</p>
</blockquote></td>
</tr>
<tr>
<td class="confluenceTd"><p><strong>❌ order id</strong></p></td>
<td class="confluenceTd"><p>TP/SL 作为<strong>独立挂单，</strong>不依赖原有仓位是否存在</p></td>
</tr>
</tbody>
</table>

</div>

2.  **Position 存在但 TP/SL 参数非法时的行为**

如修改保证金导致 SL price \< liq price：

- 订单保留，但永远无法触发？

- 系统立即标记无效 / 删除？

- 帮用户重新计算并提交一个合法 TP/SL？

3.  **Position 消失后的 TP/SL死单处理**

当 position 被平掉：

- TP/SL 是否自动取消，即Keeper 是否需要进行清理？

- 是否允许死单长期存在，还是有一个超时限制？

4.  **Keeper 遇到非法触发参数时的默认行为：**

- revert订单继续挂着

- 自动 cancel

- 系统替用户调整到合法边界

### **C｜参数冲突与连锁影响处理**

1.  **仓位参数修改导致 TP/SL 越界时的行为**

修改如下参数时可能导致 TP/SL 不再合法：collateral；entry price（由加减仓引起）；limit order price；liquidation price（保证金修改或加减仓或限价单执行引起）。此时系统对越界的处理逻辑：

- TP/SL 保留但进入不可执行状态？

- 自动 cancel 相关 TP/SL？

- 自动调整 TP/SL 到系统边界？

2.  **连锁更新逻辑**

参数变化会引发链式变化：修改 collateral → entry price 变 → liq price 变 → min SL price 变 → 原 SL 不合法。此时keeper是否：

- 自动连锁更新所有依赖参数？

- 让前端计算后要求用户重新提交？

- 允许不更新并让订单进入失效状态？

# **二、结论**

### **1. GMX设计哲学**

- **用户完全控制：**订单参数由用户决定；更新责任在**用户/前端；**合约不会自动调整任何参数；**autoCancel 是可选的**

- **Keeper 只执行，不决策：**只检查触发条件，不负责更新订单参数，不负责清理死单（autoCancel=false 的情况）

- **合约执行阶段检查：Position 合理性与订单合理性不强耦合，执行阶段再检查。**

### **2. 前端实践**

<div class="table-wrap">

<table class="confluenceTable" data-layout="default" data-local-id="b8ee5741-dacd-4551-8eaf-cb131da518c2">
<tbody>
<tr>
<th class="confluenceTh"><p><strong>逻辑</strong></p></th>
<th class="confluenceTh"><p><strong>前端处理方式</strong></p></th>
<th class="confluenceTh"><p><strong>Keeper处理方式</strong></p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>仓位变化</p></td>
<td class="confluenceTd"><p>检查所有 TP/SL → 计算新的合理边界 → 提示用户更新或自动调用 updateOrder()</p></td>
<td class="confluenceTd"><p>只检查触发条件，不负责更新关联订单参数，配合合约死单清理（仅限减仓的条件单）</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>SL price &lt; liq price</p></td>
<td class="confluenceTd"><p>提醒用户该 SL 可能无法生效</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>autoCancel</p></td>
<td class="confluenceTd"><p>默认开启</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>更新体验</p></td>
<td class="confluenceTd"><p>自动计算合理 TP/SL 并提供一键更新功能</p>
<p><strong>显示警告：</strong></p>
<ol>
<li><p>SL price &lt; liq price 时提示风险</p></li>
<li><p>订单参数与仓位不匹配时提示</p></li>
</ol></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

### **3. TP/SL Price 自动更新与责任范围**

TP/SL 订单为 **完全独立的链上订单**，存储固定的 `triggerPrice`，与 Position 仅通过 \`positionKey\` 逻辑关联。当 Position 参数变化时，订单的 \`triggerPrice\` **保持不变，不自动更新，无额外 gas 消耗** 。

> 这是有意的设计，减少链上计算复杂度

<div class="table-wrap">

|     |           |                                               |
|-----|-----------|-----------------------------------------------|
|     | **角色**  | **责任**                                      |
| 1   | 用户/前端 | 负责检测仓位变化，决定是否更新 TP/SL          |
| 2   | 合约      | 提供 \`updateOrder()\` 接口，允许修改订单参数 |
| 3   | Keeper    | 仅负责执行订单，不负责更新订单参数            |

</div>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
仓位变化（size/collateral/entry）
    ↓
前端检测 TP/SL 参数是否过期或非法
    ↓
计算新的 TP/SL 合理值
    ↓
提示用户更新（或自动更新?或实际不调用合约，只是展示层面重新计算并展示）
    ↓
调 updateOrder()
```

</div>

</div>

### 4. Position 存在但 TP/SL 参数非法时的行为

如修改保证金导致 SL price \< liq price：**订单保留，不删除，不自动调整。**合约不会主动验证 TP/SL 参数的"合法性"。订单不会因时间过长而失效。

<div class="table-wrap">

|                                    |                           |
|------------------------------------|---------------------------|
| 情况                               | GMX 行为                  |
| SL price 已落在清算价之外          | **不会主动调整或删除 SL** |
| 参数不再合理                       | 仍然允许挂单              |
| 触发 SL 时 position 可能已经不存在 | 执行 revert（死单）       |

</div>

**\<场景示例\>**

1.  Position 清算价更新为 \$1050

2.  SL 设置在 \$1000（低于清算价）

3.  当价格跌至 \$1050 → Position 先被清算

4.  如果 **autoCancel=true** → **合约**在清算/用户减仓时**自动取消** SL 订单，keeper不做额外清理

5.  如果 **autoCancel=false** → 订单仍挂着，跌至 \$1000 → SL 被触发 （这里比死单兜底**耗gas** - **多笔**keeper尝试执行时gas，以及**单笔**用户手动取消订单时的gas）

6.  Keeper 执行 → Position 已不存在 ：SL 成为**死单**，执行时被合约revert，长期存在

### 5. Keeper 遇到非法触发参数时的默认行为

GMX分三类：revert，取消以及冻结。keeper根据**错误类型**处理，不会自动调整。关键代码：`OrderHandler._handleOrderError`

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 错误类型 | 处理方式 | 订单状态 |
| `InvalidOrderPrices` | **revert** | 继续挂着，等待触发条件满足 |
| `EmptyPosition` (非市价单) | **revert** | 继续挂着，成为死单 |
| `OrderValidFromTimeNotReached` | **revert** | 继续挂着，等待生效时间 |
| `InvalidPositionMarket` | **cancel** | 订单取消，退还资金 |
| `InvalidCollateralTokenForMarket` | **cancel** | 订单取消，退还资金 |
| `InvalidPositionSizeValues` | **cancel** | 订单取消，退还资金 |
| 市价单执行失败 | **cancel** | 订单取消，退还资金 |
| 其他错误 | **freeze** | 订单冻结，需要 FROZEN_ORDER_KEEPER |

</div>

# **三、订单冲突状态表**

<div class="table-wrap">

|     |
|-----|
|     |
| 1   |
| 2   |
| 3   |
| 4   |
| 5   |
| 6   |
| 7   |
| 8   |
| 9   |
| 10  |
| 11  |
| 12  |
| 13  |
| 14  |

</div>

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="68e9c61b-7bd3-4764-a043-9c2dc76cb709">
<tbody>
<tr>
<th class="confluenceTh"><p>场景编号</p></th>
<th class="confluenceTh"><p>场景描述</p></th>
<th class="confluenceTh"><p>系统行为</p></th>
<th class="confluenceTh"><p>TP/SL 更新逻辑</p></th>
<th class="confluenceTh"><p>仓位合并逻辑</p></th>
</tr>
&#10;<tr>
<td class="confluenceTd"><p>A</p></td>
<td class="confluenceTd"><p>Market | TP/SL</p>
<p>假定Position Id = M<sub>A</sub>；Trigger Order Id = TP/SL<sub>A</sub></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>A1</p></td>
<td class="confluenceTd"><p>A + Market | TP/SL</p></td>
<td class="confluenceTd"><p>合并仓位（size、collateral、entryPrice）重算</p></td>
<td class="confluenceTd"><p>TP/SL<sub>A</sub> 全量删除；提交的新 TP/SL 作为“合并后仓位”的 TP/SL（价格需重新按新 Entry Price 校验）</p></td>
<td class="confluenceTd"><p>Entry Price = 加权平均；Fees 用合并后数值重新参与 TP/SL 公式</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>A2</p></td>
<td class="confluenceTd"><p>A + Limit | TP/SL</p></td>
<td class="confluenceTd"><p>仅生效L<sub>A2</sub>; TP/SL<sub>A2</sub> 处于 inactive</p></td>
<td class="confluenceTd"><p>inactive（不生效、但保存）</p></td>
<td class="confluenceTd"><p>仓位不变</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>A3</p></td>
<td class="confluenceTd"><p>L<sub>A2</sub>成交（限价单）</p></td>
<td class="confluenceTd"><p>合并仓位；激活 TP/SL；按合并后 Entry Price 重新验证 TP/SL 合规性。</p></td>
<td class="confluenceTd"><p>若合规→激活；不合规→取消（提示：超出 TP/SL 合规价格区间）</p></td>
<td class="confluenceTd"><p>Entry Price 按成交价与原仓位加权；Fees 取最新，重新校验 TP/SL<sub>A2</sub></p></td>
</tr>
<tr>
<td class="confluenceTd"><p>A5</p></td>
<td class="confluenceTd"><p>A2 的限价单最终未成交而被取消</p></td>
<td class="confluenceTd"><p>删除限价单，并删除 inactive TP/SL</p></td>
<td class="confluenceTd"><p>全量取消</p></td>
<td class="confluenceTd"><p>无变化</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>B</p></td>
<td class="confluenceTd"><p>Limit L<sub>B</sub>：Position Size = 0，无TP/SL</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>B1</p></td>
<td class="confluenceTd"><p>B + Limit | TP/SL</p></td>
<td class="confluenceTd"><p>两个限价单都存在；第二单的 TP/SL inactive</p></td>
<td class="confluenceTd"><p>inactive，基于L<sub>B1</sub>的 size 和 limit price成交</p></td>
<td class="confluenceTd"><p>多个挂单互不影响</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>B2</p></td>
<td class="confluenceTd"><p>L<sub>B1</sub>成交</p></td>
<td class="confluenceTd"><p>成交创建仓位；TP/SL 激活</p></td>
<td class="confluenceTd"><p>active</p></td>
<td class="confluenceTd"><p>Entry Price = limit price</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>B3</p></td>
<td class="confluenceTd"><p>L<sub>B</sub>接着成交</p></td>
<td class="confluenceTd"><p>合并仓位，Entry Price 重算</p></td>
<td class="confluenceTd"><p>保留已有 TP/SL，但需对 TP/SL 触发价格重新校验；不合规则取消</p></td>
<td class="confluenceTd"><p>若 TP/SL 无法覆盖新的仓位大小，按整体仓位使用相同触发价格</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>C</p></td>
<td class="confluenceTd"><p>Limit L<sub>C</sub>：Position Size = 0，已有TP/SL<sub>C</sub></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>C1</p></td>
<td class="confluenceTd"><p>L<sub>C</sub>全部成交</p></td>
<td class="confluenceTd"><p>仓位完整创建</p></td>
<td class="confluenceTd"><p>active</p></td>
<td class="confluenceTd"><p>Entry Price = 加权</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>C2</p></td>
<td class="confluenceTd"><p>L<sub>C</sub>取消</p></td>
<td class="confluenceTd"><p>对应TP/SL 仍保留</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>E</p></td>
<td class="confluenceTd"><p>复杂冲突：已有仓位 M<sub>E</sub> +仓位带止盈止损TP/SL<sub>ME</sub>+ 限价单L<sub>E</sub> + 限价单带止盈止损 TP/SL<sub>LE</sub></p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>E1</p></td>
<td class="confluenceTd"><p>限价单未成交</p></td>
<td class="confluenceTd"><p>两套 TP/SL 并存：一套 active，一套 inactive。仅已有仓位的 TP/SL 生效</p></td>
<td class="confluenceTd"><p>active: existing; inactive: new</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>E2</p></td>
<td class="confluenceTd"><p>限价单成交后，仓位合并</p></td>
<td class="confluenceTd"><p>两套 TP/SL 冲突，需要合并</p></td>
<td class="confluenceTd"><p>旧 TP/SL 删除；新的 TP/SL 重算后激活</p></td>
<td class="confluenceTd"><p>合并仓位后 TP/SL 必须基于最新 Entry Price 校验</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>E3</p></td>
<td class="confluenceTd"><p>限价单部分成交</p></td>
<td class="confluenceTd"><p>仓位合并部分</p></td>
<td class="confluenceTd"><p>inactive</p></td>
<td class="confluenceTd"><p>等待全部成交才激活</p></td>
</tr>
<tr>
<td class="confluenceTd"><p>E4</p></td>
<td class="confluenceTd"><p>限价单取消</p></td>
<td class="confluenceTd"><p>cancel，inactive TP/SL 移除</p></td>
<td class="confluenceTd"><p>inactive TP/SL 移除，原有active保留</p></td>
<td class="confluenceTd"></td>
</tr>
<tr>
<td class="confluenceTd"><p>E5</p></td>
<td class="confluenceTd"><p>限价单成交时，仓位已被对侧 SL/TP 平掉</p></td>
<td class="confluenceTd"><p>inactive TP/SL 删除</p></td>
<td class="confluenceTd"></td>
<td class="confluenceTd"></td>
</tr>
</tbody>
</table>

</div>

各种持仓组合计算

<div class="table-wrap">

|  |  |  |
|----|----|----|
| **场景** | Entry Price 用哪个？ | TP/SL 的价格校验怎样算？ |
| 无持仓 + 限价单 + TP/SL | Entry = Limit Price | 各 TP/SL 公式的 Entry = Limit Price |
| 有持仓 + 限价单 + TP/SL（未成交） | Entry = 合并后 Entry | TP/SL 需基于“当前持仓”校验 |
| 有持仓 + 限价单成交 | Entry = 合并后 Entry | TP/SL 全部基于新 Entry 计算 |

</div>

</div>
