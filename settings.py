# SCREEN SETTINGS #
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
FPS = 15

# COLORS #
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OFF_WHITE1 = (240, 240, 240)
OFF_WHITE = (220, 220, 220)
RED = (200, 0, 0)
LIGHT_RED = (255, 0, 0)
GREEN = (0, 180, 0)
LIGHT_GREEN = (0, 240, 0)
BLUE = (0, 0, 220)
AQUA = (0, 255, 255)
LIGHT_BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# CARD SETTINGS #
CARD_SYMBOLS = ['-', '-', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
CARD_SUITS = ['\u2660', '\u2665', '\u2663', '\u2666']
CARD_SUITS_LETTERS = ['S', 'H', 'C', 'D']
CARD_LETTERS_SUITS = {'S': 0, 'H': 1, 'C': 2, 'D': 3}
CARD_WIDTH = 120
CARD_HEIGHT = CARD_WIDTH * 1.5
CARD_FONT_SIZE = 24
CARD_BACKGROUND = OFF_WHITE1
CARD_BACKGROUND_CHOSEN = AQUA
SPACE_BETWEEN_CARDS = 20

MAX_HAND_CARDS = 5

RANKS = {
	1: 'High Card',
	2: 'Pair',
	3: 'Two Pair',
	4: 'Three of a Kind',
	5: 'Straight',
	6: 'Flush',
	7: 'Full House',
	8: 'Four of a Kind',
	9: 'Straight Flush',
	10: 'Royal Flush'
}

# BUTTON SETTINGS #
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 40

# TEXT SETTINGS #
SMALL_FONT = 16
MEDIUM_FONT = 24
BIG_FONT = 32
HUGE_FONT = 48
FONT_FAMILY1 = 'Arial'

# IMAGES #
POKER_ICON = 'poker_icon.png'
