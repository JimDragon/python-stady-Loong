# 综合案例：猜数字游戏
# 本案例综合运用了变量、数据类型转换、输入输出、循环（while）、分支（if-elif-else）、break/continue 等核心知识点。
# 游戏规则：程序随机生成一个 1-100 的数字，玩家通过输入数字进行猜测，程序会提示“大了”或“小了”，直到猜中为止。
import random

x = random.randint(1,100)

print("""
    欢迎来到澳门葡京赌场
    游戏规则：程序随机生成一个 1-100 的数字，玩家通过输入数字进行猜测，程序会提示“大了”或“小了”，直到猜中为止
    入场门票最少100元  5次内猜中 获得双倍奖金
                    10次内猜中  获得1.5倍奖金    
                    15次内猜中  不输不赢
                    15次以上    对不起，请重新开机
""")
usrMoney = input("请问您本局下注多少钱？")

count = 1
while True:
    usrInput = input("请你输入你猜想的数字")
    if not usrInput.isdigit():
        print("请输入整数")
        continue
    usrNum = int(usrInput)
    if count >15:
        print("狗屎运可以滚蛋了！")
        break
    if usrNum == x :
        print("游戏结束，欢迎下次再来")

        if count <= 5:
            sucessMoney = int(usrMoney) * 2
            print(f"恭喜你获得奖金{sucessMoney}RNB")
            break
        elif count <= 10:
            sucessMoney = int(usrMoney) * 1.5
            print(f"恭喜你获得奖金{sucessMoney}RNB")
            break
        elif count <= 15:
            sucessMoney = int(usrMoney)
            print(f"恭喜你获得奖金{sucessMoney}RNB")
            break



    count += 1

    if usrNum > x:
        print("猜大了一点，小一点试试？")
        continue
    elif usrNum < x:
        print("猜小了,more biger")
        continue



