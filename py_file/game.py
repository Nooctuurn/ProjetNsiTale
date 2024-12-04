import pygame
import sys
from random import randint
from player import Player

pygame.init()

largeur, hauteur = 1200, 600
clock = pygame.time.Clock()
pygame.display.set_caption("Smash Banana")
ecran = pygame.display.set_mode((largeur, hauteur))

background = pygame.image.load('img/fond.jpeg')
bg = pygame.transform.scale(background, (largeur, hauteur))

player = Player(0, 320, 0, 0)
keys_pressed = set()
continuer = True

while continuer:
    clock.tick(60)
    ecran.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        elif event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
            if event.key == pygame.K_x:
                continuer = False
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_UP:
                player.move_up()

        elif event.type == pygame.KEYUP:
            keys_pressed.discard(event.key)
            if not keys_pressed.intersection({pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP}):
                player.stop()

    # Update and Draw Player
    player.update()
    player.draw(ecran)

    # Refresh Screen
    pygame.display.update()
