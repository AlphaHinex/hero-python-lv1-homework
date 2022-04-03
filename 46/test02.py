#coding:utf-8


class Gun():
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price


guns = [Gun('修罗', '副武器', '666'),
        Gun('极光', '狙击枪', '999'),
        Gun('青龙', '突击步枪', '888')]
for i in guns:
    print(i.name + i.type + i.price)
