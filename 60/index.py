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
        #游戏开始状态转换为选择状态
        if event.type == KEYDOWN and event.key == K_SPACE:
            if GameVar.state == "START":
                GameVar.state = "CHOICE"
        
        
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
        #玩家B选择出战飞机
        while True:
            m = easygui.enterbox('请输入玩家B的飞机类型')
            if m == '':
                easygui.msgbox('请输入1-4的数字')
            else:
                m = int(m)
                if m == 1:
                    planeB = plane1
                    break
                elif m == 2:
                    planeB = plane2
                    break
                elif m == 3:
                    planeB = plane3
                    break
                elif m == 4:
                    planeB = plane4
                    break
                else:
                    easygui.msgbox('请输入1-4的数字')
    GameVar.flag = False   
#创建控制飞机移动方法
def move():
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_d:
            GameVar.x1 = GameVar.x1 + 5
            if GameVar.x1 > 1200:
                GameVar.x1 = 1200
        elif event.type == KEYDOWN and event.key == K_s:
            GameVar.y1 = GameVar.y1 + 5
            if GameVar.y1 > 461:
                GameVar.y1 = 461
        elif event.type == KEYDOWN and event.key == K_a:
            GameVar.x1 = GameVar.x1 - 5
            if GameVar.x1 < 0:
                GameVar.x1 = 0
        elif event.type == KEYDOWN and event.key == K_w:
            GameVar.y1 = GameVar.y1 - 5
            if GameVar.y1 < 0:
                GameVar.y1 = 0
        
               
# 定义GameVar类
class GameVar():
    enemies = []
    # 产生敌飞机的时间间隔
    lastTime = 0
    interval = 5
    # 重绘飞行物的时间间隔
    paintLastTime = 0
    paintInterval = 0.001
    #创建列表STATES存储游戏状态
    STATES = ["START","CHOICE","RUNNING","END"]
    #创建变量state存储游戏初始状态
    state = STATES[0]
    #创建变量flag控制是否可以选择比赛
    flag = True
    #创建变量存储两架飞机的坐标
    x1 = 0
    y1 = 30
    x2 = 0
    y2 = 420
#创建状态控制方法
def controlState():
    if GameVar.state == "START":
        canvas.blit(bg,(0,0))
    #选择状态下画出的图片
    elif GameVar.state == "CHOICE":
        canvas.blit(bg1,(0,0))
        canvas.blit(plane1,(160,300))
        canvas.blit(plane2,(410,300))
        canvas.blit(plane3,(670,300))
        canvas.blit(plane4,(940,300))
        pygame.display.update()
        #调用enter方法
        enter()
    
        
while True:
    #调用状态控制方法
    controlState()
    # 更新屏幕内容
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
    


