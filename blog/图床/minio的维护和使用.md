# minio的维护
## OverView
默认的端口为 9000 和 9001，记得开放端口

- 9000 为 **API** 端口，用于让程序上传下载，以及充当图床时用的也是它
- 9001 是 **Web 后台** 的端口。访问 ip:9001 即可到 Web 管理后台

## 更新
更改二进制文件，再用 mc 重启就行了
```
mc admin service restart ALIAS
```

## 备份

保存 data数据目录即可
所有数据都在里面

## 迁移
先把旧机器上的升到最新版，确保两者版本一致。然后，直接复制数据目录到新机器上，就行了

```sh
rsync -avuzP -e "ssh -p 22" -r vfly2@1.2.3.4:/mnt/minio /mnt/
```

## 参考
https://yanh.tech/2024/02/minio-server-installation-and-maintenance/
