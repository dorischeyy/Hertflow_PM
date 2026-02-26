# 多Keeper三级优先级执行架构设计

<div class="Section1">

## 概述

本文档描述了一个用于BSC链上perpetual清算和订单执行的多Keeper高可用架构。该架构采用三级优先级模式，实现无共享协调层的故障转移和自动恢复。

## 设计目标

1.  **高可用**: 三级冗余，任意两个keeper宕机系统仍可运行，可独立部署在不同aws region上

2.  **低Gas成本**: 正常情况只有Master执行，避免重复交易

3.  **无共享状态**: 每个keeper完全独立，无需共享Redis/PostgreSQL

4.  **自动恢复**: Master恢复后自动接管，Backup自动退回

5.  **纯链下方案**: 不需要部署新的链上合约

------------------------------------------------------------------------

## 架构设计

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
                              BSC 区块链
                            (唯一共享状态)
                                  ↑
         ┌────────────────────────┼────────────────────────┐
         │                        │                        │
   +-----------+            +-----------+            +-----------+
   | Keeper-A  |            | Keeper-B  |            | Keeper-C  |
   |  (Master) |            | (Backup-1)|            | (Backup-2)|
   |  优先级: 1 |            |  优先级: 2 |            |  优先级: 3 |
   |  延迟: 0s  |            |  延迟: 30s |            |  延迟: 60s |
   +-----------+            +-----------+            +-----------+
   | PostgreSQL|            | PostgreSQL|            | PostgreSQL|
   | Redis     |            | Redis     |            | Redis     |
   | JobQueue  |            | JobQueue  |            | JobQueue  |
   +-----------+            +-----------+            +-----------+
         │                        │                        │
         │ 发现Job                │ 发现Job                │ 发现Job
         │ 立即执行               │ 记录，等30s            │ 记录，等60s
         │                        │ 检查链上状态           │ 检查链上状态
         │                        │ 未执行→接管            │ 未执行→接管
         ↓                        ↓                        ↓
   ┌─────────────────────────────────────────────────────────────┐
   │                         执行流程                             │
   │  T+0:  Keeper-A 发现job，立即执行                            │
   │  T+30: Keeper-B 检查链上状态，如果未执行→接管执行              │
   │  T+60: Keeper-C 检查链上状态，如果未执行→接管执行              │
   └─────────────────────────────────────────────────────────────┘
```

</div>

</div>

------------------------------------------------------------------------

## 核心设计原则

### 1. 无分区，全量监控

所有keeper都监控所有job，只是执行时机不同：

- Keeper-A (Master): 立即执行

- Keeper-B (Backup-1): 等待30秒后检查并执行

- Keeper-C (Backup-2): 等待60秒后检查并执行

### 2. 三级延迟执行

<div class="table-wrap">

|              |        |          |                                    |
|--------------|--------|----------|------------------------------------|
| Keeper       | 优先级 | 延迟时间 | 行为                               |
| A (Master)   | 1      | 0s       | 发现job立即执行                    |
| B (Backup-1) | 2      | 30s      | 发现job后等30s，检查链上状态再决定 |
| C (Backup-2) | 3      | 60s      | 发现job后等60s，检查链上状态再决定 |

</div>

### 3. 链上状态验证

所有备份keeper执行前都检查链上状态：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
func shouldExecuteJob(job *Job, myDelay time.Duration) bool {
    // 1. 检查是否已过延迟时间
    if time.Since(job.DiscoveredAt) < myDelay {
        return false
    }

    // 2. 检查链上状态 - job是否仍需执行
    return checkJobStillPendingOnChain(job)
}
```

</div>

</div>

------------------------------------------------------------------------

## Backup Keeper如何检测Job已被执行

### 核心机制：本地事件同步

