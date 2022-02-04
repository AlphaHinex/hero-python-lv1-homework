# coding:utf-8
# 定义 Enemy 类，使用传参的方法，
# 定义属性：type（种类），life（生命），score（分数）
# 创建 hero 对象
# 访问对象的属性，在控制台中显示 1:3:5


class Enemy():
    def __init__(self, type, life, score):
        self.type = type
        self.life = life
        self.score = score


hero = Enemy('1', '3', '5')
print(hero.type + ':' + hero.life + ':' + hero.score)

