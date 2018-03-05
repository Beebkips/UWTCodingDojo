import pygame


class EasyEngine():
    def __init__(self):
        self.entities = []
        self.background = None

    def setScreen(self, x, y, color=(255, 255, 255)):
        self.background = pygame.surface((x, y))
        self.background.fill(color)

    def run(self):
        pygame.init()
        run = True
        while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                for e in entities:
                    e.key_check(event.key)

        for e in entities:
            e.update()

        
