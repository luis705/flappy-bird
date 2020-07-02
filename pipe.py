import pygame

import os


class Pipe:
    def __init__(self, x, y):
        self.img = pygame.transform.scale(pygame.image.load(
            os.path.join('assets/sprites', 'pipe-green.png')), (52, 400))
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.opening = 120

    def draw(self, win):
        """
        Draws the pipes on the screen
        Returns:
            None
        """
        if self.x + self.width > 0 and self.x < win.get_width():
            win.blit(pygame.transform.rotate(self.img, 180), (self.x, self.y - self.height))
            win.blit(self.img, (self.x, self.y + self.opening))
        self.move()

    def move(self):
        """
        Moves the pipes on the x axis
        """
        self.x -= 2
