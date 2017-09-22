import pygame
import random
<<<<<<< HEAD
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class Player(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
 
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([15, 30])
        self.image.fill(RED)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

def randomColor():
    R = random.randrange(255)
    G = random.randrange(255)
    B = random.randrange(255)
    return (R, G, B)

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Score: 0')
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(50):
    # This represents a block
    block = Block(randomColor(), 20, 15)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height/2)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
run = True
 
# Used to manage how fast the screen updates
=======

RED = (255, 0, 0)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([15,30])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

pygame.init()

screenWidth = 700
screenHeight = 400
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption('Score: 0')

player = Player()

run = True
>>>>>>> e58b130b6755de6ec026772b4fad38e910cf5360
clock = pygame.time.Clock()
score = 0
tickRate = 60
speed = 30

<<<<<<< HEAD
# -------- Main Program Loop -----------
while run:

    dpf = speed/tickRate

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        elif event.type == pygame.KEYDOWN:
           # draw blank surface to erase ball
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP:
                player.rect.y = player.rect.y - 10
            if event.key == pygame.K_DOWN:
                player.rect.y = player.rect.y + 10
            if event.key == pygame.K_LEFT:
                player.rect.x = player.rect.x - 10
            if event.key == pygame.K_RIGHT:
                player.rect.x = player.rect.x + 10

    if UP:
        player.rect.y = player.rect.y - 10
    if DOWN:
        player.rect.y = player.rect.y + 10
    if LEFT:
        player.rect.x = player.rect.x - 10
    if RIGHT:
        player.rect.x = player.rect.x + 10

    print 30/float(tickRate)
    player.rect.y = player.rect.y + (60/float(tickRate))
    if player.rect.y > screen_height - 30:
        player.rect.y = screen_height - 30
 
    # Clear the screen
    screen.fill(WHITE)
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        size = 5
        score += 1
        pygame.display.set_caption('Score: ' + str(score))
 
    for blockSprite in block_list:
        blockSprite.rect.x += random.randrange(-5, 6)
        blockSprite.rect.y += random.randrange(-5, 6)
        if blockSprite.rect.x > screen_width:
            blockSprite.rect.x = screen_width
        elif blockSprite.rect.x < 0:
            blockSprite.rect.x = 0
        elif blockSprite.rect.y > screen_height:
            blockSprite.rect.y = screen_height
        elif blockSprite.rect.y < 0:
            blockSprite.rect.y = 0

    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(tickRate)
 
pygame.quit()
=======
blockList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()
allSpritesList.add(player)

# Movement variables
UP = False
DOWN = False
LEFT = False
RIGHT = False

nextJump = pygame.time.get_ticks()
lastJump = pygame.time.get_ticks()
touchedFloor = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_UP and nextJump < pygame.time.get_ticks() \
               and touchedFloor:
                UP = True
                nextJump = pygame.time.get_ticks() + 500
                lastJump = pygame.time.get_ticks()
                touchedFloor = False
            if event.key == pygame.K_DOWN:
                DOWN = True
            if event.key == pygame.K_LEFT:
                LEFT = True
            if event.key == pygame.K_RIGHT:
                RIGHT = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                UP = False
            if event.key == pygame.K_DOWN:
                DOWN = False
            if event.key == pygame.K_LEFT:
                LEFT = False
            if event.key == pygame.K_RIGHT:
                RIGHT = False

    if nextJump < pygame.time.get_ticks():
        UP = False
    
    # Moves player around when key is pressed
    if UP:
        player.rect.y -= 15
    if DOWN:
        player.rect.y += 10
    if LEFT:
        player.rect.x -= 10
    if RIGHT:
        player.rect.x += 10

    player.rect.y += 7

    # Keeps player inside screen
    if player.rect.y > screenHeight - 30:
        player.rect.y = screenHeight - 30
        touchedFloor = True
    if player.rect.x > screenWidth - 15:
        player.rect.x = screenWidth - 15
    if player.rect.y < 0:
        player.rect.y = 0
    if player.rect.x < 0:
        player.rect.x = 0

    screen.fill(WHITE)
    allSpritesList.draw(screen)
    pygame.display.flip()
    clock.tick(tickRate)

pygame.quit()
>>>>>>> e58b130b6755de6ec026772b4fad38e910cf5360
