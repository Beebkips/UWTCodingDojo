import pygame
import random

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

pygame.init()

screenWidth = 700
screenHeight = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Score: 0')

player = Player()

run = True
clock = pygame.time.Clock()
score = 0
tickRate = 60
speed = 30

blockList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()
allSpritesList.add(player)

# Movement variables
UP = False
DOWN = False
LEFT = False
RIGHT = False

nextJump = pygame.time.get_ticks()
lastJump = pygame.time.get_ticks()
touchedFloor = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP and nextJump < pygame.time.get_ticks() \
               and touchedFloor:
                UP = True
                nextJump = pygame.time.get_ticks() + 500
                lastJump = pygame.time.get_ticks()
                touchedFloor = False
            if event.key == pygame.K_DOWN:
                DOWN = True
            if event.key == pygame.K_LEFT:
                LEFT = True
            if event.key == pygame.K_RIGHT:
                RIGHT = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                UP = False
            if event.key == pygame.K_DOWN:
                DOWN = False
            if event.key == pygame.K_LEFT:
                LEFT = False
            if event.key == pygame.K_RIGHT:
                RIGHT = False

    if nextJump < pygame.time.get_ticks():
        UP = False
    
    # Moves player around when key is pressed
    if UP:
        player.rect.y -= 15
    if DOWN:
        player.rect.y += 10
    if LEFT:
        player.rect.x -= 10
    if RIGHT:
        player.rect.x += 10

    player.rect.y += 7

    # Keeps player inside screen
    if player.rect.y > screenHeight - 30:
        player.rect.y = screenHeight - 30
        touchedFloor = True
    if player.rect.x > screenWidth - 15:
        player.rect.x = screenWidth - 15
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.x < 0:
        player.rect.x = 0

    screen.fill(WHITE)
    allSpritesList.draw(screen)
    pygame.display.flip()
    clock.tick(tickRate)

pygame.quit()
