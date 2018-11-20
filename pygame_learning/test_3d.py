#!/usr/bin/env python3
#coding=utf-8

import pygame
from pygame.locals import *
from pygame.math import Vector3

from math import *
from random import randint
import sys

SCREEN_SIZE = (640,480)
CUBE_SIZE = 300

def cal_view_dis(fov,screen_width):
	d = (screen_width/2.0)/tan(fov/2.0)
	return d

def run():
	pygame.init()
	screen = pygame.display.set_mode(SCREEN_SIZE,0)
	
	font = pygame.font.SysFont(pygame.font.get_default_font(),24)
	
	ball = pygame.image.load("mouse.png").convert_alpha()
	
	points = []

	fov = 90
	vd = cal_view_dis(fov,SCREEN_SIZE[1])
	
	for x in range(0,CUBE_SIZE+1,30):
		edge_x = x == 0 or x == CUBE_SIZE
		for y in range(0,CUBE_SIZE+1,30):
			edge_y = y == 0 or y == CUBE_SIZE
			for z in range(0,CUBE_SIZE + 1,30):
				edge_z = z == 0 or z == CUBE_SIZE
					
				if sum((edge_x,edge_y,edge_z)) >= 2:
					
					px = float(x) - CUBE_SIZE/2
					py = float(y) - CUBE_SIZE/2
					pz = float(z) - CUBE_SIZE/2
					points.append(Vector3(px,py,pz))


	def point_z(point):
		return point.z
	points.sort(key=point_z,reverse=True)
	cx,cy = SCREEN_SIZE
	cx /= 2
	cy /= 2
	
	bw,bh = ball.get_size()
	bcx = bw/2	
	bcy = bh/2
	
	camera_p = Vector3(0,0,-600)
	camera_speed = Vector3(0,0,300)     #初始速度

	clock = pygame.time.Clock()
	while True:
		for evt in pygame.event.get():
			if evt.type == QUIT:
				sys.exit()

		screen.fill((0,0,0))
		pressedKey = pygame.key.get_pressed()
		time_passed = clock.tick()/10000.

		direction = Vector3()   #加速度
		if pressedKey[K_LEFT]:
			direction.x = -1.0

		if pressedKey[K_RIGHT]:
			direction.x = +1.0
		
		if pressedKey[K_UP]:
			direction.y = +1.0

		if pressedKey[K_DOWN]:
			direction.z = -1.0

		if pressedKey[K_q]:
			direction.z = +1.0

		if pressedKey[K_a]:
			direction.z = -1.0

		if pressedKey[K_w]:
			fov = min(179,fov+1)
			w = SCREEN_SIZE[1]
			vd = cal_view_dis(fov,w)
				
		if pressedKey[K_s]:
			fov = min(179,fov+1)
			w = SCREEN_SIZE[1]
			vd = cal_view_dis(fov,w)
		
		tmp = Vector3(0,0,0)
		# s = vt + 0.5 * at^2
		tmp.x = camera_speed.x * time_passed + 0.5 * direction.x * time_passed ** 2 
		tmp.y = camera_speed.y * time_passed + 0.5 * direction.y * time_passed ** 2 
		tmp.z = camera_speed.z * time_passed + 0.5 * direction.z * time_passed ** 2 
		camera_p += (tmp.x,tmp.y,tmp.z)

		for p in points:
			x,y,z = p - camera_p
			if z > 0:
				x = x * vd / z
				y = -y * vd / z
				x += cx
				y += cy
				screen.blit(ball,(x-bcx,y-bcy))
		
		# dw = SCREEN_SIZE[0]/4
		# col = (50,255,50)
		# dp = []
		# dp.append((dw/2,100+vd/4))
		# dp.append((0,100))
		# dp.append((dw,100))
		# dp.append((dw/2,100+vd/4))
		# dp.append((dw/2,100))
		# pygame.draw.lines(screen,col,False,dp,2)

		# w = (255,255,255)

		# cam_t = font.render("camera = " + str(camera_p),True,w)
		# screen.blit(cam_t,(5,5))
		# fov_t = font.render("field of view = " + str(vd),True,w)
		# screen.blit(fov_t,(5,35))

		# t = "vd = %.3f" % vd
		# tt = font.render(t,True,w)
		# screen.blit(tt,(5,65))
		pygame.display.update()
		pygame.time.wait(40)

if __name__ == "__main__":
	run()
		
