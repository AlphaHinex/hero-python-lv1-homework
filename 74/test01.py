#coding:utf-8
import pygame,sys,random,time,easygui
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
            
#定义父类FlyingObject
class FlyingObject(object):
    def __init__(self,x,y,width,height,life,img):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.life = life
        self.img = img
        #敌飞机移动的时间间隔
        self.lastTime = 0
        self.interval = 0.01
        #添加删除属性
        self.canDelete = False
    #定义paint方法
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    #定义step方法
    def step(self):
        #判断是否到了移动的时间间隔
        if not isActionTime(self.lastTime,self.interval):
            return
        self.lastTime = time.time()
        #控制移动速度
        self.y = self.y + 2
    #定义hit方法判断两个对象之间是否发生碰撞
    def hit(self,component):
        c = component
        return c.x>self.x-c.width and c.x<self.x+self.width and \
               c.y>self.y-c.height and c.y<self.y+self.height
    #定义bang方法处理对象之间碰撞后的处理
    def bang(self,bangsign):
        #敌机和英雄机碰撞之后的处理
        if bangsign:
            if hasattr(self,'score'):
                GameVar.score += self.score
            if bangsign == 2:
                self.life -= 1
            #设置删除属性为True
            self.canDelete = True
        #敌机和子弹碰撞之后的处理
        else:
            self.life -= 1
            if self.life == 0:
                #设置删除属性为True
                self.canDelete = True
                if hasattr(self,'score'):
                    GameVar.score += self.score 
    #定义outOfBounds方法判断对象是否越界
    def outOfBounds(self):
        return self.y > 650
        
#重构Enemy类
class Enemy(FlyingObject):
    def __init__(self,x,y,width,height,type,life,score,img):
        FlyingObject.__init__(self,x,y,width,height,life,img)
        self.type = type
        self.score = score
        
#重构Hero类
class Hero(FlyingObject):
    def __init__(self,x,y,width,height,life,img):
        FlyingObject.__init__(self,x,y,width,height,life,img)
        self.x = 480/2-self.width/2
        self.y = 650-self.height-30
        self.shootLastTime = 0
        self.shootInterval = 0.3
    def shoot(self):
        if not isActionTime(self.shootLastTime,self.shootInterval):
            return
        self.shootLastTime = time.time()
        GameVar.bullets.append(Bullet(self.x+self.width/2-5,self.y-10,10,10,1,b))
        
#重构Bullet类
class Bullet(FlyingObject):
    def __init__(self,x,y,width,height,life,img):
        FlyingObject.__init__(self,x,y,width,height,life,img)
    def step(self):
        self.y = self.y - 2
    #重写outOfBounds方法判断子弹是否越界
    def outOfBounds(self):
        return self.y < -self.height
      
#创建componentEnter方法 
def componentEnter():
    #随机生成坐标
    x = random.randint(0,480-57)
    x1 = random.randint(0,480-50)
    x2 = random.randint(0,480-100)
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
            GameVar.enemies.insert(0,Enemy(x2, 0, 100, 153, 3, 10, 20, enemy3))

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
    #写出分数和生命值
    fillText('SCORE:'+str(GameVar.score),(0,0))
    fillText('LIFE:'+str(GameVar.heroes),(380,0))
         
#创建组件移动的方法
def componentStep():
    #调用sky对象的step方法
    GameVar.sky.step()
    for enemy in GameVar.enemies:
        enemy.step()
    #使子弹移动
    for bullet in GameVar.bullets:
        bullet.step()
        
#创建删除组件的方法
def componentDelete():
    for enemy in GameVar.enemies:
        if enemy.canDelete or enemy.outOfBounds():
            GameVar.enemies.remove(enemy)
    for bullet in GameVar.bullets:
        if bullet.canDelete or bullet.outOfBounds():
            GameVar.bullets.remove(bullet)
    #从列表中删除英雄机
    if GameVar.hero.canDelete == True:
        GameVar.heroes -= 1
        if GameVar.heroes == 0:
            easygui.msgbox('游戏结束')
        else:
            GameVar.hero = Hero(0,0,60,75,1,h)

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
    #添加分数和生命值
    score = 0
    heroes = 3

#定义renderText方法
def renderText(text,position):
    my_font = pygame.font.SysFont("微软雅黑", 40)
    newText = my_font.render(text,True,(255,255,255))
    canvas.blit(newText,position)
 
#创建游戏退出事件处理方法
def handleEvent():
    for event in pygame.event.get():
        if event.type==pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()  
        #英雄机跟随鼠标移动
        if event.type==MOUSEMOTION:
            GameVar.hero.x = event.pos[0]-GameVar.hero.width/2
            GameVar.hero.y = event.pos[1]-GameVar.hero.height/2 
            
            
           

#创建checkHit方法
def checkHit():
    #判断英雄机是否与每一架敌飞机发生碰撞
    for enemy in GameVar.enemies:
        if GameVar.hero.hit(enemy):
            #敌机和英雄机调用bang方法
            enemy.bang(1)
            GameVar.hero.bang(2)
        #判断每一架敌飞机是否与每一颗子弹发生碰撞
        for bullet in GameVar.bullets:
            if enemy.hit(bullet):
                #敌机和子弹调用bang方法
                enemy.bang(0)
                bullet.bang(0)
 
while True:
    #调用componentEnter方法
    componentEnter()
    #调用componentPaint方法
    componentPaint()
    #调用componentStep方法
    componentStep()
    #调用shoot方法
    GameVar.hero.shoot()
    #调用handleEvent方法
    handleEvent()
    #调用checkHit方法
    checkHit()
    #调用componentDelete方法
    componentDelete()
    #刷新屏幕
    pygame.display.update()
    #延迟处理
    pygame.time.delay(15)
    
    
    
    
    
    
