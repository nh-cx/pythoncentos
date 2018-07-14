#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import paramiko
import re

def ssh_client_sigin(ipadd, port=22, username='', passwd='', command=''):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ipadd, port=port, username=username, password=passwd, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(command)
        x = stdout.read().decode('gbk')
        return x
    except Exception as e:
        if re.match('.*Name or service not known', str(e)):
            print('用户名或者服务器ip地址填写错误。')
        elif re.match('.*Unable to connect to port', str(e)):
            print('输入的IP地址错误。')
        elif re.match('.*timed out', str(e)):
            print('超时，请检查输入的IP地址是否正确。')
        elif re.match('.*Authentication failed', str(e)):
            print('验证失败，用户名、密码错误。')
        else:
            print('{0}:{1}'.format('出错啦，请联系管理员，错误信息如下：', e))


if __name__ == '__main__':
    print('请输入IP地址、用户名、密码及命令，输入quit退出程序。')
    ipadd = input('请输入ip地址：')
    username = input('请输入用户名：')
    passwd = input('请输入密码：')
    while True:
        if ssh_client_sigin(ipadd=ipadd, username=username, passwd=passwd, command='/ip addr print'):
            print()
            command = input('command:')
            if command == 'quit':
                break
            result1 = ssh_client_sigin(ipadd=ipadd, username=username, passwd=passwd, command=command)
            print(result1)
        else:
            ipadd = input('请输入ip地址：')
            username = input('请输入用户名：')
            passwd = input('请输入密码：')
