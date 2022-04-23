#coding:utf-8
import pygame,sys,random
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

def handleEvent():
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()                 
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
    #创建paint方法
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #创建step方法
    def step(self):
        self.y  = self.y + 2
        
#创建enemies列表
enemies = [] 
def componentEnter():
    #随机生成坐标
    x = random.randint(0,480-57)
    x1 = random.randint(0,480-50)
    x2 = random.randint(0,480-169)
    #根据随机整数的值生成不同的敌飞机
    n = random.randint(0,9)
    if n <= 7:
        enemies.append(Enemy(x, 0, 57, 45, 1, 1, 1, enemy1))
    elif n == 8:
        enemies.append(Enemy(x1, 0, 50, 68, 2, 3, 5, enemy2))
    elif n == 9: 
        if len(enemies) == 0 or enemies[0].type != 3: 
            enemies.insert(0,Enemy(x2, 0, 169, 258, 3, 10, 20, enemy3))

#创建画组件方法
def componentPaint():
    #调用sky对象的paint方法
    sky.paint()
    for enemy in enemies:
        enemy.paint()  
#创建组件移动的方法
def componentStep():
    #调用sky对象的step方法
    sky.step()
    for enemy in enemies:
        enemy.step()    
#创建sky对象
sky = Sky()
while True:
    #调用componentEnter方法
    componentEnter()
    #调用componentPaint方法
    componentPaint()
    #调用componentStep方法
    componentStep()
    #处理关闭游戏
    handleEvent()
    #刷新屏幕内容
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
    
    
    
    
    