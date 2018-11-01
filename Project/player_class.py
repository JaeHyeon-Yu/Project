from pico2d import *
import game_framework
from bullet_class import *
from buff_class import *
import game_world


class Player:
    def __init__(self):
        self.x, self.y = None, None
        self.frame_x, self.frame_y = None, None
        self.size_x, self.size_y = 80, 100
        self.image = None
        self.before = None

        self.hp, self.mp = 10, 10

        self.gun = False
        self.bullet = Bullet()
        self.buff = Buff()
        self.buff_on = False


        self.animation = 0
        self.Idle_animation = [(0, 900), (75, 900)]   # 0
        self.run_animation = [(0, 500), (80, 500), (160, 500), (240, 500), (320, 500), (400, 500), (480, 500), (570, 500), (650, 500), (740, 500), (820, 500), (895, 500), (975, 500), (1055, 500), (1135, 500), (1220, 500)]    # 1
        self.back_animation = [(0, 900), (75, 900), (150, 900), (230, 900), (300, 900), (230, 900), (150, 900), (75, 900)]
        self.jump_animation = [(0, 760), (70, 745), (202, 740), (270, 740), (202, 740), (70, 745)]  # 3    # 나중에 찾자.....
        self.down_animation = None
        self.attack_animation = [(0, 420), (90, 420), (182, 420), (265, 420), (440, 420), (605, 420), (760, 420), (880, 420), (1000, 420), (90, 420)]  # 5
        self.defence_animation = [(0, 0), (50, 0), (100, 0)]

        self.gun_animation = [(0, 630), (75, 630), (155, 630), (240, 630), (325, 630), (408, 630), (492, 630), (600, 630), (325, 630), (240, 630), (155, 630)]  # 9
        self.fire_animation = [(5, 1260), (117 ,1250), (270 ,1250), (410, 1250), (550, 1250), (685, 1265), (835, 1265), (980, 1265), (1130, 1265), (1260, 1265), (0, 1025)]
        self.frame = 0
    def Initialize(self):
        self.x, self.y = 100,  410
        self.image = load_image('sprites/zerox.png')

    def draw(self):
        self.image.clip_draw(self.frame_x, self.frame_y, self.size_x, self.size_y, self.x, self.y)

        if self.gun is True:
            self.bullet.draw()
        elif self.buff_on is True:
            self.buff.draw()

    def update(self):
        if self.animation is 0:
            self.Idle_Animation()

        elif self.animation is 1:
            self.Run_Animation()

        elif self.animation is 2:
            self.Back_Animation()

        elif self.animation is 3:
            self.Jump_Animation()

        elif self.animation is 4:
            self.Down_Animation()

        elif self.animation is 5:
            self.Attck_Animation()

        elif self.animation is 6:
            self.Defense_Animation()

        elif self.animation is 7:
            self.Heal_Animation()

        elif self.animation is 8:
            self.Mana_Animation()

        elif self.animation is 9:
            self.Gun_Animation()

        elif self.animation is 10:
            self.Fire_Animation()

        if self.gun is True:
            self.bullet.update()
        if self.buff_on is True:
            self.buff.update()

    def handle_events(self):
        pass
    def update_animation(self, num):
        self.animation = num
        self.size_x = 75
        self.frame = 0
    def Idle_Animation(self):
        self.size_x = 75
        self.frame_x, self.frame_y = self.Idle_animation[self.frame]
        self.frame = (self.frame + 1) % 2
    def Run_Animation(self):
        self.frame_x, self.frame_y = self.run_animation[self.frame]
        self.frame = (self.frame + 1) % 16
        self.x += 200 // 16
        if self.frame is 15:
            self.x = 300
            self.frame = 0
            self.animation = 0
    def Back_Animation(self):
        self.frame_x, self.frame_y = self.back_animation[self.frame]
        self.frame = (self.frame+1) % 8
        self.x -= 200 // 8
        if self.frame is 15:
            self.x = 300
            self.frame = 0
            self.animation = 0          # 미완

    def Jump_Animation(self):
        self.frame_x, self.frame_y = self.jump_animation[self.frame]
        self.frame = (self.frame + 1) % 6
        self.y += 200//6

        if self.frame is 5:
            self.frame = 0
            self.animation = 0

    def Down_Animation(self):
        pass #4

    def Attck_Animation(self):
        if self.frame is 3 or self.frame is 4:
            self.size_x = 160
        elif self.frame is 5:
            self.size_x = 140
        elif self.frame is 6 or self.frame is 7:
            self.size_x = 105
        else:
            self.size_x = 80
        self.frame_x, self.frame_y = self.attack_animation[self.frame]
        self.frame = (self.frame + 1) % 10

        if self.frame is 9:
            self.frame = 0
            self.animation = 0
        if self.frame is 3 or self.frame is 4:
            self.size_x = 160
        elif self.frame is 5:
            self.size_x = 140
        elif self.frame is 6 or self.frame is 7:
            self.size_x = 105
        else:
            self.size_x = 80
        self.frame_x, self.frame_y = self.attack_animation[self.frame]
        self.frame = (self.frame+1)% 10

        if self.frame is 9:
            self.frame = 0
            self.animation = 0

    def Defense_Animation(self):
        if self.buff_on is False:
            self.buff.Initiallize(load_image('sprites/defense.png'), 1, self.x, self.y)
        self.buff_on = True
        self.animation = 0
        self.frame = 0
    def Heal_Animation(self):
        pass #7
    def Mana_Animation(self):
        pass #8
    def Gun_Animation(self):
        if self.frame is 5:
            self.size_x = 88
        elif self.frame is 6:
            self.size_x = 100
        elif self.frame is 7:
            self.size_x = 120
        elif self.frame is 8:
            self.gun = True
            self.bullet.Initialize(self.x, self.y)
            game_world.add_object(self.bullet, 1)
        else:
            self.size_x = 80
        self.frame_x, self.frame_y = self.gun_animation[self.frame]
        self.frame = (self.frame + 1) % 11

        if self.frame is 10:
            self.frame = 0
            self.animation = 0
    def Fire_Animation(self):
        if self.frame is 0:
            self.size_x = 120
            self.size_y = 120
        elif self.frame is 1:
            self.size_x = 150
            self.size_y = 140
        elif self.frame is 2:
            self.size_x = 140
            self.size_y = 140
        elif self.frame is 3 or self.frame is 4:
            self.size_x = 140
            self.size_y = 150
        elif self.frame is 5 or self.frame is 6:
            self.size_x = 150
            self.size_y = 160
        elif self.frame is 7 or self.frame is 9:
            self.size_x = 150
            self.size_y = 180
        elif self.frame is 8 or self.frame is 10:
            self.size_x = 140
            self.size_y = 180
        else:
            self.size_x = 100
            self.size_y = 100

        self.frame_x, self.frame_y = self.fire_animation[self.frame]
        self.frame = (self.frame+1)%11

        if self.frame is 10:
            self.animation = 0
            self.frame = 0
            self.size_x = 75
            self.size_y = 100

