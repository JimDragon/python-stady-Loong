"""
单继承核心：
1. 子类通过 super() 调用父类构造方法；
2. 子类无法直接访问父类私有成员（可改写名称访问，不推荐）；

··· 语法格式
    class 子类名(父类名):
    子类体  # 可新增属性/方法，或重写父类方法
"""
# 父类：通用的Person类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性：_Person__age
        print("父类Person构造方法执行")

    def eat(self):
        print(f"{self.name} 吃东西....")

# 子类1：Student（继承Person，新增score属性）
class Student(Person):
    def __init__(self, name, age,score):
        super().__init__(name, age)
        self.score = score

    def eat(self):
        super().eat()

    def study(self):
        # 不推荐：通过改写名称访问父类私有属性
        print(f"{self.name} 学习，年龄：{self._Person__age}，分数：{self.score}")

# 子类2：Teacher（继承Person，新增title属性）
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title  # 子类特有属性
        print("子类Teacher构造方法执行")

    def teach(self):
        print(f"{self.name} 老师，教授 {self.title}")

# 测试
s = Student("张三", 18, 90)
s.eat()   # 复用父类方法
s.study() # 子类特有方法

t = Teacher("王五", 28, "Python编程")
t.eat()   # 复用父类方法
t.teach() # 子类特有方法


