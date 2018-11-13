#!/usr/bin/env python
# 圆形调色盘 
import pygame
from pygame.locals import *
from sys import exit
import time
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.fill((0,0,0))




    pygame.draw.rect(screen,(c),Rect(0,240,640,240))
    pygame.display.set_caption(str(c))
    pygame.display.update()
    time.sleep(0.025)