import pygame

import os
import random
import sys

from bird import Bird
from pipe import Pipe


class Game:
    def __init__(self):
        """
        Initialize and setup game screen
        """
        self.width = 310
        self.height = 510
        self.win = pygame.display.set_mode((self.width, self.height))
        self.score = 0
        self.pipes = [Pipe(self.width + 50, random.randint(60, 400)),
                      Pipe(self.width + 250, random.randint(60, 400))]
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join("assets/sprites", "background-day.png")), (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load(os.path.join("assets/sprites", "background-night.png")), (self.width, self.height))]
        self.curr_bg = 0
        self.bgx = [0, self.backgrounds[self.curr_bg].get_width()]
        self.bird = Bird(self.width // 2, self.height // 2)

    def run(self):
        """
        Game main loop
        """
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)

            #  Move background in the x axis
            self.bgx[0] -= 1.4
            self.bgx[1] -= 1.4
            if self.bgx[0] < self.backgrounds[self.curr_bg].get_width() * -1:
                self.bgx[0] = self.backgrounds[self.curr_bg].get_width()
            if self.bgx[1] < self.backgrounds[self.curr_bg].get_width() * -1:
                self.bgx[1] = self.backgrounds[self.curr_bg].get_width()

            #  Get game events and handle them
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            #  Change background after certain scores
            if self.score % 50 == 0 and self.score != 0:
                self.curr_bg += 1
                if self.curr_bg >= len(self.backgrounds):
                    self.curr_bg = 0

            if self.bird.collide(self.win, self.pipes):
                self.game_over()

            for pipe in self.pipes:
                if pipe.x <= - pipe.width:
                    pipe.x = 350
                    pipe.y = random.randint(60, 400)

            self.draw()

        #  CLose the game
        pygame.quit()
        sys.exit()

    def draw(self):
        """
        Draw everything on the game screen
        Returns:
            None
        """
        self.win.blit(self.backgrounds[self.curr_bg], (int(self.bgx[0]), 0))
        self.win.blit(self.backgrounds[self.curr_bg], (int(self.bgx[1]), 0))
        self.bird.draw(self.win)
        for pipe in self.pipes:
            pipe.draw(self.win)
        pygame.display.update()

    def game_over(self):
        """
        Shows game over screen
        Returns:
            None
        """
        pass


game = Game()
game.run()
