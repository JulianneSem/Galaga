import pygame
import random
import sys
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
        self.rect.move_ip(-8, 0)
        if self.rect.left < 0:
            self.rect.left = 0
    def moveRight(self):
        self.rect.move_ip(8, 0)
        if self.rect.right > 800:
            self.rect.right = 800

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((30, 10))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.speed = 5
        self.timer = 0
        self.counter = 0
        self.inity = 0
        self.pattern = None
        self.projectile = EnemyProjectile()
        self.projectile.rect.x = self.rect.left + (self.rect.right - self.rect.left)/2
        self.projectile.rect.y = self.rect.y - 10

    def update(self):
        if self.counter == self.timer:
            if self.rect.y > 590:
                deltay = abs(self.rect.y - self.inity)
                self.rect = self.rect.move(0, deltay)
            elif self.rect.y < 0:
                self.rect = self.rect.move(0, self.rect.y - self.inity)
            else:
                self.rect.move_ip(0, self.speed)
                self.projectile.update()
        else:
            self.counter += 1




class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.surf = pygame.Surface((3, 10))
        self.surf.fill((255, 0, 255))
        self.rect = self.surf.get_rect()
        self.speed = -15

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top < 0:
            self.kill()


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self):
        super(EnemyProjectile, self).__init__()
        self.surf = pygame.Surface((3, 10))
        self.surf.fill((250, 0, 255))
        self.rect = self.surf.get_rect()
        self.speed = 15

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom < 0:
            self.kill()


class button(object):
    def __init__(self, x, y, text, screen):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        self.color = (42, 191, 220)
        self.text = text
        textwidth, textheight = font.size(str(text))
        self.textloc = (x+100 - (textwidth/2),y+40 -(textheight/2))
        self.position = (x, y, 200, 80)
        self.drawrect()

    def hover(self, x, y):
        if x > self.rect.x and x < self.rect.x + self.rect.width:
            if y > self.rect.y and y < self.rect.y + self.rect.height:
                self.color = (24, 145, 169)
            else:
                self.color = (42, 191, 220)
        else:
            self.color = (42, 191, 220)
        self.drawrect()

    def drawrect(self):
        self.rect = pygame.draw.rect(screen, self.color, self.position)
        text = font.render(self.text, True, (255, 255, 255))
        screen.blit(text,self.textloc)

    def click(self, x, y):
        if x > self.rect.x and x < self.rect.x + self.rect.width:
            if y > self.rect.y and y < self.rect.y + self.rect.height:
                return True
        return False


def lvl1():
    for x in range(15):
        createEnemy(40*x + 80, 25)
        createEnemy(40*x + 80, 55)

def lvl2():
    for x in range(15):
        createEnemy(40*x + 80, 25)
        createEnemy(45*x + 40, 55)
        createEnemy(40*x + 80, 85)

def createEnemy(x, y):
    enemy = Enemy(screen)
    enemy.rect.x = x
    enemy.rect.y = y
    enemy.inity = y
    enemy.timer = random.randint(25, 300)
    all_sprites.add(enemy)
    enemies.add(enemy)

def removeSprites():
    for pro in projectiles:
        pro.kill()
    for pro in enemyprojectiles:
        pro.kill()

# def getHighScores():
def createText(x, y, text):
    font = pygame.font.SysFont('Comic Sans MS', 25)
    textobj = font.render(text, True, (0, 0, 0))
    screen.blit(textobj,(x, y))

def displayScores(player_score):
    counter = 20
    place = 0
    score_holder = ['-1', '-1']
    place_holder = ['-1', '-1']
    top_score = False
    createText(360, 80, 'High Scores')
    for i in range(len(defaultscores)):
        if player_score > int(defaultscores[i][1]):
            #TODO ask for player name
            if top_score == False:
                score_holder[0] = defaultscores[i][0]
                score_holder[1] = defaultscores[i][1]
                defaultscores[i][0] = 'player 1'
                defaultscores[i][1] = str(player_score)
                top_score = True
            else:
                place_holder[0] = score_holder[0]
                place_holder[1] = score_holder[1]
                score_holder[0] = defaultscores[i][0]
                score_holder[1] = defaultscores[i][1]
                defaultscores[i][0] = place_holder[0]
                defaultscores[i][1] = place_holder[1]


        createText(320, 80 + counter, str(place + 1) + '.')
        createText(360, 80 + counter, defaultscores[i][0])
        createText(440, 80 + counter, defaultscores[i][1])
        counter += 20
        place += 1


