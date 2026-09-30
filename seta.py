import pyxel;
from entity import Entity, rect;

class Seta(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);

    def update(self):
        self.y += 5;
        return self.y > pyxel.height;

class SetasLeft(Seta):
    def __init__(self):
        super().__init__(pyxel.width*2/7 - 25/2, -25, 25, 25, 4);

    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color);
        pyxel.tri(self.x, self.y + 25/2, self.x + 23, self.y, self.x + 23, self.y + 23, 0);

class SetasUp(Seta):
    def __init__(self):
        super().__init__(pyxel.width*3/7 - 25/2, -25, 25, 25, 2);

    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color);
        pyxel.tri(self.x + 25/2, self.y, self.x + 2, self.y + 23, self.x + 23, self.y + 23, 0);

class SetasRight(Seta):
    def __init__(self):
        super().__init__(pyxel.width*4/7 - 25/2, -25, 25, 25, 5);

    def draw(self): 
        rect(self.x, self.y, self.w, self.h, self.color);
        pyxel.tri(self.x + 23, self.y + 25/2, self.x + 2, self.y + 2, self.x + 2, self.y + 25, 0);

class SetasDown(Seta):
    def __init__(self):
        super().__init__(pyxel.width*5/7 - 25/2, -25, 25, 25, 3);

    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color);
        pyxel.tri(self.x + 25/2, self.y + 23, self.x + 2, self.y + 2, self.x + 25, self.y + 2, 0);
