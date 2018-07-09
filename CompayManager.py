#!/usr/bin/python3.6
# -*- coding=utf-8 -*-
# 学习专用
from CompayPerson import Person
class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self,percent + bonus)

    # def __str__(self):
    #     self.job = 'manager'
    #     Person.__str__(self)

if __name__ == "__main__":
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones',45, 40000, 'hardware')
    tom = Person(name= 'Tom Doe', age= 50, pay=50000)
    print(sue,sue.pay,sue.lastName())

    for obj in (bob,sue,tom):
        obj.giveRaise(.10)
        print(obj)