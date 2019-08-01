# coding:utf-8
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
# 查看配置文件：在地址栏输入 chrome://version/
# 个人资料路径	C:\Users\shenfengcai\AppData\Local\Google\Chrome\User Data\Defaul
option.add_argument('--user-data-dir=C:\\Users\shenfengcai\AppData\Local\Google\Chrome\\User Data\Defaul')
driver = webdriver.Chrome(chrome_options=option)
driver.implicitly_wait(10)
driver.get("https://www.cnblogs.com/wangyjketang")
# 点击“新随笔”
driver.find_element_by_link_text("新随笔").click()
title = u"selenium3 + python3 --富文本"
content = u"这里是发帖的正文"
# 添加标题
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(title)
# 切换到内容框frame
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
time.sleep(3)
# driver.find_element_by_id("tinymce").send_keys(Keys.TAB)
driver.find_element_by_id("tinymce").send_keys(content)