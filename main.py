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
        self.x_speed = -2
        self.backgrounds = [pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "background-day.png")), (self.width, self.height)),
                            pygame.transform.scale(pygame.image.load(os.path.join("assets", "sprites", "background-night.png")), (self.width, self.height))]
        self.curr_bg = random.randint(0, 1)

        #  Entities setup
        self.bird = Bird(self.width // 2, self.height // 2)
        self.pipes = [Pipe(self.width + 50, random.randint(60, self.groundy - 150)),
                      Pipe(self.width + 250, random.randint(60, self.groundy - 150))]
        self.score = Score()

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

            #  Move ground in the x axis
            self.bgx[0] += self.x_speed
            self.bgx[1] += self.x_speed
            if self.bgx[0] < self.ground.get_width() * -1:
                self.bgx[0] = self.backgrounds[self.curr_bg].get_width()
            if self.bgx[1] < self.ground.get_width() * -1:
                self.bgx[1] = self.backgrounds[self.curr_bg].get_width()

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
                if self.bird.x + self.bird.width == pipe.x and self.bird.y < pipe.y + pipe.opening and self.bird.y > pipe.y:
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
        #  Draw background
        self.win.blit(self.backgrounds[self.curr_bg], (0, 0))

        #  Draw pipes
        for pipe in self.pipes:
            pipe.draw(self.win, self.x_speed)

        #  Draw floor
        self.win.blit(self.ground, (int(self.bgx[0]), self.groundy))
        self.win.blit(self.ground, (int(self.bgx[1]), self.groundy))

        #  Draw score and bird
        self.score.draw(self.win, self.width // 2, 40)
        self.bird.draw(self.win)
        pygame.display.update()

    def game_over(self):
        """
        Shows game over screen
        Returns:
            None
        """
        self.bird.die()
        self.x_speed = 0

    def restart(self):
        """
        Restart game
        """
        self.bird = Bird(self.width // 2, self.height // 2)
        self.x_speed = -2
        self.score.value = 0
        for i in range(len(self.pipes)):
            self.pipes[i] = Pipe(self.width + 50 + 200 * i, random.randint(60, self.groundy - 150))


game = Game()
game.run()
