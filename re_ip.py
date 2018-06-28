#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用

import re

cmd_str = 'Port-channel1.189	192.168.189.254	YES	CONFIG	up'

string_unformated = re.match('(.*)\s+(.*)\s+(.*)\s+(.*)\s+(.*)', cmd_str).groups()

str_prt1 = string_unformated[0]

str_prt2 = string_unformated[1]

str_prt3 = string_unformated[4]

# str_old_formated = '%s\n%-10s : %-70s\n%-10s : %-70s\n%-10s : %-70s\n%s' % ('-'*80, r'接口', str_prt1, r'IP地址', str_prt2, r'状态', str_prt3, '-'*80)
#
# print(str_old_formated)

str_new_formated = '{0}\n{1:10} : {2:60}\n{3:10} : {4:70}\n{5:10} : {6:70}\n{7}'.format('-'*80, '接口', str_prt1, 'IP地址', str_prt2, '状态', str_prt3, '-'*80)

print(str_new_formated)
