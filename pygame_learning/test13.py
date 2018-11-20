#!/usr/bin/env python3
#coding=utf-8

# pygame.draw 方法

import pygame
from pygame.locals import *
from sys import exit
import time
 
pygame.init()
screen = pygame.display.set_mode((1024, 768), 0, 32)
screen.fill((255,255,255))
ball = pygame.image.load("ball.png").convert_alpha()
r = ball.get_size()[0]/2

stx = 512
sty = r
curx = stx
cury = sty
curtime = time.time()
lasttime = curtime
speed = 100
clock = pygame.time.Clock()
clock.tick(15)
while True:
    speed += 2
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    curtime = time.time()
    delta = curtime - lasttime
    lasttime = curtime
    cury += speed * delta
    if cury > 768 - r:
        speed = -speed * 0.9
        cury = 768 - r
    screen.fill((255,255,255))
    # pygame.draw.circle(screen,(0,0,255),(int(curx),int(cury)),r,1)
    screen.blit(ball,(int(curx - r),int(cury - r)))

    pygame.display.update()
    # time.sleep(0.025)