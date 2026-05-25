import sys

"""
    列表生成就是生成整个列表
    而生成器就是记录一个计算公式，等你需要取值的 时候 才会去 消耗内存计算或者去储存
"""

# 用列表储存
my_list =[i for i in range(10000)]

print(my_list)
print(sys.getsizeof(my_list))

my_generator = (i for i in range(100000) if i % 2 == 0)
print(my_generator)
print(sys.getsizeof(my_generator))

"""
生成器怎么取值： next(xxx)
"""
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

"""也可以遍历取值"""
for  i  in  my_generator:
    # print(i)
    pass
