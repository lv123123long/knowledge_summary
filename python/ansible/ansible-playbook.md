# ansible-playbook

如果直接使用 ansible-playbook 显示命令不存在


可以
```
sudo find / -name ansible-playbook 2>/dev/null
```

```
sudo ln -s /usr/local/python/bin/ansible-playbook /usr/bin/ansible-playbook
```


在 /etc/profile
```
export PATH=$PATH:/usr/local/python/bin
```

```
source /etc/profile
```

```
ansible-playbook -i cluster.yaml dayu_infra.yaml -b -vvv | tee zzzz.out
```
