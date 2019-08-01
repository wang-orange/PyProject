# coding:utf-8
from selenium import webdriver

driver = webdriver.Firefox()
url = "http://mail.163.com"
driver.get(url)
driver.implicitly_wait(10)
# 切换iframe
# frame = driver.find_element_by_tag_name("iframe")
# driver.switch_to.frame(frame)
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").send_keys("123")
driver.find_element_by_name("password").send_keys("456")
driver.find_element_by_id("dologin").click()
# 释放iframe，重新回到主页面上
driver.switch_to.default_content()