#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import os
import re

GetString = os.popen('route -n').read()

print('返回的数据：\n' + GetString + '\n\n')

Info = str(GetString).split('\n')[2:-1]

# 1
for line in Info:
    if re.findall('UG', line):
        str_print = re.match('^.*\.\d\s+(\d+\.\d+\.\d+\.\d+)\s.*', line).groups()
        print('方法一:\n默认网关为：\n' + str_print[0] + '\n\n')


# 2
for line in Info:
    if re.findall('UG', line):
        str_print = line.split()[1]
        print('方法二:\n默认网关为：\n' + str_print)

