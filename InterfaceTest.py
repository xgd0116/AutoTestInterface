# --coding=utf8--
import TestCase
import InterfaceInfo
import json


class InterfaceTest:

    def __init__(self, excel_name):
        self.excel_name = excel_name
        self.gtc = TestCase.TestCase(self.excel_name)
        self.param_list = self.gtc.return_param()

    # 传入Post/get 和请求地址,根据返回值和预期结果进行匹配,并返回测试结果(PASS/False)
    def test_result(self):
        # 执行case
        req = []
        for i in self.param_list:
            test_info = InterfaceInfo.InterfaceInfo(i[1].strip('\''), i[2].strip('\''))
            actual_result = test_info.interface_test()
            expect_result = json.loads(i[3].strip('\''))
            result = inf.set_result(expect_result,actual_result)
            if result:
                print("测试通过")
            else:
                print("测试失败")
        return req

    #expect_result:预期结果,actual_result:实际结果
    #判断结果是否符合预期
    def set_result(self,expect_result,actual_result):
        result = True
        for i in expect_result:
            if i == 'code' or i == 'msg':
                if expect_result[i] != actual_result[i]:
                    result = False
                    break
            elif i == 'other' or i == 'apver':
                if expect_result[i] != actual_result['data'][i]:
                    result = False
                    break
            else:
                if expect_result[i] != actual_result['data']['result'][i]:
                    result = False
                    break
        return result

excelName = 'Baihe_Login.xlsx'

inf = InterfaceTest(excelName)
inf.test_result()

