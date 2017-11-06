# --coding=utf8--
import xlrd
import datetime
from xlwt import*

class TestResult():
    def __init__(self, excelName, expectResult, actualResult):
        self.excelName = excelName
        self.expectResult = expectResult
        self.actualResult = actualResult

    def testResult(self):
        w = Workbook()

