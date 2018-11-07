#!/usr/bin/env python3
#coding=utf-8
# pygame切换窗口大小

import pygame
from pygame import locals
from sys import exit
import time

backImg = "back.png"

SCREEN_SIZE = (512,256)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
back = pygame.image.load(backImg)
#title
FullScreen = False
pygame.display.set_caption("test4")

while True:
    for event in pygame.event.get():        
        if event.type == locals.QUIT:
            exit()
        if event.type == locals.KEYDOWN:
            if event.key == locals.K_f:
                FullScreen = not FullScreen
            if FullScreen:
                screen = pygame.display.set_mode(SCREEN_SIZE,locals.FULLSCREEN,0)
            else:
                screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
    screen.blit(back,(0,0))
    pygame.display.update()
    time.sleep(0.025)
