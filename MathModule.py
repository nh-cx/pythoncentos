#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import time
import os
import threading


def math_multi(x,y,z):
    # 打印进程和线程ID
    # print('pid tid==>',os.getpid(),threading.currentThread().ident)
    i = 1
    while i < 10:
        sum = x*y*z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)

    return sum, os.getpid(), threading.currentThread().ident

# if __name__ == "__main__":
