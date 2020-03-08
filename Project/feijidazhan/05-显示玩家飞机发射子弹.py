# coding=utf-8

# 导入游戏框架
import pygame
from pygame.locals import *
import time


# 英雄飞机类
class HeroPlane(object):
    def __init__(self, screen):
        self.x = 230
        self.y = 640
        self.screen = screen

        # 飞机图片路径
        self.imageName = "./feiji/hero.gif"

        # 创建玩家飞机图片
        self.HeroImage = pygame.image.load(self.imageName).convert()

        # 存储英雄飞机发射的所有子弹
        self.bullet_list = []
    
    #显示飞机
    def display(self):
        # 设定显示玩家飞机
        self.screen.blit(self.HeroImage, (self.x, self.y))
        # 记录飞机越界子弹
        bullet_list_record = []
        # 设定显示子弹
        for bullet in self.bullet_list:
            # 把子弹显示到窗口
            bullet.display()
            # 子弹移动
            bullet.move()
        # 判断子弹是否越界 销毁子弹
        for bullet in self.bullet_list:
            if bullet.examineBullet():
                bullet_list_record.append(bullet)
        
        # 先记录在删除 目的是为了避免BUG
        for bullet in bullet_list_record:
            self.bullet_list.remove(bullet)

    # 飞机向左移动
    def moveleft(self):
        self.x -= 20

    # 飞机向右移动
    def moveright(self):
        self.x += 20

    # 飞机向上移动
    def moveup(self):
        self.y -= 20

    # 飞机向下移动
    def movedown(self):
        self.y += 20

    # 飞机发射子弹添加
    def sheBullet(self):
        newBullet = Bullet(self.screen, self.x, self.y)
        self.bullet_list.append(newBullet)


# 子弹类
class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen

        self.imageName = "./feiji/bullet-3.gif"

        self.BulletImage = pygame.image.load(self.imageName).convert()

        # 显示子弹

    def display(self):
        self.screen.blit(self.BulletImage, (self.x, self.y))

    # 移动子弹
    def move(self):
        self.y -= 1

    def examineBullet(self):
        if self.y < 0:
            return True
        else:
            return False

	
		
			

if __name__ == "__main__":

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
            if event.type == KEYDOWN:

                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    heroplane.moveleft()

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    heroplane.moveright()

                # 检测按键是否是w或者up
                elif event.key == K_w or event.key == K_UP:
                    print("up")
                    heroplane.moveup()

                # 检测按键是否是s或者down
                elif event.key == K_s or event.key == K_DOWN:
                    print("down")
                    heroplane.movedown()
                
                elif event.key == K_SPACE:
                    print("space")
                    heroplane.sheBullet()
            time.sleep(0.01)
        
        pygame.display.update()
