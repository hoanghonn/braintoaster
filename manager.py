import random
import mode
from mode import *
from random import *


class Manager:

    numberOfGame = 2
    health = 100
    game = []
    score = 0

    def __init__(self, screen):
        math_game = MathGame()
        # color_game = ColorGame()
        ope_game = OperatorGame()
        self.game.append(math_game)
        # self.game.append(color_game)
        self.game.append(ope_game)

        while self.health > 0:
            random_game = randrange(0, self.numberOfGame)
            if len(self.game) <= 0:
                print("Error: No game in database")

            cur_game = self.game[random_game]
            cur_game.set_up_game()
            result = cur_game.play_game(screen, self.health)
            self.health = result[1]
            if result[0]:
                self.health += 2
                if self.health + 2 > 100:
                    self.health = 100
                else:
                    self.health += 2
                self.score += 10
            else:
                self.health -= 10
            print(self.health)

    def get_score(self):
        return self.score
