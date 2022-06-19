#coding:utf-8
#定义父类Fruit
class Fruit(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print('我爱吃水果')
