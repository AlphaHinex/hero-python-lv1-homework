# coding:utf-8
# 定义父类Shape


class Shape(object):
    def __init__(self, c):
        self.c = c

    def area(self):
        print(0.0625 * self.c * self.c)


class Square(Shape):
    def __init__(self, c):
        Shape.__init__(self, c)


square = Square(100)
square.area()
