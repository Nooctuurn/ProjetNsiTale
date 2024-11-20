import pygame

class Bot:
    def __init__(self, nom, pv, porter, degat, image_path):
        self.nom = nom
        self.pv = pv
        self.porter = porter
        self.degat = degat
        self.image = pygame.image.load(image_path).convert_alpha()  # Chargement de l'image

pygame.init()

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Affichage du Bot")

bot_de_pierre = Bot("Bot de pierre", 100, 50, 10, 'img/Bot.png')

x_bot, y_bot = 300, 200  # Coordonnées pour dessiner le bot

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    fenetre.fill((255, 255, 255))
    fenetre.blit(bot_de_pierre.image, (x_bot, y_bot))

    pygame.display.flip()
    clock.tick(60)
