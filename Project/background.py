from pico2d import *

STAGE_1 = 0
STAGE_2 = 1
STAGE_3 = 2

class Background:
    def __init__(self, who_are_you):
        self.image = None

        if who_are_you is STAGE_1 or who_are_you is STAGE_2:
            self.image = load_image('sprites\\map\\map1.jpg')
        elif who_are_you is STAGE_3:
            self.image = load_image('sprites\\map\\map2.png')

    def draw(self):
        self.image.draw(400, 300)
