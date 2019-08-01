# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 加载配置
profileDir = r"C:\Users\shenfengcai\AppData\Roaming\Mozilla\Firefox\Profiles\ohiqzy43.default"
profile = webdriver.FirefoxProfile(profileDir)
driver = webdriver.Firefox(profile)
# 博客首页地址
blog_url = "http://www.cnblogs.com/"
# yoyo的博客地址
yoyo_blog = blog_url + 'wangyjketang'
# 打开yoyo的博客
driver = driver.get(yoyo_blog)
# 点击“新随笔”按钮
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(5)
edit_title = u"Selenium2+python自动化23-富文本"
edit_body = u"这里是发帖的正文"
# 输入标题
driver.find_element_by_id("Editor_Edit_txbTitle").sendkeys(edit_title)
# 切换到正文frame
driver.switch_to.frame("Editor_Edit_EditorBody_ifr")
# 如果输入不成功，可以在输入之前先按个table键
driver.find_element_by_id("tinymce").sendkeys(Keys.TAB)
# 输入正文
driver.find_element_by_id("tinymce").sendkeys(edit_body)
