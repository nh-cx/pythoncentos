#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import datetime

GetDatetime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
FiveDayBefore = datetime.datetime.now() - datetime.timedelta(days=5)
FileName = 'save_fivedayago_time_' + str(GetDatetime)

myfile = open(FileName, 'w')
myfile.write(str(FiveDayBefore))
myfile.close()

