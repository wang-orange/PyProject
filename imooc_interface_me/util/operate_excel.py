#coding:utf-8
import xlrd
from xlutils.copy import copy

class OperateExcel:
    '''操作excel
    '''
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.file = '../config/cases.xls'
        else:
            self.file = excel_path
        if index == None:
            self.index = 0
        else:
            self.index = index
        self.data = self.get_data()
        self.table = self.get_sheet()

    def get_data(self):
        '''读取excel
        '''
        data = xlrd.open_workbook(self.file)
        return data

    def get_sheet(self):
        '''获取待操作的sheet
        '''
        table = self.data.sheets()[self.index]
        return table

    def get_nums(self):
        '''获取行数
        '''
        nums = self.table.nrows
        return nums

    def get_cell(self,nrow,ncol):
        '''获取单元格内容
        '''
        return self.table.cell_value(nrow,ncol)

    def get_row_values(self,nrow):
        '''获取某一行的内容
        '''
        return self.table.row_values(nrow)

    def get_col_values(self,ncol):
        '''获取某一列的内容
        '''
        return self.table.col_values(ncol)

    def write_cell(self,nrow,ncol,value):
        '''往单元格中写入内容
        '''
        read_data = xlrd.open_workbook(self.file)
        write_data = copy(read_data)
        table =  write_data.get_sheet(0)
        table.write(nrow,ncol,value)
        write_data.save(self.file)

if __name__ == '__main__':
    excel = OperateExcel()
    print(excel.get_cell(2,5))
    print(excel.get_nums())
    # excel.write_cell(7,1,'hello')

