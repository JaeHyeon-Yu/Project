from pico2d import *

class Buff:
    def __init__(self):
        self.x, self.y = None, None
        self.image = None
        self.buff = None   # 어떤 버프니
        self.frame = 0

    def Initiallize(self, image, buff, x, y):
        self.x, self.y = x, y-5
        self.image = image
        self.buff = buff

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass