# Animal Sim
---
### Animal

Fields
* `x` - x position of animal in terrarium grid
* `y` - y position of animal in terrarium grid
* `char` - the character representing the animal
* `di` - an integer representation of the direction the animal is heading represented by an integer value from {North:0, East:1, South:2, West:3)
* `color` - the color value for the drawn character (default:black)
* `terrarium` - the current terrarium object the animal is in
*  `mateTimer` - The amount of ticks between the 'MATE' action that the animal can perform (default:50)
*  `food` - The amount of ticks before the animal starves, eating food resets this timer (default:50)

Methods
* `move` - by default returns a random integer inclusive (0 to 3), called every tick by the terrarium
* `action` - by default does nothing, called every tick by the terrarium
* `do` - takes in a string representing an action that can be performed by an animal 
    * `'NONE'` - performs no action
    * `'EAT` - removes the object from the terrarium the direction the animal is currently facing and resets the food timer
    * `'MATE'` - populates an empty square next to the animal with the same type of animal
    * `'DIE'` - removes self from the terrarium
* `view` - returns a string of the current object that the animal is looking at, returns 'NoneType' if empty

---
### Sample Animal

```python
# All new animals must be added below the Animal class so they will be imported by default into AnimalSim.py

import random

# Animal Class
class Animal:
 # . . .
 
# +--------------------
# | Simple new animal example
# | Bug only overwrites the 'action' method
# +--------------------

# make sure to inherit from Animal
class Bug(Animal):

    # init
    def __init__(self):
        # class Animal init
        Animal.__init__(self)
        # set Bug character
        self.char = '%'

    # give Bug an action to perform
    def action(self):
        # check if it sees a bug
        if self.view() == 'Bug':
            # mate with bug
            self.do('MATE')
```

More complicated animal example
```python
# make sure to inherit from Animal

class Bird(Animal):
    # init
    def __init__(self):
        Animal.__init__(self)
        self.char = 'B'
        # add a counter for movement
        self.counter = 0
        # add a modifier to randomize bird direction
        self.mod = random.randrange(4)
        # change mate timer so birds can mate more often
        self.mateTimer = 5
        # birds can survive 200 ticks without food
        self.food = 200

    # override move method
    def move(self):
        # remove bird if it 'starves'
        if self.food < 0:
            self.do('DIE')
        # otherwise tick food down by 1
        else:
            self.food -= 1
        # increase movement counter
        self.counter += 1
        # birds only move in a L direction 
        # ex (NORTH -> EAST), (EAST -> SOUTH), ...
        return ((self.counter % 2) + self.mod) % 4

    def action(self):
        # if the bird is looking at a bug 'EAT' it
        if self.view() == 'Bug':
            self.do('EAT')
            # decrease mate timer, birds can mate after eating 5 bugs
            self.mateTimer -= 1
            # Move in a new random direction
            self.mod = random.randrange(4)
            # reset food timer
            self.food = 200
        # if the bird is looking at another bird try to 'MATE'
        # 'do()' method will prevent if mateTimer is not 0 or less
        if self.view() == 'Bird':
            self.do('MATE')
            self.mateTimer = 5
```
