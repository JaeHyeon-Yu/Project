from pico2d import *

NOMAL_MONSTER = 0
BOSS_MONSTER = 1

class Monster:
    def __init__(self, who_are_you):
        self.x, self.y = 700, 410
        self.frame_x, self.frame_y = 0, 0
        self.size_x, self.size_y = 100, 100

        self.hp, self.mp = None, None
        self.damage = None
        self.image = None

        self.IDLE_state_pos = None

        if who_are_you is NOMAL_MONSTER:
            self.image = load_image('sprites\\Enermy\\grunt2.png')
            self.hp, self.mp = 10, 10
            self.damage = 1
        elif who_are_you is BOSS_MONSTER:
            self.image = load_image('sprites\\Enermy\\boss.png')
            self.hp, self.mp = 100, 100
            self.damage = 3

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)