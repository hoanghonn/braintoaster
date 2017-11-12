import random, mode
from mode import *
from random import *


class Manager:

    numberOfGame = 2
    health = 100
    game = []
    score = 0

    def __init__(self,screen):
        math_game = MathGame(screen)
        color_game = ColorGame(screen)
        self.game.append(math_game)
        self.game.append(color_game)

        while self.health > 0:
            random_game = randrange(0, self.numberOfGame)
            if len(self.game) <= 0:
                print("Error: No game in database")

            cur_game = self.game[random_game]
            cur_game.set_up_game()
            cur_game.draw(screen)
            if cur_game.play_game():
                self.health += 2
                self.score += 10
            else:
                self.health -= 10
            print(self.health)

    def get_score(self):
        return self.score
