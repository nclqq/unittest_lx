import unittest
from unitTest.pwd import check_password

class TestPwd(unittest.TestCase):


    @classmethod
    def setUpClass(cla):
        print("测试用例开始执行--------")

    @classmethod
    def tearDownClass(cla):
        print("测试用例执行结束--------")


 #密码小于6位
    def test_pwd1(self):
        print("-----1.密码小于6位------")
        self.assertEqual(False,check_password("12aS"))
 #密码=6位
    def test_pwd2(self):
        print("-----2.密码等于6位------")
        self.assertEqual(True,check_password("123faS"))
 #密码>6位
    def test_pwd3(self):
        print("-----3.密码大于6位------")
        self.assertEqual(True,check_password("123asdSFFG"))
 #密码全为数字
    def test_pwd4(self):
        print("-----4.密码全为数字------")
        self.assertEqual(False,check_password("0123456789"))

# 密码不包括大写字母
    def test_pwd5(self):
        print("-----5.密码不包括大写字母------")
        self.assertEqual(False, check_password("123rtyuiop"))
# 密码不包括小写字母
    def test_pwd6(self):
        print("-----6.密码不包括小写字母------")
        self.assertEqual(False, check_password("34DFGHJKL"))

# 密码不包括数字
    def test_pwd9(self):
        print("-----9.密码不包括数字------")
        self.assertEqual(False, check_password("sdffDFGHJKL"))

# 密码全为小写字母
    def test_pwd10(self):
        print("-----10.密码全为小写字母------")
        self.assertEqual(False, check_password("sdffdfgfgfg"))

 # 密码全为大写字母
    def test_pwd11(self):
        print("-----11.密码全为大写字母------")
        self.assertEqual(False, check_password("ASDFGHJHKREETR"))

# 密码为汉字
    def test_pwd7(self):
        print("-----7.密码为汉字------")
        self.assertEqual(False, check_password("1234张三"))
# 密码为特殊字符
    def test_pwd8(self):
        print("-----8.密码为特殊字符------")
        self.assertEqual(False, check_password("324@#￥￥%……&*"))



if __name__ == '__main__':
    unittest.main()
