#!/usr/bin/env python3
#coding=utf-8
# pygame初探

import pygame
from pygame import locals
from sys import exit
import time

SCREEN_SIZE = (512,256)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
#title
pygame.display.set_caption("test1")

backImg = "back.png"
mouseImg = "mouse.png"

back = pygame.image.load(backImg) #.convert_alpha()
mouse = pygame.image.load(mouseImg)#.convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == locals.QUIT:
            exit()
    screen.blit(back,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= mouse.get_width()/2
    y -= mouse.get_height()/2

    screen.blit(mouse,(x,y))
    pygame.display.update()
    time.sleep(0.025)    

