import csv
import os
import torch
import json
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
import sys

# 设置设备
device = "cuda" if torch.cuda.is_available() else "cpu"

# 指定小模型路径
model_path = os.getenv('MODEL_PATH', "/cpfs01/projects-HDD/cfff-0082a359858b_HDD/sxc_22300240012/LLaMA-Factory/saves/output_yilun_hun_erlun_digestive")

# 从本地路径加载小模型和分词器
model = AutoPeftModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

# 读取 JSON 文件路径
json_input_file = "/cpfs01/projects-HDD/cfff-0082a359858b_HDD/sxc_22300240012/Qwen-main/Qwen-main/data/digestive_Qwen2_72b_Instruction_test.json"

# 动态获取小模型名称
model_name = os.path.basename(model_path)

# 定义处理行数
num_rows_to_process = 200

# 动态生成输出 CSV 文件路径
csv_output_file = f"test_result_digestive_for_test_{num_rows_to_process}_{model_name}.csv"
# 确保输出目录存在
output_dir = os.path.dirname(csv_output_file)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 创建 CSV 文件并写入表头
try:
    with open(csv_output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["问题", "答案", "小模型回复"])
except OSError as e:
    print(f"创建 CSV 文件时出错：{e}")
    sys.exit(1)

# 检查文件是否成功创建
if not os.path.exists(csv_output_file):
    print("CSV 文件未成功创建，程序退出。")
    sys.exit(1)

# 定义生成回复的函数
def generate_response(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    inputs = {key: value.to(device) for key, value in inputs.items()}
    outputs = model.generate(**inputs, max_new_tokens=450)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# 打开 JSON 文件并读取数据
with open(json_input_file, 'r', encoding='utf-8') as jsonfile:
    json_data = json.load(jsonfile)
    print(f"加载的数据条数: {len(json_data)}")

# 打开 CSV 文件用于写入结果
buffer = []  # 初始化缓冲区
buffer_size = 100  # 设置缓冲区大小

with open(csv_output_file, 'a', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    # 遍历前 num_rows_to_process 条数据
    for i, entry in enumerate(json_data):
        if i >= num_rows_to_process:
            break

        user_question = entry['conversations'][0]['value']
        assistant_answer = entry['conversations'][1]['value']

        # 提取"答案是"到"这是一些相关的背景信息"之间的部分
        if "答案是：" in assistant_answer and "这是一些相关的背景信息" in assistant_answer:
            extracted_answer = assistant_answer.split("答案是：")[1].split("这是一些相关的背景信息")[0].strip()
        else:
            extracted_answer = assistant_answer

        # 构建 Prompt
        prompt = f"你是一位医学专家，请先深呼吸，然后用中文一步一步地思考并回答这个问题，给出分点罗列的解释：问题：{user_question}？只解释这一个问题即可"

        # 生成模型的回复
        model_response = generate_response(model, tokenizer, prompt)

        # 将问题、提取的答案和生成的模型回复加入缓冲区
        buffer.append([user_question, extracted_answer.strip(), model_response.strip()])

        # 定期写入缓冲区到文件
        if len(buffer) >= buffer_size:
            try:
                writer.writerows(buffer)
                outfile.flush()  # 确保数据写入文件
                buffer.clear()  # 清空缓冲区
            except OSError as e:
                print(f"写入文件时出错：{e}")
                break  # 可根据需要处理错误

        # 获取当前 CSV 文件的大小
        file_size = os.path.getsize(csv_output_file)

        # 打印处理进度和 CSV 文件大小
        print(f"已处理 {i + 1}/{num_rows_to_process} 条，CSV 文件大小：{file_size} 字节", flush=True)

    # 写入剩余的缓冲区内容
    if buffer:
        writer.writerows(buffer)

# 最终输出 CSV 文件路径
print(f"所有数据的处理结果已保存到 CSV 文件：{csv_output_file}")
