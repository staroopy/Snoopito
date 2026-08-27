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
        return other.x + other.w <= self.x and other.x >= self.x + self.w and other.y + other.h <= self.y and other.y >= self.y + self.h; 
           


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

        self.x += self.velX;
        self.y += self.velY;

        for obj in objs:
            if(self.collide(obj)):
                self.x -= self.velX;
                self.y -= self.velY;

                self.velX = 0;
                self.velY = 0;

class Game:
    @staticmethod
    def run():
        pyxel.init(500, 500, title="Snoopi")

        Game.mainChar = Char(50, 50, 50, 100);
        Game.floor = Entity(0, 400, 500, 100, 1);

        pyxel.run(Game.update, Game.draw);


    @staticmethod
    def update():    

        if pyxel.btnp(pyxel.KEY_W):
            Game.mainChar.move(-90, 25);

        Game.mainChar.update([Game.floor]);

    @staticmethod
    def draw():
        pyxel.cls(0);
        Game.mainChar.draw();
        Game.floor.draw();

Game.run();