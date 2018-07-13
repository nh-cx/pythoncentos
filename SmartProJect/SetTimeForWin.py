#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
# ======程序说明======
# 时间校准，GetAdjustTime函数返回时间格式
# os.system()执行时间校准操作
# ==================
import time
import ntplib


def GetAdjustTime():
    ntp = ntplib.NTPClient()
    response = ntp.request('time.windows.com')
    ts = response.tx_time
    _date = time.strftime('%Y-%m-%d', time.localtime(ts))
    _time = time.strftime('%X', time.localtime(ts))
    return 'date {} && time {}'.format(_date, _time)


if __name__ == "__main__":
    import os
    os.system(GetAdjustTime())
