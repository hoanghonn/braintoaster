import random
# import pygame
from mode import *


class Manager:

    numberOfGame = 3
    health = 100
    game = []
    score = 0

    def __init__(self,screen):
        # screen.fill((0, 0, 0))
        # pygame.display.update()
        math_game = MathGame(screen)
        color_game = ColorGame(screen)
        self.game.append(math_game)
        self.game.append(color_game)

        while self.health > 0:
            random_game = random.randrange(0, self.numberOfGame)
            if len(self.game) <= 0:
                print("Error: No game in database")

            cur_game = self.game[random_game]
            cur_game.draw(screen)
            if cur_game.playGame():
                self.health += 2
                self.score += 10
            else:
                self.health -= 10

    def get_score(self):
        return self.score
