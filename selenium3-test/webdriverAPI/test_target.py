# coding:utf-8

from selenium import webdriver
import time

file = r"C:\Users\sfc\AppData\Roaming\Mozilla\Firefox\Profiles\5ag7m18v.default"
profile = webdriver.FirefoxProfile(file)
driver = webdriver.Firefox(profile)
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
h = driver.current_window_handle
# 添加target属性并赋值
js = 'document.getElementsByClassName("mnav")[1].setAttribute("target", "_blank");'
driver.execute_script(js)
driver.find_element_by_name("tj_trhao123").click()
time.sleep(2)
driver.switch_to.window(h)
print(driver.title)
# 删除target属性
js1 = "document.getElementsByName('tj_trhao123')[0].removeAttribute('target');"
driver.execute_script(js1)
driver.find_element_by_name("tj_trhao123").click()