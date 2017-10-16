from __future__ import print_function

"""

╔╦╗┌─┐┬─┐┬─┐┌─┐┬─┐┬┬ ┬┌┬┐ ┌─┐┬ ┬
 ║ ├┤ ├┬┘├┬┘├─┤├┬┘││ ││││ ├─┘└┬┘
 ╩ └─┘┴└─┴└─┴ ┴┴└─┴└─┘┴ ┴o┴   ┴ 

"""

"""

╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗  ╔╦╗╔═╗╦ ╦╔═╗╦ ╦
 ║║║ ║  ║║║║ ║ ║    ║ ║ ║║ ║║  ╠═╣
═╩╝╚═╝  ╝╚╝╚═╝ ╩    ╩ ╚═╝╚═╝╚═╝╩ ╩
Any of this for now.
"""

import sys, os

class Terrarium:

    def __init__(self):
        self.w = 10
        self.h = 10
        # self.terrarium = [['.' for x in range(self.w)] for y in range(self.h)]
        self.terrarium = [[None for x in range(self.w)] for y in range(self.h)]
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)
        animal.terrarium = self
        # print(len(self.animals))

        ## ===
        ## Char array
        # self.terrarium[0][0] = self.animals[len(self.animals) - 1].char
        # self.animals[len(self.animals) - 1].x = 0
        # self.animals[len(self.animals) - 1].y = 0
        ## ===

        # ===
        # Object array
        self.terrarium[0][0] = animal
        animal.x = 0
        animal.y = 0
        # ===

    def remove(self, animal):
        self.terrarium[animal.x][animal.y] = None
        self.animals.remove(animal)

    def move(self):
        for animal in self.animals:
            di = animal.move()
            animal.action(di)
            if self.getSpace(animal.x, animal.y, di)[0] == None:
                self.terrarium[animal.x][animal.y] = None
                if di == 0:
                    animal.x = (animal.x - 1 + self.w) % self.w
                elif di == 1:
                    animal.y = (animal.y - 1 + self.h) % self.h
                elif di == 2:
                    animal.x = (animal.x + 1) % self.w
                elif di == 3:
                    animal.y = (animal.y + 1) % self.h

                self.terrarium[animal.x][animal.y] = animal

    # def move(self):
    #     for animal in self.animals:
    #         di = animal.move()
    #         if self.getSpace(animal.x, animal.y, di)[0] == '.':
    #             self.terrarium[animal.x][animal.y] = '.'
    #             if di == 0:
    #                 animal.x = (animal.x - 1 + self.w) % self.w
    #             elif di == 1:
    #                 animal.y = (animal.y - 1 + self.h) % self.h
    #             elif di == 2:
    #                 animal.x = (animal.x + 1) % self.w
    #             elif di == 3:
    #                 animal.y = (animal.y + 1) % self.h

    #             self.terrarium[animal.x][animal.y] = animal.char

    ## ===
    ## Char array
    # def getSpace(self, x, y, di):
    #     if di == 0:
    #         x = (x - 1 + self.w) % self.w
    #     elif di == 1:
    #         y = (y - 1 + self.h) % self.h
    #     elif di == 2:
    #         x = (x + 1) % self.w
    #     elif di == 3:
    #         y = (y + 1) % self.h
    #     return self.terrarium[x][y], x, y
    ## ===

    # ===
    # Object Array
    def getSpace(self, x, y, di):
        if di == 0:
            x = (x - 1 + self.w) % self.w
        elif di == 1:
            y = (y - 1 + self.h) % self.h
        elif di == 2:
            x = (x + 1) % self.w
        elif di == 3:
            y = (y + 1) % self.h
        return self.terrarium[x][y], x, y
    # ===

    def getBoard():
        return self.terrarium

    def toString(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(self.w):
            for j in range(self.h):
                sys.stdout.write(self.terrarium[i][j])
            sys.stdout.write('\n')
        sys.stdout.write('\n')
        sys.stdout.flush()

"""
    def toString(self):
        for i in range(self.w):
            for j in range(self.h):
                print(self.terrarium[i][j], end='')
            print()
        print()
"""