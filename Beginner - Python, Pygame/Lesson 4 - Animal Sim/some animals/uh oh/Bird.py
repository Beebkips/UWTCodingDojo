import Animal

class Bird(Animal.Animal):
    def __init__(self):
        Animal.Animal.__init__(self)
        self.char = 'B'
        self.counter = 0

    def move(self):
        self.counter += 1
        return self.counter % 2