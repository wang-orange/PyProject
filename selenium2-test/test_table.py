# coding:utf-8
from selenium import webdriver

# Firefox浏览器配置文件地址
# profile_directory = r"C:\Users\shenfengcai\AppData\Roaming\Mozilla\Firefox\Profiles\ohiqzy43.default"
# 加载配置
# profile = webdriver.FirefoxProfile(profile_directory)
# 打开火狐浏览器
# driver = webdriver.Firefox(profile)
driver = webdriver.Firefox()
url = "file:///D:/AutoTest/xml/table.html"
driver.get(url)
driver.implicitly_wait(10)
# s = driver.find_element_by_css_selector("#myTable>tbody>tr:nth-child(2)>td:nth-child(1)")
s = driver.find_element_by_xpath("//*[@id='myTable']/tbody/tr[2]/td[1]")
print s.text