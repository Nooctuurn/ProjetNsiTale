import pygame
pygame.init()

largeur, hauteur = 1200, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Smash Banana - Menu Principal")

BLANC = (255, 255, 255)
GRIS = (169, 169, 169)

fond = pygame.image.load("img/fond.jpeg")
fond = pygame.transform.scale(fond, (largeur, hauteur))

police_titre = pygame.font.Font(None, 80)
police_boutons = pygame.font.Font(None, 50)

texte_titre = police_titre.render("Titre", True, BLANC)
titre_rect = texte_titre.get_rect(center=(largeur // 2, hauteur // 4))

bouton_largeur, bouton_hauteur = 300, 60
espacement = 20

x_bouton = (largeur - bouton_largeur) // 2
y_bouton = hauteur // 2

boutons = {
    "Solo": pygame.Rect(x_bouton, y_bouton, bouton_largeur, bouton_hauteur),
    "Multijoueur en local": pygame.Rect(x_bouton, y_bouton + bouton_hauteur + espacement, bouton_largeur, bouton_hauteur),
    "Paramètres": pygame.Rect(x_bouton, y_bouton + 2 * (bouton_hauteur + espacement), bouton_largeur, bouton_hauteur),
}

# Fonction pour afficher les boutons et le texte dessus
def dessiner_bouton(surface, rect, texte, couleur_fond, couleur_texte):
    pygame.draw.rect(surface, couleur_fond, rect)
    texte_surface = police_boutons.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=rect.center)
    surface.blit(texte_surface, texte_rect)
