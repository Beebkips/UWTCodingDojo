"""

DO NOT TOUCH

"""

import random, math

class Animal:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.char = 'A'
        self.di = None
        self.color = (0, 0, 0)
        self.terrarium = None
        self.copyTimer = 50
        self.food = 50

    def move(self):
        self.copyTimer -= 1
        return random.randrange(4)

    def action(self):
        return None

    def do(self, action):
        if action == 'NONE':
            pass
        elif action == 'EAT':
            obj = self.terrarium.getSpace(self.x, self.y, self.di)
            print('EATING ' + str(obj[0]), obj[0].x, obj[0].y)
            self.terrarium.remove(obj[0])
        elif action == 'COPY':
            done = True
            i = 0
            if self.copyTimer <= 0:
                while(done and i < 4):
                    obj = self.terrarium.getSpace(self.x, self.y, i)
                    if obj[0].__class__.__name__ == 'NoneType':
                        self.terrarium.add(self.__class__(), obj[1], obj[2])
                        done = False
                        self.copyTimer = 50
                        print(self.__class__.__name__ + ' ADDED: ', obj[0].__class__.__name__, i)
                    i += 1
        elif action == 'DIE':
            self.terrarium.remove(self)
            print(self.__class__.__name__ + ' DIED ' + str(self), self.x, self.y)

    def view(self):
        return self.terrarium.getSpace(self.x, self.y, self.di)[0].__class__.__name__
"""

DO NOT TOUCH

"""

"""
Add any new animal classes below this comment.
They will be automatically imported into the AnimalSim.
"""

class Bug(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.char = '%'

    def move(self):
        self.copyTimer -= 1
        return random.randrange(4)

    def action(self):
        if random.randrange(100) == 0:
            self.do('DIE')
        elif self.view() == 'Bug':
            self.do('COPY')

class Bird(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.char = 'B'
        self.counter = 0
        self.mod = random.randrange(4)
        self.copyTimer = 5
        self.food = 100

    def move(self):
        if self.food < 0:
            self.do('DIE')
        else:
            self.food = self.food - 1
        self.counter += 1
        return ((self.counter % 2) + self.mod) % 4

    def action(self):
        if self.view() == 'Bug':
            self.do('EAT')
            self.copyTimer -= 1
            self.mod = random.randrange(4)
            self.food = 100
        if self.view() == 'Bird':
            self.do('COPY')
            self.copyTimer = 5

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = 'C'
        self.counter = 0
        self.food = 500

    def move(self):
        if self.food < 0:
            self.do('DIE')
        else:
            self.food = self.food - 1
        self.counter += 1
        return math.floor(self.counter/4) % 4

    def action(self):
        if self.view() == 'Bird':
            print(self.view())
            self.do('EAT')
            self.copyTimer -= 1
            self.food = 500
        if self.view() == 'Cat':
            self.do('COPY')
            self.copyTimer = 15
