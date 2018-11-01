from pico2d import *


class Background:
    def __init__(self):
        self.image = None
    def Initialize(self, image):
        self.image = image

    def draw(self):
        self.image.draw(400, 300)
