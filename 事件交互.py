import random

import pygame

# 初始化硬件
pygame.init()

# 创建屏幕并设置尺寸
screen = pygame.display.set_mode([400, 600])

# 设置窗口标题
pygame.display.set_caption("飞机大战")


# 可移动父类
class MoveObject:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0  # 1234代表上下左右
        self.img = None

    # 定义所有物体可以移动
    def move(self):
        pass

    # 定义所有物体可以显示
    def show(self):
        pass


# 子弹继承与可移动父类
class Bullet(MoveObject):

    def __init__(self):
        self.img = pygame.image.load("bullet.png")

    # 重写移动
    def move(self):
        if self.d == 1:
            self.y = self.y - 2
        if self.d == 2:
            self.y = self.y + 2

    # 重写显示
    def show(self):
        screen.blit(self.img, [self.x, self.y])


# 我方法飞机继承可移动类
class Plane(MoveObject):
    def __init__(self):
        self.img = pygame.image.load("plane.png")
        self.x = 200
        self.y = 500
        self.d = 0
        # 子弹集合
        self.bulletList = []

    # 重写移动
    def move(self):
        if self.d == 1: self.y = self.y - 1
        if self.d == 2: self.y = self.y + 1
        if self.d == 3: self.x = self.x - 1
        if self.d == 4: self.x = self.x + 1

    # 重写显示
    def show(self):
        screen.blit(self.img, [self.x, self.y])

    # 飞机发射子弹
    def shot(self):
        # 创建子弹并添加到列表
        bullet = Bullet()
        bullet.x = self.x + 25
        bullet.y = self.y
        bullet.d = 1
        self.bulletList.append(bullet)


# 敌人类
class Enemy(MoveObject):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0
        self.bulletList = []
        self.img = pygame.image.load("enemy.png")

    def show(self):
        screen.blit(self.img, [self.x, self.y])

    def move(self):
        # 敌机下移动
        self.y = self.y + 1

        # 控制敌机左右移动
        if self.d == 3: self.x = self.x - 1
        if self.d == 4: self.x = self.x + 1

        # 控制敌机改变方向
        if self.x <= 0: self.d = 4
        if self.x >= 400: self.d = 3

        # 敌机低部越界
        if self.y >= 600: self.y = 0

        # 飞机发射子弹
        if random.random() < 0.001:
            self.shot()

    # 敌机发射子弹
    def shot(self):
        # 创建子弹并添加到列表
        bullet = Bullet()
        bullet.x = self.x + 12
        bullet.y = self.y
        bullet.d = 2
        self.bulletList.append(bullet)


plane = Plane()

enemyList = []
# 随机生成敌人
for i in range(1, 16):
    # 创建敌机
    enemy = Enemy()
    enemy.x = random.randint(25, 375)
    enemy.y = random.randint(25, 150)
    if random.random() < 0.5:
        enemy.d = 3
    else:
        enemy.d = 4
    # 添加敌机到集合
    enemyList.append(enemy)

# 游戏主逻辑
while True:

    # 清空屏幕
    screen.fill([0, 0, 0])

    # 显示飞机
    plane.show()

    # 飞机移动
    plane.move()

    # 显示子弹
    for b in plane.bulletList:
        b.move()
        b.show()
        if b.y < 0:
            plane.bulletList.remove(b)

    # 显示敌机
    for e in enemyList:
        e.move()
        e.show()
        for b in e.bulletList:
            b.show()
            b.move()
            if b.y <= 0:
                e.bulletList.remove(b)

    # 判断敌机和子弹碰撞
    for b in plane.bulletList:
        for e in enemyList:
            if b.x <= e.x <= b.x + 50:
                if b.y <= e.y <= b.y + 50:
                    # 从新出现敌机
                    e.x = random.randint(25, 375)
                    e.y = random.randint(25, 150)

    # 循环检测事件
    for event in pygame.event.get():

        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            exit()

        # 添加键盘事件
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP: plane.d = 1
            if event.key == pygame.K_DOWN: plane.d = 2
            if event.key == pygame.K_LEFT: plane.d = 3
            if event.key == pygame.K_RIGHT: plane.d = 4
            if event.key == pygame.K_SPACE: plane.shot()

    pygame.time.wait(5)

    # 刷新画面
    pygame.display.update()