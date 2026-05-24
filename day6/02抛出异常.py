"""
raise：主动抛出异常

当你检测到“业务规则不满足”时，可以主动抛异常中断流程：
"""
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("取款金额必须大于 0")
    if amount > balance:
        raise ValueError("余额不足")
    return balance - amount

print(withdraw(20, 30))