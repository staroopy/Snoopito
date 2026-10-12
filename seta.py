import pyxel;
from entity import Entity, rect;

class Seta(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);
        self.speed = 5;

    def update(self):
        self.y += self.speed;
        return self.y > pyxel.height;

class SetasLeft(Seta):
    def __init__(self):
        super().__init__(pyxel.width*2/7 - 25/2, -18, 25, 18, 11);

    def draw(self):
        pyxel.blt(self.x,self.y,0, 8, 141, self.w, self.h,11)

class SetasUp(Seta):
    def __init__(self):
        super().__init__(pyxel.width*3/7 - 18/2, -25, 18, 25, 11);

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 9, 161, self.w, self.h,11)
        

class SetasRight(Seta):

    def __init__(self):
        super().__init__(pyxel.width*4/7 - 25/2, -25, 25, 18, 11);

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 36, 141, self.w, self.h, 11)

class SetasDown(Seta):
    def __init__(self):
        super().__init__(pyxel.width*5/7 - 18/2, -25, 18, 25, 3);

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 38, 162, self.w, self.h, 11)