def gameOver(score):
    for pro in enemies:
        pro.kill()
    removeSprites()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    gameovertext = font.render('Game Over', True, (0, 0, 0))
    screen.blit(gameovertext,(350,20))
    scoretext = font.render('Score: ' + str(score), True, (0, 0, 0))
    screen.blit(scoretext,(350,50))
    optionselected = False
    playagainbtn = button(200, 470, 'play again', screen)
    quitbtn = button(500, 470, 'quit', screen)
    displayScores(score)
    pygame.display.flip()
    while optionselected == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if playagainbtn.click(x, y):
                    optionselected = True
                elif quitbtn.click(x, y):
                    pygame.quit()
                    sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        x, y = pygame.mouse.get_pos()
        playagainbtn.hover(x,y)
        quitbtn.hover(x,y)
        pygame.display.update()
        clock.tick(30)


pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Galaga')
screen.fill((255, 255, 255))

defaultscores = [['Alice', '300'], ['Bob', '250'], ['Carol', '200'], ['Dan', '175'],
                ['Eve', '160'], ['Frank', '150'], ['Grace', '135'], ['Heidi', '100'],
                ['Ivan', '10'], ['Judy', '5']]

# sprite group initialization
player = Player()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemyprojectiles = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# labels
font = pygame.font.SysFont('Comic Sans MS', 30)
lvltext = font.render('level: 1', True, (0, 0, 0))
screen.blit(lvltext,(750,450))
scoretext = font.render('score: 0', True, (0, 0, 0))
screen.blit(scoretext,(5,0))
livestext = font.render('lives: 3', True, (0, 0, 0))
screen.blit(livestext,(5,25))

pygame.display.flip()
running = True
wonRound = True
projectiletimer = 0
score = 0
lvl = 0
lives = 3
pygame.display.flip()

while running:
    enemiesHit = pygame.sprite.spritecollide(player, enemies, True)
    if len(enemiesHit) > 0:
        if lives > 1:
            lives -= len(enemiesHit)
            if len(enemies.sprites()) == 0:
                wonRound = True
        else:
            gameOver(score)
            screen.fill((255, 255, 255))
            score = 0
            lvl = 1
            lives = 3
            lvl1()

    if wonRound == True:
        lvl += 1
        wonRound = False
        screen.fill((255, 255, 255))
        removeSprites()
        if lvl == 1:
            lvl1()
        elif lvl == 2:
            lvl2()
        else:
            lvl1()
    if projectiletimer > 2:
        projectiletimer = 0
    elif projectiletimer > 0:
        projectiletimer += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT]:
        player.moveLeft()
    if keys[pygame.K_RIGHT]:
        player.moveRight()
    if keys[pygame.K_UP] and projectiletimer == 0:
        projectile = Projectile()
        projectile.rect.x = player.rect.left + (player.rect.right - player.rect.left)/2
        projectile.rect.y = player.rect.y - 10
        all_sprites.add(projectile)
        projectiles.add(projectile)
        projectiletimer = 1
    enemies.update()
    # Check if projectile hits enemy
    for pro in projectiles:
        pro.update()
        enemiesHit = pygame.sprite.spritecollide(pro, enemies, True)
        if len(enemiesHit) > 0:
            pro.kill()
            score += 1
        if len(enemies.sprites()) == 0:
            wonRound = True
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    lvltext = font.render('level: ' + str(lvl), True, (0, 0, 0))
    scoretext = font.render('score: ' + str(score), True, (0, 0, 0))
    livestext = font.render('lives: ' + str(lives), True, (0, 0, 0))
    screen.blit(lvltext,(5,0))
    screen.blit(scoretext,(700,0))
    screen.blit(livestext,(5,25))
    pygame.display.flip()
    screen.fill((255, 255, 255))
    clock.tick(30)
pygame.quit()
