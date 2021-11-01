# coding:utf-8
import pygame ,sys
from pygame.locals import  *
pygame.init()

# 创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255, 255, 255))

# 设置窗口标题
pygame.display.set_caption("飞机大战")

# 加载图片
enemy = pygame.image.load("images/enemy.png")
enemy2 = pygame.image.load("images/enemy2.png")
enemy3 = pygame.image.load("images/enemy3.png")
bg = pygame.image.load("images/bg.png")

def handleEvent():
	for event in pygame.event.get():
		if event.type == QUIT :
			pygame.quit()
			
while True:
	# 画出游戏背景
	
	# 更新屏幕内容
	pygame.display.update()
	# 处理关闭游戏
	handleEvent()
