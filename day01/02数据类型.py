'''
数据类型有哪些
数值类型
    整数
    浮点数
    布尔
    复数
字符串
容器
    列表
    元组
    集合
    字典
None
'''

num1 = 1
num2 = 1.2234
num3 = True
num4 = 1_000_000_000_000
num5 = "龙大侠学ai"

print(type(num1))
print(type(num2))
print(type(num3))
print(type(num4))
print(type(num5))

#布尔类型属于 int 类型的子类型
#👇验证
print(isinstance(num3, int))
print(isinstance(num3, bool))

#布尔类型可以和int计算
num6 = num3+num1
print(num6)
print(type(num6))

#数值 字符串  元组 不可变    列表 集合 字典 可以变

mylist = [1,2,3,4,5]
print(mylist)
print(id(mylist))
mylist[0] = 10
print(mylist)
print(id(mylist))

# 3️⃣ 元组（Tuple）
# 类型：tuple
#
# 特点：不可变序列，存有序元素，圆括号表示
t = (1, 2, 3)
t2 = ("a", "b", 1)

# 集合（Set）
# 空集合需要 set()，{} 是空字典
st = {1, 2, 3}
st2 = {"a", "b", "c"}


#none

def reslutNone():
    pass

reslt= reslutNone()

print(reslt)




