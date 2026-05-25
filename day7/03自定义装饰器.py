"""
装饰器本质就是一个函数： 传入一个函数作为参数，返回一个新的函数
    类似扩展这个函数的功能，相当于Java里面的aop 面向切面编程
"""


"""新的需求，在计算前后在控制台打印日志"""
# def record_logging(fun):
#     def wapp(*args,**kwargs):
#         print(f"{fun.__name__}传入的参数有{args}或者{kwargs}")
#
#         rst = fun(*args,**kwargs)
#         print(f"{fun.__name__}返回的结果是{rst}")
#         return rst
#     return wapp
#
# """定义一个简单函数"""
# @record_logging
# def add(a:int , b: int) -> int:
#     return  a + b
#
# add(2,4)


def before_after(func):
    def wrapper(*args, **kwargs):
        print("开始执行")
        res1 = func(*args, **kwargs)
        print("结束执行")
        return res1
    return wrapper

@before_after
def hello(name):
    print(f"你好，{name}")
    return "执行完成"


print(hello("张三"))

