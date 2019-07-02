#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/6/11 11:11
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_create.py
@Software : PyCharm
"""
import unittest
from ddt import ddt, data
from ALA_WeChat_1.common import contants
from ALA_WeChat_1.common import do_excel
from ALA_WeChat_1.common import logger
from ALA_WeChat_1.common.http_request import HttpRequest2
import json
from ALA_WeChat_1.common.do_mysql import mysql
# import jsonpath
# import ast

logger = logger.get_logger(__name__)


@ddt
class CreateTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'create')  # 测试create接口
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_create(self, case):
        logger.info('开始测试{}'.format(case.title))
        resp = self.http_request.http_request(case.method, case.url, case.data)
        # print('resp', resp)
        results = json.loads(resp.text)
        # print('results:', results)
        # print('type(results):', type(results))
        # print('case.expected:', case.expected)
        # print('type(case.expected):', type(case.expected))
        try:
            self.assertTrue(results["data"]["homeworkId"])
            sql_data = mysql.fetch_one(case.check_sql)
            # print("type(sql_data):", type(sql_data))
            # self.assertEqual(ast.literal_eval(case.expected), results["success"])
            # 断言，结果只有一个"data"跟"success"，data里的homeworkID是动态的，所以获取success里的value来做断言比较好
            # self.assertEqual(ast.literal_eval(case.expected), results["success"])  # 个人偏向用ast.literal_eval来替代eval
            self.excel.writer_result(case.case_id + 1, resp.text, 'PASS', str(sql_data))
            # if results["data"]["homeworkId"]:
            #     sql_data = mysql.fetch_one(case.check_sql)
            #     self.excel.writer_result(case.case_id + 1, sql_data, )
        except AssertionError as e:
            logger.error('报错了：', e)
            self.excel.writer_result(case.case_id + 1, resp.text, 'FAIL')
            raise e
        logger.info('测试结束：{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
