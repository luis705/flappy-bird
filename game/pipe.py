import pygame

import os


class Pipe:
    def __init__(self, x, y, speed):
        #  Image setup
        self.img = pygame.transform.scale(pygame.image.load(
            os.path.join('..', 'assets', 'sprites', 'pipe-green.png')), (52, 400))
        self.opening = 120
        self.top_img = pygame.transform.flip(self.img, False, True)
        self.bottom_img = self.img

        #  Physics setup
        self.x = x
        self.y = y
        self.speed = speed
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.top = self.y - self.height
        self.bottom = self.y + self.opening

    def draw(self, win):
        """
        Draws the pipes on the screen
        Parameters:
            win: surface
        Returns:
            None
        """
        if self.x + self.width > 0 and self.x < win.get_width():
            win.blit(self.top_img, (self.x, self.top))
            win.blit(self.bottom_img, (self.x, self.bottom))
        self.move()

    def move(self):
        """
        Moves the pipes on the x axis
        """
        self.x += self.speed

    def collide(self, bird):
        """
        Check if the pipe and touched the bird
        Returns:
            Bool
        """
        #  Get pip and bird masks
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.top_img)
        bottom_mask = pygame.mask.from_surface(self.bottom_img)

        #  Get top and bottom offset from the bird

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        #  Check for collision
        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True
        return False
