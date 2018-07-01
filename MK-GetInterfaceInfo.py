#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import paramiko,re
# 创建SSH对象
ssh =paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
# 第一次登陆的认证信息
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print('登录信息：SSH_INFO: IPADD=192.168.1.228 PORT=22 USER=py')

# # 输入密码
# ssh_pwd = input("请输入密码：")

# 连接服务器
ssh.connect(hostname='192.168.1.228', port=22, username='py', password='~123456')


# 执行命令
stdin, stdout, stderr = ssh.exec_command('/ip address print')

# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
str_deocde = result.decode()

str_decode_print = '\n'*2 + '返回/ip address列表\n' + '-'*60 + '\n' + str_deocde + '-'*60 + '\n'*3

print(str_decode_print)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('/interface print')

res, err = stdout.read(), stderr.read()
result = res if res else err
str_deocde2 = result.decode('gbk')

str_decode_print2 = '\n'*2 + '返回/ip address列表\n' + '-'*60 + '\n' + str_deocde2 + '-'*60 + '\n'*3

print(str_decode_print2)

# # 使用字符串的切割，并去掉0，1和-1的数据
# lines = str(str_deocde).split('\n')[2:-2]

lines = re.findall('(\d.*\w).*', str_deocde)


str_print = '格式化后的列表：\n{0}\n{1:^10}{2:20}{3:20}{4:^10}{5:20}\n'.format('-'*80, 'NUM', 'INTERFACE', 'IP ADDRESS', 'MASK', 'NETWORK')

for x in lines:
    str_split = str(x).split()

    str_print = str_print + '{0:^10}{1:20}{2:20}{3:^10}{4:20}\n'.format(str_split[0], str_split[3], str_split[1][:-3], str_split[1][-2:], str_split[2])

str_print = str_print + '-'*80


print(str_print)

# 关闭连接
ssh.close()