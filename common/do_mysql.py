#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/10 17:04
@Author   : Damon
@Email    : kangming40@163.com
@File     : do_mysql.py
@Software : PyCharm
"""
import pymysql
from common.config import conf


class DoMysql:
    """
    完成对MySQL数据库的数据操作
    """

    def __init__(self):
        host = conf.get('jdcs_database', 'host')
        user = conf.get('jdcs_database', 'user')
        password = conf.get('jdcs_database', 'password')
        port = int(conf.get('jdcs_database', 'port'))
        # 创建连接
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=port, charset='utf8')
        # 设置返回字典
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)  # 创建游标

    def fetch_one(self, sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()  # 返回一条数据（以元组形式）

    def fetch_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # 返回多条数据：元组里面嵌套元组

    def close(self):
        self.cursor.close()  # 关闭游标
        self.mysql.close()  # 关闭连接


mysql = DoMysql()
# if __name__ == '__main__':
#     mysql = DoMysql()
#     # result1 = mysql.fetch_all("select * from alading_test.al_en_plan where mac = 'F0:85:C1:D6:74:AF' ORDER BY plan_time DESC")
#     # result1 = mysql.fetch_one("SELECT * FROM alading_jdcs.al_en_homework ORDER BY update_time DESC")
#     result1 = mysql.fetch_one(
#         "SELECT plan_id FROM alading_jdcs.al_en_plan WHERE homework_id = 'e5deaf1b727d4a8598798e2d3d5e144c';")
#     print('result:', result1)
#     print('type(result1):', type(result1))
#     # planId = self.mysql.fetch_one(sql)[0]
#     # print('planId:', planId)
#     # planId = result1[0]
#     # print('planId:', planId)
#     # print('type(planId):', type(planId))
#     mysql.close()
