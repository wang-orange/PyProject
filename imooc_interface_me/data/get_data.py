#coding:utf-8
from util.operate_excel import OperateExcel
from data.global_val import GlobalVal
from util.operate_json import OperateJson
import json
import re
from util.operate_db import OperateDB

class GetData:
    '''获取数据
    '''
    def __init__(self):
        self.excel = OperateExcel()
        self.global_val = GlobalVal()

    def get_case_num(self):
        '''获取cases数量
        '''
        return self.excel.get_nums()

    def get_url(self,row):
        '''获取url
        '''
        col = self.global_val.url
        return self.excel.get_cell(row,col)

    def get_is_run(self,row):
        '''获取是否运行
        '''
        col = self.global_val.is_run
        return self.excel.get_cell(row,col)

    def get_method(self,row):
        '''获取请求方式
        '''
        col = self.global_val.method
        return self.excel.get_cell(row,col)

    def get_is_cookie(self,row):
        '''获取是否携带cookies
        '''
        col = self.global_val.is_cookie
        return self.excel.get_cell(row,col)

    def get_depend_case(self,row):
        '''获取依赖case
        '''
        col = self.global_val.depend_case
        return self.excel.get_cell(row,col)

    def get_depend_field(self,row):
        '''获取依赖case返回数据的字段
        '''
        col = self.global_val.depend_field
        return self.excel.get_cell(row,col)

    def get_depend_key(self,row):
        '''获取依赖的key
        '''
        col = self.global_val.depend_key
        return self.excel.get_cell(row,col)

    def get_request_data(self,row):
        '''获取请求数据
        '''
        operate_json = OperateJson()
        col = self.global_val.request_data
        request_key = self.excel.get_cell(row,col)
        request_data = None
        if request_key != '':
            request_data = operate_json.get_data(request_key)
            for key in request_data:
                if not isinstance(request_data[key],str):  # 如果value不是str类型
                    request_data[key] = json.dumps(request_data[key])  # 将value转换成str类型
        return request_data

    def get_expect(self,row):
        '''获取预期结果
        '''
        col  = self.global_val.expect
        return self.excel.get_cell(row,col)

    def get_expect_from_db(self,row):
        '''根据预期sql语句从db中获取预期数据
        '''
        sql = self.get_expect(row)
        db = OperateDB()
        expect = db.search_one(sql)
        return expect

    def get_depend_case_row(self,depend_case):
        '''通过依赖的case，找到该case对应的行
        '''
        case_id = self.excel.get_col_values(0)
        id_row = 0
        for id in case_id:
            if id in depend_case:
                return id_row
            id_row = id_row + 1

    def write_data(self,row,data):
        '''运行失败，将返回结果写入excel
        '''
        # print(data)
        col = self.global_val.result
        self.excel.write_cell(row,col,data)

    def search_obj(self,res):
        '''从str中匹配{ },并转换成dict再返回
        '''
        res_str = res.content.decode()  # 将bytes类型转成str
        pattern = re.compile(r'[^{]*({.*}).*')  # 匹配{****}
        res_obj = re.search(pattern,res_str)
        if res_obj:
            obj = res_obj.group(1)
            obj = json.loads(obj)
        return obj

if __name__ == '__main__':
    data = GetData()
    # print(data.get_case_num())
    # print(data.get_expect(3))
    # print(data.get_request_data(1))
    # print(data.get_depend_case_row('Imooc-003'))
    # str = '{"result":-11,"data":"","msg":"\u6ca1\u6709\u767b\u5f55"}'
    # data.write_data(2,str)
    res = data.get_expect_from_db(1)
    print(res)



