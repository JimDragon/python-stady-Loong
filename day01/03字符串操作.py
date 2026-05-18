

#使用双赢好 和 单引号 阔起来的都是字符串
str1="我老婆去做一个非常非常非常漂亮的头发"
str2='中国有嘻哈，你最喜欢谁？P！G！O！N！E！'


#单 双 引号 可以互相嵌套 ，但不能 自己嵌套自己
str3="庆祝的就已经为你'开好'，千万不要高兴得'太早'"
str4 = '把每首歌都"唱好"，再回去见你的家乡"父老"'
print(str3)
print(str4)


#三引号 所见即所得 内容包括 字符 换行 等 都不需要转义
str5="""
      "我老婆去做一个非常非常非常漂亮的头发"
      '中国有嘻哈，你最喜欢谁？P！G！O！N！E！'
"庆祝的就已经为你'开好'，千万不要高兴得'太早'"

'把每首歌都"唱好"，再回去见你的家乡"父老"'

"""
print(str5)


#转义字符  \n 换行   \字符  转义字符
str6 = "你身份证掉了👇\n         🤡 "
print(str6)


#split 函数  将字符串切分为列表
strSplit="蔡徐坤,陈立农,有长进,黄明浩,pgone,李小璐"
mysplit=strSplit.split(",")
print(mysplit)

#jion 函数 将列表用一个 字符作为连接成一个 字符串
mylist2=['蔡徐坤', '陈立农', '有长进', '黄明浩', 'pgone', '李小璐']
print("👉".join(mylist2))

#strip 去掉前后空格
strStrip="         坤 坤坤      "
print(strStrip.strip())
#去掉左边空格 lstrip  去掉 右边空格 rstrip
print(strStrip.lstrip())
print(strStrip.rstrip())

#replace 替换str 中的 字符
strReplace="村ba，县ba，区ba，渝超，中乙，中甲，中超"
print(strReplace)
print(strReplace.replace("，", "👉"))

#替换个数
print(strReplace.replace("ba", "超", 3))

