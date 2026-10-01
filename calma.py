import pyxel

class App:
    def __init__(self):
        # 1. Inicializa a janela e ativa o cursor do mouse
        pyxel.init(350, 200, title="Snoopito")
        pyxel.mouse(True)

        # Carrega a imagem do arquivo fornecido
        # Certifique-se de que o arquivo de imagem está na mesma pasta
        pyxel.images[0].load(0, 0, "gab.png")


        pyxel.sounds[0].pcm("californiando.ogg")
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.5

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

        pyxel.run(self.update, self.draw)

    def colisao_botao(self, x, y, largura, altura): #Como identificar se o botão ta sendo apertado

        mx, my = pyxel.mouse_x, pyxel.mouse_y
        return x <= mx <= x + largura and y <= my <= y + altura

    def update(self):
        if pyxel.btnp(pyxel.KEY_S):
            pyxel.quit()

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
                self.estado = 'musica'  # Muda para a tela de música (a definir)
        elif self.estado == 'musica':
            if pyxel.btnp(pyxel.KEY_V):
                self.estado = 'capa'

    def draw(self):
        pyxel.cls(5)

        if self.estado == 'capa':
            # Imagem Principal
            pyxel.blt(90, 30, 0, 135, 135, 150, 200, 11)

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

        elif self.estado == 'jogo':
            # --- Tela Principal do Jogo ---
            pyxel.rectb(15, 21, 320, 132, 0) # Borda
            pyxel.rect(16, 22, 318, 130, 15) # Preenchimento principal
            pyxel.rect(16, 129, 318, 23, 11) # Grama
            pyxel.blt(20, 150, 0, 90, 32, 80, 40, 11) # Bonequinhos na tela
            pyxel.blt(225, 175, 0, 0, 75, 70, 10, 11) # Palavra "Snoopito"
            pyxel.blt(50, 107, 0, 0, 0, 30, 30, 11) # Snoopy
            pyxel.blt(240, 100, 0, 30, 32, 30, 40, 11) # Charlie Brown

        elif self.estado == 'musica': #Tela de música
            pyxel.text(150, 30, "Instrumentais", 0)
            pyxel.text(15, 175, "Pressione V para voltar", 0)

# Inicializa o jogo
App()