每个keeper都有**独立的事件同步流程**，通过同步链上事件来更新本地状态：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
┌─────────────────────────────────────────────────────────────────────────────┐
│                              BSC 区块链                                      │
│                                                                             │
│   Master TX确认 → emit PositionDecrease/OrderExecuted 事件                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      │ 区块确认后
                                      ▼
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
  ┌───────────┐                 ┌───────────┐                 ┌───────────┐
  │ Keeper-A  │                 │ Keeper-B  │                 │ Keeper-C  │
  │FilterScanner               │FilterScanner               │FilterScanner
  └─────┬─────┘                 └─────┬─────┘                 └─────┬─────┘
        │                             │                             │
        ▼                             ▼                             ▼
  ┌───────────┐                 ┌───────────┐                 ┌───────────┐
  │   Kafka   │                 │   Kafka   │                 │   Kafka   │
  └─────┬─────┘                 └─────┬─────┘                 └─────┬─────┘
        │                             │                             │
        ▼                             ▼                             ▼
  ┌───────────┐                 ┌───────────┐                 ┌───────────┐
  │  StateVM  │                 │  StateVM  │                 │  StateVM  │
  │ 处理事件   │                 │ 处理事件   │                 │ 处理事件   │
  └─────┬─────┘                 └─────┬─────┘                 └─────┬─────┘
        │                             │                             │
        ▼                             ▼                             ▼
  ┌───────────┐                 ┌───────────┐                 ┌───────────┐
  │PostgreSQL │                 │PostgreSQL │                 │PostgreSQL │
  │Position:  │                 │Position:  │                 │Position:  │
  │Status=    │                 │Status=    │                 │Status=    │
  │Closed     │                 │Closed     │                 │Closed     │
  └───────────┘                 └───────────┘                 └───────────┘
                                      ↑
                                      │
                              Backup-1 在延迟到期后
                              查询本地 PostgreSQL
                              发现 Status=Closed
                              → Job已执行，跳过
```

</div>

</div>

### 详细时序

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
时间    Master执行            链上事件                 Backup-1同步             Backup-1决策
────────────────────────────────────────────────────────────────────────────────────────────────
T+0     发现Position P        Position存在             同步Position存在
        (可清算)                                       Status=Active

T+0                                                                             P加入队列
                                                                                等待30秒

T+1     提交清算TX

T+3     TX确认                PositionDecrease
                              事件emit到区块

T+5                           区块被确认               FilterScanner扫描
                                                       发现PositionDecrease
                                                       ↓
                                                       StateVM处理事件
                                                       ↓
                                                       PostgreSQL更新:
                                                       P.Status = Closed

T+30                                                                            延迟到期
                                                                                查询本地PostgreSQL
                                                                                P.Status == Closed
                                                                                ↓
                                                                                已执行！
                                                                                从队列移除
```

</div>

</div>

### 代码实现

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// Backup keeper检查job是否仍需执行
// 实际是查询本地PostgreSQL（已从链上同步最新状态）

func (pe *PriorityExecutor) CheckPositionPending(ctx context.Context, key string) bool {
    // 查询本地PostgreSQL（不是RPC直接查链）
    position, err := bsc_position_state.GetBSCPosition(pe.pgsqlDriver.DB, key)
    if err != nil {
        // Position不存在或查询失败，认为已处理
        pe.logger.Debug("Position不存在，认为已处理", zap.String("key", key))
        return false
    }

    // 检查状态：只有Active的position才需要清算
    isActive := position.Status == bsc_position_state.PositionActive

    pe.logger.Debug("检查Position状态",
        zap.String("key", key),
        zap.String("status", string(position.Status)),
        zap.Bool("needsExecution", isActive))

    return isActive
}

