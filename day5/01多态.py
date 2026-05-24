"""
多态核心：
1. 父类定义统一接口（如go方法）；
2. 子类重写接口实现不同逻辑；
3. 外部调用时，仅需传入子类实例，自动执行对应逻辑；

自己理解：
    Python的多态和C和Java不同
    不一定非要指定父类统一接口，只要类里面有相同的方法，名字就可以归为一个多态
    可以抽象成只要有相同的能力他们就是一个态系里面的
"""
# 父类：定义统一接口
class Animal:
    def go(self):
        """所有动物的移动行为（父类统一接口）"""
        pass

# 子类1：狗（重写go方法）
class Dog(Animal):
    def go(self):
        print("狗：四条腿跑")

# 子类2：鱼（重写go方法）
class Fish(Animal):
    def go(self):
        print("鱼：在水里游")

# 子类3：鸟（重写go方法）
class Bird(Animal):
    def go(self):
        print("鸟：张开翅膀飞")

# 通用调用函数（无需关注具体子类）
def move(animal):
    """接收Animal子类实例，调用统一接口"""
    animal.go()

# 测试：传入不同子类，执行不同行为
dog = Dog()
fish = Fish()
bird = Bird()

move(dog)   # 输出：狗：四条腿跑
move(fish)  # 输出：鱼：在水里游
move(bird)  # 输出：鸟：张开翅膀飞