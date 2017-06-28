import pygame

pygame.init()
run = True

# background
screen = pygame.display.set_mode((640,480))
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
x = 550
y = 240

# blank surface
blanksurface = pygame.Surface((50,50))
blanksurface.fill((255, 255, 255))

screen.blit(background, (0,0))
screen.blit(ballsurface, (x, y))
pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False # pygame window closed by user
        elif event.type == pygame.KEYDOWN:
            screen.blit(blanksurface, (x, y))
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP:
                y = y - 10
            if event.key == pygame.K_DOWN:
                y = y + 10
            if event.key == pygame.K_LEFT:
                x = x - 10
            if event.key == pygame.K_RIGHT:
                x = x + 10
    screen.blit(ballsurface, (x, y))
    pygame.display.flip()

pygame.quit()


    
