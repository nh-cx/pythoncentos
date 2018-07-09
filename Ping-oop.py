#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from scapy.all import *
import time

class oop_ping:
    def __init__(self, ip, length=32):
        self.ip = ip
        self.length = length

    def src(self,srcip):
        self.ip = srcip

    def size(self,length):
        self.length = length

    def one(self):
        ping_pkt = IP(dst=self.ip) / ICMP() / Raw(RandString(size=self.length))
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result:
            print('have reply')
        else:
            print('not reply!')

    def ping(self):
        ping_pkt = IP(dst=self.ip) / ICMP() / Raw(RandString(size=self.length))
        for i in range(1,5):
            ping_result = sr1(ping_pkt, timeout=2, verbose=False)
            if ping_result:
                print('have reply')
            else:
                print('not reply!')
            time.sleep(0.5)



if __name__ == "__main__":
    router = oop_ping('192.168.1.251')
    print('原IP地址一次包')
    router.one()
    print('原IP地址5次包')
    router.ping()
    print('修改包为20长度,并发送5次包')
    router.size(20)
    router.ping()
    print('修改源IP地址为192.168.1.229')
    router.src('192.168.1.229')
    router.one()