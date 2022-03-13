# coding:utf-8
# 定义Teacher类，并且存储 name，age 两个属性
# 创建列表 teacher_list 存储 Teacher 对象
# 在控制台中获取列表中下标为2的对象的两个属性
import random

class Teacher():
    def __init__(self, name, age):
        self.name = name
        self.age = age


teacher_list = [Teacher('关老师', '90岁'),
                Teacher('刘老师', '20岁'),
                Teacher('小黑老师', '99999999岁')]

# 再定义两个 Teacher 对象
teacher = Teacher('董老师', '999岁')
teacher1 = Teacher('张老师', '200岁')

# 将新定义的两个 Teacher 对象添加到队列中
# 其中一个追加到最后
# 另一个插入到下标为 3 处
teacher_list.append(teacher)
teacher_list.insert(3, teacher1)

# 随机移除队列中的一个对象
teacher_list.pop(random.randint(0, 4))

# 打印结果

print(teacher_list[2].name, teacher_list[2].age)
