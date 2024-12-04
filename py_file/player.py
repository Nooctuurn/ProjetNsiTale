import pygame
import sys
from pygame.locals import*
from random import randint

pygame.init()
largeur, hauteur = 1200, 600

sprite_sheet_RUN = pygame.image.load("Sprite\Knight 2D Pixel Art\Sprites\with_outline\RUN.png")
RUN_frame_width = sprite_sheet_RUN.get_width() // 8
RUN_frame_height = sprite_sheet_RUN.get_height()

sprite_sheet_IDLE = pygame.image.load("Sprite\Knight 2D Pixel Art\Sprites\with_outline\IDLE.png")
IDLE_frame_width = sprite_sheet_IDLE.get_width() // 8
IDLE_frame_height = sprite_sheet_IDLE.get_height()
STAY_frame = sprite_sheet_IDLE.subsurface(pygame.Rect(0, 0, IDLE_frame_width, IDLE_frame_height))

class Player(pygame.sprite.Sprite): # Classe qui gère le joueur et l'ensemble du jeu
    player = STAY_frame
    #player.set_colorkey((255, 255, 255))
    pl = pygame.transform.scale(player, (200, 200))

    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = [x, y] # Initialise la position du joueur avec les coordonnées x et y
        self.velocity = [velocity_x, velocity_y] # Initialise la vélocité du joueur avec velocity_x et velocity_y 
        self.image = Player.pl # Charge l'image du joueur
        self.rect = self.image.get_rect()  # Obtient le rectangle englobant de l'image pour la gestion des collisions
        self.rect.topleft = self.position # Place le coin supérieur gauche du rectangle à la position initiale

    def update(self):
        # Met à jour la position en ajoutant la vélocité actuelle
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] < -30: # Vérifie si la position x est en dehors des limites à gauche
            self.position[0] = -30
        elif self.position[0] + self.rect.width > largeur +20: # Vérifie si la position x est en dehors des limites à droite
            self.position[0] = largeur - self.rect.width
        elif self.position[1] + self.rect.height < 50: # Vérifie si la position y est en dehors des limites en haut
            self.position[1] = 50 - self.rect.height
        elif self.position[1] + self.rect.height > hauteur: # Vérifie si la position y est en dehors des limites en bas
            self.position[1] = hauteur - self.rect.height
        
        self.rect.topleft = self.position # Met à jour la position du rectangle englobant

    def draw(self, surface): # Dessine l'image du joueur sur la surface donnée à la position actuelle du rectangle englobant
       surface.blit(self.image, self.rect.topleft)

    def move_left(self): # Déplace le joueur vers la gauche en définissant la vélocité x à -1 et y à 0
        self.velocity[0] = -3
        self.velocity[1] = 0
    def move_right(self): # Déplace le joueur vers la droite en définissant la vélocité x à 1 et y à 0
        self.velocity[0] = 3
        self.velocity[1] = 0
    def move_up(self): # Déplace le joueur vers le haut en définissant la vélocité y à -1 et x à 0
        self.velocity[1] = -3
        self.velocity[0] = 0
    def move_down(self): # Dplace le joueur vers le bas en définissant la vélocité y à 1 et x à 0
        self.velocity[1] = 3
        self.velocity[0] = 0
    def stop(self): # Arrête le mouvement du joueur en définissant les vélocités x et y à 0
        self.velocity[0] = 0
        self.velocity[1] = 0
