# --coding=utf8--
import xlrd
import sys
import platform


class GetTestCase:

    # 获取当前系统信息,根据系统使用不同的反斜杠
    def __init__(self, excel_name):
        pf_system = platform.system()
        if pf_system == 'windows':
            self.str_system = '\\'
        elif pf_system == 'Linux' or pf_system == 'Darwin':
            self.str_system = '/'
        self.excel_name = excel_name
        self.excel_path = sys.path[0] + self.str_system + 'TestCase' + self.str_system + self.excel_name

    # 根据excelName获取表格中的用例
    def return_param(self):
        # 打开一个excel表格
        excel_data = xlrd.open_workbook(self.excel_path)

        # 获取sheet页
        excel_table = excel_data.sheet_by_index(0)

        # table.ncols获取总列数，table.nrows获取总行数
        table_ncols = excel_table.ncols
        table_nrows = excel_table.nrows

        return_list = []
        nrows_list = []

        # 将表格中的内容添加到list中
        for i in range(1, table_nrows):
            nrows_list.clear()
            for j in range(table_ncols):
                s = str(excel_table.cell(i, j))
                nrows_list.append(s[5:])
            return_list.append(nrows_list)
        return return_list



