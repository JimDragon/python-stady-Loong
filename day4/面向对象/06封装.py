"""
单下划线	      _属性名/_方法名	       约定俗成的 “非公开 API”，无强制限制，仅提醒开发者 “不要外部访问”；

双下划线	      __属性名/__方法名	   名称改写（Name Mangling）：Python 自动将其转为 _类名__属性名，类外无法直接访问；
"""

"""
演示私有属性/方法的定义与访问规则
核心：双下划线成员会被名称改写，类外需通过 _类名__成员名 访问（不推荐）
"""
class Person:
    # 私有类属性：自动改写为 _Person__home
    __home = "earth"

    def __init__(self, name):
        self.__name = name  # 私有实例属性：_Person__name
        self.__age = 0      # 私有实例属性：_Person__age
        self._sex = "male"  # 单下划线：约定非公开，无强制限制

    # 私有方法：自动改写为 _Person__check_age
    def __check_age(self, age):
        print(f"检查年龄{age}的合法性...")
        if age < 0 or age > 100:
            raise ValueError("年龄超出0-100范围")

    # 公开接口：获取私有属性
    def get_name(self):
        return self.__name

    # 公开接口：设置私有属性（带校验逻辑）
    def set_age(self, age):
        self.__check_age(age)  # 类内可直接调用私有方法
        self.__age = age

    # 公开接口：获取私有属性
    def get_age(self):
        return self.__age

# 实例化测试
p = Person("张三")

# 1. 单下划线成员：可外部访问（仅为约定）
print(f"单下划线成员访问：p._sex = {p._sex}")  # 输出：male

# 2. 双下划线成员：直接访问报错，需通过改写后的名称（不推荐）
# print(p.__name)  # 报错：AttributeError
print(f"私有属性改写后访问：p._Person__name = {p._Person__name}")  # 输出：张三
print(f"通过公开接口访问：p.get_name() = {p.get_name()}")          # 推荐方式：输出张三

# 3. 私有方法/属性的合法操作
p.set_age(18)  # 通过公开接口设置私有属性（自动触发校验）
print(f"私有属性age：p.get_age() = {p.get_age()}")                # 输出：18
# p.__check_age(20)  # 报错：AttributeError
p._Person__check_age(20)  # 强制访问改写后的私有方法（不推荐）