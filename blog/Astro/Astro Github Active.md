# Github
创建一个同名的仓库
```
- [lv123123long](https://github.com/lv123123long)/
- [lv123123long.github.io](https://github.com/lv123123long/lv123123long.github.io)
```

用户名字: lv123123long
仓库名字: lv123123long.github.io


# Astro

初始化Astro项目

# Astro 部署到 github
![[Pasted image 20240820002854.png]]

![[Pasted image 20240820002915.png]]

```
name: Deploy to GitHub Pages

  

on:

  # 每次推送到 `main` 分支时触发这个“工作流程”

  # 如果你使用了别的分支名，请按需将 `main` 替换成你的分支名

  push:

    branches: [ main ]

  # 允许你在 GitHub 上的 Actions 标签中手动触发此“工作流程”

  workflow_dispatch:

  

# 允许 job 克隆 repo 并创建一个 page deployment

permissions:

  contents: read

  pages: write

  id-token: write

  

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout your repository using git

        uses: actions/checkout@v4

      - name: Install, build, and upload your site

        uses: withastro/action@v2

        with:

          # path: . # 存储库中 Astro 项目的根位置。（可选）

          # node-version: 20 # 用于构建站点的特定 Node.js 版本，默认为 20。（可选）

          package-manager: pnpm@latest # 应使用哪个 Node.js 包管理器来安装依赖项和构建站点。会根据存储库中的 lockfile 自动检测。（可选）

  

  deploy:

    needs: build

    runs-on: ubuntu-latest

    environment:

      name: github-pages

      url: ${{ steps.deployment.outputs.page_url }}

    steps:

      - name: Deploy to GitHub Pages

        id: deployment

        uses: actions/deploy-pages@v4
```


上传的时候，一定要注意，这里用的是main分支
## 参考
https://docs.astro.build/zh-cn/guides/deploy/github/