#!/usr/bin/env python3
#coding=utf-8
# pygame事件初探

import pygame
from pygame import locals
from sys import exit
import time

SCREEN_SIZE = (512,1024)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
#title
pygame.display.set_caption("test2")

font = pygame.font.SysFont("arial",16)
f_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))

    if len(event_text) >= SCREEN_SIZE[1]/f_height:
        event_text = event_text[-int(SCREEN_SIZE[1]/f_height)-1:]
    
    if event.type == locals.QUIT:
        exit("aaa")
    screen.fill((0,0,0))
    y = SCREEN_SIZE[1] - f_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y -= f_height
    pygame.display.update()
    time.sleep(0.025)

