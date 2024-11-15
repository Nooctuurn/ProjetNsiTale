import pygame
import math


class personnage:


    def __init__(self, perso, x, y):
        self.x = x
        self.y = y
        self.perso = perso

    
    def avancer(self):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.x += 1
        
    def reculer(self):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.x -= 1

    def sauter(self):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.y += 1

    def attaque(self):



pygame.init()

#on mettra les images des personnage ici :

perso1 = pygame.image.load('image/player.png')
player = personnage(perso1, 0, 300)

#initialisation de la taille de la page 

screen = pygame.display.set_mode((1080, 720))

#maps et background
bg = pygame.image.load('image/bg.jpg')

running = True

while running:
    screen.blit(bg, (0 ,0))