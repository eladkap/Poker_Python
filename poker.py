from card import *
from hand import *
from deck import *
from settings import *


def strongerHand(hand1, hand2):
	hand1.sort()
	hand2.sort()
	rank1, _, max1 = hand1.rank()
	rank2, _, max2 = hand2.rank()
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
			max1 = max(hand1.getValues())
			max2 = max(hand2.getValues())
			if max1 > max2:
				return 1
			elif max1 < max2:
				return 2
	return 0

	
def get_value_of_symbol(symbol):
	if symbol == 'J':
		return 11
	if symbol == 'Q':
		return 12
	if symbol == 'K':
		return 13
	if symbol == 'A':
		return 14
	return int(symbol)
	

def read_line(line):
	fields = line.split(' ')
	hand1 = Hand()
	hand2 = Hand()
	for i in range(0, 5):
		value = get_value_of_symbol(fields[i][0])
		symbol = CARD_SYMBOLS[value]
		suit = CARD_LETTERS_SUITS[fields[i][1]]
		card = Card(symbol, value, suit)
		hand1.add(card)
	for i in range(5, 10):
		value = get_value_of_symbol(fields[i][0])
		symbol = fields[i][1]
		suit = CARD_LETTERS_SUITS[fields[i][1]]
		card = Card(symbol, value, suit)
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
	
	
def test1():
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

	
def test2():
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


def test3():
	card11 = Card('K', 1, 0, 0, 0, 0)
	card12 = Card('K', 0, 0, 0, 0, 0)
	card13 = Card('Q', 0, 0, 0, 0, 0)
	card14 = Card('8', 0, 0, 0, 0, 0)
	card15 = Card('7', 0, 0, 0, 0, 0)
	hand1 = Hand(0, 0, None)
	hand1.addCard(card11, None)
	hand1.addCard(card12, None)
	hand1.addCard(card13, None)
	hand1.addCard(card14, None)
	hand1.addCard(card15, None)
	print(hand1.rank())

	card21 = Card('A', 1, 0, 0, 0, 0)
	card22 = Card('A', 0, 0, 0, 0, 0)
	card23 = Card('Q', 0, 0, 0, 0, 0)
	card24 = Card('8', 0, 0, 0, 0, 0)
	card25 = Card('7', 0, 0, 0, 0, 0)
	hand2 = Hand(0, 0, None)
	hand2.addCard(card21, None)
	hand2.addCard(card22, None)
	hand2.addCard(card23, None)
	hand2.addCard(card24, None)
	hand2.addCard(card25, None)
	print(hand2.rank())

	print(strongerHand(hand1, hand2))

	
if __name__ == '__main__':
	test3()
		