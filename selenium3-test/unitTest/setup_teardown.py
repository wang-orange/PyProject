# coding:utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class Blog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.cnblogs.com/wangyjketang")
    def test_blog(self):
        time.sleep(3)
        title = '汪orange - 博客园'
        result = EC.title_is(title)(self.driver)
        print(result)
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



