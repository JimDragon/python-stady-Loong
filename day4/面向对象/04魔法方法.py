"""

方法名以 __ 开头和结尾的方法（如 __init__），特定操作时自动调用。
简单来说就是一个类的生命周期
每个生命周期做什么事情
__new__ 就是创建实例的时候就会出发
__init__  就是实例开始初始化的时候就会触发
__str__   调用str（实例）的时候触发
__del__  实例销毁的时候出发
"""

class Magic:
    def __new__(cls, name):
        print(f"{cls.__name__}经过了new，实例创建")
        instance = super().__new__(cls)
        return instance

    def __init__(self,name):
        self.name = name
        print(f"实例初始化，开始初始化{self.name}实例的属性")

    def __str__(self):
        """3. 调用 str(实例) 时执行"""
        return f"DemoClass: name={self.name}"

    def __del__(self):
        """4. 实例销毁时执行"""
        print(f"调用 __del__ 销毁 {self.name} 实例")


