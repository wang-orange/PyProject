#coding:utf-8
import json

class OpereatJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = "../config/login.json"
        else:
            self.file_path = file_path

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            try:
                data = json.load(fp)
            except:
                data = None
            return data

    # 根据关键字获取数据
    def get_data(self,keyword):
        return self.read_data()[keyword]

    # 将数据写入json文件
    def write_data(self,data):
        with open(self.file_path,'w') as wf:
            json.dump(data,wf)
            # wf.write(json.dumps(data))

if __name__ == "__main__":
    # opjson = OpereatJson()
    # # print(type(opjson.read_data()))
    # login_data = opjson.get_data('login')
    # print(login_data)
    cookie_json = OpereatJson('../config/cookie.json')
    print(cookie_json.read_data())

