#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
pap1 = {'name':'KK QIN', 'age':38, 'pay':10001, 'job':'Security'}
tan2 = {'name':'Tin Zhang', 'age':35, 'pay':9980, 'job':'Sale'}
guan3 = {'name':'Wu Jun Zhou', 'age':33, 'pay':8800, 'job':'RS'}

db = {'pan1': pap1, 'tan2': tan2, 'guan3': guan3}

if __name__ == "__main__":
    """
    把上面的数据写入到pickle-db.pl，等待测试。
    """
    import pickle

    dbfile = open('pickle-db.pl', 'wb')
    pickle.dump(db,dbfile)
    dbfile.close()