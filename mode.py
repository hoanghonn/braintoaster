import pygame, random, helper
from pygame import *
from random import *
from helper import *

class Mode():

    def __init__(self, screen):
        return

    def play_game(self):
        return None


class MathGame(Mode):
    # implement init later
    def play_game(self):

        return True


class ColorGame(Mode):

    COLOR = [('RED',255,0,0),('GREEN',0,255,0),('BLUE',0,0,255),('PURPLE',255,0,255),('YELLOW',255,255,0),('BROWN',153,102,0),('BLACK',0,0,0)]
    FOUR_COLOR = sample(COLOR, 4)
    ANSWER = randint(0,3)
    ANSWER_COLOR = randint(0,3)

    def __init__(self,screen):
        super.__init__

    def set_up_game(self):
        self.FOUR_COLOR = sample(self.COLOR, 4)
        self.ANSWER = randint(0,3)
        self.ANSWER_COLOR = randint(0,3)

    # implement init later
    def play_game(self):
        mousex = 0
        mousey = 0
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.ANSWER == 0:
                        if 10 < mousex and mousex < 245 and 10 < mousey and mousey < 210:
                            return True
                        else: return False
                    elif self.ANSWER == 1:
                        if 10 < mousex and mousex < 245 and 220 < mousey and mousey < 420:
                            return True
                        else: return False
                    elif self.ANSWER == 2:
                        if 255 < mousex and mousex < 490 and 10 < mousey and mousey < 210:
                            return True
                        else: return False
                    elif self.ANSWER == 3:
                        if 255 < mousex and mousex < 490 and 220 < mousey and mousey < 420:
                            return True
                        else: return False

    def draw(self,screen):
        screen.fill((255,255,255))
        font_blit(screen, (170,430), 40, self.FOUR_COLOR[self.ANSWER][0], (self.FOUR_COLOR[self.ANSWER_COLOR][1], self.FOUR_COLOR[self.ANSWER_COLOR][2], self.FOUR_COLOR[self.ANSWER_COLOR][3]))
        pygame.draw.rect(screen, (self.FOUR_COLOR[0][1], self.FOUR_COLOR[0][2], self.FOUR_COLOR[0][3]), (10,10,235,200))
        pygame.draw.rect(screen, (self.FOUR_COLOR[1][1], self.FOUR_COLOR[1][2], self.FOUR_COLOR[1][3]), (10,220,235,200))
        pygame.draw.rect(screen, (self.FOUR_COLOR[2][1], self.FOUR_COLOR[2][2], self.FOUR_COLOR[2][3]), (255,10,235,200))
        pygame.draw.rect(screen, (self.FOUR_COLOR[3][1], self.FOUR_COLOR[3][2], self.FOUR_COLOR[3][3]), (255,220,235,200))
        pygame.display.update()
