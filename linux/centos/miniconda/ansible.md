# ansible
## 基于python3搭建ansible环境

```bash
# 进入新建的虚拟环境
source activate py37-ansible
# 使用pip3安装ansible
pip3 install ansible
```


```
# 查找ansible文件
[root@localhost ~]# find / -name "ansible"
/root/anaconda3/envs/py37-ansible/bin/ansible
/root/anaconda3/envs/py37-ansible/lib/python3.7/site-packages/ansible
/root/anaconda3/envs/py37-ansible/lib/python3.7/site-packages/ansible_test/_data/injector/ansible
/root/anaconda3/envs/py37-ansible/lib/python3.7/site-packages/ansible_collections/ansible
/root/anaconda3/envs/py37-ansible/lib/python3.7/site-packages/ansible_collections/netbox/netbox/docs/js/ansible
# 创建软链接
ln -s /root/anaconda3/envs/py37-ansible/bin/ansible /usr/bin/ansible
```


```
(py37-ansible) [root@localhost ~]# ansible --version
ansible 2.10.3
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /root/anaconda3/envs/py37-ansible/lib/python3.7/site-packages/ansible
  executable location = /root/anaconda3/envs/py37-ansible/bin/ansible
  python version = 3.7.9 (default, Aug 31 2020, 12:42:55) [GCC 7.3.0]
```

>需要注意：pip安装ansible无config file，需手动创建  
参考配置：[https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg](https://links.jianshu.com/go?to=https%3A%2F%2Fraw.githubusercontent.com%2Fansible%2Fansible%2Fdevel%2Fexamples%2Fansible.cfg)  
创建hosts文件：  
参考配置：[https://raw.githubusercontent.com/ansible/ansible/devel/examples/hosts](https://links.jianshu.com/go?to=https%3A%2F%2Fraw.githubusercontent.com%2Fansible%2Fansible%2Fdevel%2Fexamples%2Fhosts)  
以上两个文件默认位置：/etc/ansible

  
  
## 参考

[Anaconda3基于python3搭建ansible环境 - 简书 (jianshu.com)](https://www.jianshu.com/p/bee385ae833b)

