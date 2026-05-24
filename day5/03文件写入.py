"""
写入文本文件
写入文件有两种核心模式：覆盖写入（"w"）和追加写入（"a"）。



模式 1：覆盖写入（"w"）
如果文件不存在，会自动创建；如果文件已存在，会清空原文件的所有内容，然后写入新内容。

"""
path = "out.txt"

with open(path, mode="w", encoding="utf-8") as f:
    # write() 方法：写入字符串
    # 注意：write() 不会自动添加换行符，需要手动在字符串末尾加 \n
    f.write("Hello, Python!\n")
    f.write("文件操作的核心是 with 语句\n")



"""
模式 2：追加写入（"a"）
如果文件不存在，会自动创建；如果文件已存在，会在文件的末尾追加新内容，原文件内容不会被修改。
"""
path = "out.txt"

with open(path, mode="a", encoding="utf-8") as f:
    # 追加一行内容到文件末尾
    f.write("这是追加的内容，不会覆盖原文件\n")