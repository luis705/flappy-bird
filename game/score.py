import pygame

import os
import sys


class Score:
    def __init__(self):
        #  Value setup
        self.value = 0

        #  Images setup
        self.imgs = [pygame.image.load(os.path.join(
            '..', 'assets', 'sprites', str(i) + '.png')) for i in range(10)]
        self.width = self.imgs[0].get_width()

        #  Sound setup
        if sys.platform in ['win32', 'cygwin']:
            sound_ext = '.wav'
        else:
            sound_ext = '.ogg'
        self.sound = os.path.join('..', 'assets', 'audio', 'point' + sound_ext)

    def increase(self):
        """
        Increase score value
        Returns:
            None
        """
        #  Increase score and play the sound
        self.value += 1
        self.string = str(self.value)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.sound))

        #  Change the width of the score
        images = []
        for i in str(self.value):
            number = int(i)
            images.append(self.imgs[number])
        self.width = 0
        for image in images:
            self.width += image.get_width()

    def draw(self, win, x, y):
        """
        Draw the score on the screen
        Prameters:
            win: surface
            x: integer
            y: integer
        Returns:
            None
        """

        centered_rect = pygame.Rect(((win.get_width() - self.width) // 2, y,
                                     self.width, self.imgs[0].get_height()))

        for number in str(self.value):
            win.blit(self.imgs[int(number)], centered_rect)
            centered_rect[0] += self.imgs[int(number)].get_width()
