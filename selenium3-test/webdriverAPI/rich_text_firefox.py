import time
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys

# 加载配置文件
file_path = r"C:\Users\shenfengcai\AppData\Roaming\Mozilla\Firefox\Profiles\ohiqzy43.default"
profile = webdriver.FirefoxProfile(file_path)
driver = webdriver.Firefox(profile)
url = "https://www.cnblogs.com/"
blog_name = "wangyjketang"
blog_path = os.path.join(url + blog_name)
print (blog_path)
driver.get(blog_path)
driver.implicitly_wait(5)
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
