import random

import pygame

# 初始化硬件
pygame.init()
# 创建屏幕并设置尺寸
screen = pygame.display.set_mode([400, 400])
# 设置窗口标题
pygame.display.set_caption("扫雷")


while True:
    # 循环检测事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
