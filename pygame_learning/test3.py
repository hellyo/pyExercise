#!/usr/bin/env python3
#coding=utf-8
# pygame初探

import pygame
from pygame.locals import *
from sys import exit
import time

backImg = "back.png"
SCREEN_SIZE = (512,256)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN,32)
#title
pygame.display.set_caption("test1")

back = pygame.image.load(backImg).convert_alpha()
x,y = 0,0
move_x,move_y = 0,0

while True:
	for event in pygame.event.get():        
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				exit()
			elif event.key == K_LEFT:
				move_x = -1
			elif event.key == K_RIGHT:
				move_x = 1
			elif event.key == K_UP:
				move_y = -1
			elif event.key == K_DOWN:
				move_y = 1
		elif event.type == KEYUP:
			move_x = move_y = 0
	x += move_x
	y += move_y
	screen.fill((0,0,0))
	screen.blit(back,(x,y))

	pygame.display.update()
	time.sleep(0.025)