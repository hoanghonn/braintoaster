import random
import mode
import pygame
from mode import *
from random import *


class Manager:

    numberOfGame = 4
    numberOfHardGame = numberOfGame + 2
    health = 100
    game = []
    hard_game = []
    score = 0

    def __init__(self, screen):
        math_game = MathGame()
        color_game = ColorGame()
        ope_game = OperatorGame()
        dont_game = DontTouchGame()
        a_dont_game = AdvancedDontTouchGame()
        a_color_game = AdvancedColorGame()
        a_touch_game = AdvancedTouchGame()
        self.hard_game.append(a_touch_game)
        self.hard_game.append(a_color_game)
        self.hard_game.append(a_dont_game)
        self.hard_game.append(math_game)
        self.hard_game.append(color_game)
        self.hard_game.append(ope_game)
        self.hard_game.append(dont_game)

        self.game.append(math_game)
        self.game.append(color_game)
        self.game.append(ope_game)
        self.game.append(dont_game)

        while self.health > 0:
            random_game = randrange(0, self.numberOfGame)
            random_hard_game = randrange(0, self.numberOfHardGame)
            if len(self.game) <= 0:
                print("Error: No game in database")
            if self.score > 50:
                cur_game = self.hard_game[random_hard_game]
            else:
                cur_game = self.game[random_game]
            cur_game.set_up_game()
            result = cur_game.play_game(screen, self.health, self.score)
            self.health = result[1]
            if result[0]:
                if self.health + 2 > 100:
                    self.health = 100
                else:
                    self.health += 1
                self.score += 10
            else:
                self.health -= 10

    def get_score(self):
        return self.score
