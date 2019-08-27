#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/22 11:44
@Author   : Damon
@Email    : kangming40@163.com
@File     : test_playPlan.py
@Software : PyCharm
"""
import ast
import json
import time
import unittest
from ddt import ddt, data
from common.logger import logger
from common import do_excel
from common import contants
from common import context
from common import do_mysql
from common.http_request import HttpRequest2
from common.context import Context


@ddt
class PlanTasksTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'shop_add')  # 测试shop_add接口
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)
    def test_plan_tasks(self, case):
        logger.info('开始测试{}'.format(case.title))
        case.data = context.replace(case.data)
        resp = self.http_request.http_request(case.method, case.url, case.data)
        results = json.loads(resp.text)
        try:
            sql = f"SELECT plan_id FROM alading_jdcs.al_en_plan WHERE goodsId = '{goodsId}';"
            saleprice = self.mysql.fetch_one(sql)['salePrice']  # 查询所属商品的售价
            self.assertEqual(results["data"]["shelves"]["salePrice"], saleprice)
        except ValueError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, "FAIL")
            logger.error('报错了{}'.format(e))
            raise e
        logger.info('测试结束：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
