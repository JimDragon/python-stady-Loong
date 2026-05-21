import types


class Person:

    def __init__(self, name):
        self.name = name

"""# 动态添加类属性"""
Person.home = "earth"

"""# 动态添加类方法
#先定义好方法 然后塞给这个类"""
@classmethod
def come_from(cls):
    print(f"I come from {cls.home}")
Person.come_from = come_from

# 验证
print(Person.home)      # 输出：earth
Person.come_from()      # 输出：I come from earth

"""# 
动态添加 实例属性 / 方法
    types.MethodType(方法名,实例名)
    
"""
"""
1创建对象
"""
p = Person("张飞")
"""
2创建方法，准备塞入到实例里面
"""

def do_love(self):
    print(f"{self.name}正在吃饭")
    return f"{self.name}学会了做爱"

"""
把 do_love 这个方法塞给 p实例
types.MethodType(方法名,实例名)
"""

p.do_love = types.MethodType(do_love,p)
p.do_love()

"""
__slots__ 限制动态添加

__slots__ 可限制实例能添加的属性 / 方法（仅对当前类生效，子类无效）
"""

class Person:
    __slots__ = ("name", "age")  # 仅允许添加这两个实例属性

p = Person()
p.name = "张三"  # 允许
p.age = 18       # 允许
# p.weight = 60  # 报错：weight 不在 __slots__ 中




