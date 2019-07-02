#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/6/17 17:46
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_chapterModule.py
@Software : PyCharm
"""
import unittest
from ddt import ddt, data
from ALA_WeChat_1.common.logger import logger
from ALA_WeChat_1.common import do_excel
from ALA_WeChat_1.common import contants
from ALA_WeChat_1.common.http_request import HttpRequest2
import json


@ddt
class ChapterModuleTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'chapterModule')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_chapter_module(self, case):
        logger.info("开始测试{}".format(case.title))
        resp = self.http_request.http_request(case.method, case.url, case.data)
        results = json.loads(resp.text)
        try:
            self.assertEqual(eval(case.expected), results)
            self.excel.writer_result(case.case_id + 1, resp.text, 'PASS')
        except ValueError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, 'FAIL')
            logger.error("报错了，{0}".format(e))
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
