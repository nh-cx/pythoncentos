#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import os
import re
import time

monitorPort = '80'

GetStr = os.popen('netstat -tulnp').read()

print(GetStr)

StrINFO = re.split('\n', GetStr)[2:-1]

while True:
    for x in StrINFO:
        x = str(x).split()[3]
        x = re.match('.*:(\d+)$', x).groups()[0]
        if x == monitorPort:
            print('(TCP/80)服务已经被打开')
            continue
    print('等待一秒重新开始监控！')
    time.sleep(5)
