"""自定义异常：表达更清晰的业务错误
Python 中所有异常都是「类」—— 内置异常（如 ValueError）是 Python 提前定义好的类，自定义异常就是继承 Exception 类创建的专属业务异常类。
● 必须继承 Exception（而非 BaseException）：BaseException 包含系统级异常（如 KeyboardInterrupt），自定义业务异常继承 Exception 能避免捕获到系统级错误；
● 自定义异常的核心价值：让异常语义更贴合业务场景（比如 LoginError 一眼就知道是登录相关错误，而 ValueError 是通用错误）。
"""

"""自定义异常基础用法"""

# 1. 定义自定义异常类（继承 Exception）
class LoginError(Exception):
    """
    自定义登录异常类
    用于表达所有登录相关的业务错误（用户名不存在、密码错误、验证码过期等）
    """
    # pass 表示暂时无自定义逻辑，仅继承父类功能
    pass


# 2. 业务函数中抛出自定义异常
def login(username, password):
    """模拟登录校验"""
    # 模拟数据库中的正确账号密码
    valid_username = "admin"
    valid_password = "123456"

    # 校验失败时，主动抛出 LoginError
    if username != valid_username or password != valid_password:
        # raise + 异常类实例（括号内是错误提示信息）
        raise LoginError("用户名或密码错误")
    # 校验通过，返回登录成功
    return True


# 3. 捕获并处理自定义异常
try:
    # 调用登录函数（传入错误的账号密码）
    login("tom", "111")
except LoginError as e:
    # e 是异常实例，直接打印会输出错误提示信息
    print("登录失败：", e)  # 输出：登录失败：用户名或密码错误