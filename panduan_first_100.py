import csv
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置设备
device = "cuda" if torch.cuda.is_available() else "cpu"

# 指定本地模型路径
model_path = "/cpfs01/projects-HDD/cfff-0082a359858b_HDD/sxc_22300240012/Qwen2-72B-Instruct"

# 从本地路径加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 读取输入 CSV 文件路径
csv_input_file = "/cpfs01/projects-HDD/cfff-0082a359858b_HDD/sxc_22300240012/Qwen-main/Qwen-main/test_result_digestive_for_test_200_Qwen2-72B-Instruct.csv"

# 定义处理的行数
num_rows_to_process = 200

# 动态生成输出 CSV 文件路径
csv_output_file = f"test_result_judged_{num_rows_to_process}_{os.path.basename(csv_input_file)}"

# 打开 CSV 文件，读取问题和小模型的回复
with open(csv_input_file, 'r', encoding='utf-8', errors='ignore') as infile, open(csv_output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 写入表头
    header = next(reader)  # 跳过表头
    writer.writerow(header + ['判断结果'])  # 在输出文件中保留表头并添加新列

    # 初始化计数器
    total_processed = 0
    correct_count = 0
    incorrect_count = 0

    # 遍历文件中的每一行，处理指定数量的数据
    for row in reader:
        if total_processed >= num_rows_to_process:  # 只处理前 num_rows_to_process 条数据
            break
        
        try:
            user_question = row[0]
            answer = row[1]
            small_model_response_full = row[2]

            if "只解释这一个问题即可" in small_model_response_full:
                small_model_response = small_model_response_full.split("只解释这一个问题即可")[-1].strip()
            else:
                small_model_response = small_model_response_full.strip()

            prompt = f"这是一位小模型对问题的回复内容，根据其内容判断其是否做到了正确回复。问题：{user_question}？答案是：{answer}，小模型回复：{small_model_response}。如果正确，则只直接回复1。如果错误，则只直接回复2"

            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]

            text = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            model_inputs = tokenizer([text], return_tensors="pt").to(device)

            generated_ids = model.generate(
                model_inputs.input_ids,
                max_new_tokens=1
            )
            generated_ids = [
                output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]

            response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

            total_processed += 1
            if response == '1':
                correct_count += 1
            elif response == '2':
                incorrect_count += 1

            # 计算两个正确率
            accuracy_one = correct_count / total_processed if total_processed > 0 else 0
            accuracy_two = 1 - (incorrect_count / total_processed) if total_processed > 0 else 0

            row.append(response)
            writer.writerow(row)

            outfile.flush()

            file_size = os.path.getsize(csv_output_file)

            print(f"已处理 {total_processed} 条，判断结果：{response}，CSV 文件大小：{file_size} 字节，当前正确率1：{accuracy_one:.2%}，当前正确率2：{accuracy_two:.2%}", flush=True)

        except Exception as e:
            print(f"跳过错误行: {row}，错误信息：{e}", flush=True)
            continue  # 跳过当前行

print(f"所有数据处理完毕，结果已保存到 {csv_output_file}")
