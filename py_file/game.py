import pygame
import sys
import menu
from random import randint
from player import Player
from perso_nj import Bot

pygame.init()

largeur, hauteur = 1200, 600
clock = pygame.time.Clock()
pygame.display.set_caption("Smash Banana")
ecran = pygame.display.set_mode((largeur, hauteur))

# Importation des images / icônes

# Initialisation du bot
bot = Bot("Bot de pierre", 100, 50, 1, 'img/Bot.png')
x_bot, y_bot = 800, 300  # Position initiale du bot
direction_bot = -1  # Mouvement du bot


bg_menu = pygame.image.load('img/fond.jpeg')
bg_menu = pygame.transform.scale(bg_menu,(largeur,hauteur))

bg_jeu = pygame.image.load('img/fond2.png') # Jeu
bg_jeu = pygame.transform.scale(bg_jeu, (largeur, hauteur)) # Jeu

icon = pygame.image.load('img/iconne.webp')
pygame.display.set_icon(icon)

player = ""
keys_pressed = set()
allowed_char = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_a]
gamemode = "Menu"

player = Player(-60, 500, 0, 0, 10)

continuer = True
print(f"DEBUG : Gamemode -> {gamemode}")
while continuer:
    clock.tick(60)

    if gamemode == "Menu": #Affichage du menu 
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
        

    if gamemode == "Solo": #Affichage du mode de jeu "Solo"
        ecran.blit(bg_jeu, (0, 0))
        pygame.display.set_caption("Smash Banana - Solo")

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
                if event.key == pygame.K_a:
                    player.fast_atack()
                    player.stop()
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

        # Déplacement du bot
        if bot:
            x_bot += direction_bot
            if x_bot <= 600:  # Limite gauche
                direction_bot = 1
            elif x_bot >= 800:  # Limite droite
                direction_bot = -1

        # Zone d'attaque du joueur
        if player.mouvement == "atack1":
            attack_zone = player.rect.inflate(50, 0)  # Étendre la zone d'attaque en largeur
            bot_rect = pygame.Rect(x_bot, y_bot, bot.width, bot.height)  # Rectangle du bot
            if attack_zone.colliderect(bot_rect):  # Collision entre la zone d'attaque et le bot
                bot_stop = bot.prend_des_degat(10)  # Inflige 10 dégâts au bot
                if bot_stop:  # Si le bot est détruit
                    print(f"{bot.nom} est détruit !")
                    bot = None  # Supprime le bot
                else:
                    print(f"{bot.nom} a {bot.pv} PV restants.")

        # Mise à jour et affichage
        player.update()
        player.draw(ecran)

        # Dessiner le bot
        if bot:
            ecran.blit(bot.image, (x_bot, y_bot))

    if gamemode == "Multiplayer":# Affichage du mode de jeu Multijoueur
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False

    if gamemode == "Settings":#Affichage du menu des paramètres 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False


    pygame.display.update()
