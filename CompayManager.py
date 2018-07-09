#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from CompayPerson import Person
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self,percent + bonus)



if __name__ == "__main__":
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones',45, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 50000)
    print(sue,sue.pay,sue.lastName())

    for obj in (bob,sue,tom):
        obj.giveRaise(0.1)
        print(obj)