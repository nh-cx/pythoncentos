#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import re

str_tager = '166	54a2.74f7.0326	DYNAMIC	Gi1/0/11'

str_unformat = re.match('(.*)\s+(.*)\s+(.*)\s+(.*)', str_tager).groups()

str_vlanid = str_unformat[0]
str_macadd = str_unformat[1]
str_type = str_unformat[2]
str_interface = str_unformat[3]

# str_old_print = '%s\n%-10s : %-70s\n%-10s : %-70s\n%-10s : %-70s\n%-10s : %-70s\n%s' % ('-'*80, r'VLAN ID', str_vlanid, r'MAC ADD', str_macadd, r'Type', str_type, r'Interface', str_interface, '-'*80)
#
# print(str_old_print)

str_new_print = '{0}\n{1:10} : {2:70}\n{3:10} : {4:70}\n{5:10} : {6:70}\n{7:10} : {8:70}\n{9}'.format('-'*80, r'VLAN ID', str_vlanid, r'MAC ADD', str_macadd, r'Type', str_type, r'Interface', str_interface, '-'*80)

print(str_new_print)
