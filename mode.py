import pygame, sys
import random
from helper import *
from pygame import *
from random import *

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Mode:

    def __init__(self):
        return

    def play_game(self):
        return None


class MathGame(Mode):
    math_string = ''
    result = ''
    correct_answer_rect = pygame.Rect(100, 700, 100, 100)
    wrong_answer_rect = pygame.Rect(350, 700, 100, 100)

    color = [ ('RED', 255,0,0), ('BLUE', 0,0,255)]

    # implement init later
    def __init__(self, screen):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

    def play_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.correct_answer_rect.collidepoint(mousex, mousey):
                        return True
                    elif self.wrong_answer_rect.collidepoint(mousex, mousey):
                        return False

        return False

    def set_up_game(self):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

    def draw(self, screen):
        # draw math string
        screen.fill(BLUE)

        font_blit(screen, (250, 300), 60, self.math_string, RED)

        # draw answers
        pygame.draw.rect(screen, WHITE, self.correct_answer_rect)

        # add text to button
        font_blit(screen, self.correct_answer_rect, 30, str(self.result), GREEN)

        pygame.draw.rect(screen, WHITE, self.wrong_answer_rect)
        fakeResult = self.result + 2        # change later

        font_blit(screen, self.wrong_answer_rect, 30, str(fakeResult), GREEN)

        pygame.display.update()

    def _calculate_result(self):
        if len(self.math_string) < 7:
            print("Error: not a valid math_string")
        index = 0
        temp = []
        check = 0

        while check < len(self.math_string):
            if self.math_string[check] == ' ':
                len_of_num = check-index
                if len_of_num > 0:
                    temp.append(self.math_string[index:check])
                else:
                    print("Error: not a valid operator or operand")
                index = check+1
            check += 1

        if temp[1] == "+":
            return int(temp[0]) + int(temp[2])
        elif temp[1] == "-":
            return int(temp[0]) - int(temp[2])
        elif temp[1] == "*":
            return int(temp[0]) * int(temp[2])
        else:
            return int(temp[0]) / int(temp[2])

    def _get_string(self):
        self.math_string = ""
        x = randrange(0, 100)
        y = randrange(0, 100)
        opran = randrange(0, 4)

        if opran == 1:
            self.math_string += str(x) + " + " + str(y) + " = "
        elif opran == 2:
            self.math_string += str(x) + " - " + str(y) + " = "
        elif opran == 3:
            self.math_string += str(x) + " * " + str(y) + " = "
        else:
            self.math_string += str(x) + " / " + str(y) + " = "
        return self.math_string


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
