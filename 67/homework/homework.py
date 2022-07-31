# coding:utf-8
# 创建一个 Father 类，并添加 name，age，gender 三种属性
# 通过 Father 创建一个对象 son
# 使用 hasattr 方法，检测 son 中是否含有 name 属性
# 如果有，在控制台显示 true
import random


class Father():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


son = Father('name', 'age', 'gender')
hasattr(son, 'name')
if hasattr(son, 'name'):
    print('true')
