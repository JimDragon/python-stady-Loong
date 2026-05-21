
class  Person:
# 类属性 所有实例对象使用这个一个
    home = "earth"

# 初始化方法 相当于Java里面的构造方法

    def __init__(self):
        #这个self.age  里面的age 是 实例创建的时候自己私有的 age 每个实例都用自己的
        self.age = 0


    def eat (self):
        print("吃东西...")

    def xxoo(self):
        print("交配...")

p = Person()
p.eat()
p.xxoo()
print(p.home)
print(p.age)
