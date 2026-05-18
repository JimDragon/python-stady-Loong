#  分支结构 (If)
# 分支结构用来 “根据条件执行不同代码”，是最基础的逻辑控制方式，核心是if/elif/else，满足哪个条件就执行对应的代码块。

# 新手友好示例：根据成绩判断等级（仅用数字、比较运算符）
score = 33

if score >= 90:
    print("nb")
elif score >= 80:
    print("just so so ")
elif score >= 60:
    print("are you sure?")
else:
    print("you can go home")

# Match-Case (Python 3.10+，简化版理解)
# 可以理解成 “升级版多分支”，适合按固定值匹配（比如状态码、固定选项），新手先了解即可：

# 示例：匹配HTTP状态码（仅用数字、赋值运算符）
status = 500

match status:
    case 404:
        print("can't find index")
    case 500:
        print("Your backend server has crashed. ")
    case _:
        print("call office phone 80088208820 or sendmail '123414@123.com'")

# 6.2.1 While 循环
# 只要条件为 True，就一直执行循环体，直到条件为 False 才停止（注意设置 “终止条件”，避免死循环）

time = 1

while time<5:
    if time ==3:
        break
    print(f"now time is {time}")
    time += 1

else:
    print("被break 打断不执行这里")

print("都要执行")

# 6.2.2 For 循环
# 更适合 “固定次数循环” 或 “遍历列表 / 字符串”，新手常用range()函数控制循环次数。

mylist = ['蔡徐坤', '陈立农', '有长进', '黄明浩', 'pgone', '李小璐']

for start in mylist:
    print(f"啊啊啊~~我最喜欢的明星有：{start}")

str1="hello world"
for char in str1:
    print(char)

mylist2= list(range(10))
print(mylist2)

mylist3= list(range(1,11,2))
print(mylist3)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i} × {j} = {i * j}", end="\t")
    print()