func (pe *PriorityExecutor) CheckOrderPending(ctx context.Context, key string) bool {
    order, err := bsc_order_state.GetBSCOrder(pe.pgsqlDriver.DB, key)
    if err != nil {
        return false
    }

    // 只有Created或Updated状态的order才需要执行
    // Executed/Cancelled/Frozen 状态表示已处理
    isPending := order.Status == bsc_order_state.OrderCreated ||
                 order.Status == bsc_order_state.OrderUpdated

    return isPending
}
```

</div>

</div>

### 状态转换对照

**Position状态**: \| 链上事件 \| PostgreSQL状态变化 \| Backup行为 \| \|----------\|-------------------\|------------\| \| PositionIncrease \| Active \| 需要监控 \| \| PositionDecrease (全部) \| Closed \| 跳过，已清算 \| \| InsolventClose \| Closed \| 跳过，已清算 \|

**Order状态**: \| 链上事件 \| PostgreSQL状态变化 \| Backup行为 \| \|----------\|-------------------\|------------\| \| OrderCreated \| Created \| 需要监控 \| \| OrderUpdated \| Updated \| 需要监控 \| \| OrderExecuted \| Executed \| 跳过，已执行 \| \| OrderCancelled \| Cancelled \| 跳过，已取消 \| \| OrderFrozen \| Frozen \| 跳过，需FROZEN_ORDER_KEEPER处理 \|

### 时间分析

<div class="table-wrap">

|                            |          |                  |
|----------------------------|----------|------------------|
| 阶段                       | 耗时     | 说明             |
| TX提交到区块确认           | ~3秒     | BSC出块时间约3秒 |
| 事件被FilterScanner扫描    | ~2秒     | 扫描间隔配置     |
| StateVM处理+PostgreSQL写入 | ~1秒     | 本地处理         |
| **总计**                   | **~6秒** | 远小于30秒延迟   |

</div>

**结论**: 30秒延迟设计有充足的安全缓冲（~24秒余量），确保Backup检查时本地PostgreSQL已经同步了最新的链上状态。

### 为什么不直接RPC查链？

<div class="table-wrap">

|  |  |  |
|----|----|----|
| 方案 | 优点 | 缺点 |
| 查本地PostgreSQL | 快速、无RPC成本、无限流风险 | 有几秒同步延迟 |
| 直接RPC查链 | 实时数据 | RPC成本高、可能被限流、增加复杂性 |

</div>

**选择本地PostgreSQL的原因**:

1.  30秒延迟已覆盖同步延迟

2.  避免额外RPC调用成本

3.  复用现有的事件同步基础设施

4.  查询性能更好（本地数据库 vs 远程RPC）

------------------------------------------------------------------------

## 故障转移场景

### 场景1: 正常执行（Master成功）

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
时间    Keeper-A (Master)     Keeper-B (Backup-1)    Keeper-C (Backup-2)    链上状态
─────────────────────────────────────────────────────────────────────────────────────
T+0     发现job P              发现job P               发现job P              待处理
        立即执行TX             记录到队列(等30s)        记录到队列(等60s)

T+3     TX确认                                                               已执行

T+30                           延迟到期
                               检查链上: 已执行!
                               从队列移除

T+60                                                   延迟到期
                                                       检查链上: 已执行!
                                                       从队列移除
```

</div>

</div>

### 场景2: Master故障，Backup-1接管

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
时间    Keeper-A (宕机)       Keeper-B (Backup-1)    Keeper-C (Backup-2)    链上状态
─────────────────────────────────────────────────────────────────────────────────────
T+0     [崩溃]                 发现job P               发现job P              待处理
                               记录到队列(等30s)        记录到队列(等60s)

T+30                           延迟到期
                               检查链上: 仍待处理!
                               执行TX

T+33                           TX确认                                        已执行

T+60                                                   延迟到期
                                                       检查链上: 已执行!
                                                       从队列移除
```

</div>

</div>

### 场景3: Master和Backup-1都故障，Backup-2接管

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
时间    Keeper-A (宕机)       Keeper-B (宕机)        Keeper-C (Backup-2)    链上状态
─────────────────────────────────────────────────────────────────────────────────────
T+0     [崩溃]                 [崩溃]                  发现job P              待处理
                                                       记录到队列(等60s)

T+30                           (无响应)

T+60                                                   延迟到期
                                                       检查链上: 仍待处理!
                                                       执行TX

T+63                                                   TX确认                已执行
```

</div>

</div>

------------------------------------------------------------------------

## Master恢复场景详细分析

### 场景：Keeper A挂了2分钟后恢复

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
时间线:
T+0      Keeper-A 宕机
T+0      Keeper-B/C 发现新job，加入队列
T+30     Keeper-B 延迟到期，开始接管执行
T+60     Keeper-C 延迟到期（如果B也失败）
T+120    Keeper-A 恢复
```

</div>

</div>

### 问题分析

**问题1: A恢复后立即执行，可能与B冲突**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
T+115   Job X 出现
T+115   B 发现 Job X，加入队列(等30秒到T+145执行)
T+120   A 恢复，发现 Job X，立即执行
T+123   A 执行成功
T+145   B 延迟到期，检查链上状态，发现已执行，跳过
```

</div>

</div>

✅ 这种情况OK - B会检查链上状态

