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
        self.my_turn = False

        self.hp, self.mp = 10, 10
        self.damage = 1
        self.image = load_image('sprites\\Enermy\\grunt2.png')

        self.idle_state_pos = [(0, 790, 80, 70), (70, 790, 80, 70), (140, 790, 80, 70)]
        self.run_state_pos = [(10, 600, 70, 70), (90, 600, 70, 70), (170, 600, 70, 70), (250, 600, 70, 70), (330, 600, 70, 70), (415, 600, 75, 70), (330, 600, 70, 70), (250, 600, 70, 70)]
        self.attack_state_pos = [(10, 300, 70, 70), (85, 305, 70, 70), (160, 305, 70, 75), (240, 305, 70, 75), (300, 305, 70, 75), (380, 305, 70, 75), (475, 305, 70, 75), (565, 305, 70, 75)]


    def update(self):
        if self.my_turn is False:
            self.Idle_Animation()
        elif self.now_animation is IDLE_STATE:
            self.Idle_Animation()
        elif self.now_animation is RUN_STATE:
            self.Run_Animation()
        elif self.now_animation is ATTACK_STATE:
            self.Attack_Animation()
    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)

    def Idle_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.idle_state_pos[self.frame]
        self.frame = (self.frame + 1) % 3
    def Run_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_state_pos[self.frame]
        self.frame = (self.frame + 1) % 8

        if self.frame is 7:
            self.Change_to_IDLE()

    def Attack_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.attack_state_pos[self.frame]
        self.frame = (self.frame+1) % 8

        if self.frame is 7:
            self.Change_to_IDLE()

    def Change_to_IDLE(self):
        self.my_turn = False
        self.now_animation = IDLE_STATE
        self.frame = 0

    def Change_My_Turn(self):
        self.my_turn = True