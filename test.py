# --coding=utf8--
import requests
import json
import datetime
import sys
import os
import platform
import GetTestCase
import operator

filetime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
# print(sys.path[0])
# url = 'http://plus.app.baihe.com/register/login?traceID=1&systemID=2&params={"mobile":"15198067024","password":"111111","appId":"1","plusPhoneModel":"Xiaomi-MI 4W","plusChannel":"baihe_android_bhw_y","device":"864895021559263","appUpgradeVersionCode":76,"plusClientVersion":"7.4.0","apver":"7.4.0","plusCode":"0001","plusPhoneOSVersion":"4.4.4","plusPlatform":"1202","channel":""}'
# req = requests.post(url=url)
# print(req.json())

#
# result = {'msg': '', 'code': 200, 'data': {'result': {'headPhotoUrl': 'http://photo11.baihe.com/2016/03/29/120_150/B05D51F18D35BC0F140D180A7ED5159D.jpg', 'nickname': '阿狸到莱呵呵',  'gender': '0', 'age': 30, 'accountStatus': '1', 'marriage': '1', 'marriageChn': '未婚', 'country': '86', 'countryChn': '中国', 'province': '8611', 'provinceChn': '北京市', 'city': '861105', 'cityChn': '北京朝阳', 'district': '861105', 'districtChn': '北京朝阳', 'income': '11', 'incomeChn': '30000-50000', 'isCreditedByAuth': '0', 'isCreditedById5': '0', 'isCreditedByMobile': '1', 'userService': 114, 'education': '5', 'educationChn': '本科', 'height': '170', 'iFindOpPrefer': '', 'prefer': '10_01_02,10_01_11,10_01_12,10_02_16,10_02_13,11_01_01,11_03_16,11_02_08,12_01_08,12_01_04', 'registerDate': '2015-10-14 15:01:26', 'longitude': '116.481231282552', 'latitude': '39.9960582139757', 'extra': 'baihe', 'group_id': 114, 'birthday': '19871023', 'familyDescription': '此号不用了！！！！！！！！！！！！！！！！', 'hongdou': 108, 'photosNumber': '1', 'dataIntegrity': '64', 'hasMainPhoto': '1', 'userID': '126784246', 'match': {'matchEducation': '1,2,3,4,5,6,7,8', 'matchIncome': '1,2,3,4,5,6,7,8,9,10,11,12', 'matchHousing': '1,2,3,4,5,6,7,8', 'matchMarriage': '1,2,3', 'matchChildren': '1,2,3,4', 'matchMinAge': '18', 'matchMaxAge': '35', 'matchMinHeight': '144', 'matchMaxHeight': '210', 'matchCountry': '86', 'matchCountryChn': '中国', 'matchProvince': '8611', 'matchProvinceChn': '北京市', 'matchCity': '', 'matchCityChn': '', 'matchDistrict': '', 'matchDistrictChn': ''}, 'housing': '4', 'housingChn': '已购房(有贷款)', 'children': '2', 'childrenChn': '有，和我住一起', 'loveType': '1', 'loveTypeChn': '哲学家型', 'isCreditedBySesame': '0', 'headPhotoStatus': 1}, 'other': 0, 'apver': '7.4.0'}}
# # print(result.__class__)
#
# excelName = 'Baihe_Login.xlsx'
# s = GetTestCase.GetTestCase(excelName).return_param()
#
# for i in s:
#     ss = eval(i[2].strip('\"'))
#     if operator.eq(result, ss):
#         print('OK')
#     else:
#         print('Fail')

print(filetime)




