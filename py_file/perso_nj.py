import pygame
import sys
from pygame.locals import *

pygame.init()
largeur, hauteur = 1200, 600

sprite_sheet_IDLE = pygame.image.load("Sprite\Flying Demon 2D Pixel Art\Sprites\with_outline\IDLE.png")
sprite_sheet_ATTACK = pygame.image.load("Sprite\Flying Demon 2D Pixel Art\Sprites\with_outline\ATTACK.png")
sprite_sheet_DEATH = pygame.image.load("Sprite\Flying Demon 2D Pixel Art\Sprites\with_outline\DEATH.png")

class Bot(pygame.sprite.Sprite):
    def __init__(self, nom, pv, defense, image_path ,x, y, velocity_x, velocity_y, speed):
        self.nom = nom # Le nom du bot
        self.pv = pv # Les points de vie du bot
        self.defense = defense
        self.image = pygame.image.load(image_path).convert_alpha() # Charger l'image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.width, self.height = self.image.get_size()  # Dimensions après redimensionnement
        super().__init__()
        self.position = [x, y]
        self.velocity = [velocity_x, velocity_y]
        self.IDLE_frame = self.extract_frames(sprite_sheet_IDLE, 4)
        self.ATTACK_frame = self.extract_frames(sprite_sheet_ATTACK, 8)
        self.DEATH_frame = self.extract_frames(sprite_sheet_DEATH, 7)
        self.image = self.IDLE_frame[0]  # Définit l'image à la première frame de l'animation idle
        self.rect = self.image.get_rect()  # Le rectangle basé sur la première image
        self.rect.topleft = self.position
        self.animation_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.mouvement = "idle"
        self.cote = "gauche"
        self.speed = speed

    def prend_des_degat(self, degats):
        degats_effectifs = degats - self.defense  # Applique la défense
        self.pv -= degats_effectifs
        print(f"{self.nom} a pris {degats_effectifs} dégâts. PV restants : {self.pv}.")
        self.velocity[0] = 0  # Arrêter le mouvement immédiatement après avoir pris des dégâts


    def extract_frames(self, spritesheet, num_frames):
        frame_width = spritesheet.get_width() // num_frames
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(num_frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            # Redimensionne chaque frame
            frame = pygame.transform.scale(frame, (frame_width * 2, frame_height * 2))
            frames.append(frame)
        return frames

    def update(self):
        # Met à jour la position en ajoutant la vélocité actuelle
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Vérifie si le bot change de direction
        if self.velocity[0] > 0:
            self.cote = "gauche"
        elif self.velocity[0] < 0:
            self.cote = "droite"

        self.rect.topleft = self.position  # Met à jour la position du rectangle englobant

        # Animation et orientation
        if self.mouvement == "idle" and pygame.time.get_ticks() - self.last_update_time > 100:
            self.animation_frame += 1
            if self.animation_frame >= len(self.IDLE_frame):
                self.animation_frame = 0
            current_frame = self.IDLE_frame[self.animation_frame]
            self.image = pygame.transform.flip(current_frame, True, False) if self.cote == "gauche" else current_frame
            self.last_update_time = pygame.time.get_ticks()

        if self.mouvement == "ATTACK" and pygame.time.get_ticks() - self.last_update_time > 100:
            self.animation_frame += 1
            if self.animation_frame >= len(self.ATTACK_frame):
                self.animation_frame = 0
                self.mouvement = 'idle'  # Retour à l'état idle après l'attaque
            current_frame = self.ATTACK_frame[self.animation_frame]
            self.image = pygame.transform.flip(current_frame, True, False) if self.cote == "gauche" else current_frame
            self.last_update_time = pygame.time.get_ticks()


    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)  # Dessine l'image sur la surface

    def move_left(self):
        self.velocity[0] = -self.speed
        self.velocity[1] = 0
        self.cote = "gauche"

    def move_right(self):
        self.velocity[0] = self.speed
        self.velocity[1] = 0
        self.cote = "droite"

    def stop(self):
        # Stoppe le mouvement et ajuste l'état
        self.velocity[0] = 0
        self.velocity[1] = 0
        self.mouvement = 'idle'

    def attaque(self):
        self.velocity[0] = 0
        self.velocity[1] = 0
        if self.mouvement != 'ATTACK':  # Ne passe en attaque que si ce n'est pas déjà le cas
            print(f"{self.nom} attaque !")  # Debug
            self.mouvement = 'ATTACK'
            self.animation_frame = 0
            self.last_update_time = pygame.time.get_ticks()
