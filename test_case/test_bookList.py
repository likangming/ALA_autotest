#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/24 16:35
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_bookList.py
@Software : PyCharm
"""
import unittest
from ddt import ddt, data
from ALA_WeChat_1.common import contants
from ALA_WeChat_1.common import do_excel
from ALA_WeChat_1.common import logger
from ALA_WeChat_1.common.http_request import HttpRequest2
import json
import jsonpath

logger = logger.get_logger(__name__)


@ddt
class BooklistTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'bookList')  # 测试bookList接口，读取excel里Sheet"bookList"
    cases = excel.get_case()  # 获取excel数据

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_allbooklist(self, case):
        logger.info('开始测试：{0}'.format(case.title))
        resp = self.http_request.http_request(case.method, case.url, case.data)  # 请求数据，传入excel里的method，url,data参数
        # print(resp.text)
        # print('type(resp.text):', type(resp.text))
        # print('type(case.expexted:', type(case.expected))
        results = jsonpath.jsonpath(json.loads(resp.text), "$..bookName")  # 运用了jsonpath去获取包含bookName的值（列表）
        try:
            self.assertIn(case.expected, results)  # 断言：是否在返回值里
            self.excel.writer_result(case.case_id + 1, resp.text, "PASS")  # 写入测试结果及”PASS“
        except AssertionError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, "FAIL")
            logger.error("报错了，{0}".format(e))
            raise e
        logger.info('结束测试：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
