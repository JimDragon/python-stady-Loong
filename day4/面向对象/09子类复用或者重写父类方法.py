""""
子类可通过两种方式复用父类方法，也可重写父类方法实现自定义逻辑：

    1. 复用：super().方法名() 或 父类名.方法名(self, 参数)；
    2. 重写：子类定义与父类同名的方法，覆盖原有逻辑。

"""

"""
子类复用/重写父类方法
核心：super() 自动适配继承关系，推荐优先使用
"""
class Person:
    def __init__(self, name):
        self.name = name
        print("父类构造方法执行")

    def __str__(self):
        return f"{self.name} 是一个人"

    def eat(self):
        print(f"{self.name} 吃东西....")

# 子类：Student
class Student(Person):
    # 重写父类构造方法
    def __init__(self, name, score):
        super().__init__(name)  # 复用父类构造方法
        self.score = score
        print("子类构造方法执行")

    # 复用父类方法
    def show(self):
        # 方式1：super()（推荐，适配多继承）
        super().eat()
        # 方式2：父类名.方法名（需手动传self）
        # Person.eat(self)

    # 重写父类__str__方法
    def __str__(self):
        # 复用父类__str__结果 + 子类扩展
        return super().__str__() + f"，也是学生，分数：{self.score}"

# 测试
s = Student("张三", 90)
s.show()       # 复用父类eat方法
print(s)       # 调用重写后的__str__：输出“张三是一个人，也是学生，分数：90”