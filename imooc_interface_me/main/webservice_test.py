# coding=utf-8
from suds.client import Client
import time

# IP地址搜索
url = "http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
# qq在线状态测试
url2 = "http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl"
# 创建webservice client对象
client = Client(url)
# 打印client对象所有的方法
# print(client)
# # 调用方法
# # result = client.service.qqCheckOnline('1234567')
# result = client.service.getCountryCityByIp('222.111.111.111')
# print(result)

def get_method_name():
    method_list = []
    for i in client.wsdl.services[0].ports[0].methods:
        method_list.append(i)
    return method_list

for i in get_method_name():
    print(i)
    # 找到字符串i在对象client.service中对应的方法
    func = getattr(client.service,i)
    try:
        result = func('222.111.111.111')
    except:
         result = func()
    print(result)
