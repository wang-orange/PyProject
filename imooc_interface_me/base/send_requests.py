#coding:utf-8
import requests

class SendRequests:
    '''发送请求
    '''
    def send_post(self,url,data,cookies=None):
        '''发送post请求
        '''
        if cookies == None:
            # 通过fiddler抓包时，需加上参数verify=False，否则https会报错
            response = requests.post(url=url,data=data,verify=False)
        else:
            response = requests.post(url,data,cookies,verify=False)
        return response

    def send_put(self,url,data,cookies=None):
        '''发送put请求
        '''
        if cookies == None:
            # 通过fiddler抓包时，需加上参数verify=False，否则https会报错
            response = requests.put(url=url,data=data,verify=False)
        else:
            response = requests.put(url=url,data=data,cookies=cookies,verify=False)
        return response

    def send_get(self,url,data=None,cookies=None):
        '''发送get请求
        '''
        if data == None:
            if cookies == None:
                response = requests.get(url,verify=False)
            else:
                response = requests.get(url,cookies,verify=False)
        else:
            if cookies == None:
                response = requests.get(url,data,verify=False)
            else:
                response = requests.get(url=url,params=data,cookies=cookies,verify=False)
        return response

    def send_delete(self,url,data=None,cookies=None):
        '''发送delete请求
        '''
        if data == None:
            if cookies == None:
                response = requests.delete(url,verify=False)
            else:
                response = requests.delete(url,cookies,verify=False)
        else:
            if cookies == None:
                response = requests.delete(url,data,verify=False)
            else:
                response = requests.delete(url=url,params=data,cookies=cookies,verify=False)
        return response

    def send_main(self,url,method,data=None,cookies=None):
        '''发送请求，主入口
        '''
        # print("-------------->>send_main")
        # print(url,method,data,cookies)
        if method == 'post':
            res = self.send_post(url,data,cookies)
        elif method == 'put':
            res = self.send_put(url,data,cookies)
        elif method == 'delete':
            res = self.send_delete(url,data,cookies)
        else:
            res = self.send_get(url,data,cookies)
        return res

if __name__ == "__main__":
    send = SendRequests()
    url = "https://www.imooc.com/passport/user/login"
    method = "post"
    data = {'username': 'wangyunju@163.com', 'password': 'orange0419', 'verify': 'mx6y', 'remember': '1', 'pwencode': '0', 'browser_key': '9849818247deb249853da175b9ea7312', 'referer': 'https://www.imooc.com'}
    cookies = None
    res = send.send_main(url,method,data,cookies)
    print(res)
