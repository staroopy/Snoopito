import pyxel


pyxel.init(350, 200, title="Snoopito")
pyxel.images[0].load(0,0,"png.png")

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    pyxel.cls(5)

#Tela principal (onde o jogo acontece)
    #pyxel.rectb(15, 21, 320, 132, 0) #Borda do de baixo
    #pyxel.rect(16, 22, 318, 130, 15) #É o preenchimento do retângulo principal
    #pyxel.rect(16, 129, 318, 23, 11) #Grama
    #pyxel.blt(20, 150, 0, 90, 32,  100, 40, 11) #Bonequinhos na tela
    #pyxel.blt(19, 163, 0, 90, 75,  100, 40, 11) #Bonequinhos na tela felizes (quando o player acertar a tecla)
    #pyxel.blt(225, 175, 0, 0, 75,  70, 40, 11) #Palavra "Snoopito" no jogo



#Game over:
    #pyxel.blt(145, 35, 0, 0, 190,  60, 30, 11)



#Snoopy:
    #pyxel.blt(50, 107, 0, 0, 0,  30, 30, 11)



#Snoopy pulando:
    #pyxel.blt(50, 107, 0, 25, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 51, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 77, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 102, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 127, 0,  30, 32, 11)
    #pyxel.blt(50, 107, 0, 152, 0,  30, 32, 11)



#Charlie Brown:
    #pyxel.blt(240, 100, 0, 30, 32,  30, 40, 11) #normal
    #pyxel.blt(240, 100, 0, 0, 32,  30, 40, 11) #Jogando o woodstock



#Woodstock:
    #pyxel.blt(210, 107, 0, 60, 32,  30, 20, 11)



#Setinhas do jogo (aparece para apertar):
    #pyxel.blt(95, 30, 0, 0, 130,  35, 30, 11) #Esquerda
    #pyxel.blt(165, 30, 0, 35, 130,  35, 30, 11) #Direita
    #pyxel.blt(130, 35, 0, 0, 160,  30, 30, 11) #Cima
    #pyxel.blt(190, 35, 0, 30, 160,  30, 30, 11) #Baixo



#Setinhas de fora (player apertando):
    #pyxel.blt(90, 119, 0, 61, 103,  40, 50, 11) #Esquerda
    #pyxel.blt(168, 119, 0, 105, 103,  25, 50, 11) #Direita
    #pyxel.blt(135, 119, 0, 132, 103,  25, 50, 11) #Cima 
    #pyxel.blt(196, 119, 0, 160, 103,  25, 50, 11) #Baixo 



#Capa:
    pyxel.blt(90, 0, 0, 120, 135,  150, 200, 11) #Imagem principal
    pyxel.blt(158, 130, 0, 65, 210,  50, 23, 11) #Play sem apertar
    pyxel.blt(158, 130, 0, 65, 232,  50, 23, 11) #Play apertado
    pyxel.blt(158, 155, 0, 65, 188,  50, 23, 11) #Quit sem apertar
    pyxel.blt(158, 155, 0, 65, 165,  50, 23, 11) #Quit apertado
    pyxel.blt(20, 140, 0, 90, 32,  100, 40, 11) #Bonequinhos
    pyxel.text(20, 183, "Feito por Alyssa Magano,\nGabriel Canto e Gabriel Estrela", 0)


pyxel.run(update, draw)