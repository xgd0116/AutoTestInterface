# --coding=utf8--
import requests


class InterfaceInfo:

    def __init__(self, interface_method, interface_url):
        self.interface_method = interface_method
        self.interface_url = interface_url
        self.headers = {'content-type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    # 根据excel中判断post/get
    def interface_test(self):
        req = ''
        if self.interface_method == 'post':
            req = requests.post(self.interface_url, self.headers)
        elif self.interface_method == 'get':
            req = requests.get(self.interface_url, self.headers)
        return req.json()





