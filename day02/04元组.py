"""
元组
    特点：有序，不可变，可重复，类型不限
    创建方式：
        使用小括号创建(),如果元组里面只有一个元素，要在后面加一个逗号 (x,)
        使用tuple函数 , tuple()
    获取元组里面元素的方式：
        1.使用下标
        2.遍历
"""

my_tuple=(1,2,3)
print(my_tuple)

my_tuple1=(1,)
print(type(my_tuple1))
print(my_tuple1)

my_tuple2=tuple("hello")
print(type(my_tuple2))
print(my_tuple2)

print(my_tuple2[0])

for x in my_tuple2:
    print(x)

# 获取元组中元素的索引和元素

for x , y in enumerate(my_tuple2):
    print(f"下表为{x}的元素是{y}")




