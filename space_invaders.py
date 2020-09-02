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
        self.surf.fill((0, 0, 0))
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
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect(center=(50,50))
        # self.speed = random.randint(5, 20)

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.surf = pygame.Surface((3, 10))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.speed = -1
    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top < 0:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')
screen.fill((255, 255, 255))

player = Player()
pygame.display.flip()

enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
wonRound = True
while running:
    if wonRound == True:
        enemy = Enemy()
        enemies.add(enemy)
        all_sprites.add(enemy)
        wonRound = False
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
            if event.key == K_UP:
                projectile = Projectile()
                projectile.rect.x = player.rect.left + (player.rect.right - player.rect.left)/2
                projectile.rect.y = player.rect.y - 10
                all_sprites.add(projectile)
                projectiles.add(projectile)
    for pro in projectiles:
        pro.update()
        enemiesHit = pygame.sprite.spritecollide(pro, enemies, True)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
    screen.fill((255, 255, 255))
pygame.quit()
