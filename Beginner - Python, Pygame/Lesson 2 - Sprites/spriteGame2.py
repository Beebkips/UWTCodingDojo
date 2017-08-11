import pygame
import random
 
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
    block.rect.y = random.randrange(screen_height)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
run = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0

# -------- Main Program Loop -----------
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
        elif event.type == pygame.KEYDOWN:
           # draw blank surface to erase ball
            if event.key == pygame.K_ESCAPE:
                run = False
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list:
        size = 5
        score += 1
        player.rect.w += size
        player.rect.h += size
        player.image = pygame.Surface([player.rect.w, player.rect.h])
        player.image.fill(RED)
        pygame.display.set_caption('Score: ' + str(score))
 
    for blockSprite in block_list:
        blockSprite.rect.x += random.randrange(-5, 5)
        blockSprite.rect.y += random.randrange(-5, 5)
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
    clock.tick(60)
 
pygame.quit()