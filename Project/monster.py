from pico2d import *
import main_state
import random

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
        self.num_of_turn = 0
        self.font = load_font('ENCR10B.TTF', 16)

        self.hp, self.mp =  10, 10
        self.damage = 2
        self.image = load_image('sprites\\Enermy\\grunt2.png')

        self.idle_state_pos = [(0, 790, 80, 70), (70, 790, 80, 70), (140, 790, 80, 70)]
        self.run_state_pos = [(10, 600, 70, 70), (90, 600, 70, 70), (170, 600, 70, 70), (250, 600, 70, 70), (330, 600, 70, 70), (415, 600, 75, 70), (330, 600, 70, 70), (250, 600, 70, 70)]
        self.attack_state_pos = [(10, 300, 70, 70), (85, 305, 70, 70), (160, 305, 70, 75), (240, 305, 70, 75), (300, 305, 70, 75), (380, 305, 70, 75), (475, 305, 70, 75), (565, 305, 70, 75)]

        self.on_tile = 8
        self.game_clear = load_image('sprites\\player\\clear.png')

    def update(self):
        if self.my_turn is False:
            self.Idle_Animation()
            hero = main_state.get_player()
            if hero.My_Turn_is_Now() is False:
                self.my_turn = True
                self.now_animation = RUN_STATE

        elif self.now_animation is IDLE_STATE or self.hp <= 0:
            self.Idle_Animation()
        elif self.now_animation is RUN_STATE:
            self.Run_Animation()
        elif self.now_animation is ATTACK_STATE:
            self.Attack_Animation()
    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)
        self.font.draw(self.x-50, self.y + 50, '(HP: %d)' % self.hp, (255, 255, 0))

        if self.hp <= 0:
            self.game_clear.draw(400, 300)

    def Idle_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.idle_state_pos[self.frame]
        self.frame = (self.frame + 1) % 3
    def Run_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_state_pos[self.frame]
        self.frame = (self.frame + 1) % 8
        self.x -= 200 // 8
        if self.frame is 7:
            self.Change_to_IDLE()
            self.on_tile -= 1
            main_state.turn += 1
            self.Change_My_Turn()
    def Back_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_state_pos[self.frame]
        self.frame = (self.frame + 1) % 8
        self.x += 200 // 8
        if self.frame is 7:
            self.Change_to_IDLE()
            self.on_tile -= 1
            main_state.turn += 1
            self.Change_My_Turn()
    def Up_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_state_pos[self.frame]
        self.frame = (self.frame + 1) % 8
        self.y += 200 // 8
        if self.frame is 7:
            self.Change_to_IDLE()
            self.on_tile -= 1
            main_state.turn += 1
            self.Change_My_Turn()
    def Down_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.run_state_pos[self.frame]
        self.frame = (self.frame + 1) % 8
        self.y -= 200 // 8
        if self.frame is 7:
            self.Change_to_IDLE()
            self.on_tile -= 1
            main_state.turn += 1
            self.Change_My_Turn()
    def Attack_Animation(self):
        self.frame_x, self.frame_y, self.size_x, self.size_y = self.attack_state_pos[self.frame]
        self.frame = (self.frame+1) % 8
        attack_sound = load_wav('music\\grunt_attack.wav')
        attack_sound.set_volume(128)
        if self.frame is 7:
            attack_sound.play()
            self.Change_to_IDLE()
            main_state.turn += 1
            self.Change_My_Turn()

            if main_state.hero.on_tile <= self.on_tile and self.on_tile <= main_state.hero.on_tile + 1:
                if main_state.hero.buff.buff_on is True:
                    main_state.hero.buff.update()
                main_state.hero.hp.hp -= self.damage

    def Change_to_IDLE(self):
        self.now_animation = IDLE_STATE
        self.frame = 0

    def Change_My_Turn(self):
        if self.my_turn is False:
            self.my_turn = True
        else:
            self.my_turn = False
            main_state.hero.Change_My_Turn()

    def My_Next_Action(self):
        if self.my_turn is True:
            next_action = random.randint(1, 2)

            if self.on_tile is 2 or self.on_tile is 6 or self.on_tile is 10:
               next_action = ATTACK_STATE

            self.now_animation = next_action
            self.frame = 0
