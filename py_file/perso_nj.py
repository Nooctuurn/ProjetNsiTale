import pygame
import math
import random

# Chargement des sprites
sprite_sheet_IDLE = pygame.image.load("Sprite/demon/IDLE.png")
sprite_sheet_ATTACK = pygame.image.load("Sprite/demon/ATTACK.png")



class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed=7):
        super().__init__()
        self.image = pygame.image.load("Sprite/demon/projectile.png")
        self.image = pygame.transform.scale(self.image, (30, 20))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right < 0 or self.rect.left > 1200:
            self.kill()


class Bot(pygame.sprite.Sprite):
    def __init__(self, nom, pv, defense, x, y, speed):
        super().__init__()
        self.nom = nom
        self.pv = pv
        self.defense = defense
        self.position = [x, y]
        self.velocity = [0, 0]
        self.IDLE_frame = self.extract_frames(sprite_sheet_IDLE, 4)
        self.ATTACK_frame = self.extract_frames(sprite_sheet_ATTACK, 8)
        self.image = self.IDLE_frame[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position
        self.animation_frame = 0
        self.last_update_time = pygame.time.get_ticks()
        self.mouvement = "idle"
        self.cote = ""
        self.speed = speed
        self.attack_cooldown = 3000
        self.last_attack_time = 0
        self.direction_bot = -1
        self.projectiles = pygame.sprite.Group()

    def prend_des_degat(self, degats):
        degats_effectifs = degats - self.defense
        self.pv -= degats_effectifs
        print(f"{self.nom} a pris {degats_effectifs} dégâts. PV restants : {self.pv}.")
        self.velocity[0] = 0

    def extract_frames(self, spritesheet, num_frames):
        frame_width = spritesheet.get_width() // num_frames
        frame_height = spritesheet.get_height()
        frames = []
        for i in range(num_frames):
            frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (82, 82))
            frames.append(frame)
        return frames

    def update(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.velocity[0] > 0:
            self.cote = "gauche"
        elif self.velocity[0] < 0:
            self.cote = "droite"

        self.rect.topleft = self.position

        now = pygame.time.get_ticks()

        if self.mouvement == "idle" and now - self.last_update_time > 100:
            self.animation_frame = (self.animation_frame + 1) % len(self.IDLE_frame)
            frame = self.IDLE_frame[self.animation_frame]
            self.image = pygame.transform.flip(frame, True, False) if self.cote == "gauche" else frame
            self.last_update_time = now

        if self.mouvement == "ATTACK" and now - self.last_update_time > 100:
            self.animation_frame += 1

            if self.animation_frame == 4:
                direction = -1 if self.cote == "droite" else 1
                proj = Projectile(self.rect.centerx, self.rect.centery, direction)
                self.projectiles.add(proj)

            if self.animation_frame >= len(self.ATTACK_frame):
                self.animation_frame = 0
                self.mouvement = "idle"

            frame = self.ATTACK_frame[self.animation_frame]
            self.image = pygame.transform.flip(frame, True, False) if self.cote == "gauche" else frame
            self.last_update_time = now


        self.projectiles.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.get_attack_zone(), 2)
        self.projectiles.draw(surface)

    def move_left(self):
        self.velocity = [-self.speed, 0]
        self.cote = "gauche"

    def move_right(self):
        self.velocity = [self.speed, 0]
        self.cote = "droite"

    def stop(self):
        self.velocity = [0, 0]
        self.mouvement = "idle"

    def get_attack_zone(self):
        zone_size = self.rect.width * 3
        return pygame.Rect(
            self.rect.centerx - zone_size // 2,
            self.rect.centery - zone_size // 2,
            zone_size,
            zone_size
        )

    def player_in_zone(self, player_rect):
        if self.get_attack_zone().colliderect(player_rect):
            self.attaque()

    def behavior(self, player_rect, left_limit, right_limit):
        current_time = pygame.time.get_ticks()

        if self.get_attack_zone().colliderect(player_rect):
            if self.mouvement == "idle" and current_time - self.last_attack_time >= self.attack_cooldown:
                self.attaque()
        else:
            self.velocity[0] = self.direction_bot * self.speed
            self.position[0] += self.velocity[0]

            if self.position[0] <= left_limit:
                self.direction_bot = 1
            elif self.position[0] >= right_limit:
                self.direction_bot = -1

            self.rect.topleft = self.position

    def attaque(self):
        current_time = pygame.time.get_ticks()
        if self.mouvement != "ATTACK" and current_time - self.last_attack_time >= self.attack_cooldown:
            print(f"{self.nom} attaque !")
            self.mouvement = "ATTACK"
            self.animation_frame = 0
            self.last_update_time = current_time
            self.last_attack_time = current_time
            self.velocity = [0, 0]
