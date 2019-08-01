# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "file:///D:/AutoTest/radiobox_checkbox.html"
driver.get(url)
driver.implicitly_wait(10)
# test radio
# 判断单选框是否选中:is_selected()
s = driver.find_element_by_id("boy").is_selected()
print s
if s == False:
    driver.find_element_by_id("boy").click()
time.sleep(2)
s = driver.find_element_by_id("girl").is_selected()
if s == False:
    driver.find_element_by_id("girl").click()
# test checkbox
# time.sleep(1)
# driver.find_element_by_css_selector("#c1").click()
# time.sleep(1)
# driver.find_element_by_css_selector("#c2").click()
# time.sleep(1)
# driver.find_element_by_css_selector("#c3").click()
# checkbox 全部勾选
time.sleep(1)
s = driver.find_element_by_id("c1").is_selected()
if s == False:
    cb = driver.find_elements_by_css_selector("input[type='checkbox']")
    for i in cb:
        i.click()

