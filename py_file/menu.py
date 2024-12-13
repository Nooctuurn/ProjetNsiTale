import pygame
pygame.init()

largeur, hauteur = 1200, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Smash Banana - Menu Principal")

BLEU_FONCE = (33,36,60)
OR_OMBRE = (194,36,31)
OR = (255, 236, 66)
BLEU_CLAIR = (15,171,183)

fond = pygame.image.load("img/ecran_menu.png")
fond = pygame.transform.scale(fond, (largeur, hauteur))

police_titre = pygame.font.Font(None, 80)
police_boutons = pygame.font.Font(None, 50)

texte_titre = police_titre.render("Titre", True, BLEU_CLAIR)
titre_rect = texte_titre.get_rect(center=(largeur // 2, hauteur // 4))

bouton_largeur, bouton_hauteur = 300, 60
espacement = 20

x_bouton = (largeur - bouton_largeur) // 8
y_bouton = hauteur // 2
marge = 5

boutons = { 
    # Couleur du dessus des boutons : #ffec42
    # Couleur du dessous des boutons : #c2241f
    # Couleur de l'interieur : #21243c
    # Couleur texte : #0fabb7
    "Solo": pygame.Rect(x_bouton, y_bouton-70, bouton_largeur, bouton_hauteur),
    "Multijoueur en local": pygame.Rect(x_bouton, y_bouton-70+ bouton_hauteur + espacement+ marge, bouton_largeur, bouton_hauteur),
    "Paramètres": pygame.Rect(x_bouton*7, y_bouton , bouton_largeur, bouton_hauteur),
}

# Fonction pour afficher les boutons et le texte dessus
def dessiner_bouton(surface, rect, texte, couleur_fond,couleur_marge, couleur_texte):
    pygame.draw.rect(surface,couleur_marge,rect)
    pygame.draw.rect(surface, couleur_fond, rect)
    texte_surface = police_boutons.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=rect.center)
    surface.blit(texte_surface, texte_rect)
