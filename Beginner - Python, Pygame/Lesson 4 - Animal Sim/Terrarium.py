from __future__ import print_function
import sys, os

class Terrarium:

    def __init__(self):
        self.w = 10
        self.h = 10
        self.terrarium = [['.' for x in range(self.w)] for y in range(self.h)]
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)
        # print(len(self.animals))
        self.terrarium[0][0] = self.animals[len(self.animals) - 1].char
        self.animals[len(self.animals) - 1].x = 0
        self.animals[len(self.animals) - 1].y = 0

    def move(self):
        for animal in self.animals:
            dir = animal.move()
            self.terrarium[animal.x][animal.y] = '.'
            if dir == 0:
                animal.x = (animal.x - 1 + self.w) % self.w
            elif dir == 1:
                animal.y = (animal.y - 1 + self.h) % self.h
            elif dir == 2:
                animal.x = (animal.x + 1) % self.w
            elif dir == 3:
                animal.y = (animal.y + 1) % self.h

            self.terrarium[animal.x][animal.y] = animal.char

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