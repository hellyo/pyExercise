#!/usr/bin/env python3
#coding=utf-8

import pygame
from pygame.locals import *
from sys import exit

SCREEN_SIZE = (480,640)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption("just a title")

font = pygame.font.SysFont("arial",16)
font_height = font.get_linesize()
txt = []

while True:
    print("bb")
    event = pygame.event.wait()
    print("aa")
    print(event)
    txt.append(str(event))
    txt = txt[-int(SCREEN_SIZE[1]/font_height):]
    
    if event.type == pygame.QUIT:
            exit()
    screen.fill((255,255,255))
    y = SCREEN_SIZE[1] - font_height
    for text in reversed(txt):
        screen.blit(font.render(text,True,(0,0,0)),(0,y))
        y -= font_height
    
    pygame.display.update()

