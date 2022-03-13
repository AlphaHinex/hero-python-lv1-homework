# coding:utf-8
# 创建 Vegetable 类，并且存储 name、color、benefits 三个属性
# 给对象添加 eat 方法
# 创建列表 vegetables 存储 Vegetable 对象
# 分别调用对象的 eat 方法将结果显示在控制台中
# 输出结果：
# 橙色的胡萝卜富含胡萝卜素
# 绿色的西蓝花富含维生素C
# 紫色的紫甘蓝富含维生素E


class Vegetable():
    def __init__(self, name, colour, benefits):
        self.name = name
        self.colour = colour
        self.benefits = benefits

    def eat(self):
        print(self.colour + '的' + self.name + self.benefits)


vegetables = [Vegetable('🥕', '橙色', '富含胡萝卜素'),
              Vegetable('🥦', '绿色', '富含维生素C'),
              Vegetable('紫甘蓝', '紫色', '含维生素E')]
vegetables[0].eat()
vegetables[1].eat()
vegetables[2].eat()