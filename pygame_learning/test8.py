#!/usr/bin/env python
# 调色盘 
import pygame
from pygame.locals import *
from sys import exit
import time
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

def getColorBar(height):
    r_bar = pygame.surface.Surface((640,height))
    g_bar = pygame.surface.Surface((640,height))
    b_bar = pygame.surface.Surface((640,height))

    for x in range(640):
        val = int((x/640) * 255)   
        r = (val,0,0)
        g = (0,val,0)
        b = (0,0,val)

        rect = Rect(x,0,1,height)
        pygame.draw.rect(r_bar,r,rect)
        pygame.draw.rect(g_bar,g,rect)
        pygame.draw.rect(b_bar,b,rect)
    
    return r_bar,g_bar,b_bar

r_ctrl,g_ctrl,b_ctrl = getColorBar(80)



c = [0,0,0]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
 
    screen.fill((0,0,0))
    screen.blit(r_ctrl,(0,0))
    screen.blit(g_ctrl,(0,80))
    screen.blit(b_ctrl,(0,160))
    
    x,y = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0]:   #左键被按下
        for i in range(3):
            if  i*80 < y < (i+1) * 80:
                c[i] = int((x/640) * 255)
    for i in range(3):
        pygame.draw.circle(screen,(255,255,255),(int((c[i]/255) * 640),i * 80 + 40),10)

    pygame.draw.rect(screen,(c),Rect(0,240,640,240))
    pygame.display.set_caption(str(c))
    pygame.display.update()
    time.sleep(0.025)