import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('sprite_0.png'))
        self.images.append(load_image('sprite_1.png'))
        self.images.append(load_image('sprite_2.png'))
        self.images.append(load_image('sprite_3.png'))
        self.images.append(load_image('sprite_4.png'))
        self.images.append(load_image('sprite_5.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(1, 1, 64, 64)
        self.anim_timer = 1
        self.counter = 0

        self.speed = 10
        self.direction = 'NONE'

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.counter = (self.counter + 1) % self.anim_timer
        if self.counter == self.anim_timer - 1:
            self.index = (self.index + 1) % len(self.images)
            if self.direction == 'LEFT':
                self.image = self.images[self.index]
            elif self.direction == 'RIGHT':
                self.image = pygame.transform.flip(self.images[self.index], True, False)

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                self.direction = 'RIGHT'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and \
                self.direction != 'RIGHT':
                    self.direction = 'NONE'
            if event.key == pygame.K_RIGHT and \
                self.direction != 'LEFT':
                    self.direction = 'NONE'

        if self.direction == 'LEFT':
            self.rect.x = self.rect.x - self.speed
        elif self.direction == 'RIGHT':
            self.rect.x = self.rect.x + self.speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    clock = pygame.time.Clock()

    while True:
        clock.tick(30)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        screen.fill((255,255,255))
        my_sprite.move(event)
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()