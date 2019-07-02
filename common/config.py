#!/usr/bin/env python
# _*_coding:utf-8_*_
"""
@Time     : 2019/5/10 13:59
@Author   : likangming
@Email    : kangming40@163.com
@File     : config.py
@Software : PyCharm
"""
import configparser
from ALA_WeChat_1.common import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()  # 初始化类
        self.config.read(contants.global_file)  # 先加载global
        switch = self.config.getboolean('switch', 'on')  # 通过判断switch的值，来确定使用哪个环境的配置
        if switch:      # 开关打开的时候，使用test的配置
            self.config.read(contants.test_file, encoding='utf-8')
        else:       # 开关 关闭的时候，使用issue的配置
            self.config.read(contants.issue_file, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)


class ReadBaseConfig:
    """
    完成读取任一配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.config_file)

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()       # 1.实例化供调用
conf = ReadBaseConfig()     # 读取配置文件实例化
# if __name__ == '__main__':        # 2.练习的时候
#     config = ReadConfig()
#     print(config.get('api', 'pre_url'))
