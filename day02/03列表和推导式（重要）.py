mylist=[1,2,3,4,5,6]
mylist2=[7,8,9,10,11,12,13,14,15]
print(mylist)
print(mylist2)
# 求和
print(sum(mylist))
# 求最大值
print(max(mylist))
# 求最小值
print(min(mylist))
# 求两个列表的和，就是连接起来
print(mylist + mylist2)

# 两个列表相乘，报错！！！
pass

# 列表的乘法，就是列表循环多少遍
mylist3=mylist*2
print(mylist3)

print("**"*30)
print("推导式（重点）")

# 基本推导式
# 得出1-10里面所有的数
mylist5=[x for x in range(1,11)]
print(mylist5)

# 带条件推导式
# 得出1-10 里面的偶数
mylist4=[x for x in range(1,11) if x % 2 == 0]
print(mylist4)

# 嵌套推导式
# 拼接出所有花色的扑克牌
colors = ['♠', '♥', '♣', '♦']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

puke_list=[c + r for c in colors for r in ranks]
puke_list.extend(["big king","small king"])
print(puke_list)




