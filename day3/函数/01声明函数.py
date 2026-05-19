def hello():
    """
    这是一个入门定义方法
    :return: none
    """
    print("hello function")

hello()

#函数也是对象 ，可以将函数赋值给变量
hello2 = hello
hello2()

#获取方法里面的文档注释
print(help(hello))
print(hello.__doc__)


#一个有传参 有返回值的函数
def my_sum(a,b,c):
    """
    这是一个3个数字求和的函数
    :param a: 第一个参数
    :param b: 第二个参数
    :param c: 第三个参数
    :return: 返回3个参数的和
    """
    return a+b+c


print(my_sum(1, 2, 3))
