# 合约交易引入 Avantis 机制

<div class="Section1">

> <style>[data-colorid=ovx04idtdn]{color:#ff991f} html[data-color-mode=dark] [data-colorid=ovx04idtdn]{color:#e07a00}</style>
>
> PRD: <a href="https://hertzflow.atlassian.net/wiki/spaces/H/pages/55312675/Trade+Page+_PRD" data-linked-resource-id="55312675" data-linked-resource-version="8" data-linked-resource-type="page">Trade Page 新机制引入</a>

## 1. 新增仓位模式

为避免影响原逻辑，新增配套接口，高杠杆仓位走新接口。接口逻辑与原有接口基本保持一致，只做部分特殊逻辑改造。

- 创建订单部分：createOrder → createZFPOrder

- 订单实体部分：新增 order.zfp = true

- 执行订单部分：复用已有的 executeOrder 接口，内部逻辑分流。（本身就是一个 execute by order key 的逻辑）。

  - IncreaseOrderUtils.processOrder → IncreaseOrderUtils.processZFPOrder

    - ~~IncreasePositionUtils.increasePosition → IncreasePositionUtils.increaseZFPPosition~~

  - DecreaseOrderUtils.processOrder → DecreaseOrderUtils.processZFPOrder

    - ~~DecreasePositionUtils.decreasePosition → DecreasePositionUtils.decreaseZFPPosition~~

- 仓位 id 生成规则更换，与原有仓位进行显式区分，避免仓位合并：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getPositionKey(address _account, address _market, address _collateralToken, bool _isLong) internal pure returns (bytes32) {
    bytes32 _key = keccak256(abi.encode(_account, _market, _collateralToken, _isLong));

    return _key;
}

// 结尾多拼接一个 ZFP 字符串
function getZFPPositionKey(address _account, address _market, address _collateralToken, bool _isLong) internal pure returns (bytes32) {
    bytes32 _key = keccak256(abi.encode(_account, _market, _collateralToken, _isLong, "ZFP"));

    return _key;
}
```

</div>

</div>

- 配置项部分：

  - 最大杠杆限制调整，PRD 指出 Normal 仓位杠杆部分为 1.1x - Max Lev Normal，ZFP 的杠杆则为另一个区间。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
minCollateralFactor: percentageToFloat("0.833%"), // 120x leverage
minCollateralFactorForLiquidation: percentageToFloat("0.833%"), // 120x leverage
// 新增下面的 ZFP 专属设置
minZFPCollateralFactor: percentageToFloat("0.5%"), // max 200x leverage
maxZFPCollateralFactor: percentageToFloat("0.8%"), // min 125x leverage
```

</div>

</div>

- 盈利抽成部分：

  - 判断 PnL 与保证金的比例，进行分段函数计算，每一段都对应一个 factor 配置（即 y = kx+b 的 k 和 b，还有x轴的断点位置）。

## 2. OI 重平衡损失补偿

开仓的时候，额外记录这个仓位是否属于弱势仓位。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// get position
position.setIsWeakSide(dataStore.getBool(
    keccak256(abi.encode(key, IS_WEAK_SIDE))
));

// set position
dataStore.setBool(
    keccak256(abi.encode(key, IS_WEAK_SIDE)),
    position.isWeakSide()
);
```

</div>

</div>

<span colorid="ovx04idtdn">减仓时，将 keeper 费用转给用户，而非给 keeper</span>。

ExecuteOrderUtils.executeOrder 里面，判断 order 的类型为减仓的时候，把 executionFee 设置为 0，即可实现执行费全退款（原生逻辑就是先支付，有剩余则 refund，这里设置为 0 就全退了）。

</div>
