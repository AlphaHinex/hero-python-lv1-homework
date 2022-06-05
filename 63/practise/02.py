#coding:utf-8
#定义父类Shape
class Shape(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        print(self.a + self.b + self.c)  
class Triangle(Shape):
    def __init__(self, a, b, c):
        Shape.__init__(self, a, b, c)


triangle = Triangle(3, 4, 5)
print(triangle.a + triangle.b + triangle.c)
triangle.perimeter()
