#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
import pickle
dbfile = open('pickle-db.pl', 'rb')
db = pickle.load(dbfile)
for i in db:
    print(i, '=>', db[i])

# if __name__ == "__main__":