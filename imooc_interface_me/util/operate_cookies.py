#coding:utf-8
from util.operate_json import OperateJson
import requests
import json

class OperateCookies:
    '''从登陆信息中获取cookies
    '''
    def __init__(self):
        self.cookies_file = '../config/cookies.json'

    def get_url(self,res):
        url = res['data']['url'][0]
        return url

    def get_cookies(self,res):
        '''获取cookies
        '''
        data = "&callback=jQuery191010859009273660991_1554028835974&_=1554028835976"
        url = self.get_url(res) + data
        response = requests.get(url)
        cookies_jar = response.cookies
        cookies_dict = requests.utils.dict_from_cookiejar(cookies_jar)
        return cookies_dict

    def write_cookies(self,res):
        '''将cookies写入json文件
        '''
        cookies = self.get_cookies(res)
        with open(self.cookies_file,'w') as fp:
            json.dump(cookies,fp)

    def read_cookies(self):
        '''从json文件中读取cookies
        '''
        ope_json = OperateJson(self.cookies_file)
        cookies = ope_json.read_json()
        return cookies






