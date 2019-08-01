# coding:utf-8
from handle.handle_element import HandleElement

class LoginBusiness:
    def __init__(self, i):
        self.handle = HandleElement(i)

    def login_success(self):
        '''
        登录成功
        '''
        self.handle.input_password('18600407736')
        self.handle.input_password('orange0419')
        self.handle.click_login_button()

    def user_error(self):
        '''
        用户名未注册
        '''
        self.handle.input_user('18600407777')
        self.handle.input_password('123')
        self.handle.click_login_button()
        self.handle.get_tost('用户未注册')

    def password_error(self):
        '''
        登录密码错误
        '''
        self.handle.input_user('18600407736')
        self.handle.input_password('123')
        self.handle.click_login_button()
        self.handle.get_tost('登录密码错误')
