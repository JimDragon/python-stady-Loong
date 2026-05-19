#赋值
from copy import deepcopy

a = 10
b = 10
print(id(a))
print(id(b))

#浅copy   只拷贝非引用对象
my_list = [1, [2,3]]

my_list2 = my_list.copy()
print(id(my_list))
print(id(my_list2))

#修改非应用类型值，copy后的对象不会发生改变，如果是修改了 引用指向的对象 也会受到影响
my_list[0] = 10
print(my_list)  #[10, [2, 3]]
print(my_list2)  #[1, [2, 3]]

#修改引用类型的值
my_list[1][1] = 30
print(my_list)  #[10, [2, 30]]
print(my_list2)  # [1, [2, 30]]

#深copy  方法名：deepcopy   修改里面所有的对象都不受影响 应为自己创建了对象地址 然后装进去的
my_list3 = [1,[2,3],{"name":"zhangsan","age" :18}]
print(my_list3)
my_list4 = deepcopy(my_list3)
print(my_list4)

my_list3[2]["name"] = "lisi"
print(my_list3)
print(my_list4)



