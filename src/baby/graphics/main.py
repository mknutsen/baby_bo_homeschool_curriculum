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




def set_settings(sprite_options) -> None:
    global PIXEL_DELTA_MAX, framerate, _TOLERANCE, thread, MOVEMENT, color_left, color_right, color_up, color_down, color_full, sprites
    MOVEMENT = randint(0, 100)
    PIXEL_DELTA_MAX = randint(1, 10)
    framerate = randint(1, 8)
    _TOLERANCE = randint(1, 30)
    sprites = choice(sprite_options)
    for sprite in sprites.sprites():
        sprite.color = Color(MOVEMENT)
    setting_timeout = randint(1, 15)
    print(f"""
MOVEMENT {MOVEMENT}
PIXEL_DELTA_MAX {PIXEL_DELTA_MAX}
framerate {framerate}
_TOLERANCE {_TOLERANCE}
setting_timeout {setting_timeout}
sprites {sprites.sprites()}
""")

    def wait_then_set():
        time.sleep(setting_timeout)
        set_settings(sprite_options)

    thread = Thread(target=wait_then_set, daemon=True).start()


def main():
    global sprites
    MOVEMENT = 5

    pygame.init()

    infoObject = pygame.display.Info()
    SCREEN_WIDTH = infoObject.current_w
    SCREEN_HEIGHT = infoObject.current_h
    left_x = 0
    left_y = 0
    right_x = SCREEN_WIDTH / 2
    right_y = 0

    up_x = 0
    up_y = 0
    down_y = SCREEN_HEIGHT / 2
    down_x = 0

    left = Panel(x=left_x, y=left_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    right = Panel(x=right_x, y=right_y, width=SCREEN_WIDTH / 2, height=SCREEN_HEIGHT)

    up = Panel(x=up_x, y=up_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT / 2)
    down = Panel(x=down_x, y=down_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT / 2)

    full = Panel(x=right_x, y=right_y, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


    # sprite_list_name = [Shape() for _ in range(0, 1)]
    vertical_sprites = pygame.sprite.Group([left, right])
    horizontal_sprites = pygame.sprite.Group([up, down])
    full_sprites = pygame.sprite.Group([full, ])
    set_settings([vertical_sprites, horizontal_sprites, full_sprites])
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    print("framerate:", framerate)
    print("tolerance:", _TOLERANCE)
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
