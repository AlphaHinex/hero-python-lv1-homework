#coding:utf-8
class Cock():
    def __init__(self,gender,color,weight):
        self.gender = gender
        self.color = color
        self.weight = weight
    def study(self):
        print(self.gender+self.color+self.weight)
#创建对象
cock = Cock('雄性','黑色','200g')
cock.study()

