import pygame, sys, random
from pygame.locals import *
import time 

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 200
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT),0, 32)
pygame.display.set_caption('Dino')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

bigSprite  = pygame.image.load('sprite.png')
bigSpriteRect = bigSprite.get_rect()

rect = pygame.Rect((1336,0,90,96))
dino = bigSprite.subsurface(rect)
dinoRect=dino.get_rect()


SPEED = 1

windowSurface.fill(WHITE)

windowSurface.blit(dino,dinoRect)
pygame.display.update()


moveRight=False

# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT: 
                moveRight = True
           
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                    moveRight = False
    if moveRight==True:

        if dinoRect.right + SPEED >= WINDOWWIDTH:
            dinoRect.right = WINDOWWIDTH-1
        else: 
            dinoRect.right = dinoRect.right+SPEED
        windowSurface.fill(WHITE)
        windowSurface.blit(dino,dinoRect)

    #Draw the white background onto the surface.
    pygame.display.update()
    #time.sleep(1.0/200.0)

    # Draw the window onto the screen.
    mainClock.tick(200)