#coding:utf-8
import pygame
from pygame.locals import *
import time
import random
import sys
import easygui
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480,650))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")

enemy1=pygame.image.load("images/enemy1.png")


def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()
        
        
while True:
    #在画布中写出“hello world”文字
    
    # 更新屏幕内容
    pygame.display.update()
    #监听有没有按下退出按钮
    handleEvent()
    #延时15毫秒 
    pygame.time.delay(15)
