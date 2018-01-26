'''
Gliding movement of ball object

'''

import pygame

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'NONE'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'NONE'

    # Erase ball from screen by drawing blank surface over it
    screen.blit(blanksurface, (x, y))
    # Move the ball according to the current direction chosen at
    # the specified speed
    if direction == 'LEFT':
        x = x - speed
    elif direction == 'RIGHT':
        x = x + speed

    screen.blit(ballsurface, (x, y))
    pygame.display.flip()

pygame.quit()