#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
List1 = ['aaa', 111, (4, 5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4, 5)]

for i in List1:
    if i in List2:
        print('{0:>10} {1}'.format(str(i), 'in List1 and List2'))
    else:
        print('{0:>10} {1}'.format(str(i), 'in List1'))

for x in List2:
    if x not in List1:
        print('{0:>10} {1}'.format(str(x), 'in List2'))



