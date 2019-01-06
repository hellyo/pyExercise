#!/usr/bin/env python3
#coding=utf-8
# pygame初探

import pygame
from pygame import locals
from sys import exit
import time

def setup(w,h):
    SCREEN_SIZE = (w,h)
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE,0,32)    
    pygame.display.set_caption("test1")
    clock = pygame.time.Clock()
    clock.tick(15)

def run():
    pass
    # while True:
    #     for event in pygame.event.get():        
    #     if event.type == locals.QUIT:
    #         exit()









if __name__ == "__main__":
    pass
