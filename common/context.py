#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/7/12 16:19
@Author   : Damon
@Email    : kangming40@163.com
@File     : context.py
@Software : PyCharm
"""
import re
import configparser
from common import time_operate
from common.config import config


class Context:
    homeworkId = None  # 创建的homeworkID
    planId = None  # 未完成作业列表接口 产生的planID
    textbookId = None  # 未完成作业列表接口 产生的textbookID
    title = '接口自动化测试' + time_operate.create_time  # 创建作业时的标题
    endTime = time_operate.datetime_operate(5)[0:4] + '-' + time_operate.datetime_operate(5)[
                                                            4:6] + '-' + time_operate.datetime_operate(5)[
                                                                         6:8] + ' 23:59:59'  # 创建作业时，要求完成的最后时间


def replace(data):
    p = "#(.*?)#"  # 正则表达式
    while re.search(p, data):
        print(f'请求数据：{data}')
        m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
        g = m.group(1)  # 拿到参数化的KEY
        try:
            v = config.get('data', g)  # 根据KEY取配置文件里面的值
        except configparser.NoOptionError as e:  # 如果配置文件里面没有的时候，去Context里面取
            if hasattr(Context, g):
                v = getattr(Context, g)
            else:
                print('找不到参数化的值')
                raise e
        print(f'V 的值:{v}')
        # 替换后的内容，继续用data接受
        data = re.sub(p, v, data, count=1)  # 查找替换，count查找替换的次数
    return data
