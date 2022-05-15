# coding:utf-8
# coding:utf-8
# 获取当前时间秒数值，显示在控制台上
# 获取一周后的时间秒数值，显示在控制台上

import time
t = time.time()
print(str(t) + '秒')
a = 60*60*24*7 + t
print(str(a) + '秒')
