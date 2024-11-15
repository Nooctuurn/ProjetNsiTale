import pygame
from random import *
import math

class Bot:
    def __init__(self, nom, pv, porter, degat):
        self.nom = nom
        self.pv = pv
        self.porter = porter
        self.degat = degat

    def attaque(self, cible):
        cible.pv -= self.degat  # Réduit les points de vie de la cible
        return f"{self.nom} attaque {cible.nom} et inflige {self.degat} points de dégâts. {cible.nom} a maintenant {cible.pv} PV."

# Création des bots
Bot_de_pierre = Bot("Bot de pierre", 100, 50, 10)
joueur = Bot("joueur", 50, 30, 20)

# Appel de la méthode attaque et affichage du résultat
while Bot_de_pierre.pv >= 0 or cible.pv >= 0:
    if Bot_de_pierre.pv >= 0:
        print(Bot_de_pierre.attaque(joueur))
    else:
        print("joueur a perdu")
        break

    if joueur.pv >= 0:
        print(joueur.attaque(Bot_de_pierre))
    else:
        print("joueur a perdu")
        break

qqqqqqqqqqqqqqqqqqqqqqqq