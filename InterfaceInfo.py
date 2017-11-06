# --coding=utf8--
import requests
class InterfaceInfo():

    def __init__(self, interfaceMethod, interfaceUrl):
        self.interfaceMethod = interfaceMethod
        self.interfaceUrl = interfaceUrl
        self.headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}


    def interfaceTest(self):
        if self.interfaceMethod == 'post':
            req = requests.post(self.interfaceUrl, self.headers)
        elif self.interfaceMethod == 'get':
            req = requests.get(self.interfaceUrl, self.headers)
        return req.text





