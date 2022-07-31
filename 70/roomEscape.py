# coding:utf-8
import sys, time, easygui, os, pygame
from pygame.locals import *
pygame.init()
# 设置窗口显示位置、大小、颜色、标题
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 70)
canvas = pygame.display.set_mode((1200, 580))
canvas.fill((0, 0, 0))
pygame.display.set_caption("城堡逃脱")

# 添加背景图片
bg = []
for i in range(17):
    bg.append(pygame.image.load("imgs/bg"+str(i)+".png"))

# 画初始界面
canvas.blit(bg[0], (0, 0))

# 设定游戏状态
class GameVar():
    ENTEROUT = 1       
    ESCAPE = 2         
    state = ENTEROUT   
    currentBg = 0     
    key = False        
    finding = False   

def handleEvent():  
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit() 
            sys.exit()
        #判断点击鼠标左键和不同状态调用不同方法
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if GameVar.state == GameVar.ENTEROUT:
                enterOutRoom()
            elif GameVar.state == GameVar.ESCAPE:
                escapeRoom(event)
    
#创建进出密室过程的方法
def enterOutRoom():   
    if GameVar.currentBg < 16:
        GameVar.currentBg = GameVar.currentBg + 1
    canvas.blit(bg[GameVar.currentBg],(0,0)) 
    if GameVar.currentBg ==  8:
        GameVar.state = GameVar.ESCAPE       
        GameVar.finding = True
        
        
       

  
# 创建方法判断点击到有效信息
def checkClick(e):
    x = e.pos[0]
    y = e.pos[1]
    if GameVar.finding == True:
        if x>55 and x<133 and y>311 and y<370:
            return 1 
        elif x>195 and x<254 and y>148 and y<226:
            return 2 
        elif x>705 and x<772 and y>366 and y<421:
            return 3 
        elif x>1050 and x<1155 and y>164 and y<474:
            return 4 
    else:
        return 5 
    
while True:
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    # 延时1秒 
    pygame.time.delay(500)
    