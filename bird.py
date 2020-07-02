import pygame

import math
import os
import random


class Bird:
    def __init__(self, x, y):
        self.color = ['blue', 'red', 'yellow'][random.randint(0, 2)]
        self.imgs = [pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-upflap.png')),
                     pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-midflap.png')),
                     pygame.image.load(os.path.join('assets/sprites', f'{self.color}bird-downflap.png'))]
        self.curr_img = 0
        self.angle = 0
        self.width = 34
        self.height = 24
        self.x = x - self.width // 2
        self.y = y
        self.x_speed = 2
        self.y_speed = 0

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

    def collide(self, window, pipes):
        """
        Checks if the bird touched anything
        Returns:
            Bool
        """
        #  Top of the screen
        if self.y < 0 and self.y + self.height > 0:
            return True
        #  Bottom of the screen
        if self.y < window.get_height() - 100 and self.y + self.height > window.get_height() - 100:
            return True

        #  Any pipe
        for pipe in pipes:
            if self.x > pipe.x and self.x < pipe.x + pipe.width:
                if self.y >= pipe.y + pipe.opening or self.y < pipe.y:
                    return True

        return False

    def move(self):
        """
        Move bird
        Returns:
            None
        """
        self.y += self.y_speed
        self.y_speed += .5
        self.curr_img += .2
        if self.curr_img >= 3:
            self.curr_img = 0

    def jump(self):
        """
        Changes the bird velocity and angle on jump
        Returns:
            None
        """
        self.y_speed = -9
        self.angle = 60
