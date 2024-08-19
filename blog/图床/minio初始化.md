# minio的安装
## OverView
要在Ubuntu 24.04系统上安装MinIO，你可以遵循以下步骤来进行操作。MinIO是一个高性能的对象存储服务器，设计用于云存储。它兼容Amazon S3 API，非常适合存储大量非结构化数据，如图像、视频和备份文件。以下是详细的安装指南：
## 下载
确保系统是最新的，安装必要的依赖
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install wget -y
```

```
wget https://dl.min.io/server/minio/release/linux-amd64/minio
```

## 运行
移动到指定文件夹并赋权
```
sudo cp minio /usr/local/bin/  
sudo chmod +x /usr/local/bin/minio
```

创建一个存储目录
```
sudo mkdir -p /data/minio/data
```

## 启动
### 配置环境变量（可选）

如果你想自定义MinIO的访问凭据，可以通过环境变量来设置。例如：

```bash
export MINIO_ROOT_USER=admin
export MINIO_ROOT_PASSWORD=your-strong-password
```
直接运行
```
sudo minio server /data --console-address ":9001"  
MinIO启动后，可以在浏览器中输入[http](https://so.csdn.net/so/search?q=http&spm=1001.2101.3001.7020)://ip:9001，在用户名密码处输入默认用户名密码（minioadmin/minioadmin）即可登陆系统。
```

### 配置为系统服务（可选）

为了使MinIO作为系统服务自动启动并在后台运行，你可以创建一个Systemd服务单元文件。创建文件 `/etc/systemd/system/minio.service` 并输入以下内容：

```ini
[Unit]
Description=MinIO Object Storage Server
After=network.target

[Service]
User=root # 或者其他适合运行MinIO的用户
Group=root
ExecStart=/path/to/your/minio server /opt/minio_data
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

记得将`/path/to/your/minio`替换为实际的minio二进制文件路径。之后，通过以下命令启用并启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable minio
sudo systemctl start minio
```

```
[Unit]
Description=Minio Service
 
[Service]
Environment="MINIO_ROOT_USER=lzflminio"
Environment="MINIO_ROOT_PASSWORD=lzflminio"
ExecStart= /usr/local/bin/minio server /data/minio/data --console-address ":9001"
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
StandardOutput=/data/minio/logs/minio.log
PrivateTmp=true
 
[Install]
WantedBy=multi-user.target

说明：
    MINIO_ROOT_USER:登录用户名
    MINIO_ROOT_PASSWORD 密码
    ExecStart：minio的安装路径 和控制台启动。默认启动端口9000 控制台登录端口可自行设置：演示为：9001
    StandardOutput：minio日志
```

（3）：加载服务文件
systemctl daemon-reload

（4）：设置开机自启动
systemctl enable minio.service

（5）：启动minio
systemctl start minio.service

（6）：查看状态
systemctl status minio.service

## 参考
https://blog.csdn.net/zhangleiyes123/article/details/131964406
https://cloud.tsyidc.com/Techops/247.html
