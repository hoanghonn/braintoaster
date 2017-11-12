import pygame
import sys
import random
import constants
from helper import *
from pygame import *
from random import *
from constants import *


class Mode:
    def __init__(self):
        return


class MathGame(Mode):
    math_string = ''
    result = ''
    correct_answer_rect = pygame.Rect(SCREEN_WIDTH / 4 - BUTTON_SIZE/2, SCREEN_HEIGHT * 7/10 - BUTTON_SIZE/2, BUTTON_SIZE, BUTTON_SIZE)
    wrong_answer_rect = pygame.Rect(SCREEN_WIDTH * 0.75 - BUTTON_SIZE/2,
                                    SCREEN_HEIGHT * 7/10 - BUTTON_SIZE/2,
                                    BUTTON_SIZE, BUTTON_SIZE)
    fake_result = ''

    def __init__(self):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

    def play_game(self, screen, health, score):
        cur_sec = MAX_TIME
        cur_time = pygame.time.get_ticks()
        cur_health = health
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.correct_answer_rect.collidepoint(mousex, mousey):
                        return True, cur_health
                    elif self.wrong_answer_rect.collidepoint(mousex, mousey):
                        return False, cur_health
            if cur_sec == 0:
                return False, cur_health
            temp_time = pygame.time.get_ticks()
            if 0.95 < (temp_time - cur_time)/1000:
                cur_time = temp_time
                cur_sec -= 1
            self.draw(screen, cur_health, cur_sec, score)

    def set_up_game(self):
        self.math_string = self._get_string()
        self.result = self._calculate_result()
        random_rect = randrange(0, 2)
        rand_diff = randint(-10, 11)
        if rand_diff == 0:
            rand_diff += 1
        self.fake_result = self.result + rand_diff

        if random_rect == 0:
            self.correct_answer_rect, self.wrong_answer_rect = self.wrong_answer_rect, self.correct_answer_rect

    def draw(self, screen, health, sec, score):
        screen.fill(CYAN)
        # draw math string
        font_blit(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3/10), FONT_BIG, self.math_string, PINK)

        # draw answers
        correct_answer_center = (self.correct_answer_rect.left + self.correct_answer_rect.width / 2,
                                 self.correct_answer_rect.top + self.correct_answer_rect.height / 2,
                                 self.correct_answer_rect.width, self.correct_answer_rect.height)
        pygame.draw.rect(screen, WHITE, self.correct_answer_rect)

        # add text to button
        font_blit(screen, correct_answer_center, FONT_SMALL, str(self.result), BROWN)
        wrong_answer_center = (self.wrong_answer_rect.left + self.wrong_answer_rect.width / 2,
                               self.wrong_answer_rect.top + self.wrong_answer_rect.height / 2,
                               self.wrong_answer_rect.width, self.wrong_answer_rect.height)
        pygame.draw.rect(screen, WHITE, self.wrong_answer_rect)
        font_blit(screen, wrong_answer_center, FONT_SMALL, str(self.fake_result), BROWN)

        # draw health
        draw_health(screen, health)
        # draw clock
        draw_time(screen, sec)
        # draw score
        draw_score(screen, score)

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

    COLOR = [('RED', 251, 57, 88),
             ('GREEN', 109, 201, 147),
             ('BLUE', 69, 142, 255),
             ('PURPLE', 195, 42, 163),
             ('YELLOW', 247, 180, 44),
             ('BROWN', 155, 105, 84),
             ('BLACK', 0, 0, 0)]
    FOUR_COLOR = sample(COLOR, 4)
    ANSWER = randint(0, 3)
    ANSWER_COLOR = randint(0, 3)

    def __init__(self):
        super.__init__

    def set_up_game(self):
        self.FOUR_COLOR = sample(self.COLOR, 4)
        self.ANSWER = randint(0, 3)
        self.ANSWER_COLOR = randint(0, 3)

    # implement init later

    def play_game(self,screen,health, score):
        mousex = 0
        mousey = 0
        cur_health = health
        cur_time = pygame.time.get_ticks()
        cur_sec = MAX_TIME
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.ANSWER == 0:
                        if SCREEN_WIDTH*0.04 < mousex < SCREEN_WIDTH*0.48 and \
                                                        SCREEN_HEIGHT * 0.4 < mousey < SCREEN_HEIGHT * 0.68:
                            return True, cur_health
                        else: return False, cur_health
                    elif self.ANSWER == 1:
                        if SCREEN_WIDTH*0.04 < mousex < SCREEN_WIDTH*0.48 and \
                                                        SCREEN_HEIGHT * 0.7 < mousey < SCREEN_HEIGHT * 0.98:
                            return True, cur_health
                        else: return False, cur_health
                    elif self.ANSWER == 2:
                        if SCREEN_WIDTH*0.52 < mousex < SCREEN_WIDTH*0.96 and \
                                                        SCREEN_HEIGHT * 0.4 < mousey < SCREEN_HEIGHT * 0.68:
                            return True, cur_health
                        else: return False, cur_health
                    elif self.ANSWER == 3:
                        if SCREEN_WIDTH*0.52 < mousex < SCREEN_WIDTH*0.96 and \
                                                        SCREEN_HEIGHT * 0.7 < mousey < SCREEN_HEIGHT * 0.98:
                            return True, cur_health
                        else: return False, cur_health
            # cur_health = clock

            if cur_sec == 0:
                return False, cur_health
            temp_time = pygame.time.get_ticks()
            if 0.95 < (temp_time - cur_time)/1000:
                cur_time = temp_time
                cur_sec -= 1
            self.draw(screen, cur_health, cur_sec, score)


    def draw(self,screen,health,sec, score):
        screen.fill(WHITE)
        font_blit(screen, (SCREEN_WIDTH*0.5,SCREEN_HEIGHT*0.2), FONT_BIG, self.FOUR_COLOR[self.ANSWER][0], (self.FOUR_COLOR[self.ANSWER_COLOR][1], self.FOUR_COLOR[self.ANSWER_COLOR][2], self.FOUR_COLOR[self.ANSWER_COLOR][3]))
        pygame.draw.rect(screen, (self.FOUR_COLOR[0][1], self.FOUR_COLOR[0][2], self.FOUR_COLOR[0][3]), (SCREEN_WIDTH*0.04,SCREEN_HEIGHT*0.4,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[1][1], self.FOUR_COLOR[1][2], self.FOUR_COLOR[1][3]), (SCREEN_WIDTH*0.04,SCREEN_HEIGHT*0.7,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[2][1], self.FOUR_COLOR[2][2], self.FOUR_COLOR[2][3]), (SCREEN_WIDTH*0.52,SCREEN_HEIGHT*0.4,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))
        pygame.draw.rect(screen, (self.FOUR_COLOR[3][1], self.FOUR_COLOR[3][2], self.FOUR_COLOR[3][3]), (SCREEN_WIDTH*0.52,SCREEN_HEIGHT*0.7,SCREEN_WIDTH*0.44,SCREEN_HEIGHT*0.28))

        draw_health(screen,health)
        draw_time(screen,sec)
        draw_score(screen, score)
        pygame.display.update()


