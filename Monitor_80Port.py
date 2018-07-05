#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import os
import re
import time

monitorPort = '80'

Found = False

while True:
    GetStr = os.popen('netstat -tulnp').read()
    StrINFO = re.split('\n', GetStr)[2:-1]

    Found = False
    for x in StrINFO:
        x = str(x).split()[3]
        x = re.match('.*:(\d+)$', x).groups()[0]
        if str(x) == monitorPort:
            Found = True
            print('(TCP/80)服务已经被打开')
    if not Found:
        print('等待五秒重新开始监控！')
    time.sleep(5)
