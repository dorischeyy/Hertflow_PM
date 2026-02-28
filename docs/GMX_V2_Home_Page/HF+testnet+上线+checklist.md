# HF testnet 上线 checklist

<div class="Section1">

## 前端：

<a href="https://hertzflow.atlassian.net/wiki/people/712020:4f783b90-6540-4304-98d6-605b035d4171?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:4f783b90-6540-4304-98d6-605b035d4171" target="_blank" data-linked-resource-id="426023" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">ben</a> :

- <span class="placeholder-inline-tasks">USDC → USDT 后功能验证</span>
- <span class="placeholder-inline-tasks">官网滚动动画bug修复</span>
- <span class="placeholder-inline-tasks">UI走查问题修复</span>
- <span class="placeholder-inline-tasks">非24x7交易对的开盘收盘时间段展示功能</span>
- <span class="placeholder-inline-tasks">页面上还缺少一些链接，需要@cen给到</span>

------------------------------------------------------------------------

<a href="https://hertzflow.atlassian.net/wiki/people/712020:43b2f046-5462-4c91-ad98-9aafca4eb4a8?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:43b2f046-5462-4c91-ad98-9aafca4eb4a8" target="_blank" data-linked-resource-id="426021" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">ian</a> :

- <span class="placeholder-inline-tasks">USDC → USDT 后功能验证</span>
- <span class="placeholder-inline-tasks">UI走查问题修复</span>
- <span class="placeholder-inline-tasks">动画效果优化</span>
- <span class="placeholder-inline-tasks">Hz合约适配切换</span>

------------------------------------------------------------------------

## 后端/合约：

<a href="https://hertzflow.atlassian.net/wiki/people/712020:911aa467-6af9-4fac-accb-a78eea495f59?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:911aa467-6af9-4fac-accb-a78eea495f59" target="_blank" data-linked-resource-id="163876" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">kayce</a> :

- <span class="placeholder-inline-tasks">根据产品需求调整默认参数（如有需要）</span>
- <span class="placeholder-inline-tasks">完整发布一版新的 testnet 合约</span>
  - <span class="placeholder-inline-tasks">HF 版测试通过发 HF 版</span>
  - <span class="placeholder-inline-tasks">否则发原版</span>
- <span class="placeholder-inline-tasks">verify 合约</span>

------------------------------------------------------------------------

<a href="https://hertzflow.atlassian.net/wiki/people/712020:9c2d2658-0bf5-4f67-bc6e-e2b45e6f4463?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:9c2d2658-0bf5-4f67-bc6e-e2b45e6f4463" target="_blank" data-linked-resource-id="2293771" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">soren 0x</a> :

- <span class="placeholder-inline-tasks">针对最近的修改，keeper 完整走一遍测试流程。</span>
- <span class="placeholder-inline-tasks">在多台 ec2 上启动相应的keeper 实例，并替换为 testnet 正式的合约。</span>

------------------------------------------------------------------------

<a href="https://hertzflow.atlassian.net/wiki/people/712020:68cace1e-bfc2-4a79-8083-30238e5b9849?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:68cace1e-bfc2-4a79-8083-30238e5b9849" target="_blank" data-linked-resource-id="2818059" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">dennis</a> :

- <span class="placeholder-inline-tasks">准备最新版本的合约地址配置 <a href="https://hertzflow.atlassian.net/wiki/people/712020:9c2d2658-0bf5-4f67-bc6e-e2b45e6f4463?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:9c2d2658-0bf5-4f67-bc6e-e2b45e6f4463" target="_blank" data-linked-resource-id="2293771" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">soren 0x</a> </span>
- <span class="placeholder-inline-tasks">配置testnet环境的配置文件和发布分支，并与运维核对部署脚本</span>
- <span class="placeholder-inline-tasks">服务发布 & 功能验证</span>

------------------------------------------------------------------------

## 测试：

<a href="https://hertzflow.atlassian.net/wiki/people/712020:70313448-6362-4310-986b-28f35506d43e?ref=confluence" class="confluence-userlink user-mention" data-account-id="712020:70313448-6362-4310-986b-28f35506d43e" target="_blank" data-linked-resource-id="426022" data-linked-resource-version="1" data-linked-resource-type="userinfo" data-base-url="https://hertzflow.atlassian.net/wiki">vladmair</a> :

- <span class="placeholder-inline-tasks">market更新后各个模块整体测试流程再走一遍</span>
- <span class="placeholder-inline-tasks">自动bot生成订单在更新后的market运行正常</span>

------------------------------------------------------------------------

</div>
