#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/23 10:45
@Author   : Damon
@Email    : kangming40@163.com
@File     : test009replace.py
@Software : PyCharm
"""
a = r"{123: false}"
print(a)
b = a.replace('true', 'True')
print(b)
