# --coding=utf8--
import xlrd
import datetime
from xlwt import*
import shutil
import sys
import platform
import os


class Result1:

    def __init__(self, excel_name):
        pf_system = platform.system()
        if pf_system == 'windows':
            self.str_system = '\\'
        elif pf_system == 'Linux' or pf_system == 'Darwin':
            self.str_system = '/'
        self.excel_name = excel_name
        self.case_path = sys.path[0] + self.str_system + 'TestCase' + self.str_system + self.excel_name
        self.filetime = datetime.datetime.now().strftime('%Y-%m-%d-%H')
        filtertime = datetime.datetime.now().strftime('%Y-%m-%d')
        self.filterpath = sys.path[0] + self.str_system + 'TestCase' + self.str_system + 'TestResult' + \
                    self.str_system + filtertime

        # 根据当前日期,创建对应的文件夹
        if os.path.exists(self.filterpath) is not True:
            os.mkdir(self.filterpath)


    def set_excel_result(self):
        excel_name = self.excel_name.strip('.xlsx')
        new_filepath = self.filterpath + self.str_system + excel_name + '_' + self.filetime+'.xlsx'
        if os.path.isfile(new_filepath) is not True:
            shutil.copyfile(self.case_path, new_filepath)



excelName = 'Baihe_Login.xlsx'
r = Result1(excelName)
r.set_excel_result()




