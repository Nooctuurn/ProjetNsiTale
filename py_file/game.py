import pygame
import sys
from random import randint
pygame.init()

largeur, hauteur = 1200, 600
clock = pygame.time.Clock() 
pygame.display.set_caption("Smash Banana")
ecran = pygame.display.set_mode((largeur, hauteur))     
background = pygame.image.load('img/fond.jpeg')
bg = pygame.transform.scale(background, (largeur, hauteur)) # Elements qui gères la taille de la page et le fond
#programIcon = pygame.image.load('icon.jpg')
#pygame.display.set_icon(programIcon)
continuer = True