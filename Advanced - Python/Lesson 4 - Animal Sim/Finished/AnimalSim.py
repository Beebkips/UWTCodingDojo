# -*- coding: utf-8 -*-

"""

╔═╗┌┐┌┬┌┬┐┌─┐┬  ╔═╗┬┌┬┐ ┌─┐┬ ┬
╠═╣│││││││├─┤│  ╚═╗││││ ├─┘└┬┘
╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘╚═╝┴┴ ┴o┴   ┴ 

"""

from Animal import *
from Terrarium import Terrarium
import time
import pygame

def add(terrarium):
    for i in range(100): 
        terrarium.add(Bug())
    # terrarium.add(Bug(), 1, 1)
    # terrarium.add(Bug(), 2, 2)
    for i in range(25):
        terrarium.add(Bird())
    for i in range(25):
        terrarium.add(Turtle())
    for i in range(25):
        terrarium.add(Dog())
"""

╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗  ╔╦╗╔═╗╦ ╦╔═╗╦ ╦
 ║║║ ║  ║║║║ ║ ║    ║ ║ ║║ ║║  ╠═╣
═╩╝╚═╝  ╝╚╝╚═╝ ╩    ╩ ╚═╝╚═╝╚═╝╩ ╩
The stuff below, it will break.

"""

def drawAnimals(terrarium, screen, surface, aniDotWidth, aniDotHeight, font):
    for animal in terrarium.animals:
        if font != None:
            text = font.render(animal.char, 1, (10, 10, 10))
            textpos = text.get_rect()
            screen.blit(text, (animal.x * aniDotWidth, animal.y * aniDotHeight))
        else:
            screen.blit(surface, (animal.x * aniDotWidth, animal.y * aniDotHeight))

def main():

    terrarium = Terrarium()
    add(terrarium)

    pygame.init()

    screenWidth = 680
    screenHeight = 680
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

    font = pygame.font.Font(pygame.font.get_default_font(), int(aniDotWidth))
    drawAnimals(terrarium, screen, blanksurface, aniDotWidth, aniDotHeight, None)
    drawAnimals(terrarium, screen, squaresurface, aniDotWidth, aniDotHeight, font)
    pygame.display.flip()
    time.sleep(1)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        drawAnimals(terrarium, screen, blanksurface, aniDotWidth, aniDotHeight, None)
        terrarium.move()
        drawAnimals(terrarium, screen, squaresurface, aniDotWidth, aniDotHeight, font)
        # terrarium.toString()

        pygame.display.flip()
        time.sleep(.1)
        # print(len(terrarium.animals))

    pygame.quit()


if __name__ == '__main__':
    main()
