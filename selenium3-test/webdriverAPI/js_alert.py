# coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Firefox()
# 1.常规alert框
# driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
# driver.switch_to.frame("iframeResult")
# driver.find_element_by_css_selector("html>body>input").click()
# time.sleep(3)
# driver.switch_to.alert.accept()

# 2.自定义alert框
driver.get("https://sh.xsjedu.org/")
time.sleep(2)
# 利用HTML DOM Style 对象，将display的值设置成none，去除这个弹框
js = 'document.getElementById("doyoo_mon_inner").style.display="none";'
driver.execute_script(js)
