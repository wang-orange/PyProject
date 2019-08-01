# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()  # 高版本的Firefox浏览器，使用ActionChains会没有反应
driver.get("http://www.baidu.com")
driver.implicitly_wait(20)
mouse = driver.find_element("link text", "设置")
# mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_class_name("setpref").click()
time.sleep(2)
select_e = driver.find_element("id", "nr")
Select(select_e).select_by_index(0)
time.sleep(2)
# driver.find_element_by_class_name("prefpanelgo").click()

# 用js直接点击
js = 'document.getElementsByClassName("prefpanelgo")[0].click()'
driver.execute_script(js)
# al = driver.switch_to_alert()
al = driver.switch_to.alert
time.sleep(2)
al.accept()
