# coding=utf-8
from suds.client import Client

class WebserviceTest:
    def __init__(self,url):
        ''' 实例化client
        '''
        self.client = Client(url)

    def get_method_name(self):
        ''' 获取所有方法名称
        '''
        method_list = []
        for i in self.client.wsdl.services[0].ports[0].methods:
            method_list.append(i)
        return method_list

    def get_method_paras(self,method_name):
        ''' 根据方法名获取方法的参数
        '''
        method = self.client.wsdl.services[0].ports[0].methods[method_name]
        # print(method)
        input_paras = method.binding.input
        # print(input_paras)
        paras = input_paras.param_defs(method)[0]
        print(paras)
        return paras[1].name, paras[1].type[0]

    def run_main(self):
        ''' 逐个调用方法
        '''
        for method in self.get_method_name():
            print(method)
            # paras = self.get_method_paras(method)
            # print(paras)
            # 找到字符串i在对象client.service中对应的方法
            func = getattr(self.client.service,method)
            try:
                result = func('222.111.111.111')
            except:
                 result = func()
            print(result)

if __name__ == '__main__':
    url = "http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl"
    url_1 = "http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"
    web = WebserviceTest(url_1)
    # web.excute_method()
    # print(web.get_method_paras('getGeoIPContext'))
    web.run_main()