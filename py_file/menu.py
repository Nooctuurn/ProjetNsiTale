import pygame

class Menu:
    def __init__(self, ecran, largeur, hauteur):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur
        self.in_accueil_2 = False 

        # Charger les images des deux écrans d'accueil
        self.bg_menu = pygame.image.load('img/fondacceuil1.png').convert()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (self.largeur, self.hauteur))

        self.bg_accueil_2 = pygame.image.load('img/fond.jpeg').convert()  # Image du deuxième accueil
        self.bg_accueil_2 = pygame.transform.scale(self.bg_accueil_2, (self.largeur, self.hauteur))

        # Charger le bouton "Jouer"
        self.bouton_jouer = pygame.image.load('img/boutonjouer.png').convert_alpha()
        self.bouton_jouer = pygame.transform.scale(self.bouton_jouer, (150, 100))

        # Définir la position du bouton Jouer
        self.bouton_x = (self.largeur - self.bouton_jouer.get_width()) // 2
        self.bouton_y = (self.hauteur - self.bouton_jouer.get_height()) // 1.2
        self.bouton_rect = pygame.Rect(self.bouton_x, self.bouton_y, self.bouton_jouer.get_width(), self.bouton_jouer.get_height())

    def draw(self):
        """Affiche le menu ou le deuxième écran d'accueil."""
        if self.in_accueil_2:
            self.ecran.blit(self.bg_accueil_2, (0, 0))  # Afficher le deuxième accueil
        else:
            self.ecran.blit(self.bg_menu, (0, 0))  # Afficher le premier accueil
            self.ecran.blit(self.bouton_jouer, (self.bouton_x, self.bouton_y))  # Afficher le bouton jouer

    def handle_event(self, event):
        """Gère les événements du menu."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.in_accueil_2 and self.bouton_rect.collidepoint(event.pos):
                self.in_accueil_2 = True  # Passe au deuxième écran d'accueil
