# miniconda
## OverView
维护一套随时上传的python虚拟环境


## install

https://docs.anaconda.com/miniconda/

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```


```
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

这里有一点要注意，安装好之后，要重开窗口，进入终端，让conda生效，再使用

## 使用

```
conda create -n py36 python=3.6
```

```
conda activate py36
```

```
conda deactivate
```

1. **`conda config --set channel_priority strict`**: 这个命令设置通道优先级为严格模式。在严格模式下，Conda 会按照你在配置文件中列出的通道顺序来搜索和安装包。如果在前面的通道中找到了所需的包，Conda 将不会在后续的通道中查找。这可以确保你优先从你指定的通道中获取包，而不是默认通道。
    
    例如，如果你首先添加了 `conda-forge`，然后设置了严格优先级，Conda 将首先从 `conda-forge` 通道查找和安装包，而不是 Anaconda 的默认通道。
    
2. **`conda config --add channels conda-forge`**: 这个命令将 `conda-forge` 通道添加到你的 Conda 通道列表中。`conda-forge` 是一个由社区维护的通道，提供了大量的软件包，通常更新得更频繁，可能包含一些在默认通道中找不到的包。
    
    当你添加一个新的通道时，它会被放置在通道列表的最后面。这意味着，除非设置了通道优先级，否则 Conda 会首先从其他已经配置的通道（如默认通道）搜索包，最后才从 `conda-forge` 通道搜索。


## 换源
修改国内源
这里有三组国内源可供选择：

清华镜像：

https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/

中科大镜像：

https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/

上海交大镜像：

https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/main/
https://mirrors.sjtug.sjtu.edu.cn/anaconda/pkgs/free/
https://mirrors.sjtug.sjtu.edu.cn/anaconda/cloud/conda-forge/


```
conda config --add channels   https~~~~
```

```
conda config --remove channels  https~~~~
```

命令后面加 -v  -vv -vvv 打印详细过程


## 打包虚拟环境

```
conda activate py36
conda install -c conda-forge conda-pack
```


```
conda pack -n py36 -o py36.tar.gz
```


## 参考
https://blog.csdn.net/Xiao_Spring/article/details/109130663
