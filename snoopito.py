import pyxel
pyxel.init(600, 400, title="Snoopy Dance")
pyxel.images[0].load(0,0,"papi.png")
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
def draw():
    pyxel.cls(5)
    pyxel.rectb(15, 21, 570, 302, 0) #Borda do de baixo
    pyxel.rect(16, 22, 568, 300, 15) #É o preenchimento do retângulo principal
    pyxel.rect(16, 242, 568, 80, 11) #Grama
    #Snoopy
    pyxel.blt(75, 122, 0, 0, 100,50, 100, 2) #coordenada 1 snoopy
    #pyxel.blt(75,122,0,140,1,110,121,2)
    #pyxel.blt(75,122,0,270,1,110,121,2)
#https://spelunky.fyi/mods/m/snoopy/
    pyxel.text (15,360,  "Viver e dancar, dancar e viver.\n - Snoopy (24/11/1965)", 7)
    pyxel.line(15, 350, 235, 350, 7)
pyxel.run(update, draw)