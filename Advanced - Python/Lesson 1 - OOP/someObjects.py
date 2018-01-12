class MyObject:

    # This is a constructor you use it to make
    # the python object
    def __init__(self):
        # These are fields they are the attributes of the object
        self.Attribute1 = 0
        self.Attribute2 = "Thing"

    # This is an object method that we can use on the object
    def toString(self):
        return self.Attribute2

class echoObject:

    def __init__(self):
        self.totalEchos = 0

    def echo(self, string):
        self.totalEchos += 1
        print('You said: ' + string)
        print('I have echoed ' + str(self.totalEchos) + ' times')

class Pizza:

    def __init__(self):
        self.sauce = 'tomato'
        self.cheese = 'mozzarella'
        self.meat = 'pepperoni'

    def setSauce(self, theSauce):
        self.sauce = theSauce

    def setCheese(self, cheese):
        self.cheese = theCheese

    def setMeat(self, theMeat):
        self.meat = theMeat

    def toString(self):
        print('This pizza has:')
        print('Sauce: ' + self.sauce)
        print('Cheese: ' + self.cheese)
        print('Meat: ' + self.meat)

class betterPizza:

    def __init__(self):
        self.toppings = ['Mozzarella cheese', 'Tomato sauce', 'Pepperoni']

    def toString(self):
        for item in self.toppings:
            print(item)

class anEvenBetterPizza:

    def __init__(self):
        self.toppings = {'cheese' : 'Mozzarella cheese', 'sauce' : 'Tomato sauce', 'meat' : 'Pepperoni'}

    def setSauce(self, theSauce):
        self.toppings['sauce'] = theSauce

    def setCheese(self, cheese):
        self.toppings['cheese'] = theCheese

    def setMeat(self, theMeat):
        self.toppings['meat'] = theMeat

    def toString(self):
        for item in self.toppings.keys():
            print(item + ' ' + self.toppings[item])


def main():
    aObject = MyObject()
    aObject.toString()

    echo = echoObject()

    for i in range(5):
        echo.echo('Hello')
    print()

    pizza1 = Pizza()
    pizza1.toString()
    print()

    pizza2 = betterPizza()
    pizza2.toString()
    print()

    pizza3 = anEvenBetterPizza()
    pizza3.toString()

if __name__ == "__main__":
    main()