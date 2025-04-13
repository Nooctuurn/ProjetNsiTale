from game import*
from player import*
from menu import*
import pygame
from game import Game
from menu import Menu
import pygame



pygame.init()


if __name__ == "__main__":
    # Définir les dimensions de la fenêtre
    largeur = 1200
    hauteur = 600

    # Créer la surface d'affichage
    ecran = pygame.display.set_mode((largeur, hauteur))

    # Créer une instance de Game
    game = Game(ecran, largeur, hauteur)

    # Créer une instance de Menu et passer l'instance de Game
    menu = Menu(ecran, largeur, hauteur, game)

    # Exécuter la boucle du menu
    menu.run()

    pygame.quit()