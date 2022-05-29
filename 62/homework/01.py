# coding:utf-8


class Person(object):
    def __init__(self, type):
        self.type = type

    def id(self):
        print('我是好人')


class Police(Person):
    def __init__(self, type):
        Person.__init__(self, type)


class Killer(Person):
    def __init__(self, type):
        Person.__init__(self, type)

    def id(self):
        print('我是坏人')


police = Police('警察')
killer = Killer('杀手')
police.id()
killer.id()
