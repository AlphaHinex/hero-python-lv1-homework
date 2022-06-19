#coding:utf-8
class MobilePhone(object)
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def photograph(self):
        print('拍照更清晰')
class Vivo(MobilePhone)
    def __init__(self, color, model):
        MobilePhone.__init__(self, color, model)
    def photograph(self):
        print('逆光也清晰')


