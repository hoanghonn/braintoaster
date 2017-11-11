import pygame
<<<<<<< HEAD
import helper
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
=======
import random
>>>>>>> 50b3310b2c9cfaca5faacb7aa699a1d877ef8c22


class Mode():

    def __init__(self):
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
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    helper.terminate()
                elif event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos

                # check if user clicked correct answer
                


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
            return int(temp[0]) + int(temp[2])
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
