#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import paramiko

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
        print('{0} Error {1}'.format(ipadd, e))


if __name__=='__main__':
    ipadd = input('请输入ip地址：')
    username = input('请输入用户名：')
    passwd = input('请输入密码：')
    while True:
        print()
        command = input('command:')
        result1 = ssh_client_sigin(ipadd=ipadd, username=username, passwd=passwd, command=command)
        print(result1)