**问题2: A恢复时B正在执行中**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
T+100   Job Y 出现
T+100   B 发现 Job Y，加入队列(等30秒到T+130执行)
T+120   A 恢复，发现 Job Y，立即提交TX
T+130   B 延迟到期，也提交TX
T+133   A 的TX先确认，Y已执行
T+135   B 的TX失败（已执行）
```

</div>

</div>

✅ 这种情况OK - 链会拒绝第二个TX

**问题3: A和B几乎同时提交TX**

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
T+100   Job Z 出现
T+100   B 发现 Job Z，加入队列
T+129   A 恢复
T+129.5 A 发现 Job Z，准备执行
T+130   B 延迟到期，检查链上: Z仍待处理
T+130.1 A 提交TX
T+130.2 B 提交TX
T+133   两个TX竞争，一个成功一个失败
```

</div>

</div>

✅ 这种情况OK - 链自动仲裁，只有一个成功

### 优化方案：恢复缓冲期

虽然上述场景都能正确处理，但为了**减少不必要的竞态和失败TX**，建议添加**恢复缓冲期**：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
type PriorityExecutor struct {
    // ... 其他字段 ...

    // 恢复缓冲期
    startupTime       time.Time      // 启动时间
    recoveryBuffer    time.Duration  // 恢复缓冲期（建议30秒）
    isInRecoveryMode  bool           // 是否在恢复模式
}

func (pe *PriorityExecutor) Start() {
    pe.startupTime = time.Now()
    pe.isInRecoveryMode = true

    // 恢复缓冲期结束后切换到正常模式
    go func() {
        time.Sleep(pe.recoveryBuffer)
        pe.isInRecoveryMode = false
        pe.logger.Info("恢复缓冲期结束，切换到正常模式")
    }()
}

func (pe *PriorityExecutor) ShouldExecuteImmediately() bool {
    if pe.priority != 1 {
        return false  // 只有Master才能立即执行
    }

    // 在恢复缓冲期内，Master也要等待
    if pe.isInRecoveryMode {
        return false
    }

    return true
}
```

</div>

</div>

### 带恢复缓冲期的完整时序

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
场景：Keeper A挂了2分钟后恢复（带30秒恢复缓冲期）

时间    Keeper-A            Keeper-B            Keeper-C          链上状态
────────────────────────────────────────────────────────────────────────────
T+0     [宕机]

T+10                        发现Job X            发现Job X          待处理
                            加入队列(T+40执行)    加入队列(T+70执行)

T+40                        延迟到期
                            检查链上: 待处理
                            执行TX

T+43                        TX确认                                  已执行

T+70                                             延迟到期
                                                 检查链上: 已执行
                                                 跳过

T+100                       发现Job Y            发现Job Y          待处理
                            加入队列(T+130执行)   加入队列(T+160执行)

T+120   [恢复]
        进入恢复缓冲期
        (30秒内不立即执行)

T+125   发现Job Y
        恢复模式中
        加入队列(等30秒)

T+130                       延迟到期
                            检查链上: 待处理
                            执行TX

T+133                       TX确认                                  已执行

T+150   恢复缓冲期结束
        切换到正常模式

T+155                       发现Job Z            发现Job Z          待处理
                            加入队列(T+185执行)   加入队列(T+215执行)

T+155   发现Job Z
        正常模式，立即执行

T+158   TX确认                                                      已执行

T+185                       延迟到期
                            检查链上: 已执行
                            跳过
```

</div>

</div>

### 恢复缓冲期的好处

1.  **避免竞态**: A恢复后等30秒，让B完成正在处理的job

2.  **减少失败TX**: 不会在B正在执行时抢着执行

3.  **平滑过渡**: 给系统时间稳定

4.  **Gas节省**: 减少重复提交失败的TX

------------------------------------------------------------------------

## 边界情况处理

### 竞态条件1: Master恢复时刚好Backup-1也执行

**场景**: Master在T+29恢复并执行，Backup-1在T+30也触发执行

**解决方案**: 链自动处理

- 第一个TX成功，job被执行

- 第二个TX失败（已执行）

