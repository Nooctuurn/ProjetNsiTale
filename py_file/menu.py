import pygame
import sys
import subprocess  

# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1200, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Smash Banana - Menu Principal")

icon = pygame.image.load('img/iconne.webp')
pygame.display.set_icon(icon)

# Couleurs
BLANC = (255, 255, 255)
GRIS = (169, 169, 169)

# Charger l'image de fond
fond = pygame.image.load("img/fond.jpeg")
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Police
police_titre = pygame.font.Font(None, 80)
police_boutons = pygame.font.Font(None, 50)

# Texte central
texte_titre = police_titre.render("Mettre Logo Ici", True, BLANC)
titre_rect = texte_titre.get_rect(center=(largeur // 2, hauteur // 4))

# Définir les boutons
bouton_largeur, bouton_hauteur = 300, 60
espacement = 20

# Calculer les positions des boutons
x_bouton = (largeur - bouton_largeur) // 2
y_bouton = hauteur // 2

# Créer les rectangles pour les boutons
boutons = {
    "Solo": pygame.Rect(x_bouton, y_bouton, bouton_largeur, bouton_hauteur),
    "Multijoueur en local": pygame.Rect(x_bouton, y_bouton + bouton_hauteur + espacement, bouton_largeur, bouton_hauteur),
    "Paramètres": pygame.Rect(x_bouton, y_bouton + 2 * (bouton_hauteur + espacement), bouton_largeur, bouton_hauteur),
}

# Fonction pour afficher le texte sur les boutons
def dessiner_bouton(surface, rect, texte, couleur_fond, couleur_texte):
    pygame.draw.rect(surface, couleur_fond, rect)
    texte_surface = police_boutons.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect(center=rect.center)
    surface.blit(texte_surface, texte_rect)

# Lancer le fichier game.py
def lancer_jeu(script_name):
    pygame.quit()  # Ferme la fenêtre pygame
    subprocess.run(["python", script_name])  # Lance le fichier de jeu
    sys.exit()  # Quitte le programme après avoir choisi un mode de jeu

# Boucle principale
def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
                for nom, rect in boutons.items():
                    if rect.collidepoint(event.pos):
                        if nom == "Solo":
                            lancer_jeu("py_file/game.py")  # Lance les modes de jeu / paramètres
                        elif nom == "Multijoueur en local":
                            lancer_jeu("multiplayer_game.py")  
                        elif nom == "Paramètres":
                            print("Ouvrir les paramètres")
                            

        # Affichage du fond
        fenetre.blit(fond, (0, 0))

        # Afficher le texte central
        fenetre.blit(texte_titre, titre_rect)

        # Afficher les boutons
        for nom, rect in boutons.items():
            dessiner_bouton(fenetre, rect, nom, GRIS, BLANC)

        # Mettre à jour l'affichage
        pygame.display.flip()

# Lancer le menu
menu()
