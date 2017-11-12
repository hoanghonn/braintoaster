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
        screen.fill(BLUE)
        # draw math string
        font_blit(screen, (250, 300), 60, self.math_string, RED)

        # draw answers
        pygame.draw.rect(screen, WHITE, self.correct_answer_rect)

        # add text to button
        correct_answer_rect = (self.correct_answer_rect.left + self.correct_answer_rect.width/2,
                               self.correct_answer_rect.top + self.correct_answer_rect.height/2)
        font_blit(screen, correct_answer_rect, 30, str(self.result), GREEN)

        pygame.draw.rect(screen, WHITE, self.wrong_answer_rect)

        rand_diff = randint(-10, 11)
        fake_result = self.result + rand_diff        # change later

        wrong_answer_rect = (self.wrong_answer_rect.left + self.wrong_answer_rect.width/2,
                             self.wrong_answer_rect.top + self.wrong_answer_rect.height/2)
        font_blit(screen, wrong_answer_rect, 30, str(fake_result), GREEN)

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
        x = randrange(0, 10)
        y = randrange(1, 10)
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
    def play_game(self,screen,health):
        mousex = 0
        mousey = 0
        cur_health = health
        cur_time = pygame.time.get_ticks()
        cur_sec = 3
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.ANSWER == 0:
                        if SCREEN_WIDTH*0.04 < mousex and mousex < SCREEN_WIDTH*0.48 and SCREEN_HEIGHT*0.4 < mousey and mousey < SCREEN_HEIGHT*0.68:
                            return (True, cur_health)
                        else: return (False, cur_health)
                    elif self.ANSWER == 1:
                        if SCREEN_WIDTH*0.04 < mousex and mousex < SCREEN_WIDTH*0.48 and SCREEN_HEIGHT*0.7 < mousey and mousey < SCREEN_HEIGHT*0.98:
                            return (True, cur_health)
                        else: return (False, cur_health)
                    elif self.ANSWER == 2:
                        if SCREEN_WIDTH*0.52 < mousex and mousex < SCREEN_WIDTH*0.96 and SCREEN_HEIGHT*0.4 < mousey and mousey < SCREEN_HEIGHT*0.68:
                            return (True, cur_health)
                        else: return (False, cur_health)
                    elif self.ANSWER == 3:
                        if SCREEN_WIDTH*0.52 < mousex and mousex < SCREEN_WIDTH*0.96 and SCREEN_HEIGHT*0.7 < mousey and mousey < SCREEN_HEIGHT*0.98:
                            return (True, cur_health)
                        else: return (False, cur_health)
            #cur_health = clock
            if cur_sec == 0:
                return (False, cur_health)
            temp_time = pygame.time.get_ticks()
            if 0.95 < (temp_time - cur_time)/1000:
                cur_time = temp_time
                cur_sec -= 1
            self.draw(screen, cur_health, cur_sec)



    def draw(self,screen,health,sec):
        screen.fill((255,255,255))
        font_blit(screen, (SCREEN_WIDTH*0.5,SCREEN_HEIGHT*0.5), 80, self.FOUR_COLOR[self.ANSWER][0], (self.FOUR_COLOR[self.ANSWER_COLOR][1], self.FOUR_COLOR[self.ANSWER_COLOR][2], self.FOUR_COLOR[self.ANSWER_COLOR][3]))
        pygame.draw.rect(screen, (self.FOUR_COLOR[0][1], self.FOUR_COLOR[0][2], self.FOUR_COLOR[0][3]), (SCREEN_WIDTH*0.04,SCREEN_HEIGHT*0.4,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[1][1], self.FOUR_COLOR[1][2], self.FOUR_COLOR[1][3]), (SCREEN_WIDTH*0.04,SCREEN_HEIGHT*0.7,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[2][1], self.FOUR_COLOR[2][2], self.FOUR_COLOR[2][3]), (SCREEN_WIDTH*0.52,SCREEN_HEIGHT*0.4,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[3][1], self.FOUR_COLOR[3][2], self.FOUR_COLOR[3][3]), (SCREEN_WIDTH*0.52,SCREEN_HEIGHT*0.7,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        #draw_ealth(screen,health)
        draw_time(screen,sec)
        pygame.display.update()
