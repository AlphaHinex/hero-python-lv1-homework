#coding:utf-8
import pygame,sys
from pygame.locals import*
#初始化pygame环境
pygame.init()
import time

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((650, 250))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("城市赛车")
bg=pygame.image.load("images/bg.png")
car=pygame.image.load("images/car1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()                

while True:
    
    #延时15毫秒
    pygame.time.delay(15)
    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()