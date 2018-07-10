#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from ModuleNetworkSsh import ssh_client_sigin

def SshLoginIncludeHelp(ipadd, username, passwd, command):
    result1 = ssh_client_sigin(ip_add=ipadd, user_name=username, pass_wd=passwd, ins_command=command)
    return result1

if __name__ == "__main__":
    from optparse import OptionParser
    usage = "通过使用命令行，登录SSH服务器，并执行输入的命令。\n使用办法：python3 ./SshIncludeHelp.py -i IPADDR -u USERNAME -p PASSWORD -c COMMAND\n长参数：python3 ./SshIncludeHelp.py --ipaddr IPADDR --username USERNAME --password PASSWORD --command COMMAND"
    version = "version 1.1"
    parser = OptionParser(usage=usage, version=version)

    parser.add_option("-i", "--ipaddr", dest="ip", help="你要连接的目标ip地址。", default='192.168.1.1', type="string")
    parser.add_option("-u", "--username", dest="user", help="输入你的用户名。", default='root', type="string")
    parser.add_option("-p", "--password", dest="pwd", help="输入你的密码", default='', type="string")
    parser.add_option("-c", "--command", dest="cmd", help="输入你的命令，系统会返回该命令的执行信息。如有空格，请使用''把命令行括起来。此项不填，默认执行ls", default='ls', type="string")

    (options, args) = parser.parse_args()

    returnStr = SshLoginIncludeHelp(options.ip, options.user, options.pwd, options.cmd)

    print(returnStr)