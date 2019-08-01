#coding:utf-8
from util.operate_excel import OperateExcel
from data import data_config
from util.operate_json import OpereatJson
import re
import json

class GetData:
    def __init__(self):
        self.opera_excel = OperateExcel()

    # 获取excel行数，即cases的个数
    def get_case_lines(self):
        return self.opera_excel.get_nrow()

    # 判断是否执行
    def get_is_run(self,row):
        flag = None
        col = data_config.get_run()
        is_run = self.opera_excel.get_cell(row,col)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def get_is_header(self,row):
        col = data_config.get_header()
        is_header = self.opera_excel.get_cell(row,col)
        if is_header == "":
            return None
        else:
            return is_header

    # 获取请求方式
    def get_request_method(self,row):
        col = data_config.get_request_way()
        method = self.opera_excel.get_cell(row,col)
        return method

    # 获取url
    def get_request_url(self,row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell(row,col)
        return url

    # 获取请求数据
    def get_request_data(self,row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell(row,col)
        if data == '':
            return None
        else:
            return data

    # 通过关键字从json文件中获取data对应的数据
    def get_data_from_json(self,row):
        opera = OpereatJson()
        request_data = opera.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self,row):
        col = data_config.get_expect()
        expect = self.opera_excel.get_cell(row,col)
        if expect == '':
            return None
        else:
            return expect

    # 将实际结果写入
    def write_result(self,row,value):
        col = data_config.get_result()
        self.opera_excel.write_cell(row,col,value)

    # 获取数据依赖
    def get_data_depend(self,row):
        col = data_config.get_data_depend()
        data_depend = self.opera_excel.get_cell(row,col)
        if data_depend == "":
            return None
        else:
            return data_depend

    # 获取case依赖
    def get_case_depend(self,row):
        col = data_config.get_case_depend()
        case_depend = self.opera_excel.get_cell(row,col)
        if case_depend == "":
            return None
        else:
            return case_depend

    # 获取依赖字段
    def get_field_depend(self,row):
        col = data_config.get_field_depend()
        depend_key = self.opera_excel.get_cell(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key

    # 从str中匹配{}形式的字符，并将其转换成字典格式
    def search_dict(self,bytes_obj):
        str = bytes.decode(bytes_obj)
        search_obj = re.search(r'[^{]*({.*})',str)
        if search_obj:
            search_obj = search_obj.group(1)  # 匹配{}
            # print("search_obj:",search_obj)
            search_obj = json.loads(search_obj)
        return search_obj

if __name__ == '__main__':
    byte_obj = b'aaaaa{"status":10001,"msg":"\\u6210\\u529f","data":{"userInfo":{"uid":"4699105"},"url":["http:\\/\\/www.imooc.com\\/user\\/ssologin?token=fpWSwOS9wD0dNvGQy9SEgaIl8GwoSiUQqgQHgsSPAgru9xxJPbVTuNtQuBB9bj1RabD6QFNZjTi9I_Xmcc_HOl7zTe2Gi1qmgTTVZbz0o7r1k1C2ZuLWYb1ep-pg-OrMLGe0fyXm0aPArepCCPLhpdhUY4EwNhaL9ZNQtmbi1mGbUsTN17JPh-g3FD_BIHIOdExPhfLRytG8OxENJIrxL5qOJE9AwnLcxMA52PKj5J_sAcUCLPe41tgQR0jeo0J-Fm5hAinS8l-IjL7xERyqDWbB4H8yqO-G-pjEKQnZ1H7Cd8w","http:\\/\\/coding.imooc.com\\/user\\/ssologin?token=MwzBv-2j6fSmEmF3zmr8bMo4kdhLXfEfKMYFQqMTvs9meP9oaJtV1CLttafwwjFPYhGgB0THgEHAEZpbaPA33ayLhZ1vzA51DSKH4m5mJNPPOWOgvnwtfZoUGBEGFHVUEEcZsu8FzTcJOfe3cKEyk02tu_oJXTG2zzljoL58LX1C1oMEpz8NHNsgSna4U2dntQUo2kS0oMfyWIxdda_zk-jYqOkpIz1y8mwWCxIRtmnv1YCxM3eZlMewq56JSIImj5JiB2us6CmQXYrVZUxNVDPYog31SM7P-RCxfDQM86BFZcWkK"]}}'
    data = GetData()
    dict = data.search_dict(byte_obj)
    print(dict)


