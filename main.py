import pygame

import os
import random
import sys

from bird import Bird
from pipe import Pipe
from score import Score


class Game:
    def __init__(self):
        """
        Initialize and setup game screen
        """
        # Window setup
        self.width = 310
        self.height = 510
        self.win = pygame.display.set_mode((self.width, self.height))

        #  Images setup
        self.ground = pygame.image.load(os.path.join("assets", "sprites", "base.png"))
        self.groundy = self.height - 100
        self.bgx = [0, self.ground.get_width()]
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "background-day.png")), (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "background-night.png")), (self.width, self.height))]
        self.curr_bg = random.randint(0, 1)

        #  Entities setup
        self.bird = Bird(self.width // 2, self.height // 2)
        self.pipes = [Pipe(self.width + 50, random.randint(60, self.groundy - 150)),
                      Pipe(self.width + 250, random.randint(60, self.groundy - 150))]
        self.score = Score()

    def run(self):
        """
        Game main loop
        """
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)

            #  Move ground in the x axis
            self.bgx[0] -= 2
            self.bgx[1] -= 2
            if self.bgx[0] < self.ground.get_width() * -1:
                self.bgx[0] = self.backgrounds[self.curr_bg].get_width()
            if self.bgx[1] < self.ground.get_width() * -1:
                self.bgx[1] = self.backgrounds[self.curr_bg].get_width()

            #  Get game events and handle them
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            if self.bird.collide(self.win, self.pipes):
                self.game_over()

            for pipe in self.pipes:
                #  Update score if needed
                if self.bird.x + self.bird.width == pipe.x:
                    self.score.increase()
                #  Replace pipe if needed
                if pipe.x <= - pipe.width:
                    pipe.x = 350
                    pipe.y = random.randint(60, self.groundy - 150)

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
        self.win.blit(self.backgrounds[self.curr_bg], (0, 0))
        self.win.blit(self.ground, (int(self.bgx[0]), self.groundy))
        self.win.blit(self.ground, (int(self.bgx[1]), self.groundy))
        self.bird.draw(self.win)
        for pipe in self.pipes:
            pipe.draw(self.win)

        #  Draw scores
        self.score.draw(self.win, self.width // 2, 40)

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
