# coding:utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException

# 调用函数打印cookies
def print_cookies(driver):
    for ck in driver.get_cookies():
        print('%s -> %s' %(ck['name'], ck['value']))

driver = webdriver.Firefox()
# 打开浏览器后获取cookies，为空
print(driver.get_cookies())
# 打开具体的网页后获取cookies
driver.get("http://www.cnblogs.com/")
print(driver.get_cookies())
# 添加cookie
driver.add_cookie({'name':'wwwyyy','value':'2'})
print_cookies(driver)  # 调用函数打印cookies

'''
url = "https://passport.cnblogs.com/user/signin"
driver.get(url)
driver.implicitly_wait(10)
driver.find_element_by_id("input1").send_keys(u"汪orange")
driver.find_element_by_id("input2").send_keys("orange@0419")
driver.find_element_by_css_selector("input#signin").click()
driver.find_element_by_css_selector('div.geetest_wait').click()
dragger = driver.find_element_by_css_selector("div.geetest_slider_button")
action = ActionChains(driver)
action.click_and_hold(dragger).perform()  # 鼠标左键按下不放

for index in range(198):
    try:
        action.move_by_offset(index, 0).perform()  # 平行移动鼠标
    except  UnexpectedAlertPresentException:
        break
    action.reset_actions()
    time.sleep(0.1)  # 等待停顿时间

success_text = driver.switch_to.alert.text
print(success_text)
time.sleep(5)
'''

# 登录后通过加载配置文件的方式获取登录后的cookies
usrPath = r'C:\Users\shenfengcai\AppData\Roaming\Mozilla\Firefox\Profiles\ohiqzy43.default'
profile = webdriver.FirefoxProfile(usrPath)
driver = webdriver.Firefox(profile)
driver.get('https://www.cnblogs.com/')

print("**************************************** 1")
print_cookies(driver)  # 对比登录前后cookies变化

# 获取指定name的cookie
print("************************************** 2")
print(driver.get_cookie(name = '.CNBlogsCookie'))
print(driver.get_cookie(name = '.Cnblogs.AspNetCore.Cookies'))

# 删除指定name的cookie
driver.delete_cookie('.CNBlogsCookie')
print("************************************** 3")
print_cookies(driver)
# 为了验证此cookies是登录的，可以删除后刷新页面
driver.refresh()

# 删除所有的cookies
driver.delete_all_cookies()
print("************************************** 4")
print(driver.get_cookies())

# driver.quit()