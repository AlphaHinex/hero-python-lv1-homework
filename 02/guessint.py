import random, easygui 

secret = random.randint(1, 100)
tries = 0
easygui.msgbox('现在开始猜数字，数字的范围是1-100')
temp = easygui.integerbox("请输入一个数字：")
guess = int(temp)

if guess == secret:   
    easygui.msgbox("恭喜你一次就猜对了！")   
else:
    if guess < secret:  
        easygui.msgbox("猜小了!")  
    else:
        easygui.msgbox("猜大了！") 

while guess != secret and tries < 15:
	temp = easygui.integerbox("猜错了，重新猜猜吧:")
	guess = int(temp)
	tries += 1
	if guess == secret:
		easygui.msgbox("恭喜您，猜对啦！")
	else:
		if guess < secret:
			easygui.msgbox("猜小了！")
		else:
			easygui.msgbox('猜大了')
	while tries >= 50:
		easygui.msgbox("没有机会了")
		break
easygui.msgbox("哈哈，正确数字是" + str(secret))
