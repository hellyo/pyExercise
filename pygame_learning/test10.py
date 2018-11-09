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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            button = pygame.mouse.get_pressed()
            if button[0]:
                pygame.draw.circle(screen,(0,0,255),pos,50)
                pygame.draw.arc(screen,(0,0,0),Rect(pos[0] - 50,pos[1] - 50,100,100),0,360,2)
            if button[2]:
                l,t,w,h = pos[0]-25,pos[1] - 25,50,50
                pygame.draw.rect(screen,(255,0,0),Rect(l,t,w,h))
                pygame.draw.lines(screen,(0,0,0),True,[(l,t),(l,t+h),(l+w,t+h),(l+w,t)],2)
            if button[1]:
                screen.fill((255,255,255))
        

    pygame.display.update()
    time.sleep(0.025)