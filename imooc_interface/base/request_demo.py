import requests
import json

class RunMain:
    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)

    def send_post(self,url,data):
        '''
        发送post请求
        '''
        res = requests.post(url=url, data=data).json()
        return res
        # return json.dumps(res,indent=2, sort_keys=True)  # 参数indent表示缩进，值为0时只换行，2表示换行后缩进2个字符

    def send_get(self,url,data=None):
        '''
        发送get请求
        '''
        if data == None:
            res = requests.get(url=url).json()
        else:
            res = requests.get(url=url,params=data).json()
        return res
        # return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        print("*****************************")
        if method == 'GET':
            res = self.send_get(url,data)
        elif method == 'POST':
            res = self.send_post(url,data)
        else:
            res = None
        return res

if __name__ == '__main__':
    # 通过fiddler抓post和get请求
    post_url = "https://www.imooc.com/api3/getads"
    post_data = {
        'apiname': 'getads',
        'limit': '0',
        'marking': 'iosszbanner',
        'timestamp': '1550669203539',
        'token': 'b7287df1aab00c81c53d3ed3b2304761',
        'uid': '0'
    }
    # 参数放在url中
    get_url = "https://appicome.enn.cn:8076/dynamic/concern/getDynamicRecommendInfo?recommendPosition=1&recommendType=1"
    # 参数单独放
    get_url_1 = "https://appicome.enn.cn:8076/dynamic/concern/getDynamicRecommendInfo/"
    get_para = {
        'recommendPosition':'1',
        'recommendType':'1'
    }
    run = RunMain()
    res = run.run_main(get_url_1,'GET')
    print(res)
    # run = RunMain(post_url,'POST',post_data)
    # print(run.res)



