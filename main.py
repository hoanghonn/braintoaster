import pygame
import sys
import manager
from pygame import *
from manager import *

# constants go here
COLOR = {'RED': (251, 57, 88),
         'GREEN': (37, 211, 102),
         'BLUE': (69, 142, 255),
         'PURPLE': (255, 0, 255),
         'YELLOW': (255, 200, 56),
         'BROWN': (153, 102, 0),
         'BLACK': (0, 0, 0)}
DISPLAY_SIZE = (500, 1000)
TEXT_POS = (150, 100)

pygame.init()
DISPLAYSURF = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Brain Toaster')
FONT = pygame.font.Font('Digitalt.ttf', 100)
TEXT = FONT.render('START', True, COLOR['RED'], COLOR['YELLOW'])

clock = pygame.time.Clock()


while True:
    mousex = 0
    mousey = 0
    DISPLAYSURF.fill(COLOR['GREEN'])
    DISPLAYSURF.blit(TEXT, TEXT_POS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
    if Rect(TEXT_POS, (TEXT.get_rect().width, TEXT.get_rect().height)).collidepoint(mousex, mousey):
        mng = Manager(DISPLAYSURF)
        score = mng.get_score()
    pygame.display.update()
    clock.tick(30)
