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
    def __init__(self):
            # 1. Inicializa a janela e ativa o cursor do mouse
            pyxel.init(350, 200, title="Snoopito")
            pyxel.mouse(True)
    
            pyxel.images[0].load(0, 0, "gazht.png")
    
            pyxel.sound(1).set(
                "C2E2G2C3E3G3C4C4C4C4",
                "P",
                "7777777777",
                "V",
                2
            )
            pyxel.sound(2).set(
                "F2A2C3F3R",
                "T",
                "76540",
                "S",
                3
            )
    
            self.estado = 'capa'  #Varias telas dps dessa
            self.play_pressionado = False
            self.quit_pressionado = False
            self.music_pressionado = False
            self.score = 0;
            self.life = 1;
            self.mainChar = Char(30, 110, 20, 40);
            self.charlie = Charlie(300, 110, 20, 40);
            self.floor = Entity(20, 150, 310, 20, 3);
            self.setas = [createSeta()];
            self.blocks = [
                [Block(pyxel.width*2/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_LEFT, SetasLeft],
                [Block(pyxel.width*3/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_UP, SetasUp],
                [Block(pyxel.width*4/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_RIGHT, SetasRight],
                [Block(pyxel.width*5/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_DOWN, SetasDown]
            ];
            self.amount = 0;


            pyxel.run(self.update, self.draw)
    
    def colisao_botao(self, x, y, largura, altura): #Como identificar se o botão ta sendo apertado
    
        mx, my = pyxel.mouse_x, pyxel.mouse_y
        return x <= mx <= x + largura and y <= my <= y + altura

    
    def update(self):    

        # Som de pulo nas setas
        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT):
            pyxel.play(3, 2)

#Botões da tela principal
        if self.estado == 'capa':
            no_play = self.colisao_botao(250, 60, 80, 23) #Botão play
            if no_play and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.play_pressionado = True
            else:
                self.play_pressionado = False

            if no_play and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)  #Toca som do botão
                self.estado = 'jogo'  #Muda para a tela principal do jogo

            no_quit = self.colisao_botao(250, 92, 70, 23) #Botão Quit
            if no_quit and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.quit_pressionado = True
            else:
                self.quit_pressionado = False

            if no_quit and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)
                pyxel.quit()  # Encerra o jogo

            no_music = self.colisao_botao(248, 122, 80, 25) #Botão Music
            if no_music and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.music_pressionado = True
            else:
                self.music_pressionado = False

            if no_music and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)
                self.estado = 'musica'  #Vai para as músicas

        elif self.estado == 'musica':
            if pyxel.btnp(pyxel.KEY_V):
                self.estado = 'capa'
        
            no_california = self.colisao_botao(137, 50, 80, 22)
            no_creep= self.colisao_botao(137, 130,80,21)    
            no_wall= self.colisao_botao(137,90,80, 21)

            no_secret=self.colisao_botao(0,0,10,10)

            if no_california and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)
                pyxel.sounds[0].pcm("californiando.ogg")
                pyxel.play(0, 0, loop=True)
                pyxel.channels[0].gain = 0.5

            elif no_creep and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)
                pyxel.sounds[0].pcm("Creep.ogg")
                pyxel.play(0, 0, loop=True)
                pyxel.channels[0].gain = 0.5

            elif no_wall and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3, 1)
                pyxel.sounds[0].pcm("uau.ogg")
                pyxel.play(0, 0, loop=True)
                pyxel.channels[0].gain = 0.3

            elif no_secret and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                pyxel.play(3,1)
                pyxel.sounds[0].pcm("Cheio.ogg")
                pyxel.play(0, 0, loop=True)
                pyxel.channels[0].gain = 0.3

        elif self.estado == 'jogo':
            self.charlie.update();
            self.mainChar.update(self.charlie.bird[0] if len(self.charlie.bird) else None);

            if random.random() < self.amount: 
                self.setas.append(createSeta());
                    
            for seta in self.setas: 
                if(seta.update()):
                    self.life -= 0.1;
                    self.setas.remove(seta);
                    if not len(self.setas):
                        self.setas.append(createSeta());

            if not int(self.life*10):
                self.estado = "gameo"

            for i in range(len(self.blocks)):
                if(pyxel.btnp(self.blocks[i][1])):
                    hit = checkSeta(self.blocks[i][0], self.setas, self.blocks[i][2]);
                    self.score += hit;
                    self.life -= 0.1 * (not hit);

                    if not self.score % 5 and hit:
                        self.charlie.throw();
                        self.charlie.speed = min(self.charlie.speed + 0.5, 10);
                        self.amount += 0.01;
            # print(not int(self.life*10))

        elif self.estado=='gameo':
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_V):
                self.estado = 'capa'

    def draw(self):
        rect(0, 0, pyxel.width, pyxel.height, 5)
        if self.estado == 'capa':
            # Imagem Principal
            pyxel.blt(90, 30, 0, 135, 138, 150, 200, 11)

            # Desenho do Botão Play (Solto vs Pressionado)
            if self.play_pressionado:
                pyxel.blt(250, 61, 0, 65, 232, 70, 25, 11)
            else:
                pyxel.blt(250, 60, 0, 65, 210, 80, 23, 11)

            # Desenho do Botão Quit (Solto vs Pressionado)
            if self.quit_pressionado:
                pyxel.blt(250, 92, 0, 65, 165, 70, 23, 11)
            else:
                pyxel.blt(250, 92, 0, 65, 188, 70, 23, 11)

            # Desenho do Botão Music (Solto vs Pressionado)
            if self.music_pressionado:
                pyxel.blt(248, 122, 0, 180, 0, 80, 25, 11)
            else:
                pyxel.blt(248, 122, 0, 180, 25, 80, 25, 11)

            # Demais elementos da capa
            pyxel.blt(20, 140, 0, 90, 32, 80, 40, 11)  # Bonequinhos
            pyxel.text(20, 183, "Feito por Alyssa Magano,\nGabriel Canto e Gabriel Estrela", 0)
        
        elif self.estado== 'jogo':
            pyxel.cls(5);
            pyxel.rectb(19, 39, 312, 132, 0) # Borda
            pyxel.blt(10, 160, 0, 90, 32, 80, 40, 11) # Bonequinhos na tela
            pyxel.blt(240, 185, 0, 0, 75, 70, 10, 11) # Palavra "Snoopito"
            rect(20,40,310,120,15)
            self.mainChar.draw();
            self.charlie.draw();
            self.floor.draw();

            for block in self.blocks:
                block[0].draw();
            for seta in self.setas:
                seta.draw();

            pyxel.text(10, 30, f"Score: {self.score}", 7);

            rect(10, 10, 50, 16, 7);
            rect(12, 12, (50 - 4) * self.life, 16 - 4, 8);
        
        elif self.estado == 'musica': #Tela de música
            pyxel.text(150, 30, "Instrumentais", 0)
            pyxel.text(15, 175, "Pressione V para voltar", 0)
            pyxel.blt(137, 50, 0, 180, 50, 80, 22, 11) #Hotel
            pyxel.blt(137, 130, 0, 180, 93, 80, 21, 11) #Creep
            pyxel.blt(137, 90, 0, 180, 72, 80, 21, 11) #A-wall

        elif self.estado == 'gameo': #Tela de Game Overrr
            pyxel.text(145, 45, f"Score final:\n     {self.score}", 0) #Score
            pyxel.blt(90, 75, 0, 135, 138, 150, 200, 11) #Snoopy
            pyxel.blt(140, 15, 0, 3, 193, 60, 30, 11) #Game over
            pyxel.text(30, 180, "Sair [Q]", 0) #Sair do jogo

Game();