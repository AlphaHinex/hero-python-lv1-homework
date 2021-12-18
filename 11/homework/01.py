# coding:utf-8
import easygui
# 使用输入框提示用户输入‘今天是星期几’

#使用if-elif-else语句判断，如果输入‘星期一’，在控制台显示‘复习语文’
#如果输入‘星期二’，显示‘复习数学’，输入‘星期三’，显示‘复习英语’
#输入其他内容，显示‘复习编程’

d = easygui.enterbox('请输入 1-3 的数字')
if d == '1':
    print('复习语文')
elif d == '2':
    print('复习数学')
elif d == '3':
    print('复习英语')
else:
    easygui.msgbox('复习编程')