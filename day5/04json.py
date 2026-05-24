"""

 json.dumps/json.loads（字符串级别：内存操作）


dumps（dump string）：将 Python 对象序列化为 JSON 格式的字符串（仅在内存中操作，不涉及文件）；
loads（load string）：将 JSON 格式的字符串反序列化回 Python 对象（dict/list 等）。
"""

import json  # 导入Python内置的json标准库

# 1. 定义一个Python字典（待序列化的对象）
python_data = {
    "name": "Tom",
    "age": 18,
    "is_student": True,
    "tags": ["python", "oop", "json"],
    "score": {"math": 95, "english": 88}
}

# 2. 序列化：Python对象 → JSON字符串
# 关键参数：ensure_ascii=False → 保留中文等非ASCII字符（不转成\uXXXX编码）
json_str = json.dumps(python_data, ensure_ascii=False)
print("JSON字符串：")
print(json_str)
print("数据类型：", type(json_str))  # 输出：<class 'str'>

# 3. 反序列化：JSON字符串 → Python对象
python_obj = json.loads(json_str)
print("\n反序列化后的Python对象：")
print(python_obj)
print("获取tags字段：", python_obj["tags"])  # 输出：['python', 'oop', 'json']
print("数据类型：", type(python_obj))  # 输出：<class 'dict'>