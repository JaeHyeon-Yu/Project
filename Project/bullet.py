from pico2d import *
import game_world
import main_state

class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x + 70, y
        self.image = load_image('sprites\\player\\bullet.png')

    def update(self):
        self.x += 20
        # if self.x > 400:
          #  game_world.remove_object(self)
        if main_state.monster.x <= self.x:
            main_state.hero.Change_My_Turn()
            main_state.monster.hp -= 5
    def draw(self):
        self.image.draw(self.x , self.y)