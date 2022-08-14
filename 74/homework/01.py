# coding:utf-8
import easygui
# 定义一个Car类，对象的属性包括：type(类型)、color(颜色)、number（车牌号）
# 使用Car类创建car对象
# 访问car对象的属性，并显示在信息提示框上


class Car():
    def __init__(self, type, color, number):
        self.type = type
        self.color = color
        self.number = number


car = Car('丰田', '白色', '辽A81810')

easygui.msgbox(car.type + car.color + car.number)
