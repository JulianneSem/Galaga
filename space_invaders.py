import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect()
        self.rect.left = 75
        self.rect.bottom = 550
    def moveLeft(self):
        self.rect.move_ip(-1, 0)
        if self.rect.left < 0:
            self.rect.left = 0
    def moveRight(self):
        self.rect.move_ip(1, 0)
        if self.rect.right > 800:
            self.rect.right = 800

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')
screen.fill((255, 255, 255))

player = Player()
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
                player.moveLeft()
            if event.key == K_RIGHT:
                player.moveRight()
    screen.blit(player.surf, player.rect)
    pygame.display.flip()
    screen.fill((255, 255, 255))
pygame.quit()
