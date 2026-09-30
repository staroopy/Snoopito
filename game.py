import pyxel;
import random;
from entity import *;
from seta import *;

def createSeta():
    return random.choice([SetasUp, SetasDown, SetasLeft, SetasRight])()

def checkSeta(block, setas, Seta):
    collided = False;
    groups = [seta for seta in setas if isinstance(seta, Seta)];
    for seta in groups:
        if(block.collide(seta)):
            setas.remove(seta);
            if not len(setas):
                setas.append(createSeta());
            collided = True;

    return collided;

class Game:      
    @staticmethod
    def run():
        pyxel.init(350, 200, title="Snoopy")

        Game.score = 0;
        Game.life = 1;
        Game.mainChar = Char(30, 110, 20, 40);
        Game.charlie = Charlie(300, 110, 20, 40);
        Game.floor = Entity(0, 150, 350, 50, 1);
        Game.setas = [createSeta()];
        Game.blocks = [
            [Block(pyxel.width*2/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_LEFT, SetasLeft],
            [Block(pyxel.width*3/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_UP, SetasUp],
            [Block(pyxel.width*4/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_RIGHT, SetasRight],
            [Block(pyxel.width*5/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_DOWN, SetasDown]
        ];
        Game.amount = 0;

        pyxel.run(Game.update, Game.draw);

    @staticmethod
    def update():    

        for i in range(len(Game.blocks)):
            if(pyxel.btnp(Game.blocks[i][1])):
                hit = checkSeta(Game.blocks[i][0], Game.setas, Game.blocks[i][2]);
                Game.score += hit;
                Game.life -= 0.1 * (not hit);

                if not Game.score % 5 and hit:
                    Game.charlie.throw();
                    Game.charlie.speed = min(Game.charlie.speed + 0.5, 10);
                    Game.amount += 0.01;

        Game.charlie.update();
        Game.mainChar.update(Game.charlie.bird[0] if len(Game.charlie.bird) else None);

        if random.random() < Game.amount: 
            Game.setas.append(createSeta());
            
        for seta in Game.setas: 
            if(seta.update()):
                Game.life -= 0.1;
                Game.setas.remove(seta);
                if not len(Game.setas):
                    Game.setas.append(createSeta());

        if not int(Game.life*10):
            pyxel.quit();



    @staticmethod
    def draw():
        pyxel.cls(0);
        Game.mainChar.draw();
        Game.charlie.draw();
        Game.floor.draw();

        for block in Game.blocks:
            block[0].draw();
        for seta in Game.setas:
            seta.draw();

        pyxel.text(10, 30, f"Score: {Game.score}", 5);

        rect(10, 10, 50, 16, 7);
        rect(12, 12, (50 - 4) * Game.life, 16 - 4, 8);

Game.run();