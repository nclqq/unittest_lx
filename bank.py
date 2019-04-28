class Account:
    """表示一个账户"""

    def __init__(self, name='', balance=0):
        """账户包含姓名 name，余额 balance，创建账户时指定此二项"""
        self.name = name
        self.balance = balance


class BalanceNotEnough(Exception):
    """
    专门用于表示 余额不足 的异常
    """
    pass


class BankService:
    """提供银行相关服务"""

    def store(self, amount, account): # amount:存入的   account:余额
        """
        存款
            1. 存款金额需大于 0，否则抛出 ValueError 异常

        返回余额
        """
        if amount <= 0:
            raise ValueError('存款金额必须大于 0 元', amount)

        account.balance += amount
        return account.balance

    def take(self, amount, account):
        """
        取款
            1. 取款金额需大于 0，否则抛出 ValueError 异常
            2. 账户需有足够余额，否则抛出 BalanceNotEnough 异常
        返回余额
        """
        if amount <= 0:
            raise ValueError('取款金额无效', amount)
        if account.balance < amount:
            raise BalanceNotEnough('余额不足，取款失败', account.balance)

        account.balance -= amount
        return account.balance

    def transfer(self, amount, src, dst):
        """
        转账
            1. 转账金额需大于 0，否则抛出 ValueError 异常
            2. 账户需有足够余额，否则抛出 BalanceNotEnough 异常
        """
        if amount <= 0:
            raise ValueError('转账金额无效，必须大于 0 元', amount)
        if src.balance < amount:
            raise BalanceNotEnough('余额不足，转账失败', src.balance)

        src.balance -= amount
        dst.balance += amount
