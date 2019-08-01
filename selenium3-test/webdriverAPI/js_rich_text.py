# coding:utf-8

import os
import time
from selenium import webdriver

user_path = r"C:\Users\shenfengcai\AppData\Local\Temp\rust_mozprofile.bfJD92BHud0U"
profile = webdriver.FirefoxProfile(user_path)
driver = webdriver.Firefox(profile)
url = "https://www.cnblogs.com/"
blog_name = "wangyjketang"
blog_path = os.path.join(url + blog_name)
driver.get(blog_path)
driver.implicitly_wait(5)
# # 通过js添加新随笔
# driver.find_element_by_id("blog_nav_newpost").click()
# time.sleep(2)
# driver.find_element_by_id("Editor_Edit_txbTitle").send_keys("这里是标题2")
# time.sleep(3)
# body = u"这里是通过js发布的正文内容"
# js = 'document.getElementById("Editor_Edit_EditorBody_ifr").\
#       contentWindow.document.body.innerHTML="%s"' %body
# driver.execute_script(js)
# time.sleep(2)
# # 保存草稿
# driver.find_element_by_id("Editor_Edit_lkbDraft").click()
# time.sleep(2)
# 删除刚刚添加的草稿
driver.find_element_by_id("blog_nav_admin").click()
time.sleep(2)
driver.find_element_by_xpath("//tbody/tr[2]/td[6]/a").click()
time.sleep(2)
driver.switch_to.alert.accept()

