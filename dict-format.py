#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import re
SourceString = r'''TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'''

StringAll = re.findall('TCP\s+Student\s+(.*):(\d*)\s+Teacher\s+(.*):(\d*),\s+idle\s+.*,\s+bytes\s+(\d*),\s+flags\s+(.*)\n?', SourceString)

print('打印字典\n')
print(StringAll)

StringPrint = '\n\n\n\n格式化打印输出\n\n'

for i in StringAll:
    StringPrint = StringPrint+'{0:>10}:{1:20}|{2:>10}:{3:15}|{4:>10}:{5:20}{6:>10}:{7:15}|\n{8:>10}:{9:20}|{10:>10}:{11:15}\n'.format('src', i[0], 'src_p', i[1], 'dst', i[2]+'|', 'dst_p', i[3], 'bytes', i[4], 'flags', i[5])+ '='*120+ '\n'

print(StringPrint)
