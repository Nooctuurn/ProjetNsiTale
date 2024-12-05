import pygame

class Bot:
    def __init__(self, nom, pv, porter, degat, image_path):
        self.nom = nom # le nom du mob 
        self.pv = pv # les pv du mob
        self.porter = porter # la porter des coups du mob
        self.degat = degat # les degats qu'inflige le mob
        self.image = pygame.image.load(image_path).convert_alpha()  # charger l'image
        self.width, self.height = self.image.get_size() # recuperer la taille de l'image
        self.image = pygame.transform.scale(self.image, (self.width // 2, self.height // 2))  # redimensionnement l'imagge car elle est beaucoup trop grande
        self.width //= 2 # on met a jour la redimension de l'image pour l'utiliser plus tard (largeur)
        self.height //= 2 # on met a jour la redimension de l'image pour l'utiliser plus tard (longueur)

pygame.init()
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Affichage du Bot")

# initialisation du mob
bot_de_pierre = Bot("Bot de pierre", 100, 50, 10, 'img/Bot.png')

# Coordonnées pour dessiner le mob
x_bot, y_bot = 500, 200  # position de départ
dx = -1  # Direction initiale

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mise à jour des coordonnées pour le mouvement
    x_bot += dx

    if x_bot <= 300:  # si le bot atteint la position 300 il repart vers la droite
        dx = 1
    elif x_bot >= 500:  # Si le bot atteint la position 500 il repart vers la gauche
        dx = -1

    fenetre.fill((255, 255, 255))  # fond blanc
    
    # Dessiner un carré rouge autour de l'image pour gerer la porté des attaques
    rect = pygame.Rect(x_bot, y_bot, bot_de_pierre.width, bot_de_pierre.height)  # creer un rectangle autour de l'image
    pygame.draw.rect(fenetre, (255, 0, 0), rect, 2)  # Rectangle rouge autour de l'image avec une bordure de 2 pixels

    # Dessiner le bot
    fenetre.blit(bot_de_pierre.image, (x_bot, y_bot))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
