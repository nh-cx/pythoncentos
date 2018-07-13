#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
# ======程序说明======
#
#
# ==================
import os
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
    os.system(GetAdjustTime())
