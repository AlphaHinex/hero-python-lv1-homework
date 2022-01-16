#coding:utf-8
import pygame,sys,easygui
from pygame.locals import *
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")


#加载图片
enemy=pygame.image.load("images/enemy1.png")
bg=pygame.image.load("images/bg1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()
#声明变量x1、y1、x2、y2、x3、y3存储飞机的坐标

while True:
    #画出静止不动的背景
    
    #画出三架飞机向右下方飞行,时间延迟15毫秒
    
        
    # 更新屏幕内容
    pygame.display.update()
    #监听有没有按下退出按钮
    handleEvent()
    
    