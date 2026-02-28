# GLV Token Price 代码解读

<div class="Section1">

<a href="https://github.com/gmx-io/gmx-synthetics/blob/ee721b7e2d1891312dde52964d774144208cd1a0/contracts/glv/GlvUtils.sol#L130C1-L140C6" class="external-link" rel="nofollow">GlvUtils.getGlvTokenPrice</a>

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
price = glvValue / glvSupply

glvValue：GLV 统计了它在每个 market 下拥有的 market token 数量。
计算时遍历每个 market token，计算其 USD 价值并求和。
```

</div>

</div>

</div>
