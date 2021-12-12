# coding:utf-8
import pygame, sys
from pygame.locals import QUIT
# 初始化pygame环境
pygame.init()

# 创建一个长宽分别为700/700窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("飞机大战")
enemy = pygame.image.load("images/enemy.png")
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()    
            sys.exit() 

#声明变量x1存储控制台输入的x坐标
#声明变量y1存储控制台输入的y坐标

while True:
    #根据输入的坐标画出小敌机
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
 

 
