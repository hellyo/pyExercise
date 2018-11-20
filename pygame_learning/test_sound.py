#!/usr/bin/env python3
#coding=utf-8

SCREENSIZE = (640,480)
GRAVITY = 250.0   #单位是 像素/s^2
BOUN = 0.7


import pygame 
from pygame.locals import *
from random import randint
from pygame.math import Vector2

def stero_pan(x_coord,w):
    rv = float(x_coord)/w
    lv = 1 - rv
    return (lv,rv)

class Ball(object):
    def __init__(self,position,speed,image,b_sound):
        self.position = Vector2(position)
        self.speed = Vector2(speed)
        self.image = image
        self.b_sound = b_sound
        self.age = 0.0
    
    def update(self,t):
        iw,ih = self.image.get_size()
        w,h = SCREENSIZE

        x,y = self.position
        x -= iw/2
        y -= ih/2

        bounce = False

        if y+ih >= h:
            self.speed.y = - self.speed.y * BOUN
            self.position.y = h - ih/2 - 1
            bounce = True
        
        if x <= 0:
            self.speed.x = -self.speed.x * BOUN
            self.position.x = iw / 2 + 1
            bounce = True
        elif x+iw >= w:
            self.speed.x = -self.speed.x * BOUN
            self.position.x = w - iw / 2 - 1
            bounce = True
        
        self.position += self.speed * t

        self.speed .y += t * GRAVITY

        if bounce:
            self.play()
        
        self.age += t

    def play(self):
        channel = self.b_sound.play()

        if channel is not None:
            l,r = stero_pan(self.position.x,SCREENSIZE[0])
        
    def render(self,surface):
        w,h = self.image.get_size()
        x,y = self.position
        x -= w/2
        y -= h/2
        surface.blit(self.image,(x,y))

def run():
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.init()
    pygame.mixer.set_num_channels(8)
    screen = pygame.display.set_mode(SCREENSIZE,0)

    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()

    ball = pygame.image.load("ball.png").convert_alpha()
    mouse = pygame.image.load("mouse.png").convert_alpha()

    sound = pygame.mixer.Sound("bounce.ogg")

    balls = []

    while True:
        for evt in pygame.event.get():
            if evt.type == QUIT:
                return 
            if evt.type == MOUSEBUTTONDOWN:
                random_speed = (randint(-400,400),randint(-300,0))
                new_ball = Ball(evt.pos,random_speed,ball,sound)
                balls.append(new_ball)
            
            time_passed_s = clock.tick()/1000.0
            screen.fill((255,255,255))

            dead = []
            for b in balls:
                b.update(time_passed_s)
                b.render(screen)
                if b.age > 10.0:
                    dead.append(b)
            for ball in dead:
                balls.remove(ball)
            
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(mouse,mouse_pos)
            pygame.display.update()
            # pygame.time.wait(25)

if __name__ == "__main__":
    run()








            

        


