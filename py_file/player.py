import pygame
import sys
from pygame.locals import*
from random import randint
from PIL import Image

pygame.init()
largeur, hauteur = 1200, 600

sprite_sheet_RUN = pygame.image.load("Sprite/Knight 2D Pixel Art/Sprites/with_outline/RUN.png")
sprite_sheet_IDLE = pygame.image.load("Sprite/Knight 2D Pixel Art/Sprites/with_outline/IDLE.png")

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, speed):
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
        self.cote = "droite"
        self.speed = speed

    def extract_frames(self, spritesheet, num_frames):
        frame_width = spritesheet.get_width() // num_frames
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(num_frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (300, 300))
            frames.append(frame)
        return frames

    def update(self):
        # Met à jour la position en ajoutant la vélocité actuelle
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] < -100:  # Vérifie si la position x est en dehors des limites à gauche
            self.position[0] = -100
        elif self.position[0] + self.rect.width > largeur + 100:  # Vérifie si la position x est en dehors des limites à droite
            self.position[0] = largeur + 100 - self.rect.width
        elif self.position[1] + self.rect.height < 200:  # Vérifie si la position y est en dehors des limites en haut
            self.position[1] = 200 - self.rect.height
        elif self.position[1] + self.rect.height > hauteur + 35:  # Vérifie si la position y est en dehors des limites en bas
            self.position[1] = hauteur + 35 - self.rect.height

        self.rect.topleft = self.position  # Met à jour la position du rectangle englobant

        if self.mouvement == 'run':
            if self.cote == "droite":
                # Animation de la course (changer de frame toutes les 100ms)
                if pygame.time.get_ticks() - self.last_update_time > 100:
                    self.animation_frame += 1
                    if self.animation_frame >= len(self.RUN_frame):  # Réinitialise à la première frame après la dernière
                        self.animation_frame = 0
                    self.image = self.RUN_frame[self.animation_frame]  # Choisit la frame suivante
                    self.last_update_time = pygame.time.get_ticks()

            elif self.cote == "gauche":
                # Animation de la course (changer de frame toutes les 100ms)
                if pygame.time.get_ticks() - self.last_update_time > 100:
                    self.animation_frame += 1
                    if self.animation_frame >= len(self.RUN_frame):  # Réinitialise à la première frame après la dernière
                        self.animation_frame = 0
                    current_frame = self.RUN_frame[self.animation_frame]
                    self.image = pygame.transform.flip(current_frame, True, False)
                    self.last_update_time = pygame.time.get_ticks()
        
        if self.mouvement == "idle":
            if self.cote == "droite":
                if pygame.time.get_ticks() - self.last_update_time > 100:
                    self.animation_frame += 1
                    if self.animation_frame >= len(self.IDLE_frame):
                        self.animation_frame = 0
                    self.image = self.IDLE_frame[self.animation_frame]
                    self.last_update_time = pygame.time.get_ticks()

            elif self.cote == "gauche":
                if pygame.time.get_ticks() - self.last_update_time > 100:
                    self.animation_frame += 1
                    if self.animation_frame >= len(self.IDLE_frame):
                        self.animation_frame = 0
                    current_frame = self.IDLE_frame[self.animation_frame]
                    self.image = pygame.transform.flip(current_frame, True, False)
                    self.last_update_time = pygame.time.get_ticks()
    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)  # Dessine l'image sur la surface

    def move_left(self):
        self.velocity[0] = -self.speed
        self.velocity[1] = 0
        self.cote = "gauche"
        self.mouvement = 'run'

    def move_right(self):
        self.velocity[0] = self.speed
        self.velocity[1] = 0
        self.cote = "droite"
        self.mouvement = 'run'
 
    def move_up(self):
        self.velocity[1] = -self.speed
        self.velocity[0] = 0

    def move_down(self):
        self.velocity[1] = self.speed
        self.velocity[0] = 0

    def stop(self):
        # Stoppe le mouvement et ajuste l'état
        self.velocity[0] = 0
        self.velocity[1] = 0
        if self.cote == "droite":
            self.image = self.IDLE_frame[0]  # Affiche la première frame de l'animation idle
        else:
            self.image = pygame.transform.flip(self.IDLE_frame[0], True, False)  # Flipping de l'image
        self.mouvement = 'idle'

