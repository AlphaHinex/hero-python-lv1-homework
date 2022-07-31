# coding:utf-8
import sys, time, easygui, os, pygame
from pygame.locals import *
pygame.init()
# 设置窗口显示位置、大小、颜色、标题
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 70)
canvas = pygame.display.set_mode((1200, 580))
canvas.fill((0, 0, 0))
pygame.display.set_caption("城堡逃脱")

  

def handleEvent():  
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()
        

    
while True:
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    # 延时1秒 
    pygame.time.delay(500)
    