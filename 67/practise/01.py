#coding:utf-8
import pygame,sys,random,time
from pygame.locals import *
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))

 
#创建游戏退出事件处理方法
def handleEvent():
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()  

 
while True:
    font = pygame.font.SysFont('微软雅黑', 80)
    newFont = font.render('TNT:=(. L .)=:', True, (139, 69, 0))
    canvas.blit(newFont, (10, 110))
    font = pygame.font.SysFont('微软雅黑', 80)
    newFont = font.render('TNT:=(. L .)=:', True, (0, 0, 0))
    canvas.blit(newFont, (45, 110))
    
    #调用handleEvent方法
    handleEvent()
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
    
    
    
    
    
    
