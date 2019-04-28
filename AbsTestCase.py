import unittest
from unitTest.abs import abs

class TestAbs(unittest.TestCase):
    #
    # def setUp(self):
    #     print("测试用例开始执行--------")
    #
    # def tearDown(self):
    #     print("测试用例执行结束--------")

    def test_abs1(self):
        print("第一个测试用例......")
        self.assertEqual(1,abs(1),msg="n>0")

    def test_abs2(self):
        print("第二个测试用例......")
        self.assertEqual(0,abs(0),msg="n=0")

    def test_abs3(self):
        print("第三个测试用例......")
        self.assertEqual(1,abs(-1),msg="n<0")

if __name__ == '__main__':
    unittest.main()
