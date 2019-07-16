#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/7/16 11:24
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
    excel = do_excel.DoExcel(contants.case_file, 'playPlan')  # 测试add接口
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
        print("case.data:", case.data)
        resp = self.http_request.http_request(case.method, case.url, case.data)
        results = json.loads(resp.text)
        print('返回结果：', results)
        try:
            self.assertEqual(ast.literal_eval(case.expected), results["success"])
            self.excel.writer_result(case.case_id + 1, resp.text, "PASS")

            # 判断添加作业成功后，查询数据库，取到homeworkId/也可以在返回结果中取到homeworkId
            try:
                if resp.json()["data"]["homeworkId"]:
                    homeworkId = results["data"]["homeworkId"]
                    print('homeworkId:', homeworkId)
                    # 保存到类属性里面
                    setattr(Context, "homeworkId", homeworkId)
            except KeyError as e:
                pass
            # 判断添加到我的作业簿后，查询到planID并将planId保存到类属性中
            try:
                if resp.json()["message"]:
                    logger.info('查询数据库中的planId')
                    homeworkid = getattr(Context, "homeworkId")
                    print('homeworkId:', homeworkid)
                    sql = f"SELECT plan_id FROM alading_jdcs.al_en_plan WHERE homework_id = '{homeworkid}';"
                    planId = self.mysql.fetch_one(sql)['plan_id']   # 我设置的MySQL查询是以字典形式查询的，返回结果为字典
                    print('planId:', planId)
                    # 保存到类属性中去
                    setattr(Context, "planId", planId)
            except KeyError as e:
                pass
        except ValueError as e:
            self.excel.writer_result(case.case_id + 1, resp.text, "FAIL")
            logger.error('报错了{}'.format(e))
            raise e
        logger.info('测试结束：{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
