# coding:utf-8
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/wangyjketang/")
# 获取网页源码
page = driver.page_source
# print(page)

# 非贪婪匹配，re.S(使 . 匹配包括换行在内的所有字符)
url_list = re.findall(r'href="(http.*?)"', page, re.S)  # 匹配括号内的内容，获取超链接
# print(url_list)
for i in url_list:
    print(i)