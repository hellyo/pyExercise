#!/usr/bin/env python3
#coding=utf-8

SCREENSIZE = (640,480)
GRAVITY = 100.0   #单位是 像素/s^2
BOUN = 0.7

import pygame,sys,time
from pygame.locals import *
from random import randint
from pygame.math import Vector2

class Ball(pygame.sprite.Sprite):
	def __init__(self,color,position,image):
		self.position = Vector2(position)		
		self.image = image
		self.speed = Vector2(0,50)
		self.rect = self.image.fill(color,None,BLEND_ADD)
		self.rect.topleft = position
	
	def update(self,t):
		iw,ih = self.image.get_size()
		w,h = SCREENSIZE
		x,y = self.position

		if y+ih > h:
			self.speed.y = - self.speed.y * BOUN
			self.position.y = h - ih - 1
		elif y < 0:
			self.speed.y = -self.speed.y * BOUN
			self.position.y = ih + 1
		
		if x < 0:
			self.speed.x = -self.speed.x * BOUN
			self.position.x = 1

		elif x+iw > w:
			self.speed.x = -self.speed.x * BOUN
			self.position.x = w - iw / 2 - 1

		self.position += self.speed * t
		self.speed.y += t * GRAVITY	
		self.rect.x = self.position.x
		self.rect.y = self.position.y

def run():
	pygame.init()
	screen = pygame.display.set_mode(SCREENSIZE,0)

	ball = pygame.image.load("ball.png").convert_alpha()
	clock = pygame.time.Clock()

	balls = []
	while True:
		
		for evt in pygame.event.get():
			if evt.type == QUIT:
				sys.exit()
				return 
			if evt.type == MOUSEBUTTONDOWN:				
				new_ball = Ball((255,0,0),evt.pos,ball)
				balls.append(new_ball)
						
			screen.fill((255,255,255))
			time_pass = clock.tick()
			dead = []
			
			for b in balls:			
				b.update(time_pass/1000)
				screen.blit(b.image,b.rect)
			
			
			pygame.display.update()
			# time.sleep(0.01)

if __name__ == "__main__":
	run()

