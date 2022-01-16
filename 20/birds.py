#coding:utf-8
import pygame
from pygame.locals import *
import sys
#pygame环境初始化
pygame.init()
#设置一个长为1250，宽为700的窗口
canvas = pygame.display.set_mode((1250, 700))
canvas.fill((255,255,255))
# 设置窗口标题
pygame.display.set_caption("愤怒的小鸟")
# 背景图片加载
bg = pygame.image.load('images/bg2.png') 
# 加载图片
bird = pygame.image.load('images/bird.png')
pig = pygame.image.load('images/pig.png')
slingshot1 = pygame.image.load('images/slingshot1.png')
slingshot2 = pygame.image.load('images/slingshot2.png')
stand1 = pygame.image.load('images/stand1.png')
stand2 = pygame.image.load('images/stand2.png')
stand3 = pygame.image.load('images/stand3.png')

def handleEvent():
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

x = 135
while True:
    #绘制背景、弹弓、小鸟
    canvas.blit(bg,(0,0))
    canvas.blit(slingshot1,(155,305))
    canvas.blit(slingshot2,(125,300))
    canvas.blit(bird,(105,460))
    canvas.blit(bird,(50,500))
    canvas.blit(bird,(10,500))
    if x < 1130:
        canvas.blit(bird,(x,315))
        canvas.blit(pig,(825,365))
        canvas.blit(pig,(910,365))
        canvas.blit(pig,(995,365))
        canvas.blit(pig,(1130,315))
        canvas.blit(stand1,(1132,361))
        canvas.blit(stand2,(1150,372))
        x = x + 3
    else:
        canvas.blit(bird,(1200,500))
        canvas.blit(stand3,(1080,445))
     
    
    pygame.display.update()
    handleEvent()
