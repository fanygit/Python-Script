# coding=utf-8

# 导入游戏框架
import pygame
from pygame.locals import *


if __name__ =="__main__":

    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    backgroup = pygame.image.load("./feiji/background.png").convert()   
   
    # 创建玩家飞机图片
    HeroImage  = pygame.image.load("./feiji/hero.gif").convert()

    # 设定飞机位置
    x = 230
    y = 640
    
    # 3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(backgroup, (0, 0))
        
        # 设定显示玩家飞机
        screen.blit(HeroImage, (x, y))

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
                    x -= 20
                
                # 检测按键是否是d或在right
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    x += 20
                # 检测按键是否按下空格
                elif event.key == K_SPACE:
                    print("space")



        pygame.display.update()
