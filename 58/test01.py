#coding:utf-8
import pygame
from pygame.locals import *
pygame.init()
#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 648))
canvas.fill((255,255,255))
#设置窗口标题
pygame.display.set_caption("飞机大战")
bg=pygame.image.load("images/bg1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN
        x = event.pos[0]
        y = event.pos[1]
        print(str(x) + ',' + str(y))

while True:
    canvas.blit(bg,(0,0))
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
    pygame.display.update()
    pygame.event.pump()
    handleEvent()

