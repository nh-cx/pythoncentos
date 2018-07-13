#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
# ======程序说明======
# 使用多线程对IP地址段进行扫描
# 并把扫描的结果保存到本地磁盘中
# ==================
import ipaddress
import re
from GetHostIP import get_host_ip


def get_ip_address():
    ip = get_host_ip()
    sub = re.match('.*\..*\..*\.', ip).group() + r'0/24'
    return ipaddress.ip_network(sub)


if __name__ == "__main__":
    from ModuleNetworkPing import icmp_packet
    from multiprocessing.pool import ThreadPool
    # from multiprocessing import freeze_support

    # 多线程
    # freeze_support()
    # Windows平台要加上这句，避免RuntimeError

    pool = ThreadPool()

    net = get_ip_address()

    results = []

    for i in range(0, 150):
        if net:
            break
        result = pool.apply_async(icmp_packet, args=(net.pop()))
        if result == 'have reply':
            results.append(result)

    print(results)
