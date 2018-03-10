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

import sys, os, random

class Terrarium:

    def __init__(self):
        self.w = 50
        self.h = 50
        self.terrarium = [[None for x in range(self.w)] for y in range(self.h)]
        self.animals = []

    def add(self, animal, x=None, y=None):
        self.animals.append(animal)
        animal.terrarium = self

        # ===
        # Object array
        if x is None and y is None:
            x, y = random.randrange(self.w), random.randrange(self.h)
            self.terrarium[x][y] = animal
            animal.x = x
            animal.y = y
        else:
            self.terrarium[x][y] = animal
            animal.x = x
            animal.y = y
        # ===

    def remove(self, animal):
        self.terrarium[animal.x][animal.y] = None
        self.animals.remove(animal)

    def move(self):
        for animal in self.animals:
            animal.di = animal.move()
            animal.action()
            if self.getSpace(animal.x, animal.y, animal.di)[0] == None:
                self.terrarium[animal.x][animal.y] = None
                if animal.di == 0:
                    animal.x = (animal.x - 1 + self.w) % self.w
                elif animal.di == 1:
                    animal.y = (animal.y - 1 + self.h) % self.h
                elif animal.di == 2:
                    animal.x = (animal.x + 1) % self.w
                elif animal.di == 3:
                    animal.y = (animal.y + 1) % self.h

                self.terrarium[animal.x][animal.y] = animal

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
