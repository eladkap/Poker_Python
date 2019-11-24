from card import *
from constants import *
import random


class Deck:
	def __init__(self):
		self.cards = []
		for suit in range(1, 5):
			for value in range(2, 15):
				if value >= 11:
					symbol = FACE[value]
				else:
					symbol = str(value)
				card = Card(symbol, value, suit)
				self.cards.append(card)
		
	def __len__(self):
		return len(self.cards)
		
	def swap(self, i, j):
		self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
	
	def shuffle(self):
		for i in range(len(self.cards)):
			j = random.randint(0, len(self.cards) - 1)
			self.swap(i, j)
		
	def get(self, index):
		return self.cards[index]

	def show(self):
		for card in self.cards:
			print(card)
