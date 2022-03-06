# coding:utf-8
# 创建列表cities存储五个去过的城市名称

cities = ['沈阳', '南京', '北京', '厦门', '大连']

# 利用remove函数移除自己所在的城市
cities.remove('沈阳')

# 将沈阳加回到列表中第二个位置
cities.insert(2, '沈阳')

# 在列表末尾再添加一个你去过的城市
cities.append('哈尔滨')

# 利用 pop 函数移除沈阳
cities.pop(2)

# 打印城市列表
print(cities)
