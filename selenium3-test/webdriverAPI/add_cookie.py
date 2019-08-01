# coding:utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.cnblogs.com/")
time.sleep(3)
cookie1 = {'name': '.CNBlogsCookie',
           'value': 'FCAC4B9776B5DF5140FA4A072B32408642E4C2BB13D0115CD5C676D051B786F8C2EDA56FEAE0F7DAFBF3C745B9DE71EB939BDC1C867C47F285D3035F2145ED1879C79DC0C004E7897EA2C65ECB76B92008556A96',
           'path': '/',
           'domain': 'cnblogs.com',  # 获取的cookie中‘domain’为‘.cnblogs.com’，但此处需要把‘.’去掉
           'expiry': 1539783194,
           'secure': False,
           'httpOnly': True}
cookie2 = {'name': '.Cnblogs.AspNetCore.Cookies',
           'value': 'CfDJ8J0rgDI0eRtJkfTEZKR_e80Zprny1Uo2EDP9Pg6BsUWMenKY41aunrqUD5a3M2v82IsTdokxk2pmvpCR6zhWzgKualM9oEguvENCFz8-ZFaoGmPuxWHUgLItB3gtcQlPqpB3tyAPapBf2ecAaj1AHpH4vmeull-5sWrcEFlz3ktA4ahRRZ-icyHUB4sVOVRb_qmGmKgNWiHPZGw9muP1sBjhwb2nTurFCa3JxSpfmdQPQ8jP8ErPqBEtyugcp6ET5k1dnPwCpo6N2_yCnuAznenW9WH_wXV7LHM9GLF0anIOr9Js0bYF1SQ41PghvC7OFQ',
           'path': '/',
           'domain': 'cnblogs.com',
           'expiry': 1539783195,
           'secure': False,
           'httpOnly': True}

driver.add_cookie(cookie1)
driver.add_cookie(cookie2)
# 添加登录的cookie后刷新页面，变成登录状态
time.sleep(3)
driver.refresh()