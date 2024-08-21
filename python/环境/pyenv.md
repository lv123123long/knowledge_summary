# pyenv的安装

```
https://github.com/pyenv-win/pyenv-win
```

## 安装

```
git clone https://github.com/pyenv-win/pyenv-win.git
```
或者下载zip安装包

添加环境变量

把`pyenv`添加到系统的环境变量

- 建立环境变量名：PYENV，变量值为`D:\pyenv.pyenv\pyenv-win`
- 添加以下两项至`Path`:

- - %PYENV%\bin
    - %PYENV%\shims

- 设置好之后，测试pyenv是否安装并配置成功

需要将当前终端关闭并重新打开再进行测试

## pyenv常用命令
### 设置下载镜像

由于默认的pyenv使用的下载镜像(mirror)下载时很容易超时导致下载失败或下载很慢。

为了解决这个问题，这里我们更换一个更快的下载镜像。

修改`pyenv-win\libexec\libs`目录下（特别提示，对早期pyenv-win是在pyenv-win\libexec目录下）的`pyenv-install-lib.vbs`文件中的镜像配置`mirror="https://www.python.org/ftp/python"`修改为

`mirror="https://npm.taobao.org/mirrors/python/"`，令其在下载Python版本时默认从淘宝镜像中下载。

### 查看可安装的python版本列表
```
pyenv install --list # 或 pyenv install --l
```

### 安装指定版本的python

```
输入`pyenv install <python_version>`来下载需要的Python版本。例如想要下载3.8.10版本的话可以输入

```

```
pyenv install 3.8.10
```

### `pyenv global <python_version>`--设置全局的Python版本

- 我们可以通过输入`pyenv global 3.8.10`设置全局的Python版本为3.8.10
- 设置后输入`pyenv global`确认当前设置的Python版本是否为3.8.10
- 另外在设置全局Python版本后，`D:/pyenv/.pyenv/pyenv-win`目录下有一个名为`verision`的文件，打开它就可以查看全局的Python版本

### `pyenv local <python_version>`--设置当前目录下的Python版本

- 如果使用Python开发项目(比如Django)，这时因为项目使用的库版本各不相同，这时我们要在单个项目中使用特定的Python版本进行开发，这个命令实现的效果是类似于`venv`的功能。
- 我们可以输入`pyenv local 3.8.10`设置当前目录下所有Python文件使用的Python版本。
- 与查看全局版本类似，我们同样可以输入`pyenv local`确认当前设置的Python版本；也可以在当前目录下找到一个生成的`.python-version`文件来查看当前版本

### `pyenv versions`--显示已经安装的Python版本

  


##  参考
https://juejin.cn/post/7280783758618279972