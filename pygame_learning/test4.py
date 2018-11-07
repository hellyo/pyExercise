#!/usr/bin/env python3
#coding=utf-8
# pygame拖动窗口大小

import pygame
from pygame import locals
from sys import exit
import time

backImg = "back.png"

SCREEN_SIZE = (512,256)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,locals.RESIZABLE,32)
back = pygame.image.load(backImg)
#title
FullScreen = False
pygame.display.set_caption("test4")

while True:
    event = pygame.event.wait()      
    if event.type == locals.QUIT:
        exit()
    if event.type == locals.VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE,locals.RESIZABLE,32)
        pygame.display.set_caption("resized to " + str(event.size))
    w,h = SCREEN_SIZE
    for y in range(0,h,back.get_height()):
        for x in range(0,w,back.get_width()):
            screen.blit(back,(x,y))
    pygame.display.update()
    time.sleep(0.025)
