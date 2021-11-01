# conding:utf-8
# 导入pygame,并初始化
import pygame, sys
from pygame.locals import*
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
            sys.exit()  
            
while True:
    # 使用变量在画布上画出两架敌飞机第一架坐标为(100,30)
    # 两架飞机的间隔为50
    
    
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()

    