- 两个keeper都从链上事件同步状态，清理本地队列

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 执行失败后检查是否被其他keeper处理
if err != nil {
    if !checkJobStillPendingOnChain(job.Key) {
        // 已被其他keeper处理，从队列移除
        jobQueue.Remove(job.Key)
        cooldownMgr.RemoveCooldown(job.Key)
        return
    }
    // 真正的失败，保持cooldown，下一级keeper会接管
}
```

</div>

</div>

### 竞态条件2: Backup-1和Backup-2同时尝试执行

**场景**: Backup-1在T+30执行但很慢，Backup-2在T+60也尝试执行

**解决方案**:

- Backup-2在执行前检查链上状态

- 如果Backup-1的TX还在pending，链上状态仍是"待处理"

- Backup-2也会提交TX，但只有一个成功

### Job发现时间不一致

**场景**: 三个keeper发现同一job的时间不同（网络延迟）

**解决方案**:

- 每个keeper独立记录发现时间

- 延迟计算基于本地发现时间

- 即使有几秒差异，不影响整体逻辑

- 链上状态检查保证最终一致性

------------------------------------------------------------------------

## 完整状态机

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
                                    ┌─────────────────┐
                                    │   Keeper 启动   │
                                    └────────┬────────┘
                                             │
                        ┌────────────────────┼────────────────────┐
                        │                    │                    │
                        ▼                    ▼                    ▼
              ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
              │   Priority = 1   │  │   Priority = 2   │  │   Priority = 3   │
              │     (Master)     │  │   (Backup-1)     │  │   (Backup-2)     │
              └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
                       │                    │                    │
                       ▼                    │                    │
              ┌─────────────────┐           │                    │
              │  恢复缓冲期模式  │           │                    │
              │  (30秒内等待)   │           │                    │
              └────────┬────────┘           │                    │
                       │                    │                    │
                       │ 30秒后             │                    │
                       ▼                    ▼                    ▼
              ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
              │   正常执行模式   │  │   延迟执行模式   │  │   延迟执行模式   │
              │   (立即执行)    │  │   (等30秒)      │  │   (等60秒)      │
              └────────┬────────┘  └────────┬────────┘  └────────┬────────┘
                       │                    │                    │
                       ▼                    ▼                    ▼
              ┌─────────────────────────────────────────────────────────────┐
              │                      发现可执行Job                           │
              └─────────────────────────────┬───────────────────────────────┘
                                            │
                        ┌───────────────────┼───────────────────┐
                        │                   │                   │
              Priority=1且正常模式    Priority=2          Priority=3
                        │                   │                   │
                        ▼                   ▼                   ▼
              ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
              │    立即执行     │  │  加入队列       │  │  加入队列       │
              │    提交TX       │  │  等待30秒       │  │  等待60秒       │
              └─────────────────┘  └────────┬────────┘  └────────┬────────┘
                                            │                    │
                                            ▼                    ▼
                                   ┌─────────────────┐  ┌─────────────────┐
                                   │ 延迟到期        │  │ 延迟到期        │
                                   │ 检查链上状态    │  │ 检查链上状态    │
                                   └────────┬────────┘  └────────┬────────┘
                                            │                    │
                              ┌─────────────┴─────────────┐      │
                              │                           │      │
                         已执行                        待处理     │
                              │                           │      │
                              ▼                           ▼      ▼
                     ┌─────────────┐             ┌─────────────────┐
                     │  从队列移除  │             │    执行TX       │
                     └─────────────┘             └─────────────────┘
```

</div>

</div>

------------------------------------------------------------------------

## 配置设计

### 配置结构

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
type PriorityKeeperEnv struct {
    Enabled           bool   `toml:"enabled"`

    // 优先级: 1=Master, 2=Backup-1, 3=Backup-2
    Priority          int    `toml:"priority"`

    // 执行延迟（秒）
    // Master: 0, Backup-1: 30, Backup-2: 60
    ExecutionDelay    int    `toml:"execution_delay"`

    // 恢复缓冲期（秒）
    // Master重启后等待此时间再恢复立即执行模式
    RecoveryBuffer    int    `toml:"recovery_buffer"`

    // Job队列清理间隔（秒）
    QueueCleanupInterval int `toml:"queue_cleanup_interval"`

    // Job最大保留时间（秒）
    JobMaxAge         int    `toml:"job_max_age"`
}
```

</div>

</div>

### 3-Keeper集群配置示例

**Keeper-A (Master) - server.toml**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
[PriorityKeeperEnv]
enabled = true
priority = 1                    # Master - 优先级最高
execution_delay = 0             # 立即执行
recovery_buffer = 30            # 恢复缓冲期30秒
queue_cleanup_interval = 60     # 队列清理间隔（秒）
job_max_age = 300               # Job最大保留时间（秒）
```

</div>

</div>

