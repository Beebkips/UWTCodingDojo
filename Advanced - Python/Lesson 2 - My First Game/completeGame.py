import pygame, random
# import random

pygame.init()

screen = pygame.display.set_mode((400, 600))
screenrect = screen.get_rect()

background = pygame.Surface(screen.get_size())

background.fill((255, 255, 255))
background = background.convert()

# A clock to run the game
clock = pygame.time.Clock()
# The frames per second
FPS = 30
# How fast the ball moves per second
moveLength = 200

# Draw the surfaces before we start
screen.blit(background, (0,0))
pygame.display.flip()

# This is the loop that runs our game
run = True
# This is what direction the ball will move
direction = 'NONE'

# New code

# ============================================
# ============================================

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 175
        self.rect.y = 500
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, (0, 0, 255), (25, 25), 25)
        self.image.convert_alpha()

player = pygame.sprite.Group()
p = Player()
player.add(p)

# ============================================
# ============================================

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

        self.nextLaser = pygame.time.get_ticks() + \
            random.randrange(1000, 3000)

    def update(self):
        self.rect.x += random.randrange(-5,6)
        if self.rect.x > 400:
            self.rect.x = 400
        elif self.rect.x < 0:
            self.rect.x = 0
        self.rect.y += random.randrange(-5,6)
        if self.rect.y > 200:
            self.rect.y = 200
        elif self.rect.y < 0:
            self.rect.y = 0

    def laser(self):
        if self.nextLaser < pygame.time.get_ticks():
            self.nextLaser = pygame.time.get_ticks() + random.randrange(3000, 6000)
            return True
        return False

class BugLaser(pygame.sprite.Sprite):

    def __init__(self, spawnX, spawnY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = spawnX + 20
        self.rect.y = spawnY - 20

    def update(self):
        self.rect.y += 20

bugLasers = pygame.sprite.Group()

bugs = pygame.sprite.Group()
for i in range(10):
    bugs.add(Bug(random.randrange(400), \
        random.randrange(200)))

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
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_LEFT:
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                direction = 'RIGHT'
            if event.key == pygame.K_SPACE:

# ============================================
# ============================================

                lasers.add(Laser(p.rect.x, p.rect.y))

# ============================================
# ============================================

        # Let go of a key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and \
             direction != 'RIGHT':
                direction = 'NONE'
            if event.key == pygame.K_RIGHT and \
             direction != 'LEFT':
                direction = 'NONE'

    screen.fill((255, 255, 255))
    for l in lasers:
        # check for collisions later
        pygame.sprite.spritecollide(l, bugs, True)
        l.update()
        if l.rect.y < -20:
            lasers.remove(l)

    for b in bugs:
        b.update()
        if b.laser():
            bugLasers.add(BugLaser(b.rect.x, b.rect.y))

# ============================================
# ============================================

    for l in bugLasers:
        # check for collisions later
        # if pygame.sprite.spritecollide(l, player, True):
            
        l.update()
        if l.rect.y > 610:
            lasers.remove(l)

# ============================================
# ============================================

    lasers.draw(screen)
    bugs.draw(screen)
    bugLasers.draw(screen)
    
# ============================================
# ============================================

    player.draw(screen)

    if direction == 'LEFT':
        p.rect.x = p.rect.x - speed
    elif direction == 'RIGHT':
        p.rect.x = p.rect.x + speed

# ============================================
# ============================================

    pygame.display.flip()

# Not in the loop, don't put in the loop
pygame.quit()
