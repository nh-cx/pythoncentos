#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import os
import re

# 创建文件部分
# =======================================
# os.mkdir('test')
# os.chdir('test')
# qytang1 = open('qytang1', 'w')
# qytang1.write('test file\n')
# qytang1.write('this is qytang\n')
# qytang1.close()
#
# qytang2 = open('qytang2', 'w')
# qytang2.write('test file\n')
# qytang2.write('qytang python\n')
# qytang2.close()
#
# qytang3 = open('qytang3', 'w')
# qytang3.write('test file\n')
# qytang3.write('this is python\n')
# qytang3.close()
#
# os.mkdir('qytang4')
# os.mkdir('qytang5')
# =======================================

# 获取文件列表
os.chdir('test')
filelist = os.listdir(os.getcwd())

# 遍历filelist，判断是否文件，如果是就读取里面的文件，并判断是否有需要查找的文字
FindStr = 'qytang'
PrintStr = '文件中包含"qytang"关键字的文件为：\n'
for i in filelist:
    if os.path.isfile(i):
        FindTheStr = False
        for line in open(i):
            if re.match('.*qytang.*', line):
                FindTheStr = True
        if FindTheStr:
            PrintStr = PrintStr + i + '\n'

print(PrintStr)
