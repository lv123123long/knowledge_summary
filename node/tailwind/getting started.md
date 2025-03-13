# Getting started
Css属性原子封装的 UI框架  （no javascript）

每一个css属性封装成一个类选择器

## 使用

```
#最新地址 淘宝 NPM 镜像站喊你切换新域名啦!
npm config set registry https://registry.npmmirror.com

```

[手搓一个node切换源小工具！嗨嗨嗨，又到了写轮子环节了，为什么要写这个东西呢？ 应为npm自带的源下载东西灰常慢 目前 - 掘金](https://juejin.cn/post/7194374326303326266)

```
npm init -y

npm install -D tailwindcss

npx tailwindcss init 
```
npx 命令初始化一个 tailwindcss.config.js 文件


```
npx tailwindcss -i .\src\input.css -o .\src\input.css -- watch
```