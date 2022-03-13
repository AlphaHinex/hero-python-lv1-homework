#coding:utf-8
import pygame
from pygame.locals import *
import sys
import random
import time

#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 648))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")

#加载图片
enemy1=pygame.image.load("images/enemy1.png")
enemy2=pygame.image.load("images/enemy2.png")
enemy3=pygame.image.load("images/enemy3.png")
bg=pygame.image.load("images/bg1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
#定义Enemy类
class Enemy():
    def __init__(self,x,y,width,height,type,life,score,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.life = life
        self.score = score
        self.img = img
    #创建对象的方法
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.x = self.x + 2
        self.y = self.y + 2
    

while True:
    canvas.blit(bg,(0,0))
    
    
    # 更新屏幕内容
    pygame.display.update()
    #监听有没有按下退出按钮
    handleEvent()




    
   
       
