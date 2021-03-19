import sys
import time
from threading import Thread

import pygame
from pygame.sprite import Sprite
from random import randint, choice

_HORIZONTAL_OFFSET = 0
_VERTICAL_OFFSET = 0


def ms_to_sec(milliseconds) -> float:
    return milliseconds / 1000


def should_draw_shape():
    return randint(0, 100) <= _TOLERANCE


MOVEMENT = 5




class Color:
    def __init__(self):
        movement = randint(-MOVEMENT, MOVEMENT)
        self.r = 255 if movement < 0 else 0
        self.g = 255 if movement < 0 else 0
        self.b = 255 if movement < 0 else 0
        self.movement = [movement, movement, movement]
        print(movement, self.r, self.g, self.b)
        # print(self.__dict__)

    def new_color(self):
        # movement = (randint(-MOVEMENT, MOVEMENT), randint(-MOVEMENT, MOVEMENT), randint(-MOVEMENT, MOVEMENT))
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


class Panel(Sprite):
    def __init__(self, x, y, width, height, color):
        Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color

    def update(self):
        color = self.color.new_color()
        # print(color)
        self.image.fill(color)
        pass


class Shape(Sprite):

    def __init__(self):
        Sprite.__init__(self)
        self.normal_color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.deltaX = randint(-PIXEL_DELTA_MAX, PIXEL_DELTA_MAX)
        self.deltaY = randint(-PIXEL_DELTA_MAX, PIXEL_DELTA_MAX)
        self.x = randint(0, SCREEN_WIDTH)
        self.y = randint(0, SCREEN_HEIGHT)
        width = randint(0, SCREEN_WIDTH - self.x)
        height = randint(0, SCREEN_HEIGHT - self.y)
        self.image = pygame.Surface((width, height))

        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        timeout = randint(0, 10)
        self.time_end_seconds = time.time() + timeout
        print(f"""
welcome child:
birth: {self.x}, {self.y}
size: {width}, {height}
timeout = {timeout}
type:
""")

    def update(self):
        self.rect.move_ip(self.deltaX, self.deltaY)
        self.image.fill(self.normal_color)


def set_settings() -> None:
    global PIXEL_DELTA_MAX, framerate, _TOLERANCE, thread, MOVEMENT, color_left, color_right
    MOVEMENT = randint(0, 100)
    PIXEL_DELTA_MAX = randint(1, 10)
    framerate = randint(1, 8)
    _TOLERANCE = randint(1, 30)
    color_left = Color()
    color_right = Color()
    setting_timeout = randint(1, 15)
    print(f"""
MOVEMENT {MOVEMENT}
PIXEL_DELTA_MAX {PIXEL_DELTA_MAX}
framerate {framerate}
_TOLERANCE {_TOLERANCE}
setting_timeout {setting_timeout}""")

    def wait_then_set():
        time.sleep(setting_timeout)
        set_settings()

    thread = Thread(target=wait_then_set, daemon=True).start()


pygame.init()
set_settings()

color_left = Color()
color_right = Color()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
left_x = 0
left_y = 0
right_x = SCREEN_WIDTH / 2
right_y = 0

left = Panel(x=left_x, y=left_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, color=color_left)
# right = Panel(x=right_x, y=right_y, width=SCREEN_WIDTH / 2, height=SCREEN_HEIGHT, color=color_right)

print("framerate:", framerate)
print("tolerance:", _TOLERANCE)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_COLOR = (0, 0, 0)

# sprite_list_name = [Shape() for _ in range(0, 1)]
sprites = pygame.sprite.Group()
sprites.add(left)
# sprites.add(right)
clock = pygame.time.Clock()
while True:
    # print("top of loop")
    # if should_draw_shape():
    #     sprites.add(Shape())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    current_time_seconds = time.time()
    # for s in sprites.sprites():
    #     if s.time_end_seconds < current_time_seconds:
    #         s.kill()

    screen.fill(SCREEN_COLOR)
    sprites.draw(screen)
    sprites.update()
    pygame.display.flip()
    clock.tick(framerate)
