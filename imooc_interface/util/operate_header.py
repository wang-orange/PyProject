#coding:utf-8
import requests
import json
from base.run_request import RunRequest
from util.operate_json import OpereatJson

class OperateHeader:
    '''获取、读写cookie
    '''
    def __init__(self,response):
        self.res = response
        cookie_path = "../config/cookie.json"
        self.opreate_json = OpereatJson(cookie_path)

    # 获取登录返回的token的url
    def get_response_url(self):
        url = self.res['data']['url'][0]
        return url

    # 获取cookie
    def get_cookie(self):
        data = "&callback=jQuery191017973647154617467_1553341637781&_=1553341637783"
        request_url = self.get_response_url() + data
        cookie = requests.get(request_url).cookies
        # print("cookie:",cookie)
        cookie = requests.utils.dict_from_cookiejar(cookie)
        return cookie

    # 将cookie写入文件
    def write_cookie(self):
        cookie = self.get_cookie()
        self.opreate_json.write_data(cookie)

    # 从cookie的json文件中读取cookie
    def read_cookie(self,key):
        cookie = self.opreate_json.get_data(key)
        return cookie

if __name__ == '__main__':
    url = "https://www.imooc.com/passport/user/login"
    data = {
        "username":"wangyunju@163.com",
		"password":"orange0419",
		"verify":"mx6y",
		"remember":"1",
		"pwencode":"0",
		"browser_key":"9849818247deb249853da175b9ea7312",
		"referer":"https://www.imooc.com"
    }
    res = requests.post(url,data).json()
    print(res)
    operate_header = OperateHeader(res)
    operate_header.write_cookie()
    data = operate_header.read_cookie()
    print(data)
