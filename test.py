import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation de Gravité")

# Couleurs
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Définir un objet (une balle)
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_y = 0  # Vitesse verticale initiale

# Gravité
gravity = 0.5  # Force de gravité
bounce = -0.7  # Coefficient de rebond

# Horloge pour contrôler la fréquence d'images
clock = pygame.time.Clock()

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Appliquer la gravité
    ball_speed_y += gravity
    ball_y += ball_speed_y

    # Détecter le sol (et rebondir)
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_speed_y *= bounce  # Rebondir avec une perte d'énergie

    # Dessiner tout
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (ball_x, int(ball_y)), ball_radius)

    # Rafraîchir l'écran
    pygame.display.flip()
    clock.tick(60)  # Limiter à 60 FPS
