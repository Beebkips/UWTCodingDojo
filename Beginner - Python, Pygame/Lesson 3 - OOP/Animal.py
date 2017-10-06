import random

class Animal:

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self):
        return random.randrange(4)