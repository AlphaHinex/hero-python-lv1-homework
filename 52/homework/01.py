# coding:utf-8
# 请定义一个 Cat 类，包含类属性：猫科
# 使用 __init__ 实例化方法创建对象属性 name
# 实例化一个任意名称的猫，在控制台中输出：猫名 属于 猫科


class Cat():
    type = '猫科'

    def __init__(self, name):
        self.name = name


print(Cat('🐱').name + '属于' + Cat.type)
