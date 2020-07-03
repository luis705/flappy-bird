import pygame

import math
import os
import random
import sys


class Bird:
    def __init__(self, x, y):
        #  Images setup
        self.color = ['blue', 'red', 'yellow'][random.randint(0, 2)]
        self.imgs = [pygame.image.load(os.path.join('assets', 'sprites', f'{self.color}bird-upflap.png')),
                     pygame.image.load(os.path.join('assets', 'sprites', f'{self.color}bird-midflap.png')),
                     pygame.image.load(os.path.join('assets', 'sprites', f'{self.color}bird-downflap.png'))]
        self.curr_img = 0
        self.angle = 0

        #  Physics setup
        self.width = 34
        self.height = 24
        self.x = x - self.width // 2 - 30
        self.y = y
        self.x_speed = 2
        self.y_speed = 0
        self.dead = False

        #  Sound setup
        if sys.platform in ['win32', 'cygwin']:
            sound_ext = '.wav'
        else:
            sound_ext = '.ogg'
        self.sounds = {'wing': os.path.join('assets', 'audio', 'wing' + sound_ext),
                       'hit': os.path.join('assets', 'audio', 'hit' + sound_ext),
                       'die': os.path.join('assets', 'audio', 'die' + sound_ext)
                       }

    def draw(self, win):
        """
        Draws the bird with the given images
        Parameters:
            win: surface
        Returns:
            None
        """
        if self.angle > -70:
            self.angle -= 2

        win.blit(pygame.transform.rotate(self.imgs[math.floor(self.curr_img)], self.angle), (self.x, self.y))
        if not self.dead:
            self.move()
        else:
            self.fall(win)

    def collide(self, win, pipes):
        """
        Checks if the bird touched anything
        Returns:
            Bool
        """
        #  Bottom of the screen
        if self.y + self.height > win.get_height() - 110:
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
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.sounds.get('wing')))
        self.y_speed = -9
        self.angle = 60

    def die(self):
        self.dead = True
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.sounds.get('hit')))

    def fall(self, win):
        if self.y + self.height < win.get_height() - 110:
            self.y += self.y_speed
            self.y_speed += .5
            pygame.mixer.Channel(2).play(pygame.mixer.Sound(self.sounds.get('die')))

    def hit_sound(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(self.sounds.get('hit')))
