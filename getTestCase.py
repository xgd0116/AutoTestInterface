# --coding=utf8--
import xlrd
import sys

class GetTestCase(object):

    def __init__(self, excelName):
        self.excelPath = sys.path[0] + '\TestCase\\' + excelName
        self.excelName = excelName

    #根据excelName获取表格中的用例
    def returnParam(self):
        #打开一个excel表格
        excelData = xlrd.open_workbook(self.excelPath)

        #获取sheet页
        excelTable = excelData.sheet_by_index(0)

        #table.ncols获取总列数，table.nrows获取总行数
        tableNcols = excelTable.ncols
        tableNrows = excelTable.nrows

        returnList = []
        NrowsList = []

        #将表格中的内容添加到list中
        for i in range(1, tableNrows):
            NrowsList.clear()
            for j in range(tableNcols):
                s = str(excelTable.cell(i, j))
                NrowsList.append(s[5:])
            returnList.append(NrowsList)
        return returnList



