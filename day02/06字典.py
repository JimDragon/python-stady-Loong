"""
字典
    相当于Java 的 hashmap

    Key的要求：必须是不可变类型（如字符串、数字、元组），列表不能做 Key。
    创建方式：
        {}
        dict（）函数


"""
info = {"name": "Tom", "age": 18 ,"address" : "上海"}


d2 = dict(name="Jerry", age=20, address="重庆") # 使用工厂函数
print(d2)
# 2. 访问

print(info["name"])
print(info["age"])

print(info.get("sex"))     # None (安全访问，不存在不报错)
print(info.get("sex", "男")) # 男 (设置默认值)

# 修改
info["size"] = "28cm"    #没有key 就是新增
info["name"] = "jim"     #存在key 就是修改

if "name" in info:
    print(f"{'name'}存在")

# 常用的方法
print(info.keys())   #获取所有键 (视图对象)
print(info.values())  #获取所有值 (视图对象)

print(info.items())    #获取所有键值对 (返回元组列表)

info.update(d2)    #后面覆盖前面，没有则是添加
print(info)

#setdefault 存在就返回，不存在就添加这个key，还可以赋值
print(info.setdefault("name"))

info.setdefault("qq","818928912@qq.com")
print(info)

# 删除指定 key 并返回 value，不存在可给默认值
print(info.pop("qq"))
print(info)

# 删除并返回字典中最后一个键值对（Python 3.7+ 保持插入顺序
print(info.popitem())
print(info)

# clear()	清空字典所有元素

# copy()   浅拷贝字典
info3 = info.copy()
print(info3)

# dict.fromkeys(seq, val)   生成新字典，所有 key 对应同一个 value

info4 = dict.fromkeys(["x","y","z"],"霸气侧漏")
print(info4)


# 字典推导式

# 将两个列表组合成字典
keys = ['name', 'age', 'city']
values = ['Tom', 18, 'Beijing']
info5 = {k : v for k, v in zip(keys,values)}
# {'name': 'Tom', 'age': 18, 'city': 'Beijing'}

data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
group = {}
for category, name in data:
    group.setdefault(category, []).append(name)

    # {"fruit":["apple"]}
    # {"fruit":["apple", "banana"]}
    # {"fruit":["apple", "banana"],"veg":["carrot"]}

print(group)
# {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

# 遍历字典
d = {'a': 1, 'b': 2}
# 遍历 Key
for k in d:
    print(k)

# 遍历 Value
for v in d.values():
    print(v)

# 遍历 Key-Value
for k, v in d.items():
    print(f"{k} -> {v}")