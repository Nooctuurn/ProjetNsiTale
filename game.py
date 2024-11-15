import pygame as pg
pg.init()

largeur, hauteur = 1200, 800
screen = pg.display.set_mode((largeur, hauteur))

continuer = True
while continuer:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = False
pg.quit()