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

def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()    
            sys.exit() 

def fillText(text, position):
    # 设置字体
    TextFont = pygame.font.SysFont('微软雅黑', 40)
    # 设置字体其他样式
    newText = TextFont.render(text, True, (255, 0, 0))
    canvas.blit(newText, position)

while True:
    # 声明变量string并赋值为007
    # 使用字符串拼接符将字符串‘ID’与变量string拼接写在屏幕(220,280)的位置
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
 

 
