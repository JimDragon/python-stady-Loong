"""定义一个生成器：
        可以生成1 - n  的个数
"""
from collections.abc import Iterator

"""自己理解的写法"""
def my_range(n:int) :


    my_generator = (i for i in range(1,n+1))
    return my_generator


for i in  my_range(3):
    print(i)

"""老师引入yield   这个可以理解成3个步骤 暂停 return  下次调用next()当前步骤继续执行"""
def my_range2(n:int) ->Iterator[int]  :
    i1 = 1
    while i1 <= n:
        yield i1
        i1 += 1


print(my_range2(5))


