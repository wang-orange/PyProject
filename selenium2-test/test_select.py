# coding:utf-8
import time
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# 需要设置等待时间，否则后面有些定位可能会报错：
# Element is not currently visible and so may not be interacted with
driver.implicitly_wait(10)
# 鼠标移动到“设置”按钮
# mouse = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(mouse).perform()
# 定位到“搜索设置”按钮，并点击
driver.find_element_by_css_selector(".setpref").click()
# 分两步:先定位下拉框，再点击选项
# driver.find_element_by_id("nr").find_element_by_xpath("//option[2]").click()
# 一步定位到下拉框中的选项并点击
# driver.find_element_by_xpath("//select[@id='nr']").click()
# driver.find_element_by_css_selector("select#nr>option:nth-child(1)").click()
# 通过select_by定位
s = driver.find_element_by_id('nr')
# Select(s).select_by_index(1)  # 通过索引定位
# time.sleep(2)
# Select(s).select_by_value("50")  # 通过value定位
# time.sleep(2)
Select(s).select_by_visible_text("每页显示10条")  # 通过text定位
time.sleep(2)
# s.click()
# 定位“保存设置”按钮，并点击
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(2)
# 获取alert弹框
t = driver.switch_to.alert
driver.switch_to_alert().accept()
# print t.text
# t.accept()
