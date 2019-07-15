#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/7/15 15:27
@Author   : Damon
@Email    : kangming40@163.com
@File     : time_operate.py
@Software : PyCharm
"""
import datetime


# 54. 如果当前的日期为 20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。
def datetime_operate(n: int):
    now = datetime.datetime.now()  # 获取当前时间
    # print(now)
    _new_date = now + datetime.timedelta(days=n)  # 获取指定天数后的新日期
    # print(_new_date)
    new_date = _new_date.strftime("%Y%m%d")  # 转换为指定的输出格式
    # print(new_date)
    return new_date
