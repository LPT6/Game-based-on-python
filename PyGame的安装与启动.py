# 1.pygame简介
# pygame是python语言中最热门的一个游戏开发框架。
# pygame为游戏开发者提供了图形显示和事件交互等基本功能。
# pygame底层是基于OpenGL实现的
# 使用pygame之前先安装：
#
# pip install PyGame
# 2.pygame游戏框架
# 一个空白的游戏开发框架例子如下：
import pygame

# 初始化硬件
pygame.init()
# 创建屏幕并设置尺寸
screen = pygame.display.set_mode([640, 480])

# 设置窗口标题
pygame.display.set_caption("我的游戏")

while True:
    # 在这里实现你的游戏
    pass
    # 循环检测事件
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            exit()
    # 刷新画面
    pygame.display.update()
