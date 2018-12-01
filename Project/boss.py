from pico2d import *
import main_state
import random

IDLE_STATE = 0
RUN_STATE = 1
ATTACK_STATE = 2

class Boss:
    def __init__(self):
        self.x, self.y = 700, 410
        self.frame_x, self.frame_y = None, None
        self.size_x, self.size_y = None, None
        self.frame = 0
        self.now_animation = IDLE_STATE
        self.my_turn = False
        self.num_of_turn = 0

        self.hp, self.mp = 50, 50
        self.damage = 5
        self.image = load_image('sprites\\Enermy\\boss.png')

        self.idle_animation = [(800, 1780, 100, 100)]

        self.on_tile = 8
        self.game_clear = load_image('sprites\\player\\clear.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)