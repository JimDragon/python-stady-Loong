# Python 3.9+ 可直接用 list/dict，无需导入 typing；3.8及以下需 from typing import List, Dict
from typing import List, Dict, Optional, Union, Any

# 1. 基础变量注解
name: str = "Alice"
age: int = 25
height: float = 1.68
is_student: bool = True

# 2. 容器类型注解
scores: List[int] = [80, 90, 95]  # 整数列表
user_info: Dict[str, Union[str, int]] = {"name": "Bob", "age": 30}  # 混合类型字典
optional_name: Optional[str] = None  # 可能为字符串或None
mixed_type: Union[int, str] = 100    # 可以是int或str

# 3. 函数注解（核心：提升可读性和IDE提示）
def greet(name: str, times: int = 1) -> str:
    """
    生成问候语
    Args:
        name (str): 要问候的人名（必填）
        times (int): 重复次数（默认1）
    Returns:
        str: 拼接后的问候语
    """
    return f"Hello, {name}! " * times

def find_user(user_id: int) -> Optional[str]:
    """
    根据ID查找用户
    Args:
        user_id (int): 用户ID
    Returns:
        Optional[str]: 找到返回用户名，未找到返回None
    """
    if user_id == 1:
        return "Admin"
    return None

# 4. 函数调用（IDE会提示参数类型，写错会警告）
print(greet("Bob", 2))  # 正确：Hello, Bob! Hello, Bob!
# greet(123)  # IDE警告：Expected type 'str', got 'int' instead（运行时仍能执行）

# 5. 类型别名（简化复杂类型）
UserList = List[Dict[str, Union[str, int]]]  # 定义类型别名
def get_users() -> UserList:
    """返回用户列表"""
    return [{"name": "Charlie", "age": 35}, {"name": "David", "age": 40}]