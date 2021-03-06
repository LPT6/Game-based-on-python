import pygame

# 初始化硬件
pygame.init()

# 创建屏幕
screen = pygame.display.set_mode([400, 400])

# 设置窗口标题
pygame.display.set_caption("五子棋")


# 绘制棋盘
def drawGird():
    i = 0
    while i <= 400:
        pygame.draw.line(screen, [0, 0, 0], [0, i], [400, i], 1)
        pygame.draw.line(screen, [0, 0, 0], [i, 0], [i, 400], 1)
        i = i + 20


# 点亮第x行y列个圆形
def drawCir(x, y, color):
    #  绘制实心圆形：屏幕，颜色，圆点坐标，半径
    pygame.draw.circle(screen, color, [(y - 1) * 20, (x - 1) * 20], 10)


# 步骤数目
step = 1

# 背景颜色
screen.fill([204, 102, 51])

# 绘制棋盘
drawGird()

# 游戏主循环
while True:

    # 循环检测事件
    for event in pygame.event.get():

        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            exit()

        # 鼠标事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 获取屏幕坐标
            x, y = pygame.mouse.get_pos()

            print("鼠标按下坐标：", x, " ", y)
            # 屏幕坐标转方块坐标
            x = int((pygame.mouse.get_pos()[1] ) / 20)+1
            y = int((pygame.mouse.get_pos()[0] ) / 20)+1
            print("点击方块位置：", x, " ", y)

            # 左键单击
            if pygame.mouse.get_pressed()[0] == 1:

                # 黑色先手，黑白轮下
                color = [0, 0, 0]
                if step % 2 == 0:
                    color = [255, 255, 255]
                drawCir(x, y, color)
                step = step + 1

    # 刷新画面
    pygame.display.update()