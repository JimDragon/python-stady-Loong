#单行注释
'''
多行注释
'''

name = "龙大侠"

age = 27
print(id(age))
size = 20.8

is_china = True
is_usa = False


age = 26
brother_age = 26
#打印变量地址
print(id(age))
print(id(brother_age))
#打印变量类型
print(type(age))
print(name)
print(age)
print(size)
print(is_china)
print(is_usa)

#给多个变量赋同一个值
a = b = c = 345345
print(a)
print(b)
print(c)

#给多个变量赋同时赋值
aa,bb,cc=11,22,33
print(aa)
print(bb)
print(cc)


#常量赋值 常量用大写
PI=3.12341412423452351231123123145414
print(PI)
print(type(PI))



