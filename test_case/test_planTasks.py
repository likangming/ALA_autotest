#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/7/15 11:04
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_planTasks.py
@Software : PyCharm
"""
import ast
import json
import unittest
from ddt import ddt, data
from common.logger import logger
from common import do_excel
from common import contants
from common.context import Context
from common.http_request import HttpRequest2


@ddt
class PlanTasksTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'planTasks')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_plan_tasks(self, case):
        logger.info('开始测试{}'.format(case.title))
        resp = self.http_request.http_request(case.method, case.url, case.data)
        results = json.loads(resp.text)
        print('返回结果：', results)
        try:
            self.assertEqual(ast.literal_eval(case.expected), results["success"])
            self.excel.writer_result(case.case_id + 1, resp.text, "PASS")

            # 判断有查询到作业时，取到planID 和 textbookID
            planId = results["data"]["list"][0]['planId']
            logger.info("planID:{}".format(planId))
            print("planID:", planId)
            textbookId = results["data"]["list"][0]['textbookId']
            logger.info("textbookId:{}".format(textbookId))
            print("textbookId:", textbookId)
            setattr(Context, 'planId', str(planId))
            setattr(Context, 'textbookId', str(textbookId))
        except ValueError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, "FAIL")
            logger.error('报错了{}'.format(e))
            raise e
        logger.info('测试结束：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
