import pygame
import sys
import manager
from pygame import *
from manager import *

# constants go here
COLOR = {'RED': (251, 57, 88),
         'GREEN': (37, 211, 102),
         'BLUE': (69, 142, 255),
         'PURPLE': (255, 0, 255),
         'YELLOW': (255, 200, 56),
         'BROWN': (153, 102, 0),
         'BLACK': (0, 0, 0)}
TEXT_POS = (150, 100)

pygame.init()
DISPLAYSURF = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Brain Toaster')
clock = pygame.time.Clock()

score = -1
highScore = 0
bg = pygame.mixer.music('/asset/bgmusic.mp3')
bg.play()

while True:
    mousex = 0
    mousey = 0

    # draw background pic
    background = pygame.image.load('asset/bg-01.png')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    background_rect = background.get_rect()
    DISPLAYSURF.blit(background, background_rect)

    # draw logo
    logo = pygame.image.load('asset/braintoasted.png')
    logo = pygame.transform.scale(logo, LOGO_SIZE)
    logo_rect = logo.get_rect()
    logo_rect_pos = (SCREEN_WIDTH/2 - logo_rect.width/2, SCREEN_HEIGHT/3 - logo_rect.height/2)
    logo_rect = logo_rect.move(logo_rect_pos)
    DISPLAYSURF.blit(logo, logo_rect)

    # draw start button
    start = pygame.image.load('asset/start.png')
    start = pygame.transform.scale(start, START_SIZE)
    start_rect = start.get_rect()
    start_rect_pos = (SCREEN_WIDTH/2 - logo_rect.width/2, SCREEN_HEIGHT*4/5 - start_rect.height/2)
    start_rect = start_rect.move(start_rect_pos)
    DISPLAYSURF.blit(start, start_rect)

    # draw score
    if score != -1:
        print_score = 'Score: ' + str(score)
        score_rect = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.6)
        font_blit(DISPLAYSURF, score_rect, FONT_BIG, print_score, YELLOW)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
    if start_rect.collidepoint(mousex, mousey):
        mng = Manager(DISPLAYSURF)
        score = mng.get_score()

    if score > highScore:
        highScore = score
    print_highScore = 'High Score: ' + str(highScore)
    highSCore_rect = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.7)
    font_blit(DISPLAYSURF, highSCore_rect, FONT_SMALL, print_highScore, YELLOW)

    pygame.display.update()
    clock.tick(30)
