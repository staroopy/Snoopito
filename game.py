import math;
import pyxel;
import random;

def rect(x, y, w, h, color):
    pyxel.rect(x, y, w, h, color);

def createSeta():
    return random.choice([SetasUp, SetasDown, SetasLeft, SetasRight])()

def checkSeta(block, setas, Seta):
    collided = False;
    groups = [seta for seta in setas if isinstance(seta, Seta)];
    for seta in groups:
        if(block.collide(seta)):
            setas.remove(seta);
            setas.append(createSeta());
            collided = True;

    return collided;

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

class Block(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);

class Game:      
    @staticmethod
    def run():
        pyxel.init(350, 200, title="Snoopy")

        Game.score = 0;
        Game.life = 1;
        Game.mainChar = Char(20, 0, 20, 40);
        Game.floor = Entity(0, 150, 350, 50, 1);
        Game.setas = [createSeta()];
        Game.blocks = [
            Block(pyxel.width*2/7 - 15, pyxel.height*.8 - 15, 30, 30, 7),
            Block(pyxel.width*3/7 - 15, pyxel.height*.8 - 15, 30, 30, 7),
            Block(pyxel.width*4/7 - 15, pyxel.height*.8 - 15, 30, 30, 7),
            Block(pyxel.width*5/7 - 15, pyxel.height*.8 - 15, 30, 30, 7)
        ];

        pyxel.run(Game.update, Game.draw);

    @staticmethod
    def update():    
        Game.mainChar.update([Game.floor]);

        for seta in Game.setas: 
            if(seta.update()):
                Game.life -= 0.1;
                Game.setas.remove(seta);
                Game.setas.append(createSeta());

        if(pyxel.btnp(pyxel.KEY_LEFT)):
            Game.score += checkSeta(Game.blocks[0], Game.setas, SetasLeft);

        if(pyxel.btnp(pyxel.KEY_UP)):
            Game.score += checkSeta(Game.blocks[1], Game.setas, SetasUp);

        if(pyxel.btnp(pyxel.KEY_RIGHT)):
            Game.score += checkSeta(Game.blocks[2], Game.setas, SetasRight);

        if(pyxel.btnp(pyxel.KEY_DOWN)):
            Game.score += checkSeta(Game.blocks[3], Game.setas, SetasDown);

        if pyxel.btnp(pyxel.KEY_W) and Game.char.grounded:
            Game.char.move(-90, 25);
            Game.char.grounded = False;

        if not int(Game.life*10):
            pyxel.quit();
    @staticmethod
    def draw():
        pyxel.cls(0);
        Game.mainChar.draw();
        Game.floor.draw();

        for block in Game.blocks:
            block.draw();
        for seta in Game.setas:
            seta.draw();

        pyxel.text(10, 45, f"Score: {Game.score}", 5);

        rect(10, 10, 100, 30, 7);
        rect(15, 15, 90 * Game.life, 20, 8);
Game.run();