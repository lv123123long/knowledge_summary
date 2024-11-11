# model_download.py
import os
import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
# 下载模型
model_dir = snapshot_download('qwen/Qwen2-7B-Instruct', cache_dir='/root/autodl-tmp', revision='master')

"""
model_id：模型的唯一标识，标识模型的名称和版本
revision：模型的版本或分支；表示下载主分支的最新版本
cache_dir：模型缓存目录
use_auth_token：是否使用令牌，访问私有模型或者需要认证的模型
force_download：是否强制重新下载模型，默认是False
proxies：dict，代理设置，设置代理服务器
local_files_only：是否只从缓存中加载模型，默认False
user_agent：用户代理字符串
timeout：下载超时时间，默认None
trust_remote_code：是否信任远程代码，默认为False
ignore_files: list，忽略的文件列表，可以用来指定下载模型时需要忽略的文件
"""