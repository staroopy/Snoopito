import pyxel;
from entity import *;

def drawCapa(game):
    # Imagem Principal
    pyxel.blt(90, 30, 0, 135, 138, 150, 200, 11)

    # Desenho do Botão Play (Solto vs Pressionado)
    if game.play_pressionado:
        pyxel.blt(250, 61, 0, 65, 232, 70, 25, 11)
    else:
        pyxel.blt(250, 60, 0, 65, 210, 80, 23, 11)

    # Desenho do Botão Quit (Solto vs Pressionado)
    if game.quit_pressionado:
        pyxel.blt(250, 92, 0, 65, 165, 70, 23, 11)
    else:
        pyxel.blt(250, 92, 0, 65, 188, 70, 23, 11)

    # Desenho do Botão Music (Solto vs Pressionado)
    if game.music_pressionado:
        pyxel.blt(248, 122, 0, 180, 0, 80, 25, 11)
    else:
        pyxel.blt(248, 122, 0, 180, 25, 80, 25, 11)

    # Demais elementos da capa
    pyxel.blt(20, 140, 0, 90, 32, 80, 40, 11)  # Bonequinhos
    pyxel.text(20, 183, "Feito por Alyssa Magano,\nGabriel Canto e Gabriel Estrela", 0)

def drawGame(game):
    pyxel.cls(5);
    rect(20,40,310,120,15)
    
    game.floor.draw();
    game.mainChar.draw();
    game.charlie.draw();

    for block in game.blocks:
        block[0].draw();
    for seta in game.setas:
        seta.draw();

    rect(0, 0, 20, pyxel.height, 5);
    rect(0, 0, pyxel.width, 40, 5);
    rect(0, 170, pyxel.width, 40, 5);
        
    pyxel.rectb(19, 39, 312, 132, 0) # Borda
    pyxel.blt(10, 160, 0, 90, 32, 80, 40, 11) # Bonequinhos na tela
    pyxel.blt(240, 185, 0, 0, 75, 70, 10, 11) # Palavra "Snoopito"


    pyxel.text(10, 30, f"Score: {game.score}", 7);

    rect(10, 10, 50, 16, 7);
    rect(12, 12, (50 - 4) * game.life, 16 - 4, 8);
