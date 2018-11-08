#!/usr/bin/env python3
#coding=utf-8
# pygame字体

import pygame
from pygame import locals
from sys import exit
import time

SCREEN_SIZE = (512,256)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)

all_colors = pygame.Surface((4096,4096),depth=24)

for r in range(256):
    x = (r&15) * 256
    y = (r>>4) * 256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g,y+b),(r,g,b))
pygame.image.save(all_colors,"color.bmp")
print("done!!")
