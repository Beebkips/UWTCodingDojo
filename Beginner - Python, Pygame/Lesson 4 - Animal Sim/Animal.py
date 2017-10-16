"""

╔═╗┌┐┌┬┌┬┐┌─┐┬   ┌─┐┬ ┬
╠═╣│││││││├─┤│   ├─┘└┬┘
╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘o┴   ┴ 

"""

import random

class Animal:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = (0, 0, 0)
        self.terrarium = None

    def move(self):
        return random.randrange(4)

    def action(self, di):
        return None

class Bug(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.char = '%'

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = 'B'
        self.counter = 0

    def move(self):
        self.counter += 1
        return self.counter % 2

    def action(self, di):
        obj = self.terrarium.getSpace(self.x, self.y, di)
        # print(repr(obj), isinstance(obj[0], Bug))
        # print(type(Animal).__dict__)
        if isinstance(obj[0], Bug):
            self.terrarium.remove(obj[0])

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = 'D'
        self.counter = 0

    def move(self):
        self.counter += 1
        return math.floor(self.counter/4) % 4