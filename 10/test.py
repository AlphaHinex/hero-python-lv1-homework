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
bg = pygame.image.load("imgs/images/b1.jpg")
end = pygame.image.load("imgs/images/end.png")
#人物
person1 = pygame.image.load("imgs/images/1.png")
person2 = pygame.image.load("imgs/images/2.png")
person3 = pygame.image.load("imgs/images/3.png")
person4 = pygame.image.load("imgs/images/4.png")
person5 = pygame.image.load("imgs/images/5.png")
person6 = pygame.image.load("imgs/images/6.png")
person7 = pygame.image.load("imgs/images/7.png")
person8 = pygame.image.load("imgs/images/8.png")
person9 = pygame.image.load("imgs/images/9.png")
# 设置标题
pygame.display.set_caption("宫崎骏动画合集")

# 窗口点击事件
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        

def fillText(text,position):
    #设置字体
    TextFont = pygame.font.Font('fonts/font3.ttf',25)
    #设置字体其他样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)

while True:
    
    # 更新屏幕内容
    pygame.display.update()
    # 监听有没有按下退出按钮
    handleEvent()








