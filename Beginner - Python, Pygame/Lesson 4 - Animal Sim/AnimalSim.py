from Bug import Bug
from Terrarium import Terrarium
import time
import pygame

# def drawTerrarium(terrarium):
#     for i in range(terrarium.w):
#         for j in range(terrarium.h):

def drawAnimals(terrarium, screen, surface, aniDotWidth, aniDotHeight):
    for animal in terrarium.animals:
        screen.blit(surface, (animal.x * aniDotWidth, animal.y * aniDotHeight))

def main():

    terrarium = Terrarium()
    terrarium.add(Bug())
    terrarium.add(Bug())

    pygame.init()

    screenWidth = 400
    screenHeight = 400
    aniDotWidth = screenWidth/terrarium.w
    aniDotHeight = screenHeight/terrarium.h
    # print(aniDotWidth, aniDotHeight)
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    screenrect = screen.get_rect()
    background = pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    background = background.convert()
    screen.blit(background, (0,0))

    # squaresurface = pygame.Surface((aniDotWidth, aniDotHeight))
    squaresurface = pygame.Surface((40, 40))
    squaresurface.fill((0, 0, 0))
    square = squaresurface.get_rect()

    blanksurface = pygame.Surface((aniDotWidth, aniDotHeight))
    blanksurface.fill((255, 255, 255))

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        drawAnimals(terrarium, screen, blanksurface, aniDotWidth, aniDotHeight)
        terrarium.move()
        drawAnimals(terrarium, screen, squaresurface, aniDotWidth, aniDotHeight)
        # terrarium.toString()

        pygame.display.flip()
        time.sleep(.1)

    pygame.quit()


if __name__ == '__main__':
    main()