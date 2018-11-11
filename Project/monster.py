from pico2d import *

NOMAL_MONSTER = 0
BOSS_MONSTER = 1

class Monster:
    def __init__(self, who_are_you):
        self.x, self.y = None, None
        self.frame_x, self.frame_y = None, None
        self.hp, self.mp = None, None
        self.damage = None
        self.image = None

        if who_are_you is NOMAL_MONSTER:
            pass
        elif who_are_you is BOSS_MONSTER:
            pass