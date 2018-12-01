from pico2d import *

class Barrier:
    def __init__(self, x, y):
        self.x, self.y = x, y-5
        self.image = load_image('sprites\\player\\defense.png')
        self.buff_on = False

    def draw(self):
        if self.buff_on:
            self.image.draw(self.x, self.y)

    def update(self):
        if self.buff_on is False:
            self.buff_on = True
        else:
            self.buff_on = False

    def Pos_Update(self, x, y):
        self.x, self.y = x, y-5