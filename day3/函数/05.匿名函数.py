a = True + 3
print(a)

my_list = [2,1,-9,-48,6444,-65]
list.sort(my_list,key=lambda x: abs(x),reverse=True)
print(my_list)

my_list2 = sorted(my_list,key=lambda x : x**2 ,reverse=True)
print(my_list2)

