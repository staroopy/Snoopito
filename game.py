import math;
import pyxel;
import random;

def rect(x, y, w, h, color):
    pyxel.rect(x, y, w, h, color);

def createSeta():
    return SetasUp() if random.random() < 1/4 else SetasDown() if random.random() < 1/3 else SetasLeft() if random.random() < 1/2 else SetasRight();

class Entity:
    def __init__(self, x, y, w, h, color):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.color = color;

    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color);

    def collide(self, other):
        return other.x + other.w >= self.x and other.x <= self.x + self.w and other.y + other.h >= self.y and other.y <= self.y + self.h; 


class Char(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 11);
        self.velX = 0;
        self.velY = 0;

    def move(self, ang, mag):
        ang *= math.pi/180;

        self.velX += math.cos(ang) * mag;
        self.velY += math.sin(ang) * mag;

    def update(self, objs):
        # gravidade
        self.velY += 1;

        if pyxel.btnp(pyxel.KEY_W) and self.grounded:
            self.move(-90, 25);
            self.grounded = False;

        self.x += self.velX;
        self.y += self.velY;

        for obj in objs:
            if(self.collide(obj)):
                self.x -= self.velX;
                self.y -= self.velY;

                self.velX = 0;
                self.velY = 0;

                self.grounded = True;

class Seta(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);

    def update(self):
        self.y += 10;
        return self.y > pyxel.height;

class SetasUp(Seta):
    def __init__(self):
        super().__init__(pyxel.width*.3, -25, 50, 50, 2);

class SetasDown(Seta):
    def __init__(self):
        super().__init__(pyxel.width*.4, -25, 50, 50, 3);

class SetasLeft(Seta):
    def __init__(self):
        super().__init__(pyxel.width*.5, -25, 50, 50, 4);

class SetasRight(Seta):
    def __init__(self):
        super().__init__(pyxel.width*.6, -25, 50, 50, 5);

class Block(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);

class Game:      
    @staticmethod
    def run():
        pyxel.init(860, 540, title="Snoopi")

        Game.mainChar = Char(50, 50, 50, 100);
        Game.floor = Entity(0, 440, 960, 100, 1);
        Game.setas = [createSeta()];
        Game.blocks = [
            Block(pyxel.width*.3 - 15, pyxel.height*.8 - 15, 80, 80, 7),
            Block(pyxel.width*.4 - 15, pyxel.height*.8 - 15, 80, 80, 7),
            Block(pyxel.width*.5 - 15, pyxel.height*.8 - 15, 80, 80, 7),
            Block(pyxel.width*.6 - 15, pyxel.height*.8 - 15, 80, 80, 7)
        ];

        pyxel.run(Game.update, Game.draw);

    @staticmethod
    def update():    
        Game.mainChar.update([Game.floor]);
        for seta in Game.setas:
            if(seta.update()):
                Game.setas.remove(seta);
                Game.setas.append(createSeta())


    @staticmethod
    def draw():
        pyxel.cls(0);
        Game.mainChar.draw();
        Game.floor.draw();

        for block in Game.blocks:
            block.draw();
        for seta in Game.setas:
            seta.draw();



Game.run();