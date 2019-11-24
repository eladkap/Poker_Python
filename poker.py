from card import *
from hand import *
from deck import *
from constants import *


def strongest_hand(hand1, hand2):
	hand1.sort()
	hand2.sort()
	rank1, max1 = hand1.rank()
	rank2, max2 = hand2.rank()
	if rank1 > rank2:
		return 1
	elif rank1 < rank2:
		return 2
	else:
		if max1 > max2:
			return 1
		elif max1 < max2:
			return 2
		else:
			max1 = max(hand1.get_values())
			max2 = max(hand2.get_values())
			if max1 > max2:
				return 1
			elif max1 < max2:
				return 2
	return 0


def read_line(line):
	fields = line.split(' ')
	hand1 = Hand()
	hand2 = Hand()
	for i in range(0, 5):
		card = Card()
		card.set(fields[i])
		hand1.add(card)
	for i in range(5, 10):
		card = Card()
		card.set(fields[i])
		hand2.add(card)
	return hand1, hand2
		
		
def read_hands(file):
	player1_wins = 0
	with open(file, 'r') as reader:
		lines = reader.readlins()
		for line in lines:
			hand1, hand2 = read_line(line)
			if winner(hand1, hand2) == 1:
				player1_wins += 1
	return player1_wins
	
	
def test():
	#line = '8C 8S 8D 9H 9S 7C 2C 5C 3C AC'
	line = '4C 4S 7D 7H KS 7C 2C 5C 3C AC'
	hand1, hand2 = read_line(line)
	print(hand1)
	print(hand2)
	hand1.sort()
	hand2.sort()
	print(hand1)
	print(hand2)
	
	rank1, max1 = hand1.rank()
	print(RANKS[rank1], max1)
	
	rank2, max2 = hand2.rank()
	print(RANKS[rank2], max2)
	
	'''
	deck = Deck()
	deck.shuffle()
	deck.show()
	print(len(deck))
	'''
	
	
if __name__ == '__main__':
	h1 = None
	h2 = None
	with open('C:\Temp\p054_poker.txt', 'r') as reader:
		player1_wins = 0
		player2_wins = 0
		lines = reader.readlines()
		for line in lines:
			hand1, hand2 = read_line(line)
			win = strongest_hand(hand1, hand2)
			if win == 1:
				player1_wins += 1
			else:
				player2_wins += 1

		print(len(lines))
		print(player1_wins)
		print(player2_wins)
		