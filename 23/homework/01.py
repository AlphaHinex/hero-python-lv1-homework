# coding:utf-8
#定义Pen类

#创建pen对象

#访问对象的属性并显示在控制台上

import easygui


class Pen:
    def __init__(self):
        self .color = 'orange'
        self.type = 'hero'


pen = Pen()
easygui.msgbox('pen:' + pen.color + ':' + pen.type)
