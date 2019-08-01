#coding:utf-8
import json
import requests

class OperateJson:
    '''操作json文件
    '''
    def __init__(self,file_path=None):
        if file_path == None:
            self.file = '../config/login.json'
        else:
            self.file = file_path

    def read_json(self):
        '''读取请求数据
        '''
        with open(self.file) as rf:
            data = json.load(rf)
            return data

    def get_data(self,key):
        '''通过关键字获取对应的数据
        '''
        try:
            return self.read_json()[key]
        except:
            return None


if __name__ == '__main__':
    operate_json = OperateJson()
    # cookie_json = OperateJson('../config/cookies.json')
    # print(operate_json.get_data('submit'))
    # cookies = {'login':"wangyunju1erty"}
    # cookie_json.write_cookie_json(cookies)
    data = operate_json.get_data("check_list")
    print(data)
