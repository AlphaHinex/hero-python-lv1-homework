# coding:utf-8
import pygame
#创建一个长宽分别为480/650窗口
canvas = pygame.display.set_mode((480, 650))
canvas.fill((255,255,255))
#加载飞机图片
enemy1 = pygame.image.load("images/enemy1.png")
enemy2 = pygame.image.load("images/enemy2.png")
enemy3 = pygame.image.load("images/enemy3.png")

#定义Enemy类
class Enemy():
    def __init__(self,x,y,width,height,type,life,score,img):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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

#使用列表存储Enemy对象
enemies = [Enemy(100,0,57,45,1,1,1,enemy1),
           Enemy(200,0,50,68,2,3,5,enemy2),
           Enemy(300,0,169,258,3,20,20,enemy3)]

      





      