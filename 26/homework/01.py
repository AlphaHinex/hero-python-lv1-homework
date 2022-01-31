# coding:utf-8
# 定义 Phone 类，属性包括：name（名字）、price（价格）
# 在类中添加 use 方法，在控制台中显示内容
# 使用 Phone 类创建 phone 对象
# 调用 phone 对象的 use 方法
# 输出"使用iphoneX2000砸核桃"


class Phone():
    def __init__(self):
        self.name = 'iphonex'
        self.price = '2000'

    def use(self):
        print('使用' + self.name + self.price + '砸核桃')


phone = Phone()
phone.use()
