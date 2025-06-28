<h1 align="center">PrecisionBoost</h1>

<p align="center">
<a href="https://github.com/destinybird/PrecisionBoost"><img src="https://img.shields.io/badge/GitHub-24292e" alt="github"></a>
<a href="https://www.modelscope.cn/models/suxinchun/PrecisionBoost"><img src="https://img.shields.io/badge/ModelScope-blueviolet" alt="modelscope"></a>
</p>

<div align="center">

**在线体验：[ModelScope PrecisionBoost](https://www.modelscope.cn/models/suxinchun/PrecisionBoost)**
</div>

<div align="center">
👋 联系我们: 22300240012@m.fudan.edu.cn
</div>

<div align="center">
<img src="https://github.com/destinybird/PrecisionBoost/blob/master/华佗.jpg" alt="PrecisionBoost Logo"/>
</div>

<br>

## 🌈 项目简介

**PrecisionBoost** 是一个专注于医疗问答的机器学习项目，基于 Qwen 模型，通过创新的两阶段知识蒸馏框架，从大型语言模型中提炼知识，优化小型模型在医疗领域的推理能力。项目涵盖通用医疗与消化系统问答场景，提供高效、可靠的解决方案。


## 📅 模型列表

| 模型名称 | 平台 | 链接 |
| :------: | :----: | :----: |
| PrecisionBoost | ModelScope | [PrecisionBoost](https://www.modelscope.cn/models/suxinchun/PrecisionBoost/files) |
| PrecisionBoost-digestive | ModelScope | [PrecisionBoost-digestive](https://www.modelscope.cn/models/suxinchun/PrecisionBoost-digestive/files) |

## 📚 数据与代码

包含医疗问答数据集和脚本，支持数据处理与模型微调，数据源自公开资源并经优化。

## 🔓 使用方法

以下是使用 PrecisionBoost 模型进行医疗问答的示例：

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(task=Tasks.text_generation, model='suxinchun/PrecisionBoost')

query = "消化不良的常见原因是什么？"

prompt = f"### 问题：\n{query}\n\n### 回答：\n"
result = pipe(prompt)
print(result['text'])
```

**输出示例**：
```
### 问题：
消化不良的常见原因是什么？

### 回答：
消化不良的常见原因包括饮食不当（如过量进食或辛辣食物）、胃肠道疾病（如胃炎、胃食管反流）、压力或焦虑、药物副作用等。建议咨询医生以明确诊断。
```

## 🎓 致谢

感谢以下项目与平台的支持：
- [Qwen](https://github.com/QwenLM/Qwen)：提供基座模型与技术支持。
- [ModelScope](https://www.modelscope.cn/)：模型托管与在线体验平台。
- [CMExam](https://github.com/williamliujl/CMExam) 与 [MedQA](https://github.com/jind11/MedQA)：提供高质量医疗数据集。

项目 logo 来自三国杀。



---

## PrecisionBoost (English Version)

### Project Overview

**PrecisionBoost** is a medical question-answering project built on the Qwen model, leveraging a novel two-stage knowledge distillation framework. By distilling knowledge from large language models, it optimizes small models for robust reasoning in general medical and digestive system domains, offering efficient and reliable solutions.


### Model List

| Model Name | Platform | Link |
| :--------: | :------: | :----: |
| PrecisionBoost | ModelScope | [PrecisionBoost](https://www.modelscope.cn/models/suxinchun/PrecisionBoost/files) |
| PrecisionBoost-digestive | ModelScope | [PrecisionBoost-digestive](https://www.modelscope.cn/models/suxinchun/PrecisionBoost-digestive/files) |

### Data and Code

The project includes medical question-answering datasets and scripts for data processing and model fine-tuning, sourced from curated public resources.

### Usage

```python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(task=Tasks.text_generation, model='suxinchun/PrecisionBoost')

query = "What are common causes of indigestion?"

prompt = f"### Question:\n{query}\n\n### Answer:\n"
result = pipe(prompt)
print(result['text'])
```

**Output Example**:
```
### Question:
What are common causes of indigestion?

### Answer:
Common causes of indigestion include improper diet (e.g., overeating or spicy foods), gastrointestinal disorders (e.g., gastritis, GERD), stress or anxiety, and medication side effects. Consult a doctor for a precise diagnosis.
```

### Acknowledgments

Thanks to [Qwen](https://github.com/QwenLM/Qwen), [ModelScope](https://www.modelscope.cn/), [CMExam](https://github.com/williamliujl/CMExam), and [MedQA](https://github.com/jind11/MedQA) for their support.

The project logo is sourced from *Three Kingdoms Kill*.

