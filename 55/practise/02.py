#coding:utf-8
#定义Hair类
class Hair():
    def __init__(self,length,color):
        self.length = length 
        self.color = color 
    
#创建hair对象并访问对象的属性调用对象的方法
hair = Hair('长发','黑色')
print(hair.color+'的'+hair.length)

