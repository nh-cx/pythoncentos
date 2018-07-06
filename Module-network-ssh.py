#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import paramiko


def ssh_client_sigin(ip_add, port=22, user_name='', pass_wd='', ins_command=''):
    """
    ssh client with command
    :param ip_add:
    :param port:
    :param user_name:
    :param pass_wd:
    :param ins_command:
    :return: command result
    """
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip_add, port=port, username=user_name, password=pass_wd, timeout=5, compress=True)
        stdin, stdout, stderr = ssh.exec_command(ins_command)
        x = stdout.read().decode('gbk')
        return x
    except Exception as e:
        print('{0} Error {1}'.format(ip_add, e))


if __name__ == '__main__':
    ipadd = input('请输入ip地址：')
    username = input('请输入用户名：')
    passwd = input('请输入密码：')
    while True:
        print()
        command = input('command:')
        result1 = ssh_client_sigin(ip_add=ipadd, user_name=username, pass_wd=passwd, ins_command=command)
        print(result1)
