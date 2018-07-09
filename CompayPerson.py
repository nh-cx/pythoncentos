#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
class Person:
    def __init__(self, name, age, pay = 0, job = None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay *= (1.0 + percent)

    def __str__(self):
        return  '{0}:{1}\n{2}:{3}\n{4}:{5}\n{6}:{7}\n'.format('class', self.__class__.__name__, 'name', self.name, 'pay', self.pay, 'job', self.job)


if __name__ == "__main__":
    Tom = Person('Tom Smith', 19, 3500, 'Assistant')
    print(Tom.lastName())
    print(Tom.job)
    print('')
    print(Tom)
