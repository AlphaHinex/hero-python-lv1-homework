year = int(input('年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('是闰年')
else:
    print('是平年')
