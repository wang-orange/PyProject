# coding:utf-8
import random
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
href_list = driver.find_elements_by_css_selector(".t>a")
print href_list
for i in href_list:
    print i.get_attribute("href")
r = random.randint(0,10)
href_list[r].click()
# driver.get(href_list[r].get_attribute("href"))

