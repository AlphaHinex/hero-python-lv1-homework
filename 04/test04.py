# coding:utf-8
import pygame, sys
from pygame.locals import QUIT

# 初始化pygame环境
pygame.init()

# 创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("飞机大战")
bg = pygame.image.load("images/bg1.png")

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()    
            sys.exit() 

def fillText(text, position):
    # 设置系统的默认字体
    TextFont = pygame.font.Font('font1.ttf', 40)
    # 设置生命值的样式
    newText = TextFont.render(text, True, (255, 255, 255))
    canvas.blit(newText, position)


while True:
    # 画出游戏背景 
    canvas.blit(bg,(0,0))
    fillText('分数',(0,5))
    # 
    
    # 
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
 

 
