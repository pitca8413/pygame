# 1024 x 600 크기의 창 만들기

import pygame, time

# 파이 게임 초기화 및 창 생성하기
pygame.init()
width, height = 1024, 600
size = (width, height)
screen = pygame.display.set_mode(size)

# 창 2초간 유지하기
pygame.draw.rect(screen, (200, 200, 200), [10, 10, 500, 50], 2)
pygame.display.flip()

time.sleep(2)