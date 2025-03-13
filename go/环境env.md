# go env

## go get

```
go get -u github.com/korb1n/test-project
```
* 用来获取和安装Go模块或包
* -u表示更新已存在的包到最新版本

下载过程
1. 查找仓库
2. 克隆拉取代码，Go 会在你的 GOPATH 或者 GO MODULE 的目录结构中创建一个新的文件夹，并将仓库克隆到这个位置。如果已经存在，它会拉取最新的更改。
3. 安装依赖，如果它依赖第三方库的话，会递归获取这些依赖
4. 构建和安装，最后go会编译代码，并将生成二进制文件或者库文件放置在合适的位置

存放位置
- **使用 Go Modules (推荐)**: 如果你在一个启用了 Go Modules 的项目中运行 `go get` 命令，那么下载的包会被存放在 `$GOPATH/pkg/mod` 目录下。Go Modules 是 Go 1.11 版本引入的一种新的依赖管理方式，它允许每个项目有自己的依赖版本，而不需要全局共享。
    
- **不使用 Go Modules**: 如果没有启用 Go Modules，下载的包将会被放置在 `$GOPATH/src` 下面对应的位置。例如，对于 `github.com/korb1n/test-project`，它会被放置在 `$GOPATH/src/github.com/korb1n/test-project`。同时，相关的二进制文件或者库文件会被安装到 `$GOPATH/bin` 和 `$GOPATH/pkg` 中。

## 代理
go env -w GO111MODULE=on 

go env -w GOPROXY=https://goproxy.io,direct

