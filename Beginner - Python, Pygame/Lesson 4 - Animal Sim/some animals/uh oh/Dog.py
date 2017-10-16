import Animal
import math

class Dog(Animal.Animal):
    def __init__(self):
        Animal.Animal.__init__(self)
        self.char = 'D'
        self.counter = 0

    def move(self):
        self.counter += 1
        return math.floor(self.counter/4) % 4
