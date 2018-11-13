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
back = pygame.image.load("back.png")
font =pygame.font.SysFont("cn",80)
text_sur = font.render(u"你好",True,(0,0,255))

x = (SCREEN_SIZE[0] - text_sur.get_width())/2;
y = (SCREEN_SIZE[1] - text_sur.get_height())/2

#title
pygame.display.set_caption("test6-font")

while True:
    for event in pygame.event.get():        
        if event.type == locals.QUIT:
            exit()
    screen.blit(back,(0,0))

    x -= 2
    if x < -text_sur.get_width():
        x = SCREEN_SIZE[0] - text_sur.get_width() 

    screen.blit(text_sur,(x,y))
    pygame.display.update()
    time.sleep(0.025)
