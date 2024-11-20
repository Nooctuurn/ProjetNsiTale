import pygame
from player import*
from player import Player
pygame.init()

largeur, hauteur = 1200, 800
ecran = pygame.image.load('img/fond.jpeg')
ecran = pygame.transform.scale(ecran, (largeur, hauteur))
screen = pygame.display.set_mode((largeur, hauteur))

player = Player(0, 320, 0, 0)
keys_pressed = set()
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_x: # Ferme le jeu quand on appuie sur la croix ou sur la touche x en mettant la variable continuer à False
            continuer = False

        elif event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()              # Gère touts les déplacements du joueurs en fonction de quelle flèche est pressée
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_UP:
                player.move_up()
        if event.type == pygame.KEYUP:
            keys_pressed.discard(event.key) # Retire la touche relâchée de l'ensemble des touches pressées
            if not keys_pressed.intersection({pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP}):
                player.stop()
    player.update()
    screen.blit(ecran, (0, 0))
    player.draw(ecran)
    pygame.display.update()
pygame.quit()