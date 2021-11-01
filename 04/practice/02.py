#coding:utf-8
import pygame,sys
from pygame.locals import QUIT
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")
bg=pygame.image.load("images/bg4.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()    
            sys.exit() 

def fillText(text,position):
    #设置系统的默认字体
    TextFont = pygame.font.Font('font.ttf',30)
    #设置生命值的样式
    newText = TextFont.render(text,True,(0,0,0))
    canvas.blit(newText,position)


while True:
    #在屏幕上写出文字
    
    # 更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()
 

 
