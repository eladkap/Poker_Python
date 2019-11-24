class Hand:
	def __init__(self):
		self.cards = []
		
	def __str__(self):
		s = ''
		for card in self.cards:
			s += str(card) + ' '
		return s
		
	def add(self, card):
		self.cards.append(card)
		
	def sort(self):
		self.cards.sort()
	
	def is_flush(self):
		suits_hist = [0] * 5
		for card in self.cards:
			suits_hist[card.suit] += 1
		return 5 in suits_hist
		
	def is_straight(self):
		values = [card.value for card in self.cards]
		values.sort()
		for i in range(len(values) - 1):
			if values[i] != values[i + 1] - 1:
				return False
		return True
		
	def is_royal(self):
		values = [card.value for card in self.cards]
		return self.is_straight() and max(self.get_values()) == 14
		
	
	def get_values(self):
		return [card.value for card in self.cards]
		
	
	def get_value_of(self, count):
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
			return 8, self.get_value_of(4)
			
		# Full house
		if 3 in values_hist and 2 in values_hist:
			return 7, self.get_value_of(3)
			
		# Three of a kind
		if 3 in values_hist:
			return 4, self.get_value_of(3)
			
		# Two pair
		if values_hist.count(2) == 2:
			return 3, self.get_value_of(2)
			
		# Pair
		if values_hist.count(2) == 1:
			return 2, self.get_value_of(2)
			
		if self.is_royal() and self.is_flush():
			return 10, max(self.get_values())
		
		# Straight Flush
		if self.is_straight() and self.is_flush():
			return 9, max(self.get_values())
			
		# Straight
		if self.is_straight():
			return 5, max(self.get_values())
			
		# Flush
		if self.is_flush():
			return 6, max(self.get_values())
		
		# High card
		return 1, max(self.get_values())
		