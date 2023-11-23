from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)
        draw_rectangle(*self.get_draw_bb())
    def update(self):
        pass

    def get_draw_bb(self):
        tx, ty = self.x - server.background.window_left, self.y - server.background.window_bottom
        return tx - 10, ty - 10, tx + 10, ty + 10

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == "Boy:Ball":
            game_world.remove_object(self)
