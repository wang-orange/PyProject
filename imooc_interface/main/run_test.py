#coding:utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.dirname(curPath)
sys.path.append(rootPath)
from data.get_data import GetData
from base.run_request import RunRequest
import json
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.operate_header import OperateHeader
from util.operate_json import OpereatJson
from util.send_email import SendMail
import unittest
import HTMLTestRunner

class RunTest(unittest.TestCase):
    # def __init__(self,methodName='runTest'):
    #     self.run_method = RunRequest()
    #     self.data = GetData()

    # 程序执行的入口
    def test_go_on_run(self):
        run_method = RunRequest()
        data = GetData()
        cases_num = data.get_case_lines()
        fail_count = 0
        pass_count = 0

        for i in range(1,cases_num):
            url = data.get_request_url(i)
            method = data.get_request_method(i)
            cookie_flag = data.get_is_header(i)
            request_data = data.get_data_from_json(i)
            is_run = data.get_is_run(i)
            expect = data.get_expect_data(i)
            depend_case = data.get_case_depend(i)
            depend = DependentData(depend_case)
            if is_run:
                print("--------------run ",i)
                if depend_case != None:  # 有依赖case
                    print("-------------->depend")
                    # 获取依赖的响应数据
                    depend_response_data = depend.get_data_from_key(i)
                    depend_field = data.get_field_depend(i)
                    # 更新依赖字段的值
                    request_data[depend_field] = depend_response_data
                if cookie_flag == 'write':  # 需要写入cookies
                    res = run_method.run_main(method,url,request_data)
                    print(res)
                    operate_header = OperateHeader(res.json())
                    operate_header.write_cookie()
                elif cookie_flag == 'yes':  # 需要携带cookies
                    operate_json = OpereatJson('../config/cookie.json')
                    cookies = operate_json.read_data()
                    # print(cookies)
                    res = run_method.run_main(method,url,request_data,cookies)
                else:
                    res = run_method.run_main(method,url,request_data)
                com = CommonUtil()
                res_str = bytes.decode(res.content)
                # self.data.write_result(i,res_str)
                if com.is_contains(expect, res_str):
                    print("测试通过")
                    # self.assertTrue(True)
                    pass_count = pass_count+1
                    data.write_result(i,"pass")
                else:
                    print("测试失败")
                    # self.assertTrue(False)
                    data.write_result(i,res_str)
                    fail_count = fail_count+1
                res_dict = data.search_dict(res.content)
                if res_dict:
                    res_format = json.dumps(res_dict,ensure_ascii=False,indent=2,sort_keys=True)
                    print(res_format)
                else:
                    print(res.content)
        print(pass_count, fail_count)
        send = SendMail()
        send.send_main(pass_count, fail_count)

if __name__ == '__main__':
    run_test = RunTest()
    # print(run.go_on_run())
    suite = unittest.TestSuite()
    suite.addTest(RunTest('test_go_on_run'))
    report = '../report/TestReport.html'
    with open(report,'wb') as wf:
        run = HTMLTestRunner.HTMLTestRunner(wf, title= '接口自动化测试', description= '接口自动化测试结果统计')
        run.run(suite)


