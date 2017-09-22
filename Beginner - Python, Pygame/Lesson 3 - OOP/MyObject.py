class Circle:
    
    def __init__(self):
        self.color = 'Black'
        self.radius = 1.0
        self.x = 0.0
        self.y = 0.0

    def print_circle(self):
        print 'Color: ' + self.color
        print 'Radius: ' + str(self.radius)
        print 'X: ' + str(self.x)
        print 'Y: ' + str(self.y)

    def set_color(self, color):
        self.color = color

    def set_radius(self, radius):
        self.radius = radius

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y