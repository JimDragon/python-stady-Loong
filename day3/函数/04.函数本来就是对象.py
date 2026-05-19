"""
在Python中，函数也是一种数据类型。
    所以，函数也是一个对象，它可以：
    ● 函数可以被赋值给变量
    ● 函数可以作为参数传递给其他函数
    ● 函数可以作为函数的返回值
    ● 函数可以存储在数据结构中
    这种特性使得Python支持高阶函数、闭包、装饰器等高级编程技术。

"""
"""
 赋值给变量   赋值的时候不要写()
            如果你想把函数赋值给变量写了(),那么就是把函数的返回值给变量了
                而不是把整个函数传给变量
"""
# 可以使用函数可以给变量赋值
def one ():
    print("one")
two=one
two()


"""
作为参数传递
# 函数可以作为参数传递
"""
def say_hi():

    print("Hi!")


def call_function(func):
    func()  # 这里要求传给func的实参是一个函数。

call_function(say_hi)  # say_hi是一个函数，它作为参数被传给了call_function函数

"""
作为返回值
"""

# 函数可以作为返回值
def get_function():
    def inner_function():
        print("Inner function")
    return inner_function

#调用get_function函数
func = get_function() # 得到的是一个函数
func() # 调用func()函数

"""# 2.8.4 存进数据结构"""
# 函数可以被存储到数据结构中
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# 将函数存储在列表中，同样也可以被存储在元组、字典等容器中
operations = [add, subtract, multiply, divide]
for operation in operations:
    result = operation(5, 3)
    print(operation.__name__ , ": ", result)