class OperatorGame(Mode):

    missing_string = ''
    result = ''

    plus_rec = pygame.Rect(SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 3, SCREEN_WIDTH / 3)
    minus_rec = pygame.Rect((SCREEN_WIDTH/ 6) + (SCREEN_WIDTH / 3) + 10, SCREEN_HEIGHT/2, SCREEN_WIDTH / 3, SCREEN_WIDTH / 3)
    multiply_rec = pygame.Rect(SCREEN_WIDTH / 6, SCREEN_HEIGHT/2+ + (SCREEN_WIDTH/3) + 10, SCREEN_WIDTH / 3, SCREEN_WIDTH / 3)
    divide_rec = pygame.Rect((SCREEN_WIDTH/ 6) + (SCREEN_WIDTH / 3) + 10, SCREEN_HEIGHT/2+(SCREEN_WIDTH/3) + 10, SCREEN_WIDTH / 3, SCREEN_WIDTH / 3)
    ope = ["+", "-", "*", "/"]

    def __init__(self):
        self.missing_string = self._get_string()
        self.result = self._get_operator()
        self.result_index = self.ope.index(self.result)

    def play_game(self, screen, health, score):
        cur_health = health
        cur_time = pygame.time.get_ticks()
        cur_sec = MAX_TIME
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if self.plus_rec.collidepoint(mousex, mousey):
                        if self.result_index == 0:
                            return True, cur_health
                        else:
                            return False,cur_health
                    if self.minus_rec.collidepoint(mousex, mousey):
                        if self.result_index == 1:
                            return True, cur_health
                        else:
                            return False, cur_health
                    if self.multiply_rec.collidepoint(mousex, mousey):
                        if self.result_index == 2:
                            return True, cur_health
                        else:
                            return False, cur_health
                    if self.divide_rec.collidepoint(mousex, mousey):
                        if self.result_index == 3:
                            return True, cur_health
                        else:
                            return False, cur_health

                else:
                    self.draw(screen, cur_health, cur_sec, score)
            if cur_sec == 0:
                return False, cur_health
            temp_time = pygame.time.get_ticks()
            if 0.95 < (temp_time - cur_time) / 1000:
                cur_time = temp_time
                cur_sec -= 1
            self.draw(screen, cur_health, cur_sec, score)

    def set_up_game(self):
        self.missing_string = self._get_string()
        self.result = self._get_operator()
        self.result_index = self.ope.index(self.result)

    def draw(self, screen, health, sec, score):
        screen.fill((69, 187, 255))
        # draw math string
        font_blit(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3/10), FONT_BIG, self._update_missing_string(self.missing_string), PINK)

        # draw answers
        pygame.draw.rect(screen, WHITE, self.plus_rec)
        pygame.draw.rect(screen, WHITE, self.minus_rec)
        pygame.draw.rect(screen, WHITE, self.multiply_rec)
        pygame.draw.rect(screen, WHITE, self.divide_rec)

        # add text to button
        plus_rect = (self.plus_rec.left + self.plus_rec.width/2, self.plus_rec.top + self.plus_rec.height/2)
        font_blit(screen, plus_rect, FONT_SMALL, "+", BROWN)

        minus_rect = (self.minus_rec.left + self.minus_rec.width / 2, self.minus_rec.top + self.minus_rec.height / 2)
        font_blit(screen, minus_rect, FONT_SMALL, "-", BROWN)

        mul_rect = (self.multiply_rec.left + self.multiply_rec.width / 2, self.multiply_rec.top + self.multiply_rec.height / 2)
        font_blit(screen, mul_rect, FONT_SMALL, "*", BROWN)

        divide_rect = (self.divide_rec.left + self.divide_rec.width / 2, self.divide_rec.top + self.divide_rec.height / 2)
        font_blit(screen, divide_rect, FONT_SMALL, "/", BROWN)

        # draw health
        draw_health(screen, health)
        # draw clock
        draw_time(screen, sec)
        # draw score
        draw_score(screen, score)

        pygame.display.update()

    def _update_missing_string(self, string):
        if len(self.missing_string) < 9:
            print("Error: not a valid missing_string")
        temp = string
        operator_list = ["+", "-", "*", "/"]
        check = 0
        for chr in string:
            if check == 0 and chr in operator_list:
                check = 1
                temp = temp.replace(chr, "  ")
                return temp
        return temp

    def _get_operator(self):
        if len(self.missing_string) < 9:
            print("Error: not a valid missing_string")

        operator_list = ["+", "-", "*", "/"]
        for chr in self.missing_string:
            if chr in operator_list:
                return chr
        return -1

    def _get_string(self):
        self.missing_string = ""

        x = randrange(1, 10)
        y = randrange(1, 10)
        opran = randrange(0, 4)

        if opran == 1:
            res = x + y
            self.missing_string += str(x) + " + " + str(y) + " = " + str(res)
        elif opran == 2:
            res = x - y
            self.missing_string += str(x) + " - " + str(y) + " = " + str(res)
        elif opran == 3:
            res = x*y
            self.missing_string += str(x) + " * " + str(y) + " = " + str(res)
        else:
            res = x/y
            self.missing_string += str(x) + " / " + str(y) + " = " + str(res)
        print(self.missing_string)
        return self.missing_string


