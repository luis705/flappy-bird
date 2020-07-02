import pygame

import random
import os
import math


class Bird:
    def __init__(self, x, y):
        self.width = 34
        self.height = 24
        self.x = x - self.width // 2
        self.y = y
        self.x_speed = 2
        self.y_speed = 0
        self.width = 34
        self.height = 24
        self.color = ['blue', 'red', 'yellow'][random.randint(0, 2)]
        self.imgs = [pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-upflap.png')),
                     pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-midflap.png')),
                     pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-downflap.png'))]
        self.curr_img = 0
        self.angle = 0

    def draw(self, win):
        """
        Draws the bird with the given images
        Parameters:
            win: surface
        Returns:
            None
        """
        if self.angle > -60:
            self.angle -= 2

        win.blit(pygame.transform.rotate(self.imgs[math.floor(self.curr_img)], self.angle), (self.x, self.y))
        self.move()

    def collide_top(self):
        """
        Checks if the bird touched the top of the screen
        Returns:
            Bool
        """
        return self.y < 0 and self.y + self.height > 0

    def collide_bottom(self, y):
        """
        Checks if the bird touched the bottom of the screen
        Parameters:
            y: integer
        Returns:
            Bool
        """
        return self.y < y and self.y + self.height > y

    def move(self):
        """
        Move bird
        Returns:
            None
        """
        self.y += self.y_speed
        self.y_speed += .75
        if self.curr_img != 0:
            self.curr_img += .01
        if self.curr_img >= 3:
            self.curr_img = 0

    def jump(self):
        """
        Changes the bird velocity and angle on jump
        Returns:
            None
        """
        self.y_speed = -15
        self.angle = 60
        self.curr_img = 1
