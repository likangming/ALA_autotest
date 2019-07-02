#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:likangming
# Created time:2019/5/10 14:35
# Filename:contants.py
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前项目的路径
# case_file = os.path.join(base_dir, 'data', 'cases.xlsx')        # 测试用例的路径
case_file = os.path.join(base_dir, 'data', 'alawechat_cases.xlsx')  # 测试用例的路径
global_file = os.path.join(base_dir, 'conf', 'global.conf')  # global配置文件
online_file = os.path.join(base_dir, 'conf', 'online.conf')  # 阿里云环境配置文件
test_file = os.path.join(base_dir, 'conf', 'test.conf')  # 测试环境配置文件
issue_file = os.path.join(base_dir, 'conf', 'issue.conf')  # 预发布环境配置文件
config_file = os.path.join(base_dir, 'conf', 'config.conf')  # 配置文件
log_dir = os.path.join(base_dir, 'log')
case_dir = os.path.join(base_dir, 'test_case')
report_dir = os.path.join(base_dir, 'reports')
# print(report_dir)
