# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(5)
mouse = driver.find_element_by_link_text("更多产品")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(2)
ele = driver.find_element_by_link_text("全部产品>>")
# ele = driver.find_element_by_name("tj_more")
print(ele.text)
ele.click()
