# coding:utf-8
# 在画布 50,150 的位置写出一个水果的单词
# 设置字体颜色为黑色 (0,0,0)
# 设置字体样式为微软雅黑，50号字

import pygame,sys,random,time
from pygame.locals import *
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))


#创建游戏退出事件处理方法
def handleEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()


def fruit(text, position):
    font = pygame.font.SysFont('微软雅黑', 50)
    newFont = font.render(text, True, (0, 0, 0))
    canvas.blit(newFont, position)


fruit('apple', (50, 150))

while True:
    #调用handleEvent方法
    handleEvent()
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
