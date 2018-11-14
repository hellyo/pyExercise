#!/usr/bin/env python3
#coding=utf-8

background_image_filename = 'back.png'
sprite_image_filename = 'mouse.png'
 
import pygame,time
from pygame.locals import *
from sys import exit
from pygame.math import Vector2
 
pygame.init()
 
screen = pygame.display.set_mode((1280, 960), 0, 32)
 
#background = pygame.image.load(background_image_filename).convert()
background = pygame.surface.Surface((1280,960)).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()
 
clock = pygame.time.Clock()
 
position = Vector2(100.0, 100.0)
heading = Vector2()
 
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    background.fill((0,0,0))
    screen.blit(background, (0,0),)
    screen.blit(sprite, position)
 
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
 
    # 参数前面加*意味着把列表或元组展开
    destination = Vector2( *pygame.mouse.get_pos() ) - Vector2( *sprite.get_size() )/2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2(destination.x-position.x, destination.y - position.y)
    # 向量规格化
    vector_to_mouse.normalize()
 
    # 这个heading可以看做是鱼的速度，但是由于这样的运算，鱼的速度就不断改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动。
    heading = heading + vector_to_mouse * 0.6
    #print(vector_to_mouse.x,vector_to_mouse.y,heading.x,heading.y)
    position += heading * time_passed_seconds

    pygame.display.update()
    time.sleep(0.025)
