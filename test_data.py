#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/27 13:59
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_data.py
@Software : PyCharm
"""
from common.http_request import HttpRequest
import json
import jsonpath
import time

# data = {"status": 1, "code": "10001", "data": [
#     {"id": 1, "investId": "1", "createTime": "2018-04-27 12:24:01", "terms": "1", "unfinishedInterest": "1.0",
#      "unfinishedPrincipal": "0", "repaymentDate": "2018-05-27 12:24:01", "actualRepaymentDate": None, "status": "0"},
#     {"id": 2, "investId": "1", "createTime": "2018-04-27 12:24:01", "terms": "2", "unfinishedInterest": "1.0",
#      "unfinishedPrincipal": "0", "repaymentDate": "2018-06-27 12:24:01", "actualRepaymentDate": None, "status": "0"},
#     {"id": 3, "investId": "1", "createTime": "2018-04-27 12:24:01", "terms": "3", "unfinishedInterest": "1.0",
#      "unfinishedPrincipal": "100.00", "repaymentDate": "2018-07-27 12:24:01",
#      "actualRepaymentDate": None, "status": "0"}], "msg": "获取信息成功"}

# params = {"openId": "oSrIn52wjxC8t3GKweSXjJp8DMVY"}
# url = r"https://jdwx.alavening.com/alading-interface/webook/grade.ajax"
# method = "get"
# resp = HttpRequest2().http_request(method=method, url=url, data=params)
# print(resp.text)
# print(time.localtime(time.time()))
data = {'openId': 'oSrIn55nLMabEySTSHD98cSxwxQ0', 'nickname': 'Mr. Zero'}
# data = {'bookType': 'langwenLWTE', 'openId': 'oSrIn55nLMabEySTSHD98cSxwxQ0', 'nickname': 'Mr. Zero'}
url = 'https://jdwx.alavening.com/alading-interface/webook/bookList.ajax'
request = HttpRequest()
resp = request.http_request('get', url, data)
print(resp.text)
print(type(resp.text))
# d = json.loads(resp.text)
# print(d)
# print(type(d))
# results = jsonpath.jsonpath(json.loads(resp.text), "$..bookName")
# if '朗文LWTE 1A' in results:
#     print('good')
# print(results)
# result1 = jsonpath.jsonpath(json.loads(resp.text), "$.data.*")
result2 = jsonpath.jsonpath(json.loads(resp.text), "$.data..bookName")
print(result2)
a = 3
print(~a)
