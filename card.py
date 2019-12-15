from settings import *
from main_window import *
from utils import *


class Card:
	def __init__(self, symbol, suit, x, y, w, h):
		self.symbol = symbol
		self.value = CARD_VALUES[symbol]
		self.suit = suit
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.visible = False
		self.is_chosen = False
	
	def __str__(self):
		return CARD_SYMBOLS[self.value] + CARD_SUITS[self.suit]
		
	def set(self, symbol, value, suit):
		self.symbol = symbol
		self.value = value
		self.suit = suit
			
	def __eq__(other):
		return self.value == other.value
		
	def __lt__(self, other):
		return self.value < other.value
			
	def __gt__(self, other):
		return self.value > other.value
	
	def __lte__(self, other):
		return self.value <= other.value
			
	def __gte__(self, other):
		return self.value >= other.value
		
	def isVisible(self):
		return self.visible

	def setVisible(self, value):
		self.visible = value

	def isChosen(self):
		return self.is_chosen

	def setChosen(self, value):
		self.is_chosen = value

	def reveal(self):
		self.visible = True
		
	def draw(self):
		# Draw card frame
		if self.is_chosen:
			window.fill(AQUA, rect=[self.x, self.y, self.w, self.h])
		else:
			window.fill(CARD_BACKGROUND, rect=[self.x, self.y, self.w, self.h])
		
		if self.visible:
			font_color = ((self.suit % 2 == 1) * 255, 0, 0)
			showText(self.symbol, [self.x + 2, self.y], font_color, FONT_FAMILY1, CARD_FONT_SIZE, False, 0)
			showText(CARD_SUITS[self.suit], [self.x + 2, self.y + CARD_FONT_SIZE], font_color, FONT_FAMILY1, CARD_FONT_SIZE, False, 0)
			showText(CARD_SUITS[self.suit], [self.x + self.w - 18, self.y + self.h - CARD_FONT_SIZE * 2], font_color, FONT_FAMILY1, CARD_FONT_SIZE, False, 0)
			showText(self.symbol, [self.x + self.w - 18, self.y + self.h - CARD_FONT_SIZE], font_color, FONT_FAMILY1, CARD_FONT_SIZE, False, 0)
			# center suit
			showText(CARD_SUITS[self.suit], [self.x + self.w / 2 - CARD_FONT_SIZE / 2, self.y + self.h / 2 - CARD_FONT_SIZE / 2],font_color, FONT_FAMILY1, CARD_FONT_SIZE, False, 0)
		
	def isClicked(self, click_pos):
		x = click_pos[0]
		y = click_pos[1]
		return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h
