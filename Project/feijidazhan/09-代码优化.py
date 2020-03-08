# coding=utf-8

import random
# 导入游戏框架
import pygame
from pygame.locals import *
import time


# 飞机类基类
class Plan(object):
    def __init__(self, screen, name):
        #
        self.name = name
        # 显示窗口
        self.screen = screen
        # 创建玩家飞机图片
        self.image = pygame.image.load(self.imageName).convert()
        # 存储英雄飞机发射的所有子弹
        self.bullet_list = []

    # 显示飞机
    def display(self):
        # 设定显示玩家飞机
        self.screen.blit(self.image, (self.x, self.y))
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

    # 飞机发射子弹添加
    def sheBullet(self):
        heroBullet = Bullet(self.screen, self.name, self.x, self.y)
        self.bullet_list.append(heroBullet)


# 英雄飞机类
class HeroPlane(Plan):
    def __init__(self, screen, name):
        # 显示坐标
        self.x = 230
        self.y = 640
        # 飞机图片路径
        self.imageName = "./feiji/hero.gif"
        # 重载父类__init__方法
        super().__init__(screen, name)

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


# 敌人飞机类
class EnemyPlane(Plan):
    # 重写父类 __init__方法
    def __init__(self, screen, name):
        # 显示坐标
        self.x = 0
        self.y = 0
        # 飞机图片路径
        self.imageName = "./feiji/enemy-1.gif"
        # 飞机默认走向
        self.direction = "right"
        # 重载父类方法
        super().__init__(screen, name)

    # 敌机移动
    def move(self):
        if self.direction == "right":
            self.x += 0.2
        elif self.direction == "left":
            self.x -= 0.2
        if self.x >= 480 - 50:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    # 敌机发射子弹
    def sheBullet(self):
        # 设置子弹发射频率
        num = random.randint(1, 250)
        if num == 25:
            # 重载父类sheBullet方法
            super().sheBullet()


class Bullet(object):
    def __init__(self, screen, planName, x, y):

        # 传入类型
        self.genre = planName
        # 显示窗口
        self.screen = screen
        if self.genre == "hero":
            # 子弹默认坐标
            self.x = x + 40
            self.y = y - 20
            # 子弹图片路径
            self.imageName = "./feiji/bullet-3.gif"
        elif self.genre == "enemy":
            # 子弹默认坐标
            self.x = x + 25
            self.y = y + 30
            # 子弹图片路径
            self.imageName = "./feiji/bullet-1.gif"
        # 生成子弹图片
        self.image = pygame.image.load(self.imageName).convert()

    # 显示子弹
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    # 移动子弹
    def move(self):
        if self.genre == "hero":
            self.y -= 0.5
        elif self.genre == "enemy":
            self.y += 0.5

    # 判断子弹是否越界
    def examineBullet(self):
        if self.y < 0 or self.y > 890:
            return True
        else:
            return False


if __name__ == "__main__":

    # 1.创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)

    # 2.创建一个和窗口大小的图片，用来充当背景
    backgroup = pygame.image.load("./feiji/background.png").convert()

    # 创建一个英雄飞机对象
    heroplane = HeroPlane(screen, "hero")

    # 创建一个敌人飞机对象
    enemyplane = EnemyPlane(screen, "enemy")

    # 3.把背景图片放到窗口中显示
    while True:
        # 设定需要显示的背景图
        screen.blit(backgroup, (0, 0))

        # 显示英雄飞机
        heroplane.display()

        # 显示敌人飞机
        enemyplane.display()

        # 敌人飞机发射子弹
        enemyplane.sheBullet()

        # 敌人飞机移动
        enemyplane.move()

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
                #
                elif event.key == K_SPACE:
                    print("space")
                    heroplane.sheBullet()

            time.sleep(0.01)

        pygame.display.update()
