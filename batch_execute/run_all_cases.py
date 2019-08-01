# coding:utf-8
import unittest
import os
import HTMLTestRunner

# case路径
# case_path = os.path.join(os.getcwd(), 'case')
case_path = "./case"
print(case_path)
# 报告存放路径
report_path = os.path.join(os.getcwd(), 'report')

def all_cases():
    discover = unittest.TestLoader().discover(case_path, pattern="test*.py",top_level_dir=None)
    # print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_cases())
    report = os.path.join(report_path, 'result.html')
    with open(report,'wb') as fo:
        runner = HTMLTestRunner.HTMLTestRunner(fo, title=u'自动化测试报告，测试结果如下：',\
                                           description=u'用例执行情况')
        runner.run(all_cases())
