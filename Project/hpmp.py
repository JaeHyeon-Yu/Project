from pico2d import *
import game_framework

class Hp:
    def __init__(self):
        self.hp = 10
        self.image = None

    def Initilize(self):
        self.image = load_image('sprites/player_hp.png')

    def update(self, num):
        self.hp -= num


    def draw(self):
        self.image.clip_draw(0, 20 * (10 - self.hp), 30, self.hp * 20, 30, 300)


class Mp:
    def __init__(self):
        self.mp = 10
        self.image = None
    def Initilize(self):
        self.image = load_image('sprites/player_mp.png')

    def update(self, num):
        self.mp -= num


    def draw(self):
        self.image.clip_draw(0, 20*(10-self.mp), 30, self.mp*20, 800-30, 300)
