'''
Gliding movement of ball object

'''

import pygame, random

pygame.init()
run = True

# background
screen = pygame.display.set_mode((400,600))
screenrect = screen.get_rect()
background = pygame.Surface(screen.get_size())
background.fill((255,255,255))
background = background.convert()

# ball
ballsurface = pygame.Surface((50,50))
ballsurface.set_colorkey((0,0,0))
pygame.draw.circle(ballsurface, (0,0,255), (25, 25), 25)
ballsurface = ballsurface.convert_alpha()
ballrect = ballsurface.get_rect()
x = 175
y = 500

# blank surface
blanksurface = pygame.Surface((50,50))
blanksurface.fill((255, 255, 255))

# FPS and speed
clock = pygame.time.Clock()
# Frames per second
FPS = 30
# Set how far you want the ball to move every second
moveLength = 200

screen.blit(background, (0,0))
screen.blit(ballsurface, (x, y))
pygame.display.flip()

direction = 'NONE'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# NEW CODE BELOW

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

# Hold all the lasers we make
lasers = pygame.sprite.Group()

class Bug(pygame.sprite.Sprite):
    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill((100, 255, 100))
        self.rect = self.image.get_rect()
        self.rect.x = spawnX
        self.rect.y = spawnY

# Hold all the bugs we make
bugs = pygame.sprite.Group()
for i in range(10):
    bugs.add(Bug(random.randrange(400), random.randrange(200)))

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

while run:
    # Make the pygame tick 30 milliseconds
    clock.tick(FPS)
    # Set the distance the ball is moving to the
    # length/FPS so it will move the entire length
    # over one second
    speed = moveLength/FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            # Check what key has been pressed and set
            # the ball direction to it
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# NEW CODE BELOW

            if event.key == pygame.K_SPACE:
                lasers.add(Laser(x,y))

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'NONE'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'NONE'

    # Erase ball from screen by drawing blank surface over it
    # screen.blit(blanksurface, (x, y))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# NEW CODE BELOW
    
    screen.fill((255,255,255))
    for l in lasers:
        pygame.sprite.spritecollide(l, bugs, True)
        l.update()
        if l.rect.y < -20:
            lasers.remove(l)

    lasers.draw(screen)
    bugs.draw(screen)


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # Move the ball according to the current direction chosen at
    # the specified speed
    if direction == 'LEFT':
        x = x - speed
    elif direction == 'RIGHT':
        x = x + speed

    screen.blit(ballsurface, (x, y))
    pygame.display.flip()

pygame.quit()