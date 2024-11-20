import pygame
import sys
import math
from game import*


player_velocity = 5.00
class Player(pygame.sprite.Sprite):
    player = pygame.image.load('img/perso.png')
    player = pygame.transform.scale(player, (80, 60))

    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = [x, y]
        self.velocity = [velocity_x, velocity_y]
        self.image = Player.player
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.last_shot_time = 0
        self.last_spawn_time = 0
        self.last_spawn1_time = 0
        self.last_spawn2_time = 0
        self.mob_velocity = -4.000
        self.frequence = 550

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] + self.rect.width > 900:
            self.position[0] = 900 - self.rect.width
        elif self.position[1] + self.rect.height < 320:
            self.position[1] = 320 - self.rect.height
        elif self.position[1] + self.rect.height > 410:
            self.position[1] = 410 - self.rect.height
        
        self.rect.topleft = self.position 

    def draw(self, surface):
       surface.blit(self.image, self.rect.topleft)

    def move_left(self):
        self.velocity[0] = -1
        self.velocity[1] = 0
    def move_right(self):
        self.velocity[0] = 1
        self.velocity[1] = 0
    def move_up(self):
        self.velocity[1] = -1
        self.velocity[0] = 0
    def move_down(self):
        self.velocity[1] = 1
        self.velocity[0] = 0
    def stop(self):
        self.velocity[0] = 0
        self.velocity[1] = 0
