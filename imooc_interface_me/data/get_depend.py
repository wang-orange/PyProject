#coding:utf-8
from jsonpath_rw import jsonpath,parse
from data.get_data import GetData
from base.send_requests import SendRequests
from util.operate_cookies import OperateCookies


class GetDepend:
    '''处理有依赖的case
    '''
    def run_depend(self,depend_case):
        '''执行依赖的case
        '''
        data = GetData()
        send = SendRequests()
        # print(depend_case)
        row = data.get_depend_case_row(depend_case)
        # print(row)
        url = data.get_url(row)
        method = data.get_method(row)
        is_cookie = data.get_is_cookie(row)
        cookies = None
        if is_cookie == 'yes':
            ope_cookies = OperateCookies()
            cookies = ope_cookies.read_cookies()
        request_data = data.get_request_data(row)
        response = send.send_main(url,method,request_data,cookies)
        return response

    def get_depend_data(self,depend_case,depend_field):
        '''从依赖case的返回结果中获取依赖的字段
        '''
        data = GetData()
        response_data = self.run_depend(depend_case)
        response = data.search_obj(response_data)
        jsonpath_exp = parse(depend_field)
        result = jsonpath_exp.find(response)
        # print(result)
        return [match.value for match in result][0]
