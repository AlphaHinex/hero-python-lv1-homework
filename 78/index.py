#coding:utf-8
import pygame,sys
import easygui
import random
import time
import datetime
import os
from pygame.locals import*
os.environ[ 'SDL_VIDEO_WINDOW_POS']="%d,%d"%(300, 50)
pygame.init()
canvas=pygame.display.set_mode((480, 650))
pygame.display.set_caption("红心大战")
# 加载图片
bg=pygame.image.load("images/bg3.png")
bg2=pygame.image.load("images/bg2.png")
bg3=pygame.image.load("images/bg5.png")
loveR=pygame.image.load("images/loveRed.png")
loveB=pygame.image.load("images/loveBlack.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type==QUIT  or  event.type==KEYDOWN and event.key==K_ESCAPE :
            pygame.quit()
            sys.exit()
# 写文字方法      
def fillText(text, position):
    TextFont = pygame.font.Font('images/WRYH.ttf', 25)
    newText = TextFont.render(text, True, (255, 0, 0))
    canvas.blit(newText, position)    
#创建黑心变量
mouseX = 200
mouseY = 200
bWidth = 18
bHeight = 18
bSpeed = 210
#创建黑心方法
arrBlove = []
def createBlove(bloveNum):
    for i in range(0, bloveNum):
        randPos = random.randint(0,3)
        randX = random.random()*(480-bWidth)
        randY = random.random()*(480-bHeight)
        speed = random.random()*200+bSpeed 
        if randPos == 0:
            arrBlove.append(Blove(randX,0,loveB,bWidth,bHeight,mouseX,mouseY,speed))  
        elif randPos == 1:
            arrBlove.append(Blove(462,randY,loveB,bWidth,bHeight,mouseX,mouseY,speed))
        elif randPos == 2:
            arrBlove.append(Blove(randX,632,loveB,bWidth,bHeight,mouseX,mouseY,speed))
        elif randPos == 3:
            arrBlove.append(Blove(0,randY,loveB,bWidth,bHeight,mouseX,mouseY,speed))

#创建黑心类
class Blove():
    global mouseX,mouseY
    def __init__(self,x,y,img,width,height,mouseX,mouseY,speed):
        self.x = x
        self.y = y
        self.img = img
        self.width = width
        self.height = height
        self.mouseX = mouseX
        self.mouseY = mouseY
        self.speed = speed
        self.xs = (self.mouseX-self.x)/speed
        self.ys = (self.mouseY-self.y)/speed
#创建生成黑心对象方法
bloveNum = 0
def born():
    global bloveNum
    if len(arrBlove) <= 0:
        bloveNum = bloveNum + 1
        createBlove(bloveNum)
#创建画图片方法  
def drawAll():
    canvas.blit(bg,(0,0))
    #绘制黑心
    for arrB in arrBlove:
        canvas.blit(arrB.img,(arrB.x,arrB.y))
#创建移动方法
def moveAll():
    global mouseX,mouseY
    for arrB in arrBlove:
        arrB.x = arrB.xs + arrB.x
        arrB.y = arrB.ys + arrB.y
#创建游戏开关方法
s = True
def switch():
    global s
    if s:
        #调用画图片方法
        drawAll()
        #调用生成黑心的方法
        born()
        #调用移动方法
        moveAll()

while True:
    #调用游戏开关方法
    switch()
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()



