import pygame
import sys
from game import*
from random import randint
from player import Player

pygame.init()

largeur, hauteur = 1200, 600
clock = pygame.time.Clock()
pygame.display.set_caption("Smash Banana")
ecran = pygame.display.set_mode((largeur, hauteur))

background = pygame.image.load('img/fond2.png')
bg = pygame.transform.scale(background, (largeur, hauteur))

icon = pygame.image.load('img/iconne.webp')
pygame.display.set_icon(icon)



player = Player(-60, 500, 0, 0, 4)
keys_pressed = set()
gamemode = "menu"
continuer = True

while continuer:
    if gamemode == "menu" :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                for nom, rect in boutons.items():
                    if rect.collidepoint(event.pos):
                        if nom == "Solo":
                            gamemode = "game"  # Lance les modes de jeu / paramètres
                        elif nom == "Multijoueur en local":
                            print("Lancer le mode multijoueur") 
                        elif nom == "Paramètres":
                            print("Ouvrir les paramètres")
    if gamemode == "multiplayer":
        ...
        
    if gamemode == "parametres":
        ...
    
    if gamemode == "game" :
        clock.tick(60)
        ecran.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

            elif event.type == pygame.KEYDOWN:
                keys_pressed.add(event.key)
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_LEFT:
                    player.move_left()
                #if event.key == pygame.K_DOWN:
                    #player.move_down()
                #if event.key == pygame.K_UP:
                    #player.move_up()

            elif event.type == pygame.KEYUP:
                keys_pressed.discard(event.key)
                if not keys_pressed.intersection({pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP}):
                    player.stop()

    # Update and Draw Player
    player.update()
    player.draw(ecran)

    # Refresh Screen
    pygame.display.update()
