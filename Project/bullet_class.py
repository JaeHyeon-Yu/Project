from pico2d import *
import game_world

class Bullet:
    def __init__(self):
        self.x, self.y = None, None
        self.image = None

    def Initialize(self, x, y):
        self.x, self.y = x + 70, y
        self.image = load_image('sprites/bullet.png')

    def update(self):
        self.x += 10
        if self.x > 600:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x , self.y)