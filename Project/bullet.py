from pico2d import *
import game_world
import main_state

class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x + 70, y
        self.image = load_image('.\\sprites\\player\\bullet.png')
        self.bullet_is_fly = True

    def update(self):
        self.x += 20
        hero = main_state.get_player()
        monster = main_state.get_monster()
        if monster.x <= self.x and monster.y-50 <= self.y and self.y <= monster.y + 50 and self.bullet_is_fly is True:
            hero.Change_My_Turn()
            monster.hp -= 5
            self.bullet_is_fly = False
        elif self.x >= 800 and self.bullet_is_fly is True:
            hero.Change_My_Turn()
            self.bullet_is_fly = False
    def draw(self):
        if self.bullet_is_fly is True:
            self.image.draw(self.x , self.y)