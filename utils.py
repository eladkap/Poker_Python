import pygame
from settings import *
from main_window import *


def textObjects(text, color, font_family, font_size):
		font = pygame.font.SysFont(font_family, font_size)
		text_surface = font.render(text, True, color)
		return text_surface, text_surface.get_rect()

def showText(text, location, color, font_family, font_size, center_flag, y_offset):
		if center_flag:
			text_surface, text_rect = textObjects(text, color, font_family, font_size)
			text_rect.center = (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2) + y_offset
			window.blit(text_surface, text_rect)
		else:
			font = pygame.font.SysFont(font_family, font_size)
			text_obj = font.render(text, True, color)
			window.blit(text_obj, location)
