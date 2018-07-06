#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import ModuleNetworkPing
import ModuleNetworkSsh
import DemoNetworkDataIpDns


if __name__ == '__main__':
    for i in DemoNetworkDataIpDns.IP_ADDRESS_Demo_List:
        PingResult = ModuleNetworkPing.icmp_packet(i)
        print('IP:'+i+'  '+PingResult)
        if 'have reply' == PingResult:
            result = ModuleNetworkSsh.ssh_client_sigin(i, user_name='py', pass_wd='~123456', ins_command='/ip add print')
            if result is None:
                print("无法SSH Host:"+i)
            else:
                print(result)
        print()