class DontTouchGame(Mode):
    instruction = 'do not touch'
    not_rec = pygame.Rect(SCREEN_WIDTH / 20, SCREEN_HEIGHT / 10, SCREEN_WIDTH - SCREEN_WIDTH * 0.9, SCREEN_HEIGHT - SCREEN_HEIGHT*4/5)

    def __init__(self):
        super.__init__

    def play_game(self, screen, health, score):
        cur_sec = MAX_TIME
        cur_time = pygame.time.get_ticks()
        cur_health = health
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    return False, cur_health

            if cur_sec == 0:
                return True, cur_health
            temp_time = pygame.time.get_ticks()
            if 0.95 < (temp_time - cur_time)/1000:
                cur_time = temp_time
                cur_sec -= 1
            self.draw(screen, cur_health, cur_sec, score)

    def set_up_game(self):
        instruction = 'do not touch'

    def draw(self, screen, health, sec, score):
        screen.fill(LIGHT_GREEN)
        # draw instruction
        font_blit(screen, (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3/10), FONT_SMALL, self.instruction, RED)

        pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH /6, SCREEN_HEIGHT / 2, 300, 300))


        # draw health
        draw_health(screen, health)
        # draw clock
        draw_time(screen, sec)
        # draw score
        draw_score(screen, score)
        pygame.display.update()


