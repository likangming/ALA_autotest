#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:likangming
# Created time:2019/4/17 14:24
# Filename:http_request.py
import requests
import ast
from ALA_WeChat_1.common.config import config
from ALA_WeChat_1.common import logger

logger = logger.get_logger(__name__)


# from requests.packages import *


class HttpRequest:

    # def __init__(self, method, url, data=None, json=None, cookie=None):
    #     self.url = url
    #     self.method = method
    #     self.data = data
    #     self.json = json
    #     self.cookie = cookie

    @staticmethod
    def http_request(method, url, data=None, json=None, cookie=None):
        if type(data) == str:
            data = ast.literal_eval(data)  # 将str转成字典
        # requests.packages.urllib3.disable_warnings()
        if method.upper() == 'GET':
            try:
                res = requests.get(url, params=data, cookies=cookie)
            except Exception as e:
                print('执行get请求报错，错误为：%s' % e)
                res = 'Error:GET请求报错：{0}'.format(e)
        elif method.upper() == 'POST':
            if json:
                try:
                    res = requests.post(url, json=json, cookies=cookie)
                except Exception as e:
                    print('执行post请求报错，错误为：%s' % e)
                    res = 'Error:POST请求报错：{0}'.format(e)
            else:
                try:
                    res = requests.post(url, data=data, cookies=cookie)
                except Exception as e:
                    print('执行post请求报错，错误为：%s' % e)
                    res = 'Error:POST请求报错：{0}'.format(e)
        else:
            print('你的请求方式不正确！')
            # res = 'Error:请求方法不对报错：%s' % self.method
            res = 'Error:请求方法不对报错：{0}'.format(method)
        return res


class HttpRequest2:

    def __init__(self):
        self.session = requests.sessions.session()  # 打开一个session

    def http_request(self, method, url, data=None, json=None, cookie=None):
        if type(data) == str:
            data = ast.literal_eval(data)  # 将str转成字典

        # 拼接URL
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url:{0}'.format(url))
        logger.debug('请求data:{0}'.format(data))

        if method.upper() == 'GET':
            try:
                res = self.session.request(method=method, url=url, params=data, cookies=cookie)
            except Exception as e:
                res = 'Error:GET请求报错：{0}'.format(e)
        elif method.upper() == 'POST':
            if json:
                try:
                    res = self.session.request(method=method, url=url, json=json, cookies=cookie)
                except Exception as e:
                    res = 'Error:POST请求报错：{0}'.format(e)
            else:
                try:
                    res = self.session.request(method=method, url=url, data=data, cookies=cookie)
                except Exception as e:
                    res = 'Error:POST请求报错：{0}'.format(e)
        else:
            print('你的请求方式不正确！')
            res = 'Error:请求方法不对报错：%s' % method
            # res = 'Error:请求方法不对报错：{0}'.format(method)
        return res

    def close(self):
        self.session.close()  # 关闭session

# if __name__ == '__main__':
#     http2 = HttpRequest2()
#     resp = http2.http_request('postttt',
#                               'http://test.lemonban.com/futureloan/mvc/api/member/register',
#                               data='{"mobilephone": "15810447878", "pwd": "123456"}')
#     print(resp)
#     print(resp.text)
#     print(resp.cookies)
#     print(resp.json())
#     # params = {"mobilephone": "15810447878", "amount": "1000"}
# resp = http2.http_request('post', 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', data=params)
#     # print(resp.text)
#     http2.close()
