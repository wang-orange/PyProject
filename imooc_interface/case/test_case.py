#coding:utf-8
import unittest
from base.request_demo import RunMain
import HTMLTestRunner
import mock

class TestMethod(unittest.TestCase):

    # 执行用例之前执行一次
    def setUp(self):
        self.run = RunMain()

    # # 执行用例之后执行一次
    # def tearDown(self):
    #     print("This is --->tearDown")

    @classmethod
    def setUpClass(cls):
        '''
        类执行之前的方法
        '''
        print("类执行之前的方法")
        # global run
        # cls.run = RunMain()

    @classmethod
    def tearDownClass(cls):
        '''
        类执行之后的方法
        '''
        print("类执行之后的方法")

    # @unittest.skip('test_01')  # 跳过该用例
    def test_01(self):
        print("这是第一个case")
        get_url = "https://appicome.enn.cn:8076/dynamic/concern/getDynamicRecommendInfo/"
        get_para = {
        'recommendPosition':'1',
        'recommendType':'1'
        }
        response_data = {'code':'1234', 'name':'zhangsan'}
        self.run.run_main = mock.Mock(return_value=response_data)  # 通过mock对象替换掉self.run.run_main
        res = self.run.run_main(get_url,'GET',get_para)
        print(res)
        self.assertEqual(res['code'],'1234','测试成功！')

    def test_02(self):
        print("这是第二个case")
        get_url = "https://appicome.enn.cn:8076/dynamic/concern/getDynamicRecommendInfo/"
        get_para = {
        'recommendPosition':'0',
        'recommendType':'1'
        }
        res = self.run.run_main(get_url,'GET',get_para)
        print(res)
        self.assertEqual(res['code'],'802900','测试失败！')

if __name__ == '__main__':
    # unittest.main()  # 1-运行所有case
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))
    unittest.TextTestRunner().run(suite)  # 2-选择性运行某些case
    # filepath = '../report/TestReport.html'
    # with open(filepath,'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(fp,title='测试练习',description='This is first test')
    #     runner.run(suit)

