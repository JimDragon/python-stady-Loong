#隐形转换
# 整形+浮点 = 浮点
num=8
num2 = 3.3
num4 = 0.1
num6 = 2
num3 = num+num2
print(num3)

# 浮点 + 浮点 =浮点
num5 = num2 + num4
print(num5)


#2 个 整数相除 = 浮点
num7 = num/num6
print(num7)

# 整数+ 字符串 报错！！

#显示转换（强制转换）
strNum="456"
print(type(int(strNum)),int(strNum))

#浮点转int 只保留 整数部分
print(int(4.1233))

#bool 转 int true👉1  false👉0
print(int(True))
print(int(False))

#object 👉 str
print(str(12344))
print(str(3.1415926))
print(str(False))
print(str(True))
print(str(['蔡徐坤', '陈立农', '有长进', '黄明浩', 'pgone', '李小璐']))

# （数值0，空值，空容器） 转换成bool 就是False ,其他都是 True
print(bool(0))
print(bool())
print(bool([]))
print(bool(""))
print(bool(1))
print(bool("有字符"))
print(bool([1, 2, 3, 4, 5]))

#二进制 和 str 之间的转换  encode  decode
#encode :  str 👉 bytes
#decode ： bytes 👉  str

strAndBytes="演员和歌手"
bytesData=strAndBytes.encode("utf-8")
print(type(bytesData),bytesData)

print(bytesData.decode("utf-8"))







