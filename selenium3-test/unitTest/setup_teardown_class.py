# coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start !")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        print("end!!")

    # def setUp(self):
    #     print("setUP...")
    #
    # def tearDown(self):
    #     print("tearDown...")

    def test_01(self):
        print("执行用例01")

    def test_03(self):
        print("执行用例03")

    def test_02(self):
        print("执行用例02")

    def testadd(self):
        print("add方法")

if __name__ == "__main__":
    unittest.main()
