from main_window import *


class CardImage:
	def __init__(self, card, x, y, w, h):
		self.card = card
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.visible = False
		self.chosen = False
		
	def is_visible(self):
		return self.visible

	def set_visible(self, value):
		self.visible = value

	def is_chosen(self):
		return self.chosen

	def set_chosen(self, value):
		self.is_chosen = value

	def reveal(self):
		self.visible = True
		
	def draw(self):
		# Draw card frame
		window.fill((240,240,240), rect=[self.x, self.y, self.w, self.h])