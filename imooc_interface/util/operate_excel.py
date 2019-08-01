#coding:utf-8
import xlrd
from xlutils.copy import copy

class OperateExcel:
    def __init__(self, file_name=None, sheet_index=None):
        if file_name:
            self.file = file_name
            self.sheet_index = sheet_index
        else:
            self.file = '../config/interface.xls'
            self.sheet_index = 0
        self.table = self.get_table()

    # 获取sheet
    def get_table(self):
        excel = xlrd.open_workbook(self.file)
        table = excel.sheets()[self.sheet_index]
        return table

    # 获取行数
    def get_nrow(self):
        return self.table.nrows

    # 获取单元格内容
    def get_cell(self,nrow,ncol):
        # print("get_cell----",nrow,ncol)
        return self.table.cell_value(nrow,ncol)

    # 将数据追加写入单元格
    def write_cell(self,nrow,ncol,value):
        read_data = xlrd.open_workbook(self.file)  # 读取excel,此时为只读属性
        write_data = copy(read_data)  # 将r转为w
        sheet_data = write_data.get_sheet(0)  # 操作sheet1
        sheet_data.write(nrow,ncol,value)
        write_data.save(self.file)

    # 获取某一行的值，将以列表形式返回
    def get_row_values(self,nrow):
        return self.table.row_values(nrow)

    # 获取某一列的值，默认取第一列的内容
    def get_col_values(self,ncol=None):
        if ncol == None:
            ncol = 0
        return self.table.col_values(ncol)

    # 通过caseId定位该ID所在的行
    def get_case_nrow(self,case_id):
        case_ids = self.get_col_values()
        num = 0
        for id in case_ids:
            if case_id in id:
                return num
            num = num + 1

    # 通过caseId得到该行的内容
    def get_case_data(self,case_id):
        nrow = self.get_case_nrow(case_id)
        row_datas = self.get_row_values(nrow)
        return row_datas

if __name__ == '__main__':
    excel = OperateExcel()
    # print(excel.get_nrow())
    # print(excel.get_cell(1,3))
    # print(excel.get_row_value(0))
    # excel.write_cell(1,11,'pass')
    datas = excel.get_case_data('Imooc-001')
    print(datas)


