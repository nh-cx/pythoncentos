#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from MathModule import math_multi
from multiprocessing import Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import random

# 多线程
# freeze_support()
# Windows平台要加上这句，避免RuntimeError

# 有效控制并发进程或者线程数，不设置为内核数
# 得到内核数的方法
# cpus = multiprocessing.cpu_count()

# ProcessPool是多进程
pool = ProcessPool(processes=4)

# ThreadPool是多线程
# pool = ThreadPool()

results = []
for i in range(0, 10):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    z = random.randint(1, 10)
    result = pool.apply_async(math_multi, args=(x, y, z))
    results.append(result)

# pool.apply_async采用异步方式调用task
# pool.apply则是采用同步方式调用
# 同步方式意味着下一个task需要等待上一个task完成后才能开始运行
# 这显然不是我们想要的功能，所以采用异步方式连续地提交任务。


pool.close()
pool.join()
# 调用join之前，先调用close函数，否则会出错。
# 执行完close后不会有新的进程加入到pool
# join函数等待所有子进程结束

for i in results:
    print(i.get())

# if __name__ == "__main__":
