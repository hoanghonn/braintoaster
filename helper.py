import pygame, sys
from pygame import *


def font_blit(screen, center, size, text, color, background_color = None):
    FONT = pygame.font.Font('Digitalt.ttf', size)
    TEXT = 'none'
    if background_color == None:
        TEXT = FONT.render(text, True, color)
    else:
        TEXT = FONT.render(text, True, color, background_color)
    screen.blit(TEXT, (center[0] - TEXT.get_rect().width/2, center[1] - TEXT.get_rect().height/2))
    return (TEXT.get_rect().width, TEXT.get_rect().height)


def terminate():
    pygame.quit()
    sys.exit()

def draw_time(screen,sec):
    font_blit(screen,(400,100),80,str(sec),(0,0,0))
