"""
列表切片
    list[开始 :结束 :步长 ]
        开始              不写从头开始取
              结束        不写取到尾巴
                    步长  为负数翻过来取
        包含   不包括
"""
mylist=[1,2,3,4,5,6,7,8,9]
print(mylist)

mylist2=mylist[:]
print(mylist2)


mylist3=mylist[:3]
print(mylist3)

mylist4=mylist[3:]
print(mylist4)

mylist5=mylist[:]
print(mylist5)

mylist6=mylist[::-1]
print(mylist6)

mylist7=mylist[::-2]
print(mylist7)


