import pygame
from main_window import *
from settings import *
from utils import *


class Button:
	def __init__(self, x, y, w, h, text, font_family, font_size, forecolor, backcolor1, backcolor2):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.text = text
		self.font = pygame.font.SysFont(font_family, font_size)
		self.font_size = font_size
		self.font_family = font_family
		self.forecolor = forecolor
		self.backcolor1 = backcolor1
		self.backcolor2 = backcolor2
		self.is_hidden = False
		self.is_enabled = True

	def draw(self, mouse_pos):
		if self.is_hidden:
			return
		if self.is_enabled:	
			if self.mouseOver(mouse_pos):
				self.setBackcolor(self.backcolor2)
			else:
				self.setBackcolor(self.backcolor1)
		else:
			self.setBackcolor(GRAY)	
		pygame.draw.rect(window, self.backcolor, (self.x, self.y, self.w, self.h))	
		txt = self.font.render(self.text, True, self.forecolor)	
		text_surf, text_rect = textObjects(self.text, self.forecolor, self.font_family, self.font_size)
		text_rect.center = (self.x + self.w / 2, self.y + self.h / 2)
		window.blit(txt, text_rect)

	def setBackcolor(self, backcolor):
		self.backcolor = backcolor
		
	def show(self):
		self.is_hidden = False
		
	def hide(self):
		self.is_hidden = True
		
	def enable(self):
		self.is_enabled = True
		
	def disable(self):
		self.is_enabled = False
		
	def isEnabled(self):
		return self.is_enabled
		
	def mouseClick(self, mouse_pos):
		if not self.is_enabled:
			return False
		x_axis = mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w
		y_axis = mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h
		return x_axis and y_axis
		
	def mouseOver(self, mouse_pos):
		if not self.is_enabled:
			return False
		x_axis = mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.w
		y_axis = mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.h
		return x_axis and y_axis
		