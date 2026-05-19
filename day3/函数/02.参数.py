
"""
#形参 就是 写方法时候定义的参数
# 实参 就是 调用方法的时候传进去的参数
"""

# 1.位置参数   根据形参写的位置依次顺序传入进去

def 位置(name,age):
    print(name,age)

位置("龙飞扬",18)

# 默认值参数  意思就是：形参后面加一个等号 写入默认值  比如 conutry = "中国"

def 默认参数(name,age,country="中国"):
    print(name, age,country)
默认参数("jimLoong",27)

# 关键字参数 简单来说就是调用方法传实参的时候
# 用(形参=实参,形参=实参,形参=实参)的方式就 不用按顺序 传入
def 关键字参数(name,age,country="中国"):
    print(name, age,country)

关键字参数(age=15,name="curry")

"""
可变参数
   1 用 *形参名字  接受多个参数 储存为元组()
   2 用 **形参名字  接受多个参数 储存为字典{"xx":xx,"yy":yy}}
限制:
   3 一个函数里面最多存在一个 *  和 一个 ** 类型的形参
   4 *参数 后面可以有 **参数 ; *参数后面的 普通参数 必须通过 关键字的形式 赋值
"""
#1
def one(*hobby):
    print(hobby)

one("跑步","打炮","走草") #('跑步', '打炮', '走草')

#2
def two(name,**contact_person):
    """
    :param name:           名字
    :param contact_person: 家庭联系人,通过字典方式传入
    :return: None
    """
    print(name, contact_person)

two("陈冠希",张柏芝=19839201,钟欣桐=12314414411)

# 定义函数，如果可变参数后面还有普通参数，那么普通参数必须使用关键字参数给普通参数赋值
def print_info(name, *hobby, age):
    print(f"{name} 的爱好是：{hobby}，年龄：{age}")
# 调用函数
print_info( "张三","跑步", "看电影", "看小说", age = 18)

# 定义函数，**contact_person可变参数必须在最后
def print_info1(name, *hobby, **contact_person):
    print(f"{name} 的爱好是：{hobby}，联系人有：{contact_person}")
# 调用函数
print_info1("张三","跑步", "看电影", "看小说", mon = "12345678901", dad = "12345678902")


# 5. 解包传参
# 定义函数
def print_info(name, age):
    print(f"{name} 的年龄是：{age}")
# 调用函数
print_info(*["张三", 18]) # 列表解包，要求列表元素个数与参数个数一致
print_info(*("张三", 18)) # 元组解包，要求元组元素个数与参数个数一致
print_info(*{"张三", 18}) # 不推荐用集合，因为集合是无序的
print_info(**{"name": "张三", "age": 18}) # 字典解包，要求字典的key与参数名一致




