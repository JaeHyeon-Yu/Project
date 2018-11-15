from pico2d import *

IDLE_STATE = 0
RUN_STATE = 1
ATTACK_STATE = 2

class Monster:
    def __init__(self):
        self.x, self.y = 700, 410
        self.frame_x, self.frame_y = None, None
        self.size_x, self.size_y = None, None
        self.frame = 0
        self.now_animation = IDLE_STATE

        self.hp, self.mp = 10, 10
        self.damage = 1
        self.image = load_image('sprites\\Enermy\\grunt2.png')

        self.idle_state_pos = [(0, 790, 80, 70), (70, 790, 80, 70), (140, 790, 80, 70)]


    def update(self):
        if self.now_animation is IDLE_STATE:
            self.Idle_Animation()

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)

    def Idle_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.idle_state_pos[self.frame]
        self.frame = (self.frame + 1) % 3