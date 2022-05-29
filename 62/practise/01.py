#coding:utf-8
#创建父类Hobby
class Hobby(object):
     def __init__(self,level):
         self.level = level
     def learn(self):
         print('跳舞使人体态优美')
