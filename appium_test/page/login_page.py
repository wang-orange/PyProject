# coding:utf-8
from util.locate_element import LocateElement
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    '''
    获取登录页面各元素
    '''
    def __init__(self, i):
        driver = BaseDriver(i)
        self.locate = LocateElement(driver)

    def get_user(self):
        '''
        用户名元素
        '''
        return self.locate.find_element('username')

    def get_password(self):
        '''
        密码元素
        '''
        return self.locate.find_element('password')

    def get_login_button(self):
        '''
        用户名元素
        '''
        return self.locate.find_element('login_button')


    def get_tost(self, message):
        '''
        tost元素
        '''
        tost_elemnt = ('xpath', '//*[contains(@test, '+message+')]')
        return WebDriverWait(self.locate.driver, 20, 0.1).until(EC.presence_of_element_located(tost_elemnt))