#coding=utf-8

import xlrd
from xlutils.copy import copy

class ExcelUtil():
    def __init__(self,file_path=None,index=None):
        if file_path is None:
            self.file_path = 'F:/Python/5itest_po_3/config/keywords.xls'
        else:
            self.file_path = file_path
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.file_path,index)
        self.table = self.data.sheets()[index]
        #行数
        # rows = self.get_lines()

    #期待的文件格式
    #[[],[],[]]
    def get_data(self):
        # print(self.rows)
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    #写入数据
    def write_value(self,row,value):
        self.data = xlrd.open_workbook(self.file_path)
        read_value = self.data
        write_value = copy(read_value)
        write_value.get_sheet(0).write(row,9,value)
        write_value.save(self.file_path)

    def get_value(self,row,col):
        rows = self.get_lines()
        if row < rows:
            result = self.table.cell(row,col).value
            return result
        return None


    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

if __name__ == '__main__':
    instan = ExcelUtil(r'F:\Python\5itest_po_3\config\case_excel.xls')
    # instan.write_value(7,'test1')
    # print(instan.get_value(10,1))
    # print(instan.get_lines())
    print(instan.get_data())
    print(instan.get_value(1,1))