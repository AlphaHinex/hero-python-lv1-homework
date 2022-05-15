#coding:utf-8
import pygame,sys,random,time
from pygame.locals import *
#初始化pygame环境
pygame.init()

#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))

#设置窗口标题
pygame.display.set_caption("飞机大战")
bg=pygame.image.load("images/bg1.png")
enemy1 = pygame.image.load("images/enemy1.png")
enemy2 = pygame.image.load("images/enemy2.png")
enemy3 = pygame.image.load("images/enemy3.png")
b=pygame.image.load("images/bullet1.png")
h=pygame.image.load("images/hero.png")

#添加时间间隔的方法
def isActionTime(lastTime, interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval
              
#定义Sky类
class Sky():
    def __init__(self):
        self.width = 480
        self.height = 852
        self.img = bg
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = -self.height
    #创建paint方法
    def paint(self):
        canvas.blit(self.img,(self.x1,self.y1))
        canvas.blit(self.img,(self.x2,self.y2))
    #创建step方法
    def step(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        if self.y1 > self.height:
            self.y1 = -self.height
        if self.y2 > self.height:
            self.y2 = -self.height

#定义Enemy类
class Enemy():
    def __init__(self,x,y,width,height,type,life,score,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.life = life
        self.score = score
        self.img = img
        #敌飞机移动的时间间隔
        self.lastTime = 0
        self.interval = 0.01
    #创建paint方法
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #创建step方法
    def step(self):
        #判断是否到了敌飞机移动的时间间隔
        if not isActionTime(self.lastTime,self.interval):
            return
        self.lastTime = time.time()
        self.y  = self.y + 2   

#定义Hero类
class Hero():
    def __init__(self,x,y,width,height,life,img):
        self.width = width
        self.height = height
        self.x = 480/2-self.width/2
        self.y = 650-self.height-30
        self.life = life
        self.img = img
        self.shootLastTime = 0
        self.shootInterval = 0.3
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def shoot(self):
        if not isActionTime(self.shootLastTime,self.shootInterval):
            return
        self.shootLastTime = time.time()
        #向列表中添加子弹对象
        GameVar.bullets.append(Bullet(self.x+self.width/2-5,self.y-10,10,10,1,b))
        
        
#定义Bullet类
class Bullet():
    def __init__(self,x,y,width,height,life,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.life = life
        self.img = img
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def step(self):
        self.y = self.y - 2    
        
#创建componentEnter方法 
def componentEnter():
    #随机生成坐标
    x = random.randint(0,480-57)
    x1 = random.randint(0,480-50)
    x2 = random.randint(0,480-169)
    #根据随机整数的值生成不同的敌飞机
    n = random.randint(0,9)
    #判断是否到了产生敌飞机的时间
    if not isActionTime(GameVar.lastTime,GameVar.interval):
        return
    GameVar.lastTime = time.time()
    if n <= 7:
        GameVar.enemies.append(Enemy(x, 0, 57, 45, 1, 1, 1, enemy1))
    elif n == 8:
        GameVar.enemies.append(Enemy(x1, 0, 50, 68, 2, 3, 5, enemy2))
    elif n == 9: 
        if len(GameVar.enemies) == 0 or GameVar.enemies[0].type != 3: 
            GameVar.enemies.insert(0,Enemy(x2, 0, 169, 258, 3, 10, 20, enemy3))

#创建画组件方法
def componentPaint():
    #判断是否到了飞行物重绘的时间
    if not isActionTime(GameVar.paintLastTime,GameVar.paintInterval):
        return
    GameVar.paintLastTime = time.time()
    #调用sky对象的paint方法
    GameVar.sky.paint()
    for enemy in GameVar.enemies:
        enemy.paint()
    #画出英雄机
    GameVar.hero.paint()
    #画出子弹对象
    for bullet in GameVar.bullets:
        bullet.paint()
         
#创建组件移动的方法
def componentStep():
    #调用sky对象的step方法
    GameVar.sky.step()
    for enemy in GameVar.enemies:
        enemy.step()
    #使子弹移动
    for bullet in GameVar.bullets:
        bullet.step()
        

#定义GameVar类
class GameVar():
    sky = Sky()
    enemies = []
    #产生敌飞机的时间间隔
    lastTime = 0
    interval = 1.5
    #重绘飞行物的时间间隔
    paintLastTime = 0
    paintInterval = 0.04
    #创建英雄机对象
    hero = Hero(0,0,60,75,1,h)
    #创建列表存储子弹对象
    bullets = []
 

 
 
while True:
    #调用componentEnter方法
    componentEnter()
    #调用componentPaint方法
    componentPaint()
    #调用componentStep方法
    componentStep()
    #调用shoot方法
    GameVar.hero.shoot()
    
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
    
    
    
    
    
    
