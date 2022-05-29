# coding:utf-8
import pygame
import easygui
import random
import time
import easygui
import sys
import os
from pygame.locals import*
pygame.init()
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 50)
canvas = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("生死时速")
# 加载图片
plane1 = pygame.image.load("images/feiji1.png")
plane2 = pygame.image.load("images/feiji2.png")
plane3 = pygame.image.load("images/feiji3.png")
plane4 = pygame.image.load("images/feiji4.png")
plane5 = pygame.image.load("images/feiji5.png")
planeA = pygame.image.load("images/feiji1.png")
planeB = pygame.image.load("images/feiji1.png")
bg = pygame.image.load("images/bg1.png")
bg1 = pygame.image.load("images/bg2.png")
bg2 = pygame.image.load("images/bg3.png")
victory = pygame.image.load("images/victory.png")
stone = pygame.image.load("images/stone.png")

# 按键事件
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT  or  (event.type == KEYDOWN and event.key == K_ESCAPE) :
            pygame.quit()
            sys.exit()
        
# 画红线    
def draw():
    pygame.draw.rect(canvas, (255, 0, 0), (1100, 0, 10, 600))
# 添加时间间隔的方法
def isActionTime(lastTime, interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval
class Enemy():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
    # 创建paint方法
    def paint_step(self):
        canvas.blit(self.img, (self.x, self.y))
        self.x = self.x - 0.5
#  创建componentEnter方法
def componentEnter():
    # 随机生成坐标
    y = random.randint(0, 600 - 57)
    # 判断是否到了产生敌飞机的时间
    if not isActionTime(GameVar.lastTime, GameVar.interval):
        return
    GameVar.lastTime = time.time()
    GameVar.enemies.append(Enemy(1200, y, stone))
# 创建画组件方法
def componentPaint():
    for enemy in GameVar.enemies:
        enemy.paint_step()
        if (enemy.x > GameVar.x1 and enemy.x <= GameVar.x1 + 100) and (enemy.y <= GameVar.y1 and enemy.y + 100 >= GameVar.y1) : 
            GameVar.x1 = GameVar.x1 - 100
            if GameVar.x1 < 0:
                GameVar.x1 = 0
        elif(enemy.x > GameVar.x1 and enemy.x <= GameVar.x1 + 100) and (enemy.y > GameVar.y1 and enemy.y < GameVar.y1 + 100):
            GameVar.x1 = GameVar.x1 - 100
            if GameVar.x1 < 0:
                GameVar.x1 = 0
        if  (enemy.x > GameVar.x2 and enemy.x <= GameVar.x2 + 100) and (enemy.y <= GameVar.y2 and enemy.y + 100 >= GameVar.y2) : 
            GameVar.x2 = GameVar.x2 - 100
            if GameVar.x2 < 0:
                GameVar.x2 = 0
        elif(enemy.x > GameVar.x2 and enemy.x <= GameVar.x2 + 100) and (enemy.y > GameVar.y2 and enemy.y < GameVar.y2 + 100):
            GameVar.x2 = GameVar.x2 - 100 
            if GameVar.x2 < 0:
                GameVar.x2 = 0 
#定义选择出战飞机方法
def enter():
    global planeA,planeB
    if GameVar.flag:
        while True:
            n = easygui.enterbox('请输入玩家A的飞机类型')
            if n == '':
                easygui.msgbox('请输入1-4的数字')
            else:
                n = int(n)
                if n == 1:
                    planeA = plane1
                    break
                elif n == 2:
                    planeA = plane2
                    break
                elif n == 3:
                    planeA = plane3
                    break
                elif n == 4:
                    planeA = plane4
                    break
                else:
                    easygui.msgbox('请输入1-4的数字')
        
    GameVar.flag = False               
# 定义GameVar类
class GameVar():
    enemies = []
    # 产生敌飞机的时间间隔
    lastTime = 0
    interval = 5
    # 重绘飞行物的时间间隔
    paintLastTime = 0
    paintInterval = 0.001
    

        
            
while True:
    
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
    


