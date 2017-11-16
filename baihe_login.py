# --coding=utf8--
import InterfaceTest

excelName = 'Baihe_Login.xlsx'
test = InterfaceTest.InterfaceTest(excelName)
s = test.test_result()
for i in s:
    print(i.strip('\''))
