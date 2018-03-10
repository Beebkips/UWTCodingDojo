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
