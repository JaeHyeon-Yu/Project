from pico2d import *
import game_framework

class Hp:
    def __init__(self):
        self.hp = 10
        self.image = load_image('sprites/player_hp.png')

class Mp:
    def __init__(self):
        self.mp = 10
        self.image = load_image('sprites/player_mp.png')