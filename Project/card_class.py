from pico2d import *

class Card:
    def __init__(self):
        self.image = None
        self.tx, self.ty = 0, 0
        self.sx, self.sy = 0,  0
        self.number = None
        self.use = None
        self.mp = 0

    def Initialize(self, num, image, tx, ty):
        self.image = image
        self.number = num
        self.tx, self.ty = tx, ty
        self.use = False

        if num is 3:
            self.mp = 3
        elif num is 5:
            self.mp = 5



    def draw(self):
        if self.use is False:
            self.image.draw(self.tx, self.ty)


    def Click(self, x, y):
        if self.tx - 55 <= x and x <= self.tx + 55 and self.ty - 70 <= y and y <= self.ty + 70:
            return True
        else:
            return False

    def Check(self):
        if self.image == None:
            return True
        else:
            return False

    def delete(self):
        self.use = True