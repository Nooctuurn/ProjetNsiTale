import pygame

class Menu:
    def __init__(self, ecran, largeur, hauteur):
        self.ecran = ecran
        self.largeur = largeur
        self.hauteur = hauteur

        # Charger l'image de fond du menu
        self.bg_menu = pygame.image.load('img/fondacceuiljouer.png').convert()
        self.bg_menu = pygame.transform.scale(self.bg_menu, (self.largeur, self.hauteur))

        # Définition du bouton "Jouer"
        self.button_color = (0, 200, 0)
        self.button_hover_color = (0, 255, 0)  # Vert clair au survol
        self.button_rect = pygame.Rect(self.largeur // 2 - 100, 300, 200, 60)
        self.button_text = pygame.font.Font(None, 40).render("Jouer", True, (255, 255, 255))

    def draw(self):
        """Affiche le menu avec un bouton Jouer."""
        self.ecran.blit(self.bg_menu, (0, 0))

        # Récupérer la position de la souris
        mouse_pos = pygame.mouse.get_pos()

        # Vérifier si la souris est sur le bouton pour changer sa couleur
        button_color = self.button_hover_color if self.button_rect.collidepoint(mouse_pos) else self.button_color

        pygame.draw.rect(self.ecran, button_color, self.button_rect, border_radius=15)
        self.ecran.blit(self.button_text, (self.button_rect.x + 60, self.button_rect.y + 15))

    def handle_click(self, event, game):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.button_rect.collidepoint(event.pos):
                game.is_playing = True
