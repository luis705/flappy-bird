import pygame

import os

from bird import Bird


class Game:
    def __init__(self):
        """
        Initialize and setup game screen
        """
        self.width = 310
        self.height = 510
        self.win = pygame.display.set_mode((self.width, self.height))
        self.score = 0
        self.pipes = []
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join("assets/sprites", "background-day.png")), (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load(os.path.join("assets/sprites", "background-night.png")), (self.width, self.height))]
        self.curr_bg = 0

    def run(self):
        """
        Game main loop
        """
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if self.score % 50 == 0 and self.score != 0:
                self.curr_bg += 1
                if self.curr_bg >= len(self.backgrounds):
                    self.curr_bg = 0

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.backgrounds[self.curr_bg], (0, 0))
        pygame.display.update()


game = Game()
game.run()
