# coding:utf-8
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--user-data-dir=C:\\Users\shenfengcai\AppData\Local\Google\Chrome\\User Data\Defaul')
driver = webdriver.Chrome(chrome_options=option)
# 打开博客
driver.get('https://www.cnblogs.com/wangyjketang/')
driver.implicitly_wait(10)
# 点击“新随笔”
driver.find_element_by_link_text("新随笔").click()
# 点击“上传图片”
driver.find_element_by_css_selector("img.mceIcon").click()
# 找到所有iframe，并定位到第二个
frame = driver.find_elements_by_tag_name('iframe')[1]
# 切换到iframe
driver.switch_to.frame(frame)
# 点击“上传本地图片”，并上传
driver.find_element_by_name("file").send_keys("D:\AutoTest\python.jpg")