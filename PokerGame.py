import pygame
from settings import *
from main_window import *
from card import *
from card_image import *
from hand import *
from deck import *
from button import *
from poker import *


class PokerGame:
	def __init__(self):
		self.setupGame()

	def setupGame(self):
		self.setButtons()
		self.resetRound()
		
	def resetRound(self):
		self.game_quit = False
		window.fill(BLACK)
		self.deck = Deck()
		self.deck.shuffle()
		print('Deck with %d packs was created.' % len(self.deck))
		
		# Set player hand
		print('Set player hand')
		self.player_hand = Hand(SCREEN_WIDTH / 2 - CARD_WIDTH * 3, 100, 1)
		for i in range(MAX_HAND_CARDS):
			card = self.deck.pop()
			self.player_hand.addCard(card, to_reveal=True)
		self.player_hand.display()

		#Set dealer hand
		print('Set dealer hand')
		self.dealer_hand = Hand(SCREEN_WIDTH / 2 - CARD_WIDTH * 3, SCREEN_HEIGHT - CARD_HEIGHT - 100, 2)
		for i in range(MAX_HAND_CARDS):
			card = self.deck.pop()
			self.dealer_hand.addCard(card, to_reveal=False)
		self.dealer_hand.display()
		
		print('Set ranks')
		self.setRanks()
		self.displayRanks(True, False)
		
		# LOOP #
		while not self.game_quit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
				if event.type == pygame.MOUSEBUTTONUP:
					mouse_pos = pygame.mouse.get_pos()
					self.mousePressed(mouse_pos)

			self.btn_new_round.hide()
			self.btn_reveal_dealer_hand.show()
			self.btn_sort_hand.show()
			self.btn_swap_cards.show()	
			self.displayButtons()
		
			pygame.display.update()
			clock.tick(FPS)
		
	def displayButtons(self):
		mouse_pos = pygame.mouse.get_pos()
		self.btn_new_round.draw(mouse_pos)
		self.btn_reveal_dealer_hand.draw(mouse_pos)
		self.btn_sort_hand.draw(mouse_pos)
		self.btn_swap_cards.draw(mouse_pos)
		
	def swapCards(self):
		print('Swap cards')
		#for i in range(len(self.player_hand) - 1, -1, -1):
		for i in range(len(self.player_hand)):
			if self.player_hand.getCard(i).isChosen():
				card = self.player_hand.removeCard(i)
				self.deck.pushFront(card)
				card = self.deck.pop()
				self.player_hand.insertCard(card, i, to_reveal=True)
		self.setRanks()
		self.redrawGame()
		self.btn_swap_cards.disable()
		
	def setButtons(self):
		self.btn_new_round = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT, 'New Round', FONT_FAMILY1, SMALL_FONT, BLACK, OFF_WHITE, AQUA)
		self.btn_reveal_dealer_hand = Button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BUTTON_WIDTH, BUTTON_HEIGHT, 'Reveal Dealer', FONT_FAMILY1, SMALL_FONT, BLACK, OFF_WHITE, AQUA)
		self.btn_sort_hand = Button(SCREEN_WIDTH * 0.75, 100, BUTTON_WIDTH, BUTTON_HEIGHT, 'Sort Hand', FONT_FAMILY1, SMALL_FONT, BLACK, OFF_WHITE, AQUA)
		self.btn_swap_cards = Button(SCREEN_WIDTH * 0.75, 150, BUTTON_WIDTH, BUTTON_HEIGHT, 'Swap Cards', FONT_FAMILY1, SMALL_FONT, BLACK, OFF_WHITE, AQUA)	
		
	def setRanks(self):
		player_r, player_b, _ = self.player_hand.rank()
		dealer_r, dealer_b, _ = self.dealer_hand.rank()
		self.playerRank = RANKS[player_r] + ' of ' + player_b
		self.dealerRank = RANKS[dealer_r] + ' of ' + dealer_b
		
	def displayRanks(self, player_flag, dealer_flag):
		if (player_flag):
			showText(self.playerRank, [self.player_hand.x - 300, self.player_hand.y + CARD_HEIGHT / 2], OFF_WHITE, FONT_FAMILY1, MEDIUM_FONT, False, 0)
		if (dealer_flag):
			showText(self.dealerRank, [self.dealer_hand.x - 300, self.dealer_hand.y + CARD_HEIGHT / 2], OFF_WHITE, FONT_FAMILY1, MEDIUM_FONT, False, 0)
		
	def redrawGame(self):
		window.fill(BLACK)
		self.player_hand.display()
		self.dealer_hand.display()
		self.displayRanks(True, False)
		self.displayButtons()
		
	def sortPlayerHand(self):
		window.fill(BLACK)
		self.player_hand.sort()
		self.redrawGame()
		
	def revealDealerHand(self):
		window.fill(BLACK)
		for card in self.dealer_hand.cards:
			card.reveal()
		self.player_hand.display()
		self.dealer_hand.display()
		self.btn_reveal_dealer_hand.disable()
		self.checkWinner()
	
	def checkWinner(self):
		res = strongerHand(self.player_hand, self.dealer_hand)
		if res == 1:
			showText('Player Wins!', [SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 100], GREEN, FONT_FAMILY1, MEDIUM_FONT, False, 0)
		elif res == 2:
			showText('Dealer Wins!', [SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 100], RED, FONT_FAMILY1, MEDIUM_FONT, False, 0)
		else:
			showText('TIE!',[SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2 - 100], WHITE, FONT_FAMILY1, MEDIUM_FONT, False, 0)
		self.displayRanks(True, True);
		self.btn_new_round.show()
		self.btn_reveal_dealer_hand.disable()
		self.displayButtons()

	def mousePressed(self, mouse_pos):
		#click = pygame.mouse.get_pressed()
		if self.btn_swap_cards.mouseClick(mouse_pos):
			self.swapCards()
		if self.btn_sort_hand.mouseClick(mouse_pos):
			self.sortPlayerHand()
		if self.btn_reveal_dealer_hand.mouseClick(mouse_pos):
			self.revealDealerHand()
		
		if self.btn_swap_cards.isEnabled():
			for card in self.player_hand.cards:
				if card.isClicked(mouse_pos):
					if not card.isChosen():
						card.setChosen(True)
						card.draw()
					else:
						card.setChosen(False)
						card.draw()
					return
	
	def quit(self):
		pygame.quit()
		quit()

		
# INITIALIZE GAME #
poker_game = PokerGame()
# INITIALIZE GAME #
