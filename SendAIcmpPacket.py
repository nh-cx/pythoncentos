#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from scapy.all import *

def icmp_packet(host):
    ping_pkt = IP(dst=host)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return 'have reply'
    else:
        return 'not reply!'

if __name__=='__main__':
    result1 = icmp_packet('192.168.8.251')
    print('ping 192.168.8.251:\n'+result1)
    print()
    result2 = icmp_packet('192.168.8.242')
    print('ping 192.168.8.242:\n'+result2)