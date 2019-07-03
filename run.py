#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:likangming
# Created time:2019/4/17 14:21
# Filename:run.py
import unittest
from common import HTMLTestRunnerNew
from common import contants
import time

discover = unittest.defaultTestLoader.discover(contants.case_dir, 'test_*.py')
data = time.strftime('%Y%m%d', time.localtime(time.time()))
name = 'Alavening微信公众号接口测试' + data
with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title=name, description='WeChat API Test',
                                              tester='Kevin')
    runner.run(discover)
