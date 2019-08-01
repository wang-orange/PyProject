#coding:utf-8
import os
import sys
rootPath = os.path.dirname(os.getcwd())
sys.path.append(rootPath)  # 将项目所在目录添加到环境变量
from data.get_data import GetData
from base.send_requests import SendRequests
from data.get_depend import GetDepend
import json
from util.operate_cookies import OperateCookies
from util.common_util import CommonUtil
from util.send_email import SendEmail
import mock

class RunMain:
    def __init__(self):
        self.data = GetData()
        self.send = SendRequests()
        self.depend = GetDepend()
        self.operate_cookies = OperateCookies()

    def run_main(self):
        case_num = self.data.get_case_num()
        pass_count = 0
        fail_count = 0
        for i in range(1,case_num):
            is_run = self.data.get_is_run(i)
            if is_run == 'yes':
                print("----------- ",i)
                url = self.data.get_url(i)
                method = self.data.get_method(i)
                is_cookie = self.data.get_is_cookie(i)
                depend_case = self.data.get_depend_case(i)
                depend_field = self.data.get_depend_field(i)
                depend_key = self.data.get_depend_key(i)
                request_data = self.data.get_request_data(i)
                # expect = self.data.get_expect_from_db(i)
                expect = self.data.get_expect(i)
                # print(expect)
                if depend_case != '':
                    print(depend_field,depend_key)
                    new_depend_data = self.depend.get_depend_data(depend_case,depend_field)
                    print(new_depend_data)
                    request_data[depend_key] = new_depend_data
                cookies = None  # 存放cookies
                if is_cookie == 'yes':
                    cookies = self.operate_cookies.read_cookies()
                # send = mock.Mock(return_value=expect)
                # self.send.send_main = send
                res = self.send.send_main(url,method,request_data,cookies)
                if is_cookie == 'write':
                    self.operate_cookies.write_cookies(res.json())
                # 判断是否包含预期结果
                contain = CommonUtil()
                flag = contain.is_contain(expect,res)
                if flag: # 执行成功
                    print('--- 测试通过')
                    self.data.write_data(i,'pass')
                    pass_count = pass_count + 1
                else:
                    print('--- 测试失败')
                    res_str = bytes.decode(res.content)
                    self.data.write_data(i,res_str)
                    fail_count = fail_count + 1
                try:
                    res_format = json.dumps(res.json(),ensure_ascii=False,indent=2,sort_keys=True)
                    print(res_format)
                except:
                    print(res.content)
        # send_email = SendEmail()
        # send_email.send_main(pass_count,fail_count)

if __name__ == "__main__":
    run  = RunMain()
    res = run.run_main()
    print(res)



