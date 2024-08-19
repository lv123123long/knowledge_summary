# [PicList](https://github.com/Kuingsmile/PicList)
## OverView
PicList 是一款高效的云存储和图床平台管理工具，在 PicGo 的基础上经过深度的二次开发。支持非常丰富的存储方式：WebDAV、S3 API 兼容平台、腾讯COS V5、Github 等，还有插件功能，通过插件可以支持 MinIO。

GitHub： [Kuingsmile/PicList: An image upload and manage tool, base on PicGo (github.com)](https://sspai.com/link?target=https%3A%2F%2Fgithub.com%2FKuingsmile%2FPicList)

### 安装 PicList

下载地址： https://github.com/Kuingsmile/PicList/releases ，找到需要的版本下载安装。

### 设置 PicList 使用 MinIO 当图床

1. 在【插件】界面，搜索 `MinIO` ，安装作者是 herbertzz 的那个插件。其 GitHub 地址是 https://github.com/Herbertzz/picgo-plugin-minio 。（可能需要先安装 [nodejs](https://sspai.com/link?target=https%3A%2F%2Fnodejs.org%2Fen%2F) ，并且还有重启电脑才能生效）
2. 在【图床】，选择【MinIO图床】，编辑配置，需要说明的有
    - endPoint：服务端的域名或者 IP 地址，ib.ahfei.blog
    - port： 443
    - userSSL：是否开启 SSL，选择开启
    - accessKey：安装 Minio Server 时设置的用户名，vfly2
    - secretKey：之前设置的密码，pass_vfly2_word
    - bucket：创建的桶名称，imagesbed
3. 保存配置
4. 在【上传】，选择图床，然后随便上传一张图片试试是否成功（实际体验，如果与服务端网络不太好，超过 1 MB 就很容易失败）

### 配合Obsidian使用

简单说明作用： **在拖入图片到 Obsidian 时，自动上传到图床**

1. Obsidian 安装插件：Image Auto Upload Plugin
2. 进入插件设置页面，
    - 修改默认上传器为 `PicGo(app)`
    - 设置 `PicGo server 上传接口` 为 `http://127.0.0.1:36677/upload`
    - 该插件还额外支持通过 PicList 进行云端删除，在删除接口填入 `http://127.0.0.1:36677/delete`
    - 其他设置按需选择

## 参考
https://sspai.com/post/86900