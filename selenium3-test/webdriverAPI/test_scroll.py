# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/")
print(driver.name)  # 打印浏览器名称

# # 回到顶部
# def scroll_top():
#     if driver.name == "chrome":
#         js = "var q=document.body.scrollTop=0"  # 不管用
#     else:
#         js = "var q=document.documentElement.scrollTop=0"
#     return driver.execute_script(js)
# # 拉到底部
# def scroll_foot():
#     if driver.name == "chrome":
#         js = "var q=document.body.scrollTop=10000"  # 不管用
#     else:
#         js = "var q=document.documentElement.scrollTop=10000"
#     return driver.execute_script(js)
#
# scroll_foot()
# time.sleep(3)
# scroll_top()

# 滚到底部
js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(3)
# 滚到顶部
js = "window.scrollTo(0, 0)"
driver.execute_script(js)

