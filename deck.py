from card import *
from hand import *
from settings import *
import random


class Deck:
	def __init__(self, packs=1):
		self.cards = []
		for i in range(packs):
			for suit in range(0, 4):
				for value in range(2, 15):
					symbol = CARD_SYMBOLS[value]
					card = Card(symbol, suit, 0, 0, CARD_WIDTH, CARD_HEIGHT)
					self.cards.append(card)
		
	def __len__(self):
		return len(self.cards)
		
	def isEmpty(self):
		return len(self.cards) == 0
		
	def swap(self, i, j):
		self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
	
	def shuffle(self):
		for i in range(len(self.cards)):
			j = random.randint(0, len(self.cards) - 1)
			self.swap(i, j)
		
	def get(self, index):
		return self.cards[index]
		
	def top(self):
		if len(self.cards) > 0:
			return self.cards[-1]
		return None
		
	def pop(self):
		return self.cards.pop()
		
	def pushFront(self, card):
		self.cards.insert(0, card)

	def show(self):
		for card in self.cards:
			print(card)
