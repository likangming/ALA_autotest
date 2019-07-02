#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/6/17 16:28
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_chapterList.py
@Software : PyCharm
"""
# from ALA_WeChat_1.common.do_mysql import mysql
from common import contants
from common.http_request import HttpRequest2
# from ALA_WeChat_1.common.config import conf
from common import logger
from common import do_excel
import unittest
from ddt import ddt, data
import json
import ast

logger = logger.get_logger(__name__)


@ddt
class ChapterListTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'chapterList')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置")
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_chapter_list(self, case):
        logger.info('开始测试{}'.format(case.title))
        resp = self.http_request.http_request(case.method, case.url, case.data)
        # print('case.data:', case.data)
        # print('resp:', resp)
        # print('type(resp):', type(resp))
        results = json.loads(resp.text)
        # print(results["success"])
        try:
            self.assertEqual(ast.literal_eval(case.expected), results["success"])
            self.assertTrue(results["data"][0]["nodule"])
            self.excel.writer_result(case.case_id + 1, resp.text, "PASS")
        except AssertionError as e:
            logger.error('报错了{}'.format(e))
            self.excel.writer_result(case.case_id + 1, resp.text, "FAIL")
            raise e
        logger.info('测试结束'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
