# coding=utf-8

# 导入游戏框架
import pygame
from pygame.locals import *

# 英雄飞机类
class HeroPlane(object):
    def __init__(self, screen):
        self.x = 230
        self.y = 640
        self.screen = screen
        
        # 飞机图片路径
        self.imageName = "./feiji/hero.gif"
        
        # 创建玩家飞机图片
        self.HeroImage  = pygame.image.load(self.imageName).convert()
        
    # 显示飞机
    def display(self):

        # 设定显示玩家飞机
        self.screen.blit(self.HeroImage, (self.x, self.y))
    
    # 飞机向左移动
    def moveleft(self):
        self.x -= 20
    
    # 飞机向右移动
    def moveright(self):
        self.x += 20
   
    # 飞机发射子弹 
    def sheBullet(self):
        pass



if __name__ =="__main__":

    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    backgroup = pygame.image.load("./feiji/background.png").convert()   
   
    # 创建一个英雄飞机对象
    heroplane = HeroPlane(screen)
    
    # 3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(backgroup, (0, 0))
        
        # 显示英雄飞机
        heroplane.display()
    
        # 获取事件
        for event in pygame.event.get():

            # 判断是否点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()

            # 判断是否按下了按键
            if event.type ==KEYDOWN:
            
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    heroplane.moveleft()
                
                # 检测按键是否是d或在right
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    heroplane.moveright()

                # 检测按键是否按下空格
                elif event.key == K_SPACE:
                    print("space")



        pygame.display.update()
