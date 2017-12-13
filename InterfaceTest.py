# --coding=utf8--
import TestCase
import InterfaceInfo
import operator


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
            s = test_info.interface_test()
            # if operator.eq(eval(i[3].strip('\"')), s):
            real_result = eval(i[3].strip('\"'))
            print(inf.walk_sort(real_result))
            if operator.eq(inf.walk_sort(s) , inf.walk_sort(real_result)):
                req.append('测试通过')
            else:
                req.append('测试失败')
        return req

    def walk_sort(self, v):
        if isinstance(v, dict):
            for i,j in v.items():
                inf.walk_sort(j)
        if isinstance(v, (tuple, list)):
            v.sort()
            for k in v:
                inf.walk_sort(k)
        return v

excelName = 'Baihe_Login.xlsx'

inf = InterfaceTest(excelName)
req1 = inf.test_result()
print(req1)

