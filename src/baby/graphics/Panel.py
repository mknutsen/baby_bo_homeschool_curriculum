from random import randint

from pygame import Surface
from pygame.sprite import Sprite


class Panel(Sprite):
    def __init__(self, x, y, width, height):
        Sprite.__init__(self)
        self.image = Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = Color(0)

    def update(self):
        color = self.color.new_color()
        self.image.fill(color)
        pass


class Color:
    def __init__(self, movement_max):
        movement = randint(-movement_max, movement_max)
        self.r = 255 if movement < 0 else 0
        self.g = 255 if movement < 0 else 0
        self.b = 255 if movement < 0 else 0
        self.movement = [movement, movement, movement]

    def new_color(self):
        self.r = self.r + self.movement[0]
        self.g = self.g + self.movement[1]
        self.b = self.b + self.movement[2]

        if self.r > 255 or self.r < 0:
            self.movement[0] *= -1
            self.r = 255 if self.r >= 255 else 0
        if self.g > 255 or self.g < 0:
            self.movement[1] *= -1
            self.g = 255 if self.g >= 255 else 0
        if self.b > 255 or self.b < 0:
            self.movement[2] *= -1
            self.b = 255 if self.b >= 255 else 0

        return self.r, self.g, self.b
