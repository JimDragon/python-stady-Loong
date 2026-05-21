class  Person:
# 类属性 所有实例对象使用这个一个
    home = "earth"

# 初始化方法 相当于Java里面的构造方法

    def __init__(self,name,sex,age):
        # 公开的属性
        self.name = name
        # 约定非公开属性，无强制限制访问
        self._sex = sex
        # 强制非公开属性，无法强制访问，但有其他方法可以访问
        self.__age = age



    def eat (self):
        print("吃东西...")

    def xxoo(self):
        print("交配...")

p = Person("jim","男",27)

# 通过下面的方式分别可以取到值
print(p.name)
print(p._sex)                     #不推荐这样访问
print(p._Person__age)             #不推荐这样访问

p.name = "kris"
p._sex = "女"
p._Person__age = 30

print(p.name)
print(p._sex)                     #不推荐这样访问
print(p._Person__age)             #不推荐这样访问


