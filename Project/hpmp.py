from pico2d import *
import game_framework

class Hp:
    def __init__(self):
        self.hp = 10
        self.image = None

    def Initilize(self):
        self.image = load_image('sprites/player_hp.png')


    def draw(self):
        self.image.clip_draw(0, 0, 30, 200, 30, 300)


class Mp:
    def __init__(self):
        self.mp = 10
        self.image = None
    def Initilize(self):
        self.image = load_image('sprites/player_mp.png')


    def draw(self):
        self.image.clip_draw(0, 0, 30, 200, 800-30, 300)
