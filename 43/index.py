#coding:utf-8
import pygame,sys,random
from pygame.locals import*
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

enemies = []
def componentEnter():
    x1 = random.randint(0, 480-57)
    x2 = random.randint(0, 480-50)
    x3 = random.randint(0, 480-160)

    n = random.randint(0, 9)

    if n <= 7:
         enemies.append(Enemy(x1, 0, 57, 45, 1, 1, 1, enemy1))
    if n == 8:
         enemies.append(Enemy(x2, 10, 50, 68, 2, 3, 5, enemy2))
    if n == 9:
         enemies.append(Enemy(x3, 0, 169, 258, 3, 10, 20, enemy3))






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
        


       
#创建sky对象
sky = Sky()
while True:
    #调用sky对象的paint方法
    sky.paint()
    #调用sky对象的step方法
    sky.step()
    componentEnter()
    enemies[0].paint()
    enemies[0].step()
    
    #更新屏幕内容
    pygame.display.update()
    #处理关闭游戏
    handleEvent()
    pygame.time.delay(15)