import pygame, sys
import random
import helper
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
        x = random.randrange(0, 100)
        y = random.randrange(0, 100)
        opran = random.randrange(0, 4)

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
    # implement init later
    def play_game(self):
        return True
