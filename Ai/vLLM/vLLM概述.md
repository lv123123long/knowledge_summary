# vLLM概述
vLLM 框架是一个高效的大语言模型推理和部署服务系统，具备以下特性
高效的内存管理：通过 PagedAttention 算法，vLLM 实现了对 KV 缓存的高效管理，减少了内存浪费，优化了模型的运行效率。
高吞吐量：vLLM 支持异步处理和连续批处理请求，显著提高了模型推理的吞吐量，加速了文本生成和处理速度。
易用性：vLLM 与 HuggingFace 模型无缝集成，支持多种流行的大型语言模型，简化了模型部署和推理的过程。兼容 OpenAI 的 API 服务器。
分布式推理：框架支持在多 GPU 环境中进行分布式推理，通过模型并行策略和高效的数据通信，提升了处理大型模型的能力。
开源共享：vLLM 由于其开源的属性，拥有活跃的社区支持，这也便于开发者贡献和改进，共同推动技术发展。

```
# 升级pip
python -m pip install --upgrade pip
# 更换 pypi 源加速库的安装
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install modelscope==1.11.0
pip install openai==1.17.1
pip install torch==2.1.2+cu121
pip install tqdm==4.64.1
pip install transformers==4.39.3
# 下载flash-attn 请等待大约10分钟左右~
MAX_JOBS=8 pip install flash-attn --no-build-isolation
pip install vllm==0.4.0.post1

```
MAX_JOBS=8: 这是一个环境变量设置，用于指定可以并行执行的最大任务数（jobs）。在这个例子中，将最大并行任务数设为了 8。这通常用于加速编译过程，尤其是在安装那些包含需要编译的 C 或 C++ 扩展的 Python 包时。
pip install flash-attn: 这是使用 pip（Python 的包管理工具）来安装一个叫做 flash-attn 的包。flash-attn 是一个针对高效注意力机制计算优化的库，常用于加速深度学习模型中的注意力层计算。
--no-build-isolation: 这个选项告诉 pip 不要创建一个隔离的构建环境来安装包。通常，pip 会尝试在一个独立的环境中构建包，这样可以确保不同包之间的依赖不会互相冲突。但是，在某些情况下，比如当你的系统已经正确配置了所有必要的构建依赖时，禁用构建隔离可能会加快安装过程。需要注意的是，这样做可能会导致依赖冲突的问题，特别是在处理复杂的依赖关系时。



## 参考

[[大模型]Qwen2-7B-Instruct vLLM 部署调用_vllm qwen2-CSDN博客](https://blog.csdn.net/FL1623863129/article/details/139693141)