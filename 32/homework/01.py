# coding:utf-8
# 使用传参的方式创建Enemy类，定义属性：type和color，
# 定义方法fly()实现在控制台显示属性
# 创建enemy对象，调用fly方法
# 在控制台输出 红色小敌机在飞翔


class Enemy():
    def __init__(self, type, color):
        self.type = type
        self.color = color

    def fly(self):
        print(self.color + self.type + '在飞翔')


enemy = Enemy('小敌机', '红色')
enemy.fly()
