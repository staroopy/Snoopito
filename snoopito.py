import pyxel


pyxel.init(350, 200, title="Snoopito")
pyxel.images[0].load(0,0,"gab.png")



def update():
    if pyxel.btnp(pyxel.KEY_S):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT):#pulo
        pyxel.play(3,2)
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3,1)


class App:
     def __init__(self):
        # Hotel California:
        pyxel.sounds[0].pcm("californiando.ogg") 
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.5


        # 
        # pyxel.sounds[0].pcm("californiando.ogg") 
        # pyxel.play(0, 0, loop=True)
        # pyxel.channels[0].gain = 0.5


        pyxel.sound(1).set( #botões (start e quit)
    "C2E2G2C3E3G3C4C4C4C4", 
    "P",                    
    "7777777777",           
    "V",                    
    2                       
)
        pyxel.sound(2).set( #pulo
    "F2A2C3F3R",    
    "T",            
    "76540",        
    "S",           
    3               
)



def draw():
    pyxel.cls(5)



#Tela principal (onde o jogo acontece)
    # pyxel.rectb(15, 21, 320, 132, 0) #Borda do de baixo
    # pyxel.rect(16, 22, 318, 130, 15) #É o preenchimento do retângulo principal
    # pyxel.rect(16, 129, 318, 23, 11) #Grama
    # pyxel.blt(20, 150, 0, 90, 32,  100, 40, 11) #Bonequinhos na tela
    # pyxel.blt(19, 163, 0, 90, 75,  100, 40, 11) #Bonequinhos na tela felizes (quando o player acertar a tecla)
    # pyxel.blt(225, 175, 0, 0, 75,  70, 10, 11) #Palavra "Snoopito" no jogo



#Game over:
    # pyxel.blt(132, 35, 0, 0, 190,  60, 30, 11)



#Snoopy:
    # pyxel.blt(50, 107, 0, 0, 0,  30, 30, 11)



#Snoopy pulando:
    #pyxel.blt(50, 107, 0, 25, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 51, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 77, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 102, 0,  30, 30, 11)
    #pyxel.blt(50, 107, 0, 127, 0,  30, 32, 11)
    #pyxel.blt(50, 107, 0, 152, 0,  30, 32, 11)



#Charlie Brown:
    # pyxel.blt(240, 100, 0, 30, 32,  30, 40, 11) #normal
    # pyxel.blt(240, 100, 0, 0, 32,  30, 40, 11) #Jogando o woodstock


#Score:
    # pyxel.blt(140, 160, 0, 0, 85,  70, 40, 11)


#Woodstock:
    # pyxel.blt(210, 107, 0, 60, 32,  30, 20, 11)



#Setinhas do jogo (aparece para apertar):
    # pyxel.blt(95, 30, 0, 0, 130,  35, 30, 11) #Esquerda
    # pyxel.blt(165, 30, 0, 35, 130,  35, 30, 11) #Direita
    # pyxel.blt(130, 35, 0, 0, 160,  30, 30, 11) #Cima
    # pyxel.blt(190, 35, 0, 30, 160,  30, 30, 11) #Baixo



#Setinhas de fora (player apertando):
    # pyxel.blt(90, 119, 0, 61, 103,  40, 50, 11) #Esquerda
    # pyxel.blt(168, 119, 0, 105, 103,  25, 50, 11) #Direita
    # pyxel.blt(135, 119, 0, 132, 103,  25, 50, 11) #Cima 
    # pyxel.blt(196, 119, 0, 160, 103,  25, 50, 11) #Baixo 



#Capa:
    pyxel.blt(90, 30, 0, 135, 135,  150, 200, 11) #Imagem principal
    pyxel.blt(250, 60, 0, 65, 210,  80, 23, 11) #Play sem apertar
    pyxel.blt(250, 61, 0, 65, 232,  70, 25, 11) #Play apertado
    pyxel.blt(250, 92, 0, 65, 188,  70, 23, 11) #Quit sem apertar
    pyxel.blt(250, 92, 0, 65, 165,  70, 23, 11) #Quit apertado
    pyxel.blt(248, 122, 0, 180, 0,  80, 25, 11) #Music sem apertar
    pyxel.blt(248, 122, 0, 180, 0,  80, 25, 11) #Music sem apertar
    pyxel.blt(20, 140, 0, 90, 32,  80, 40, 11) #Bonequinhos
    pyxel.text(20, 183, "Feito por Alyssa Magano,\nGabriel Canto e Gabriel Estrela", 0)



App()
pyxel.run(update, draw)