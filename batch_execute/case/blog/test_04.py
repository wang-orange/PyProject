# coding:utf-8

from selenium import webdriver
import unittest
import time

class Test(unittest.TestCase):
    def setUp(self):
        print("04-Start!")
    def tearDown(self):
        time.sleep(2)
        print("04-end!!")
    def test_01(self):
        print("04-执行用例01")
    def test_03(self):
        print("04-执行用例03")
    def test_02(self):
        print("04-执行用例02")
if __name__ == "__main__":
    unittest.main()