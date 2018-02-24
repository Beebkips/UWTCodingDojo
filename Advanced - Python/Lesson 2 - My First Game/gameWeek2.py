import pygame, random
# import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
screenrect = screen.get_rect()

background = pygame.Surface(screen.get_size())

background.fill((255, 255, 255))
background = background.convert()

ball = pygame.Surface((50, 50))
ball.set_colorkey((0, 0, 0))
ball = ball.convert_alpha()
pygame.draw.circle(ball, (0, 0, 255), (25, 25), 25)
# ball = ball.get_rect()

# Ball's starting coordinates
x = 175
y = 500

# This is a blank surface to cover up our animations
blank = pygame.Surface((50, 50))
blank.fill((255, 255, 255))

# A clock to run the game
clock = pygame.time.Clock()
# The frames per second
FPS = 30
# How fast the ball moves per second
moveLength = 200

# Draw the surfaces before we start
screen.blit(background, (0,0))
screen.blit(ball, (x, y))
pygame.display.flip()

# This is the loop that runs our game
run = True
# This is what direction the ball will move
direction = 'NONE'

# New code

class Laser(pygame.sprite.Sprite):

    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = spawnX + 20
        self.rect.y = spawnY - 20

    def update(self):
        self.rect.y -= 20

lasers = pygame.sprite.Group()

class Bug(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill((100, 255, 100))
        self.rect = self.image.get_rect()
        self.rect.x = spawnX
        self.rect.y = spawnY

bugs = pygame.sprite.Group()
for i in range(10):
    bugs.add(Bug(random.randrange(400), \
        random.randrange(200)))

# This is new code

while run:
    # Make the clock tick about 30 times a second
    clock.tick(FPS)
    # This is how far our ball is going to move
    # When we divide the moveLength by 30 it will
    # Move the whole length after 30 times
    speed = moveLength/FPS

    for event in pygame.event.get():
        # pygame window is closed by user
        if event.type == pygame.QUIT:
            run = False

        # Push a key down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_SPACE:
                lasers.add(Laser(x, y))

        # Let go of a key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and \
             direction != 'RIGHT':
                direction = 'NONE'
            if event.key == pygame.K_RIGHT and \
             direction != 'LEFT':
                direction = 'NONE'

# New code =======    

    screen.fill((255, 255, 255))
    for l in lasers:
        # check for collisions later
        pygame.sprite.spritecollide(l, bugs, True)
        l.update()
        if l.rect.y < -20:
            lasers.remove(l)

    lasers.draw(screen)
    bugs.draw(screen)

# this is new code =======
    screen.blit(blank, (x, y))
    if direction == 'LEFT':
        x = x - speed
    elif direction == 'RIGHT':
        x = x + speed

    screen.blit(ball, (x, y))
    pygame.display.flip()

# Not in the loop, don't put in the loop
pygame.quit()
