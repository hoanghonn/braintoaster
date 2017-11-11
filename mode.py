import pygame

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


class Mode():

    def __init__(self, screen):
        return

    def play_game(self):
        return None


class MathGame(Mode):
    math_string = ''
    result = ''

    # implement init later
    def __init__(self, screen):
        self.math_string = self._get_string()
        self.result = self._calculate_result()


    def play_game(self):
        # while True:
        #     for event in pygame.event.get()


        return False

    def draw(self, screen):
        # draw math string
        print('Start Drawing')
        screen.fill(BLUE)

        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render(self.math_string, True, RED)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (250, 300)
        screen.blit(textSurfaceObj, textRectObj)

        # draw answers
        pygame.draw.rect(screen, WHITE, (100, 700, 100, 100))

        # add text to button
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        textSurfaceObj = smallText.render(self.result, True, GREEN)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = ( (100 + 100/2), (700 + 100/2))
        screen.blit(textSurfaceObj, textRectObj)

        pygame.draw.rect(screen, WHITE, (350, 700, 100, 100))
        fakeResult = self.result + '2' #change later
        textSurfaceObj = smallText.render(fakeResult, True, GREEN)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = ((350 + 100 / 2), (700 + 100 / 2))
        screen.blit(textSurfaceObj, textRectObj)

        pygame.display.update()



class ColorGame(Mode):
    # implement init later
    def play_game(self):
        return True
