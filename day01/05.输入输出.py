#阻断式输入，让用户输入，接受到的都是 string

outStr=input("请输入你最喜欢的电影:\n")
print("所以今年的金像奖是："+outStr)


outAge=input("请输入你的年龄后开机：")
intAge=int(outAge)

if intAge>18:
    print("欢迎光临，请上二楼")
else:
    print("小麻批娃儿个人爬")

#输出多个字符  可以 乘
print("*" * 8)

#格式化占位 直接学习推荐 f 方法 官方推荐

name = "邓超"
age = 47
salary = 10_000_000.245

print(f"{name}今年{age}岁，今年的总收入{salary:,.2f}元人民币")



