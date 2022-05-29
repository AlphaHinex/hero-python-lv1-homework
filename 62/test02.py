#coding:utf-8
class Father(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Lan(Father):
    def __init__(self, name, color):
        Father.__init__(self, name, color)

