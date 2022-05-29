#coding:utf-8
#定义父类Father
class Father(object):
    def __init__(self,name,complexion):
        self.name = name
        self.complexion = complexion
    def speak(self):
        print('我没有天赋')
#定义子类
class Ming(Father):
    def __init__(self,name,complexion):
        Father.__init__(self,name,complexion)
class Hua(Father):
    def __init__(self,name,complexion):
        Father.__init__(self,name,complexion)       
#创建对象并访问属性调用方法
ming = Ming('小明','肤色亮')
hua = Hua('小华','肤色暗')
print(ming.name+ming.complexion)
ming.speak()
print(hua.name+hua.complexion)
hua.speak()