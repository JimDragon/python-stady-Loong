class Person:
    home = "地球"



    def __init__(self,name,sex,age):
        self.name = name
        self._sex =sex
        self.__age =age

    #类方法  @classmethod
    # 类方法可以拿到类属性 但不能拿到实例属性
    # 类比理解：类和类属性和方法都比实例先创建。就像爸爸不知道未出生的儿子长什么样子
    @classmethod
    def class_meth(cls):
        print(f"类属性home的值是{cls.home}")


    """
    实例方法
    没有修饰
    """
    def eat(self):
        """实例方法：访问类属性+实例属性"""
        print(f"{self.name} is eating in {Person.home}")


    """
    静态方法
    修饰词：@starticmethod
    可以用实例.方法  也可以用类名.方法
    """
    @staticmethod
    def say(word):
        print(f"他会说{word}")



p = Person
p.class_meth()

Person.say("english")


