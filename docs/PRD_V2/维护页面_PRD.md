# 维护页面_PRD

<div class="Section1">

# <style>[data-colorid=pujr9tso84]{color:#bf2600} html[data-color-mode=dark] [data-colorid=pujr9tso84]{color:#ff6640}</style>基础信息

1.  需求背景：独立的前端静态页面，用于在产品进行系统升级、紧急维护或重大故障修复时，向用户展示维护信息。

2.  页面：动图+文案+手动刷新按钮

3.  方案<span colorid="pujr9tso84">（需技术提供并确认）</span>：通过**运维开关**控制展示，包含**动态可配置白名单**控制豁免路径。

<div class="table-wrap">

<table class="confluenceTable" data-table-width="760" data-layout="default" data-local-id="0956ab5d-5c70-41a6-84a7-9529647e2d3e">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr data-local-id="5f1ace56-bffe-4974-a36a-6ddddc0acf46">
<td class="confluenceTd" data-highlight-colour="#f8f8f8" data-local-id="a15a6dda-d4c5-4fa7-b03a-f1a13e695c2b"><p>用户发起请求<br />
↓<br />
请求先到 <strong>Cloudflare Worker（边缘层）</strong><br />
↓<br />
<strong>判断是否命中白名单（运维可动态配置）</strong><br />
白名单需包含以下类型：</p>
<ul>
<li><p>管理员 IP</p></li>
<li><p>特定 Header / Cookie（如运维或内部访问标识）</p></li>
<li><p><strong>指定路径（必须包含 Keeper / 清算相关接口）</strong></p></li>
</ul>
<blockquote>
<p>Keeper 路径在维护期间必须放行，防止因维护页拦截导致清算无法执行，进而产生死单或系统性风险。</p>
</blockquote>
<p>↓<br />
<strong>命中白名单 → 直接放行访问，不展示维护页</strong><br />
↓<br />
<strong>未命中白名单</strong><br />
↓<br />
从 <strong>Cloudflare Worker 本地缓存</strong> 读取维护开关 <code>maintenance_flag</code></p>
<ul>
<li><p>缓存命中：</p>
<ul>
<li><p>ON → 返回维护页面</p></li>
<li><p>OFF → 正常访问</p></li>
</ul></li>
<li><p>缓存未命中：</p>
<ul>
<li><p>访问 Redis 读取最新维护状态</p></li>
<li><p>写入本地缓存（带 TTL）</p></li>
<li><p>再根据 ON / OFF 决定是否展示维护页</p></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

</div>

# 产品需求

<span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size"><img src="5d57aa3412805d4923429a43f7a64beab9e5c7a123d9f45c1f54856ee53499d1" class="confluence-embedded-image image-center" loading="lazy" data-image-src="https://hertzflow.atlassian.net/wiki/download/attachments/77660267/Screenshot%202026-01-26%20at%2018.58.54.png?version=1&amp;modificationDate=1769425156827&amp;cacheVersion=1&amp;api=v2" data-height="649" data-width="1044" data-unresolved-comment-count="0" data-linked-resource-id="77660288" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="Screenshot 2026-01-26 at 18.58.54.png" data-base-url="https://hertzflow.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="77660267" data-linked-resource-container-version="2" data-media-id="e2f5fab0-70e9-4dca-b9df-5a03c14d35e7" data-media-type="file" width="468" height="291" alt="Screenshot 2026-01-26 at 18.58.54.png" /></span>

- 现有<a href="https://www.figma.com/design/AmguvHz2zBT9YzQgH9AVB8/HertzFlow?node-id=4032-19725&amp;t=l3HnspPa1cqkegde-4" class="external-link" rel="nofollow">UI稿</a>，补充light mode，改一下插图即可（静态动态不限。白色黑色背景兼容）若文案需要配合改找我

- ddl：周中前

- 参考： <a href="https://uk.pinterest.com/pin/104708760083277574/" class="external-link" data-card-appearance="inline" data-local-id="2765f405-23e6-4a18-8052-60d53454e304" rel="nofollow">https://uk.pinterest.com/pin/104708760083277574/</a> ；<a href="https://uk.pinterest.com/pin/7107311905552311/" class="external-link" rel="nofollow">https://uk.pinterest.com/pin/7107311905552311/</a>；<a href="https://dribbble.com/shots/26482697-Flowstep-maintenance-page-Framer" class="external-link" rel="nofollow">https://dribbble.com/shots/26482697-Flowstep-maintenance-page-Framer</a>；<a href="https://dribbble.com/shots/4202911-Maintenance-Page" class="external-link" rel="nofollow">https://dribbble.com/shots/4202911-Maintenance-Page</a>

</div>
