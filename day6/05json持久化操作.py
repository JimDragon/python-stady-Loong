""""
 json.dump/json.load（文件级别：持久化操作）


dump：将 Python 对象序列化后直接写入文件（一步完成 “序列化 + 写文件”）；
load：从 JSON 文件中读取内容，并反序列化为 Python 对象（一步完成 “读文件 + 反序列化”）。

"""

import json

# 1. 定义要写入文件的Python数据（列表+字典）
user_list = [
    {"name": "Tom", "age": 18, "city": "北京"},
    {"name": "Jerry", "age": 20, "city": "上海"},
    {"name": "Alice", "age": 19, "city": "广州"}
]

# 2. 序列化并写入JSON文件
file_path = "users.json"
with open(file_path, "w", encoding="utf-8") as f:
    # 关键参数：
    # - ensure_ascii=False：保留中文
    # - indent=2：格式化输出（缩进2个空格），便于阅读/调试（生产环境可省略，减少文件体积）
    json.dump(user_list, f, ensure_ascii=False, indent=2)

# 3. 从JSON文件读取并反序列化
with open(file_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("从文件读取的Python对象：")
print(loaded_data)
print("第一个用户的姓名：", loaded_data[0]["name"])  # 输出：Tom
print("数据类型：", type(loaded_data))  # 输出：<class 'list'>