# coding:utf-8
import pygame
from pygame.locals import *
import sys
import random
import time
import os
pygame.init()
# 创建窗口
os.environ[ 'SDL_VIDEO_WINDOW_POS']="%d,%d"%(130, 65)
canvas = pygame.display.set_mode((1000, 600))
# 背景
bg = pygame.image.load("imgs/b1.jpg")
bg2 = pygame.image.load("imgs/b2.jpg")
end = pygame.image.load("imgs/end1.png")
#人物
Hulk = pygame.image.load("imgs/1.png")
Thor = pygame.image.load("imgs/2.png")
Black_Widow = pygame.image.load("imgs/3.png")
Captain_America = pygame.image.load("imgs/4.png")
Iron_Man = pygame.image.load("imgs/5.png")
Black_panther = pygame.image.load("imgs/6.png")
Spiderman = pygame.image.load("imgs/7.png")
Thanos = pygame.image.load("imgs/8.png")

# 设置标题
pygame.display.set_caption("复仇者联盟")

# 窗口点击事件
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        
def fillText(text,position):
    #设置系统的默认字体
    TextFont = pygame.font.SysFont('宋体',40)
    #设置生命值的样式
    newText = TextFont.render(text,True,(255,255,255))
    canvas.blit(newText,position)
    

    # 更新屏幕内容
    pygame.display.update()
    # 监听有没有按下退出按钮
    handleEvent()








