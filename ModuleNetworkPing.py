#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from scapy.all import *


def icmp_packet(host):
    """
    parameter like '192.168.1.1'
    return strType
    """
    ping_pkt = IP(dst=host) / ICMP() / Raw(RandString(size=32))
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 'have reply'
    else:
        return 'not reply!'


if __name__ == '__main__':
    result1 = icmp_packet('192.168.1.251')
    print('ping 192.168.1.251:\n' + result1)
    print()
    result2 = icmp_packet('192.168.1.242')
    print('ping 192.168.1.242:\n' + result2)
