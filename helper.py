import pygame, sys, constants
from pygame import *
from constants import *


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

def draw_health(screen, health):
    health_width = health / 100.0 * SCREEN_WIDTH
    health_bar = (0,0, health_width, 50)

    pygame.draw.rect(screen, (255,0,0), health_bar)

def draw_time(screen,sec):
    font_blit(screen,(400,100),80,str(sec),(0,0,0))
