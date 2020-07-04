import pygame

import os
import random
import sys

from base import Base
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
        pygame.display.set_caption('Flappy Bird')

        #  Images setup
        self.groundy = self.height - 100
        self.x_speed = -2
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'sprites', 'background-day.png')), (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load(os.path.join('..', 'assets', 'sprites', 'background-night.png')), (self.width, self.height))]
        self.curr_bg = random.randint(0, 1)
        self.game_over_img = pygame.image.load(os.path.join('..', 'assets', 'sprites', 'gameover.png'))
        self.is_over = False

        #  Entities setup
        self.bird = Bird(self.width // 2, self.height // 2)
        self.pipes = [Pipe(self.width + 50, random.randint(60, self.groundy - 150), self.x_speed),
                      Pipe(self.width + 250, random.randint(60, self.groundy - 150), self.x_speed)]
        self.score = Score()
        self.base = Base(self.groundy, self.x_speed)

        #  Sound setup
        pygame.mixer.init()

    def run(self):
        """
        Game main loop
        """
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)

            #  Get game events and handle them
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.bird.dead:
                        self.bird.jump()

                    if event.key == 114 and self.bird.dead:
                        self.restart()

            if self.bird.collide(self.win, self.pipes):
                if not self.bird.dead:
                    self.game_over()
                    self.bird.hit_sound()

            for pipe in self.pipes:
                #  Update score if needed
                if self.bird.x >= pipe.x and not pipe.passed:
                    self.score.increase()
                    pipe.passed = True
                #  Replace pipe if needed
                if pipe.x <= - pipe.width:
                    pipe.x = 350
                    pipe.y = random.randint(60, self.groundy - 150)
                    pipe.passed = False

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
        #  Draw background
        self.win.blit(self.backgrounds[self.curr_bg], (0, 0))

        #  Draw pipes and bas
        for pipe in self.pipes:
            pipe.draw(self.win)
        self.base.draw(self.win)

        #  Draw score and game over sign
        if self.is_over:
            self.win.blit(self.game_over_img, ((self.win.get_width() -
                                                self.game_over_img.get_width()) // 2, 40))
            self.score.draw(self.win, self.width // 2, self.win.get_height() // 2)
        else:
            self.score.draw(self.win, self.width // 2, 40)

        #  Draw bird and update screen
        self.bird.draw(self.win)
        pygame.display.update()

    def game_over(self):
        """
        Shows game over screen
        Returns:
            None
        """
        self.bird.die()
        self.is_over = True
        for pipe in self.pipes:
            pipe.speed = 0
        self.base.speed = 0

    def restart(self):
        """
        Restart game
        """
        self.bird = Bird(self.width // 2, self.height // 2)
        self.base.speed = self.x_speed
        self.score.value = 0
        self.is_over = False
        for i in range(len(self.pipes)):
            self.pipes[i] = Pipe(self.width + 50 + 200 * i,
                                 random.randint(60, self.groundy - 150), self.x_speed)


game = Game()
game.run()
