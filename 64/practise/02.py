#coding:utf-8
#定义父类Food
class Food(object):
    def __init__(self,name,taste):
        self.name = name
        self.taste = taste
    def eat(self):
        print(self.name+self.taste) 