**Keeper-B (Backup-1) - server.toml**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
[PriorityKeeperEnv]
enabled = true
priority = 2                    # Backup-1 - 第二优先级
execution_delay = 30            # 等待30秒后执行
recovery_buffer = 0             # Backup不需要恢复缓冲期
queue_cleanup_interval = 60
job_max_age = 300
```

</div>

</div>

**Keeper-C (Backup-2) - server.toml**:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
[PriorityKeeperEnv]
enabled = true
priority = 3                    # Backup-2 - 第三优先级
execution_delay = 60            # 等待60秒后执行
recovery_buffer = 0             # Backup不需要恢复缓冲期
queue_cleanup_interval = 60
job_max_age = 300
```

</div>

</div>

------------------------------------------------------------------------

## 核心代码结构

### 1. JobQueue

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// executor_app/executor/job_queue.go

type JobType string
const (
    JobTypeLiquidation JobType = "liquidation"
    JobTypeOrder       JobType = "order"
    JobTypeDeposit     JobType = "deposit"
    JobTypeWithdrawal  JobType = "withdrawal"
    // ... 其他类型
)

type Job struct {
    Key           string      // position key 或 order key
    Type          JobType
    DiscoveredAt  time.Time   // 本keeper发现此job的时间
    ExecuteAfter  time.Time   // 延迟后的执行时间
    Data          interface{} // job相关数据（position/order信息）
}

type JobQueue struct {
    mu             sync.RWMutex
    jobs           map[string]*Job
    executionDelay time.Duration
    maxAge         time.Duration
    logger         *zap.Logger
}

func NewJobQueue(executionDelay, maxAge time.Duration, logger *zap.Logger) *JobQueue

// 添加job到队列
func (q *JobQueue) Add(key string, jobType JobType, data interface{})

// 获取已到期且待执行的jobs
func (q *JobQueue) GetReadyJobs() []*Job

// 从队列移除job
func (q *JobQueue) Remove(key string)

// 检查job是否在队列中
func (q *JobQueue) Exists(key string) bool

// 清理过期的jobs
func (q *JobQueue) Cleanup()

// 启动清理goroutine
func (q *JobQueue) StartCleanupLoop(ctx context.Context, interval time.Duration)
```

</div>

</div>

### 2. PriorityExecutor

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// executor_app/executor/priority_executor.go

type PriorityExecutor struct {
    priority         int
    executionDelay   time.Duration
    recoveryBuffer   time.Duration
    jobQueue         *JobQueue
    pgsqlDriver      *pgsql.PgsqlDriver
    logger           *zap.Logger

    // 恢复模式
    startupTime      time.Time
    isInRecoveryMode bool
    mu               sync.RWMutex
}

func NewPriorityExecutor(cfg *PriorityKeeperEnv, pgsql *pgsql.PgsqlDriver, logger *zap.Logger) *PriorityExecutor

// 启动执行器（进入恢复模式）
func (pe *PriorityExecutor) Start()

// 判断是否应该立即执行
func (pe *PriorityExecutor) ShouldExecuteImmediately() bool

// Master直接执行，Backup添加到队列
func (pe *PriorityExecutor) HandleJob(key string, jobType JobType, data interface{}, executeFunc func())

// 处理队列中已到期的jobs
func (pe *PriorityExecutor) ProcessReadyJobs(ctx context.Context, checkPending func(string, JobType) bool, execute func(*Job))

// 检查Position是否仍待处理
func (pe *PriorityExecutor) CheckPositionPending(ctx context.Context, key string) bool

// 检查Order是否仍待处理
func (pe *PriorityExecutor) CheckOrderPending(ctx context.Context, key string) bool
```

</div>

</div>

### 3. Trigger修改模式

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// executor_app/executor/liquidation_trigger.go

func (e *Executor) checkAndExecuteLiquidations(ctx context.Context) {
    // ... 获取价格和可清算positions ...

    for _, pos := range positions {
        if e.PriorityEnabled {
            if e.PriorityExecutor.ShouldExecuteImmediately() {
                // Master正常模式：立即执行
                e.executeLiquidation(ctx, &pos, priceData)
            } else {
                // Master恢复模式或Backup：加入队列
                e.PriorityExecutor.jobQueue.Add(pos.PositionKey, JobTypeLiquidation, &pos)
            }
        } else {
            // 单keeper模式
            e.executeLiquidation(ctx, &pos, priceData)
        }
    }

    // 处理队列中已到期的jobs
    if e.PriorityEnabled {
        e.processBackupJobs(ctx)
    }
}
```

</div>

</div>

------------------------------------------------------------------------

## Gas成本对比

### 当前模型（乐观执行，3个keeper都执行）

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
假设每天1000次清算：
- 成功交易: 1000次 × 0.001 BNB = 1.0 BNB
- 失败交易: 2000次 × 0.0003 BNB = 0.6 BNB (revert仍消耗gas)
- 总计: ~1.6 BNB/天
```

