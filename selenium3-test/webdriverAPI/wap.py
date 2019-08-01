# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions()
# 伪装iphone访问
option.add_argument('--user-agent=iphone')
# 伪装Android访问
# option.add_argument("--user-agent=Android")
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://www.taobao.com")