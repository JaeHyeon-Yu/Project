from pico2d import *
import game_framework
from bullet import *
from buff import *
from hpmp import *
import game_world

IDLE_STATE = 0
RUN_STATE = 1
BACKSTEP_STATE = 2
JUMP_STATE = 3
DOWN_STATE = 4
ATTACK_STATE = 5
DEFENSE_STATE = 6
HP_HEAL_STATE = 7
MP_HEAL_STATE = 8
GUN_STATE = 9
SPECIAL_ATTACK_STATE = 10

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class Player:
    def __init__(self):
        self.x, self.y = 100, 410
        self.frame_x, self.frame_y = None, None
        self.size_x, self.size_y = 80, 100
        self.image = load_image('sprites\\player\\zerox.png')
        self.my_turn = False

        self.hp, self.mp = Hp(), Mp()

        self.gun_is_fired = False
        self.bullet = None
        self.buff = None


        self.now_animation = IDLE_STATE
        self.Idle_animation_pos = [(0, 900, 75, 100), (75, 900, 75, 100)]   # 0
        self.run_animation_pos = [(0, 500, 75, 100), (80, 500, 75, 100), (160, 500, 75, 100), (240, 500, 75, 100), (320, 500, 75, 100), (400, 500, 75, 100), (480, 500, 75, 100), (570, 500, 75, 100), (650, 500, 75, 100), (740, 500, 75, 100), (820, 500, 75, 100), (895, 500, 75, 100), (975, 500, 75, 100), (1055, 500, 75, 100), (1135, 500, 75, 100), (1220, 500, 75, 100)]    # 1
        self.back_animation_pos = [(0, 900, 75, 100), (75, 900, 75, 100), (150, 900, 75, 100), (230, 900, 75, 100), (300, 900, 75, 100), (230, 900, 75, 100), (150, 900, 75, 100), (75, 900, 75, 100)]
        self.jump_animation_pos = [(0, 760, 75, 100), (70, 745, 75, 100), (202, 740, 75, 100), (270, 740, 75, 100), (202, 740, 75, 100), (70, 745, 75, 100)]  # 3    # 나중에 찾자.....
        self.down_animation_pos = None
        self.attack_animation_pos = [(0, 420, 80, 100), (90, 420, 80, 100), (182, 420, 80, 100), (265, 420, 160, 100), (440, 420, 160, 100), (605, 420, 140, 100), (760, 420, 105, 100), (880, 420, 105, 100), (1000, 420, 80, 100), (90, 420, 80, 100)]  # 5
        self.defence_animation_pos = [(0, 0), (50, 0), (100, 0)]

        self.gun_animation_pos = [(0, 630, 80, 100), (75, 630, 80, 100), (155, 630, 80, 100), (240, 630, 80, 100), (325, 630, 80, 100), (408, 630, 88, 100), (492, 630, 100, 100), (600, 630, 120, 100), (325, 630, 80, 100), (240, 630, 80, 100), (155, 630, 80, 100)]  # 9
        self.fire_animation_pos = [(5, 1260, 120, 120), (117 ,1250, 150, 140), (270 ,1250, 140, 140), (410, 1250, 140, 150), (550, 1250, 140, 150), (685, 1265, 150, 160), (835, 1265, 150, 160), (980, 1265, 150, 180), (1130, 1265, 150, 180), (1260, 1265, 140, 180), (0, 1025, 140, 180)]
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)
        self.hp.draw()
        self.mp.draw()
        if self.gun_is_fired is True:
            self.bullet.draw()
    def update(self):
        if self.my_turn is False:
            self.Idle_Animation()

        elif self.now_animation is IDLE_STATE:
            self.Idle_Animation()

        elif self.now_animation is RUN_STATE:
            self.Run_Animation()

        elif self.now_animation is BACKSTEP_STATE:
            self.Back_Animation()

        elif self.now_animation is JUMP_STATE:
            self.Jump_Animation()

        elif self.now_animation is DOWN_STATE:
            self.Down_Animation()

        elif self.now_animation is ATTACK_STATE:
            self.Attck_Animation()

        elif self.now_animation is DEFENSE_STATE:
            self.Defense_Animation()

        elif self.now_animation is HP_HEAL_STATE:
            self.Heal_Animation()

        elif self.now_animation is MP_HEAL_STATE:
            self.Mana_Animation()

        elif self.now_animation is GUN_STATE:
            self.Gun_Animation()

        elif self.now_animation is SPECIAL_ATTACK_STATE:
            self.Fire_Animation()

        if self.gun_is_fired is True:
            self.bullet.update()
    def handle_events(self):
        pass
    def update_animation(self, num):
        self.now_animation = num
        self.frame = 0
    def Idle_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.Idle_animation_pos[self.frame]
        self.frame = (self.frame + 1) % 2
    def Run_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_animation_pos[self.frame]
        self.frame = (self.frame + 1) % 16
        self.x += 200 // 16
        if self.frame is 15:
            self.x = 300
            self.Change_to_IDLE()
    def Back_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.back_animation_pos[self.frame]
        self.frame = (self.frame+1) % 8
        self.x -= 200 // 8
        if self.frame is 15:
            self.x = 300
            self.frame = 0
            self.now_animation = IDLE_STATE          # 미완
    def Jump_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.jump_animation_pos[self.frame]
        self.frame = (self.frame + 1) % 6
        self.y += 200//6

        if self.frame is 5:
            self.Change_to_IDLE()
    def Down_Animation(self):
        pass
    def Attck_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.attack_animation_pos[self.frame]
        self.frame = (self.frame + 1) % 10

        if self.frame is 9:
            self.Change_to_IDLE()
    def Defense_Animation(self):
        self.size_x = 75
        self.size_y = 100
        self.now_animation = IDLE_STATE
        self.frame = 0
    def Heal_Animation(self):
        self.size_x = 75
        self.size_y = 100
        self.hp.update(-2)
        self.now_animation = IDLE_STATE
    def Mana_Animation(self):
        self.size_x = 75
        self.size_y = 100
        self.mp.update(-2)
        self.now_animation = IDLE_STATE
    def Gun_Animation(self):
        if self.frame is 0:
            self.mp.update(3)
        elif self.frame is 8:
            self.gun_is_fired = True
            self.bullet = Bullet(self.x, self.y)
            game_world.add_object(self.bullet, 1)
        elif self.frame is 10:
            self.Change_to_IDLE()

        self.frame_x, self.frame_y, self.size_x, self.size_y = self.gun_animation_pos[self.frame]
        self.frame = (self.frame + 1) % 11
    def Fire_Animation(self):
        if self.frame is 0:
            self.mp.update(5)
        elif self.frame is 10:
            self.Change_to_IDLE()

        self.frame_x, self.frame_y, self.size_x, self.size_y = self.fire_animation_pos[self.frame]
        self.frame = (self.frame+1) % 11

    def Change_to_IDLE(self):
        self.frame = 0
        self.now_animation = IDLE_STATE