# coding:utf-8
# 创建 Dog 类，并且存储 name，action 两个属性
# 在类中添加 behavior 方法，显示谁（name）会做什么（action）
# 创建列表 dogs 存储 Dog 对象
# 使用 for in 循环遍历列表调用对象的 behavior 方法
# 将结果显示在控制台中
# 呆萌的二哈会拆墙
# 温顺的金毛会陪伴
# 可爱的泰迪会撒娇


class Dog():
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def behavior(self):
        print(self.name + '在' + self.action)


dogs = [Dog('二哈', '拆家'),
        Dog('金毛', '陪伴'),
        Dog('泰迪', '撒娇')]
for a in dogs:
    a.behavior()