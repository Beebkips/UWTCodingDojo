import pygame

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
        # Let go of a key
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'NONE'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'NONE'

    screen.blit(blank, (x, y))
    if direction == 'LEFT':
        x = x - speed
    elif direction == 'RIGHT':
        x = x + speed

    screen.blit(ball, (x, y))
    pygame.display.flip()

# Not in the loop, don't put in the loop
pygame.quit()
