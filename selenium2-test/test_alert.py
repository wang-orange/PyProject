# coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
url = "file:///D:/AutoTest/test_alert_confirm_prompt.html"
driver.get(url)
driver.implicitly_wait(5)
# time.sleep(2)
''' alert '''
driver.find_element_by_id("alert").click()
t = driver.switch_to.alert  # 切换到警告框上
print t.text  # 打印警告框上文本信息
time.sleep(2)
# t.accept()  # 点击确定按钮
t.dismiss()  # 相当于点右上角X，取消弹出框
''' confirm '''
time.sleep(2)
driver.find_element_by_id("confirm").click()
t = driver.switch_to.alert # 切换到确认框
print t.text
time.sleep(2)
# t.accept()
t.dismiss()
''' prompt '''
time.sleep(2)
driver.find_element_by_id("prompt").click()
time.sleep(2)
t = driver.switch_to.alert
print t.text
t.send_keys("hello selenium2")
time.sleep(2)
t.accept()
# t.dismiss()



