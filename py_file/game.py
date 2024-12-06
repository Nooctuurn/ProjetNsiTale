import pygame
import sys
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

player = Player(-60, 500, 0, 0, 10)
keys_pressed = set()
continuer = True
allowed_char = [pygame.K_RIGHT, pygame.K_LEFT]

while continuer:
    clock.tick(60)
    ecran.blit(bg, (0, 0))

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

    # Update and Draw Player
    player.update()
    player.draw(ecran)

    # Refresh Screen
    pygame.display.update()
