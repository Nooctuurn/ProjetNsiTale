import pygame
import sys
import menu
from random import randint
from player import Player

pygame.init()

largeur, hauteur = 1200, 600
clock = pygame.time.Clock()
pygame.display.set_caption("Smash Banana")
ecran = pygame.display.set_mode((largeur, hauteur))

# Importation des images / icônes

bg_menu = pygame.image.load('img/fond.jpeg')
bg_menu = pygame.transform.scale(bg_menu,(largeur,hauteur))

bg_jeu = pygame.image.load('img/fond2.png') # Jeu
bg_jeu = pygame.transform.scale(bg_jeu, (largeur, hauteur)) # Jeu

icon = pygame.image.load('img/iconne.webp')
pygame.display.set_icon(icon)

player = ""
keys_pressed = set()
allowed_char = [pygame.K_RIGHT, pygame.K_LEFT]
gamemode = "Menu"

continuer = True
print(f"DEBUG : Gamemode -> {gamemode}")
while continuer:
    clock.tick(60)
    if gamemode == "Menu":
        ecran.blit(bg_menu,(0,0))
        pygame.display.set_caption("Smash Banana - Menu Principal")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                for nom, rect in menu.boutons.items(): # Lance les modes de jeu / paramètres
                    if rect.collidepoint(event.pos):
                        if nom == "Solo":
                            gamemode = "Solo"
                            print(f"DEBUG : Gamemode -> {gamemode}")
                            break
                        
                        elif nom == "Multijoueur en local":
                              gamemode = "Multiplayer"
                              print(f"DEBUG : Gamemode -> {gamemode}")
                              break
                        
                        elif nom == "Paramètres":
                            gamemode = "Settings"
                            print(f"DEBUG : Gamemode -> {gamemode}")
                            break

        for nom, rect in menu.boutons.items():
            menu.dessiner_bouton(menu.fenetre, rect, nom, menu.GRIS, menu.BLANC)
        

    if gamemode == "Solo" :
        ecran.blit(bg_jeu, (0, 0))
        player = Player(-60, 500, 0, 0, 10)
        print("DEBUG : BLOQUÉ ICI2")
        pygame.display.set_caption("Smash Banana - Solo")
        print("DEBUG : BLOQUÉ ICI1")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

            elif event.type == pygame.KEYDOWN:
                if not event.key in allowed_char:
                    break
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
                if not event.key in allowed_char:
                    break
                keys_pressed.discard(event.key)
                if not keys_pressed.intersection({pygame.K_RIGHT, pygame.K_LEFT}):
                        player.stop()

        player.update()
        player.draw(ecran)

    if gamemode == "Multiplayer" :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

    if gamemode == "Settings" : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False


    pygame.display.update()
