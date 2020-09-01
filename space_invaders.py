import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN
)
def moveLeft():
    print("left")
def moveRight():
    print("Right")

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')
screen.fill((255, 255, 255))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                moveLeft()
            if event.key == K_RIGHT:
                moveRight()
pygame.quit()
