# GMX V2 Oracle 合约

<div class="Section1">

<style type="text/css">/**/
div.rbtoc1772270895239 {padding: 0px;}
div.rbtoc1772270895239 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270895239 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270895239">

- [1. Oracle Modifier](#GMXV2Oracle合约-1.OracleModifier)
- [2. Oracle 合约](#GMXV2Oracle合约-2.Oracle合约)

</div>

## 1. Oracle Modifier

GMX 合约适用 modifier 语法来配置价格，也就是说 keeper 需要在执行订单的时候 post price，然后会触发 modifier 逻辑，让 post 上来的价格在本次 tx 内可见，结束执行后，会清除掉。具体见:

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/oracle/OracleModule.sol#L26C1-L32C6" class="external-link" rel="nofollow">OracleModule.withOraclePrices</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
modifier withOraclePrices(
    OracleUtils.SetPricesParams memory params
) {
    oracle.setPrices(params);
    _;
    oracle.clearAllPrices();
}
```

</div>

</div>

------------------------------------------------------------------------

## 2. Oracle 合约

这里指的是上面 modifier 中，`oracle.setPrices(params)`中调用的 oracle：<a href="https://github.com/gmx-io/gmx-synthetics/blob/v2.2/contracts/oracle/Oracle.sol" class="external-link" rel="nofollow">Oracle.sol</a>

其中 `setPrices`逻辑很简单：就是校验价格有效后就设置进去让本次执行可见，然后执行结束完毕就 clear：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function setPrices(
    OracleUtils.SetPricesParams memory params
) external onlyController {
    OracleUtils.ValidatedPrice[] memory prices = _validatePrices(params, false);

    _setPrices(prices);
}
```

</div>

</div>

关注 `_validatePrices` 逻辑如何校验的价格：<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/oracle/Oracle.sol#L232C5-L328C6" class="external-link" rel="nofollow">Oracle._validatePrices</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
for (uint256 i; i < params.tokens.length; i++) {
    address _provider = params.providers[i];
    IOracleProvider provider = IOracleProvider(_provider);

    // ...

    bytes memory data = params.data[i];

    // 调用了 provider 去获取价格，获取出来的就已经是 validated 了
    OracleUtils.ValidatedPrice memory validatedPrice = provider.getOraclePrice(
        token,
        data
    );

    // ...
}
```

</div>

</div>

可以看到底层是调用了 provider 去获取价格，显然 provider 可以有很多种，这里我们随机选取一种 `GmOracleProvider` 来看他如何实现：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getOraclePrice(
    address token,
    bytes memory data
) external view returns (OracleUtils.ValidatedPrice memory) {
    // 这里做的反序列化
    GmOracleUtils.Report memory report = abi.decode(data, (GmOracleUtils.Report));
    address[] memory signers = _getSigners(report.signerInfo);

    // ...

    bytes32 salt = _getSalt();

    for (uint256 i = 0; i < signers.length; i++) {
        uint256 minPrice = report.minPrices[i];
        uint256 maxPrice = report.maxPrices[i];

        if (minPrice > maxPrice) {
            revert Errors.InvalidGmSignerMinMaxPrice(minPrice, maxPrice);
        }
        // 这里做了验签
        GmOracleUtils.validateSigner(
            salt,
            report,
            token,
            minPrice,
            maxPrice,
            tokenOracleType,
            report.signatures[i], // 带上来的价格必须是签名价格
            signers[i]            // 配置的 signer
        );
    }
        
    // ...

    return OracleUtils.ValidatedPrice({
        token: token,
        min: medianMinPrice,
        max: medianMaxPrice,
        timestamp: report.oracleTimestamp,
        provider: address(this)
    });
}
```

</div>

</div>

到这里逻辑比较清晰了，其实就和 v1 的 oracle 逻辑差不多，签名价格在合约内进行验签。

如果使用 Chainlink 作为价格来源，则不需要你 post price，而是它会从链上直接读取，因此也就不需要验证签名:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getPriceFeedPrice(DataStore dataStore, address token) internal view returns (bool, uint256) {
    // 安全性来自这里，通过 datastore 配置死信任的 chainlink 价格合约地址
    // 只要地址正确配置，也就不需要验签
    address priceFeedAddress = dataStore.getAddress(Keys.priceFeedKey(token));
    if (priceFeedAddress == address(0)) {
        return (false, 0);
    }

    IPriceFeed priceFeed = IPriceFeed(priceFeedAddress);

    (
        /* uint80 roundID */,
        int256 _price,
        /* uint256 startedAt */,
        uint256 timestamp,
        /* uint80 answeredInRound */
    ) = priceFeed.latestRoundData();

    // ...
}
```

</div>

</div>

至于别的 provider 这里不展开说明，不同的 provider 主要实现了不同的数据处理，因为每个 provider 用了不同的数据格式来上传价格，并且用了不同的精度标准。底层安全性来源，通用的方式上面也列举了两种：

- 签名验证

- 地址配置

</div>
