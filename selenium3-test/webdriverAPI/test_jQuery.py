# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")
driver.implicitly_wait(10)
# 输入账号
user = "$('#input1').val('汪orange')"
driver.execute_script(user)
time.sleep(3)
# 清空文本
# clear = "$('#input1').val('')"
# driver.execute_script(clear)
# time.sleep(2)
# 输入密码
pwd = "$('#input2').val('orange0419')"
driver.execute_script(pwd)
# 点击登录
button = "$('#signin').click()"
driver.execute_script(button)