# (WIP) GMX V2 部署流程

<div class="Section1">

> Github Repo: <a href="https://github.com/HertzFlow/contracts-v2-bsc" class="external-link" data-card-appearance="inline" data-local-id="d4025ef2-ecb3-4fbc-9426-4cd7d4b08478" rel="nofollow">https://github.com/HertzFlow/contracts-v2-bsc</a>

<style type="text/css">/**/
div.rbtoc1772270911415 {padding: 0px;}
div.rbtoc1772270911415 ul {list-style: none;margin-left: 0px;}
div.rbtoc1772270911415 li {margin-left: 0px;padding-left: 0px;}

/**/</style>

<div class="toc-macro rbtoc1772270911415">

- [0. fork 版本选择](#id-(WIP)GMXV2部署流程-0.fork版本选择)
- [主要功能](#id-(WIP)GMXV2部署流程-主要功能)
- [实际用途](#id-(WIP)GMXV2部署流程-实际用途)
- [1. 部署流程概述](#id-(WIP)GMXV2部署流程-1.部署流程概述)
  - [1.1 GMX V2 项目基础知识和准备工作](#id-(WIP)GMXV2部署流程-1.1GMXV2项目基础知识和准备工作)
- [2. 部署合约](#id-(WIP)GMXV2部署流程-2.部署合约)
- [3. 踩过的坑和注意点](#id-(WIP)GMXV2部署流程-3.踩过的坑和注意点)
  - [3.1 部署 Test Token](#id-(WIP)GMXV2部署流程-3.1部署TestToken)
  - [3.2 部署 Oracle](#id-(WIP)GMXV2部署流程-3.2部署Oracle)

</div>

## 0. fork 版本选择

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**TL;DR**

v2.3-branch

最新 commit id：1cc4ef9ca19f26bd51b3e175d2c0d3a595a2ac02

</div>

</div>

**当前主要有两个选择：**

- git tag v2.2

- git branch v2.3-branch

> 注：最新的 tag 就是 v2.2

**非代码区别：**

v2.2 官方管理不善，无法直接编译，yarn dependency 依赖管理有缺失，但是经过一些 yarn add 依赖补齐可以解决。而 v2.3-branch 可以一次性构建成功。

**代码区别：**

我们只关注 `./contracts` 中对于合约逻辑的修改。

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="26725309364b67cace30cebd30c860936e5a40659210b42495bb52e5fe4cc430" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/53575717/image-20251211-125621.png?version=1&amp;modificationDate=1765457786020&amp;cacheVersion=1&amp;api=v2" data-height="899" data-width="504" data-unresolved-comment-count="0" data-linked-resource-id="54034512" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251211-125621.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="53575717" data-linked-resource-container-version="9" data-media-id="0b776b2f-6560-40a8-a084-971fcf15cf91" data-media-type="file" width="468" height="835" alt="image-20251211-125621.png" /></span>

整体来看，对于核心的合约完全没有任何改动（指：交易，流动性，强平相关所有）。

细节上看:

- mock，略

- v1 指代 GMX v1，我们没有这个历史包袱

- multichain 我们不涉及

- automation 合约所谓的自动化处理，不太看的懂，claude 指出这是 Chainlink 发出一些信号触发 GMX 进行自动操作的一个工具，总之和主流程是解耦的，没什么影响：

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

这是一个 **Chainlink Functions (CRE - Chainlink Runtime Environment) 接收器合约**，用于让 GMX v2 协议能够接收和执行来自 Chainlink 去中心化计算网络的自动化任务。

## 主要功能

1.  **接收 Chainlink 工作流执行结果**

- `onReport` 函数接收来自 Chainlink Forwarder 的报告

- 解析工作流元数据（ID、名称、所有者）

2.  **多层安全验证**

solidity

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
// 验证工作流所有者是否有 CRE_KEEPER 角色
if (!roleStore.hasRole(workflowOwner, Role.CRE_KEEPER))

// 验证工作流 ID 是否被授权
if (!dataStore.getBool(Keys2.creReceiverAuthorizedWorkflowIdsKey(workflowId)))
```

</div>

</div>

3.  **执行链上调用**

- 从 report 中解码目标合约地址和调用数据

- 执行低级别 `call` 调用

- 处理执行失败情况

4.  **事件记录**

- 发出 "CRE Workflow Executed" 事件，包含完整的 metadata 和 report

## 实际用途

这个合约让 GMX v2 可以实现：

- **自动化价格更新**：通过 Chainlink 预言机网络定期更新资产价格

- **清算触发**：监控链下数据，满足条件时自动触发清算

- **复杂计算外包**：将复杂的链下计算（如风险评估、资金费率计算）交给 Chainlink 网络处理后再上链执行

- **跨链数据同步**：获取其他链的数据状态

这是 GMX v2 向更自动化、去中心化方向演进的基础设施组件。

<a href="https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on" class="external-link" rel="nofollow">Claude is AI and can make mistakes.</a>\
<a href="https://support.anthropic.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on" class="external-link" rel="nofollow">Please double-check responses.</a>

Sonnet 4.5

</div>

</div>

- claim 模块，这部分是 GMX 用来手动给用户补偿的合约，具体来说 GMX 会往这个合约里面存入资金，用户签署条款并且签名之后可以从这个合约里面领取自己的补偿，可能用于活动和事故。和主流程无关。

- event / utils 等工具模块，略。

- config 模块，新增了关于 oracle 的一些配置，核心逻辑在于变更 oracle price feed 的配置，也就是如何对接 edge / chainlink 的链上 price，这里和我们关系不大。

- Fee 模块，部分手续费会抽水，在 datastore 里面逻辑隔离存储（Market 合约持有，但不计入池子），这部分资产可以由 Fee 模块进行提取。目前 Fee 的逻辑如下：

  - 交易中抽水，逻辑记录手续费数量，手续费本身存在 market 合约中

  - keeper 调用 FeeHandler 的 claimFee，把 market 合约中的手续费转入 FeeHandler 合约，比如 100 USDC

    - 根据 FeeHandler 入金的 100 USDC，记录可兑换 80GMX + 20 WNT

  - 用户调用 buyBack，给出 80 GMX + 20 WNT 存入合约，换走 FeeHandler 持有的 100 USDC

  - keeper 通过 FeeDistributor，提走 80GMX + 20WNT

<span style="background-color: rgb(254,222,200);">注意：这里 FeeDistributor 的逻辑很复杂，涉及到跨链部署时，每个链 stake 的 GMX Token 数量按照比例分配并且在链上构造了状态机流转分步运行。我们单链部署的情况下应该不需要这套逻辑，可能需要把 FeeHandler 的逻辑修改，允许 keeper 直接提走对应的 Fee 抽水，而不是转入当前 FeeHandler 合约等待分配。</span>

------------------------------------------------------------------------

## 1. 部署流程概述

### 1.1 GMX V2 项目基础知识和准备工作

**基础知识：**

- 使用 **<u>hardhat</u>** 构建

- 使用 **<u>yarn</u>** 进行 js 依赖管理

- 使用 **<u>hardhat-deploy</u>** 插件进行合约部署

<div class="confluence-information-macro confluence-information-macro-information">

<span class="aui-icon aui-icon-small aui-iconfont-info confluence-information-macro-icon"></span>

<div class="confluence-information-macro-body">

**hardhat-deploy 插件**

hardhat 脚手架使用 `hardhat.config.ts` 文件进行设置。

hardhat-deploy 插件提供了 deploy 命令，允许你执行 `yarn hardhat deploy` 进行一键部署操作。

其中 deploy 命令可以通过修改 `hardhat.config.ts` 的 task 进行 override，比如 GMX 官方要求你必须提供一个环境变量才能部署非本地环境：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
task("deploy", "Deploy contracts", async (taskArgs: any, env, runSuper) => {
  env.deployTags = taskArgs.tags ?? "";
  if (
    !(process.env.SKIP_AUTO_HANDLER_REDEPLOYMENT == "true" || process.env.SKIP_AUTO_HANDLER_REDEPLOYMENT == "false") &&
    env.network.name != "hardhat"
  ) {
    throw new Error("SKIP_AUTO_HANDLER_REDEPLOYMENT flag is mandatory");
  }
  await runSuper();
});
```

</div>

</div>

hardhat-deploy 插件的默认行为：

读取 `./deploy` 目录下的 ts 文件，根据命名字典序进行依次运行，当然，该插件也允许你在部署脚本内进行 dependency 的配置，自动根据依赖顺序进行部署，GMX 正是采用了这个方法而非命名顺序。

部署的结果会输出在 `./deployments/${network_name}`目录下，结果就是 abi 文件。通过这些文件，可以实现避免重复部署的功能。原理是：插件会对比 artifact 目录下的产物和 deployments 下的部署 abi。因此如果你删除了 deployments 目录，部署将会重新全量执行。

</div>

</div>

------------------------------------------------------------------------

**准备工作：**

1.  clone 仓库到本地

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
git clone git@github.com/...
```

</div>

</div>

2.  项目初始化

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
yarn install --frozen-lockfile
```

</div>

</div>

3.  编译 solidity 合约代码

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
yarn hardhat compile
```

</div>

</div>

4.  编写 .env 文件

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# bsc wallet privatekey
# hardhat.config.ts 中通过该环境变量读取私钥，使用该钱包进行部署
ACCOUNT_KEY=

# bsc scan api key(explorer)
# 部署后，通过 etherScan 进行合约的 verify
# 经过 verify 的合约，可以在区块浏览器上查看源码以及获得 verified 的标识
# 原理其实就是上传了你的合约源代码
# 目前 bsc 统一接入 etherscan v2 api，因此需要你注册好账户去这里创建你自己的 apikey:
# https://etherscan.io/apidashboard
BSCSCAN_API_KEY=

# skip deployed handler contracts
# 对于 xxxHandler 合约，是否跳过已经部署的部分
# 这部分通常推荐设置为 true
# 初次部署可以加速中断后继续部署的速度
# handler 合约本身也没有资金逻辑，只是 utils 合约的一个封装
SKIP_AUTO_HANDLER_REDEPLOYMENT=true

# deploy wait wait confirmations
# suggest at least 2 for non-local env, and must be 1 for local env
# 本地部署必须设置为 1，因为本地 hardhat 网络是没有多节点的
# 上传到外部区块链设置为 2 可以降低 NONCE_EXPIRED 等错误发生几率
WAIT_CONFIRMATIONS=1
```

</div>

</div>

5.  生成合约的部署顺序

由于 GMX V2 采用了模块化设计，导致其合约体量非常大，一次完整的部署包含了大约150个合约。因此简单的使用 `yarn hardhat deploy --network bscTestnet` 极其耗时并且容易因为网络问题和区块链确认等机制而失败中断。<u>因此我更倾向于手动拆分部署流程，按模块进行部署</u>，即：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
yarn hardhat deploy --network bscTestnet --tags ${Contract}
```

</div>

</div>

为了得到 `tags` 具体有哪些，以及其顺序，需要梳理 `./deploy`下每个脚本中的配置，该梳理工作量非常繁重，依赖 AI 分析或许能解决部分问题，但是这里暂时没有采用 ，而是直接通过解析本地 hardhat 部署流程，得到了一套完整的部署顺序：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
# rg -F 也可以替换为 grep
yarn hardhat deploy --network hardhat | \
  rg -F 'deployed at' | \
  awk '{gsub(/"/, "", $2); print $2}' > deploy-order.txt
```

</div>

</div>

该命令在本地 hardhat 网络进行部署，捕获 `hardhat-deploy` 插件在部署合约时输出的日志进行字符串分析。

得到的文件如下，每一行是一个合约的名字:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
RoleStore
DataStore
WETH
GMX
ESGMX
WBTC
USDC
USDT
EventEmitter
...
```

</div>

</div>

至此准备工作完成。

------------------------------------------------------------------------

## 2. 部署合约

部署合约的步骤经过 1 中准备已经非常简单，遍历 `deploy-order.txt`文件的每一行，去调用:

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
yarn hardhat deploy --network bscTestnet --tags ${Contract}
```

</div>

</div>

<span class="status-macro aui-lozenge aui-lozenge-visual-refresh aui-lozenge-current">WARN</span> 真正部署到非本地环境时，注意把 `.env` 文件里面的 `WAIT_CONFIRMATIONS=1` 修改为 2，否则容易出现大量的网络等错误导致部署中断，浪费 GAS。

------------------------------------------------------------------------

## 3. 踩过的坑和注意点

### 3.1 部署 Test Token

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
RoleStore
DataStore
WETH
GMX
ESGMX
WBTC
USDC
USDT
EventEmitter
```

</div>

</div>

这里不难看到，`DataStore`合约和 `EventEmitter` 合约中间有许多 Token 合约的名字，这些 Token 合约显然在线上 mainnet 不应该由我们自己部署，应当是本地测试所依赖的一些辅助合约。

于此同时，这部分合约还不是手动部署的，而是通过 `./deploy/deployTestTokens.ts` 脚本，读取 `./config/tokens.ts`里面配置的 token 名单进行自动化部署的，由于我们是通过 deploy hardhat 生成的合约清单，因此会包含这些东西。

我们需要在生成清单之后，将这些 tokens 去除掉。

### 3.2 部署 Oracle

GMX V2 合约的 oracle 模块做的比较通用，支持包括 Chainlink、Edge(Chaos Lab 出品) 和 GmOracle 以及自定义 oracle 的一系列不同价格来源。根据我们的需求，我们其实只需要部署好 `GmOracleProvider` 即可 —— 这个 oracle 是类似于 v1 的通过非对称密钥签名机制来验证价格可信的经典 oracle，主要用于我们官方自建的价格来源，也就是我们自己的链下 oracle。其余的 provider 其实不需要，也就无需费心研究 chainlink 的部署配置了。

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
从 deploy-order.txt 中删除：
- ChainlinkDataStreamProvider
- EdgeDataStreamVerifier
- EdgeDataStreamProvider
```

</div>

</div>

注意，chainlink 相关合约中，还有一个特殊的存在：`ChainlinkPriceFeedProvider`。这也是一个 OracleProvider，但是它在合约中的作用非常特殊：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
ValidatedPrice memory validatedPrice = provider.getOraclePrice(token, data);

// 我们的 GmOracleProvider 这里会返回 false，会走进这个分支。
if (!provider.isChainlinkOnChainProvider()) {
    (bool hasRefPrice, uint256 refPrice) = ChainlinkPriceFeedUtils.getPriceFeedPrice(dataStore, token);

    if (hasRefPrice) {
        _validateRefPrice(
            token,
            validatedPrice.min,
            refPrice,
            maxRefPriceDeviationFactor
        );

        _validateRefPrice(
            token,
            validatedPrice.max,
            refPrice,
            maxRefPriceDeviationFactor
        );
    }
}

prices[i] = validatedPrice;
```

</div>

</div>

核心逻辑在于：GmOracleProvider 上报的价格，可能会根据 Chainlink 的报价进行调整。获取 Chainlink 报价的逻辑就是用上面这个特殊合约获取的，然而只要不配置 Chainlink 对应的 token 报价地址，我们可以快速返回，绕过这个调整，达成和 v1 一样只信任自己 oracle 报价不调整的逻辑：

<div class="code panel pdl" style="border-width: 1px;">

<div class="codeContent panelContent pdl">

``` syntaxhighlighter-pre
function getPriceFeedPrice(DataStore dataStore, address token) internal view returns (bool, uint256) {
    address priceFeedAddress = dataStore.getAddress(Keys.priceFeedKey(token));
    // 这里不配置，就会返回 0 地址，从而快速 return
    if (priceFeedAddress == address(0)) {
        return (false, 0);
    }
    // ...
}
```

</div>

</div>

因此 `ChainlinkPriceFeedProvider`合约是否部署，取决于我们是否希望利用这个 feature，当前情况下可能不太需要考虑这一点，我们不做任何配置，是否部署它也就不重要了。

具体影响的配置文件如下：

`/deploy/configureOracleTokens.ts`中有如下逻辑：

1.  配置好某个 token 的 oracle 应该是某个 provider（这里是我们的 GmOracleProvider）

2.  如果配置了 priceFeed 就往下走去修改 dataStore 了

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="b9af22cc3747ce974876565e35c5cf6ac09e16a5e962d079d7c403a1c59117b5" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/53575717/image-20251211-124851.png?version=1&amp;modificationDate=1765457335988&amp;cacheVersion=1&amp;api=v2" data-height="352" data-width="785" data-unresolved-comment-count="0" data-linked-resource-id="54100054" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251211-124851.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="53575717" data-linked-resource-container-version="9" data-media-id="81266817-f37f-4913-8e43-9f4d1e00301b" data-media-type="file" width="468" height="210" alt="image-20251211-124851.png" /></span>

上面的 ts 读取的配置来源于：`./config/token.ts`

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="35b122c3fb19b9e01525fb630973e98b799e795653bc2940eca52f7c8c0f679a" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/53575717/image-20251211-125042.png?version=1&amp;modificationDate=1765457445651&amp;cacheVersion=1&amp;api=v2" data-height="281" data-width="627" data-unresolved-comment-count="0" data-linked-resource-id="54132875" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="image-20251211-125042.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="53575717" data-linked-resource-container-version="9" data-media-id="762f6a54-7949-4796-9a17-561164cfa9f2" data-media-type="file" width="468" height="209" alt="image-20251211-125042.png" /></span>

这里圈起来的地方删掉即可。

</div>
