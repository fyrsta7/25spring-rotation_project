# 结合大模型的程序优化

本仓库是熊英飞老师组为 2025 年北京大学图灵班轮转设计的实践项目之一，主要涉及和大模型相关的程序优化技术。

如果在完成项目的过程中遇到了任何问题，请随时通过微信或者邮件 (zhaoyuwei@stu.pku.edu.cn) 与负责的同学联系。另外，请大家善用大模型，可以解决大家在写代码时遇到的很多问题。

## 项目概述

### 动机

程序优化在现代计算领域具有重要意义，它直接关系到软件的执行效率、资源利用率以及用户体验。在性能需求不断提高和硬件环境日益复杂的背景下，传统的优化手段往往面临规则设计繁琐、自动化程度不足等瓶颈。而大模型凭借强大的自然语言理解与生成能力，以及在模式识别和知识推理中的卓越表现，为解决这些问题提供了新的可能。通过将大模型应用于程序优化任务，我们可以探索更加智能化、自动化的优化手段，从而提升程序开发效率并实现更高效的代码性能。

### 主要构成

- part1：尝试使用 api 来调用大模型，了解 api 相关的设置。尝试获取代码库中的 commit 信息。了解提示工程技术。
- part2：尝试使用大模型来完成给定的程序优化任务，在具体的任务上对比不同 prompt 的效果。
- part3：阅读相关论文。
- part4：选择一个路线并进一步探索。可以根据给定的路线来探索，或者尝试复现论文并提出改进。

注意：part2 和 part3 的顺序不是固定的，可以交叉完成。

### 时间安排

完成基础任务：
- part1：1周
- part2：1.5周
- part3：1.5周
- part4：1周

分配更多时间给后续探索：
- part1：1周
- part2：1-1.5周
- part3：1周
- part4：1.5-2周


## part 1

在开展具体的项目之前，我们需要了解并尝试使用基本的工具。该部分的构成如下：
- 1.0：简单学习 Git 以及命令行的使用
- 1.1：尝试使用 api 来调用大模型，了解 api 相关的设置
- 1.2：了解提示工程技术
- 1.3：尝试获取代码库中的 commit 信息

### 1.0

（有任何问题都可以先问大模型）

- 学习命令行的基本使用方式
    - 参考 https://missing-semester-cn.github.io/2020/shell-tools/
- 运行 python 脚本
    - 在本地配置 python 环境，并尝试在命令行运行 `python hello_world.py`
    - 如果需要的话，可以尝试使用 pyenv 工具管理 python 版本。
- 学习 Git
    - 参考 https://missing-semester-cn.github.io/2020/version-control/
    - 了解如何进行简单的版本管理
- 了解 GitHub 的主要用法，例如可以从以下几个问题入手
    - 配置环境，并在命令行使用 `git clone` 来下载代码，例如可以下载本项目。尝试使用 `git pull` 来获取代码库的更新。
    - 尝试在 GitHub 网页上查看 commit 信息。
    - 尝试在 GitHub 上创建仓库，并使用 `git push` 将本地的代码同步更新到 GitHub。
        - 注意：如果你需要在本项目的基础上进行修改，并希望将代码保存到 GitHub，请另外新开一个仓库来存储你自己的代码，而不要直接修改本项目对应的仓库。例如你可以使用 GitHub 上的 fork。

### 1.1

#### 1.1.1 - 尝试使用 api 来调用大模型

