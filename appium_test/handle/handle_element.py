# coding:utf-8
from page.login_page import LoginPage

class HandleElement:
    '''
    操作元素
    '''
    def __init__(self, i):
        self.login = LoginPage(i)

    def input_user(self, username):
        '''
        输入用户名
        '''
        self.login.get_user().sendkeys(username)

    def input_password(self, pwd):
        '''
        输入密码
        '''
        self.login.get_password().sendkeys(pwd)

    def click_login_button(self):
        '''
        点击登录按钮
        '''
        self.login.get_login_button().click()

    def get_tost(self, message):
        '''
        检查信息是否出现
        '''
        self.login.get_tost(message)


