# coding:utf-8
import pygame, os, time, easygui
from pygame.locals import*
pygame.init()
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
canvas = pygame.display.set_mode((1200, 640))
pygame.display.set_caption("龙珠超-神龙篇")
# 加载音乐和图片
bg_music1 = pygame.mixer.Sound('images/bgmusic.wav')
bg_music2 = pygame.mixer.Sound('images/bgmusic2.wav')
bg1 = pygame.image.load("images/bg.png")
# 关闭窗口代码
def handleEvent():
    for event in pygame.event.get():
        if event.type == QUIT  or  event.type == KEYDOWN and event.key == K_ESCAPE :
            pygame.quit()
            sys.exit()
        
  
# 创建选择人物方法       
def choice():
    name = ('孙悟空', '贝吉塔', '超赛悟空', '18号')
    p1 = easygui.buttonbox(msg="请选择人物", title="", choices=name)
    if p1 == '孙悟空':
        Game.hero = pygame.image.load("images/h1.png")
    elif p1 == '贝吉塔':    
        Game.hero = pygame.image.load("images/h2.png")
    elif p1 == '超赛悟空':    
        Game.hero = pygame.image.load("images/h3.png")  
    else:
        Game.hero = pygame.image.load("images/h4.png")    
                  
while True:
    pygame.display.update()
    # 处理关闭游戏
    handleEvent()
