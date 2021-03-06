import pygame
import random

# 初始化硬件
pygame.init()

# 创建屏幕并设置尺寸
screen = pygame.display.set_mode([400, 600])

# 设置窗口标题
pygame.display.set_caption("飞机大战")


# 定义可移动物体的父类
class MoveObject:
    # 所有可移动物体都具有x坐标,y坐标,d方向和图片属性
    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0
        self.img = None

    # 定义所有可移动物体可以显示到屏幕上
    def show(self):
        pass

    # 定义所有可移动物体具有移动行为
    def move(self):
        pass


# 子弹类
class Bullet(MoveObject):
    # 横纵x,y坐标
    def __init__(self):
        self.img = pygame.image.load("bullet.png")

    # 重写子弹显示
    def show(self):
        screen.blit(self.img, [self.x, self.y])

    # 重写子弹移动
    def move(self):
        if self.d == 1: self.y -= 2
        if self.d == 2: self.y += 2


# 我方飞机类
class Plane(MoveObject):
    # 横纵x,y坐标;子弹属性
    def __init__(self):
        self.x = 200
        self.y = 500
        self.d = 0
        self.img = pygame.image.load("plane.png")
        self.bulletList = []

    # 重写飞机显示
    def show(self):
        screen.blit(self.img, [self.x, self.y])

    # 重写飞机移动
    def move(self):
        if self.d == 1: self.y -= 1
        if self.d == 2: self.y += 1
        if self.d == 3: self.x -= 1
        if self.d == 4: self.x += 1

    # 发射子弹
    def shot(self):
        # 创建并添加
        bullet = Bullet()
        bullet.x = self.x + 25
        bullet.y = self.y
        bullet.d = 1
        self.bulletList.append(bullet)


# 敌机类
class Enemy(MoveObject):
    # 横纵x,y坐标;子弹集合
    def __init__(self):
        self.x = 0
        self.y = 0
        self.d = 0
        self.img = pygame.image.load("enemy.png")
        # 敌机子弹集合
        self.bulletList = []

    # 敌机显示
    def show(self):
        screen.blit(self.img, [self.x, self.y])

    # 敌机移动
    def move(self):
        # 敌机下移动
        self.y += 1
        # 控制敌机左右移动
        if self.d == 3: self.x -= 1
        if self.d == 4: self.x += 1
        # 控制敌机改变方向
        if self.x <= 0: self.d = 4
        if self.x >= 400: self.d = 3
        # 敌机底部越界
        if self.y >= 600: self.y = 0
        # 敌机发射子弹
        if random.random() < 0.001:
            self.shot()

    # 发射子弹
    def shot(self):
        # 创建子弹并添加
        bullet = Bullet()
        bullet.x = self.x + 12
        bullet.y = self.y
        bullet.d = 2
        self.bulletList.append(bullet)


# 创建飞机类
plane = Plane()
# 敌机集合
enemyList = []
# 随机生成敌机
#游戏结束标志,0进行,1结束
flag=0
for i in range(1, 16):
    enemy = Enemy()
    enemy.x = random.randint(25, 375)
    enemy.y = random.randint(25, 150)
    if random.random() < 0.5:
        enemy.d = 3
    else:
        enemy.d = 4
    # 添加敌机到敌机集合
    enemyList.append(enemy)
# 游戏主逻辑
while True:

    # 清除屏幕
    screen.fill([0, 0, 0])
    # 显示飞机
    plane.show()
    if flag==0:
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
            b.move()
            b.show()
            if b.y <= 0:
                e.bulletList.remove(b)
    # 判断敌机和子弹碰撞
    for b in plane.bulletList:
        for e in enemyList:
            if b.x <= e.x <= b.x + 30:
                if b.y <= e.y <= b.y + 30:
                    # 重新出现敌机
                    e.x = random.randint(25, 375)
                    e.x = random.randint(25, 150)
    # 判断游戏结束
    for e in enemyList:
        for e_b in e.bulletList:
            if e_b.x-20<= plane.x+30 <= e_b.x + 20:
                if e_b.y-20<= plane.y+30 <= e_b.y + 20:
                    flag=1
    #游戏结束
    if flag==1:
        font = pygame.font.SysFont('arial', 50)
        text = font.render('Game Over!', True, [255, 0, 0])
        screen.blit(text, [100, 250])
    # 循环检测事件
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            exit()
        # 添加键盘事件,改变飞机移动方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: plane.d = 1
            if event.key == pygame.K_DOWN: plane.d = 2
            if event.key == pygame.K_LEFT: plane.d = 3
            if event.key == pygame.K_RIGHT: plane.d = 4
            if event.key == pygame.K_SPACE and flag==0: plane.shot()
    # 游戏延迟
    pygame.time.wait(5)
    # 屏幕更新
    pygame.display.update()
