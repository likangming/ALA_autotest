#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/21 14:30
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_version.py
@Software : PyCharm
"""
import unittest
from ddt import ddt, data
from common import do_excel
from common import contants
from common.http_request import HttpRequest2
from common.logger import logger
import jsonpath
import json


@ddt
class BooksTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'settle')  # settle接口
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_requets = HttpRequest2()  # 请求类

    @data(*cases)
    def test_books(self, case):
        logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_requets.http_request(case.method, case.url, case.data)
        results = jsonpath.jsonpath(resp.text)
        try:
            self.assertIn(case.expected, results)
            self.excel.writer_result(case.case_id + 1, resp.text, 'PASS')
        except AssertionError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, 'FAIL')
            logger.error("报错了，{0}".format(e))
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_requets.close()
