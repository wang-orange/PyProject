# coding:utf-8

from selenium import webdriver
import unittest
import time

class Blogs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://passport.cnblogs.com/user/signin")
        self.driver.implicitly_wait(10)
    def login(self, user, pwd):
        ''' 登录方法，账号和密码参数化 '''
        self.driver.find_element_by_id("input1").send_keys(user)
        self.driver.find_element_by_id("input2").send_keys(pwd)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)
    def is_login_success(self):
        ''' 判断是否获取到登录账号名称 '''
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False
    def test_01(self):
        ''' 登录案例：输入正确的账号、密码 '''
        self.login("汪orange", "orange@0419")
        result = self.is_login_success()
        self.assertTrue(result)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
