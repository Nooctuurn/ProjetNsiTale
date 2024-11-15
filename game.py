import pygame as pg
pg.init()

largeur, hauteur = 1200, 800
ecran = pg.image.load('img/fond.jpeg')
ecran = pg.transform.scale(ecran, (largeur, hauteur))
screen = pg.display.set_mode((largeur, hauteur))

continuer = True
while continuer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = False
    screen.blit(ecran, (0, 0))
    pg.display.flip()
pg.quit()