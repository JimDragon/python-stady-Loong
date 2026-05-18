'''
列表
    可变 有序 可重复  类型不限制
    创建方式
        []
        使用 list()

'''

# 创建一个普通列表
mylist = [1,2.2,True,"Stephen",[1,2,3]]
print(mylist)



#find mylist  Stephen
print(mylist[3])

# 查找 mylist 里面 列表 [1,2,3] 里面的3
print(mylist[4][2])

#修改 mylist 里面 True 为 False
mylist[2] =False
print(mylist)


print("+"*30)
# use list() make a list

mylist2=list(range(1,11,2))
print(mylist2)

# list 常用的函数
"""
增
| 方法                 | 用法                   | 说明                    |
| ------------------ | -------------------- | --------------------- |
| `append(x)`        | `lst.append(10)`     | 在列表末尾添加一个元素           |
| `extend(iterable)` | `lst.extend([1,2])`  | 在列表末尾一次性追加另一个可迭代对象的元素 |
| `insert(i, x)`     | `lst.insert(1, 'a')` | 在指定位置插入元素             |


删除：
| 方法          | 用法                         | 说明               |
| ----------- | -------------------------- | ---------------- |
| `pop([i])`  | `lst.pop()` / `lst.pop(1)` | 删除并返回指定位置元素，默认末尾 |
| `remove(x)` | `lst.remove(2)`            | 删除第一个匹配的元素值      |
| `clear()`   | `lst.clear()`              | 清空列表所有元素         |


查询
| 方法                         | 用法             | 说明            |
| -------------------------- | -------------- | ------------- |
| `index(x[, start[, end]])` | `lst.index(3)` | 返回第一个匹配元素的索引  |
| `count(x)`                 | `lst.count(2)` | 返回元素在列表中出现的次数 |

排序，反转
| 方法                              | 用法                                      | 说明                      |
| ------------------------------- | --------------------------------------- | ----------------------- |
| `sort(key=None, reverse=False)` | `lst.sort()` / `lst.sort(reverse=True)` | 原地升序排序，可选 key 和 reverse |
| `sorted(lst)`                   | `s = sorted(lst)`                       | 返回新排序列表，不修改原列表          |
| `reverse()`                     | `lst.reverse()`                         | 原地反转列表元素顺序              |


copy
| 方法       | 用法                  | 说明    |
| -------- | ------------------- | ----- |
| `copy()` | `lst2 = lst.copy()` | 浅拷贝列表 |

"""

mylist2.append("毕福剑")
print(mylist2)

mylist2.extend([1,2,3])
print(mylist2)

mylist2.insert(0,"gogogo")
print(mylist2)

print(mylist2.pop(3))
print(mylist2)

mylist2.remove("gogogo")
print(mylist2)


mylist2.clear()
print(mylist2)

#排序只支相同类型的数据排序 比如 数值排序  英文首字母排序  列表先排第一个元素，然后排下一个元素。。。 对象排序应该没有这个场景省略。。

mylist3=list(range(1,11,2))
print(mylist3)

print("lst.sort()用法 从小到大排")
mylist3.sort()
print(mylist3)

print("lst.reverse()用法 不是从大到小排 ，而是 反转")
mylist3.reverse()
print(mylist3)

# 排序后返回先列表
mylist4=sorted(mylist3)
print(mylist4)

mylistOver=mylist4.copy()
print(id(mylist4))

mylist5=mylist4
print(id(mylist5))
print(mylistOver)
print(id(mylistOver))




