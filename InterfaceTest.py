# --coding=utf8--
import GetTestCase
import InterfaceInfo
import operator


class InterfaceTest:

    def __init__(self, excel_name):
        self.excel_name = excel_name
        self.gtc = GetTestCase.GetTestCase(self.excel_name)
        self.param_list = self.gtc.return_param()

    # 传入Post/get 和请求地址,根据返回值和预期结果进行匹配,并整理到excel表格中
    def test_result(self):

        # 创建对应的result表格

        # 执行case
        for i in self.param_list:
            test_info = InterfaceInfo.InterfaceInfo(i[1].strip('\''), i[2].strip('\''))
            s = test_info.interface_test()
            if operator.eq(eval(i[3].strip('\"')), s):
                return True
        return True





    # 判断预期结果和实际结果是否一致,test_result为预期结果,real_result为实际结果,其中,参数需要为dict
    def equal_result(self, test_result, real_result):
        if operator.eq(test_result, real_result):
            return True
        else:
            return False

excelName = 'Baihe_Login.xlsx'

inf = InterfaceTest(excelName)
inf.add_result()

