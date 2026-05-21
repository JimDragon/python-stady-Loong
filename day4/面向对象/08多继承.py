"""
多继承允许子类同时继承多个父类的属性和方法，核心规则：
1. 属性 / 方法重名时，按 “从左到右” 顺序覆盖；
2. 方法查找时，先查子类，再按继承顺序查父类；
3. 常用 “混入类（Mixin）” 模式：将单一功能封装为 Mixin 类，通过多继承组合功能。


多继承示例（Mixin 模式）
"""
"""
Mixin模式核心：
1. 每个Mixin类封装单一功能（如飞行、游泳），不单独实例化；
2. 主类通过多继承组合多个Mixin的功能，实现“能力复用”；
"""
# Mixin类1：飞行能力
class Flyable:
    def fly(self):
        print(f"{self.name} 正在飞行")

# Mixin类2：游泳能力
class Swimming:
    def swim(self):
        print(f"{self.name} 正在游泳")

# Mixin类3：行走能力
class Walkable:
    def walk(self):
        print(f"{self.name} 正在行走")

# 基础类：鸟类（提供核心属性）
class Bird:
    def __init__(self, name):
        self.name = name  # 所有Mixin类依赖的核心属性

    def make_sound(self):
        print(f"{self.name} 在鸣叫")

# 子类：鸭子（组合基础类+多个Mixin）
class Duck(Bird, Flyable, Swimming, Walkable):
    def __init__(self, name):
        super().__init__(name)  # 初始化基础类属性

    # 子类特有方法
    def catch_fish(self):
        print(f"{self.name} 正在抓鱼")

# 测试：鸭子拥有所有组合能力
duck = Duck("小黄鸭")
duck.fly()         # 来自Flyable
duck.swim()        # 来自Swimming
duck.walk()        # 来自Walkable
duck.make_sound()  # 来自Bird
duck.catch_fish()  # 子类特有