from pico2d import *

class Barrier:
    def __init__(self, x, y):
        self.x, self.y = x, y-5
        self.image = load_image('sprites\\player\\defense.png')
        self.buff_on = True

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass