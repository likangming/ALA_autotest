#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/20 16:16
@Author   : Damon
@Email    : kangming40@163.com
@File     : logger.py
@Software : PyCharm
"""
import logging
from common import contants


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')
    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"  # 输出格式
    formatter = logging.Formatter(fmt=fmt)
    console_handler = logging.StreamHandler()  # 控制台
    # 把日志级别放到配置文件里面配置：优化
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(contants.log_dir + '/alawechat_cases.log')  # 将日志写入到自己指定的文件
    # 把日志级别放到配置文件里面配置
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


# 验证：debug模式不显示，其他的显示
logger = get_logger('case')
# logger.info('测试开始')
# logger.error('测试报错')
# logger.debug('测试数据')
# logger.info('测试结束')
