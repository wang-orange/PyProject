# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("file:///D:/AutoTest/xml/div_scroll.html")
driver.implicitly_wait(10)
# 纵向滚到底部
time.sleep(2)
js1 = 'document.getElementById("yoyoketang").scrollTop=10000'
driver.execute_script(js1)
time.sleep(2)

# 纵向滚到顶部
js2 ='document.getElementById("yoyoketang").scrollTop=0'
driver.execute_script(js2)
time.sleep(2)

# 横向滚到右侧
js3 = 'document.getElementById("yoyoketang").scrollLeft=10000'
driver.execute_script(js3)
time.sleep(2)

# 横向滚到左侧
js4 = 'document.getElementById("yoyoketang").scrollLeft=0'
driver.execute_script(js4)
time.sleep(2)

# 获取的class返回时list对象，取list的第一个
js5 = 'document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)