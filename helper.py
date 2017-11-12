import pygame, sys
from pygame import *

def font_blit(screen, center, size, text, color, background_color = None):
    FONT = pygame.font.Font('FreeSansBold.ttf', size)
    TEXT = 'none';
    if background_color == None:
        TEXT = FONT.render(text, True, color)
    else:
        TEXT = FONT.render(text, True, color, background_color)
    screen.blit(TEXT, center)
    return (TEXT.get_rect().width, TEXT.get_rect().height)

def terminate():
    pygame.quit()
    sys.exit()