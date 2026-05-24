""""
读取文本文件（一次性读取）


适用于小文件（文件大小远小于内存），一次性将文件全部内容读取为一个字符串。
"""

# 定义文件路径（相对路径：相对于当前程序运行的目录；绝对路径：完整路径，如 C:/data.txt）
path = "data.txt"

# with 语句：自动关闭文件
# 参数说明："r" = 只读模式；encoding="utf-8" = 指定字符编码，读写中文必须显式指定
with open(path, mode="r", encoding="utf-8") as f:
    # read()：一次性读取文件的全部内容
    full_text = f.read()

# 打印读取到的内容
print(full_text)

"""
按行读取文本文件（逐行遍历）
适用于大文件（如日志文件、数据量巨大的文本），逐行读取并处理，不会一次性占用大量内存，是处理大文件的标准写法。
"""

path = "data.txt"

with open(path, mode="r", encoding="utf-8") as f:
    # 直接遍历文件句柄 f，会自动按行读取
    for line in f:
        # 注意：每行的末尾会自带一个换行符 \n
        # rstrip("\n")：移除行尾的换行符，避免打印时出现多余的空行
        cleaned_line = line.rstrip("\n")
        print(cleaned_line)