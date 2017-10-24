"""

╔═╗┌┐┌┬┌┬┐┌─┐┬   ┌─┐┬ ┬
╠═╣│││││││├─┤│   ├─┘└┬┘
╩ ╩┘└┘┴┴ ┴┴ ┴┴─┘o┴   ┴ 

"""

"""

╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗  ╔╦╗╔═╗╦ ╦╔═╗╦ ╦
 ║║║ ║  ║║║║ ║ ║    ║ ║ ║║ ║║  ╠═╣
═╩╝╚═╝  ╝╚╝╚═╝ ╩    ╩ ╚═╝╚═╝╚═╝╩ ╩

"""

import random

class Animal:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.char = 'A'
        self.di = None
        self.color = (0, 0, 0)
        self.terrarium = None
        self.mateTimer = 50
        self.food = 50

    def move(self):
        self.mateTimer -= 1
        return random.randrange(4)

    def action(self):
        return None

    def do(self, action):
        if action == 'NONE':
            pass
        elif action == 'EAT':
            obj = self.terrarium.getSpace(self.x, self.y, self.di)
            self.terrarium.remove(obj[0])
        elif action == 'MATE':
            done = True
            i = 0
            if self.mateTimer <= 0:
                while(done and i < 4):
                    obj = self.terrarium.getSpace(self.x, self.y, i)
                    if obj[0].__class__.__name__ == 'NoneType':
                        self.terrarium.add(self.__class__(), obj[1], obj[2])
                        done = False
                        self.mateTimer = 50
                        print(self.__class__.__name__ + ' ADDED: ', obj[0].__class__.__name__, i)
                    i += 1
        elif action == 'DIE':
            self.terrarium.remove(self)
            print(self.__class__.__name__ + ' DIED')

    def view(self):
        return self.terrarium.getSpace(self.x, self.y, self.di)[0].__class__.__name__
"""

╔╦╗╔═╗  ╔╗╔╔═╗╔╦╗  ╔╦╗╔═╗╦ ╦╔═╗╦ ╦
 ║║║ ║  ║║║║ ║ ║    ║ ║ ║║ ║║  ╠═╣
═╩╝╚═╝  ╝╚╝╚═╝ ╩    ╩ ╚═╝╚═╝╚═╝╩ ╩

"""

"""
Add any new animal classes below this comment.
They will be automatically imported into the AnimalSim.
"""
class Bug(Animal):

    def __init__(self):
        Animal.__init__(self)
        self.char = '%'

    def action(self):
        if self.view() == 'Bug':
            self.do('MATE')

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = 'B'
        self.counter = 0
        self.mod = random.randrange(4)
        self.mateTimer = 5
        self.food = 100

    def move(self):
        if self.food < 0:
            self.do('DIE')
        else:
            self.food -= 1
        self.counter += 1
        return ((self.counter % 2) + self.mod) % 4

    def action(self):
        if self.view() == 'Bug':
            self.do('EAT')
            self.mateTimer -= 1
            self.mod = random.randrange(4)
            self.food = 100
        if self.view() == 'Bird':
            self.do('MATE')
            self.mateTimer = 5

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = 'D'
        self.counter = 0

    def move(self):
        self.counter += 1
        return math.floor(self.counter/4) % 4

class Turtle(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.char = '@'
        self.spooked = False

    def move(self):
        if self.spooked:
            return -1
        else:
            return random.randrange(4)

    def action(self):
        if self.view() != 'NoneType':
            self.spooked = True