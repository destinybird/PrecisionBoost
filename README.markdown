## PrecisionBoost（中文版）

### 项目简介
PrecisionBoost 是一个基于 Qwen 模型的机器学习项目，专注于医疗领域的问答任务，通过 LoRA 微调优化模型性能。项目包括通用医疗问答和消化系统领域的模型和数据集，最终模型为 `output_merged_Qwen72B`（通用）和 `output_merged_digestive`（消化系统）。

### 模型文件
由于模型文件较大，训练好的模型托管在 ModelScope 上，可从以下链接下载：
- **PrecisionBoost 通用模型**：[ModelScope PrecisionBoost](https://www.modelscope.cn/models/suxinchun/PrecisionBoost/files)
- **PrecisionBoost 消化系统模型**：[ModelScope PrecisionBoost-digestive](https://www.modelscope.cn/models/suxinchun/PrecisionBoost-digestive/files)

### 文件列表
本仓库包含以下 10 个文件：
1. **`ChatMed.csv`**：医疗问答测试集，来自 [CMExam](https://github.com/williamliujl/CMExam/blob/main/data/train.csv)。
2. **`q&a.csv`**：通用问答测试集。
3. **`Qwen72B.json`**：通用训练和测试数据集，对应 `output_merged_Qwen72B` 模型。
4. **`digestive_Qwen2_72b_Instruction.json`**：消化系统指令数据集，来自 [MedQA](https://github.com/jind11/MedQA)，已拆分为训练和测试集。
5. **`digestive_Qwen2_72b_Instruction_train.json`**：消化系统训练集。
6. **`digestive_Qwen2_72b_Instruction_test.json`**：消化系统测试集。
7. **`merged_Qwen72B.json`**：合并的通用数据集。
8. **`merged_digestive.json`**：合并的消化系统数据集。
9. **`ceshi_first_100_from_json.py`**：用于从 JSON 文件提取前 100 条记录的 Python 脚本。
10. **`finetune/finetune_lora_single_gpu.sh`**：单 GPU LoRA 微调的 Bash 脚本。

### 模型性能
- **output_merged_Qwen72B**（通用）：
  - 整体正确率：27.33%。
  - `ChatMed.csv` 测试集：89%。
  - `q&a.csv` 测试集：26.13%。
- **output_merged_digestive**（消化系统）：
  - 整体正确率：59.69%（训练集 59.6%，测试集 62.5%）。
- **基线对比**：
  - 原始 Qwen-7B：33%（通用），34.17%（消化系统训练）。
  - Qwen2-72B-Instruct：83%（`q&a.csv`），96%（`ChatMed.csv`），73.5%（消化系统测试）。

### 使用说明
1. **下载模型**：从 ModelScope 链接获取 `output_merged_Qwen72B` 和 `output_merged_digestive`。
2. **准备数据**：使用 `ChatMed.csv`、`q&a.csv` 或 JSON 文件进行测试或训练。
3. **运行脚本**：
   - 使用 `ceshi_first_100_from_json.py` 处理 JSON 数据。
   - 使用 `finetune/finetune_lora_single_gpu.sh` 进行微调（需调整路径和参数）。
4. **环境要求**：安装 PyTorch、ModelScope SDK 等依赖，参考 ModelScope 文档。

### 联系方式
如有问题或合作意向，请联系 `suxinchun`。

---

## PrecisionBoost (English Version)

### Project Overview
PrecisionBoost is a machine learning project based on the Qwen model, focusing on medical question-answering tasks. It leverages LoRA fine-tuning to enhance model performance in general and digestive system domains. The final models are `output_merged_Qwen72B` (general) and `output_merged_digestive` (digestive system).

### Model Files
Due to their large size, the trained models are hosted on ModelScope. Download them from:
- **PrecisionBoost General Model**: [ModelScope PrecisionBoost](https://www.modelscope.cn/models/suxinchun/PrecisionBoost/files)
- **PrecisionBoost Digestive Model**: [ModelScope PrecisionBoost-digestive](https://www.modelscope.cn/models/suxinchun/PrecisionBoost-digestive/files)

### File List
This repository contains the following 10 files:
1. **`ChatMed.csv`**: Medical question-answering test dataset, sourced from [CMExam](https://github.com/williamliujl/CMExam/blob/main/data/train.csv).
2. **`q&a.csv`**: General question-answering test dataset.
3. **`Qwen72B.json`**: General training and test dataset, corresponding to the `output_merged_Qwen72B` model.
4. **`digestive_Qwen2_72b_Instruction.json`**: Digestive system instruction dataset, sourced from [MedQA](https://github.com/jind11/MedQA), split into training and test sets.
5. **`digestive_Qwen2_72b_Instruction_train.json`**: Digestive system training dataset.
6. **`digestive_Qwen2_72b_Instruction_test.json`**: Digestive system test dataset.
7. **`merged_Qwen72B.json`**: Merged general dataset.
8. **`merged_digestive.json`**: Merged digestive system dataset.
9. **`ceshi_first_100_from_json.py`**: Python script to extract the first 100 records from JSON files.
10. **`finetune/finetune_lora_single_gpu.sh`**: Bash script for LoRA fine-tuning on a single GPU.

### Model Performance
- **output_merged_Qwen72B** (General):
  - Overall accuracy: 27.33%.
  - `ChatMed.csv` test set: 89%.
  - `q&a.csv` test set: 26.13%.
- **output_merged_digestive** (Digestive System):
  - Overall accuracy: 59.69% (training 59.6%, test 62.5%).
- **Baseline Comparison**:
  - Original Qwen-7B: 33% (general), 34.17% (digestive training).
  - Qwen2-72B-Instruct: 83% (`q&a.csv`), 96% (`ChatMed.csv`), 73.5% (digestive test).

### Usage
1. **Download Models**: Obtain `output_merged_Qwen72B` and `output_merged_digestive` from ModelScope links.
2. **Prepare Data**: Use `ChatMed.csv`, `q&a.csv`, or JSON files for testing or training.
3. **Run Scripts**:
   - Process JSON data with `ceshi_first_100_from_json.py`.
   - Fine-tune models using `finetune/finetune_lora_single_gpu.sh` (adjust paths and parameters as needed).
4. **Environment**: Install dependencies like PyTorch and ModelScope SDK. Refer to ModelScope documentation.

### Contact
For questions or collaboration, contact `suxinchun`.