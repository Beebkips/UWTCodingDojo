import pygame
import sys
import random

W = 20
H = 20
grid = [[0 for i in range(W)] for j in range(H)]

blackSquare = pygame.Surface((25, 25))
blackSquare.fill((0, 0, 0))

whiteSquare = pygame.Surface((25, 25))
whiteSquare.fill((255, 255, 255))

def randomGrid():
    for i in range(W):
        for j in range(H):
            grid[i][j] = random.randrange(2)

def drawGrid(screen):
    for i in range(W):
        for j in range(H):
            if grid[i][j] == 1:
                screen.blit(blackSquare, (i * 25, j * 25))
            else:
                screen.blit(whiteSquare, (i * 25, j * 25))

def updateCells():
    tempGrid = [[0 for i in range(W)] for j in range(H)]
    for i in range(W):
        for j in range(H):
            neighbors = checkCell(i, j)
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                tempGrid[i][j] = 0
            elif grid[i][j] == 1 and (neighbors == 2 or neighbors == 3):
                tempGrid[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                tempGrid[i][j] = 1 

    for i in range(W):
        for j in range(H):
            grid[i][j] = tempGrid[i][j]
    

def checkCell(i, j):
    count = 0
    for k in range(-1, 2, 1):
        for l in range(-1, 2, 1):
            count += grid[(i + k) % W][(j + l) % H]
    return count - grid[i][j]

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    randomGrid()

    while True:

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        screen.fill((255, 255, 255))
        grid = updateCells()
        # print(grid)
        drawGrid(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()