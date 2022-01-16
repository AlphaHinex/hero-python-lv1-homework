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
bg = pygame.image.load('images/bg.png') 
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

while True:
          
        
    
    pygame.display.update()
    handleEvent()
