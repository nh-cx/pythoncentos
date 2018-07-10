#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import pickle
def open_pickle_file(pl_file):
    dbfile = open(pl_file, 'rb')
    db = pickle.load(dbfile)
    return db

if __name__ == "__main__":
    mydb = open_pickle_file('pickle-db.pl')
    for i in mydb:
        print(i,'==>',mydb[i])

    print(mydb['tan2']['pay'])
    mydb['tan2']['pay'] = int(mydb['tan2']['pay']*1.6)

    dbfile = open('pickle-db.pl', 'wb')
    pickle.dump(mydb, dbfile)
    dbfile.close()

    mydb = open_pickle_file('pickle-db.pl')
    for i in mydb:
        print(i, '==>', mydb[i])
