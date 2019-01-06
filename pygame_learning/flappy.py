#!/usr/bin/env python3
#coding=utf-8
# pygame初探

import pygame
from pygame import locals
from sys import exit
import time

<<<<<<< HEAD
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
=======
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
>>>>>>> 8d2ca413ba7c9cea86cbd9f94dfcf79bd7fd4162
