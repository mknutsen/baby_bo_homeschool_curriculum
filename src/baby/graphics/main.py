import sys
import time
from threading import Thread

import pygame
from pygame.sprite import Sprite
from random import randint, choice

from baby.graphics.Panel import Color, Panel

_HORIZONTAL_OFFSET = 0
_VERTICAL_OFFSET = 0


def ms_to_sec(milliseconds) -> float:
    return milliseconds / 1000


def should_draw_shape():
    return randint(0, 100) <= _TOLERANCE


MOVEMENT = 5



def set_settings() -> None:
    global PIXEL_DELTA_MAX, framerate, _TOLERANCE, thread, MOVEMENT, color_left, color_right
    MOVEMENT = randint(0, 100)
    PIXEL_DELTA_MAX = randint(1, 10)
    framerate = randint(1, 8)
    _TOLERANCE = randint(1, 30)
    color_left = Color(MOVEMENT)
    color_right = Color(MOVEMENT)
    setting_timeout = randint(1, 15)
    print(f"""
MOVEMENT {MOVEMENT}
PIXEL_DELTA_MAX {PIXEL_DELTA_MAX}
framerate {framerate}
_TOLERANCE {_TOLERANCE}
setting_timeout {setting_timeout}
""")

    def wait_then_set():
        time.sleep(setting_timeout)
        set_settings()

    thread = Thread(target=wait_then_set, daemon=True).start()

def main():
    pygame.init()
    set_settings()

    infoObject = pygame.display.Info()
    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h
    left_x = 0
    left_y = 0
    right_x = SCREEN_WIDTH / 2
    right_y = 0

    left = Panel(x=left_x, y=left_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, color=color_left)
    right = Panel(x=right_x, y=right_y, width=SCREEN_WIDTH / 2, height=SCREEN_HEIGHT, color=color_right)

    print("framerate:", framerate)
    print("tolerance:", _TOLERANCE)

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # sprite_list_name = [Shape() for _ in range(0, 1)]
    sprites = pygame.sprite.Group()
    sprites.add(left)
    sprites.add(right)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
        clock.tick(framerate)

if __name__ == "__main__":
    main()