from constants import *


class Card:
	def __init__(self, symbol='-', value=0, suit=0):
		self.symbol = symbol
		self.value = value
		self.suit = suit
	
	def __str__(self):
		#return self.symbol + ',' + str(self.suit)
		return str(self.value) + SUIT_INDEX[self.suit]
		
	def set(self, string):
		item1 = string[0]
		item2 = string[1]
		self.symbol = item1
		self.suit = SUIT[item2]
		if item1 in DICT.keys():
			self.value = DICT[item1]
		else:
			self.value = int(item1)
			
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
		
