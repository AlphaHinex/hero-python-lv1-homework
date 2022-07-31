list = []
for i in range(7, 101, 7):
    list.append(i)
c = len(list)
s = sum(list)
password = str(c) + str(s)
print(password)
