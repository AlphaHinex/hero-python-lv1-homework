#coding:utf-8
class Father(object):
    def __init__(self, name, complexion):
        self.name = name
        self.complexion = complexion

    def speak(self):
        print('我没有天赋')


class Ming(Father):
    def __init__(self, name, complexion):
        Father.__init__(self, name, complexion)


class Hua (Father):
    def __init__(self, name, complexion, skill):
        Father.__init__(self, name, complexion)
        self.skill = skill
    def speak(self):
        print('有天赋')


ming = Ming('小明', '肤色亮')
hua = Hua('小华', '肤色暗', '绝对音感')
print(ming.name + ming.complexion)
print(hua.name + hua.complexion)
ming.speak()
hua.speak()
