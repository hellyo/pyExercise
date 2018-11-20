#!/usr/bin/env python3
#coding=utf-8

# AI 测试,有限状态机
import pygame
from pygame.locals import *
from pygame.math import Vector2

class GameEntity(object):
	def __init__(self,world,name,image):
		self.world = world
		self.name = name
		self.image = image
		self.location = Vector2(0,0)
		self.destination = Vector2(0,0)
		self.speed = 0
		self.brain = StateMachine()
		self.id = 0	
	
	def render(self,surface):
		x,y = self.location
		w,h = self.image.get_size()
		surface.blit(self.image,(x-w/2,y - h/2))

	def process(self,time_passed):
		self.brain.think()
		if self.speed > 0 and self.location != self.destination:
			vec_to_des = self.destination - self.location
			dis = vec_to_des.get_length()
			heading = vec_to_des.normalize()
			t_dis = min(dis,time_passed * self.speed)
			self.location += t_dis * heading


class World(object):
	def __init__(self):
		self.entities = {}
		self.entity_id = 0

		self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
		self.background.fill((255,255,255))
		pygame.draw.circle(self.background,(200,255,200),NEST_POSITION,int(NEST_SIZE))

	
	def add_entity(self,entity):
		self.entities[self.entity_id] = entity
		entity.id = self.entity_id
		self.entity += 1

	def remove_entity(self,entity):
		del self.entities[entity.id]

	def get(self,entity_id):
		if entity_id in self.entities:
			return self.entities[entity_id]
		else:
			return None

	def process(self,time_passed):
		time_passed_s = time_passed / 1000.0
		for e in self.entities.values():
			e.process(time_passed_s)
		
	def render(self,surface):
		surface.blit(self.background,(0,0))
		for e in self.entities.values():
			e.render(surface)
	
	def get_close_e(self,name,location,r=100):
		location = Vector2(*location)
		for e in self.entities.values():
			if e.name == name:
				dis = Vector2(location - e.location).length()
				if dis < r:
					return e
		return None
	
class Ant(GameEntity):
	#num = 0
	def __init__(self,world,image):		
		super.__init__(self,world,"ant",image)
		exploring_state = AntStateExploring()
		seeking_state = AntStateSeeking()
		delivering_state = AntStateDelivering()
		hunting_state = AntStateHunting()

		self.brain.add_state(exploring_state)
		self.brain.add_state(seeking_state)
		self.brain.add_state(delivering_state)
		self.brain.add_state(hunting_state)

		self.carry_image = None
	
	def carry(self,image):
		self.carry_image = image
	
	def drop(self,surface):
		if self.carry_image:
			x,y = self.location
			w,h = self.carry_image.get_size()
			surface.blit(self.carry_image,(x-w,y-h/2))
			self.carry_image = None
	
	def render(self,surface):
		super.render(self,surface)

		if self.carry_image:
			x,y = self.location
			w,h = self.carry_image.get_size()
			surface.blit(self.carry_image,(x-w,y-h/2))


class State(object):
	def __init__(self,name):
		self.name = name

	def do_actions(self):
		pass
	
	def check_condition(self):
		pass
	
	def entry_actions(self):
		pass
	
	def exit_actions(self):
		pass

class StateMachine(object):
	def __init__(self):
		self.states = {}
		self.active_state = None
	
	def add_state(self,state):
		self.states[state.name] = state
	
	def think(self):
		if self.active_state is None:
			return 
		self.active_state.do_actions()
		new_state_name = self.active_state.check_condition()
		if new_state_name is not None:
			self.set_state(new_state_name)
	
	def set_state(self,name):
		if self.active_state is not None:
			self.active_state.exit_actions()
		self.active_state == self.states[name]
		self.active_state.entry_actions()
	

			



		
	
	
			
		


			