</div>

</div>

### 优先级模型（只有一个keeper执行）

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
假设每天1000次清算，99%由Master执行，1%故障转移：
- Master成功: 990次 × 0.001 BNB = 0.99 BNB
- Backup接管: 10次 × 0.001 BNB = 0.01 BNB
- 偶尔竞态失败: ~5次 × 0.0003 BNB = 0.0015 BNB
- 总计: ~1.0 BNB/天
- 节省: 37.5%
```

</div>

</div>

------------------------------------------------------------------------

## 实现步骤

### 第一阶段: 核心框架

1.  添加 `PriorityKeeperEnv` 配置结构到 `config/config.go`

2.  实现 `JobQueue` (`executor_app/executor/job_queue.go`)

3.  实现 `PriorityExecutor` (`executor_app/executor/priority_executor.go`)

4.  修改 `Executor` 初始化 (`executor_app/executor/executor.go`)

### 第二阶段: Trigger改造

5.  修改 `liquidation_trigger.go` - 添加优先级逻辑

6.  修改 `order_trigger.go` - 添加优先级逻辑

7.  修改 `order_request_trigger.go` - 添加优先级逻辑

8.  修改其他trigger文件 (deposit, withdrawal, adl, shift, glv等)

### 第三阶段: 测试

9.  单元测试: JobQueue、PriorityExecutor

10. 集成测试: 模拟多keeper场景

11. E2E测试: 故障转移验证

------------------------------------------------------------------------

## 关键文件路径

<div class="table-wrap">

|                                                  |                     |
|--------------------------------------------------|---------------------|
| 文件                                             | 作用                |
| `config/config.go`                               | 配置结构定义        |
| `executor_app/executor/executor.go`              | Executor初始化      |
| `executor_app/executor/job_queue.go`             | Job队列管理 (新增)  |
| `executor_app/executor/priority_executor.go`     | 优先级执行器 (新增) |
| `executor_app/executor/liquidation_trigger.go`   | 清算触发            |
| `executor_app/executor/order_trigger.go`         | 订单触发            |
| `executor_app/executor/order_request_trigger.go` | 市价单触发          |
| `executor_app/executor/cooldown_manager.go`      | Cooldown模式参考    |
| `core_bsc/model/bsc_position_state/`             | Position状态查询    |
| `core_bsc/model/bsc_order_state/`                | Order状态查询       |

</div>

------------------------------------------------------------------------

## 注意事项

### 1. 内存队列设计

- 使用内存队列，keeper重启后队列丢失

- 不影响可用性：其他keeper会继续监控并接管

- 实现简单，无额外依赖

### 2. 价格数据新鲜度

Backup keeper执行时可能价格已变化，需要：

- 重新从数据库获取最新价格

- 重新验证触发条件是否仍然满足

### 3. 监控和告警

建议添加以下监控指标：

- 每个keeper的job执行次数

- 故障转移次数（接管执行次数）

- 队列长度

- 执行延迟

- 恢复缓冲期状态

------------------------------------------------------------------------

## 总结

### 架构优势

1.  **简单**: 无分区，所有keeper监控所有job

2.  **高可用**: 三级冗余（Master → Backup-1 → Backup-2）

3.  **低Gas**: 正常情况只有Master执行

4.  **无协调**: 纯链下方案，无共享状态

5.  **优雅恢复**: Master恢复后有缓冲期，避免与Backup冲突

### 故障转移时间

- Master宕机 → 30秒后Backup-1接管

- Master+Backup-1都宕机 → 60秒后Backup-2接管

- Master恢复 → 30秒缓冲期后恢复正常执行

- 最坏情况：60秒内系统恢复执行能力

### 确认的参数

<div class="table-wrap">

|              |        |                      |
|--------------|--------|----------------------|
| 参数         | 值     | 说明                 |
| Backup-1延迟 | 30秒   | Master超时后接管     |
| Backup-2延迟 | 60秒   | Backup-1也超时后接管 |
| 恢复缓冲期   | 30秒   | Master重启后等待时间 |
| 队列持久化   | 不需要 | 使用内存队列         |

</div>

</div>
