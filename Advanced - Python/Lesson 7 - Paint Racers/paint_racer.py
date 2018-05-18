import pygame
import sys

grid = [[0 for i in range(20)] for j in range(20)]

class PlayerOneSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerOneSprite, self).__init__()
        self.size = 25
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self):
        grid[self.rect.x//self.size - 1]\
            [self.rect.y//self.size - 1] = 1

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.rect.x = (self.rect.x - self.size) % 500
            if event.key == pygame.K_RIGHT:
                self.rect.x = (self.rect.x + self.size) % 500
            if event.key == pygame.K_DOWN:
                self.rect.y = (self.rect.y + self.size) % 500
            if event.key == pygame.K_UP:
                self.rect.y = (self.rect.y - self.size) % 500

class PlayerTwoSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(PlayerTwoSprite, self).__init__()
        self.size = 25
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 475
        self.rect.y = 475

    def update(self):
        grid[self.rect.x//self.size - 1]\
            [self.rect.y//self.size - 1] = 2

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.rect.x = (self.rect.x - self.size) % 500
            if event.key == pygame.K_d:
                self.rect.x = (self.rect.x + self.size) % 500
            if event.key == pygame.K_s:
                self.rect.y = (self.rect.y + self.size) % 500
            if event.key == pygame.K_w:
                self.rect.y = (self.rect.y - self.size) % 500

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    p1 = PlayerOneSprite()
    p2 = PlayerTwoSprite()
    my_group = pygame.sprite.Group()
    my_group.add(p1)
    my_group.add(p2)

    clock = pygame.time.Clock()

    while pygame.time.get_ticks() < 30 * 1000:
        clock.tick(30)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        my_group.update()
        p1.move(event)
        p2.move(event)
        my_group.draw(screen)
        pygame.display.flip()

    p1score = 0
    p2score = 0
    for i in range(20):
        for j in range(20):
            if grid[i][j] == 1:
                p1score += 1
            if grid[i][j] == 2:
                p2score += 1

    font = pygame.font.Font(pygame.font.get_default_font(), 25)
    if p1score > p2score:
        text = font.render("Player 1 Wins!", 20, (255, 255, 255))
    elif p1score < p2score:
        text = font.render("Player 2 Wins!", 20, (255, 255, 255))
    else:
        text = font.render("It's a tie!", 20, (255, 255, 255))
    screen.blit(text, (25, 25))
    pygame.display.flip()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)


if __name__ == '__main__':
    main()