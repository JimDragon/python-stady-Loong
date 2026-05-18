# 成员运算符
# 用于判断 “元素是否在容器中”，核心是in（存在）、not in（不存在），支持字符串、列表、元组、字典等。
# 字符串中判断子串
text = "hello world"

print(("he" in text))
print(("djb" not in text))

# 列表/元组中判断元素

mylist = [1,2,3,4,5,6,7,8,9,10]
print((11 in mylist))
print((1 not in mylist))


# 字典中默认判断key（不是value）

myMap={"name":"张飞","age":18}
print(("name" in myMap))
print(("张飞" in myMap.values()))

# 身份运算符
# 用于判断 “两个变量是否指向同一个内存地址”，核心是is、is not。
# Java 核心差异（非常重要）：
# ● Python is ≈ Java ==：比较内存地址（Reference Equality）。
# ● Python == ≈ Java equals()：比较值（Value Equality）。
# 绝大多数情况下（判断数值、字符串内容），请使用 ==。只有判断 None 时推荐使用 is

'''
大飞总结：
  == 比较值 
  is 比较地址  小整数-5~256 共用  其他不共用
'''

# 示例1：小整数池（Python优化，-5~256的整数共用地址）
x = 10
y = 10

print(x == y)
print(x is y)

# 示例2：大整数（超出小整数池，地址不同）
a = 257
b = 257

print(a == b)
print(a is b)

# 示例3：None的判断（推荐用is）
x = None

print(x is None)
print(x == None)
print(x is not None)

#  运算符优先级
# 当一个表达式中有多个运算符时，Python 会按优先级依次计算（优先级高的先算），优先级从高到低核心顺序：

'''
大飞总结：
    杨幂优先，先乘除，求模 整除  加减法  然后是比较 然后是什么 not and or
'''
# 示例：按优先级计算
result = 2 + 3 * 4 **2  # 先算4²=16 → 再算3×16=48 → 最后算2+48=50
print(result)  # 50

# 技巧：不确定优先级时，用()括号强制改变顺序（更易读）
result = (2 + 3) * (4 **2)  # 先算2+3=5、4²=16 → 再算5×16=80
print(result)  # 80



