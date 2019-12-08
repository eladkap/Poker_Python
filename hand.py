from settings import *


class Hand:
	def __init__(self, x, y, player):
		self.cards = []
		self.x = x
		self.y = y
		self.player = player
		
	def __str__(self):
		s = ''
		for card in self.cards:
			s += str(card) + ' '
		return s
		
	def __len__(self):
		return len(self.cards)
		
	def addCard(self, card, to_reveal):
		if to_reveal:
			card.reveal()
		self.cards.append(card)
		
	def insertCard(self, card, index, to_reveal=True):
		if to_reveal:
			card.reveal()
		self.cards.insert(index, card)
		
	def getCard(self, index):
		return self.cards[index]
		
	def popCard(self):
		return self.cards.pop()
		
	def removeCard(self, index):
		return self.cards.pop(index)
		
	def sort(self):
		self.cards.sort()
	
	def display(self):
		x = self.x
		y = self.y
		for card in self.cards:
			card.x = x
			card.y = y;
			card.draw()
			x += CARD_WIDTH + SPACE_BETWEEN_CARDS

	def isFlush(self):
		suits_hist = [0] * 5
		for card in self.cards:
			suits_hist[card.suit] += 1
		return 5 in suits_hist
		
	def isStraight(self):
		values = [card.value for card in self.cards]
		values.sort()
		for i in range(len(values) - 1):
			if values[i] != values[i + 1] - 1:
				return False
		return True
		
	def isRoyal(self):
		values = [card.value for card in self.cards]
		return self.isStraight() and max(self.getValues()) == 14		
	
	def getValues(self):
		return [card.value for card in self.cards]	
	
	def getValueOf(self, count):
		values_hist = [0] * 15
		values = []
		for card in self.cards:
			values_hist[card.value] += 1
		for i in range(len(values_hist)):
			if values_hist[i] == count:
				values.append(i)
		return max(values)
				
	def rank(self):
		values_hist = [0] * 15
		suits_hist = [0] * 5
		for card in self.cards:
			values_hist[card.value] += 1
			suits_hist[card.suit] += 1
			
		# Four of a kind
		if 4 in values_hist:
			return 8, CARD_SYMBOLS[self.getValueOf(4)], self.getValueOf(4)
			
		# Full house
		if 3 in values_hist and 2 in values_hist:
			return 7, CARD_SYMBOLS[self.getValueOf(3)], self.getValueOf(3)
			
		# Three of a kind
		if 3 in values_hist:
			return 4, CARD_SYMBOLS[self.getValueOf(3)], self.getValueOf(3)
			
		# Two pair
		if values_hist.count(2) == 2:
			return 3, CARD_SYMBOLS[self.getValueOf(2)], self.getValueOf(2)
			
		# Pair
		if values_hist.count(2) == 1:
			return 2, CARD_SYMBOLS[self.getValueOf(2)], self.getValueOf(2)
			
		if self.isRoyal() and self.isFlush():
			return 10, CARD_SYMBOLS[max(self.getValues())], max(self.getValues())
		
		# Straight Flush
		if self.isStraight() and self.isFlush():
			return 9, CARD_SYMBOLS[max(self.getValues())], max(self.getValues())
			
		# Straight
		if self.isStraight():
			return 5, CARD_SYMBOLS[max(self.getValues())], max(self.getValues())
			
		# Flush
		if self.isFlush():
			return 6, CARD_SYMBOLS[max(self.getValues())], max(self.getValues())
		
		# High card
		return 1, CARD_SYMBOLS[max(self.getValues())], max(self.getValues())
		