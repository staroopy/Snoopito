import math;
import pyxel;

def rect(x, y, w, h, color):
    pyxel.rect(x, y, w, h, color);


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

        print(ang)
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

class Setas(Entity):
    def __init__(self, x, y, w, h):
        super().__init_(x, y, w, h);
        self.direction;

    def update():
        

class SetasUp(Setas):
    def __init__(self, x, y):
        super().__init_(x, y, 25, 25);
        self.direction = 'U';

class SetasDown(Setas):
    def __init__(self, x, y):
        super().__init_(x, y, 25, 25);
        self.direction = 'D';

class SetasLeft(Setas):
    def __init__(self, x, y):
        super().__init_(x, y, 25, 25);
        self.direction = 'L';

class SetasRight(Setas):
    def __init__(self, x, y):
        super().__init_(x, y, 25, 25);
        self.direction = 'R';

class Game:
    @staticmethod
    def run():
        pyxel.init(860, 540, title="Snoopi")

        Game.mainChar = Char(50, 50, 50, 100);
        Game.floor = Entity(0, 440, 960, 100, 1);

        pyxel.run(Game.update, Game.draw);


    @staticmethod
    def update():    
        Game.mainChar.update([Game.floor]);

    @staticmethod
    def draw():
        pyxel.cls(0);
        Game.mainChar.draw();
        Game.floor.draw();

Game.run();