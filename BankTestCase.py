import unittest
from unitTest.bank import BankService
from unitTest.bank import Account
from unitTest.bank import BalanceNotEnough

class TestBank(unittest.TestCase):
    bank=BankService()
    a=Account()
    b=Account()

    a.balance=1000
    b.balance=1000

    @classmethod
    def setUpClass(cla):
        print("测试用例开始执行--------")

    @classmethod
    def tearDownClass(cla):
        print("测试用例执行结束--------")


 #存款
    def test_store1(self):
        print("-----存款为负数------")
        with self.assertRaises(ValueError):
            self.bank.store(-100, self.a)

    #try--catch语句
        # try:
        #     BankService().store(0, self.a)
        # except Exception as e:
        #     print(e)
        #     assert (ValueError('存款金额必须大于 0 元', 0),e)

    def test_store2(self):
        print("-----存款为0------")
        with self.assertRaises(ValueError):
            self.bank.store(0, self.a)

    def test_store3(self):
        print("-----存款正常------")
        self.assertEqual(1100,BankService().store(100,self.a),msg="amount=100,存款成功")

#存款
    def test_take1(self):
        print("-----取款为负数------")
        with self.assertRaises(ValueError):
            self.bank.take(-100, self.a)

    def test_take2(self):
        print("-----取款为0------")
        with self.assertRaises(ValueError):
            self.bank.take(0, self.a)

    def test_take3(self):
        print("-----取款超出------")
        with self.assertRaises(BalanceNotEnough):
            self.bank.take(2000, self.a)

    def test_take4(self):
        print("-----取款正常------")
        self.assertEqual(1000,BankService().take(100,self.a),msg="amount=100,取款成功")

 #转账
    def test_transfer1(self):
        print("-----转账为负数------")
        with self.assertRaises(ValueError):
            self.bank.transfer(-100, self.a,self.b)

    def test_transfer2(self):
        print("-----转账为0------")
        with self.assertRaises(ValueError):
            self.bank.transfer(0, self.a,self.b)

    def test_transfer3(self):
        print("-----转账超出------")
        with self.assertRaises(BalanceNotEnough):
            self.bank.transfer(2000, self.a,self.b)

    def test_transfer4(self):
        print("-----转账正常------")
        BankService().transfer(500, self.a,self.b)
        print(self.a.balance)
        print(self.b.balance)
        assert (500,self.a.balance)



if __name__ == '__main__':
    unittest.main()
