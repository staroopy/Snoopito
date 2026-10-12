import random, pyxel;
from seta import *;


def updateCapa(game): 
    no_play = game.colisao_botao(250, 60, 80, 23) #Botão play
    if no_play and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        game.play_pressionado = True
    else:
        game.play_pressionado = False

    if no_play and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)  #Toca som do botão
        game.estado = 'jogo'  #Muda para a tela principal do jogo

    no_quit = game.colisao_botao(250, 92, 70, 23) #Botão Quit
    if no_quit and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        game.quit_pressionado = True
    else:
        game.quit_pressionado = False

    if no_quit and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)
        pyxel.quit()  # Encerra o jogo

    no_music = game.colisao_botao(248, 122, 80, 25) #Botão Music
    if no_music and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        game.music_pressionado = True
    else:
        game.music_pressionado = False

    if no_music and pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)
        game.estado = 'musica'  #Vai para as músicas

def updateMusica(game):
    if pyxel.btnp(pyxel.KEY_V):
        game.estado = 'capa'
        
    no_california = game.colisao_botao(137, 50, 80, 22)
    no_creep= game.colisao_botao(137, 130,80,21)    
    no_wall= game.colisao_botao(137,90,80, 21)

    no_secret=game.colisao_botao(0,0,10,10)

    if no_california and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)
        pyxel.sounds[0].pcm("musicas/californiando.ogg")
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.5

    elif no_creep and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)
        pyxel.sounds[0].pcm("musicas/Creep.ogg")
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.5

    elif no_wall and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3, 1)
        pyxel.sounds[0].pcm("musicas/uau.ogg")
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.3

    elif no_secret and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
        pyxel.play(3,1)
        pyxel.sounds[0].pcm("musicas/Cheio.ogg")
        pyxel.play(0, 0, loop=True)
        pyxel.channels[0].gain = 0.3


#GameFunctions
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

def updateGame(game):
    game.charlie.update();
    game.mainChar.update(game.charlie.bird);

    if random.random() < game.amount: 
        game.setas.append(createSeta());
            
    for seta in game.setas: 
        if(seta.update()):
            game.life -= 0.1;
            game.setas.remove(seta);
            if not len(game.setas):
                game.setas.append(createSeta());

    if not int(game.life*10):
        game.estado = "gameo"

    for i in range(len(game.blocks)):
        game.blocks[i][0].update();

        if(pyxel.btnp(game.blocks[i][1])):
            
            game.blocks[i][0].touch();

            hit = checkSeta(game.blocks[i][0], game.setas, game.blocks[i][2]);
            game.score += hit;
            game.life -= 0.1 * (not hit);

            if not game.score % 5 and hit:
                game.charlie.speed = min(game.charlie.speed + 0.5, 10);
                game.amount += 0.01;