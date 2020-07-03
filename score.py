import pygame

import os
import sys


class Score:
    def __init__(self):
        self.value = 0
        self.string = str(self.value)
        self.imgs = [pygame.image.load(os.path.join(
            'assets', 'sprites', str(i) + '.png')) for i in range(10)]
        if sys.platform in ['win32', 'cygwin']:
            sound_ext = '.wav'
        else:
            sound_ext = '.ogg'
        self.sound = os.path.join('assets', 'audio', 'point' + sound_ext)

    def increase(self):
        self.value += 1
        self.string = str(self.value)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound(self.sound))

    def draw(self, win, x, y):
        """
        Draw the score on the screen !!!!!NEEDS IMPROVEMENT!!!!!
        Prameters:
            win: surface
            x: integer
            y: integer
        Returns:
            None
        """
        if len(str(self.value)) == 1:
            win.blit(self.imgs[self.value],
                     ((x - self.imgs[self.value].get_width(), y)))

        elif len(str(self.value)) == 2:
            win.blit(self.imgs[int(str(self.value)[0])],
                     (x - self.imgs[int(str(self.value)[0])].get_width(), y))
            win.blit(self.imgs[int(str(self.value)[1])],
                     (x, y))

        elif len(str(self.value)) == 3:
            hundreds_width = self.imgs[int(str(self.value)[0])].get_width()
            tenths_width = self.imgs[int(str(self.value)[1])].get_width()
            units_width = self.imgs[int(str(self.value)[2])].get_width()
            win.blit(self.imgs[int(str(self.value)[0])],
                     (x - hundreds_width - tenths_width, y))
            win.blit(self.imgs[int(str(self.value)[1])],
                     (x - tenths_width, y))
            win.blit(self.imgs[int(str(self.value)[2])],
                     (x - tenths_width + units_width, y))

        elif len(str(self.value)) == 4:
            thousends_width = self.imgs[int(str(self.value)[0])].get_width()
            hundreds_width = self.imgs[int(str(self.value)[1])].get_width()
            tenths_width = self.imgs[int(str(self.value)[2])].get_width()
            units_width = self.imgs[int(str(self.value)[3])].get_width()

            win.blit(self.imgs[int(str(self.value)[0])],
                     (x - hundreds_width - thousends_width, y))
            win.blit(self.imgs[int(str(self.value)[1])],
                     (x - hundreds_width, y))
            win.blit(self.imgs[int(str(self.value)[2])],
                     (x, y))
            win.blit(self.imgs[int(str(self.value)[3])],
                     (x + tenths_width, y))

        elif len(str(self.value)) == 5:
            ten_thousends_width = self.imgs[int(str(self.value)[0])].get_width()
            thousends_width = self.imgs[int(str(self.value)[1])].get_width()
            hundreds_width = self.imgs[int(str(self.value)[2])].get_width()
            tenths_width = self.imgs[int(str(self.value)[3])].get_width()
            units_width = self.imgs[int(str(self.value)[4])].get_width()

            win.blit(self.imgs[int(str(self.value)[0])],
                     (x - thousends_width - ten_thousends_width, y))
            win.blit(self.imgs[int(str(self.value)[1])],
                     (x - thousends_width, y))
            win.blit(self.imgs[int(str(self.value)[2])],
                     (x, y))
            win.blit(self.imgs[int(str(self.value)[3])],
                     (x + tenths_width, y))
            win.blit(self.imgs[int(str(self.value)[4])],
                     (x + units_width, y))
