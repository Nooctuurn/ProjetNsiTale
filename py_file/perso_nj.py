import pygame

class Bot:
    def __init__(self, nom, pv, attaque, defense, image_path):
        self.nom = nom # Le nom du bot
        self.pv = pv # Les points de vie du bot
        self.attaque = attaque
        self.defense = defense
        self.image = pygame.image.load(image_path).convert_alpha() # Charger l'image
        self.width, self.height = self.image.get_size()  # Dimensions basées sur l'image

    def prend_des_degat(self, degats):
        degats_effectifs = 10 - self.defense  # Applique la défense
        self.pv -= degats_effectifs
        print(f"{self.nom} a pris {degats_effectifs} dégâts. PV restants : {self.pv}.")
        return self.pv <= 0  # Retourne True si le bot n'a plus de PV
