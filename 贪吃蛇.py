import pygame
import random

# 初始化
pygame.init()
# 屏幕大小
screen = pygame.display.set_mode([501, 501])
# 游戏名字
pygame.display.set_caption("RetroSnaker")


# 食物类
class Food:
    def __init__(self):
        # 食物初始化在12行12列位置
        self.x = 12
        self.y = 12

    def show(self):
        drawRect(self.x, self.y)


# 蛇类
class Snake:
    def __init__(self):
        # 蛇的身体坐标集合；以第一个元素为蛇头
        self.body_x = [5, 6, 7, 8, 9]
        self.body_y = [9, 9, 9, 9, 9]
        # 长度
        self.len = 5
        # 方向1234代表上下左右
        self.d = 1

    # 显示到屏幕
    def show(self):
        for i in range(0, len(self.body_x)):
            drawRect(self.body_x[i], self.body_y[i])

    def move(self):

        # 1.先保存原来的头
        x, y = self.body_x[0], self.body_y[0]
        # 2.头再动
        if self.d == 1: self.body_x[0] -= 1
        if self.d == 2: self.body_x[0] += 1
        if self.d == 3: self.body_y[0] -= 1
        if self.d == 4: self.body_y[0] += 1
        # 3.身子跟着动
        # 原来身子除身子的第一个小方格外的后部分,接替原来是身子的部分 i=4,3,2最前的小方格
        for i in range(self.len - 1, 0, -1):
            self.body_x[i] = self.body_x[i - 1]
            self.body_y[i] = self.body_y[i - 1]
        # 原来身子的第一个小方格,接替原来的头
        self.body_x[1], self.body_y[1] = x, y
        print(self.body_x)
        print(self.body_y)

    # 吃食物
    def eat(self, food):
        self.body_x.append(food.x)
        self.body_y.append(food.y)
        self.len += 1


a = 0


# 游戏结束检测
def checkGameOver(snake):
    global flag
    # 是否撞墙
    if snake.body_x[0] > 25 or snake.body_x[0] < 1 or snake.body_y[0] > 25 or snake.body_y[0] < 1:
        # 设置游戏结束
        print("撞墙")
        flag = 1
    # 是否被咬死
    if snake.len > 5:
        for i in range(3, snake.len - 1):
            if snake.body_x[0] == snake.body_x[i]:
                if snake.body_y[0] == snake.body_y[i]:
                    # 设置游戏结束
                    flag = 1
                    print("被咬死")
                    break


# 绘制网格
def drawGird():
    i = 0
    while i <= 400:
        pygame.draw.line(screen, [0, 0, 0], [0, i], [400, i], 1)
        pygame.draw.line(screen, [0, 0, 0], [i, 0], [i, 400], 1)
        i += 20


# 点亮第x行y列的小方块
def drawRect(x, y):
    pygame.draw.rect(screen, [200, 200, 200], [[(y - 1) * 20 + 1, (x - 1) * 20 + 1], [19, 19]])


# 创建蛇
snake = Snake()
# 创建食物
food = Food()
# 游戏状态标志，0进行1结束
flag = 0
# 游戏开始延迟次数
i = 6

while True:
    # 屏幕清楚：把屏幕涂黑
    screen.fill([0, 0, 0])
    # 绘制网格
    drawGird()
    # 绘制蛇
    snake.show()
    # 食物显示
    food.show()
    # 游戏结束检测
    checkGameOver(snake)
    # 判断游戏是否
    if flag == 1:
        # 弹出游戏结束提示
        font = pygame.font.SysFont('arial', 40)
        text = font.render('Game Over!', True, [255, 0, 0])
        screen.blit(text, [160, 220])
        pygame.display.update()
    # 蛇移动
    else:
        # 游戏未结束蛇继续移动
        snake.move()

    # 判断蛇吃食物
    if snake.body_x[0] == food.x:
        if snake.body_y[0] == food.y:
            print("吃到食物了")
            snake.eat(food)
            # 新的食物随机出现
            food.x = random.randint(1, 24)
            food.y = random.randint(1, 24)
    # 循环接收事件
    for event in pygame.event.get():
        # 退出
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            # 修改蛇的方向
            if event.key == pygame.K_UP and snake.d != 2: snake.d = 1
            if event.key == pygame.K_DOWN and snake.d != 1: snake.d = 2
            if event.key == pygame.K_LEFT and snake.d != 4: snake.d = 3
            if event.key == pygame.K_RIGHT and snake.d != 3: snake.d = 4

    # 游戏延迟
    if (snake.len > 6):
        pygame.time.wait(10000)
    if (snake.len <= 15):
        pygame.time.wait(100)
    else:
        # 长度达到15,蛇成年,其移动速度跟其长度线性相关
        if 100 - int(snake.len / 2)>10:
            pygame.time.wait(100 - int(snake.len / 2))
    # 游戏界面更新
    pygame.display.update()
    # 游戏开始延迟
    if i > 0:
        pygame.time.wait(40 + i * 30)
        i -= 1
