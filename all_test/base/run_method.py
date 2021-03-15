# coding:utf-8
import requests


class RunMethod:
    def getCookies(self, url, data, header=None):
        session = requests.Session()
        session.post(url, data, headers=header, verify=False)
        return session.cookies.get_dict()

    def post_main(self, url, data, header=None, cookies=None):
        res = None
        if header is not None:
            res = requests.post(url=url, data=data, headers=header, cookies=cookies, verify=False)
        else:
            res = requests.post(url=url, data=data, cookies=cookies, verify=False)
        return res

    def get_main(self, url, data, header, cookies=None):
        res = None
        if header is not None:

            res = requests.get(url=url, data=data, headers=header, cookies=cookies, verify=False)
        else:
            res = requests.get(url=url, data=data, cookies=cookies, verify=False)

        return res

    def run_main(self, method, url, data, header, cookies=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header, cookies)
        elif method == 'get':
            res = self.get_main(url, data, header, cookies)
        return res
