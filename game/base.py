import pygame

import os


class Base:
    def __init__(self, y, speed):
        #  Image setup
        self.img = pygame.image.load(os.path.join('..', 'assets', 'sprites', 'base.png'))
        self.width = self.img.get_width()

        #  Movement setup
        self.y = y
        self.x1 = 0
        self.x2 = self.width
        self.speed = speed

    def draw(self, win):
        """
        Draw the base on the screen and calls the move method
        Returns:
            None
        """
        win.blit(self.img, (self.x1, self.y))
        win.blit(self.img, (self.x2, self.y))
        self.move()

    def move(self):
        """
        Move the base to simulate bird movement
        Returns:
            None
        """
        #  Move the base
        self.x1 += self.speed
        self.x2 += self.speed

        #  If image is out of the screen put it on
        #  the other side to be scrolled again
        if self.x1 + self.width < 0:
            self.x1 = self.x2 + self.width

        if self.x2 + self.width < 0:
            self.x2 = self.x1 + self.width
