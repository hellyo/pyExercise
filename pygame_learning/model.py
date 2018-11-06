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

while True:
    for event in pygame.event.get():        
        if event.type == locals.QUIT:
            exit()
time.sleep()
