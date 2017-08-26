import pygame
import random

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,30])
        self.image.fill(RED)

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

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(tickRate)

pygame.quit()
