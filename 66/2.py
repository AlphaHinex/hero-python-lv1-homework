x = int(input('请输入x坐标'))
y = int(input('请输入y坐标'))

if x >= 100 and x <= 400 and y >= 100 and y <= 400:
    print('您的点在' + str(x), str(y))
else:
    print('不在范围内')