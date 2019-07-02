#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/21 17:30
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_version.py
@Software : PyCharm
"""
import unittest
from ddt import ddt, data
from ALA_WeChat_1.common import do_excel
from ALA_WeChat_1.common import contants
from ALA_WeChat_1.common.http_request import HttpRequest2
from ALA_WeChat_1.common.logger import logger
import jsonpath
import json


@ddt
class BooksTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'version')  # version接口
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_requets = HttpRequest2()  # 请求类

    @data(*cases)
    def test_books(self, case):
        logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_requets.http_request(case.method, case.url, case.data)
        # result = resp.text.replace('true', 'True')
        # result = eval(result.replace('false', 'False'))
        results = jsonpath.jsonpath(json.loads(resp.text), "$..gradeName")  # 运用了jsonpath去获取包含bookName的值（列表）
        # print('case.expected:', case.expected)
        # print(type(case.expected))
        # print('result:', result)
        # print('type(result):', type(result))
        try:
            # self.assertEqual(case.expected, result)
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
