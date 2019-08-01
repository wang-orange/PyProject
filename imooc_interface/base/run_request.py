#coding:utf-8
import requests

class RunRequest:
    def post_main(self,url,data,header=None):
        ''' Post 请求 '''
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        # print(res.status_code)
        return res

    def get_main(self,url,data=None,header=None):
        ''' Get 请求 '''
        if header != None:
            res = requests.get(url=url,params=data,cookies=header)
        else:
            res = requests.get(url=url,params=data)
        # print(res.status_code)
        return res

    def run_main(self,method,url,data=None,header=None):
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res

if __name__ == '__main__':
    run = RunRequest()
    # url = "https://coding.imooc.com/lesson/ajaxmediauser/"
    # data = {"mid":"8371","learn_time":"660.418","mode":"video","video_point":"1298"}
    # method =  "post"
    # header = None
    # res = run.run_main(method,url,data,header)
    # print(res.json())
    url = "https://order.imooc.com/pay/submitorder"
    data = {'jsonpcallback': 'jQuery1113016267611019698558_1553176082724', 'goods_ids': '1400', '_': '1553176082729'}
    cookie = {"apsid": "hlYWY1ZDcyN2YxODU0NjAxNTU2NjAyM2NiNGI2NzkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANDY5OTEwNQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB3YW5neXVuanVAMTYzLmNvbQAAAAAAAAAAAAAAAAAAADVkNjUwYzQzMzZhNjgzZTU3Y2M4MGFlMDAzOTMwOGM2S9OWXDNEIlo%3DMD", "cvde": "5c96d34b334db-1", "imooc_isnew": "1", "imooc_isnew_ct": "1553388363", "imooc_uuid": "44e20630-a14f-42f4-981f-d161b166f71f", "last_login_username": "wangyunju%40163.com", "loginstate": "1"}
    res = run.get_main(url,data,cookie)
    print(res.text)




