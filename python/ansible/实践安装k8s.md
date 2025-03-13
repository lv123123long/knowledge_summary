# install k8s

```
ansible-playbook -i cluster.yaml dayu_infra.yaml -b -vvv | tee zzzz.out
```

## 配置文件ansible.cfg

Ansible没有使用当前目录下的ansible.cfg文件的原因是因为该目录（/opt/install_k8s）是所有用户都可写的（world-writable），即对所有用户都具有写权限。Ansible出于安全考虑，会忽略位于世界可写目录中的配置文件。

解决方案
修改目录权限
你需要修改/opt/install_k8s目录的权限，使其不是世界可写的。可以通过以下命令来改变目录权限：

Bash
深色版本
sudo chmod 755 /opt/install_k8s
这将确保只有目录的所有者可以写入，而其他用户只能读取和执行。


## SElinux

```
"item": "etcd-client-req-csr.json.j2",
    "msg": "Aborting, target uses selinux but python bindings (libselinux-python) aren't installed!"

```

问题的核心在于目标系统使用了SELinux，但缺少Python的SELinux绑定库（libselinux-python）。这个库对于在启用了SELinux的系统上正确处理文件权限和标签非常重要。

检查
/etc/selinux/config 或者使用命令
```
getenforce
```

```
cat /proc/cmdline

sestatus
```