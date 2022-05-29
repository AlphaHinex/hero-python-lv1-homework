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
#加载图片
bg=pygame.image.load("images/bg1.png")
startgame=pygame.image.load("images/startGame.png")
logo=pygame.image.load("images/LOGO.png")

#创建handleEvent方法
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION and \
                       event.button == 1:
            GameVar.sky.paint()

            
        
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
    def paint(self):
        canvas.blit(self.img,(self.x1,self.y1))
        canvas.blit(self.img,(self.x2,self.y2))
    def step(self):
        self.y1 = self.y1 + 1
        self.y2 = self.y2 + 1
        if self.y1 > self.height:
            self.y1 = -self.height
        if self.y2 > self.height:
            self.y2 = -self.height
#定义GameVar类
class GameVar():
    sky = None
#创建sky对象
GameVar.sky = Sky() 
#定义paintStart方法 
def paintStart():
    GameVar.sky.paint()
    canvas.blit(logo, (-40, 200))
    canvas.blit(startgame, (150, 400))   
paintStart()     
   
while True: 
    #更新屏幕内容
    pygame.display.update()
    #延时15毫秒 
    pygame.time.delay(15)
    #监听有没有按下退出按钮
    handleEvent()




    
   
       
