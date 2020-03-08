# coding=utf-8

# 导入游戏框架
import pygame


if __name__ =="__main__":

    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    backgroup = pygame.image.load("./feiji/background.png").convert()   
   
   # 3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(backgroup, (0,0))
        # 刷新显示
        pygame.display.update()


