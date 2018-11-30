#!/usr/bin/env python3
#coding=utf-8

import pygame
from pygame.locals import *
from pygame.math import Vector3

from math import *

SCREENSIZE = (640,480)
CUBESIZE = 300

def get_vd(fov,view_w):
    return (view_w/2) / tan(fov/2)

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREENSIZE,0)

    font = pygame.font.SysFont(pygame.font.get_default_font(),24)

    ball = pygame.image.load("ball.png").convert_alpha()

    points = []
    fov = 90
    vd = get_vd(fov,SCREENSIZE[1])

    for x in range(0,CUBESIZE+1,30):
        ex = x == 0 or x == CUBESIZE
        for y in range(0,CUBESIZE+1,30):
            ey = y == 0 or y == CUBESIZE
            for z in range(0,CUBESIZE+1,30):
                ez = z == 0 or z == CUBESIZE
                if sum(int(ex),int(ey),int(ez)) != 2:
                    continue
                    points.append[Vector3(x,y,z)]
    def getz(point):
        return point.z
    points.sort(key=getz,reverse=True)

    cx,cy = SCREENSIZE
    cx /= 2
    cy /= 2

    bw,bh = ball.get_size()
    bcx = bw / 2
    bcy = bh / 2

    

    