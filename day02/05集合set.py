"""
集合 (Set)
    特点：
        无序 , 不重复
    创建方式：
        使用{} ，注意 里面不给元素 只能用 set（） 创建，否则就是一个字典
        使用 set（）
    原理：
        类似一个只有key，没有value 的字典
    应用场景：
        去重
        数学的集合运算

"""

s1 = {1,2,3}

# 使用set（）创建
s2 = set([1, 2, 2, 3]) # {1, 2, 3} 自动去重
print(type(s2))

s3 = set() # 注意：空集合必须用 set()，{} 是空字典

names = ['Tom', 'Jerry', 'Tom', 'Spike']
name_set=set(names)
print(name_set)

#常用方法：
# 追加
name_set.add("jim")
print(name_set)
# 添加多个元素
name_set.update(["孙红雷","黄渤"])
print(name_set)
# 删除元素 (不存在的话会报错)
name_set.remove("孙红雷")
print(name_set)
# 删除元素 (不存在不报错)
name_set.discard("孙悟空")
# 随机弹出元素
name_set.pop()
print(name_set)
# set 每次输出的顺序经常会乱 先转成list有序的，然后用sorted（）排序

name_set_list =list (name_set)
list_123=sorted(name_set_list, key=name_set_list.index)
print(list_123)

# 清空集合
name_set.clear()
print(name_set)


"""
=======================
集合运算 (交并差)

"""
python_devs = {'Tom', 'Jerry', 'Spike'}
java_devs = {'Tom', 'Tyke'}

mini_python_devs = {'Tom', 'Jerry'}

print(python_devs & java_devs)  # 交集 (都会的人): {'Tom'}
print(python_devs | java_devs)  # 并集 (所有人): {'Tom', 'Jerry', 'Spike', 'Tyke'}
print(python_devs - java_devs)  # 差集 (只会Python): {'Jerry', 'Spike'}
print(python_devs ^ java_devs)  # 对称差集 (只懂一门的): {'Jerry', 'Spike', 'Tyke'}

# 集合常用判断
"""
方法	                描述
isdisjoint()	    是否无交集
issubset()	        是否为子集 (<=)
issuperset()	    是否为父集 (>=)
"""
print(python_devs.isdisjoint(java_devs)) #false

print(java_devs.issubset(python_devs))  #f

print(mini_python_devs.issubset(python_devs)) #t

print(python_devs.issuperset(java_devs)) #f

print(python_devs.issuperset(mini_python_devs)) #t