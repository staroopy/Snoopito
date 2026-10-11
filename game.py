import pyxel;
from entity import *;
from loopFunctions.updateFunctions import *;
from loopFunctions.drawFunctions import *;

class Game:
    def __init__(self):
        # 1. Inicializa a janela e ativa o cursor do mouse
        pyxel.init(350, 200, title="Snoopito")
        pyxel.mouse(True)

        pyxel.images[0].load(0, 0, "musicas/gazht.png")

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
        self.mainChar = Char(30, 124, 19, 30);
        self.charlie = Charlie(300, 110, 20, 40);
        self.floor = Entity(20, 150, 310, 20, 3);
        self.setas = [createSeta()];
        self.blocks = [
            [Blockesquerda(pyxel.width*2/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_LEFT, SetasLeft],
            [Blockcima(pyxel.width*3/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_UP, SetasUp],
            [Blockdireita(pyxel.width*4/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_RIGHT, SetasRight],
            [Blockbaixo(pyxel.width*5/7 - 15, pyxel.height*.8 - 15, 30, 30, 7), pyxel.KEY_DOWN, SetasDown]
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
            updateCapa(self);

        elif self.estado == 'musica':
            updateMusica(self);

        elif self.estado == 'jogo':
            updateGame(self);

        elif self.estado=='gameo':
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_V):
                self.estado = 'capa'

    def draw(self):
        rect(0, 0, pyxel.width, pyxel.height, 5)
        if self.estado == 'capa':
            drawCapa(self);
        
        elif self.estado == 'jogo':
            drawGame(self);

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