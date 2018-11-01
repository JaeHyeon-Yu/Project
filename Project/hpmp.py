from pico2d import *
import game_framework

class Hp:
    def __init__(self):
        self.hp = 10
        self.image = None

    def Initilize(self):
        self.image = load_image('sprites/player_hp.png')


    def draw(self):
        i = 0
        while i < self.hp:
            self.image.draw(30, 300)
            i += 1


class Mp:
    def __init__(self):
        self.mp = 10
        self.image = load_image('sprites/player_mp.png')

