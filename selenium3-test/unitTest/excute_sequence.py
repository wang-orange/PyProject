# coding:utf-8

import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("start!")
    def tearDown(self):
        time.sleep(1)
        print("end!!")
    def test01(self):
        print("执行用例01")
    def test03(self):
        print("执行用例03")
    def test02(self):
        print("执行用例02")
    def Addtest(self):  # 该方法不会被执行，需要以test开头
        print("add方法")
if __name__ == "__main__":
    unittest.main()