使用组内的[大模型门户](https://llm.xmcp.ltd/)来获取 api key，目前可以调用 DeepSeek、通义千问、OpenAI 等模型，每位同学的限额是每月100刀。组内统一报销费用，只能用于自己的科研轮转项目，不能转借或者倒卖。

`test_api.py` 中是一个简单的大模型调用示例。
你需要先创建 `config.py` 文件，将大模型调用相关的变量（包括 `xmcp_base_url`, `xmcp_api_key`, `xmcp_model`）放在里面。注意保护好自己的 api key，防止泄露。如果要在 GitHub 上存放项目，注意不要将 api key 同步更新上去。如果发现 api key 有可能已经泄露，请立刻联系管理员充值秘钥。
然后你可以使用 `python test_api.py` 来运行 `test_api.py`。


#### 1.1.2 - 了解 api 相关的设置

参考以下资料了解如何通过 api 调用大模型以及相关的参数设置（OpenAI 和 DeepSeek 用的同一个库，所以可以先阅读 DeepSeek 文档，了解基本设置）：
- https://api-docs.deepseek.com/zh-cn
- https://platform.openai.com/docs
- https://cookbook.openai.com/

主要的设置包括：
- message：https://api-docs.deepseek.com/zh-cn/
    - role
    - content
- temperature：https://api-docs.deepseek.com/zh-cn/quick_start/parameter_settings
- logprobs: https://cookbook.openai.com/examples/using_logprobs & https://api-docs.deepseek.com/zh-cn/api/create-chat-completion
- 对话补全：https://api-docs.deepseek.com/zh-cn/api/create-chat-completion
- JSON Output：https://api-docs.deepseek.com/zh-cn/guides/json_mode
- 上下文硬盘缓存：https://api-docs.deepseek.com/zh-cn/guides/kv_cache
- ...

尝试编写脚本来通过 api 调用大模型，尝试调整输入的参数以及获取输出的各类信息。


### 1.2 - 了解提示工程技术

参考以下资料了解提示工程技术：
- https://www.promptingguide.ai/zh

主要技术包括：
- 零样本提示
- 少样本提示
- 链式思考（CoT）提示
- 检索增强生成 (RAG)
    - https://www.promptingguide.ai/zh/techniques/rag
    - https://www.zhihu.com/tardis/zm/art/675509396?source_id=1003
    - https://arxiv.org/abs/2005.11401: 提出 RAG 技术的论文
        - https://blog.csdn.net/weixin_43221845/article/details/142610477: 随便找的一个论文解读
- ...


### 1.3 - 尝试获取代码库中的 commit 信息

编写脚本，在给定代码库以及 commit hash 后，自动获取 commit 中的所有信息。主要有以下两种思路：
- （后续主要用到的方案）如果 commit 集中来自于一个或多个代码库，可以考虑将整个代码库下载到本地，并且直接从 git 信息中获取需要的部分
- 如果 commit 分散在许多不同的代码库，可以考虑直接调用 GitHub api，获取对应的 commit 信息。GitHub api 有调用频率的限制，主要有以下几种解决方法。
    - 多注册几个账号获得更多的 key
    - 纯等待，例如每调用一次 api 之后 sleep(n)
    - 改用第一种方法

可以使用[RocksDB](https://github.com/facebook/rocksdb)代码库来尝试实现上述功能

## part 2

在这一部分，我们将在给定的 task 上尝试使用一些 prompt 技术，并对比效果。该部分的构成如下：
- 2.1：使用大模型来判断一个 commit 的主要目的是否为性能优化
- 2.2：使用大模型尝试优化一段代码

该部分将继续使用[RocksDB](https://github.com/facebook/rocksdb)代码库。

### 2.1

判断一个 commit 的主要目的是否为性能优化

- 从代码库的git信息中直接获取commit信息
- 使用不同的prompt让大模型给出答案
    - 如何让大模型只回答 true / false / unknown（在大模型不确定的时候就回答unknown）
    - 如何提高大模型的回答准确率
    - 是否有一些类型的任务大模型认为不是性能优化，但在人类判断的结果上属于性能优化？比如优化内存访问的效率
- 提高大模型回答的置信度（选做，不是非常重要）
    - 尝试获得输出token的置信度
    - 根据置信度判断，大模型是否在某些时刻实际上比较确定但回答了unknown，在某些时刻实际上不确定但回答了true/false
    - 如何优化上述问题

### 2.2

使用大模型尝试优化一段代码（即尝试复现某个只修改了一个函数的 commit 中的优化），主要有以下两种优化思路：
- 2.2.1：在所有任务上给统一的命令
- 2.2.2：在 prompt 中加入一些针对性的提示

在这一部分中，提供两类 comimt 可用于优化。你可以先从第一类中挑选几个并尝试优化，然后再考虑第二类中的 commit。
- 第一类 commit 来自[RAPGen](https://arxiv.org/abs/2306.17077)，这里的每个 commit 中都只做了 api 调用层面的修改。具体内容放在文件 `part2/rapgen_benchmark.json` 中，每个 commit 包含三方面信息，分别是所在的代码库，对应的 commit hash，以及被修改的文件名。
- 第二类 commit 来自[RocksDB](https://github.com/facebook/rocksdb)，这里的每个 commit 都只修改了一个函数。具体内容放在文件 `part2/rocksdb_benchmark.json` 中（但其中可能有一些错误，部分 commit 可能修改了不止一个函数，直接跳过即可。每个 commit 对应的 `github_commit_url` 字段是该 commit 所在的网址，可以直接在网页上确认该 commit 一共修改了哪些内容。）理论上来说，你可以在 part2.1 的基础上进一步做筛选，最终得到这里用到的 commit，例如筛选出只修改了一个文件中一个函数的 commit，但这些步骤比较繁琐，在此就直接跳过。

另外，在 2.2.3 中我们会判断优化后代码的正确性，包括语义是否保持不变以及是否实现了性能提升这两部分。
无论我们以何种方式实现代码优化，都需要在得到结果后进行判断，所以 2.2.3 的任务应该与 2.2.1 & 2.2.2 相结合。

#### 2.2.1

在所有任务上给统一的命令，作为 baseline 方法。

- 只进行一轮对话。直接和大模型说：请你分析以下代码中是否存在性能优化的可能，请给出三种可能的性能优化方式，并给出你的优化结果
    - 分析大模型给出的优化方式有哪些类型，是否有一些是我们不想要的（例如提升代码可读性、可维护性等），调整prompt来规避这些可能。
    - 判断大模型给出的优化是否是正确的方向，以及优化的结果是否保持语义不变并且有真正的性能提升。
- 使用 CoT。引导大模型先阅读并理解给出的代码，然后分析有什么性能优化的机会，最后给出优化的结果。

#### 2.2.2

在 prompt 中加入针对该代码的一些提示，请尝试排列组合不同的提示内容以及不同的提示策略，并分析最终效果。

增加的提示内容可以分为以下两种：
- 只包含优化方向，不包含任何示例代码或者具体的修改方式
- 包含示例代码（优化前后的代码对比），并且该示例代码中的优化方式和我们现在想实现的优化方式基本类似，通过这种途径直接告诉大模型具体的修改方式

提示策略可以分为以下两种：
- 只进行一轮对话。人工判断里面有哪些可能的性能优化，并直接告诉大模型请你重点考虑xx方面的优化
- 使用 CoT。具体流程类似 2.2.1，但在大模型给出一些性能优化的方向之后，手动判断哪一种使我们最希望实现的，并引导大模型采用该种优化。

#### 2.2.3

判断优化后代码的正确性，主要包含以下两个方面：
- 语义是否保持不变
    - 若代码库中包含 unit test，尝试在优化前后分别运行
    - 人工判断
- 是否真正实现了性能提升
    - 若代码库中包含 performance test，尝试在优化前后分别运行
    - 人工判断

第一类 commit 没有直接可以使用的测试；第二类 commit 请参考 `part2/rocksdb_test.md` 来尝试运行 RocksDB 代码库中的 unit test 和 performance test，主要是运行 performance test。


## part 3

给定一些现有工作，阅读论文。可以先粗略过一遍所有论文，然后在优化小规模代码 / 大规模代码中选择一个感兴趣的方向进行精读。后续的 part4 也将在选择的方向上继续进行。

现有论文：
- 优化大规模代码
    - 同一个作者的前后两篇连续的工作
        - DeepDev-PERF：https://dl.acm.org/doi/abs/10.1145/3540250.3549096
        - RAPGen：https://arxiv.org/abs/2306.17077
    - performance bug
        - TANDEM: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9110902
        - A Large-Scale Empirical Study of Real-Life Performance Issues in Open Source Projects：https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9757842
- 优化小规模代码（算法竞赛题） - PIE 和 SBLLM 是比较主要的论文。
    - PIE：https://arxiv.org/abs/2302.07867
    - Learning to Improve Code Efficiency：https://arxiv.org/abs/2208.05297
    - Supersonic：https://ieeexplore.ieee.org/abstract/document/10606318/
    - SBLLM：https://arxiv.org/abs/2408.12159



## part 4（在 4.1.1 / 4.1.2 / 4.2 中选择一个方向完成）

该部分的构成如下：
- 4.1 考虑优化大规模代码
- 4.2 考虑优化小规模代码（算法竞赛题）

### 4.1

考虑优化大规模代码，主要方式有以下两种：
- 4.1.1：遵循现有路线，进一步向下探索
- 4.1.2：复现论文中的工具，自行提出一些改进策略并实现

#### 4.1.1
- 在不同 commit 之间交叉对比，寻找共同点
    - 分析不同 commit 实现的优化类型
    - 寻找优化方向类似的 commit
    - 根据上述结果，尝试搭建一个简单的分类系统，例如性能优化可以根据目的分成优化时间复杂度 / 空间复杂度，每一个大类下可以继续细分。
- 根据上述构建的分类系统，涉及prompt引导大模型给出每个 commit 的具体分类
    - 例如可以按照树结构，一层层询问大模型，并逐渐确定 commit 具体实现的优化类型
- 根据具体分类，引导大模型实现优化
    - 搭建一个通用的 prompt 框架
    - 根据具体分类，在 prompt 中加入针对性的提示，具体有以下两种形式
        - 该优化方式的总结，例如将 A 替换成 B
        - 该类优化的一个或多个具体例子，例如一段现有的代码（包含 A）和对应的优化后代码（包含 B）

#### 4.1.2

参考 part3 中给出的论文，复现现有的优化大规模代码的工具。

尝试组合不同论文中的技术，或改进现有技术，判断效果是否有所提升。

但目前想要复现可能还有一些额外的困难，例如 RAPGen 中需要构建知识库，就涉及到从 GitHub 爬所有相关的代码库，并在 commit 中筛选出所有实现了 api 替换的部分，需要调用程序分析工具等。并且 C# 的代码库数量较少，而 C/C++ 的代码库数量超级多。

### 4.2

参考 part3 中给出的论文，复现现有的优化小规模代码（算法竞赛题）的工具

尝试组合不同论文中的技术，或改进现有技术，判断效果是否有所提升。

PIE: https://github.com/LearningOpt/pie

SBLLM: https://github.com/shuzhenggao/sbllm


## TODO

- 完善提示工程中的主要技术
- 完善part2，例如给出具体用于优化的commit等
- 考虑每个part新建一个文件，将readme拆分到不同文件中？