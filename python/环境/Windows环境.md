# python

## pip

官方源地址: [https://pypi.org/simple](https://link.zhihu.com/?target=https%3A//pypi.org/simple)

```python3
# 部分模块国更新不及时需要切换到官网 执行下面的命令  或者-i
pip config set global.index-url  https://pypi.org/simple  
pip install xx -i https://pypi.org/simple
```

国内

```text
# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple

# 豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/
```



```
pip install wechatpy -i http://pypi.org/simple/ --trusted-host pypi.org
```



## 安装github最新包

```
pip install https://github.com/jxtech/wechatpy/archive/master.zip -i https://pypi.org/simple
```





```
pip install -r requirements.txt
```

