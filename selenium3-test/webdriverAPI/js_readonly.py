# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")
driver.implicitly_wait(10)
# 去掉元素的readonly属性
js = 'document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js)

# # 1.清空文本后输入值
# driver.find_element_by_id("train_date").clear()
# time.sleep(2)
# driver.find_element_by_id("train_date").send_keys("2018-09-23")

# 2.用js方法直接修改value的值
js_value = 'document.getElementById("train_date").value="2018-09-26"'
driver.execute_script(js_value)