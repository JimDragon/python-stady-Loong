
"""
try / except / else / finally
"""

try:
    # 可能出错的代码放在 try 里
    x = int("123")
except ValueError:
    # 只处理你“预期会发生”的异常
    print("转换失败：不是合法数字")
else:
    # 没异常才会执行
    print("转换成功：", x)
finally:
    # 无论是否异常都会执行（常用于资源清理）
    print("不管成功失败都会执行到这里")

"""捕获多个异常"""

try:
    a = int("1")
    b = 10 / 0
except (ValueError, ZeroDivisionError) as e:
    print("发生错误：", e)

"""不建议：裸 except
    场景 1：用具体异常（推荐）
"""
try:
    # 步骤1：读文件
    with open("data.txt", "r") as f:
        content = f.read()
    # 步骤2：转数字（假设文件内容是字符串）
    num = int(content)
    # 步骤3：这里故意写错变量名（你没预料到的错误）
    print(numm)  # 变量名错了，会触发 NameError
except FileNotFoundError:
    # 只捕获“文件不存在”的异常
    print("错误：文件找不到")
except ValueError:
    # 只捕获“转换数字失败”的异常
    print("错误：文件内容不是合法数字")

"""!!!!!!!!场景 2：用裸 except（危险!!!!!!!!!!"""
try:
    with open("data.txt", "r") as f:
        content = f.read()
    num = int(content)
    print(numm)  # 变量名错误
except:  # 裸 except：捕捉所有异常
    print("出错了，但不知道为啥")