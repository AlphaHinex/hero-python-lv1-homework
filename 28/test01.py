#coding:utf-8
import easygui
#使用变量存储用户输入的信息
name = easygui.enterbox('请输入您注册的帐号')
pwd = easygui.enterbox('请输入您注册的密码')
#定义User类
class User():
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
    def register(self):
        easygui.msgbox('您注册的帐号为:'+self.name+
                             '\n'+'您注册的密码为:'+self.pwd)
user = User(name,pwd)
user.register()
#使用if来判断用户帐号及密码是否正确
myName = easygui.enterbox('请输入您登录的帐号')
if myName == name:
    myPwd = easygui.enterbox('请输入您登录的密码')
    if myPwd == pwd:
        easygui.msgbox('登录成功')
    if myPwd != pwd:
        easygui.msgbox('登录失败')
else:
    easygui.msgbox('帐号不匹配')