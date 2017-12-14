import requests
import json

class AccountLogin:

    def __init__(self, username, password, apver):
        self.username = username
        self.password = password
        self.apver = apver

    def login(self):
        data = {}
        data['mobile'] = self.username
        data['password'] = self.password
        data['appId'] = 1
        data['plusPhoneModel'] = 'Xiaomi-MI4W'
        data['plusChannel'] = 'baihe_android_bhw_y'
        data['device'] = '864895021559263'
        data['appUpgradeVersionCode'] = 76
        data['plusClientVersion'] = self.apver
        data['apver'] = self.apver
        data['plusCode'] = '0001'
        data['plusPhoneOSVersion'] = '4.4.4'
        data['plusPlatform'] = '1202'
        data['channel'] = ''

        all_param = {}
        all_param['params'] = json.dumps(data)
        all_param['traceID'] = '1'
        all_param['systemID'] = '2'

        test_url = 'http://plus.app.baihe.com/register/login'
        req = requests.post(test_url, all_param)
        print(req.json())
        print(req.cookies)



if __name__ == '__main__':
    AccountLogin('13716927954', 'qqqqqqqq', '7.6.0').login()

