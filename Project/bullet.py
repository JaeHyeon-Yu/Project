from pico2d import *
import game_world

class Bullet:
    def __init__(self, x, y):
        self.x, self.y = x + 70, y
        self.image = load_image('sprites\\player\\bullet.png')

    def update(self):
        self.x += 10
        if self.x > 600:
            game_world.remove_object(1)

    def draw(self):
        self.image.draw(self.x , self.y)