import math;
import pyxel;

def rect(x, y, w, h, color):
    pyxel.rect(x, y, w, h, color);

def lerp(a, b, t):
    return a+(b-a)*t

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
    def __init__(self, x, y, w, h, color = 11):
        super().__init__(x, y, w, h, color);
        self.velX = 0;
        self.velY = 0;
        self.maxHeight = 40;
        self.minHeight = [y];
        self.t = 0;

    def draw(self):
        # rect(self.x, self.y, self.w, self.h, self.color);
        
        spriteCount = round(6 * min(round(self.t*10)/10 *2, 1));
        pyxel.blt(self.x, self.y, 0, 0 + self.w*spriteCount, 0, self.w, self.h, 11);
    
    def update(self, obj):
        self.y = self.minHeight[0]; 
        self.t = 0;
        if obj:
            begin = pyxel.width * .25;
            end = 0 - obj.w;
            t = (obj.x - begin) / (end - begin);
            self.t = abs(abs(t - .5)*2-1) if t >= 0 else 0;
            self.y = lerp(self.minHeight[0], self.maxHeight, self.t); 


class Charlie(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 13)
        self.speed = 1;
        self.bird = Bird(x, y+h*.3, 1, 1);
        self.sprite = 1;

    def update(self):
        if(self.bird.update(self.speed)):
            self.bird.x = self.x;
            self.sprite = 0;
        
        if(self.bird.x < pyxel.width/2):
            self.sprite = 1;

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.w*self.sprite, 37, self.w, self.h, 11);

        self.bird.draw();
#passaro
class Bird(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 13)

    def update(self, speed):
        self.x -= speed;
        return self.x + self.w < 0
    def draw (self):
        rect(self.x,self.y,self.w,self.h,self.color)
        pyxel.blt(self.x,self.y,0,71,38,25,25,11)


class Block(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);
        self.scale = 1;

    def touch(self):
        self.scale = 1.3;

    def update(self):
        self.scale = lerp(self.scale, 1, .3);


class Blockcima(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 166, 114, self.w, self.h, 11, scale=self.scale)


class Blockbaixo(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 197, 114, self.w, self.h, 11, scale=self.scale)


class Blockesquerda(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 103, 114, self.w, self.h, 11, scale=self.scale)


class Blockdireita(Block):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 135, 114, self.w, self.h, 11, scale=self.scale)