import pygame
import sys
from pygame.locals import*
from random import randint

pygame.init()
largeur, hauteur = 1200, 600

sprite_sheet_RUN = pygame.image.load("Sprite\Knight 2D Pixel Art\Sprites\with_outline\RUN.png")
sprite_sheet_IDLE = pygame.image.load("Sprite\Knight 2D Pixel Art\Sprites\with_outline\IDLE.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.position = [x, y]
        self.velocity = [velocity_x, velocity_y]
        self.IDLE_frame = self.extract_frames(sprite_sheet_IDLE, 7)
        self.RUN_frame = self.extract_frames(sprite_sheet_RUN, 8)
        self.image = self.IDLE_frame[0]  # Définit l'image à la première frame de l'animation idle
        self.rect = self.image.get_rect()  # Le rectangle basé sur la première image
        self.rect.topleft = self.position
        self.animation_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.mouvement = "idle"

    def extract_frames(self, spritesheet, num_frames):
        frame_width = spritesheet.get_width() // num_frames
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(num_frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (200, 200))
            frames.append(frame)
        return frames

    def update(self):
        # Met à jour la position en ajoutant la vélocité actuelle
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] < -30:  # Vérifie si la position x est en dehors des limites à gauche
            self.position[0] = -30
        elif self.position[0] + self.rect.width > largeur + 20:  # Vérifie si la position x est en dehors des limites à droite
            self.position[0] = largeur - self.rect.width
        elif self.position[1] + self.rect.height < 50:  # Vérifie si la position y est en dehors des limites en haut
            self.position[1] = 50 - self.rect.height
        elif self.position[1] + self.rect.height > hauteur:  # Vérifie si la position y est en dehors des limites en bas
            self.position[1] = hauteur - self.rect.height

        self.rect.topleft = self.position  # Met à jour la position du rectangle englobant

        if self.mouvement == "run":
            # Animation de la course (changer de frame toutes les 100ms)
            if pygame.time.get_ticks() - self.last_update_time > 100:
                self.animation_frame += 1
                if self.animation_frame >= len(self.RUN_frame):  # Réinitialise à la première frame après la dernière
                    self.animation_frame = 0
                self.image = self.RUN_frame[self.animation_frame]  # Choisit la frame suivante
                self.last_update_time = pygame.time.get_ticks()
        
        if self.mouvement == "idle":
            # Animation de la pose (changer de frame toutes les 100ms)
            if pygame.time.get_ticks() - self.last_update_time > 100:
                self.animation_frame += 1
                if self.animation_frame >= len(self.IDLE_frame):  # Réinitialise à la première frame après la dernière
                    self.animation_frame = 0
                self.image = self.IDLE_frame[self.animation_frame]  # Choisit la frame suivante
                self.last_update_time = pygame.time.get_ticks()

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)  # Dessine l'image sur la surface

    def move_left(self):
        self.velocity[0] = -3
        self.velocity[1] = 0
        self.image = self.RUN_frame[0]  # Affiche la première frame de l'animation de course
        self.mouvement = 'run'

    def move_right(self):
        self.velocity[0] = 3
        self.velocity[1] = 0
        self.image = self.RUN_frame[0]  # Affiche la première frame de l'animation de course
        self.mouvement = 'run'

    def move_up(self):
        self.velocity[1] = -3
        self.velocity[0] = 0

    def move_down(self):
        self.velocity[1] = 3
        self.velocity[0] = 0

    def stop(self):
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.image = self.IDLE_frame[0]  # Affiche la première frame de l'animation idle
        self.mouvement = 'idle'

