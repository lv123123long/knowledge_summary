# 图床
## github

1. 创建一个公开的仓库
2. 访问https://github.com/settings/tokens 页面，创建一个 `token`，用于 `PicGo` 访问仓库。
3. [参考](https://ilaozhu.com/archives/2063/)


## jsDelivr

`jsDelivr` 是一个免费的开源文件 `CDN`，与 `Github` 和 `NPM` 紧密集成，能够自动为几乎所有开源项目提供可靠的 `CDN` 服务，且没有带宽限制或高级功能，任何人都可以完全免费使用。

`jsDelivr` 在国内外`290+`的区域都有 `CDN`节点，并且访问速度很快，基本上可以保证在任何地方都能快速访问到。

1. 只需要通过`https://cdn.jsdelivr.net/gh/用户名/仓库名/文件路径`来引用资源文件即可

我们知道，`CDN` 本质上就是一个缓存系统，因此，当我们更新资源文件后（如更换一个 LOGO），就必须更新缓存，才能让新文件生效。

事实上，`jsDelivr`的缓存会在一段时间之后自动失效，但如果你想要立即使用新的资源，就需要手动更新缓存。

* 操作也很简单，只需要将上面的`https://cdn.jsdelivr.net/`替换成`https://purge.jsdelivr.net/`，然后通过浏览器访问一下就可以了

> 如果你的网站访问量很小，那么`jsDelivr`可能并没有缓存资源，首次访问时，资源需要先从 `Github` 加载到`jsDelivr`的`CDN`节点，再从节点返回给客户端，可能会出现用了`CDN`比不用`CDN`更慢的结果。



[参考](https://ilaozhu.com/archives/2062/)


## pictList

![image-20240818230725714](https://cdn.jsdelivr.net/gh/lv123123long/image-repo/image-20240818230725714.png)



## Typora

![image-20240818230820534](https://cdn.jsdelivr.net/gh/lv123123long/image-repo/image-20240818230820534.png)

