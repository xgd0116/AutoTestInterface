# --coding=utf8--
import GetTestCase
import InterfaceInfo
import json
class InterfaceTest():

    def __init__(self, excelName):
        self.excelName = excelName

    def interfaceTest(self):
        gtc = GetTestCase.GetTestCase(self.excelName)
        paramList = gtc.returnParam()
        for i in paramList:
            testInfo = InterfaceInfo.InterfaceInfo(i[0].strip('\''), i[1].strip('\''))
            s = testInfo.interfaceTest()
            print(s)


test = InterfaceTest('Baihe_Login.xlsx')
test.interfaceTest()