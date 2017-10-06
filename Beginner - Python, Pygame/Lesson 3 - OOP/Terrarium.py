from __future__ import print_function
import sys

class Terrarium:

    def __init__(self):
        self.w = 5
        self.h = 5
        self.terrarium = [['.' for x in range(self.w)] for y in range(self.h)]
        self.animal = None

    def add(self, animal):
        self.animal = animal
        self.terrarium[0][0] = self.animal.char
        self.animal.x = 0
        self.animal.y = 0

    def move(self):
        dir = self.animal.move()
        self.terrarium[self.animal.x][self.animal.y] = '.'
        if dir == 0:
            self.animal.x = (self.animal.x - 1 + 5) % 5
        elif dir == 1:
            self.animal.y = (self.animal.y - 1 + 5) % 5 
        elif dir == 2:
            self.animal.x = (self.animal.x + 1) % 5
        elif dir == 3:
            self.animal.y = (self.animal.y + 1) % 5

        self.terrarium[self.animal.x][self.animal.y] = self.animal.char

    def toString(self):
        for i in range(self.w):
            for j in range(self.h):
                print(self.terrarium[i][j], end='')
            print()
        print()