import json

def convert_jsonl():
    # 定义输入和输出文件路径
    input_file = "data/wikipedia-cn-20230720-filtered/wikipedia-cn-20230720-filtered.json"
    output_file = "data/wikipedia-cn-20230720-filtered/wikipedia-cn-20230720-filtered.jsonl"

    # 读取 JSON 文件并转换为 JSONL 格式
    try:
        with open(input_file, "r", encoding="utf-8") as infile:
            data = json.load(infile)  # 假设输入文件为标准 JSON 格式

        with open(output_file, "w", encoding="utf-8") as outfile:
            for entry in data:
                json_line = json.dumps(entry, ensure_ascii=False)
                outfile.write(json_line + "\n")

        print(f"转换完成！JSONL 文件已保存到: {output_file}")

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == '__main__':
    convert_jsonl()
