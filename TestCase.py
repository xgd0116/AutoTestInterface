# --coding=utf8--
import xlrd
import sys
import platform
import datetime
import os
import shutil


class TestCase:

    def __init__(self, excel_name):
        # 获取当前系统信息,根据系统使用不同的反斜杠
        pf_system = platform.system()
        if pf_system == 'windows':
            self.str_system = '\\'
        elif pf_system == 'Linux' or pf_system == 'Darwin':
            self.str_system = '/'
        self.excel_name = excel_name
        # 当前用例文件夹路径
        self.excel_path = sys.path[0] + self.str_system + 'TestCase' + self.str_system + self.excel_name
        # 当前用例表格路径
        self.case_path = sys.path[0] + self.str_system + 'TestCase' + self.str_system + self.excel_name
        # 获取当前日期(年-月-日-时)--用作结果文件夹命名
        self.filetime = datetime.datetime.now().strftime('%Y-%m-%d-%H')
        # 获取当前日期(年-月-日)--用作结果表格命名
        self.filtertime = datetime.datetime.now().strftime('%Y-%m-%d')
        # 结果表格路径
        self.filterpath = sys.path[0] + self.str_system + 'TestCase' + self.str_system + 'TestResult' + \
                    self.str_system + self.filtertime
        # 根据当前日期,创建对应的文件夹
        if os.path.exists(self.filterpath) is not True:
            os.mkdir(self.filterpath)
        # 生成以用例表格名来命名的结果表格
        excel_name = self.excel_name.strip('.xlsx')
        new_filepath = self.filterpath + self.str_system + excel_name + '_' + self.filetime+'.xlsx'
        # 创建当前日期的TestResult表格
        if os.path.isfile(new_filepath) is not True:
            shutil.copy(self.case_path, new_filepath)
        # 打开用例表
        self.excel_data = xlrd.open_workbook(self.excel_path)
        self.excel_table = self.excel_data.sheet_by_index(0)
        # 用例表格总列数
        self.table_ncols = self.excel_table.ncols
        # 用例表格总行数
        self.table_nrows = self.excel_table.nrows
        # 打开结果表
        # self.excel_result = xlrd.open_workbook(self.filterpath)
    # 返回表格中的用例数据
    def return_param(self):
        return_list = []
        # 将表格中的内容添加到list中
        for i in range(1, self.table_nrows):
            nrows_list = []
            for j in range(self.table_ncols):
                s = str(self.excel_table.cell(i, j))
                nrows_list.append(s[5:])
            return_list.append(nrows_list)
        return return_list

    # 将结果添加到表格中
    def set_excel_result(self):
        print()




