import pygame
import sys
import math
from game import*


player_velocity = 5.00
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/perso.png')
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect
        self.velocity = player_velocity
    
    def update(self):
        self.rect.x += self.velocity
        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > largeur or self.rect.y > hauteur:
            self.kill()