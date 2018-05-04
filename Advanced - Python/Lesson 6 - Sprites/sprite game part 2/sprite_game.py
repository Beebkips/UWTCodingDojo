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
        self.rect = pygame.Rect(1, 1, 100, 100)
        self.anim_timer = 1
        self.counter = 0

        self.speed = 10
        self.direction = 'NONE'

    def update(self):
        self.counter = (self.counter + 1) % self.anim_timer
        if self.counter == self.anim_timer - 1:
            self.index = (self.index + 1) % len(self.images)
            if self.direction == 'LEFT':
                self.image = self.images[self.index]
            elif self.direction == 'RIGHT':
                self.image = \
                    pygame.transform.flip\
                    (self.images[self.index], True, False)

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
        if self.direction == 'RIGHT':
            self.rect.x = self.rect.x + self.speed
        if self.rect.y < 275:
            self.rect.y += 10
        if self.rect.x > 500 and self.direction == 'RIGHT':
            self.rect.x = -150
        if self.rect.x < -150 and self.direction == 'LEFT':
            self.rect.x = 600

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

        my_group.update()
        screen.fill((255, 255, 255))
        my_sprite.move(event)
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
