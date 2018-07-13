#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
# ======程序说明======
# 使用多线程对IP地址段进行扫描
# 并把扫描的结果保存到本地磁盘中
# ==================
import ipaddress
import GetHostIP


net = ipaddress.ip_network('')

# if __name__ == "__main__":