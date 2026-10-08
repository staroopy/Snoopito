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
        super().__init__(pyxel.width*2/7 - 25/2, -25, 25, 25, 11);

    def draw(self):
       
        pyxel.blt(self.x,self.y,0,9,135,25,25,11)

class SetasUp(Seta):
    def __init__(self):
        super().__init__(pyxel.width*3/7 - 25/2, -25, 25, 25, 11);

    def draw(self):

        pyxel.blt(self.x,self.y,0,9,161,25,25,11)
        

class SetasRight(Seta):

    def __init__(self):
        super().__init__(pyxel.width*4/7 - 25/2, -25, 25, 25, 11);

    def draw(self): 

        pyxel.blt(self.x,self.y,0,35,135,25,25,11)

class SetasDown(Seta):
    def __init__(self):
        super().__init__(pyxel.width*5/7 - 25/2, -25, 25, 25, 3);

    def draw(self):
         pyxel.blt(self.x,self.y,0,36,163,25,25,11)
