#coding:utf-8
#定义父类Shape
class Shape(object):
    def __init__(self,c):
        self.c = c
    def area(self):
        print(0.0796*self.c*self.c)
