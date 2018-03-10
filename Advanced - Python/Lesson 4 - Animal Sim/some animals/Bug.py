import random
import Animal

class Bug(Animal.Animal):

    def __init__(self):
        Animal.Animal.__init__(self)
        self.char = '%'
"""
    def move(self):
        return random.randrange(4)
"""