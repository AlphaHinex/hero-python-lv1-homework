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
bloveNum = 0
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







while True:
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()



