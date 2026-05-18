from operator import length_hint

a = 7
b = 3
print(a / b) # 真除
print(a // b)  #保留整数
print(a % b)   #保留余数  求模
print(a ** b)  # 7的3次方

# 海象运算符 (:=)：Python 3.8+ 新增，核心优势是 “在表达式内部赋值”，避免重复计算。

text = "12"

if(length := len(text))>3:
    print(f"长度足够，长度有{length}")
else:
    print(f"长度不够，只有{length}")

# 比较运算符
# 用于比较两个值的大小 / 是否相等，返回结果永远是布尔值（True/False）

print(3 > 2)     # True
print(3 < 2)     # False
print(3 == 3)    # True
print(3 != 3)    # False

# 链式比较（Python 特有，Java 不支持）

age = 66
if(18<age<60):
    pass
else:
    print("你不符合开车年龄")



# 逻辑运算符
# 用于组合多个布尔条件，核心是and（与）、or（或）、not（非），具有短路特性（提升执行效率）。

age1 = 55
print(age1>=18 and age1<=65)

print(age1<=18 or age1>=65)

print( not age1< 69)

# 短路特性示例（第二个表达式不会执行）
print(False and (1/0))  # 不会报错，因为False and 直接返回False
print(True or (1/0))    # 不会报错，因为True or 直接返回True

print(True and (1/0))  #会报错，因为 and 前后为 True 还得 判断 后面是否为 True
print(False or (1/0))  #会报错，因为 or 前后为 False 还得 判断 后面是否为 False

