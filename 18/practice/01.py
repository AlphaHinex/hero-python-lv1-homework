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
#声明变量表示汽车和背景的坐标

#声明变量表示背景的宽和第二张背景的坐标

while True:
    #画出背景并移动
    
    #画出第二张背景并实现背景连续横向移动
    
    #画出汽车并向左移动，当超过左侧边界后,从右侧出现继续向左移动
    
    #延时15毫秒
    pygame.time.delay(15)
    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()