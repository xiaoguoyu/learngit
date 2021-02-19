import pygame
from sys import exit
from time import sleep

RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]


def set_text(screen, x, y, width, high, text):
    ft = pygame.font.SysFont("Bell MT", min(width, high) // 3)  # 设置字体和字号（字号设置小一点不然地儿不够）
    t = ft.render(text, True, (123, 123, 123))
    screen.blit(t, (x, y + high / 3))  # 放在button的大概中间


def update(color, screen, x, y, width, high, text):
    pos = (x, y, width, high)
    if color == "red":
        pygame.draw.rect(screen, RED, pos, 0)
        set_text(screen, x, y, width, high, text)
        pygame.display.update()
        return True
    elif color == "green":
        pygame.draw.rect(screen, GREEN, pos, 0)
        set_text(screen, x, y, width, high, text)
        pygame.display.update()
        return True
    else:
        pygame.draw.rect(screen, BLUE, pos, 0)
        set_text(screen, x, y, width, high, text)
        pygame.display.update()
        sleep(0.05)  # 让人看到蓝色效果
        update("green", screen, x, y, width, high, text)
        return False


def set_button(screen, x, y, width, high, text):
    global pos, greened, reded, isin
    pos = (x, y, width, high)
    isin = False  # 鼠标是否在button内
    reded = False  # 是否已经填充了红色
    greened = False  # 同理
    if (event.type == pygame.MOUSEBUTTONDOWN) and (x < pygame.mouse.get_pos()[0] < x + width) and (
            y < pygame.mouse.get_pos()[1] < y + high):  # 鼠标点击并在button内button变成蓝色
        greened = update("blue", screen, x, y, width, high, text)
    elif (x < pygame.mouse.get_pos()[0] < x + width) and (y < pygame.mouse.get_pos()[1] < y + high) and (
            not greened):
        greened = update("green", screen, x, y, width, high, text)
    elif (not isin) and (not reded):  # 红色是普通状态
        reded = update("red", screen, x, y, width, high, text)
        isin = True
    elif (not ((x < pygame.mouse.get_pos()[0] < x + width) and (y < pygame.mouse.get_pos()[1] < y + high))) and (
    not reded):
        isin = False
        reded = False


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode([350, 350])
    screen.fill((255, 255, 255))
    while True:
        for event in pygame.event.get():
            for i in range(2):
                for j in range(2):
                    if event.type == pygame.QUIT:
                        exit(0)
                    x = i * 150
                    y = j * 150
                    width = 150
                    high = 150
                    text = "button"
                    set_button(screen, x, y, width, high, text)
            x = 300
            y = 0
            width = 50
            high = 300
            text = "button"
            set_button(screen, x, y, width, high, text)
            x, y = y, x
            width, high = high, width
            set_button(screen, x, y, width, high, text)
            set_button(screen, 300, 300, 50, 50, text)
