#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:likangming
# Created time:2019/4/17 14:37
# Filename:test007.py
import ast
data = '123'
if type(data) == str:
    print(r"It's str")
data = ast.literal_eval(data)
print(type(data))