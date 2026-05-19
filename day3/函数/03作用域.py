"""
主要讲解就是变量赋值问题:
    一句话解决:就近原则
        假设说一个变量在最小局部环境中去比他大环境作用域里取值
            首先就是找局部里面这个变量是否赋值
            然后找嵌入函数里面函数里面是否赋值
            然后找全局里面是否赋值 也就是这个.py文件里面是否声明赋值
            最后就是在python内裤里面去找
    反之:不能在大的作用域里面去取小作用域里面的值
"""

# =================变量作用域====================
# if-else语句块中定义变量，不会开启新的变量作用域
import random
a= random.randint(1,10) # 全局变量
if a>5:
    result = "big" # 全局变量，因为当前if不在函数，闭包中
    print("a的值是：",a)
else:
    result = "small"
print("result的值是：",result) # if-else语句块外，仍然可以访问result


# =================变量作用域====================
# 在函数中定义变量，会开启新的变量作用域
# G (Global): 模块级别变量
x = "global" # 全局变量
def outer():
    # E (Enclosing): 闭包
    y = "enclosing" # 外层函数变量，在整个outer函数中都可以访问

    # 在外部函数体中定义内部函数
    def inner():
        # L (Local): 函数内部变量
        z = "local" # 局部变量，仅限于inner函数内部访问
        print(f"\t在inner中访问局部变量z的值是：{z}")  # 访问局部变量
        print(f"\t在inner中访问嵌套变量y的值是：{y}")  # 访问外层函数变量
        print(f"\t在inner中访问全局变量x的值是：{x}")  # 访问全局变量
        print(f"\t在inner中访问内建函数的值是：{len}")  # 访问内建函数

    # 在外部函数体中调用内部函数
    print("在outer中调用inner函数")
    inner()
    # print(f"在outer中访问内层函数变量z的值是：{z}") # 报错
    print(f"在outer中访问外层函数变量y的值是：{y}")
    print(f"在outer中访问全局变量x的值是：{x}")
    print(f"在outer中访问内建函数的值是：{len}")

# 调用外部函数函数
print("调用outer函数")
outer()
# print(f"在main中访问内层函数变量z的值是：{z}") # 报错
# print(f"在main中访问外层函数变量y的值是：{y}") # 报错
print(f"在main中访问全局变量x的值是：{x}")
print(f"在main中访问内建函数的值是：{len}")

"""

# global
小作用域里面可以修改全局作用域里面定义的可变变量值(比如:list,无序集合set,字典dict),
但是不能修改全局作用域里面不可变变量值(比如:元组tuple,int,float,bool,str),会创建一个新的局部变量
如果说小作用域非要修改全局作用域里面的不可变变量值就要使用 global

"""

# =========可变类型在局部修改可以不使用global关键字===========
listDemo = [1,2,3] #  可变类型，全局变量
# 定义函数
def change_list():
    listDemo.append(4)
    print("change_list()函数中，listDemo的值是：",listDemo) # listDemo= [1,2,3,4]
    # listDemo = [4,5,6] # 错误，因为Python 默认会把这个变量当作局部变量

# 调用函数
print("调用change_list()函数之前，listDemo的值是：",listDemo)  # listDemo= [1,2,3]
change_list()
print("调用change_list()函数之后，listDemo的值是：",listDemo)  # listDemo= [1,2,3,4]


# =============未使用global关键字无法修改不可变类型全局变量的值=============
x = "global"
# 定义函数
def change_x_one():
    # x += "local" # 错误，因为没有global关键字，无法修改全局变量
    x = "local" # 没有global关键字，给x赋值，Python 默认会把这个变量当作局部变量
    print("change_x_one()函数中，x的值是：",x) # x= local

# 调用函数
print("调用change_x_one()函数之前，x的值是：",x) # x= global
change_x_one()
print("调用change_x_one()函数之后，x的值是：",x) # x= global
print()


# ===============使用global关键字才可以修改不可变类型全局变量的值=================
# global关键字，可以修改全局变量的值
x = "global"
# 定义函数
def change_x_two():
    global x # 添加global关键字，修改全局变量的值
    x = "local"
    print("change_x_two()函数中，x的值是：",x) # x= local

# 调用函数
print("调用change_x_two()函数之前，x的值是：",x) # x= global
change_x_two()
print("调用change_x_two()函数之后，x的值是：",x) # x= local
print()

"""
nonlocal 也用作内部作用域修改外部作用域的变量的场景，不过此时外部作用域不是全局作用域而是"嵌套作用域"。
"""

# ========使用nonlocal关键字在内部作用域修改外部作用域不可变类型变量的值==============
def function_outer():
    str_demo = "outer"
    print("function_outer()函数中，str_demo的值是：",str_demo)
    def function_inner():
        nonlocal str_demo
        str_demo = "inner"
    # 调用内部函数
    print("调用内部函数function_inner()后")
    function_inner()
    print("function_outer()函数中，str_demo的值是：",str_demo)

# 调用外部函数
function_outer()