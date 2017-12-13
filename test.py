# --coding=utf8--
import requests
import json
import datetime
import sys
import os
import platform
import TestCase
import operator

filetime = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
print(sys.path[0])
url = 'http://plus.app.baihe.com/register/login?traceID=1&systemID=2&params={"mobile":"15198067024","password":"111111","appId":"1","plusPhoneModel":"Xiaomi-MI 4W","plusChannel":"baihe_android_bhw_y","device":"864895021559263","appUpgradeVersionCode":76,"plusClientVersion":"7.4.0","apver":"7.4.0","plusCode":"0001","plusPhoneOSVersion":"4.4.4","plusPlatform":"1202","channel":""}'
req = requests.post(url=url)
# testresult = req.json()
testresult = req.json()
result = {"code":200,"msg":"","data":{"result":{"nickname":"\u963f\u72f8\u5230\u83b1\u5475\u5475","headPhotoUrl":"http:\/\/photo9.baihe.com\/2016\/03\/29\/120_150\/B05D51F18D35BC0F140D180A7ED5159D.jpg","gender":"0","age":30,"accountStatus":"1","marriage":"1","marriageChn":"\u672a\u5a5a","country":"86","countryChn":"\u4e2d\u56fd","province":"8611","provinceChn":"\u5317\u4eac\u5e02","city":"861101","cityChn":"\u5317\u4eac\u4e1c\u57ce","district":"861101","districtChn":"\u5317\u4eac\u4e1c\u57ce","income":"10","incomeChn":"25000-30000","isCreditedByAuth":"1","isCreditedById5":"1","isCreditedByMobile":"1","userService":98,"education":"3","educationChn":"\u9ad8\u4e2d","height":"180","iFindOpPrefer":"","prefer":"10_01_02,10_01_12,10_01_07,11_01_04,11_02_12,12_01_05,12_01_03,12_01_04,13_02_17","registerDate":"2015-10-14 15:01:26","longitude":"116.481271972656","latitude":"39.9960199652778","extra":"baihe","group_id":98,"birthday":"19871023","familyDescription":"\u65e0\u5b9e\u540d\u8ba4\u8bc1\uff0c\u65e0\u624b\u673a\u8ba4\u8bc1\uff0c\u65e0\u7167\u7247 \u52ff\u6270 \r\n\uff01\uff01\uff01\uff01\u5475\u5475\n\u83dc\u554a\u554a\u554a\n\u8c01\n\u662f\u8c01\n\u53c8\u662f\u8c01","hongdou":"","photosNumber":"0","dataIntegrity":"57","hasMainPhoto":"1","userID":"126784246","match":{"matchEducation":"1,2,3,4,5,6,7,8","matchIncome":"1,2,3,4,5,6,7,8","matchHousing":"1,2,3,4,5,6,7,8","matchMarriage":"1,2,3","matchChildren":"1,2,3,4","matchMinAge":"22","matchMaxAge":"44","matchMinHeight":"144","matchMaxHeight":"196","matchCountry":"86","matchCountryChn":"\u4e2d\u56fd","matchProvince":"8611","matchProvinceChn":"\u5317\u4eac\u5e02","matchCity":"","matchCityChn":"","matchDistrict":"","matchDistrictChn":""},"housing":"4","housingChn":"\u5df2\u8d2d\u623f(\u6709\u8d37\u6b3e)","children":"2","childrenChn":"\u6709\uff0c\u548c\u6211\u4f4f\u4e00\u8d77","loveType":"1","loveTypeChn":"\u54f2\u5b66\u5bb6\u578b","isCreditedBySesame":"0","headPhotoStatus":"1"},"other":0,"apver":"7.4.0"}}


def getvalues(v):
    s = []
    for i, j in v.items():
        if isinstance(j, dict):
            getvalues(j)
        else:
            s.append(str(i)+str(j))

r = json.loads(json.dumps(result))

print(getvalues(r))
# getvalues(testresult)


# result = {'code': 200, 'msg': '', 'data': {'result': {'nickname': '阿狸到莱呵呵',  'headPhotoUrl': 'http://photo11.baihe.com/2016/03/29/120_150/B05D51F18D35BC0F140D180A7ED5159D.jpg', 'gender': '0', 'age': 30, 'accountStatus': '1', 'marriage': '1', 'marriageChn': '未婚', 'country': '86', 'countryChn': '中国', 'province': '8611', 'provinceChn': '北京市', 'city': '861105', 'cityChn': '北京朝阳', 'district': '861105', 'districtChn': '北京朝阳', 'income': '11', 'incomeChn': '30000-50000', 'isCreditedByAuth': '0', 'isCreditedById5': '0', 'isCreditedByMobile': '1', 'userService': 114, 'education': '5', 'educationChn': '本科', 'height': '170', 'iFindOpPrefer': '', 'prefer': '10_01_02,10_01_11,10_01_12,10_02_16,10_02_13,11_01_01,11_03_16,11_02_08,12_01_08,12_01_04', 'registerDate': '2015-10-14 15:01:26', 'longitude': '116.481231282552', 'latitude': '39.9960582139757', 'extra': 'baihe', 'group_id': 114, 'birthday': '19871023', 'familyDescription': '此号不用了！！！！！！！！！！！！！！！！', 'hongdou': 108, 'photosNumber': '1', 'dataIntegrity': '64', 'hasMainPhoto': '1', 'userID': '126784246', 'match': {'matchEducation': '1,2,3,4,5,6,7,8', 'matchIncome': '1,2,3,4,5,6,7,8,9,10,11,12', 'matchHousing': '1,2,3,4,5,6,7,8', 'matchMarriage': '1,2,3', 'matchChildren': '1,2,3,4', 'matchMinAge': '18', 'matchMaxAge': '35', 'matchMinHeight': '144', 'matchMaxHeight': '210', 'matchCountry': '86', 'matchCountryChn': '中国', 'matchProvince': '8611', 'matchProvinceChn': '北京市', 'matchCity': '', 'matchCityChn': '', 'matchDistrict': '', 'matchDistrictChn': ''}, 'housing': '4', 'housingChn': '已购房(有贷款)', 'children': '2', 'childrenChn': '有，和我住一起', 'loveType': '1', 'loveTypeChn': '哲学家型', 'isCreditedBySesame': '0', 'headPhotoStatus': 1}, 'other': 0, 'apver': '7.4.0'}}
# result = {'code': 40075, 'msg': '为了保障您的账户安全,请输入验证码', 'data': {'result': {'num': 28, 'showCode': True, 'isBlackIP': 2}, 'other': 0, 'apver': '7.4.0'}}












