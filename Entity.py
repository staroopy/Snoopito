
class Entity:
    def __init__(self, x, y, w, h, color):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;
        self.color = color;

    def draw(self):
        rect(self.x, self.y, self.w, self.h, self.color);

    def collider(self, other, callback):
        if  other.x + other.w <= self.x and other.x >= self.x + self.w and other.y + other.h <= self.y and other.y >= self.y + self.h:
            callback(); 
           


class Char(Entity):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h, 11);
        self.velX = 0;
        self.velY = 0;

    def collide(self):
        self.color = 5;

    def move(self, ang, mag):
        ang *= math.pi/180;

        print(ang)
        self.velX += math.cos(ang) * mag;
        self.velY += math.sin(ang) * mag;

    def update(self):
        # gravidade
        self.velY += 1;

        self.x += self.velX;
        self.y += self.velY;

        if(self.y + self.h >= 400):
            self.x -= self.velX;
            self.y -= self.velY;

            self.velX = 0;
            self.velY = 0;