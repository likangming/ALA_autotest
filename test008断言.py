#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/20 18:55
@Author   : Damon
@Email    : kangming40@163.com
@File     : test008断言.py
@Software : PyCharm
"""
import requests

# import json
# a = {"data": [{"gradeName": "一年级上学期", "grade": "1A"}, ], "success": True}
# b = True
# if b in a.items():
#     print('yes')
# # c = "{"data": [{"gradeName": "一年级"}], "success": true}"
# # b = "{"success": true}"
# # print(json.load(a))
# # print(type(a))
# url = "https://jdwx.alavening.com/alading-interface/webook/grade.ajax"
# params = {"openId": "oSrIn52wjxC8t3GKweSXjJp8DMVY"}
# res = requests.get(url, params=params)
# print('res:', res)
# print('type(res):', type(res))
# print('res.text:', res.text)
# print('type(res.text):', type(res.text))
# res.text.replace('true', 'True')
# print('replace后:', res.text)
# a = res.text.replace('true', 'True')
# print('替换后的res.text:', a)
# print('type(a):', type(a))
# a = eval(a)
# print('type(a):', type(a))
# b = {"success": True}
# c = str(b)
# print('c', c)
# if b in a:
#     print('hhhhh')
# else:
#     print('999999999999')
# b = eval(a)
# print('b:', b)
# print('type(b):', type(b))


# from selenium import webdriver
# import time
# # 打开谷歌浏览器
# driver = webdriver.Chrome()
# # 访问百度首页
# driver.get("http://www.baidu.com")
# time.sleep(1)
# driver.close()

# 判断是否在字典里
data = {"success": True, "data": [
    {
        "bookImg": "https://jdwx.alavening.com/alading_file/enDeclaim/1903181845242hmY/1Ayiban.jpg",
        "bookName": "朗文LWTE 1A",
        "secId": "20190318152702096860",
        "bookDesc": "（LWTE）香港朗文英语教材Longman Welcome To English 一年级上册1A"
    },
    {
        "bookImg": "https://jdwx.alavening.com/alading_file/enDeclaim/190318184620c3Jw/1Byiban.jpg",
        "bookName": "朗文LWTE  1B",
        "secId": "20190318152838228080",
        "bookDesc": "（LWTE）香港朗文英语教材Longman Welcome To English 一年级下册1B"
    }]}
# data2 = "{data: 123, abc: [1, 2, 3, 4, {ccc: 123}]}"
# print("data2:", data2)
# if "ccc: 123" in data2:
#     print("true")
# print(data)
# if data
# for i in data.items():
#     print(i)
# che1 = {"success": True}
# if "朗文LWTE 1A" in data.values():
#     print('right')


# 排序
# numlist = [2, 6, 1, 90, 6, 30, 3, 50]
# numlist.sort()
# print(numlist)


# def list_sort(l):
#     for a in range(1, len(l)):
#         b = a - 1
#         if l[b] < l[a]:
#             t = l[a]
#             l[a] = l[b]
#             b -= 1
#             while b >= 0 and l[b] > t:
#                 l[b + 1] = l[b]
#                 b -= 1
#             l[b + 1] = t
#     return l
#
#
# l = [10, 20, 15, 17, 49, 38, 25, 33]
# print(list_sort(l))
data2 = '{"data":[{"bookImg":"https://jdwx.alavening.com/alading_file/enDeclaim/190318185208fxMH/6Byiban.jpg",' \
        '"bookName":"朗文LWTE  6B","secId":"20190318154322789b82",' \
        '"bookDesc":"（LWTE）香港朗文英语教材Longman Welcome To English 六年级下册6B"},' \
        '{"bookImg":"https://jdwx.alavening.com/alading_file/enDeclaim/190318184508YIPF/6Byiban.jpg",' \
        '"bookName":"朗文PLE  6B","secId":"2019031815544819114c",' \
        '"bookDesc":"朗文Primary Longman Elect 6B (六年级下学期)\\r\\n适用于使用本教材的学生"}],"success":true}'
check1 = 'bookName":"朗文LWTE  6B'
check = 'bookName":"朗文LWTE 6B'
for i in check1:
    print(i, end=' ')
print()
for j in check:
    print(j, end=' ')
print('type(data2):', type(data2))
print('type(check1):', type(check1))
# if check in data2:
#     print('right')
