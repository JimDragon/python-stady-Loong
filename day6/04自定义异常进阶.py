"""
自定义异常的进阶用法（增强错误信息）
基础版仅能传递字符串提示，进阶版可自定义属性（如错误码、错误详情），让异常信息更完整（便于日志记录、前端展示）：
"""


class LoginError(Exception):
    """
    增强版登录异常类
    :param message: 错误提示信息
    :param error_code: 自定义错误码（如1001=用户名错，1002=密码错）
    :param detail: 错误详情（可选，如请求ID、时间戳）
    """

    def __init__(self, message, error_code, detail=None):
        # 调用父类 __init__ 方法，保证基础异常功能
        super().__init__(message)
        # 新增自定义属性
        self.error_code = error_code
        self.detail = detail


# 业务函数中按不同错误类型抛异常
def login(username, password):
    valid_username = "admin"
    valid_password = "123456"

    if username != valid_username:
        # 用户名错误：错误码1001，附带详情
        raise LoginError(
            message="用户名不存在",
            error_code=1001,
            detail=f"尝试登录的用户名：{username}"
        )
    if password != valid_password:
        # 密码错误：错误码1002
        raise LoginError(
            message="密码错误",
            error_code=1002,
            detail=f"用户名 {username} 输入了错误密码"
        )
    return True


# 捕获异常时，获取自定义属性
try:
    login("tom", "111")  # 用户名错误
except LoginError as e:
    print(f"登录失败：{e}")  # 输出：登录失败：用户名不存在
    print(f"错误码：{e.error_code}")  # 输出：错误码：1001
    print(f"错误详情：{e.detail}")  # 输出：错误详情：尝试登录的用户名：tom

try:
    login("admin", "654321")  # 密码错误
except LoginError as e:
    print(f"登录失败：{e}")  # 输出：登录失败：密码错误
    print(f"错误码：{e.error_code}")  # 输出：错误码：1002