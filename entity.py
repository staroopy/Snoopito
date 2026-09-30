import math;
import pyxel;

JUMP_BEGIN = .25  # fração da largura da tela onde o pulo começa

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
        self.maxHeight = 30;
        self.minHeight = [y];

    def update(self, obj):
        self.y = self.minHeight[0]; 
        
        if obj:
            begin = pyxel.width*JUMP_BEGIN;
            end = 0 - obj.w;
            t = (obj.x - begin) / (end - begin);
            t = abs(abs(t - .5)*2-1)  if t >= 0 else 0;
            self.y = lerp(self.minHeight[0], self.maxHeight, t); 


class Charlie(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 13)
        self.bird = [];
        self.pending = 0;

        # velocidade única pra todos os pássaros, assim ninguém alcança o da
        # frente e a distância mínima do canThrow continua valendo
        self.speed = 5;

    def canThrow(self):
        if not self.bird:
            return True;
        # o último pássaro precisa estar longe o bastante pra que, quando o da
        # frente sumir, o próximo ainda não tenha entrado na faixa do pulo
        last = self.bird[-1];
        return self.x - last.x >= pyxel.width*JUMP_BEGIN + last.w;

    def update(self):
        if self.pending and self.canThrow():
            self.bird.append(Bird(self.x, self.y, 5, 5));
            self.pending -= 1;

        for bird in self.bird:
            if(bird.update(self.speed)):
                self.bird.remove(bird);

    def draw(self):
        super().draw();

        for bird in self.bird:
            bird.draw()

    def throw(self):
        self.pending += 1;

class Bird(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 13)

    def update(self, speed):
        self.x -= speed;
        return self.x + self.w < 0

class Block(Entity):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color);