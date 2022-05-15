#coding:utf-8
import pygame
pygame.init()
#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 648))
canvas.fill((255,255,255))
#设置窗口标题
pygame.display.set_caption("飞机大战")
      
while True:
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(1000)
    list = pygame.event.get()
    print(list)


    
   

