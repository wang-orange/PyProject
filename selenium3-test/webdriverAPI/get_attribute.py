# coding:utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 获取页面title
print(driver.title)
# 获取元素的文本
text = driver.find_element_by_id("setf").text
print(text)
# 获取元素的标签
tag = driver.find_element_by_id("kw").tag_name
print(tag)
# 获取元素的其他属性
classname = driver.find_element_by_id("kw").get_attribute("class")
print(classname)
name = driver.find_element_by_id("kw").get_attribute("name")
print(name)
# 获取输入框的内容
driver.find_element_by_id("kw").send_keys("yoyoketang")
value = driver.find_element_by_id("kw").get_attribute("value")
print(value)
# 获取浏览器名称
print(driver.name)