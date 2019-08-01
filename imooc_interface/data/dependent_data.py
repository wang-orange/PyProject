#coding:utf-8
from util.operate_excel import OperateExcel
from data.get_data import GetData
from base.run_request import RunRequest
from jsonpath_rw import jsonpath,parse
from util.operate_json import OpereatJson

class DependentData:
    ''' 获取依赖数据
    '''
    def __init__(self,case_id):
        self.case_id = case_id
        self.excel = OperateExcel()
        self.data = GetData()

    # 通过依赖的case_id得到该依赖case的行的内容
    def get_case_line_values(self):
        case_datas = self.excel.get_case_data(self.case_id)
        return case_datas

    # 执行依赖的case，得到运行结果
    def run_depend(self):
        row_num = self.excel.get_case_nrow(self.case_id)
        url = self.data.get_request_url(row_num)
        method = self.data.get_request_method(row_num)
        is_header = self.data.get_is_header(row_num)
        request_data = self.data.get_data_from_json(row_num)
        run = RunRequest()
        if is_header == 'yes':
            operate_json = OpereatJson('../config/cookie.json')
            cookies = operate_json.read_data()
            res = run.run_main(method,url,request_data,cookies)
        else:
            res = run.run_main(method,url,request_data)
        # print(res.content)
        return res

    #  根据依赖的key，从依赖case的响应中获取想要的字段
    def get_data_from_key(self,nrow):
        depend_data = self.data.get_data_depend(nrow)
        response_data = self.run_depend().content
        response_data = self.data.search_dict(response_data)  # 将str转换成dict
        jsonpath_expr = parse(depend_data)  # 按照该模式去搜索查找
        find_result = jsonpath_expr.find(response_data)
        return [match.value for match in find_result][0]


if __name__ == "__main__":
    depend = DependentData("Imooc-003")
    # res = depend.run_depend()
    # print(res.content)
    data = depend.get_data_from_key(5)
    print(data)


