import pygame
from pygame import font

# 初始化硬件
pygame.init()
# 创建屏幕并设置尺寸
screen = pygame.display.set_mode([860, 640])

# 设置窗口标题
pygame.display.set_caption("我的游戏")

while True:
    # 绘制直线：屏幕 颜色 起点坐标 结束坐标 粗细
    pygame.draw.line(screen, [0, 255, 0], [10, 20], [80, 120], 4)
    # 绘制空心圆：屏幕 颜色 圆点坐标 半径 粗细
    pygame.draw.circle(screen, [255, 0, 0], [200, 200], 80, 4)

    # 绘制实心圆：去掉粗细就是实心的
    pygame.draw.circle(screen, [0, 0, 255], [300, 300], 100)

    # 绘制矩形:屏幕 颜色 ((顶点x坐标,顶点y坐标),(长度，宽度)) 粗细
    pygame.draw.rect(screen, [0, 255, 255], [[400, 400], [70, 100]], 2)
    # 绘制实心矩形:屏幕 颜色 ((顶点x坐标,顶点y坐标),(长度，宽度))
    pygame.draw.rect(screen, [255, 255, 0], [[200, 0], [80, 100]])
    # 绘制图片
    img = pygame.image.load("a.png")
    screen.blit(img, [550, 100])
    # 加载并绘制文字
    # 先查看字体：print(py.font.get_fonts())
    # print(pygame.font.get_fonts())
    font = pygame.font.SysFont('arial', 32)
    text = font.render('hello,python', True, [255, 255, 255])
    screen.blit(text, [150, 400])
    # 循环检测事件
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            exit()
    # 刷新画面
    pygame.display.update()
